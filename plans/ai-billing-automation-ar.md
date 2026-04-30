---
title: AI Auto-Billing สำหรับ AR วางบิล Partner
related_process: partner-billing-ar
status: draft
owner: โอ๋ (Accounting Manager)
created: 2026-04-30
updated: 2026-04-30
---

# AI Auto-Billing สำหรับ AR วางบิล Partner

## Problem

AR Officer (มุก) ต้องดึง Order Report จากระบบของ Partner 13+ รายด้วยตนเอง แต่ละรายมีช่องทาง ราคา และเงื่อนไขสัญญาที่แตกต่างกัน ทำให้ต้องค้นสัญญา สร้างสูตรคำนวณ และตรวจทานทุกรอบบิล ส่งผลให้:
- ใช้เวลามากต่อรอบวางบิล (15 วัน / 30 วัน)
- มีความเสี่ยงคลาดเคลื่อนจากการคำนวณมือ
- ยากในการ scale เมื่อมี Partner เพิ่มขึ้น
- ถ้าคนดูแลลาหรือออก ไม่มีใครรู้สูตรหรือเงื่อนไขแต่ละราย

## Analysis

### Root Cause
- ราคาต่อ Order ขึ้นอยู่กับ Rate Card ในสัญญาของแต่ละ Partner (ไม่มี standard)
- ข้อมูล Order กระจายอยู่ใน Portal / Email / Google Sheet ของแต่ละ Partner
- ปัจจุบันยังไม่มีระบบกลางที่ดึงข้อมูลมารวม + คำนวณอัตโนมัติ

### โอกาส
AI (LLM + Automation) สามารถ:
1. **อ่านสัญญา** → แปลง Rate Card เป็นโครงสร้างข้อมูล (JSON)
2. **ดึง Order** → เชื่อมต่อ API / Sheet / Email parsing ของแต่ละ Partner
3. **คำนวณยอด** → จับคู่ Order กับ Rate Card → ได้ยอด Invoice โดยอัตโนมัติ
4. **Draft Invoice** → สร้างข้อมูลพร้อมนำเข้า PEAK หรือออก Invoice ได้ทันที

### Partner ที่ต้องวางบิลด้วยมือ (เป้าหมาย Automate)
รอบ 15 วัน: Samurai, Klook, KKDay SCM, DreamCT, Globaltix, Patois (6 ราย)
รอบ 30 วัน: Yoowifi, Thailand Elite, KKDay POS, Golfdigg, Veltra, Avagard, BnBCondo, Toto, Hippo (9 ราย)

## Plan

### Actions

| # | Action | Owner | Target | Status | Notes |
|---|---|---|---|---|---|
| 1 | รวบรวม Contract/Rate Card ของ Partner ทุกราย (13+ ราย) | มุก + โอ๋ | 2026-05-15 | planned | สำเนา PDF/Word ทุกสัญญา รวมถึง Rate ที่ตกลงกันทาง Email |
| 2 | ให้ AI อ่าน Contract และแปลง Rate Card เป็น Structured Data (JSON) | โอ๋ + Dev | 2026-05-23 | planned | ใช้ Claude API อ่าน PDF → สร้าง Rate Card JSON ต่อ Partner |
| 3 | เชื่อมต่อแหล่งข้อมูล Order นำร่อง 3 ราย (Klook, KKDay SCM, Samurai) | Dev | 2026-06-06 | planned | API / Google Sheet API / Email Parser |
| 4 | สร้าง AI Price Calculator: รับ Order + Rate Card → คำนวณยอด Invoice | Dev | 2026-06-20 | planned | Validate ผลลัพธ์กับที่คำนวณมือย้อนหลัง 3 เดือน |
| 5 | Pilot Test กับ 3 Partner นำร่อง (Klook, KKDay SCM, Samurai) | มุก + Dev | 2026-07-04 | planned | รัน parallel กับ manual 1 รอบ — เปรียบเทียบยอด |
| 6 | Roll out Partner ที่เหลือทั้งหมด + ปิด Manual Process | มุก + Dev | 2026-07-31 | planned | อบรมมุกใช้งาน, สร้าง SOP ใหม่ |

### Dependencies
- ต้องได้รับสำเนา Contract ครบทุกราย (บางรายอาจตกลงด้วยวาจา — ต้อง confirm ลายลักษณ์อักษร)
- ระบบหลังบ้าน Partner บางรายไม่มี API → ต้องประเมินทางเลือก (Screen scraping / Email parsing)
- PEAK ต้องรองรับการนำเข้า Invoice แบบ bulk หรือ API

### Risks
| ความเสี่ยง | ระดับ | Mitigation |
|---|---|---|
| Contract บางรายไม่มีเป็นลายลักษณ์อักษร | สูง | ให้มุกทวนกับ Partner ก่อนเริ่ม Phase 2 |
| Partner Portal ไม่มี API | กลาง | ใช้ Email parsing หรือ Sheet connector แทน |
| AI คำนวณผิดในกรณี Edge case | กลาง | เปรียบเทียบกับ manual 1 รอบก่อน go-live |
| PEAK ไม่รองรับ bulk import | ต่ำ | ใช้ PEAK API หรือ copy-paste structured data |

### Success Criteria
- AR Officer ใช้เวลาต่อรอบวางบิลลดลง ≥ 70%
- ยอด Invoice ที่ AI คำนวณตรงกับ manual ≥ 99%
- ไม่ต้องสร้างหรือแก้สูตรเองเลยเมื่อมี Partner ใหม่ — แค่โยนสัญญาให้ AI
