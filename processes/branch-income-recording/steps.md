---
title: Branch Income Recording — Steps
process_id: branch-income-recording
updated: 2026-04-28
---

# Branch Income Recording — Step Breakdown

## ขั้นตอนบันทึก AI Income รายวัน

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | รับ Dairy Sale Report จาก Lark (Notification Sales Report - External) | Intern / AR Officer | Lark → Notification Sales Report (External) → Dairy Sale Report | ข้อมูลยอดขายแต่ละสาขา | หลังปิดร้านทุกวัน |
| 2 | บันทึก AI Income ลง Sheet Income แยกตามสาขา | Intern / AR Officer | Google Sheet: AI Income (Tab เดือนปัจจุบัน) | Sheet Income อัปเดต | แยก Storage / Delivery / Silicone Wheel; แยก Cash / QR / Credit / Alipay / WeChat |
| 3 | สร้างโฟลเดอร์ payin วันที่ใน Drive → บันทึกสลิปจาก Line "AI Gang" | Intern / AR Officer | Drive → New Folder ชื่อ "payin DD.MM.YY" | สลิปตามสาขา | ตั้งชื่อรูปตามชื่อสาขา เช่น CTW H 20.08.24 |
| 4 | ตรวจสอบยอดเงินสด: สลิปฝากใน Lark vs AI Income Excel | Intern / AR Officer | Lark / Excel | ✔ เครื่องหมายยืนยันสาขา | ถ้าสาขาไหนยังไม่มีรูปสลิป แจ้งฟีงได้เลย |
| 5 | สร้างใบเสร็จรับเงิน (RT/RE) ใน PEAK สำหรับแต่ละสาขา | Intern / AR Officer | PEAK → รายรับ → ใบเสร็จ → สร้างหรือคัดลอกจากฉบับเก่า | RT/RE ในระบบ | เลือก: P00001 ฝากกระเป๋า / P00002 รับ-ส่งกระเป๋า / P00010 ล้อยางซิลิโคน |
| 6 | ใส่ยอดเงินแยกตามประเภท → กดรับชำระ → เลือกช่องทางชำระ | Intern / AR Officer | PEAK | ใบเสร็จ (RT) อนุมัติแล้ว | กดรับชำระ → ขั้นสูง ถ้าชำระหลายช่องทาง; ใส่ค่าธรรมเนียมธนาคาร (รหัส 530501) ถ้ามี |
| 7 | แนบ Payslip ใน PEAK → อนุมัติใบเสร็จ | Intern / AR Officer | PEAK | ใบเสร็จอนุมัติแล้ว | แนบ Payslip จาก Line Group ทุกครั้ง |
| 8 | Print RT/RE → RV → Credit Advice (ถ้ามี) | Intern / AR Officer | PEAK | ชุดเอกสาร 1 ชุด | RV ต้อง Print แนบ Payslip (cash) ด้วย |
| 9 | บันทึกเลข RV ใน AI Statement (Column J = RV, Column K = สาขา+วันที่) | Intern / AR Officer | Google Sheet: AI Statement | Statement อัปเดต | ดูวันที่จาก Column A, รายการจาก Column C |
| 10 | เรียงเอกสาร: RV + RT/RE + Credit Advice → เก็บแฟ้ม "ใบสำคัญรับ" | Intern / AR Officer | — | แฟ้มเอกสาร | — |

## ใบเสร็จให้ลูกค้าทั่วไป (Walk-in ต้องการใบเสร็จเบิกบริษัท)

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | สร้างใบเสร็จ → เลือกชื่อลูกค้าทั่วไป | AR Officer | PEAK → รายรับ → ใบเสร็จ | RT | ขั้นตอนเดียวกับข้อ 5–10 ด้านบน |

## รับชำระจาก Partner (กรณีมีใบแจ้งหนี้เดิม)

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | ไปที่ PEAK → รายรับ → ใบแจ้งหนี้ → กดรับชำระ | AR Officer | PEAK | ใบเสร็จ RV | ตรวจค่าธรรมเนียม / หัก ณ ที่จ่ายก่อนยืนยัน |
| 2 | แนบ Payslip → กดยืนยันใบเสร็จรับเงิน | AR Officer | PEAK | ใบเสร็จอนุมัติแล้ว | — |
| 3 | Print และเรียงเอกสาร → เก็บแฟ้ม | AR Officer | — | แฟ้มเอกสาร | — |

## Print E-TAX INVOICE FOR EWALLET

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | เปิด Email → Click mail ขึ้นต้นด้วย "Fwd: E-TAX INVOICE FOR EWALLET" | Intern | Gmail: acc.intern2024@gmail.com | ไฟล์ PDF | รหัสเปิดไฟล์: 98687 |
| 2 | Print ไฟล์ PDF | Intern | Printer | ใบ E-TAX | — |
