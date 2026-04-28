---
title: Bank Statement Reconciliation — Steps
process_id: bank-statement-reconciliation
updated: 2026-04-28
---

# Bank Statement Reconciliation — Step Breakdown

## ฝั่ง AR — กระทบยอด Statement กับรายได้ (รายวัน)

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | Download Statement จาก Kbank website | AR Officer / Intern | Kbank Website | ไฟล์ Statement | AI: AI_Statement_1313100347_2024; MS: MS_Statement_9021001659_2024 |
| 2 | นำข้อมูล Statement มาวางใน Sheet AI_Statement รายวัน | AR Officer / Intern | Google Sheets: AI_Statement | Sheet อัปเดต | — |
| 3 | Reconcile รายได้ที่บันทึกใน PEAK (RV-xxxxxxxx) กับ Statement → บันทึกไว้ในชีท AI_Statement พร้อมคำอธิบาย | AR Officer / Intern | PEAK / Google Sheets | ยอด Reconcile | Column J = เลข RV, Column K = สาขา+วันที่ |
| 4 | ตรวจสอบ Column C (รายการ/คำอธิบาย) และ Column F (จำนวนเงิน) ว่าครบถ้วน | AR Officer / Intern | Google Sheets | Statement ครบถ้วน | RE ที่บันทึกใน PEAK ต้องปรากฏใน Statement |

---

## ฝั่ง AP — เช็ค Statement ด้านค่าใช้จ่าย (รายเดือน)

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | เปิด Statement → ดูที่ Column E (ถอนเงิน) = ยอดที่ถอนออกจากบัญชีบริษัท | AP Officer | Statement Sheet | รายการถอนเงิน | ข้อมูลอยู่ใน Drive แยกตาม Sheet |
| 2 | แยกประเภทรายการ: ยอดที่บัญชีแจ้งเบิกโดยตรง (มีตั้งหนี้ใน PEAK แล้ว) vs ยอดที่แผนกอื่นๆเบิกตรงกับคุณโฮ่ (ยังไม่ผ่านบัญชี) | AP Officer | Statement / PEAK | รายการที่จัดประเภทแล้ว | — |
| 3 | ติดตามเอกสารจากแผนกที่เบิกตรงกับคุณโฮ่ → บันทึกค่าใช้จ่ายให้ตรงเดือนนั้น | AP Officer | เอกสาร / PEAK | EXP บันทึกแล้ว | บันทึกให้ตรงเดือนเสมอ |
| 4 | กระทบยอดถอนทุกรายการใน Statement จนครบ | AP Officer | Statement | Statement กระทบยอดแล้ว | — |

---

## Statement ที่ใช้

| บัญชี | Sheet ที่ใช้ | สำหรับ |
|---|---|---|
| AI — 1313100347 | AI_Statement_1313100347_2024 | รายได้ / รายจ่าย Airportels |
| MS — 9021001659 | MS_Statement_9021001659_2024 | รายได้ / รายจ่าย Makesend |

---

## Reconcile Summary

| รายการ | ตรวจที่ไหน | ผลที่ต้องการ |
|---|---|---|
| รายได้สาขา (RV) | Column J/K ใน AI Statement | ทุก RV มีในทั้ง PEAK และ Statement |
| รายได้ PayPal | JV โอนเงินออกจากกระเป๋า PayPal | ยอดตรงกับ Kbank Statement |
| รายได้ Omise | JV Transfer Omise → Kbank | ยอดตรงกับ Kbank Statement |
| ค่าใช้จ่าย (ถอนเงิน) | Column E ใน Statement | ทุกรายการมีเอกสาร EXP ใน PEAK |
