# 📋 OBJECTIVE CHARTERS (OC)

**Format:** Executive Summary | 1 page per OC | PMBOK-aligned  
**Total:** 7 Objective Charters covering 75 key findings  
**Timeline:** Q1-Q4 2025 (12 months)  
**Total Budget Estimate:** $850K - $1,200K

---

## OBJECTIVE CHARTER: Request Fulfillment Management

**Charter ID:** `OC-RFM-001`  
**Owner:** Service Desk Manager | **Sponsor:** IT Director  
**Period:** Q1-Q2 2025 (6 tháng) | **Status:** Planning

---

### 1. BUSINESS CONTEXT

Hiện tại Request Fulfillment thiếu metrics tracking (0%), không đo CSAT, và không tích hợp ITSM. Dẫn đến không biết hiệu suất, không justify resources, và users không hài lòng (engagement 25%).

### 2. OBJECTIVE (SMART)

Thiết lập Request Fulfillment Management chuyên nghiệp với SLA compliance >90%, CSAT >4.0/5.0, và giảm 20% cycle time trong vòng 6 tháng thông qua metrics tracking, quality measurement và ITSM integration.

### 3. SCOPE

**✅ In Scope:**
- Setup dashboard tracking 5 KPIs (SLA %, cycle time, backlog, MTTR, CSAT)
- CSAT survey automation
- ITSM integration (Incident/Change/CMDB linkage)
- Monthly service review process
- Business service mapping (>75% coverage)

**❌ Out of Scope:**
- Service Catalog redesign
- Headcount tăng thêm >2 FTE

### 4. SUCCESS CRITERIA & METRICS

1. SLA compliance >90% (baseline: không đo)
2. CSAT score >4.0/5.0 với response rate >60%
3. Average cycle time giảm 20%
4. User engagement tăng từ 25% lên 70%
5. Business service mapping coverage >75%

### 5. RACI

| Role | Person/Team |
|------|-------------|
| **Sponsor** (Approver) | IT Director |
| **Accountable** (Single point) | Service Desk Manager |
| **Responsible** (Doers) | ITSM Specialist, BI Analyst |
| **Consulted** (Input) | Development Team, Infrastructure Team, Business Units |
| **Informed** (Updates) | All End Users, Management |

### 6. KEY MILESTONES

- 🏁 T1: Dashboard framework + KPI definitions approved
- 🏁 T2: CSAT survey live, first data collection
- 🏁 T3: ITSM integration design completed
- 🏁 T4: Service review process piloted
- 🏁 T5: User engagement campaign launched
- 🏁 T6: Business service mapping completed, full production

### 7. RESOURCES & BUDGET

- **Team Size:** 2-3 FTE (ITSM Specialist, BI Analyst, part-time support)
- **Budget:** Medium (~$50-100K cho tools + training)
- **Key Tools:** Power BI/Grafana, Survey tool (TypeForm/Google), ITSM platform

### 8. TOP RISKS & MITIGATION

**Risk 1:** User không participate CSAT survey (<30% response rate)  
- **Impact:** `HIGH`  
- **Mitigation:** Gamification, incentives, simplify survey (3 questions), follow-up campaigns

**Risk 2:** ITSM integration phức tạp, delay 2-3 tháng  
- **Impact:** `MEDIUM`  
- **Mitigation:** Phân giai đoạn (manual linking trước, auto sau), external consultant nếu cần

### 9. DEPENDENCIES

- ⚠️ ITSM platform phải có API/webhooks (critical)
- ⚠️ BI tool procurement approved by Finance
- ⚠️ Business Units provide service mapping input

### 10. FINDINGS ADDRESSED

6 findings (4 CRITICAL): Metrics not tracked, NO CSAT, Weak ITSM integration, NO service review, Weak user engagement, NO business service mapping

---

## OBJECTIVE CHARTER: Incident Management

**Charter ID:** `OC-IM-002`  
**Owner:** Incident Manager (new hire) | **Sponsor:** IT Director  
**Period:** Q1-Q3 2025 (9 tháng) | **Status:** Planning

---

### 1. BUSINESS CONTEXT

Incident Management hiện tại: không có IM role, không có SLA approved, escalation ad-hoc, 0% automation, không integrate với CMDB/Problem/Change, và không ITIL compliant. User complaints tăng 40% QoQ.

