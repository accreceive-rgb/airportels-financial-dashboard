"""
ระบบตรวจสอบยอดโอนจ่าย Rider
เปรียบเทียบรายการเบิก (PR) กับสลิปโอนจ่าย
"""

import sys
import os
import re
import json
from pathlib import Path
from datetime import datetime

# ---- ข้อมูลจาก PR (parttime 07.05.2026.pdf) ----
# สกัดข้อมูลจาก PDF รายการเบิกด้วย pdfplumber

def extract_pr_data(pdf_path: str) -> list[dict]:
    """สกัดข้อมูลจาก Payment Requisition PDF"""
    try:
        import pdfplumber
    except ImportError:
        print("กรุณาติดตั้ง: pip install pdfplumber")
        sys.exit(1)

    entries = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    if not row or len(row) < 4:
                        continue
                    # หาแถวที่มีหมายเลข (รายการ)
                    cell0 = str(row[0]).strip() if row[0] else ""
                    if not cell0.isdigit():
                        continue
                    no = int(cell0)
                    # ชื่อไรเดอร์/รายการ
                    name = ""
                    for cell in row[3:6]:
                        if cell and str(cell).strip():
                            name = str(cell).strip()
                            break
                    # ยอดเงิน (Total Amount คอลัมน์สุดท้าย)
                    total_str = ""
                    for cell in reversed(row):
                        if cell and str(cell).strip():
                            total_str = str(cell).strip()
                            break
                    try:
                        total = float(total_str.replace(",", ""))
                    except ValueError:
                        total = 0.0

                    entries.append({
                        "no": no,
                        "name": name,
                        "amount": total,
                        "raw": row
                    })
    return entries


# ---- ข้อมูล PR แบบ hardcode (จากที่อ่านไว้แล้ว) ----
PR_DATA = [
    {"no": 1,  "name": "จิรวัฒน์ วงษ์วรรณ (สำรอง) / Por ช่วยงานอาหารคลีน", "amount": 550.00,   "wht": 0.00,   "type": "part-time"},
    {"no": 2,  "name": "จิรวัฒน์ วงษ์วรรณ (สำรอง) / Por ช่วยงานอาหารคลีน", "amount": 550.00,   "wht": 0.00,   "type": "part-time"},
    {"no": 3,  "name": "Bat-HKT PN (ค่าส่งกระเป๋ากอล์ฟ 1 ใบ)",              "amount": 704.00,   "wht": 0.00,   "type": "delivery"},
    {"no": 4,  "name": "วัชระ เกตุสำเภา DS (ยกเลิก OD ค่าเสียเวลา)",        "amount": 100.00,   "wht": 0.00,   "type": "other"},
    {"no": 5,  "name": "Bat-HKT DS (คาร์โก้ภูเก็ต)",                         "amount": 800.00,   "wht": 0.00,   "type": "delivery"},
    {"no": 6,  "name": "Bat-HKT PN (Deep Andaman Queen--Grand Mercure--HKT)", "amount": 1358.00,  "wht": 42.00,  "type": "delivery"},
    {"no": 7,  "name": "Narit ภูเก็ต PN (HKT DOME--Little Nyonya Hotel)",    "amount": 600.00,   "wht": 0.00,   "type": "delivery"},
    {"no": 8,  "name": "ธรณินทร์ เจนวัธัญูกิจ / โย หัวหิน",                 "amount": 3249.50,  "wht": 100.50, "type": "part-time"},
    {"no": 9,  "name": "ธรณินทร์ เจนวัธัญูกิจ / โย หัวหิน / เบิ้ม อนุชา",  "amount": 1891.50,  "wht": 58.50,  "type": "part-time"},
    {"no": 10, "name": "อุ่นใจ โตนะโพธิ์ / Part-Time",                       "amount": 1028.20,  "wht": 31.80,  "type": "part-time"},
    {"no": 11, "name": "ธนภูมิ ไตรสมพร / Part-Time",                         "amount": 800.00,   "wht": 0.00,   "type": "part-time"},
    {"no": 12, "name": "บรรณลือศักดิ์ โมราสุทธิ์ / Part-Time",              "amount": 1571.40,  "wht": 48.60,  "type": "part-time"},
    {"no": 13, "name": "วีรวัลย์ อยู่ดิษฐ / Part-Time",                     "amount": 2492.90,  "wht": 77.10,  "type": "part-time"},
    {"no": 14, "name": "ดำรงศักดิ์ ศรีเดช / Part-Time",                      "amount": 1571.40,  "wht": 48.60,  "type": "part-time"},
    {"no": 15, "name": "ไพโรจน์ กุณารักษ์ / Prairot Taxi",                   "amount": 1193.10,  "wht": 36.90,  "type": "taxi"},
    {"no": 16, "name": "ภัทรพงศ์ ตันหยง / Part-Time",                        "amount": 1571.40,  "wht": 48.60,  "type": "part-time"},
    {"no": 17, "name": "สกล จ้างตระกูล / Part-Time",                         "amount": 850.00,   "wht": 0.00,   "type": "part-time"},
    {"no": 18, "name": "จิรวัฒน์ โขงรัมย์ / Expressway",                     "amount": 20.00,    "wht": 0.00,   "type": "expressway"},
    {"no": 19, "name": "รณชัย มิตรรักษ์ / Expressway",                       "amount": 130.00,   "wht": 0.00,   "type": "expressway"},
    {"no": 20, "name": "เทพอนันต์ โพธิ์เขียว / Expressway",                  "amount": 130.00,   "wht": 0.00,   "type": "expressway"},
    {"no": 21, "name": "วิทยา ทัพธานี / Expressway",                         "amount": 130.00,   "wht": 0.00,   "type": "expressway"},
    {"no": 22, "name": "อุ่นใจ โตนะโพธิ์ / Expressway",                     "amount": 115.00,   "wht": 0.00,   "type": "expressway"},
    {"no": 23, "name": "วีรวัลย์ อยู่ดิษฐ / Expressway",                    "amount": 65.00,    "wht": 0.00,   "type": "expressway"},
    {"no": 24, "name": "วีรวัลย์ อยู่ดิษฐ / ค่าน้ำแข็ง",                   "amount": 70.00,    "wht": 0.00,   "type": "other"},
]

