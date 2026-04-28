---
title: Online Payment Recording — Steps
process_id: online-payment-recording
updated: 2026-04-28
---

# Online Payment Recording — Step Breakdown

## PayPal (รายเดือน)

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | Login PayPal → กิจกรรม → รายงานทั้งหมด → สร้างรายงาน → เลือกวันที่ | AR Officer | PayPal Dashboard | รายงาน PayPal | user: airsudarat |
| 2 | Copy ข้อมูลจากรายงาน → วางใน Sheet Statement Paypal.xlsx (Tab เดือนล่าสุด) | AR Officer | Google Sheets | Sheet Statement Paypal | Drive: AI Accounting → AI Statement → Paypal |
| 3 | SUM คอลัมน์ F, G, H | AR Officer | Excel | ยอดรวม | — |
| 4 | คำนวณรายได้: คอลัมน์ H ลบยอดถอนใน Statement (เข้า Kbank + Trazy) | AR Officer | Excel | ยอดรายได้ | — |
| 5 | คำนวณรายได้สุทธิ: คอลัมน์ H ลบ คอลัมน์ I (ลบค่าธรรมเนียม) | AR Officer | Excel | ยอดรายได้สุทธิ | — |
| 6 | สร้างใบเสร็จใน PEAK ใส่รายละเอียดค่าธรรมเนียม (บันทึกเงินเข้ากระเป๋า PayPal) | AR Officer | PEAK | ใบเสร็จ RE + RV | — |
| 7 | นำเลข RE + RV บันทึกใน Statement Paypal | AR Officer | Excel | Statement Paypal อัปเดต | — |
| 8 | PEAK → การเงิน → กระเป๋าเงิน PayPal → ทำรายการ → โอนเงินออก → ใส่วันที่ + ยอดตาม Kbank | AR Officer | PEAK | รายการ JVFN | บันทึกรับเงินเข้า Kbank |
| 9 | นำเลข JVFN บันทึกใน AI Statement (Kbank) | AR Officer | Google Sheets | Statement Kbank อัปเดต | — |
| 10 | แคปกระเป๋า PayPal → วางใน Statement Paypal (ยอดสุทธิต้องเท่ากับ SUM คอลัมน์ J) | AR Officer | Excel | ยืนยันยอดถูกต้อง | — |

---

## Omise (รายเดือน / ระหว่างเดือน)

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | Login Omise Dashboard → เมนู Transfer → ดูรายการที่ถูกโอนเข้า Kbank | AR Officer | https://dashboard.omise.co | รายการโอน Omise | user: sudarat@airportels.co |
| 2 | นำยอดที่โอนเข้ากสิกรมาบันทึกใน PEAK → สร้าง JV หักค่าธรรมเนียมการโอน → อนุมัติเอกสาร | AR Officer | PEAK | JV Omise | — |
| 3 | ดาวน์โหลดไฟล์จาก Omise → เมนู Transfer → Export → เลือกเดือน | AR Officer | Omise / Drive | ไฟล์ Omise | ถ้าไม่มีเมนู Export → หาจาก Drive (Omise statement ตามเดือน) |
| 4 | สร้าง JV บันทึกเงิน Omise เข้าธนาคาร → แนบไฟล์ Omise + Kbank Statement | AR Officer | PEAK | JV พร้อมเอกสารแนบ | — |

---

## ภาษีขาย (Output VAT) — Omise / PayPal

หลังบันทึก JV ครบแล้ว ให้ทำรายงาน Reconcile ภาษีขาย VS AI Income ตามกระบวนการ **Tax Filing & Reporting** (ขั้นตอนภาษีขาย)

| รายการ | ผลที่ต้องการ |
|---|---|
| JV รายได้ Omise / PayPal | ถูกรวมในรายงานภาษีขาย (ตรวจจากหมวด 410212 delivery) |
| JV Refund ข้ามเดือน | บันทึกเป็นติดลบในรายได้ (ดูคำอธิบาย JV ก่อน) |