### 2. OBJECTIVE (SMART)

Xây dựng Incident Management process tuân thủ ITIL với P1 MTTR <4h (compliance >95%), P2 <8h (>90%), escalation compliance >95%, và automation rate >60% trong 9 tháng.

### 3. SCOPE

**✅ In Scope:**
- Hire/assign Incident Manager + define role
- SLA definition và approval (P1-P4)
- Formal escalation matrix
- Workflow automation (auto-create, assign, categorize)
- ITSM integration (Problem/Change/CMDB)
- ITIL compliance implementation

**❌ Out of Scope:**
- Major Incident Management (Phase 2)
- 24/7 support expansion

### 4. SUCCESS CRITERIA & METRICS

1. P1 MTTR <4h với compliance >95%
2. P2 MTTR <8h với compliance >90%
3. Escalation compliance >95%
4. Automation rate >60%
5. Incident-CMDB linkage >80%
6. ITIL compliance score >85%

### 5. RACI

| Role | Person/Team |
|------|-------------|
| **Sponsor** (Approver) | IT Director |
| **Accountable** (Single point) | Incident Manager (new role) |
| **Responsible** (Doers) | Service Desk Team, ITSM Specialist, DevOps (automation) |
| **Consulted** (Input) | Development Team, Infrastructure Team, Technical SMEs |
| **Informed** (Updates) | All End Users, Management, CAB |

### 6. KEY MILESTONES

- 🏁 T1: IM role hired/assigned, SLA approved by management
- 🏁 T2: Escalation matrix deployed, team trained
- 🏁 T3: Automation pilot (auto-create, assign) for 20% volume
- 🏁 T6: ITSM integration live, CMDB linkage operational
- 🏁 T9: ITIL compliance audit passed, full automation

### 7. RESOURCES & BUDGET

- **Team Size:** 1 Incident Manager + 3-5 support staff
- **Budget:** Medium-High (~$100-150K: IM salary + automation tools)
- **Key Tools:** ITSM platform với automation engine, Monitoring tools integration, CMDB

### 8. TOP RISKS & MITIGATION

**Risk 1:** Incident Manager role rejected by existing team (turf war)  
- **Impact:** `HIGH`  
- **Mitigation:** Clear charter, authority from IT Director, involve team in role design, quick wins

**Risk 2:** SLA targets không realistic, fail ngay từ đầu  
- **Impact:** `HIGH`  
- **Mitigation:** Baseline measurement 1 tháng trước khi set SLA, start với achievable targets, review quarterly

### 9. DEPENDENCIES

- ⚠️ Headcount approval cho Incident Manager (CRITICAL)
- ⚠️ ITSM platform automation capability
- ⚠️ CMDB phải có data accuracy >80% (dependency on Configuration Management OC)

### 10. FINDINGS ADDRESSED

6 findings (4 CRITICAL): IM role not defined, SLA not approved, Escalation ad-hoc, Automation 0%, ITSM integration 0%, ITIL compliance 0%

---

## OBJECTIVE CHARTER: Change Management

**Charter ID:** `OC-CM-003`  
**Owner:** Change Manager | **Sponsor:** CTO  
**Period:** Q1-Q4 2025 (12 tháng) | **Status:** Planning

---

### 1. BUSINESS CONTEXT

Change Management có 19 findings (nhiều nhất), bao gồm: không có risk assessment framework, không có backup policy, audit không systematic, CR template phức tạp, CAB governance yếu, và Change Failure Rate cao (15-20%).

### 2. OBJECTIVE (SMART)

Nâng Change success rate từ 80-85% lên >95%, giảm Emergency changes từ 18% xuống <10%, và đạt audit compliance >90% trong 12 tháng thông qua risk-based approach, formal governance và automation.

### 3. SCOPE

**✅ In Scope:**
- Risk assessment framework (scale 1-5) + escalation
- Data retention policy + backup procedure
- CM audit process (quarterly)
- CR template optimization (3 types)
- CAB governance (charter, criteria, cadence)
- RACI formal documentation
- Incident-Change linkage automation
- CMDB integration for impact analysis
- PIR automation with CI/CD
- Training + certification program

**❌ Out of Scope:**
- Full Standard Change automation library (Phase 2)
- Tool replacement (sử dụng ITSM platform hiện tại)