PR_GRAND_TOTAL = 21541.40


def extract_slip_data_ocr(pdf_path: str) -> list[dict]:
    """
    สกัดข้อมูลจากสลิปโอนจ่าย (PDF รูปภาพ) ด้วย OCR
    คืนค่า list ของ {page, recipient, amount, bank, datetime, raw_text}
    """
    slips = []

    # ลอง pdfplumber ก่อน (กรณีมี text layer)
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"สลิป PDF มีทั้งหมด {total_pages} หน้า")

            for i, page in enumerate(pdf.pages):
                text = page.extract_text() or ""
                if text.strip():
                    slip = parse_slip_text(text, page_no=i + 1)
                    if slip:
                        slips.append(slip)
                    if (i + 1) % 50 == 0:
                        print(f"  อ่านสลิปแล้ว {i + 1}/{total_pages} หน้า...")

        if slips:
            print(f"✓ สกัดได้ {len(slips)} สลิปจาก text layer")
            return slips
    except Exception as e:
        print(f"pdfplumber error: {e}")

    # ถ้าไม่มี text layer → ใช้ OCR
    print("ไม่พบ text layer → ใช้ OCR (ต้องติดตั้ง pytesseract + pdf2image)")
    try:
        import pytesseract
        from pdf2image import convert_from_path
        from PIL import Image

        # ตั้ง path ของ Tesseract
        possible_paths = [
            r"C:\Program Files\Tesseract-OCR\tesseract.exe",
            r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        ]
        for p in possible_paths:
            if os.path.exists(p):
                pytesseract.pytesseract.tesseract_cmd = p
                break

        print("กำลังแปลง PDF เป็นรูปภาพ...")
        images = convert_from_path(pdf_path, dpi=200, thread_count=4)
        total_pages = len(images)
        print(f"แปลงได้ {total_pages} หน้า กำลัง OCR...")

        for i, img in enumerate(images):
            # OCR ด้วยภาษาไทย+อังกฤษ
            text = pytesseract.image_to_string(img, lang="tha+eng")
            slip = parse_slip_text(text, page_no=i + 1)
            if slip:
                slips.append(slip)
            if (i + 1) % 20 == 0:
                print(f"  OCR แล้ว {i + 1}/{total_pages} หน้า...")

    except ImportError as e:
        print(f"ขาด library: {e}")
        print("ติดตั้งด้วย: pip install pytesseract pdf2image pillow")
    except Exception as e:
        print(f"OCR error: {e}")

    return slips


