# BÁO CÁO ĐÁNH GIÁ HIỆN TRẠNG & KẾ HOẠCH TRIỂN KHAI ITSM/QA 2026
## ITSM/QA Current State Assessment & 12-Month Implementation Roadmap

**Ngày báo cáo:** 02/12/2025
**Phiên bản:** 1.0
**Đối tượng:** Ban Lãnh Đạo (Leadership Team)
**Người thực hiện:** ITSM & QA Team

---

## TÓM TẮT ĐIỀU HÀNH (EXECUTIVE SUMMARY)

### 1. Tổng Quan Tình Hình (Overview)

Đánh giá hiện trạng trưởng thành (maturity assessment) của 7 mảng hoạt động ITSM và QA cho thấy **mức độ trung bình 38%**, tương đương **Level 1-2** (Initial to Managed). Điều này phản ánh một tổ chức đang trong giai đoạn chuyển đổi từ hoạt động **ad-hoc sang quy trình hóa**, nhưng còn nhiều khoảng trống quan trọng cần khắc phục.

#### Maturity Levels Chi Tiết:

| Mảng Hoạt động | Điểm Số | Mức độ | Trạng thái | Target 12M |
|----------------|---------|--------|------------|------------|
| **Change Management (CM)** | 58.5% | Level 2 | 🟢 Tốt nhất | Level 3 (60-75%) |
| **Request Management (RM)** | 47.8% | Level 1.8 | 🟡 Khá | Level 2 (55-65%) |
| **Incident Management (IM)** | 44.3% | Level 1.8 | 🟡 Khá | Level 3 (60-70%) |
| **Process QA (PQA)** | 41.2% | Level 2 Low | 🟡 Trung bình | Level 2 High (50-65%) |
| **Quality Control (QC)** | 30.8% | Level 1 | 🟠 Yếu | Level 2 (45-50%) |
| **3rd Party Management** | 19.4% | Level 1 | 🔴 Rất yếu | Level 2 (45-60%) |
| **CMDB** | 9.3% | Level 1 | 🔴 **Nghiêm trọng** | Level 2 (45-60%) |

**Trung bình:** 35.9% → Target: 55-65% (+20-30%)

### 2. Điểm Mạnh & Thành Tựu (Strengths)

✅ **Change Management:** Quy trình rõ ràng, SLA tracking tốt (77%), CFR < 5%, có CAB setup
✅ **Team Resources:** 6.5 FTE dedicated cho ITSM/QA, có ownership mindset
✅ **Tools Foundation:** Jira 100%, Grafana dashboard, CI/CD 98% integration
✅ **Culture:** Blame-free culture tốt, collaboration giữa teams ổn định
✅ **Security:** VA/Pentest định kỳ, Secure-SDLC đã triển khai

### 3. Khoảng Trống Nghiêm Trọng (Critical Gaps)

#### 🔴 **Gap 1: KHÔNG CÓ CMDB (9.3% - NGHIÊM TRỌNG NHẤT)**
- **Hiện trạng:** Sử dụng Excel thủ công, không có tool chuyên dụng
- **Ảnh hưởng:** Blocks tất cả integration (IM-CM-RM), không track dependencies, impact analysis không thể thực hiện
- **Urgency:** Must fix Q1-Q2, affects tất cả 6 mảng khác

#### 🔴 **Gap 2: KHÔNG CÓ METRICS/KPI DASHBOARD**
- **Hiện trạng:**
  - PQA: 13.6% metrics
  - QC: 23% measurement
  - RM: 20.8% metrics (không track volume, SLA%, cycle time)
  - IM: 50% nhưng không có KPI formal
  - 3rd Party: 8% metrics
- **Ảnh hưởng:** Không đo lường được hiệu quả, không có basis cho quyết định lãnh đạo, không chứng minh ROI
- **Urgency:** Q1 foundation, Q2 automation

#### 🔴 **Gap 3: KHÔNG CÓ COMPLIANCE/AUDIT FRAMEWORK**
- **Hiện trạng:**
  - CM: 0% compliance
  - IM: 0% ITIL compliance
  - QC: 15% compliance
  - CMDB: 6.2% compliance
- **Ảnh hưởng:** Rủi ro audit bên ngoài, không tuân thủ ISO/ITIL, không có audit trail
- **Urgency:** Q1 checklist, Q2-Q3 audit cycles

#### 🔴 **Gap 4: THIẾU NGUỒN LỰC NGHIÊM TRỌNG**
- **Hiện trạng:**
  - CMDB: **0 FTE** (đáng ra cần 1-2 FTE)
  - 3rd Party: **0 FTE** (đáng ra cần 1 FTE)
  - IM: 1.5 FTE (thiếu IM Manager role formal, cần 2-2.5 FTE)
  - PQA: 1 FTE cho 7 mảng audit (coverage chỉ 3%, cần 2 FTE)
- **Ảnh hưởng:** Cannot scale, phụ thuộc key persons, burnout risk
- **Urgency:** Must hire Q1-Q2

#### 🔴 **Gap 5: KHÔNG CÓ AUTOMATION**
- **Hiện trạng:**
  - IM: 20% automation (routing, priority, creation đều manual)
  - RM: 0% auto-categorization
  - Integration: 100% manual linking giữa processes