### 4. SUCCESS CRITERIA & METRICS

1. Change success rate >95% (baseline: 80-85%)
2. Emergency changes <10% (baseline: 18%)
3. CAB attendance >80%
4. PIR completion rate >90%
5. CMDB linkage >85%
6. Audit compliance score >90%
7. Team CM certification >70%

### 5. RACI

| Role | Person/Team |
|------|-------------|
| **Sponsor** (Approver) | CTO |
| **Accountable** (Single point) | Change Manager |
| **Responsible** (Doers) | Change Management Team (2-3 coordinators), CAB Members |
| **Consulted** (Input) | Development Team, DevOps, Infrastructure, PQA, Product Team |
| **Informed** (Updates) | All technical teams, Business stakeholders, Management |

### 6. KEY MILESTONES

- 🏁 T1: Risk framework approved, RACI published
- 🏁 T3: CAB charter signed, simplified CR templates live
- 🏁 T6: CMDB integration operational, communication plan deployed
- 🏁 T9: PIR automation with CI/CD, maintenance windows defined
- 🏁 T12: Training program completed, compliance audit passed

### 7. RESOURCES & BUDGET

- **Team Size:** 2-3 Change Coordinators full-time + CAB members part-time (5-7 people)
- **Budget:** High (~$150-200K: automation, training, audit)
- **Key Tools:** ITSM platform, CMDB, CI/CD integration, Dashboard/BI

### 8. TOP RISKS & MITIGATION

**Risk 1:** CAB meetings overhead, slow down changes (business complaints)  
- **Impact:** `MEDIUM`  
- **Mitigation:** Pre-screening by Change team, batch approval cho low-risk, emergency CAB only when needed, time-boxing meetings

**Risk 2:** CMDB data inaccurate (60-70%), impact analysis sai  
- **Impact:** `HIGH`  
- **Mitigation:** Parallel CMDB improvement (dependency), validation step before change, fallback to manual review

### 9. DEPENDENCIES

- ⚠️ CMDB accuracy improvement to >80% (from Configuration Management OC) - CRITICAL
- ⚠️ CAB members commitment (time allocation from their managers)
- ⚠️ CI/CD pipeline stability for PIR automation

### 10. FINDINGS ADDRESSED

19 findings (3 CRITICAL): Risk assessment missing, No backup/retention policy, No CM audit, Complex CR template, Weak CAB governance, No RACI, No CFR analysis, Manual Incident-Change link, No CMDB integration, etc.

---

## OBJECTIVE CHARTER: Configuration Management

**Charter ID:** `OC-CFG-004`  
**Owner:** CMDB Manager (new role) | **Sponsor:** CTO  
**Period:** Q2-Q4 2025 (9 tháng) | **Status:** Planning

---

### 1. BUSINESS CONTEXT

Configuration Management critical gaps: Không có CMDB policy, đang dùng Excel (!), không map relationships, không audit, không có ownership, và không integrate với IM/CM. Impact: Change impact analysis sai, Incident resolution chậm.

### 2. OBJECTIVE (SMART)

Triển khai CMDB tool chuyên nghiệp thay Excel với accuracy >95%, CI coverage >90%, relationship accuracy >90%, và integrate với IM/CM trong 9 tháng.

### 3. SCOPE

**✅ In Scope:**
- CMDB policy formal + approval
- CMDB tool selection + procurement + implementation
- CI classification schema + relationship types
- Top 20 critical services mapping (CI + relationships)
- CI ownership assignment (100%)
- CMDB Steward role + governance
- IM-CM-CMDB integration
- Auto-discovery implementation (servers, network, cloud)
- Quarterly audit process

**❌ Out of Scope:**
- Full enterprise architecture modeling (>100 services)
- Financial asset management integration

### 4. SUCCESS CRITERIA & METRICS

1. CMDB accuracy >95% (validated quarterly)
2. CI coverage >90% cho critical infrastructure
3. Relationship accuracy >90%
4. CI update timeliness <24h
5. Incident-CMDB linkage >80%
6. Change-CMDB impact analysis usage >85%
7. Auto-discovery coverage >70%

### 5. RACI