def parse_slip_text(text: str, page_no: int) -> dict | None:
    """
    แยกข้อมูลจากข้อความใน slip หนึ่งหน้า
    รองรับสลิป SCB, KBank, BBL, PromptPay ฯลฯ
    """
    if not text or len(text.strip()) < 20:
        return None

    result = {
        "page": page_no,
        "recipient": "",
        "amount": 0.0,
        "bank": "",
        "account": "",
        "datetime": "",
        "ref": "",
        "raw_text": text.strip()
    }

    lines = [l.strip() for l in text.split("\n") if l.strip()]

    # ค้นหาจำนวนเงิน — รูปแบบ: 1,234.56 หรือ 1234.56
    amount_patterns = [
        r"จำนวนเงิน[:\s]*([0-9,]+\.?\d*)",
        r"Amount[:\s]*([0-9,]+\.?\d*)",
        r"([0-9]{1,3}(?:,[0-9]{3})*\.[0-9]{2})\s*(?:บาท|THB|฿)",
        r"โอนเงิน[:\s]*([0-9,]+\.?\d*)",
        r"ยอดโอน[:\s]*([0-9,]+\.?\d*)",
        r"Total[:\s]*([0-9,]+\.?\d*)",
    ]
    for pat in amount_patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            try:
                result["amount"] = float(m.group(1).replace(",", ""))
                break
            except ValueError:
                pass

    # ค้นหาชื่อผู้รับ
    recipient_patterns = [
        r"(?:ผู้รับ|ชื่อผู้รับ|Recipient|To|ไปยัง)[:\s]+([^\n]+)",
        r"(?:โอนไปยัง|ไปที่)[:\s]+([^\n]+)",
        r"(?:Name|ชื่อ)[:\s]+([^\n]+)",
    ]
    for pat in recipient_patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            result["recipient"] = m.group(1).strip()
            break

    # ค้นหาธนาคาร
    banks = {
        "SCB": ["SCB", "ไทยพาณิชย์", "Siam Commercial"],
        "KBank": ["KBank", "กสิกรไทย", "Kasikorn"],
        "BBL": ["BBL", "กรุงเทพ", "Bangkok Bank"],
        "KTB": ["KTB", "กรุงไทย", "Krungthai"],
        "TMB": ["TMB", "ทหารไทย"],
        "SCG": ["SCG"],
        "PromptPay": ["พร้อมเพย์", "PromptPay"],
    }
    for bank_name, keywords in banks.items():
        for kw in keywords:
            if kw.lower() in text.lower():
                result["bank"] = bank_name
                break
        if result["bank"]:
            break

    # ค้นหาเลขบัญชี
    acc_m = re.search(r"(?:บัญชี|Account|เลขที่)[:\s]*([0-9\-x*]{8,20})", text, re.IGNORECASE)
    if acc_m:
        result["account"] = acc_m.group(1).strip()

    # ค้นหาวันที่/เวลา
    dt_m = re.search(
        r"(\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4}[\s,]*\d{1,2}:\d{2}(?::\d{2})?)",
        text
    )
    if dt_m:
        result["datetime"] = dt_m.group(1).strip()

    # ค้นหาเลข ref
    ref_m = re.search(r"(?:Ref|อ้างอิง|เลขที่รายการ)[.:\s]*([A-Z0-9]{6,30})", text, re.IGNORECASE)
    if ref_m:
        result["ref"] = ref_m.group(1).strip()

    # ถ้าไม่พบยอดเงิน ให้ข้ามหน้านี้
    if result["amount"] == 0.0:
        return None

    return result