- **Ảnh hưởng:** High MTTA/MTTR, human error, không scalable
- **Urgency:** Q2-Q3 implementation

### 4. Cross-Cutting Themes (Vấn đề chung cho tất cả mảng)

| Theme | Impact Areas | Severity |
|-------|--------------|----------|
| **RACI chưa formalized** | All 7 areas | HIGH |
| **SLA chưa định nghĩa rõ** | IM (25%), RM (partial) | HIGH |
| **Training/Certification thiếu** | All areas - ITIL cert = 0% | MEDIUM |
| **Manual integration** | IM-CM-RM-CMDB | HIGH |
| **Data quality standards = 0** | CMDB, RM, IM | MEDIUM |

### 5. Đề Xuất Giải Pháp (Proposed Solution)

#### 4 Mục Tiêu Chính (4 Objectives - OC1 to OC4):

**OC1: Thiết lập Framework Quản trị ITSM**
📋 Policies, Roles, RACI, SLA cho tất cả mảng
⏰ Timeline: Q1-Q2 (6 tháng)
💰 Cost: Low (mainly internal effort)
✅ Success: 7 policy docs, 7 RACI matrices, SLA definitions approved

**OC2: Xây dựng CMDB Chuẩn hóa**
🗄️ Tool selection, CI classification, data population, integration
⏰ Timeline: Q1-Q4 (12 tháng, phased)
💰 Cost: $20-50K tool + 1 FTE CMDB Admin
✅ Success: CMDB tool deployed, 50% CIs populated Q2, 80% Q4

**OC3: Nâng cao Mức độ Trưởng thành ITSM**
🚀 Cải thiện chất lượng, tăng tốc release, tiết kiệm chi phí
⏰ Timeline: Q2-Q4 (9 tháng)
💰 Cost: Automation tools, training
✅ Success: +20% maturity avg, 30% MTTA/MTTR reduction, CFR < 3%

**OC4: Thiết lập Metrics & Dashboards**
📊 KPI dashboards, CSAT mechanism, monthly reviews
⏰ Timeline: Q1-Q3 (9 tháng)
💰 Cost: BI support, dashboard tools
✅ Success: 30+ KPIs tracking, 5+ dashboards live, CSAT > 75%

### 6. Kế Hoạch 12 Tháng (12-Month Roadmap Summary)

#### **Q1 2026 (Jan-Mar): FOUNDATION - Policies & Hires**
- ✅ Hire CMDB Admin (CRITICAL)
- ✅ RACI matrices all areas (Quick Win)
- ✅ SLA definitions IM/RM (Quick Win)
- ✅ PQA audit checklists (Quick Win)
- ✅ KPI framework defined
- ✅ CMDB policy & tool evaluation
- **OC Progress:** OC1: 60%, OC2: 20%, OC3: 15%, OC4: 40%

#### **Q2 2026 (Apr-Jun): BUILD - Infrastructure**
- ✅ CMDB tool deployed, CI population starts
- ✅ Hire 3rd Party Management Lead
- ✅ Dashboards go-live (5+ areas)
- ✅ CSAT surveys launched
- ✅ Automation Phase 1 (Jira auto-routing)
- ✅ Audit preparation completed
- **OC Progress:** OC1: 80%, OC2: 50%, OC3: 35%, OC4: 70%

#### **Q3 2026 (Jul-Sep): INTEGRATION - Cross-Process Workflows**
- ✅ CMDB integration with IM, CM, RM
- ✅ Automation expansion (priority, assignment)
- ✅ Training programs rollout
- ✅ First audit cycle completed
- ✅ 3rd Party VMS deployed
- **OC Progress:** OC1: 95%, OC2: 75%, OC3: 60%, OC4: 85%

#### **Q4 2026 (Oct-Dec): OPTIMIZATION - Continuous Improvement**
- ✅ Process optimization based on metrics
- ✅ Maturity reassessment
- ✅ Annual audits completed
- ✅ 2027 roadmap planning
- **OC Progress:** OC1: 100%, OC2: 90%, OC3: 75%, OC4: 95%

### 7. Nguồn Lực Cần Thiết (Resource Requirements)

#### **Nhân sự mới (New Hires):**
| Position | Timing | Priority | Estimated Cost | Justification |
|----------|--------|----------|----------------|---------------|
| **CMDB Admin/Steward** | Jan 2026 | 🔴 CRITICAL | $60-80K/year | Blocks OC2, affects all ITSM |
| **3rd Party Management Lead** | Apr 2026 | 🔴 CRITICAL | $60-80K/year | 19.4% maturity, vendor risk |
| **IM L2 Engineer** | Jun 2026 | 🟡 MEDIUM | $40-50K/year | Volume scaling, SLA support |
| **PQA Additional Auditor** | Q3 2026 | 🟢 LOW | $50-60K/year | Coverage 3%→80% |

**Total New Headcount: 2 must-have (Q1-Q2), 2 optional (Q3-Q4)**
**Year 1 Personnel Cost: $120-210K**

#### **Cross-functional Support:**
- BI/Analytics team: Dashboard development (Q1-Q2)
- Jira Admin: Automation configuration (Q2-Q3)
- DevOps team: CMDB-CI/CD integration (Q3)
- HR/L&D: Training programs (Q2-Q4)
- Infrastructure team: CMDB data population (Q2-Q4)