| Role | Person/Team |
|------|-------------|
| **Sponsor** (Approver) | CTO |
| **Accountable** (Single point) | CMDB Manager (new role) |
| **Responsible** (Doers) | Configuration Analysts (2-3), CMDB Steward |
| **Consulted** (Input) | All technical teams, Infrastructure, DevOps, Security, Network team |
| **Informed** (Updates) | Incident Management, Change Management, Problem Management, Management |

### 6. KEY MILESTONES

- 🏁 T4: CMDB policy approved, tool RFP issued
- 🏁 T5: Tool selected, procurement completed, initial data load from Excel
- 🏁 T6: Relationship mapping pilot (5 critical services), CI ownership assigned
- 🏁 T7: IM-CM integration deployed
- 🏁 T9: Auto-discovery operational, quarterly audit process live
- 🏁 T12: Full production with >95% accuracy

### 7. RESOURCES & BUDGET

- **Team Size:** 2-3 Configuration Analysts full-time + CMDB Manager
- **Budget:** High (~$200-300K: tool license $100K+, implementation, training)
- **Key Tools:** CMDB tool (ServiceNow/Jira Insight/iTop/Device42), Discovery tools, Integration adapters

### 8. TOP RISKS & MITIGATION

**Risk 1:** CMDB tool selection sai, không meet requirements sau khi mua  
- **Impact:** `CRITICAL`  
- **Mitigation:** Detailed RFP (50+ requirements), POC với 2-3 vendors, stakeholder review committee, phased payment

**Risk 2:** Data migration từ Excel: data dirty (50% accuracy), nhiều lỗi  
- **Impact:** `HIGH`  
- **Mitigation:** Data cleansing workshop 1 tháng trước migration, validation rules trong CMDB, accept phân giai đoạn (critical services first)

### 9. DEPENDENCIES

- ⚠️ CMDB tool budget approval ($100-200K) - CRITICAL
- ⚠️ Technical teams provide CI data và maintain ownership
- ⚠️ Monitoring tools APIs available for auto-discovery

### 10. FINDINGS ADDRESSED

11 findings (2 CRITICAL): No CMDB policy, Using Excel (!), No CI relationships mapping, No audit, No CI ownership, No CMDB Steward, No IM/CM integration, No data quality standards, No auto-population, Part-time team, No KPIs

---

## OBJECTIVE CHARTER: Process QA

**Charter ID:** `OC-PQA-005`  
**Owner:** PQA Lead | **Sponsor:** IT Director  
**Period:** Q1-Q4 2025 (12 tháng) | **Status:** Planning

---

### 1. BUSINESS CONTEXT

Process QA gần như không tồn tại: Không có audit checklists, audit yearly only (không đủ), coverage 3% (1/30 processes), metrics 10%, không escalation. Result: Process compliance unknown, risks không được phát hiện.

### 2. OBJECTIVE (SMART)

Xây dựng Process QA function từ 0 với audit coverage >30% (Year 1), quarterly audit cadence, metrics tracking >80%, và process compliance score average >85% trong 12 tháng.

### 3. SCOPE

**✅ In Scope:**
- Audit checklists cho 10 ITSM processes (IM, CM, PM, RFC, CMDB, SLM, CAB, 3PM, RFM, BCM)
- Quarterly audit schedule + execution
- Coverage expansion: 3% → 30% (Year 1) → 50% (Year 2)
- Metrics framework (15+ KPIs per process)
- Escalation matrix (Critical <7 days, High <30 days)
- Process maturity assessment model (CMMI Level 1-5)

**❌ Out of Scope:**
- Code quality audit (QC team)
- Security audit (Security team)
- Financial audit (Finance team)

### 4. SUCCESS CRITERIA & METRICS

1. Audit coverage >30% processes (baseline: 3%)
2. Quarterly audit on-time >95%
3. Critical findings resolution <7 days: 100%
4. High findings resolution <30 days: >90%
5. Process compliance average >85%
6. Metrics tracking coverage >80%
7. Process maturity tăng Level 2→3 (average)

### 5. RACI

| Role | Person/Team |
|------|-------------|
| **Sponsor** (Approver) | IT Director |
| **Accountable** (Single point) | PQA Lead |
| **Responsible** (Doers) | Process Auditors (2), Compliance Specialist |
| **Consulted** (Input) | All process owners (IM, CM, PM, etc.), ITSM Lead, External auditors |
| **Informed** (Updates) | Management, Audit Committee, Process teams |