def match_pr_to_slips(pr_list: list[dict], slips: list[dict]) -> list[dict]:
    """
    จับคู่รายการ PR กับสลิป
    เปรียบเทียบยอดเงิน ± tolerance 1 บาท
    """
    TOLERANCE = 1.0
    results = []

    slip_used = [False] * len(slips)

    for pr in pr_list:
        pr_amount = pr["amount"]
        matched_slip = None
        matched_idx = -1

        # หาสลิปที่ยอดตรง
        for i, slip in enumerate(slips):
            if slip_used[i]:
                continue
            if abs(slip["amount"] - pr_amount) <= TOLERANCE:
                matched_slip = slip
                matched_idx = i
                break

        if matched_slip:
            slip_used[matched_idx] = True
            diff = round(matched_slip["amount"] - pr_amount, 2)
            results.append({
                "pr_no": pr["no"],
                "pr_name": pr["name"],
                "pr_amount": pr_amount,
                "pr_type": pr.get("type", ""),
                "slip_page": matched_slip["page"],
                "slip_amount": matched_slip["amount"],
                "slip_recipient": matched_slip["recipient"],
                "slip_bank": matched_slip["bank"],
                "slip_datetime": matched_slip["datetime"],
                "slip_ref": matched_slip["ref"],
                "diff": diff,
                "status": "OK" if abs(diff) <= TOLERANCE else "MISMATCH",
            })
        else:
            results.append({
                "pr_no": pr["no"],
                "pr_name": pr["name"],
                "pr_amount": pr_amount,
                "pr_type": pr.get("type", ""),
                "slip_page": None,
                "slip_amount": None,
                "slip_recipient": "",
                "slip_bank": "",
                "slip_datetime": "",
                "slip_ref": "",
                "diff": None,
                "status": "NO_SLIP",
            })

    # สลิปที่ไม่มี PR match (โอนเกิน?)
    unmatched_slips = []
    for i, slip in enumerate(slips):
        if not slip_used[i]:
            unmatched_slips.append({
                "slip_page": slip["page"],
                "slip_amount": slip["amount"],
                "slip_recipient": slip["recipient"],
                "slip_bank": slip["bank"],
                "slip_datetime": slip["datetime"],
                "slip_ref": slip["ref"],
                "status": "EXTRA_SLIP",
            })

    return results, unmatched_slips