#### **Tools/Software Budget:**
| Tool | Cost/Year | Timing | Decision Maker |
|------|-----------|--------|----------------|
| CMDB Tool (ServiceNow/Jira Assets/Freshservice) | $20-50K | Q1 evaluation, Q2 deploy | CTO + IT Manager |
| VMS (Vendor Management System) | $10-20K | Q2 evaluation, Q3 deploy | Procurement + ITAM |
| Dashboard/BI tools | $0-10K | Q2 (may use existing Grafana) | BI Manager |

**Total Tools Budget: $30-80K/year**

#### **Training & Certification:**
- ITIL Foundation/Practitioner: 8 people × $500-1000 = $4-8K
- Tool training (CMDB, Jira automation): $2-5K
- External workshops/consultants: $10-20K
- **Total Training: $16-33K**

#### **Optional Consulting:**
- CMDB implementation support: $20-40K (if internal capacity insufficient)
- Process consulting (ITIL alignment): $10-20K
- **Total Consulting: $30-60K (one-time)**

### 8. ROI & Business Case

#### **Total Investment Year 1: $200-350K**
- Personnel: $120-210K (2-4 FTE)
- Tools: $30-80K
- Training: $16-33K
- Consulting (optional): $30-60K

#### **Expected Returns:**

**Cost Savings (Quantifiable):**
1. **Automation efficiency:** 60 hours/week manual work saved = **$150K/year**
2. **Reduced downtime:** 30% faster incident resolution = **$100K/year** (at $1000/hour downtime cost)
3. **Fewer failures:** CM CFR 5%→2% = 15 fewer failures × $2000 = **$30K/year**
4. **Vendor optimization:** Better 3rd party management = **$50K/year** (contract optimization, avoid vendor failures)

**Total Annual Savings: $330K/year**

**Payback Period: 9-12 months** (conservative estimate)

**Non-Quantifiable Benefits:**
- ✅ Compliance/audit readiness (avoid penalties, meet SOX/ISO)
- ✅ Risk mitigation (vendor failures, security incidents)
- ✅ Faster time-to-market (better CM/Release management)
- ✅ Higher quality (QC maturity, PQA effectiveness)
- ✅ Customer satisfaction (CSAT tracking, faster resolution)
- ✅ Team productivity (automation, clear processes)

### 9. Rủi Ro Chính & Biện Pháp (Key Risks & Mitigations)

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Hiring delays** (CMDB Admin) | HIGH | CRITICAL | Start hiring Dec 2025; Interim: repurpose Infrastructure team member |
| **Resource overload** (6.5 FTE for 7 initiatives) | HIGH | HIGH | Strict prioritization Q1; Use cross-functional support; Consider consultants |
| **Tool budget approval delays** | MEDIUM | HIGH | Build ROI case; Start with free tools (Jira Assets); Phased procurement |
| **Resistance to change** | MEDIUM | MEDIUM | Change management plan; Training programs; Executive sponsorship |
| **Integration complexity** | MEDIUM | MEDIUM | Phased rollout; API discovery Q1; Pilot IM-CM first |

### 10. Quyết Định Cần Thiết từ Ban Lãnh Đạo (Leadership Decisions Needed)

#### **Immediate (Dec 2025 - Jan 2026):**
1. ✅ **Approve hiring:** 2 new FTE (CMDB Admin Q1, 3rd Party Lead Q2)
2. ✅ **Approve budget:** $30-80K for tools (CMDB, VMS)
3. ✅ **Mandate priorities:** Teams focus on OC1-OC4 initiatives
4. ✅ **Executive sponsorship:** CTO/CIO to enforce change management
5. ✅ **Formalize IM Manager role:** Give authority to existing Mid Senior

#### **Q1 2026:**
6. ✅ Review and approve policies (CMDB, 3rd Party, PQA checklists)
7. ✅ Approve CMDB tool selection
8. ✅ Approve training budget and plan

#### **Ongoing:**
9. ✅ Monthly steering committee reviews (KPI dashboards)
10. ✅ Quarterly roadmap adjustments
11. ✅ Go/No-go decisions for Phase 2-3-4

### 11. Next Steps (Immediate Actions)

#### **Week 1 (Dec 9-13, 2025):**
- [ ] Present this report to Leadership Team
- [ ] Get approval for hiring and budget
- [ ] Post CMDB Admin job description
- [ ] Kick off RACI documentation working group

#### **Week 2-4 (Dec 16 - Jan 3, 2026):**
- [ ] Interview CMDB Admin candidates
- [ ] Start Quick Wins: SLA workshops, Change freeze calendar
- [ ] Form OC1-OC4 project teams
- [ ] Create detailed Q1 project plan

#### **January 2026:**
- [ ] Onboard CMDB Admin
- [ ] Execute Q1 roadmap (see detailed plan Section 5)
- [ ] Monthly progress review Jan 31

## PHẦN 2: ĐÁNH GIÁ HIỆN TRẠNG CHI TIẾT (DETAILED CURRENT STATE ASSESSMENT)

### 2.1. Change Management (CM) - 58.5% ⭐ Tốt Nhất

**Mức độ trưởng thành:** Level 2 (Managed) → Target Level 3 (Defined)

