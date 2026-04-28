## 2026-04-28 — อัพเดทกระบวนการจาก SOP จริง (AP / AR / Internship)

### What was done
- อ่านและวิเคราะห์ 3 ไฟล์ SOP: Accounting Officer AP SOP (มอส), Accounts Receivable SOP (มุก), Internship SOP
- อัพเดท 4 กระบวนการหลักด้วยข้อมูลจาก SOP จริง:
  - **Rider Payroll**: เพิ่ม FT (คำนวณยอด AI จาก Shipment Report, JVFN, รหัสบัญชี) + PT (CSH009, หัก/ไม่หัก WHT 3%)
  - **Partner Billing & AR**: เพิ่ม Partner list 15+ ราย พร้อมรอบวางบิล, credit term, email, ช่องทางดึง Order
  - **Tax Filing**: เพิ่มขั้นตอน ภงด.3/53, ภาษีซื้อ, ภาษีขาย, RD Prep, e-Filing แบบ step-by-step
  - **Branch Income Recording**: เพิ่ม Lark → Sheet Income → PEAK (RT/RV/RE) → AI Statement flow จริง
- อัพเดท dashboard sub-pages ทั้ง 4 หน้า
- อัพเดท dashboard/index.html activity log

### Files changed
- `processes/rider-payroll/steps.md` — ขยายจาก 5 rows เป็น 20+ rows จริง
- `processes/rider-payroll/overview.md` — เพิ่ม tools, timing, pain points จาก SOP
- `processes/partner-billing-ar/steps.md` — เพิ่ม Partner list + billing schedule
- `processes/partner-billing-ar/overview.md` — เพิ่ม timing table ตาม billing cycle
- `processes/tax-filing-reporting/steps.md` — เพิ่ม 3 sub-process (ภงด.3/53, ซื้อ, ขาย)
- `processes/branch-income-recording/steps.md` — เพิ่ม Lark flow + 4 sub-sections
- `dashboard/pages/process-rider-payroll.html` — updated step tables
- `dashboard/pages/process-partner-billing-ar.html` — updated + partner tables
- `dashboard/pages/process-tax-filing-reporting.html` — updated + 3 sections
- `dashboard/pages/process-branch-income-recording.html` — updated + 4 sections
- `dashboard/index.html` — updatedAt + activity log
- `processes/expense-reimbursement/steps.md` — เพิ่ม 3 sub-sections (ตั้งหนี้ 6 ขั้น, ชำระหนี้ 3 ขั้น, WHT 2 ขั้น) + ตารางอ้างอิงเอกสารแนบ
- `processes/petty-cash-advance/steps.md` — เพิ่ม 3 sub-sections (ใช้เงินสดย่อย, เคลีย 7 วัน 5 ขั้น, จัดซื้อ) + ตารางเอกสารตามประเภท
- `dashboard/pages/process-expense-reimbursement.html` — แทน 8 generic rows ด้วย 3 sub-sections + reference table เอกสารแนบ
- `dashboard/pages/process-petty-cash-advance.html` — แทน 7 generic rows ด้วย 3 sub-sections + reference table ตามประเภท

### Still TBD
- Landlord Revenue Reporting: ยังไม่ได้อัพเดท monthly report flow
- Online Payment Recording: รายละเอียด Paypal / Omise flow จาก AR SOP
- Commission Payment: รายละเอียด MS Go Payment Voucher จาก AP SOP
- Bank Statement Reconciliation: รายละเอียด AI Statement reconcile flow
- Fixed Assets: stub — ยังไม่มีข้อมูลจาก SOP

### Suggested next steps
- อัพเดท Online Payment Recording (Omise/PayPal) จาก AR SOP
- อัพเดท Commission Payment (MS Go) จาก AP SOP
- อัพเดท Landlord Revenue Reporting (monthly + branch contacts)
- สร้าง Mermaid flowchart สำหรับ Partner Billing & AR
- ตรวจสอบกับมุกและมอสว่ากระบวนการที่จดไว้ตรงกับที่ทำจริงไหม

---

## 2026-04-27 — Process mapping complete

### What was done
- Analyzed job descriptions for 4 roles: Accounting Manager, AR Officer, AP Officer, Intern Accounting
- Identified and created 12 distinct processes across 5 categories
- Created 24 process markdown files (overview.md + steps.md × 12)
- Updated dashboard/index.html DASHBOARD_DATA with all 12 processes and 5 team members
- Updated dashboard/data.json with full process data export
- Created 12 process sub-pages: dashboard/pages/process-*.html
- Updated department/overview.md with full team table
- Updated department/process-map.md with all 12 processes

### Files changed
- `processes/*/overview.md` × 12 — created
- `processes/*/steps.md` × 12 — created
- `department/overview.md` — team table updated (5 members)
- `department/process-map.md` — 12 processes added
- `dashboard/index.html` — DASHBOARD_DATA updated (12 processes, 5 members)
- `dashboard/data.json` — full data export updated
- `dashboard/pages/process-*.html` × 12 — created

### Process categories
| Category | Processes |
|---|---|
| Revenue / AR | Branch Income Recording, Landlord Revenue Reporting, Online Payment Recording, Partner Billing & AR, Bank Statement Reconciliation |
| Expense / AP | Petty Cash & Advance, Expense Reimbursement, Rider Payroll, Commission Payment |
| Compliance | Tax Filing & Reporting |
| Assets | Fixed Assets Management |
| Reporting | Monthly Financial Close |

### Still TBD
- Department mission
- Pain points for each process
- Approval flow details for Petty Cash
- Rider payroll frequency and payment channel
- Commission data source
- Bank statement pull frequency

---

## 2026-04-27 — Department name corrected

### What was done
- Corrected department name from "MAKESEND Financial" to "Airportels Financial"
- MAKESEND is a sub-workflow/business unit within Airportels Financial (not the top-level department)
- Updated: .madga, department/overview.md, process-map.md, dashboard/index.html, data.json, README.md, CLAUDE.md

### Files changed
- `.madga` — department: "Airportels Financial"
- `department/overview.md` — renamed + added Sub-Departments section noting MAKESEND
- `department/process-map.md` — renamed
- `dashboard/index.html` — title + DASHBOARD_DATA updated
- `dashboard/data.json` — department name updated
- `README.md` — title updated
- `CLAUDE.md` — all references updated

### Still TBD
- Department mission
- Team members (beyond Oh)
- All processes

### Suggested next steps
- Describe Airportels Financial's main workflows — including MAKESEND and other business units

---

## 2026-04-27 — Project initialized

### What was done
- Project scaffolded for MAKESEND Financial (Airportels)
- Git repository connected to remote
- Created full folder structure: department/, processes/, plans/, dashboard/
- Created: CLAUDE.md, .madga, README.md, .gitignore, department/overview.md, department/process-map.md, dashboard/index.html
- Dashboard configured for online mode (CDN libraries)

### Files changed
- `README.md` — updated with MADGA project template
- `.madga` — ecosystem marker created (v1.3)
- `.gitignore` — created
- `department/overview.md` — placeholder created
- `department/process-map.md` — empty index created
- `dashboard/index.html` — base dashboard created
- `CLAUDE.md` — project rules generated

### Still TBD
- Department mission
- Team members list
- All processes (none added yet)
- Plans (none yet)

### Suggested next steps
- Tell Claude about your team's processes — what does MAKESEND Financial do day-to-day?
- Add team members: name + role
- Fill in department mission

---
