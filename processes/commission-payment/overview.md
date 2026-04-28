---
title: Commission Payment (MS Go / Partner)
process_id: commission-payment
owner: AP Officer (มอส)
category: Expense / AP
status: active
completeness: partial
updated: 2026-04-28
---

# Commission Payment — จ่าย Commission MS Go / Partner

## Purpose
จัดทำ Payment Voucher และดำเนินการจ่าย Commission ประจำเดือนให้กับ MS Go และ Partner พร้อมออกหัก ณ ที่จ่าย

## Stakeholders

| Name / Role | Involvement | Internal/External |
|---|---|---|
| AP Officer | จัดทำ Payment Voucher, ออกหัก ณ ที่จ่าย | Internal |
| Accounting Manager | ตรวจสอบและอนุมัติ | Internal |
| คุณโฮ่ | อนุมัติขั้นสุดท้าย | Internal |
| MS Go / Partner | ผู้รับ Commission | External |

## Tools & Systems

| Tool | Purpose in this process | Notes |
|---|---|---|
| PEAK | บันทึกบัญชี Payment Voucher | — |
| เอกสารหัก ณ ที่จ่าย | ออกให้ผู้รับ Commission | ภ.ง.ด.3 หรือ 53 |

## Timing
Monthly — ทุกเดือน

## Inputs
- ไฟล์ 2 ไฟล์จากโอ๋: partners Accounting Report_MSGO_ตาราง + ตาราง_Dropoff
- ยอด Order จาก Sheet MSGO_ID (รายการยกเลิก)
- ยอดยืนยันจากสาขา (ผ่าน Line Official)

## Outputs
- Payment Voucher Commission MS Go (แยกตามสาขา)
- ใบเบิกค่าคอมมิชชั่น
- EXP + PV + ใบหัก ณ ที่จ่าย (ชุดจ่ายแต่ละสาขา)
- ไฟล์จัดเก็บใน Drive: MAKESEND Accounting

## Timing

| กำหนด | รายการ |
|---|---|
| ภายในวันที่ 5 ของเดือน | ส่ง Payment Voucher ให้สาขา confirm ยอด |
| ภายในวันที่ 15 ของเดือน | เบิกจ่าย Commission ให้สาขา |

## Cross-Department Links
- Receives from: โอ๋ (ไฟล์ Accounting Report MSGO)
- Hands off to: Tax Filing (WHT ใน 50ทวิ), Bank Statement (JVFN)

## Pain Points
- ต้องรอสาขา confirm ยอดผ่าน Line ก่อนจ่าย — บางสาขาช้า
- ต้องนำข้อมูล Dropoff มาใส่แยกสาขา (false=Ambient, true=Chilled) ด้วยมือ
