---
title: Partner Billing & Accounts Receivable
process_id: partner-billing-ar
owner: AR Officer (มุก)
category: Revenue / AR
status: active
completeness: partial
updated: 2026-04-28
---

# Partner Billing & AR — วางบิลและเรียกเก็บรายได้จาก Partner

## Purpose
ออก Invoice เรียกเก็บรายได้จาก Partner ตามรอบวางบิล (15/30 วัน หรือตามกำหนด) ตรวจสอบ Order ให้ครบ รับชำระ บันทึกเข้า PEAK และติดตามเอกสารหัก ณ ที่จ่าย

## Stakeholders

| Name / Role | Involvement | Internal/External |
|---|---|---|
| มุก (AR Officer) | ดึง Order, ตรวจสอบ, ออก Invoice, รับชำระ, ติดตาม WHT | Internal |
| โอ๋ (Accounting Manager) | กำกับดูแล | Internal |
| Guest Service Executive | ช่วยตรวจสอบ Order ที่ตกหล่น | Internal |
| Partners (15+ ราย) | ชำระเงินและส่งเอกสาร | External |

## Tools & Systems

| Tool | Purpose in this process | Notes |
|---|---|---|
| PEAK | ออก Invoice, รับชำระ, พิมพ์เอกสาร | รายรับ → ใบแจ้งหนี้ |
| Google Sheets: AIRPORTELs partner's orders | ตรวจสอบ Order ครบถ้วน | Vlookup ตรวจหาตกหล่น |
| ระบบของแต่ละ Partner | ดึง Order Report | Klook Portal, SCM, Veltra, Globaltix ฯลฯ |
| Email | ส่ง Invoice, รับชำระ | CC: accountingpayment@airportels.asia ทุกราย |

## Timing

| รอบ | Partner | กำหนด |
|---|---|---|
| ทุก 15 วัน | Samurai, Klook, KKDay SCM, DreamCT, Globaltix, Patois | ชำระทุกศุกร์ที่ 2 และ 4 |
| รายเดือน / 30 วัน | Yoowifi, Thailand Elite, KKDay POS, Golfdigg, Veltra, Avagard, BnBCondo, Toto, Hippo | 1 ครั้งต่อเดือน |
| อัตโนมัติ | Stasher, Vertoe, Viator, Traveloka, Qeepl, Radical, Pelago, Trazy | รับเงินตามระบบ ไม่ต้องวางบิล |

## Inputs
- Order Report จากระบบของแต่ละ Partner
- Sheet: AIRPORTELs partner's orders (ข้อมูล Order รวม)
- เอกสารหัก ณ ที่จ่าย (50ทวิ) จาก Partner

## Outputs
- Invoice (INV-xxxxx) ส่งให้ Partner
- ใบเสร็จรับเงิน (RV + RE/RT) บันทึกใน PEAK
- เอกสารหัก ณ ที่จ่ายที่แสกนและบันทึกในระบบ
- แฟ้มจัดเก็บ: ใบสำคัญรับ, INV/TAX, สมุดรายวัน

## Cross-Department Links
- Receives from: Branch Income Recording (ยอดขายใน Sheet Income)
- Hands off to: Bank Statement Reconciliation (รับเงินเข้าบัญชี), Tax Filing (WHT ที่ได้รับ)

## Pain Points
- Partner 15+ รายมีวงรอบและช่องทางดึง Order ต่างกัน
- Order ตกหล่นต้องประสานงานกับ Guest Service Executive
- Thailand Elite: ต้องส่งเอกสาร Job Assignment จริงทางไปรษณีย์
- Trazy: ชำระผ่าน Paypal ต้องบันทึกแยก
