---
title: Partner Billing & AR — Steps
process_id: partner-billing-ar
updated: 2026-04-28
---

# Partner Billing & AR — Step Breakdown

## ขั้นตอนหลัก (ทุก Partner)

| # | Step | Actor | Tool/System | Output | Notes |
|---|---|---|---|---|---|
| 1 | ดึง/รับรายงาน Order จาก Partner (ตามช่องทางของแต่ละ Partner) | AR Officer | ตามระบบ Partner | ไฟล์ Order Report | ดูตารางด้านล่างสำหรับ Partner แต่ละราย |
| 2 | ตรวจสอบ Order กับ Sheet: AIRPORTELs partner's orders | AR Officer | Google Sheets | Order ที่ตรวจแล้ว | Vlookup Booking Reference / Booking No. — แจ้ง Guest Service ถ้าตกหล่น |
| 3 | สร้างใบแจ้งหนี้ใน PEAK | AR Officer | PEAK → รายรับ → ใบแจ้งหนี้ | Invoice (INV-xxxxx) | แบ่งตามประเภทบริการ: ฝาก/ส่ง/ล้อยาง |
| 4 | ส่ง Email วางบิล + ใบแจ้งหนี้ให้ Partner | AR Officer | Email | Invoice ที่ส่งแล้ว | ดู Email / CC ของแต่ละ Partner ด้านล่าง |
| 5 | รอการชำระเงินตาม Credit Term | AR Officer | — | — | ดู Credit Term แต่ละ Partner |
| 6 | รับชำระ → กดรับชำระจากใบแจ้งหนี้ใน PEAK | AR Officer | PEAK | ใบเสร็จรับเงิน RV | ตรวจเช็คค่าธรรมเนียม / หัก ณ ที่จ่าย |
| 7 | พิมพ์ RV + RE/RT + Credit Advice → เรียงชุด → เก็บแฟ้ม "ใบสำคัญรับ" | AR Officer | PEAK | เอกสารชุดรับ | RV + RT/RE + Credit Advice (ถ้ามี) |
| 8 | ติดตามเอกสารหัก ณ ที่จ่ายจาก Partner | AR Officer | PEAK → การเงิน → ภาษีถูกหัก ณ ที่จ่าย | เอกสาร WHT ที่บันทึกแล้ว | แสกนแนบเข้าระบบ + เก็บแฟ้ม |

---

## Partner List & Billing Details

### รอบวางบิลทุก 15 วัน (ชำระทุกศุกร์ที่ 2 และ 4)

| Partner | Credit Term | ช่องทางดึง Order | Email วางบิล |
|---|---|---|---|
| Samurai wifi | 7 วันหลังวางบิล | Drive / Sheet Airportel Samuri wifi record | bsmobileacc@bangkoksamurai.com; cc: vsu_cm@bangkoksamurai.com |
| Klook | 7 วันหลังวางบิล | Email: Klook Booking Report (PDF+Excel) | settlement@klook.com; cc: minnie.siripasid@klook.com |
| KKDay SCM | 10 วันหลังวางบิล | Email / SCM System | op-ap-eng@kkday.com; cc: bd-th@kkday.com |
| DreamCT | 5 วันหลังวางบิล | Sheet: AIRPORTELs partner's orders (filter DreamCT) | ติดต่อคุณเอมผ่าน Line Group "DreamCT" ก่อนส่ง |
| Globaltix | 7–14 วันหลังวางบิล | https://merchant.globaltix.com (status: Redeemed เท่านั้น) | suchunya@globaltix.com; cc: globaltix-th@globaltix.com |
| Patois (พาทัวร์) | — | — | — |

### รอบวางบิลทุก 30 วัน / รายเดือน