#### Điểm Mạnh:
- ✅ **Governance 94%:** Chính sách rõ ràng, CAB setup, tất cả stakeholders nắm rõ quy trình
- ✅ **Metrics 77%:** SLA tracking tốt, CFR < 5%, có dashboard theo dõi hàng tuần
- ✅ **Tools 70%:** Jira tracking 100%, audit trail đầy đủ, truy xuất tốt
- ✅ **Process 59.5%:** RFC template rõ ràng, PIR đã thực hiện, rollback rate thấp (1-2%)

#### Khoảng Trống & Findings:
- 🔴 **Compliance 0%:** Chưa có audit → **Finding CM-F3**
- 🔴 **Integration 21%:** RFC from Incident manual, chưa CMDB → **CM-F9, CM-F10**
- 🔴 **People 45%:** Training hạn chế, competency matrix chưa rõ → **CM-F18, CM-F19**
- 🔴 **Risk assessment chưa có framework** → **CM-F1**

**Nguồn Lực:** 1 Mid Senior (adequate)
**Quick Wins Q1:** Risk Framework, MW SLA, Freeze Calendar, RACI → 4 items

---

### 2.2. Request Management (RM) - 47.8% 🟡 Khá

**Mức độ trưởng thành:** Level 1.8 → Target Level 2 (55-65%)

#### Điểm Mạnh:
- ✅ **People 62.5%:** 3 FTE, training OK
- ✅ **Governance 58.3%:** 2 flows rõ, SLA defined

#### Khoảng Trống & Findings:
- 🔴 **Measurement 20.8%:** KHÔNG track volume, SLA%, cycle time → **RM-F1** (CRITICAL)
- 🔴 **CSAT 0%** → **RM-F2** (CRITICAL)
- 🟡 **Auto categorization 0%** → **RM-F4** (HIGH)
- 🟡 **Quality check 50%** → **RM-F5** (HIGH)

**Nguồn Lực:** 3 FTE (junior-heavy)
**Quick Wins Q1:** Metrics dashboard, Roles/approval, Auto-routing, Monthly review → 4 items

---

### 2.3. Incident Management (IM) - 44.3% 🟡 Khá

**Mức độ trưởng thành:** Level 1.8 → Target Level 3 (60-70%)

#### Điểm Mạnh:
- ✅ **Improvement 66.7%:** Review, RCA tốt
- ✅ **Process 50%:** Phân biệt Incident vs Request 100%

#### Khoảng Trống & Findings:
- 🔴 **Integration 16.7%:** Chưa CMDB → **IM-F1** (CRITICAL)
- 🔴 **Compliance 33.3%:** ITIL=0% → **IM-F2** (CRITICAL)
- 🔴 **Automation 20%:** Manual all → **IM-F3** (HIGH)
- 🔴 **SLA 25%:** Chưa define rõ → **IM-F5** (HIGH)
- 🔴 **IM Manager role chưa formal** → **IM-F4** (HIGH)

**Nguồn Lực:** 1.5 FTE (understaffed) + Need formalize IM Manager role
**Quick Wins Q1:** SLA P1-P4, Escalation path, RACI, KPI dashboard, Auto-priority → 5 items

---

### 2.4. Process QA (PQA) - 41.2% 🟡 Trung Bình

**Mức độ trưởng thành:** Level 2 Low → Target Level 2 High (50-65%)

#### Điểm Mạnh:
- ✅ **Governance 68.8%:** QA độc lập 100%, report CIO/CTO

#### Khoảng Trống & Findings:
- 🔴 **Metrics 13.6%:** Không KPI dashboard → **PQA-F5** (CRITICAL)
- 🔴 **Audit coverage 3%** (1/year, 1/30 processes) → **PQA-F3** (CRITICAL)
- 🔴 **Không audit checklist** CM/IM/PM/Config → **PQA-F2** (CRITICAL)
- 🔴 **Compliance 30%:** Không compliance checklist → **PQA-F4** (CRITICAL)
- 🔴 **Tools 37.5%:** Excel thủ công, chưa integrate ITSM → **PQA-F6** (CRITICAL)

**Nguồn Lực:** 1 Mid Senior (insufficient, coverage 3%, target 80%)
**Quick Wins Q1:** Audit checklists, QA database schema, RACI, Competency matrix → 4 items

---

### 2.5. Quality Control (QC) - 30.8% 🟠 Yếu

**Mức độ trưởng thành:** Level 1 → Target Level 2 (45-50%)

#### Điểm Mạnh:
- ✅ **Security 60%:** VA/Pentest định kỳ
- ✅ **CI/CD 98%:** Unit test at build

#### Khoảng Trống & Findings:
- 🔴 **Compliance 15%:** Không ITIL/ISO → **QC-FC07** (HIGH)
- 🔴 **Data & Tools 17.5%:** No automation strategy → **QC-FC05, FC06** (HIGH)
- 🔴 **Measurement 23%:** No metrics/KPI → **QC-FC03** (HIGH)
- 🔴 **Process 31%:** Test Planning unstandardized → **QC-FC02** (HIGH)
- 🔴 **Không QC Strategy** → **QC-FC01** (HIGH)

**Nguồn Lực:** QC team (size unclear)
**Quick Wins Q1:** Quality gate FAIL build, Formalize QC Policy, Defect triage weekly

---

### 2.6. CMDB - 9.3% 🔴 Nghiêm Trọng Nhất

**Mức độ trưởng thành:** Level 1 → Target Level 2 (45-60%)

