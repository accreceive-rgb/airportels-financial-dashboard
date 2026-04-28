---
title: Online Payment Recording (Omise / PayPal)
process_id: online-payment-recording
owner: AR Officer (มุก)
category: Revenue / AR
status: active
completeness: partial
updated: 2026-04-28
---

# Online Payment Recording — บันทึกรายได้ Omise / PayPal

## Purpose
ดึงรายงานและบันทึกบัญชีรายได้จากช่องทางชำระเงินออนไลน์ (Omise, PayPal) เข้าระบบ PEAK พร้อม Reconcile กับ Kbank Statement

## Stakeholders

| Name / Role | Involvement | Internal/External |
|---|---|---|
| มุก (AR Officer) | บันทึกรายได้ PayPal, Omise เข้า PEAK, Reconcile | Internal |
| โอ๋ (Accounting Manager) | กำกับดูแล | Internal |

## Tools & Systems

| Tool | Purpose in this process | Notes |
|---|---|---|
| Omise Dashboard | ดึงรายการ Transfer เข้า Kbank | https://dashboard.omise.co; user: sudarat@airportels.co |
| PayPal | ดึงรายงานรายได้ | user: airsudarat |
| PEAK | สร้างใบเสร็จ RV, JV โอนเงิน, บันทึกค่าธรรมเนียม | — |
| Sheet: Statement Paypal.xlsx | รวบรวมข้อมูล PayPal ทั้งเดือน | Drive: AI Accounting → AI Statement → Paypal |
| Sheet: AI_Statement | บันทึกเลข JVFN กับ Statement Kbank | — |

## Timing
รายเดือน (Omise ระหว่างเดือนถ้ามีโอนเข้า)

## Inputs
- รายงานจาก PayPal (กิจกรรม → รายงานทั้งหมด)
- ไฟล์ Export จาก Omise (Transfer menu)
- Kbank Statement (เพื่อ Reconcile ยอดโอนเข้า)

## Outputs
- ใบเสร็จ RE + RV ใน PEAK (PayPal)
- JV บันทึกรายได้ Omise เข้าธนาคาร
- JVFN โอนเงินออกจากกระเป๋า PayPal → Kbank
- Statement Paypal.xlsx อัปเดตครบ

## Cross-Department Links
- Receives from: Omise / PayPal (ระบบ External)
- Hands off to: Bank Statement Reconciliation (JVFN ใน Kbank Statement), Tax Filing (JV รายได้ต้องปรากฏในภาษีขาย)

## Pain Points
- Omise ไม่มีเมนู Export ทุกครั้ง — ต้องหาไฟล์จาก Drive แทน
- PayPal Refund ข้ามเดือน ต้องบันทึกเป็นติดลบรายได้ (ระวังอย่า double count)