def generate_html_report(
    results: list[dict],
    unmatched_slips: list[dict],
    pr_total: float,
    slip_total: float,
    report_date: str,
    output_path: str
):
    """สร้าง HTML report สวยงาม"""

    ok_count = sum(1 for r in results if r["status"] == "OK")
    mismatch_count = sum(1 for r in results if r["status"] == "MISMATCH")
    no_slip_count = sum(1 for r in results if r["status"] == "NO_SLIP")
    extra_count = len(unmatched_slips)
    total_count = len(results)
    overall_diff = round(slip_total - pr_total, 2)

    def status_badge(status):
        badges = {
            "OK": '<span class="badge ok">✓ ถูกต้อง</span>',
            "MISMATCH": '<span class="badge mismatch">⚠ ยอดไม่ตรง</span>',
            "NO_SLIP": '<span class="badge no-slip">✗ ไม่มีสลิป</span>',
            "EXTRA_SLIP": '<span class="badge extra">! สลิปเกิน</span>',
        }
        return badges.get(status, status)

    def fmt_amount(val):
        if val is None:
            return '<span class="na">—</span>'
        return f'<span class="amount">{val:,.2f}</span>'

    def diff_cell(diff, status):
        if diff is None:
            return '<td class="na">—</td>'
        color = "green" if abs(diff) < 0.01 else ("red" if abs(diff) > 1 else "orange")
        sign = "+" if diff > 0 else ""
        return f'<td style="color:{color};font-weight:bold">{sign}{diff:,.2f}</td>'

    rows_html = ""
    for r in results:
        rows_html += f"""
        <tr class="row-{r['status'].lower()}">
            <td class="center">{r['pr_no']}</td>
            <td class="name">{r['pr_name']}</td>
            <td class="center">{r['pr_type']}</td>
            <td class="right">{fmt_amount(r['pr_amount'])}</td>
            <td class="center">{r['slip_page'] or '—'}</td>
            <td class="right">{fmt_amount(r['slip_amount'])}</td>
            <td class="center">{r['slip_bank'] or '—'}</td>
            <td class="center">{r['slip_datetime'] or '—'}</td>
            {diff_cell(r['diff'], r['status'])}
            <td class="center">{status_badge(r['status'])}</td>
        </tr>"""

    extra_rows = ""
    for s in unmatched_slips:
        extra_rows += f"""
        <tr class="row-extra_slip">
            <td class="center">—</td>
            <td class="name">{s['slip_recipient'] or '(ไม่ทราบชื่อ)'}</td>
            <td class="center">—</td>
            <td class="right">—</td>
            <td class="center">{s['slip_page']}</td>
            <td class="right">{fmt_amount(s['slip_amount'])}</td>
            <td class="center">{s['slip_bank'] or '—'}</td>
            <td class="center">{s['slip_datetime'] or '—'}</td>
            <td style="color:orange;font-weight:bold">—</td>
            <td class="center">{status_badge('EXTRA_SLIP')}</td>
        </tr>"""

    html = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ตรวจสอบยอดโอนจ่าย Rider — {report_date}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: #f0f2f5; color: #222; }}
  .container {{ max-width: 1400px; margin: 0 auto; padding: 24px; }}

  /* Header */
  .header {{ background: linear-gradient(135deg, #1a237e, #283593); color: white;
             border-radius: 12px; padding: 24px 32px; margin-bottom: 24px; }}
  .header h1 {{ font-size: 1.6rem; font-weight: 700; }}
  .header .sub {{ font-size: 0.9rem; opacity: 0.8; margin-top: 4px; }}
  .header .company {{ font-size: 0.85rem; opacity: 0.7; margin-top: 2px; }}

  /* Summary cards */
  .summary {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
              gap: 16px; margin-bottom: 24px; }}
  .card {{ background: white; border-radius: 10px; padding: 20px; text-align: center;
           box-shadow: 0 2px 8px rgba(0,0,0,.08); }}
  .card .label {{ font-size: 0.8rem; color: #666; margin-bottom: 6px; }}
  .card .value {{ font-size: 1.8rem; font-weight: 700; }}
  .card.total   .value {{ color: #1a237e; }}
  .card.ok      .value {{ color: #2e7d32; }}
  .card.mismatch .value {{ color: #f57f17; }}
  .card.no-slip  .value {{ color: #c62828; }}
  .card.extra    .value {{ color: #e65100; }}
  .card.diff-ok  .value {{ color: #2e7d32; }}
  .card.diff-bad .value {{ color: #c62828; }}

  /* Table */
  .table-wrap {{ background: white; border-radius: 10px; overflow: hidden;
                 box-shadow: 0 2px 8px rgba(0,0,0,.08); margin-bottom: 24px; }}
  .table-title {{ padding: 16px 20px; font-weight: 600; font-size: 1rem;
                  border-bottom: 1px solid #e0e0e0; background: #fafafa; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 0.85rem; }}
  th {{ background: #1a237e; color: white; padding: 10px 12px; text-align: center;
        font-weight: 600; font-size: 0.8rem; white-space: nowrap; }}
  td {{ padding: 9px 12px; border-bottom: 1px solid #f0f0f0; }}
  tr:last-child td {{ border-bottom: none; }}
  tr:hover {{ background: #f8f9ff; }}
  .center {{ text-align: center; }}
  .right  {{ text-align: right; }}
  .name   {{ max-width: 280px; }}
  .na     {{ color: #aaa; text-align: center; }}
  .amount {{ font-family: monospace; font-weight: 600; }}

  /* Row colors */
  .row-ok         {{ background: #f1f8e9; }}
  .row-mismatch   {{ background: #fff8e1; }}
  .row-no_slip    {{ background: #ffebee; }}
  .row-extra_slip {{ background: #fff3e0; }}

  /* Badges */
  .badge {{ display: inline-block; padding: 3px 10px; border-radius: 20px;
            font-size: 0.75rem; font-weight: 600; white-space: nowrap; }}
  .badge.ok       {{ background: #c8e6c9; color: #1b5e20; }}
  .badge.mismatch {{ background: #fff9c4; color: #f57f17; }}
  .badge.no-slip  {{ background: #ffcdd2; color: #b71c1c; }}
  .badge.extra    {{ background: #ffe0b2; color: #bf360c; }}

  /* Totals row */
  .totals-row td {{ font-weight: 700; background: #e8eaf6; font-size: 0.9rem; }}

  /* Legend */
  .legend {{ display: flex; gap: 16px; flex-wrap: wrap; padding: 12px 20px;
             background: #fafafa; border-top: 1px solid #e0e0e0; font-size: 0.8rem; }}
  .legend span {{ display: flex; align-items: center; gap: 6px; }}
  .dot {{ width: 12px; height: 12px; border-radius: 3px; }}
  .dot-ok       {{ background: #c8e6c9; }}
  .dot-mismatch {{ background: #fff9c4; border: 1px solid #f0c040; }}
  .dot-no-slip  {{ background: #ffcdd2; }}
  .dot-extra    {{ background: #ffe0b2; }}

  .footer {{ text-align: center; font-size: 0.8rem; color: #999; margin-top: 16px; }}
  .alert-box {{ background: #fff3e0; border-left: 4px solid #ff9800;
                border-radius: 6px; padding: 14px 18px; margin-bottom: 20px; font-size: 0.9rem; }}
  .alert-box.success {{ background: #e8f5e9; border-color: #4caf50; }}
</style>
</head>
<body>
<div class="container">

  <div class="header">
    <h1>ระบบตรวจสอบยอดโอนจ่าย Rider</h1>
    <div class="sub">เปรียบเทียบรายการเบิก (PR) กับสลิปโอนจ่าย</div>
    <div class="company">MAKESEND EXPRESS COMPANY LIMITED &nbsp;|&nbsp; วันที่ {report_date}</div>
  </div>

  {"" if overall_diff == 0 else f'<div class="alert-box">⚠ ยอดรวมต่างกัน <strong>{overall_diff:+,.2f} บาท</strong> — กรุณาตรวจสอบรายการที่มีปัญหา</div>'}
  {"" if overall_diff != 0 else '<div class="alert-box success">✓ ยอดรวมตรงกัน — ไม่พบความผิดปกติในภาพรวม</div>'}

  <div class="summary">
    <div class="card total">
      <div class="label">รายการทั้งหมด (PR)</div>
      <div class="value">{total_count}</div>
    </div>
    <div class="card ok">
      <div class="label">✓ ถูกต้อง</div>
      <div class="value">{ok_count}</div>
    </div>
    <div class="card mismatch">
      <div class="label">⚠ ยอดไม่ตรง</div>
      <div class="value">{mismatch_count}</div>
    </div>
    <div class="card no-slip">
      <div class="label">✗ ไม่มีสลิป</div>
      <div class="value">{no_slip_count}</div>
    </div>
    <div class="card extra">
      <div class="label">! สลิปเกิน PR</div>
      <div class="value">{extra_count}</div>
    </div>
    <div class="card {'diff-ok' if abs(overall_diff) < 1 else 'diff-bad'}">
      <div class="label">ผลต่างยอดรวม</div>
      <div class="value">{overall_diff:+,.2f}</div>
    </div>
  </div>

  <div class="table-wrap">
    <div class="table-title">รายละเอียดการตรวจสอบแต่ละรายการ</div>
    <table>
      <thead>
        <tr>
          <th>No.</th>
          <th>ชื่อ / รายการ</th>
          <th>ประเภท</th>
          <th>ยอด PR (บาท)</th>
          <th>หน้าสลิป</th>
          <th>ยอดสลิป (บาท)</th>
          <th>ธนาคาร</th>
          <th>วันเวลาโอน</th>
          <th>ผลต่าง</th>
          <th>สถานะ</th>
        </tr>
      </thead>
      <tbody>
        {rows_html}
        {extra_rows}
        <tr class="totals-row">
          <td colspan="3" class="right">รวมทั้งสิ้น</td>
          <td class="right">{pr_total:,.2f}</td>
          <td>—</td>
          <td class="right">{slip_total:,.2f}</td>
          <td colspan="2">—</td>
          <td style="color:{'green' if abs(overall_diff)<1 else 'red'}">{overall_diff:+,.2f}</td>
          <td>—</td>
        </tr>
      </tbody>
    </table>
    <div class="legend">
      <span><span class="dot dot-ok"></span> ถูกต้อง</span>
      <span><span class="dot dot-mismatch"></span> ยอดไม่ตรง</span>
      <span><span class="dot dot-no-slip"></span> ไม่มีสลิป</span>
      <span><span class="dot dot-extra"></span> สลิปเกิน PR</span>
    </div>
  </div>

  <div class="footer">
    สร้างโดยระบบ MADGA Payment Verification &nbsp;|&nbsp; {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
  </div>
</div>
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ สร้าง report ที่: {output_path}")


def main():
    pr_pdf = r"C:\Users\AI-IT-386\Downloads\parttime 07.05.2026.pdf"
    slip_pdf = r"C:\Users\AI-IT-386\Downloads\สลิปโอนจ่าย 07.05.2026.pdf"
    report_date = "07/05/2026"
    output_html = r"C:\Users\AI-IT-386\Downloads\payment_verification_07052026.html"

    print("=" * 60)
    print("ระบบตรวจสอบยอดโอนจ่าย Rider — MAKESEND EXPRESS")
    print("=" * 60)

    # 1. ใช้ข้อมูล PR ที่ hardcode แล้ว
    print(f"\n[1] โหลดข้อมูล PR: {len(PR_DATA)} รายการ, ยอดรวม {PR_GRAND_TOTAL:,.2f} บาท")

    # 2. สกัดข้อมูลสลิป
    print(f"\n[2] กำลังอ่านสลิป: {slip_pdf}")
    slips = extract_slip_data_ocr(slip_pdf)
    print(f"    → พบสลิปทั้งหมด {len(slips)} รายการ")

    if not slips:
        print("\n⚠ ไม่สามารถสกัดข้อมูลจากสลิปได้")
        print("   กรุณาตรวจสอบว่าติดตั้ง library ครบ:")
        print("   pip install pdfplumber pytesseract pdf2image pillow")
        print("\n   กำลังสร้าง report ด้วยข้อมูล PR อย่างเดียว...")
        slips = []

    slip_total = sum(s["amount"] for s in slips)
    print(f"    → ยอดรวมสลิป: {slip_total:,.2f} บาท")

    # 3. จับคู่และเปรียบเทียบ
    print("\n[3] กำลังเปรียบเทียบรายการ...")
    results, unmatched = match_pr_to_slips(PR_DATA, slips)

    ok = sum(1 for r in results if r["status"] == "OK")
    no_slip = sum(1 for r in results if r["status"] == "NO_SLIP")
    mismatch = sum(1 for r in results if r["status"] == "MISMATCH")

    print(f"    ✓ ถูกต้อง:   {ok} รายการ")
    print(f"    ✗ ไม่มีสลิป: {no_slip} รายการ")
    print(f"    ⚠ ยอดไม่ตรง: {mismatch} รายการ")
    print(f"    ! สลิปเกิน:  {len(unmatched)} รายการ")

    # 4. สร้าง HTML report
    print(f"\n[4] กำลังสร้าง HTML report...")
    generate_html_report(
        results=results,
        unmatched_slips=unmatched,
        pr_total=PR_GRAND_TOTAL,
        slip_total=slip_total,
        report_date=report_date,
        output_path=output_html,
    )

    print(f"\n{'=' * 60}")
    print(f"เสร็จสิ้น! เปิด report ที่:")
    print(f"  {output_html}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