#### Tình trạng CRITICAL:
- 🔴 **ALL dimensions < 25%**
- 🔴 **Tools 0%:** Excel only → **CMDB-F2** (CRITICAL)
- 🔴 **Integration 0%:** No IM/CM/RM integration → **CMDB-F9** (HIGH)
- 🔴 **Compliance 10%:** No audit trail → **CMDB-F5** (HIGH)
- 🔴 **People 25%:** 0 FTE dedicated → **CMDB-F15** (MEDIUM)
- 🔴 **Metrics 7.1%:** No KPIs → **CMDB-F8** (MEDIUM)
- 🔴 **No policy, no CI process, no steward** → **CMDB-F1, F3, F6, F7** (CRITICAL)

**Nguồn Lực:** **0 FTE** - NGHIÊM TRỌNG
**CRITICAL Action:** HIRE CMDB Admin Q1 (Week 1)
**Quick Wins Q1:** Policy, Steward/CI Owners, CI Classification, Tool evaluation

---

### 2.7. 3rd Party Management - 19.4% 🔴 Rất Yếu

**Mức độ trưởng thành:** Level 1 → Target Level 2 (45-60%)

#### Khoảng Trống & Findings:
- 🔴 **Tools 14%:** Không VMS → **3P-F2** (CRITICAL)
- 🔴 **Measurement 8%:** Không KPI/metric → **3P-F5** (CRITICAL)
- 🔴 **Process 28%:** Evaluation ad-hoc, no RFP/RFQ → **3P-F3** (CRITICAL)
- 🔴 **Integration 10%:** Vendor incidents không ITSM → **3P-F8** (CRITICAL)
- 🔴 **Compliance 25%:** Không enforce ISO/SOC2 → **3P-F4** (CRITICAL)
- 🔴 **No policy** → **3P-F1** (CRITICAL)

**Nguồn Lực:** **0 FTE** - NGHIÊM TRỌNG
**CRITICAL Action:** HIRE 3rd Party Lead Q2
**Quick Wins Q1:** Policy, Risk framework, RFP template, Compliance checklist

---

## PHẦN 3: KẾ HOẠCH TRIỂN KHAI 12 THÁNG CHI TIẾT
### DETAILED 12-MONTH IMPLEMENTATION ROADMAP

### 3.1. Q1 2026 (Jan-Mar): PHASE 1 - FOUNDATION

**Objective Progress Target:** OC1: 60% | OC2: 20% | OC3: 15% | OC4: 40%

#### **JANUARY 2026 - Foundation Month**

| # | Activity | Owner | Findings Addressed | OC Mapping | Effort | Resources Needed |
|---|----------|-------|-------------------|------------|--------|------------------|
| 1.1 | **HIRE CMDB Admin** | HR + IT Manager | CMDB-F15, CMDB-ALL | OC2 | HIGH | $60-80K/year |
| 1.2 | **RACI Matrices All Areas** (CM, IM, RM, PQA, QC) | All Leads | PQA-F1, CM-F7, IM-F4, RM-F3, QC-OC02 | OC1 | LOW (2w) | Internal effort |
| 1.3 | **SLA Workshops IM/RM** (P1-P4 definition) | IM/RM Leads + Service Mgr | IM-F5, RM-F3 | OC1 | MED (2w) | Workshops |
| 1.4 | **PQA Audit Checklists** (CM, IM, Config, PM) | PQA Lead | PQA-F2 | OC1 | MED (2w) | ITIL/ISO templates |
| 1.5 | **Change Freeze Calendar 2026** | CM Lead | CM-F14 | OC1 | LOW (1w) | None |
| 1.6 | **KPI Framework Kickoff** | All Leads + BI | PQA-F5, QC-FC03, RM-F1, IM-F6, 3P-F5 | OC4 | MED (start) | BI support |
| 1.7 | **Formalize IM Manager Role** | Head IT Ops + HR | IM-F4 | OC1 | LOW (title) | No cost |

**Deliverables End-Jan:** 7 RACI matrices, SLA approved, 4 audit checklists, Freeze calendar, KPI framework draft

---

#### **FEBRUARY 2026 - Policy & Design Month**

| # | Activity | Owner | Findings Addressed | OC Mapping | Effort | Resources Needed |
|---|----------|-------|-------------------|------------|--------|------------------|
| 2.1 | **CMDB Policy Document** | CMDB Admin | CMDB-F1 | OC2 | MED (2w) | Internal |
| 2.2 | **CMDB Tool Evaluation** | CMDB Admin + Infra | CMDB-F2 | OC2 | HIGH (3w) | Vendor demos |
| 2.3 | **Compliance Checklists** (All areas) | PQA + Compliance | PQA-F4, CM-F3, QC-FC07 | OC1 | MED (2w) | ISO/ITIL standards |
| 2.4 | **Risk Assessment Framework** (CM) | CM Lead + CAB | CM-F1 | OC1 | MED (2w) | Workshop |
| 2.5 | **KPI Finalization** (30+ KPIs defined) | All Leads + BI | Multiple findings | OC4 | MED (2w) | BI support |
| 2.6 | **Monthly Review Setup** (IM, RM) | IM/RM Leads | RM-F7 | OC4 | LOW (1w) | Calendar setup |
| 2.7 | **3rd Party Policy Draft** | Governance | 3P-F1 | OC1 | MED (2w) | Procurement input |
| 2.8 | **Post 3rd Party Lead Job** | HR | 3P-ALL | OC1 | LOW (1w) | HR support |

