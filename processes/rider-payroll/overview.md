---
title: Rider Payroll Processing
process_id: rider-payroll
owner: AP Officer (มอส) / Intern Accounting
category: Expense / AP
status: active
completeness: partial
updated: 2026-04-28
---

# Rider Payroll — ค่าจ้าง Rider Full-time / Part-time

## Purpose
ตรวจสอบเอกสาร คำนวณยอด และบันทึกบัญชีค่าจ้าง Rider ทั้ง Full-time และ Part-time เข้าระบบ PEAK พร้อมจัดทำหักณที่จ่ายและจัดเก็บเอกสาร

## Stakeholders

| Name / Role | Involvement | Internal/External |
|---|---|---|
| มอส (AP Officer) | ตรวจเช็คเอกสาร คำนวณยอด บันทึกบัญชี จัดเก็บ | Internal |
| Intern Accounting | ช่วยบันทึกบัญชี จัดเก็บ | Internal |
| โอ๋ (Accounting Manager) | ตรวจสอบและอนุมัติ | Internal |
| คุณโฮ่ (CEO) | อนุมัติยอดเบิกจ่าย | Internal |
| อนวัช ธนะตัน (Fleet) | จัดทำใบเบิกและนำส่งเอกสาร Rider | Internal |

## Tools & Systems

| Tool | Purpose in this process | Notes |
|---|---|---|
| PEAK | บันทึก EXP, JVFN, พิมพ์เอกสาร | รายจ่าย → บันทึกค่าใช้จ่าย |
| Line Group: Acc&Fleet Document | รับเอกสารใบเบิกจาก Fleet | ใช้ทั้ง FT และ PT |
| Line Group: Operation Executive | แจ้งยอดคุณโฮ่อนุมัติ | รอบ 16–30/31 เท่านั้น |
| Drive: MAKESEND Accounting | Shipment Report (คำนวณยอด AI), จัดเก็บ WHT | _Client by INVOICES → 7974_Airportels |
| K PLUS SME | ช่องทางโอนจ่าย | ดูวันที่โอนจากสลิป |

## Timing

| รอบ | ความถี่ |
|---|---|
| Fulltime รอบ 1–15 | ต้นเดือน (หลังวันที่ 15) |
| Fulltime รอบ 16–30/31 | ปลายเดือน (หลังสิ้นเดือน) |
| Parttime | เกือบทุกวัน / ตามที่ Fleet แจ้ง |

## Inputs
- ใบเบิกค่าจ้าง Rider จาก Fleet (Line Group: Acc&Fleet Document)
- Shipment Report จาก Drive MAKESEND (ใช้คำนวณยอด AI รอบ 16–30/31)
- สลิปโอนเงิน (K PLUS SME)
- สำเนาบัตรประชาชน Rider (สำหรับชุดจ่าย)

## Outputs
- EXP + PV + ใบหัก ณ ที่จ่าย (ชุดจ่าย Rider แต่ละคน)
- รายการบัญชีใน PEAK (EXP, JVFN)
- ไฟล์ PDF ใบหัก ณ ที่จ่าย (50ทวิ) จัดเก็บใน Drive ตามชื่อและเดือน

## Cross-Department Links
- Receives from: Fleet / Operations (ใบเบิก, สลิปโอน)
- Hands off to: Tax Filing & Reporting (ภงด.3 — หักณที่จ่าย Riders)

## Pain Points
- คำนวณยอด AI รอบ 16–30/31 ต้องทำด้วยมือ (เลือก Riders ให้ยอดใกล้ Grand Total ±200–400)
- Parttime เบิกจ่ายแทบทุกวัน — ต้องติดตามเอกสารจาก Fleet ให้ทันเดือนนั้น
- ถ้าเดือนไหนยอดต่างกับ Grand Total มาก ให้ทบยอดไปเดือนถัดไปได้