### 6. KEY MILESTONES

- 🏁 T1: Audit checklists approved, escalation matrix published
- 🏁 T3: Q1 audit completed (IM, CM, PM) - 10% coverage
- 🏁 T6: Q2 audit completed (expand +3 processes) - 20% coverage
- 🏁 T9: Q3 audit + maturity assessment framework deployed
- 🏁 T12: Q4 audit + annual compliance report - 30% coverage achieved

### 7. RESOURCES & BUDGET

- **Team Size:** 2-3 PQA specialists (PQA Lead + 2 Auditors)
- **Budget:** Medium (~$80-120K: salaries, GRC tool optional, training)
- **Key Tools:** GRC tool (optional, có thể dùng Excel/SharePoint Year 1), Audit management platform, Dashboard

### 8. TOP RISKS & MITIGATION

**Risk 1:** Process owners resist audit, không cooperate (culture issue)  
- **Impact:** `HIGH`  
- **Mitigation:** Position audit as 'help not blame', management mandate, collaborative approach, quick wins showcase, training on value of audit

**Risk 2:** PQA team thiếu technical ITSM knowledge, audit không chất lượng  
- **Impact:** `MEDIUM`  
- **Mitigation:** Hire ITIL-certified auditors, continuous training, SME support cho từng audit, external consultant Year 1

### 9. DEPENDENCIES

- ⚠️ Management commitment và enforcement of audit findings
- ⚠️ Process owners allocate time for audits (2-4 hours/audit)
- ⚠️ Headcount approval cho PQA team (2-3 FTE)

### 10. FINDINGS ADDRESSED

6 findings (5 CRITICAL!): No audit checklists, Audit yearly only, Coverage 3%, Metrics 10%, No escalation, No maturity assessment

---

## OBJECTIVE CHARTER: 3rd Party Management

**Charter ID:** `OC-3PM-006`  
**Owner:** Vendor Manager (new role) | **Sponsor:** CFO / CTO  
**Period:** Q1-Q3 2025 (9 tháng) | **Status:** Planning

---

### 1. BUSINESS CONTEXT

3rd Party Management hoàn toàn ad-hoc: Không policy, không vendor classification, không SLA monitoring, không metrics, không risk assessment. Result: Vendor risks unknown, SLA breaches không phát hiện, contracts renewed mà không review performance.

### 2. OBJECTIVE (SMART)

Thiết lập formal 3PM framework với 100% vendors classified, Tier 1 SLA compliance >95%, vendor performance reviews on-time >90%, và giảm 25% vendor-related incidents trong 9 tháng.

### 3. SCOPE

**✅ In Scope:**
- 3PM Policy formal (approval by management)
- Vendor classification matrix (Tier 1/2/3 by criticality, spend, risk)
- Complete vendor inventory database
- SLA monitoring dashboard (automated data feed)
- Vendor performance scorecard (monthly for Tier 1, quarterly for Tier 2)
- Risk assessment templates + register
- RACI for 3PM activities

**❌ Out of Scope:**
- Contract negotiation (Procurement team)
- Vendor onboarding automation (Phase 2)
- Legal review (Legal team)

### 4. SUCCESS CRITERIA & METRICS

1. 100% vendors classified (Tier 1/2/3)
2. Tier 1 vendors SLA compliance >95%
3. Vendor performance review on-time >90%
4. High-risk vendors có mitigation plan: 100%
5. Vendor-related incidents giảm 25%
6. Contract renewal lead time -30%

### 5. RACI

| Role | Person/Team |
|------|-------------|
| **Sponsor** (Approver) | CFO / CTO (co-sponsor) |
| **Accountable** (Single point) | Vendor Manager (new role) |
| **Responsible** (Doers) | Contract Specialist, ITSM Lead (for SLA monitoring) |
| **Consulted** (Input) | Procurement, Legal, Finance, All technical teams using vendors |
| **Informed** (Updates) | Management, Business units, Audit Committee |

### 6. KEY MILESTONES

- 🏁 T1: 3PM Policy approved, complete vendor inventory (30-50 vendors expected)
- 🏁 T2: Vendor classification completed, validated by stakeholders
- 🏁 T3: SLA monitoring pilot for Tier 1 vendors (10-15 vendors)
- 🏁 T6: Full SLA monitoring operational, risk assessment completed
- 🏁 T9: Performance tracking live, quarterly reviews established