**Deliverables End-Feb:** CMDB policy, tool evaluation report, compliance checklists, risk framework, 30+ KPIs defined

---

#### **MARCH 2026 - Preparation for Build Phase**

| # | Activity | Owner | Findings Addressed | OC Mapping | Effort | Resources Needed |
|---|----------|-------|-------------------|------------|--------|------------------|
| 3.1 | **CMDB Tool Selection & Procurement** | CMDB Admin + Procurement | CMDB-F2 | OC2 | MED (2w) | Budget $20-50K |
| 3.2 | **CSAT Survey Design** (IM, RM) | IM/RM Leads | RM-F2, IM-F6 | OC4 | MED (2w) | Survey platform |
| 3.3 | **Automation Rules Design** (Jira) | Jira Admin + IM/RM | IM-F3, RM-F4 | OC3 | HIGH (3w) | Jira Admin time |
| 3.4 | **Dashboard Mockups** (IM, RM, CM, PQA) | BI + Leads | Multiple findings | OC4 | HIGH (3w) | BI team |
| 3.5 | **CI Classification & Naming Convention** | CMDB Admin + Infra | CMDB-F3 | OC2 | MED (2w) | Infra team |
| 3.6 | **Assign CMDB Steward & CI Owners** | CMDB Admin + IT Mgr | CMDB-F6, F7 | OC2 | LOW (1w) | None |
| 3.7 | **QC Policy Formalization** | QC Lead + PQA | QC-FC01, QC-OC01 | OC1 | MED (2w) | Internal |
| 3.8 | **Q1 Review & Q2 Planning** | All Leads | - | ALL OC | MED (1w) | Workshop |

**Deliverables End-Q1:** Tool selected & procured, CSAT ready, Automation designed, Dashboards mockups, CI framework, Q2 plan

**Q1 Success Metrics:**
- ✅ 7 policy documents published
- ✅ 7 RACI matrices approved
- ✅ SLA definitions approved (IM, RM)
- ✅ 30+ KPIs defined
- ✅ CMDB Admin onboarded
- ✅ CMDB tool selected
- ✅ 3rd Party Lead job posted
- ✅ Audit checklists ready

---

### 3.2. Q2 2026 (Apr-Jun): PHASE 2 - BUILD INFRASTRUCTURE

**Objective Progress Target:** OC1: 80% | OC2: 50% | OC3: 35% | OC4: 70%

#### **APRIL 2026 - Build Phase Start**

| # | Activity | Owner | Findings Addressed | OC Mapping | Effort | Resources Needed |
|---|----------|-------|-------------------|------------|--------|------------------|
| 4.1 | **CMDB Tool Deployment** | CMDB Admin + Vendor + DevOps | CMDB-F2 | OC2 | HIGH (4w) | Vendor support |
| 4.2 | **CI Data Population Starts** | CMDB Admin + Infra | CMDB-F3 | OC2 | ONGOING | Infra team time |
| 4.3 | **Dashboard Development** (5+ areas) | BI Team | Multiple findings | OC4 | HIGH (4w) | BI team |
| 4.4 | **Jira Automation Implementation Phase 1** | Jira Admin + IM/RM | IM-F3, RM-F4 | OC3 | HIGH (3w) | Jira Admin |
| 4.5 | **Interview 3rd Party Lead Candidates** | HR + Hiring Mgr | 3P-F15 | OC1 | MED (2w) | HR support |
| 4.6 | **MW Policy & SLA** (CM) | CM Lead + IT Ops | CM-F13 | OC1 | MED (2w) | Workshop |
| 4.7 | **Defect Triage Ceremony Setup** (QC) | QC Lead | QC-FC08 | OC3 | LOW (1w) | None |

**Deliverables End-Apr:** CMDB deployed, CI data 20% populated, Dashboards 50% done, Automation 30% done

---

#### **MAY 2026 - Infrastructure Buildout**

| # | Activity | Owner | Findings Addressed | OC Mapping | Effort | Resources Needed |
|---|----------|-------|-------------------|------------|--------|------------------|
| 5.1 | **CI Data Population Continues** (Target: 50%) | CMDB Admin + Infra | CMDB-F3 | OC2 | ONGOING | Infra team |
| 5.2 | **Dashboards Go-Live** (IM, RM, CM, PQA, QC) | BI + Leads | Multiple findings | OC4 | MED (2w) | BI team |
| 5.3 | **CSAT Launch** (IM, RM) | IM/RM Leads | RM-F2, IM-F6 | OC4 | LOW (1w) | Survey tool |
| 5.4 | **3rd Party Lead Onboarding** | HR + 3P Lead | 3P-ALL | OC1 | MED (2w) | Onboarding |
| 5.5 | **Automation Testing** (Jira) | Jira Admin + QA | IM-F3, RM-F4 | OC3 | MED (2w) | QA support |
| 5.6 | **PQA Q2 Audit Cycle Kickoff** | PQA Lead | PQA-F3 | OC1 | ONGOING | PQA time |
| 5.7 | **KB Top Incidents** (IM) | IM Mgr + L2/L3 | IM-F8 | OC3 | MED (4w) | IM team |

