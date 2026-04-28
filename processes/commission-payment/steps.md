---
title: Commission Payment — Steps
process_id: commission-payment
updated: 2026-04-28
---

# Commission Payment — Step Breakdown

## Commission MS Go (รายเดือน)

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | โอ๋เตรียมไฟล์ 2 ไฟล์ไว้ใน Drive | โอ๋ (Accounting Manager) | Drive: MAKESEND Accounting → MS go | partners Accounting Report_MSGO_ตาราง + ตาราง_Dropoff | — |
| 2 | เปิดไฟล์ partners Accounting Report_MSGO_ตาราง → Tab CALCULATE | AP Officer | Excel | ข้อมูล Order สาขา | — |
| 3 | Copy: service date, user id, branch_name, Actual_Parcel, Actual_income, MS_order_id, COD → ใส่ใน Sheet "Payment Voucher" | AP Officer | Excel (Sheet Payment Voucher) | ข้อมูลใน PV | — |
| 4 | เปลี่ยนวันที่ 1 และ 30/31 ในแถบสีน้ำเงิน + เรียง Column K (วันที่ 1 ถึงสิ้นเดือน) | AP Officer | Excel | PV อัปเดต | ข้อมูลวิ่งอัตโนมัติหลังกรอก |
| 5 | ตรวจ Total Column L, M, N ต้องตรงกับ partners Accounting Report ตาราง | AP Officer | Excel | ยืนยันยอดถูกต้อง | — |
| 6 | ดึงข้อมูลจากตาราง_Dropoff → Filter ทีละสาขา → ใส่ใน Payment Voucher ฝาก/ส่ง (false=Ambient, true=Chilled) | AP Officer | Excel | PV ครบทุกสาขา | ทำไปจนครบทุกสาขาที่มีรายการ |
| 7 | ดึงรายการยกเลิกจาก Sheet MSGO_ID → ใส่ใน Payment Voucher: วันที่, Tracking Number, Amount ตามสาขา | AP Officer | Excel | รายการยกเลิกครบ | — |
| 8 | แจ้งโอ๋ตรวจสอบ → Print ใบ Payment → ส่งให้สาขา confirm ยอดผ่าน Line Official | AP Officer | Printer / Line | PV ยืนยันจากสาขา | **ภายในวันที่ 5 ของเดือน** |
| 9 | จัดทำใบเบิกค่าคอมมิชชั่น → ลงยอดจ่ายแต่ละสาขาจาก PV | AP Officer | Excel: MAKESEND Accounting → MS go → ใบเบิกCommissionMS Go | ใบเบิก Commission | **เบิกจ่ายภายในวันที่ 15** |
| 10 | บันทึก JVFN โอนเงินพักที่ "เงินสด-ธีรศักดิ์" ใน PEAK | AP Officer | PEAK → การเงิน → โอนเงิน | รายการ JVFN | บัญชีบริษัทโอนพักก่อน |
| 11 | เมื่อ "เงินสด-ธีรศักดิ์" โอนให้สาขา → บันทึก EXP ใน PEAK | AP Officer | PEAK → รายจ่าย → บันทึกค่าใช้จ่าย | EXP Commission | คัดลอกจากชื่อเดิม; จ่ายโดย "เงินสด-ธีรศักดิ์" |
| 12 | แนบสำเนาบัตร ปชช., สลิปโอน → อนุมัติ → พิมพ์ EXP + PV + ใบหัก ณ ที่จ่าย (ถ้ามี) | AP Officer | PEAK | ชุดเอกสาร Commission | — |
| 13 | จัดเก็บเอกสารใน Drive | AP Officer | Drive: MAKESEND Accounting | ไฟล์จัดเก็บ | PV → CommissionMSgo2024 → เดือน; สลิปโอน → Pay-in commission ms go → เดือน; WHT → MAKESEND Taxation → 50ทวิ → เดือน |

---

## Deadline Summary

| กำหนด | รายการ |
|---|---|
| วันที่ 5 ของเดือน | ส่ง Payment Voucher ให้สาขา confirm |
| วันที่ 15 ของเดือน | เบิกจ่าย Commission ให้สาขา |