### 7. RESOURCES & BUDGET

- **Team Size:** 1-2 Vendor Managers (1 FTE, 1 part-time or shared with Procurement)
- **Budget:** Medium (~$60-100K: VM salary, vendor mgmt platform, training)
- **Key Tools:** Vendor management platform (Coupa/SAP Ariba/Gartner alternative), Contract repository, Dashboard

### 8. TOP RISKS & MITIGATION

**Risk 1:** Vendors không provide SLA data (contractual gap)  
- **Impact:** `HIGH`  
- **Mitigation:** Review contracts, add reporting clause at renewal, escalate to vendor management, manual collection interim

**Risk 2:** Too many vendors (>50) with limited resources (1-2 FTE)  
- **Impact:** `MEDIUM`  
- **Mitigation:** Prioritize Tier 1 (focus 80% effort), vendor consolidation strategy, automate data collection

### 9. DEPENDENCIES

- ⚠️ Contract repository accessible (Legal/Procurement)
- ⚠️ Vendor cooperation on SLA reporting
- ⚠️ Headcount approval for Vendor Manager role

### 10. FINDINGS ADDRESSED

6 findings (4 CRITICAL): No 3PM Policy, No vendor classification, No SLA monitoring, No vendor metrics, No risk assessment, No roles & authority

---

## OBJECTIVE CHARTER: Quality Control

**Charter ID:** `OC-QC-007`  
**Owner:** QC Lead | **Sponsor:** CTO / VP Engineering  
**Period:** Q1-Q4 2025 (12 tháng) | **Status:** Planning

---

### 1. BUSINESS CONTEXT

QC có 21 findings (nhiều nhất cùng CM): Không strategy, không test planning chuẩn, không metrics/KPIs, không đo test coverage, không automation strategy, chỉ 1 test environment (bottleneck), skill gap lớn (25-30% biết automation). Defect leakage cao 8-10%.

### 2. OBJECTIVE (SMART)

Transform QC từ ad-hoc thành systematic với test coverage >80%, automation coverage >60%, defect leakage <5%, và QC team automation skill từ 25% lên 70% trong 12 tháng thông qua QC strategy, automation framework và training program.

### 3. SCOPE

**✅ In Scope:**
- QC Strategy document (3-year roadmap)
- Test planning process standardization
- QC metrics dashboard (15+ KPIs)
- Test coverage tool + measurement
- Test automation framework (Selenium/Playwright/Cypress)
- Test data management process + masking
- ISO 29119 compliance gap analysis + roadmap
- Quality gates enforcement (6 gates)
- Test environment expansion (+1 environment minimum)
- QC training program (automation, performance, security)
- Defect triage weekly process

**❌ Out of Scope:**
- Full shift-left testing (Phase 2)
- Production monitoring & observability

### 4. SUCCESS CRITERIA & METRICS

1. Test coverage >80% (baseline: không đo)
2. Test automation coverage >60% (baseline: 10-15%)
3. Defect leakage <5% (baseline: 8-10%)
4. Test execution efficiency >90%
5. Regression automation >80%
6. QC team automation skill >70% (baseline: 25-30%)
7. ISO 29119 compliance gap <20%
8. Quality gate compliance >90%
9. Test environment availability >95%

### 5. RACI

| Role | Person/Team |
|------|-------------|
| **Sponsor** (Approver) | CTO / VP Engineering |
| **Accountable** (Single point) | QC Lead |
| **Responsible** (Doers) | Test Engineers (5-8), Automation Engineers (2-3) |
| **Consulted** (Input) | Development Team, DevOps, Product Team, Security Team |
| **Informed** (Updates) | End users, Product Management, Business stakeholders, Management |

### 6. KEY MILESTONES

- 🏁 T1-3: QC Strategy approved, metrics dashboard live, test planning standardized (Phase 1)
- 🏁 T4-6: Test coverage tool deployed, automation framework selected + pilot (Phase 2)
- 🏁 T7-9: Automation implementation (60% regression), +1 test environment deployed, performance baseline (Phase 3)
- 🏁 T10-12: ISO compliance roadmap, training program completed (70% team certified), continuous improvement (Phase 4)