**Deliverables End-May:** CI 50%, Dashboards live, CSAT operational, 3P Lead onboarded, Automation testing

---

#### **JUNE 2026 - Q2 Completion & Integration Prep**

| # | Activity | Owner | Findings Addressed | OC Mapping | Effort | Resources Needed |
|---|----------|-------|-------------------|------------|--------|------------------|
| 6.1 | **CI Relationship Mapping** | CMDB Admin + Architect | CMDB-F4 | OC2 | HIGH (3w) | Architect time |
| 6.2 | **Automation Go-Live Phase 1** (IM/RM routing) | Jira Admin | IM-F3, RM-F4 | OC3 | MED (phased) | Support plan |
| 6.3 | **3rd Party VMS Evaluation** | 3P Lead + Procurement | 3P-F2 | OC1 | HIGH (4w) | Vendor demos |
| 6.4 | **Audit Preparation** (Audit readiness check) | PQA + Compliance | Multiple findings | OC1 | MED (2w) | Compliance team |
| 6.5 | **High-Risk Approval Workflow** (CM) | CM Lead + Jira Admin | CM-F1 | OC3 | MED (2w) | Jira config |
| 6.6 | **Quality Gate FAIL Build** (QC) | QC Lead + DevOps | QC-FC09 | OC3 | MED (2w) | DevOps time |
| 6.7 | **Q2 Review & Adjustments** | All Leads | - | ALL OC | MED (1w) | Workshop |

**Deliverables End-Q2:** CI 60%, relationships mapped, Automation Phase 1 live, VMS evaluated, Audit ready

**Q2 Success Metrics:**
- ✅ CMDB tool deployed, 60% CIs populated
- ✅ 5+ dashboards operational
- ✅ CSAT surveys collecting data
- ✅ Automation Phase 1 (30% processes)
- ✅ 3rd Party Lead hired & onboarded
- ✅ Audit readiness 80%

---

### 3.3. Q3 2026 (Jul-Sep): PHASE 3 - INTEGRATION & OPTIMIZATION

**Objective Progress Target:** OC1: 95% | OC2: 75% | OC3: 60% | OC4: 85%

#### **Key Activities Q3:**

| # | Activity | Owner | Findings Addressed | OC Mapping | Effort | Resources Needed |
|---|----------|-------|-------------------|------------|--------|------------------|
| 7.1 | **CMDB-IM Integration** | CMDB + IM + DevOps | IM-F1, CMDB-F9 | OC2, OC3 | HIGH (4w) | DevOps team |
| 7.2 | **CMDB-CM Integration** | CMDB + CM + DevOps | CM-F10, CMDB-F9 | OC2, OC3 | HIGH (4w) | DevOps team |
| 7.3 | **CMDB-RM Integration** | CMDB + RM + DevOps | RM-F8, CMDB-F9 | OC2, OC3 | MED (3w) | DevOps team |
| 7.4 | **Automation Expansion Phase 2** (Priority, Assignment) | Jira Admin + All | IM-F3, RM-F4 | OC3 | HIGH (6w) | Jira Admin |
| 7.5 | **Training Programs Rollout** (ITIL, Tools) | L&D + Leads | CM-F18, IM-F7, Multiple | OC3 | HIGH (8w) | L&D + Budget |
| 7.6 | **First Audit Cycle Execution** | PQA + External Auditor | PQA-F3, CM-F3, Multiple | OC1 | HIGH (6w) | Audit firm |
| 7.7 | **3rd Party VMS Deployment** | 3P Lead + IT Ops | 3P-F2 | OC1 | HIGH (6w) | VMS vendor |
| 7.8 | **CI Data Population Complete** (Target: 80%) | CMDB Admin + Infra | CMDB-F3 | OC2 | ONGOING | Infra team |
| 7.9 | **Test Automation Strategy** (QC) | QC Lead | QC-FC05 | OC3 | HIGH (4w) | QC team |

**Q3 Success Metrics:**
- ✅ CMDB integrated with 3 processes (IM, CM, RM)
- ✅ Automation rate 50%+
- ✅ First audit completed, findings < 10 major
- ✅ Training completion > 70%
- ✅ VMS deployed
- ✅ CI data 80% complete

---

### 3.4. Q4 2026 (Oct-Dec): PHASE 4 - CONTINUOUS IMPROVEMENT

**Objective Progress Target:** OC1: 100% | OC2: 90% | OC3: 75% | OC4: 95%

#### **Key Activities Q4:**

| # | Activity | Owner | Findings Addressed | OC Mapping | Effort | Resources Needed |
|---|----------|-------|-------------------|------------|--------|------------------|
| 8.1 | **Process Optimization Based on Metrics** | All Leads | Multiple findings | OC3 | ONGOING | Analytics |
| 8.2 | **Maturity Reassessment** (All 7 areas) | PQA + External | ALL | ALL OC | MED (3w) | Assessment tool |
| 8.3 | **Annual Compliance Audits** | PQA + Compliance + External | OC1 findings | OC1 | HIGH (4w) | Audit firm |
| 8.4 | **Tool Refinements** (CMDB, Dashboards, Automation) | Tech Leads | Based on usage | OC2, OC4 | MED | Vendor support |
| 8.5 | **Automation Phase 3** (Advanced workflows) | Jira Admin + DevOps | OC3 | OC3 | MED (4w) | DevOps time |
| 8.6 | **2027 Roadmap Planning** | All Leads | - | Future | MED (3w) | Leadership input |
| 8.7 | **Year-End Reviews & Retrospectives** | All Teams | - | ALL OC | LOW (2w) | Workshop |
| 8.8 | **CI Data to 90%+, Lifecycle Mgmt** | CMDB Admin | CMDB-F12 | OC2 | ONGOING | Infra team |

