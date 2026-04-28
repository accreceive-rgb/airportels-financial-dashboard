---
title: Rider Payroll Processing — Steps
process_id: rider-payroll
updated: 2026-04-28
---

# Rider Payroll — Step Breakdown

## Fulltime Riders (2 รอบต่อเดือน)

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | รับใบเบิกค่าจ้าง Riders รอบ 1–15 จาก Fleet | AP Officer / Intern | Line Group: Acc&Fleet Document | ใบเบิกรอบ 1–15 | MS จ่ายเต็มจำนวน 100% |
| 2 | คำนวณยอด AI สำหรับรอบ 16–30/31 จาก Shipment Report | AP Officer | Drive: MAKESEND Accounting → _Client by INVOICES → 7974_Airportels | ยอด Grand Total AI | ยอดต่างกับ Grand Total ได้ไม่เกิน ±200–400 บาท |
| 3 | คัดเลือก Riders ที่ AI จ่าย (ไม่รวมค่าประกันและ Advance) | AP Officer | Sheet "เบิกเงิน" | รายชื่อ Riders ฝั่ง AI / ฝั่ง MS | ใช้ชื่อ "AI 16–30/เดือน/ปี" และ "MS 16–30/เดือน/ปี" |
| 4 | แจ้งยอดให้คุณโฮ่อนุมัติ | AP Officer | Line Group: Operation Executive | การอนุมัติ | — |
| 5 | บันทึก JVFN โอนเงินไปพักที่ "เงินสด-อนวัช" ใน PEAK | AP Officer | PEAK → การเงิน → เงินสด/ธนาคาร/e-Wallet → โอนเงิน | รายการ JVFN | แนบสลิปโอน + ใบเบิกในเอกสาร |
| 6 | ตรวจเช็คใบเบิก vs ยอดโอน (ทางด่วน, น้ำมัน, EasyPass มีใบเสร็จครบ?) | AP Officer / Intern | เอกสาร | เอกสารผ่านการตรวจ | ติดตามจาก Fleet ถ้าไม่ครบ |
| 7 | บันทึกค่าใช้จ่าย Riders ใน PEAK (คัดลอก EXP เดิม) | AP Officer / Intern | PEAK → รายจ่าย → บันทึกค่าใช้จ่าย | EXP รายการใหม่ | รหัส 510107, หัก ณ ที่จ่าย 3%, จ่ายโดย "เงินสด-อนวัช" |
| 8 | อนุมัติค่าใช้จ่าย → พิมพ์ EXP + PV + ใบหัก ณ ที่จ่าย | AP Officer / Intern | PEAK | EXP, PV, ใบ WHT | แนบสำเนาบัตร ปชช. + สลิปโอน |
| 9 | ส่งโอ๋ตรวจสอบและอนุมัติ | AP Officer | — | ความถูกต้องที่ยืนยันแล้ว | — |
| 10 | Save ใบหัก ณ ที่จ่าย เป็น PDF → จัดเก็บใน Drive | AP Officer / Intern | Drive: MAKESEND Accounting | ไฟล์ PDF WHT | แยก FT/PT ตามชื่อ Rider + เก็บใน 50ทวิ ตามเดือน |

## Parttime Riders (เกือบทุกวัน)

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | ดู Statement → เจอโอนให้ "อนวัช ธนะตัน" | AP Officer / Intern | PEAK / Statement | รายการที่ต้องบันทึก | Fleet เบิกกับคุณโฮ่โดยตรง ไม่ผ่านบัญชี |
| 2 | ติดตามเอกสารการจ่ายจาก Fleet | AP Officer / Intern | Line Group: Acc&Fleet Document | ใบเบิก + สลิปโอน | บันทึกภายในเดือนที่มีการจ่าย |
| 3 | บันทึก JVFN โอนเงินไปที่ "อนวัช-Riders Part-time" ใน PEAK | AP Officer / Intern | PEAK → การเงิน → โอนเงิน | รายการ JVFN | — |
| 4A | บันทึก EXP (ไม่มีหัก ณ ที่จ่าย) ในนาม "อนวัช ธนะตัน" | AP Officer / Intern | PEAK | EXP | จ่ายโดย "อนวัช-Riders Part-time (CSH009)" |
| 4B | บันทึก EXP (มีหัก ณ ที่จ่าย 3%) ในชื่อ Rider จริง | AP Officer / Intern | PEAK | EXP + WHT | รหัส 510107, หัก 3%, CSH009 |
| 5 | อนุมัติ → พิมพ์ EXP + PV (+ใบหัก ณ ที่จ่าย ถ้ามี) | AP Officer / Intern | PEAK | ชุดเอกสาร | แนบสลิป + สำเนาบัตร ปชช. |
| 6 | Save ใบหัก ณ ที่จ่าย → จัดเก็บใน Drive | AP Officer / Intern | Drive: MAKESEND Accounting | ไฟล์ PDF WHT | โฟลเดอร์ WHT_Rider Part-time 2024 ตามรายชื่อ |

## ค่าใช้จ่ายเพิ่มเติม (ทางด่วน, น้ำมัน, ประกัน, ค่าเสื้อ, Advance)

| รหัสบัญชี | ประเภทค่าใช้จ่าย |
|---|---|
| 510107 | ค่าขนส่งสินค้า, EasyPass |
| 510118 | ค่าน้ำมัน |
| 113203 | Advance, เบิกเงินล่วงหน้า |
| 212309 | ค่าประกัน, ค่าประกัน DV |
| 420109 | ค่าเคลม, ค่าปรับ |
| 530303 | ค่าโทรศัพท์ |
| 520218 | ค่าติดตั้งสติ๊กเกอร์ |

## Deadline Summary

| รอบ | กำหนด |
|---|---|
| Fulltime รอบ 1–15 | บันทึกเมื่อครบ 2 รอบ (หลังวันที่ 16) |
| Fulltime รอบ 16–30/31 | บันทึกเมื่อได้เอกสารครบ |
| Parttime | บันทึกภายในเดือนที่มีการจ่าย |
