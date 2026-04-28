---
title: Landlord Revenue Reporting — Steps
process_id: landlord-revenue-reporting
updated: 2026-04-28
---

# Landlord Revenue Reporting — Step Breakdown

## รายงานรายวัน (สาขา TPY, ICS, MBK, PNX)

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | ดึงข้อมูลยอดขายจาก Sale Report Sheet ของแต่ละสาขา (TPY/ICS/PNX) | Intern / AR Officer | Google Sheets: TPY / ICS Sale Report | ข้อมูลยอดขายรายวัน | ดู Column B: จำนวน Order, Column F: Normal luggage, Column G: Special, Column N: Storage, Column O: Delivery |
| 2 | บันทึกข้อมูลลงใน Sheet Commission branch (ช่อง No.Order, Quantity, Amount) | Intern / AR Officer | Sheet: Commission branch | ตาราง Summary | แยก DPS / Luggage ให้ถูกต้อง |
| 3 | Save PDF ตั้งชื่อ: ปีเดือนวัน-ชื่อสาขา เช่น 2024-08-12-TPY | Intern / AR Officer | — | ไฟล์ PDF | — |
| 4A | **TPY** — ส่ง Email Report | Intern / AR Officer | Gmail: Sudarat@airportels.co | Email ส่งแล้ว | To: cashier.pattaya@terminal21.co.th; CC: accountingpayment@airportels.asia |
| 4B | **ICS** — Upload Report + แนบไฟล์ JPEG ใน website | Intern / AR Officer | https://www.siamsmartcollection.com | ส่งรายงานแล้ว | แปลงเป็น JPEG ก่อนแนบ |
| 4C | **MBK** — เปิด Dashboard Postels → Land Lord Daily Report → เลือกวันที่/MBK/View | Intern / AR Officer | https://postels.airportels.asia/admin/login | ข้อมูล MBK | กด F12 ถ้าต้องแก้ไข |
| 5 | **MBK** — บันทึก PDF → Submit ยอดขายใน website MBK | Intern / AR Officer | https://gpcollection.mbkgroup.co.th/DailyData/InputDailySale.php | ส่งรายงานแล้ว | รายงานได้แค่ 3 วันย้อนหลัง; เกินกำหนดส่ง Email: chalermpoon@mbkgroup.co.th; CC: accountingpayment@airportels.asia |

---

## รายงานรายเดือน (สาขาทั้งหมด)

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | ตรวจสอบรายได้ใน Sheet Income ตรงกับ Sheet Business Performance | AR Officer | Google Sheets | ยอดตรงกัน 2 Sheet | ทำก่อนส่ง Landlord ทุกครั้ง |
| 2 | Copy ยอด Total (ยอดขายรวมแต่ละวัน) ใส่ใน Form Sheet ตามสาขา | AR Officer | Sheet: Commission branch → Form | Form ครบทุกสาขา | มี Form เฉพาะ T21, CTWHug, CTWGroove, CSM, ICS, TPY, CPY |
| 3 | ส่ง Email รายงานรายเดือนตาม Landlord ด้านล่าง | AR Officer | Gmail | Email ส่งแล้ว | CC: accountingpayment@airportels.asia ทุกราย |

---

## Landlord Contact List (รายเดือน)

| สาขา | To (Email) | CC |
|---|---|---|
| T21 | kanokphorn@terminal21.co.th | acc_receive@airportels.co, accountingpayment@airportels.asia, jinaron@terminal21.co.th |
| CTWHug / CTWGroove | SoPatcharee@centralpattana.co.th, KhaKanjana@centralpattana.co.th, thrasamee@centralpattana.co.th, FinanceCenter4.Consign@centralpattana.co.th | acc_receive@airportels.co, accountingpayment@airportels.asia, anan@airportels.asia |
| CSM | FinanceCenter4.Consign@centralpattana.co.th | tameena@centralpattana.co.th, accountingpayment@airportels.asia, acc_receive@airportels.co |
| ICS | tarnwimon.b@siampiwat.com | arunrat.t@siampiwat.com, acc_receive@airportels.co |
| TPY | cashier.pattaya@terminal21.co.th | accountingpayment@airportels.asia |
| CPY | FinanceCenter4.Consign@centralpattana.co.th | tameena@centralpattana.co.th, accountingpayment@airportels.asia, acc_receive@airportels.co |
| CNX | supreeya.k@airportthai.co.th | accountingpayment@airportels.asia, anan@airportels.asia, acc_receive@airportels.co, pimnara.j@airportthai.co.th |

### CNX — ขั้นตอนพิเศษ

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | นำรายได้ Total ทั้งเดือนวางใน Column T Row 20 ของ Form CNX | AR Officer | Google Sheets | Form CNX ครบ | — |
| 2 | Print Form → ผู้บริหารเซ็น → Scan เก็บไฟล์ใน Drive | AR Officer | Printer / Drive | ไฟล์ Scan | — |
| 3 | ส่ง Email พร้อมไฟล์ Scan | AR Officer | Gmail | Email ส่งแล้ว | — |
| 4 | ส่งรายงานฉบับจริงที่ผู้บริหารเซ็น **ทางไปรษณีย์** | AR Officer | ไปรษณีย์ | เอกสารส่งแล้ว | ผู้รับ: คุณเนม สุปรียา — สวนพาณิชย์และแผนงาน ฝ่ายอำนวยการท่าอากาศยานเชียงใหม่ ชั้น 1 อาคารสำนักงาน ทชม. เลขที่ 60 ถนนมหิดล ต.สุเทพ อ.เมือง จ.เชียงใหม่ 50200 โทร 089-9999219 |