**Q4 Success Metrics:**
- ✅ Overall ITSM maturity 55%+ (from 38%)
- ✅ All OC1-OC4 objectives 90%+ complete
- ✅ SLA compliance > 85%
- ✅ CSAT score > 75%
- ✅ Annual audits passed
- ✅ CI data 90%+, lifecycle managed
- ✅ 2027 roadmap approved

---

## PHẦN 4: RESOURCE PLANNING & GOVERNANCE

### 4.1. Hiring Plan & Justification

| Role | Timing | Justification | Impact if Not Hired | Budget |
|------|--------|---------------|---------------------|--------|
| **CMDB Admin** | Jan 2026 | Blocks OC2 entirely, affects all 6 areas integration | Roadmap delays 3-6 months, Excel CMDB continues | $60-80K |
| **3rd Party Lead** | Apr 2026 | 19.4% maturity, vendor risk, contract optimization | Vendor failures, cost overruns, compliance risk | $60-80K |
| **IM L2 Engineer** | Jun 2026 | 1.5 FTE for growing volume, SLA support | SLA breaches, team burnout, MTTA/MTTR increase | $40-50K |
| **PQA Auditor** | Q3 2026 | Coverage 3%→80% needs capacity | Audit coverage stays low, compliance risk | $50-60K |

**Total Year 1 Personnel: $120-210K (2 must-have, 2 optional)**

### 4.2. Cross-Functional Support Requirements

| Team | Support Needed | Timeline | Commitment |
|------|----------------|----------|------------|
| **BI/Analytics** | Dashboard development, KPI automation | Q1-Q2 | 0.3-0.5 FTE |
| **Jira Admin** | Automation configuration, workflow design | Q2-Q3 | 0.2-0.3 FTE |
| **DevOps** | CMDB-CI/CD integration, API development | Q3 | 0.3-0.5 FTE |
| **HR/L&D** | Training programs, hiring support | Q2-Q4 | 0.2 FTE |
| **Infrastructure** | CMDB data population, CI ownership | Q2-Q4 | 0.5 FTE |
| **Compliance** | Audit support, checklist validation | Q1-Q3 | 0.2 FTE |

### 4.3. Governance Structure

#### **Steering Committee (Monthly)**
- **Members:** CTO/CIO, IT Manager, ITSM Lead, PQA Lead
- **Purpose:** OC1-OC4 progress review, budget approvals, go/no-go decisions
- **Deliverable:** Monthly status dashboard

#### **Working Groups (Weekly/Bi-weekly)**
- **OC1 Working Group:** Policy & governance (Q1-Q2 focus)
- **OC2 Working Group:** CMDB implementation (Q1-Q4)
- **OC3 Working Group:** Process improvement & automation (Q2-Q4)
- **OC4 Working Group:** Metrics & dashboards (Q1-Q3)

#### **Decision Points & Escalation**
- **Week 4:** CMDB Admin hiring decision
- **Week 8:** CMDB tool selection approval
- **Month 3:** Q2 budget & resource commitment
- **Month 6:** Phase 3 integration go/no-go
- **Month 9:** 2027 roadmap & budget

---

## PHỤ LỤC A: GLOSSARY - THUẬT NGỮ (for Non-Technical Leadership)

- **ITSM (IT Service Management):** Quản lý Dịch vụ CNTT - Bộ quy trình và công cụ để quản lý các dịch vụ IT
- **CMDB (Configuration Management Database):** Cơ sở dữ liệu quản lý cấu hình - Lưu trữ thông tin tất cả thiết bị, ứng dụng, mối quan hệ
- **SLA (Service Level Agreement):** Thỏa thuận mức độ dịch vụ - Cam kết thời gian xử lý (ví dụ: P1 incident resolve trong 4h)
- **KPI (Key Performance Indicator):** Chỉ số đo lường hiệu suất - Metrics để đánh giá performance (ví dụ: MTTA, MTTR)
- **RACI Matrix:** Ma trận phân công trách nhiệm - Ai Responsible, Accountable, Consulted, Informed
- **Maturity Level:** Mức độ trưởng thành - Thang đo 1-5: 1=Ad-hoc, 2=Managed, 3=Defined, 4=Measured, 5=Optimizing
- **CFR (Change Failure Rate):** Tỷ lệ thất bại khi thay đổi - % changes gây sự cố
- **MTTA (Mean Time To Acknowledge):** Thời gian trung bình nhận biết sự cố
- **MTTR (Mean Time To Resolve):** Thời gian trung bình giải quyết sự cố
- **CI (Configuration Item):** Đơn vị cấu hình - Server, app, database, network device
- **CSAT (Customer Satisfaction):** Độ hài lòng khách hàng - Survey score
- **ITIL (Information Technology Infrastructure Library):** Bộ best practices cho ITSM
- **VMS (Vendor Management System):** Hệ thống quản lý nhà cung cấp

---