### 7. RESOURCES & BUDGET

- **Team Size:** 5-8 QC engineers (2-3 automation specialists, 1 performance engineer)
- **Budget:** High (~$200-300K: automation tools, test environment, training, certifications)
- **Key Tools:** Test management (Jira/TestRail), Automation (Selenium/Playwright), Performance (JMeter/Gatling), Test data mgmt, Code coverage (SonarQube)

### 8. TOP RISKS & MITIGATION

**Risk 1:** Automation skill gap quá lớn (75% team không biết), training không kịp  
- **Impact:** `CRITICAL`  
- **Mitigation:** Intensive bootcamp (3 months), hire 1-2 automation experts, external consultants for framework setup, pair programming, realistic timeline (accept <60% nếu cần)

**Risk 2:** Chỉ 1 test environment - bottleneck nghiêm trọng, teams xung đột  
- **Impact:** `HIGH`  
- **Mitigation:** Prioritize +1 environment deployment (T7-T9), containerization (Docker), environment booking system, cloud-based test env

### 9. DEPENDENCIES

- ⚠️ Test environment infrastructure budget approved (~$50-100K)
- ⚠️ Development team cooperation on automation (code testability)
- ⚠️ SonarQube operational (hoặc tương đương) for coverage
- ⚠️ Training budget approved (~$30-50K)

### 10. FINDINGS ADDRESSED

21 findings (7 CRITICAL): No QC strategy, No test planning, No metrics/KPIs, No test coverage, No automation strategy, No test data mgmt, No international standards compliance, weak defect mgmt, weak quality gates, only 1 test env, và 11 findings khác

---

## OC SUMMARY TABLE

| Charter ID | Initiative | Owner | Duration | Budget | KPIs | Risks |
|------------|-----------|-------|----------|--------|------|-------|
| OC-RFM-001 | Request Fulfillment Management | Service Desk Manager | 6 tháng | Medium | 5 | 2 |
| OC-IM-002 | Incident Management | Incident Manager (new hire) | 9 tháng | Medium-High | 6 | 2 |
| OC-CM-003 | Change Management | Change Manager | 12 tháng | High | 7 | 2 |
| OC-CFG-004 | Configuration Management | CMDB Manager (new role) | 9 tháng | High | 7 | 2 |
| OC-PQA-005 | Process QA | PQA Lead | 12 tháng | Medium | 7 | 2 |
| OC-3PM-006 | 3rd Party Management | Vendor Manager (new role) | 9 tháng | Medium | 6 | 2 |
| OC-QC-007 | Quality Control | QC Lead | 12 tháng | High | 9 | 2 |

---

## DEPENDENCIES MATRIX

```
Configuration Management (CMDB) 
    ↓
├─ Incident Management (needs CMDB accuracy >80%)
├─ Change Management (needs CMDB for impact analysis)
└─ 3rd Party Management (needs CMDB for vendor CI tracking)

Process QA
    ↓
├─ All OCs (provides compliance audit)
└─ Continuous improvement feedback

ITSM Platform & Automation
    ↓
├─ Incident Management (automation workflows)
├─ Request Fulfillment (dashboard & CSAT)
└─ Change Management (PIR automation)
```

---

## CRITICAL SUCCESS FACTORS

### Phase Sequencing
1. **Q1 (Foundation):** Process QA, 3PM, IM/RFM governance setup
2. **Q2 (Infrastructure):** Configuration Management (CMDB) - CRITICAL BLOCKER
3. **Q3 (Integration):** IM-CM-CMDB integration + QC Automation
4. **Q4 (Maturity):** Compliance, training, continuous improvement

### Resource Requirements
- **New Hires:** 4-5 roles (Incident Manager, CMDB Manager, Vendor Manager, +1-2 automation engineers)
- **Budget:** $850K-$1.2M total over 12 months
- **Executive Time:** ~20% CTO/IT Director for sponsorship & decision making

### Risk Mitigation
- **CMDB tool selection:** Highest risk - needs careful RFP + POC
- **Skills gap (QC automation):** Training bootcamp + external consultants
- **Change resistance:** Strong change management + quick wins approach

---

**Document Owner:** ITSM Program Manager  
**Last Updated:** 2025-11-25  
**Version:** 2.0 (Executive Format)  
**Status:** Draft for Approval