| Partner | Credit Term | ช่องทางดึง Order | Email / ช่องทาง |
|---|---|---|---|
| Yoowifi | 10 วันหลังวางบิล | Email ขอรายงานจาก TSWorld Info (info@ts-world.co) | info@ts-world.co |
| Thailand Elite | 15 วันหลังวางบิล | ใบ Job Assignment จากสาขา → แสกน → Drive | rsvn@thailandelite.com; ส่งเอกสารจริงตามที่อยู่ |
| KKDay POS | วันที่ 25 ของเดือน | https://pos.kkday.com → CSV → รายงานค่าธรรมเนียม (3 สาขา: T21/DMK/BKK + CTW) | megan.chang@kkday.com; cc: หลายคน |
| Golfdigg | วันที่ 15 ของเดือน | Sheet: Golf Bag Delivery x AIRPORTELs (Responses) | business@golfdigg.com |
| Veltra | วันที่ 25 ของเดือนถัดไป | https://www.veltra.com/ptr/ptr_login → menu Billing → confirm all | agnes.niehof@veltra.com; cc: info-asia@veltra.com |
| Avagard Capsule | วันที่ 8 ของเดือนถัดไป | Sheet: BKK Sale Report tab AirportelsxAvargard | ส่งทาง Line คุณ Tatchaya |
| BnBCondo | รายเดือน, 5 วันหลังวางบิล | Sheet: BnBCondo key pick-up orders.xlsx | — |
| Toto Booking | วันที่ 15 เดือนถัดไป | Email ขอ Order ภายในวันที่ 5 (account@totobooking.com) | รอรายงานตอบกลับ |
| Hippo Tech | 5 วันหลังวางบิล | Email ขอ Order ภายในวันที่ 5 | รอรายงานในเมล |

### ไม่ต้องวางบิล (รับเงินอัตโนมัติ / ตามระบบ)

| Partner | วิธีรับเงิน | หมายเหตุ |
|---|---|---|
| Stasher | โอนเข้าบัญชีอัตโนมัติ | ไม่มี contract |
| Vertoe | โอนเข้าบัญชีอัตโนมัติ | ไม่มี contract |
| Viator | โอนเข้าบัญชีอัตโนมัติ | ไม่มี contract |
| Traveloka | โอนเข้าบัญชีอัตโนมัติ | ไม่มี contract |
| Qeepl | โอนเข้าบัญชีอัตโนมัติ | ไม่มี contract |
| Lean Team / Siri (Radical) | วันที่ 1 ของเดือนถัดไป | https://radicalstorage.com/angel/ → Payment → Invoice |
| Encounter (Pelago) | 15 วันหลังชำระ | https://provider.pelago.co → analytics / sale report |
| Trazy | ภายใน 3 วันทำการเดือนถัดไป | ชำระผ่าน Paypal |

---

## Samurai wifi — รายละเอียดพิเศษ

| รายการค่าบริการ | อัตรา |
|---|---|
| รับ-คืนเครื่อง (เลข Res No. ไม่ซ้ำ) | 40 บาท/ครั้ง |
| รับ-คืนเครื่อง (Res No. ซ้ำทั้ง pick up + return) | 20 บาท (0.5 ครั้ง) |
| ค่าสต็อคเครื่อง Beacon DMK | 2,000 บาท/เดือน |
| ค่าสต็อค CNX/HKT/TPY (3 ที่) | 1,500 บาท/เดือน |
| ค่าขนส่ง Pocket wifi | ตามจริง |

---

## การจัดเก็บเอกสาร

| แฟ้ม | เนื้อหา | การเรียง |
|---|---|---|
| แฟ้มใบสำคัญรับ | RV + RE/RT + INV + Credit Advice | เรียงตาม RV มากไปน้อย |
| แฟ้ม INV/TAX | INV/RE/RT | เรียงมากไปน้อย |
| แฟ้มสมุดรายวันทั่วไป | JV | เรียงมากไปน้อย |
| แฟ้มถูกหัก ณ ที่จ่าย | เอกสาร WHT จาก Partner | เขียนเลข RV บนเอกสาร เรียงตาม RV |
