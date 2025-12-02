# BÁO CÁO ĐÁNH GIÁ HIỆN TRẠNG VÀ LỘ TRÌNH TRIỂN KHAI ITSM & QA

**Ngày báo cáo:** 02/12/2025
**Đối tượng:** Ban Lãnh Đạo
**Người thực hiện:** IT Service Management Team

---

## EXECUTIVE SUMMARY

### Tổng quan
Báo cáo này trình bày đánh giá toàn diện về mức độ trưởng thành (maturity) của các hoạt động ITSM và QA hiện tại, phân tích khoảng cách (gap) so với các tiêu chuẩn ngành, và đề xuất lộ trình triển khai chi tiết trong 12 tháng tới để đạt các mục tiêu chiến lược.

### Điểm chính
- **Tình trạng chung:** Các hoạt động ITSM đang ở giai đoạn **INITIAL đến MANAGED** (Level 1-2), với điểm số trung bình **20-58%**
- **Điểm mạnh:** Có quy trình cơ bản, công cụ Jira hoạt động tốt, governance framework sơ khai
- **Rủi ro quan trọng:** Thiếu compliance/audit, không có CMDB, integration yếu, thiếu metrics và KPIs
- **Nguồn lực:** Hiện có 6 FTE, thiếu nghiêm trọng 3-5 FTE để đạt mục tiêu Level 3
- **Đầu tư cần thiết:** 12 tháng tới cần 5-7 FTE bổ sung, ngân sách công cụ cho CMDB và VMS

---

## I. ĐÁNH GIÁ HIỆN TRẠNG THEO MỨC ĐỘ TRƯỞNG THÀNH

### 1.1. TỔNG QUAN MATURITY LEVELS

| **Mảng ITSM/QA** | **Điểm hiện tại** | **Level hiện tại** | **Mục tiêu 12M** | **Gap cần cải thiện** |
|------------------|-------------------|--------------------|-----------------|-----------------------|
| **Change Management (CM)** | 41.5/71 = **58.45%** | Level 2: MANAGED (đang tiến tới 3) | Level 3: DEFINED (60-75%) | +7-17% |
| **Incident Management (IM)** | 27.0/61 = **44.3%** | Level 1.8: LATE INITIAL | Level 3: DEFINED (60-70%) | +16-26% |
| **Request Management (RM)** | 44.0/92 = **47.83%** | Level 1: LATE INITIAL | Level 2: MANAGED (55-65%) | +7-17% |
| **Configuration Management (CMDB)** | 5/53 = **9.34%** | Level 1: INITIAL | Level 2: MANAGED (45-60%) | +36-51% |
| **Process Quality Assurance (PQA)** | 30.5/74 = **41.2%** | Level 2: MANAGED (LOW) | Level 2: MANAGED (HIGH) (50-65%) | +9-24% |
| **Quality Control (QC)** | 37.0/120 = **30.83%** | Level 1: INITIAL | Level 2: MANAGED (45-50%) | +14-19% |
| **3rd Party Management** | 9.5/50 = **19.4%** | Level 1: INITIAL | Level 2: MANAGED (45-60%) | +26-41% |

### 1.2. PHÂN TÍCH 8 KHÍA CẠNH QUẢN TRỊ

#### **A. Governance (Quản trị) - Trung bình: 35-50%**
**Điểm sáng:**
- CM có governance 94% (tốt nhất): Chính sách rõ ràng, CAB đã setup
- IM và RM có policy cơ bản, phân loại rõ ràng
- PQA độc lập, report trực tiếp CIO/CTO

**Vấn đề nghiêm trọng:**
- **RACI chưa chính thức** cho tất cả các mảng → trách nhiệm mơ hồ
- **Roles chưa rõ:** Incident Manager chưa có (IM), CMDB Steward chưa có (CMDB), Vendor Manager chưa có (3rd Party)
- **Escalation path ad-hoc**, không có quy trình leo thang chính thức
- CMDB và 3rd Party chưa có policy formal

**Khuyến nghị:**
- Q1 2026: Ban hành RACI matrix cho tất cả mảng ITSM
- Q1 2026: Bổ nhiệm các vai trò quan trọng (Incident Manager, CMDB Steward)
- Q1 2026: Thiết lập escalation path 3 cấp cho IM

---

#### **B. Process (Quy trình) - Trung bình: 30-55%**
**Điểm sáng:**
- CM có quy trình RFC rõ ràng, PIR được thực hiện, rollback rate thấp (1-2%)
- IM có quy trình end-to-end, phân biệt Incident vs Request tốt (100%)
- RM có 2 flows chính xác định, multiple submit channels

**Vấn đề nghiêm trọng:**
- **CM:** Không có Maintenance Window policy, risk framework yếu, freeze policy ad-hoc
- **IM:** SLA chưa formal (25%), escalation ad-hoc, workflow chưa automation
- **CMDB:** Không có formal CI identification process (16.7%), không track CI lifecycle
- **QC:** Test planning không chuẩn hóa, defect management không nhất quán
- **3rd Party:** Vendor evaluation ad-hoc (28%), không có RFP/RFQ standard

**Khuyến nghị:**
- Q1 2026: Xây dựng Risk Assessment Framework 5x5 cho CM
- Q1 2026: Định nghĩa SLA P1-P4 cho IM với Response/Diagnosis/Resolution time
- Q1 2026: Tạo CI identification và intake process cho CMDB
- Q2 2026: Chuẩn hóa Test Planning process và Defect Management cho QC
- Q1 2026: Xây dựng RFP/RFQ template cho 3rd Party Management

---

#### **C. Tools & Data (Công cụ và Dữ liệu) - Trung bình: 17-70%**
**Điểm sáng:**
- CM: Jira tracking 100%, audit trail đầy đủ, có khả năng truy xuất (70%)
- IM: Jira + Grafana dashboard đang hoạt động (40.9%)
- RM: Jira workflow OK với SLA alerts (54.2%)

**Vấn đề nghiêm trọng (CRITICAL):**
- **CMDB: 0%** - Hiện dùng Excel thủ công, không có CMDB tool chuyên dụng
- **3rd Party: 14%** - Không có VMS (Vendor Management System), hợp đồng scattered
- **QC: 17.5%** - Không có automation strategy, adoption chỉ 25-30%, không Test Data Management
- **PQA: 37.5%** - Sử dụng Excel thủ công, chưa tích hợp với ITSM
- **CM:** Chưa có quy định về data retention và backup policy
- **IM:** Không có automation cho routing/priority/ticket creation

**Khuyến nghị:**
- Q1-Q2 2026: **MUA/TRIỂN KHAI CMDB TOOL** - Ưu tiên số 1 (ServiceNow/Atlassian/Cherwell)
- Q1-Q2 2026: **ĐÁNH GIÁ VÀ CHỌN VMS** cho 3rd Party Management
- Q2 2026: Xây dựng Test Automation Strategy cho QC
- Q1 2026: Thiết kế QA Database schema và integration roadmap cho PQA
- Q1 2026: Xây dựng Data Retention Policy cho CM (1-3-5 năm theo tier)

---

#### **D. Integration (Tích hợp) - Trung bình: 10-43%**
**Vấn đề nghiêm trọng (CRITICAL):**
- **IM: 16.7%** - Chưa có CMDB, link issue thủ công, không auto-create
- **CMDB: 0%** - Không integrate với Incident, Change, hay bất kỳ ITSM process nào
- **CM: 21%** - Manual RFC from Incident, chưa có CMDB integration
- **3rd Party: 10%** - Vendor incidents không tracking trong ITSM
- **QC: 37%** - Chỉ 1 environment (dev/sit/uat không tách), build không fail on test fail

**Khuyến nghị:**
- Q3-Q4 2026: **Tích hợp CMDB với Incident và Change Management** (sau khi CMDB đã có data)
- Q2 2026: Thiết kế ITSM integration roadmap với CMDB scope
- Q2 2026: Configure quality gate để FAIL build khi tests fail (SonarQube)
- Q4 2026: Tích hợp Vendor incidents vào ITSM tracking
- Q1 2026: Xây dựng automation cho Incident-Change linkage

---

#### **E. Metrics & Measurement (Đo lường) - Trung bình: 8-50%**
**Vấn đề nghiêm trọng (CRITICAL):**
- **PQA: 13.6%** - CRITICAL: Chưa có KPI dashboard, không có trend analysis
- **RM: 20.8%** - CRITICAL: Không track volume, SLA%, cycle time, quality metrics
- **QC: 23%** - Không có metrics/KPI, không có reports, không dashboards
- **CMDB: 7.1%** - Không có KPIs để đo effectiveness (coverage, quality, usage)
- **3rd Party: 8%** - Chưa có KPI/metric vendor, dashboard = 0
- **IM: 50%** - Có dashboard Grafana nhưng chưa có KPI formal, CSAT = 0

**Điểm sáng:**
- **CM: 77%** - SLA tracking trong luồng CR, CFR < 5%, có Dashboard và đo lường hàng tuần

**Khuyến nghị:**
- Q1 2026: **Xác định bộ KPI chính cho tất cả mảng** (8-12 KPIs/mảng)
- Q1-Q2 2026: Xây dựng KPI Dashboards (IM, RM, CMDB, PQA, QC, 3rd Party)
- Q1 2026: Setup CSAT survey cho IM và RM
- Q2 2026: Thiết lập automated reporting và trend analysis
- Q1 2026: Tự động hóa dashboard CM để lấy dữ liệu theo thời gian chọn

**Bộ KPI đề xuất cho từng mảng:**
- **IM:** MTTA, MTTR, SLA%, FCR, Escalation Rate, Data Quality, CSAT
- **CM:** Change Success Rate, CFR, SLA%, Emergency Change %, CAB Effectiveness, Automation Rate
- **RM:** Volume, SLA%, Cycle Time, Quality Metrics, CSAT, Automation Rate
- **CMDB:** Coverage %, Data Accuracy %, CI Relationships %, Update Frequency, Usage Rate
- **PQA:** Audit Coverage %, Findings/Audit, CAPA Closure Rate, Review Frequency, Compliance Score
- **QC:** Test Coverage, Defect Density, Automation Rate, Test Execution Rate, Defect Leakage
- **3rd Party:** Vendor Performance Score, SLA%, Risk Score, Compliance Rate, Cost Optimization

---

#### **F. Compliance (Tuân thủ) - Trung bình: 10-50%**
**Vấn đề nghiêm trọng (CRITICAL):**
- **CM: 0%** - Chưa có audit, No audit checklist
- **IM: 0-33%** - ITIL compliance = 0%, audit trail yếu, chưa external audit
- **CMDB: 10%** - Không có audit trail, không track thay đổi
- **PQA: 30%** - Chưa có compliance checklist, không map với ISO/ITIL
- **QC: 15%** - Không ITIL/ISO, không audit, không traceability
- **3rd Party: 25%** - Chưa enforce ISO/SOC2 standards cho vendors

**Khuyến nghị:**
- Q1 2026: **Xây dựng Compliance Checklist cho tất cả mảng** (map với ITIL 4, ISO 20000, ISO 27001)
- Q1 2026: Thiết lập audit trail system cho CM, IM, CMDB
- Q1-Q2 2026: Lập kế hoạch internal audit định kỳ (quarterly)
- Q2 2026: Map ITIL 4 practices với quy trình hiện tại
- Q1 2026: Xây dựng compliance checklist cho vendor security (ISO/SOC2)

---

#### **G. People (Nguồn lực) - Trung bình: 25-62%**
**Điểm sáng:**
- **RM: 62.5%** - Team đủ nhân lực (3 FTE), có competency training, cross-training
- **IM: 50%** - Team engaged, blame-free culture
- **CM: 45%** - Team có kinh nghiệm

**Vấn đề nghiêm trọng:**
- **CMDB: 6.2%** - CMDB team part-time, không có dedicated resource
- **3rd Party: 25%** - Không có dedicated team, chưa có Vendor Manager
- **PQA: 50%** - Chưa có competence matrix cho auditor
- **Tất cả mảng:** Chưa có ITIL certification, training chủ yếu self-learning

**Phân tích nguồn lực hiện tại vs cần thiết:**

| **Mảng** | **Hiện có** | **Cần thiết (Level 3)** | **Gap** | **Ưu tiên tuyển** |
|----------|-------------|-------------------------|---------|-------------------|
| Change Management | 1 Mid Senior | 1 Senior + 0.5 FTE (part-time từ team khác) | 0.5 FTE | **Low** - Có thể xoay sở |
| Incident Management | 1 Mid Senior + 0.5 FTE part-time | 1 Senior IM Manager + 1 Junior | 0.5 FTE | **Medium** - Cần IM Manager formal |
| Request Management | 3 FTE (1 Last Junior, 2 Mid Junior) | 3-4 FTE | 0-1 FTE | **Low** - Đủ cho hiện tại |
| Process QA | 1 Mid Senior | 2 FTE (1 Senior + 1 Junior) | 1 FTE | **High** - Cần mở rộng audit |
| Configuration Management | **0 FTE** | 2 FTE (1 CMDB Admin + 1 Data Analyst) | **2 FTE** | **CRITICAL** - Không thể triển khai CMDB |
| 3rd Party Management | **0 FTE** | 1 FTE (Vendor Manager) | **1 FTE** | **High** - Rủi ro vendor cao |
| **TỔNG** | **6 FTE** | **11-12 FTE** | **5-6 FTE** | **Cần tuyển ngay 3-5 FTE trong Q1-Q2 2026** |

**Khuyến nghị:**
- **Q1 2026 (URGENT):**
  - Tuyển 1 CMDB Administrator (Mid-Senior level)
  - Tuyển 1 Vendor Manager
  - Tuyển 1 PQA Junior Auditor
- **Q2-Q3 2026:**
  - Bổ nhiệm Incident Manager (promote internal hoặc hire external)
  - Tuyển 1 CMDB Data Analyst
- **Q1-Q4 2026:**
  - ITIL 4 Foundation training cho toàn bộ ITSM team (10-15 người)
  - ITIL 4 Specialist training cho key roles (5-7 người)
  - Xây dựng competency matrix cho tất cả vị trí

---

#### **H. Improvement (Cải tiến) - Trung bình: 16-66%**
**Điểm sáng:**
- **IM: 66.7%** - Review, RCA, action tracking tốt

**Vấn đề:**
- **3rd Party: 17%** - Risk mitigation không documented
- **PQA: 35.7%** - Chưa có backlog cải tiến, các cải tiến rời rạc
- **RM: 37.5%** - Không review service định kỳ, bottleneck không identify formal
- **CMDB: 4.2%** - Không có improvement process

**Khuyến nghị:**
- Q1 2026: Thiết lập improvement backlog cho tất cả mảng
- Q2 2026: Quarterly service review meetings
- Q2 2026: Lessons learned sessions sau mỗi major incident/change
- Q3 2026: Continuous improvement process (retrospectives)

---

## II. KEY FINDINGS & CRITICAL GAPS

### 2.1. TOP 10 RỦI RO NGHIÊM TRỌNG (CRITICAL)

| **#** | **Rủi ro** | **Mảng** | **Ảnh hưởng** | **Hành động khắc phục** | **Timeline** |
|-------|-----------|---------|---------------|------------------------|-------------|
| 1 | **Không có CMDB tool chuyên dụng** | CMDB | Không biết impact của changes, không track dependencies, khó RCA | Mua và triển khai CMDB tool, populate 50% CIs trong 6 tháng | Q1-Q3 2026 |
| 2 | **Compliance audit = 0 cho tất cả mảng** | All | Rủi ro pháp lý, không pass external audit, không chứng minh tuân thủ | Xây dựng compliance checklist, internal audit quarterly | Q1 2026 |
| 3 | **ITSM integration = 0 (manual linking)** | IM, CM | Không truy xuất, MTTA/MTTR cao, effort cao, data không chính xác | Xây dựng ITSM integration roadmap, auto-linking | Q2-Q4 2026 |
| 4 | **Không có CMDB team (0 FTE dedicated)** | CMDB | Không thể triển khai CMDB, phụ thuộc part-time, không scale | Tuyển CMDB Administrator và Data Analyst | Q1 2026 |
| 5 | **Không có Vendor Manager (0 FTE)** | 3rd Party | Vendor risks không quản lý, SLA tracking manual, security gaps | Tuyển Vendor Manager, xây dựng policy | Q1 2026 |
| 6 | **SLA formal chưa có cho IM** | IM | Không có expectation rõ, khó prioritize, dễ bị phàn nàn | Define SLA P1-P4 với Response/Diagnosis/Resolution time | Q1 2026 |
| 7 | **Metrics dashboards = 0 cho 5/7 mảng** | RM, PQA, QC, CMDB, 3rd Party | Không đo được performance, không có data để quyết định | Xây dựng KPI dashboards cho tất cả mảng | Q1-Q2 2026 |
| 8 | **Risk assessment framework chưa có** | CM | Không phân loại rủi ro, tất cả CR theo luồng chung, có thể chậm | Tạo Risk Assessment 5x5 (Impact vs Likelihood) | Q1 2026 |
| 9 | **Automation = 0 cho IM** | IM | Manual routing/priority/creation → MTTA cao, dễ miss alert | Jira auto-routing, auto-priority, auto-notification | Q2-Q3 2026 |
| 10 | **Quality gate không thực thi** | QC | Bugs leak sang production, code quality không đảm bảo | Configure SonarQube để fail build khi tests fail | Q1 2026 |

### 2.2. QUICK WINS (Tuần 1-8 / Q1 2026)

**Các hành động có impact cao, effort thấp, có thể triển khai ngay:**

#### **Change Management (6 Quick Wins)**
1. **Risk Assessment Framework** - Xây thang đánh giá 5x5 (Low-Med effort, High impact) - CM Lead - Q1 2026
2. **Maintenance Window SLA** - Per-system window + 48h notification (Medium effort, High impact) - CM Lead - Q1 2026
3. **Change Freeze Calendar 2026** - Publish freeze dates, embed in Jira (Low effort, Medium impact) - CM Lead - Dec 2025
4. **High-Risk Approval Workflow** - Auto-escalate to CTO/Security/Business (Medium effort, High impact) - CM Lead - Q1 2026
5. **RACI Formal Document** - Matrix RACI per bước (Low effort, Medium impact) - CM Lead - Q1 2026
6. **RFC Template Simplification** - Remove redundant fields (Low-Med effort, Medium impact) - CM Lead - Q2 2026

#### **Incident Management (6 Quick Wins)**
1. **Định nghĩa SLA P1-P4** - 2-3 workshops, document & publish (Medium/2-3w, High impact) - IM Manager - Q1 2026
2. **Escalation path 3 cấp** - L1-L2-L3 triggers, authority, guideline (Low/1w, High impact) - Head IT Ops - Q1 2026
3. **RACI cho IM** - Liệt kê bước, gắn R/A/C/I (Low/1w, Medium impact) - IM Manager - Q1 2026
4. **Chốt bộ KPI IM** - 8-12 KPIs với dashboard (Medium/3-4w, High impact) - IM Manager - Q1-Q2 2026
5. **Auto-tag priority** - Rule Jira cho P1-P4 (Low-Med/2w, Medium-High impact) - Jira Admin - Q2 2026
6. **KB top incidents** - 10-20 incidents với workarounds (Medium/4w, Medium impact) - IM Manager - Q2 2026

#### **CMDB (5 Quick Wins)**
1. **CMDB Policy Charter** - Policy approved & communicated (Low/2-3 days, High impact) - Service Manager - Week 1-2
2. **CI Owner Assignment** - 100% critical CIs have owners (Low/1 day, High impact) - IT Manager - Week 1
3. **CI Classification & Naming** - Naming convention documented (Low/3-4 days, High impact) - Infra Team - Week 1-2
4. **Improve Excel CMDB Search** - Search time < 1 minute (Low/2-3 days, Medium impact) - CMDB Admin - Week 4-6
5. **CI Metrics Dashboard** - Monthly report generated (Low/2 days, Medium impact) - Data Analyst - Week 6-8

#### **Process QA (4 Quick Wins)**
1. **Backlog cải tiến** - Tracking system (Low, High impact) - PQA - Q1 2026
2. **Checklist Audit** - Cho IM, CM, PM, Config (Medium, High impact) - PQA - Jan 2026
3. **QA Database schema** - Design + integration roadmap (Medium, High impact) - PQA + Jira Admin - Jan 2026
4. **QA Charter & RACI** - Hoàn thiện và truyền thông (Low, High impact) - PQA - Jan 2026

#### **Quality Control (5 Quick Wins)**
1. **Configure quality gate** - Fail build when tests fail (Low/1w, High impact) - DevOps - Dec 2025
2. **Formalize QC Policy** - Document in Confluence (Low/2-3w, Medium impact) - QC Lead - Dec 2025
3. **RCA process documentation** - From incidents (Low/2-3w, Medium impact) - QC Team - Dec 2025
4. **Defect triage ceremony** - Weekly meeting (Low/1-2w, Medium impact) - QC Lead - Dec 2025
5. **Security testing schedule** - Document roadmap (Low/1w, Medium impact) - QC Lead - Dec 2025

#### **3rd Party Management (5 Quick Wins)**
1. **3rd party policy** - Scope, roles, process (Medium, Critical impact) - Governance - Jan 2026
2. **Compliance checklist** - ISO/SOC2 requirements (Low, Critical impact) - ANTT - Jan 2026
3. **RFP/RFQ template** - Standard template (Medium, High impact) - Procurement - Jan 2026
4. **Vendor KPI definition** - Scorecard (Medium, High impact) - ITAM - Jan 2026
5. **SLA monitoring process** - Escalation (Low, High impact) - IT Ops - Jan 2026

---

## III. LỘ TRÌNH TRIỂN KHAI 12 THÁNG (THEO 4 OBJECTIVES)

### 3.1. MAPPING VỚI OBJECTIVES

| **Objective** | **Mô tả** | **Các mảng liên quan** | **KPI đo lường** |
|---------------|-----------|----------------------|------------------|
| **OC1** | Thiết lập Framework quản trị ITSM với policies, roles, RACI và SLA | All areas | % policies approved, % roles assigned, RACI completion |
| **OC2** | Xây dựng CMDB chuẩn hóa | CMDB, CM, IM | CMDB coverage %, data accuracy %, integration % |
| **OC3** | Nâng cao mức độ trưởng thành - Cải thiện chất lượng, tăng tốc release, tiết kiệm chi phí | CM, IM, RM, QC | CFR, MTTR, cycle time, defect density, cost savings |
| **OC4** | Thiết lập key metrics dashboards, CSAT mechanism, monthly reviews | All areas | # dashboards live, CSAT score, review completion % |

### 3.2. ROADMAP CHI TIẾT THEO QUÝ

---

#### **Q1 2026: FOUNDATION & GOVERNANCE (Jan - Mar)**

**Mục tiêu:** Thiết lập nền tảng, chính sách, vai trò, và quick wins (OC1 + OC4 init)

**Tuyển dụng URGENT (Timeline: Jan 2026):**
- ✅ Tuyển CMDB Administrator (Mid-Senior) - Start Date: 15/01/2026
- ✅ Tuyển Vendor Manager - Start Date: 15/01/2026
- ✅ Tuyển PQA Junior Auditor - Start Date: 01/02/2026

**Hạng mục triển khai:**

| **#** | **Hạng mục** | **Mô tả** | **Owner** | **Nguồn lực** | **Finding liên quan** | **OC** | **Deliverable** | **Week** |
|-------|-------------|-----------|-----------|---------------|---------------------|--------|----------------|---------|
| **GOVERNANCE & POLICIES** |
| 1.1 | **Ban hành RACI Matrix** | Xây dựng RACI cho CM, IM, RM, CMDB, PQA | ITSM Lead | CM Lead, IM Manager, RM Lead, PQA Lead | CM #7, IM #4, All governance | OC1 | RACI approved & published | W1-2 |
| 1.2 | **Bổ nhiệm key roles** | Incident Manager, CMDB Steward | IT Manager | HR support | IM #3, CMDB #7 | OC1 | Job descriptions, assignments | W1 |
| 1.3 | **CMDB Policy Charter** | Define CI types, scope, roles, approval | Service Manager | CMDB Admin (new hire) | CMDB #1 | OC1, OC2 | CMDB policy v1.0 | W1-2 |
| 1.4 | **3rd Party Management Policy** | Scope, roles, vendor classification | Vendor Manager (new) | Governance, ITAM | 3PM #1 | OC1 | 3PM policy v1.0 | W2-4 |
| 1.5 | **PQA Charter & Scope** | Hoàn thiện roles, RACI, scope | PQA Lead | PQA team | PQA #1 | OC1 | PQA charter v2.0 | W1-2 |
| **PROCESS FRAMEWORK** |
| 1.6 | **IM SLA Definition P1-P4** | Workshop, define Response/Diagnosis/Resolution SLA | IM Manager | Service Manager, team leads | IM #5 | OC1, OC3 | SLA document approved | W2-4 |
| 1.7 | **CM Risk Assessment 5x5** | Impact vs Likelihood, H/M/L criteria | CM Lead | IT Governance, CAB | CM #1 | OC1, OC3 | Risk framework v1.0 | W3-6 |
| 1.8 | **Escalation Path 3 cấp (IM)** | L1-L2-L3 triggers, authority | Head IT Ops | IM Manager | IM #4 | OC1 | Escalation guideline | W2-3 |
| 1.9 | **CI Classification & Naming** | Naming convention, CI taxonomy | CMDB Admin | Infra Team | CMDB #3 | OC2 | CI classification v1.0 | W1-2 |
| 1.10 | **Maintenance Window Policy** | Per-system window, 48h notification | CM Lead | IT Ops | CM #13 | OC1, OC3 | MW policy v1.0 | W4-8 |
| **TOOLS & AUTOMATION** |
| 1.11 | **CMDB Tool Selection** | Evaluate ServiceNow/Atlassian/Cherwell | IT Architect | CMDB Admin, Procurement | CMDB #2 | OC2 | Tool selected, budget approved | W6-12 |
| 1.12 | **Quality Gate Config** | SonarQube fail build on test fail | DevOps | QC Lead | QC #9 | OC3 | Quality gate live | W1-2 |
| 1.13 | **Change Freeze Calendar 2026** | Publish freeze dates in Jira | CM Lead | Dev teams | CM #14 | OC1 | Freeze calendar published | W1 |
| **METRICS & DASHBOARDS** |
| 1.14 | **Define KPIs for all areas** | 8-12 KPIs per area | Each Lead | BI Team | All #6 metrics | OC4 | KPI definitions approved | W3-4 |
| 1.15 | **IM KPI Dashboard** | MTTA, MTTR, SLA%, FCR, Escalation | IM Manager | BI Team | IM #6 | OC4 | IM dashboard live | W6-8 |
| 1.16 | **RM Metrics Dashboard** | Volume, SLA%, Cycle time | RM Lead | BI Team | RM metrics | OC4 | RM dashboard live | W6-8 |
| 1.17 | **CSAT Survey Setup (IM, RM)** | Survey tool, process | Service Manager | IM/RM Leads | IM #6, RM measurement | OC4 | CSAT launched | W4-6 |
| **COMPLIANCE & AUDIT** |
| 1.18 | **PQA Audit Checklist** | For CM, IM, Config, PM | PQA Lead | PQA Junior (new) | PQA #2 | OC1 | Checklists approved | W4-8 |
| 1.19 | **Compliance Checklist (3PM)** | ISO/SOC2 requirements | ANTT | Vendor Manager | 3PM #4 | OC1 | Compliance checklist v1 | W2-4 |
| 1.20 | **Data Retention Policy (CM)** | 1-3-5 years retention by tier | IT Governance | CM Lead, Infra | CM #2 | OC1 | Data retention policy | W8-12 |
| **TRAINING & CHANGE MANAGEMENT** |
| 1.21 | **ITIL 4 Foundation Training** | 15 người ITSM team | HR | L&D, external trainer | All people gaps | OC1 | 15 certified | W8-12 |
| 1.22 | **Onboarding new hires** | CMDB Admin, Vendor Mgr, PQA Junior | ITSM Lead | HR, team leads | People gaps | OC1 | 3 onboarded | W1-4 |

**Deliverables cuối Q1:**
- ✅ 5 Policies approved (CMDB, 3PM, PQA, MW, Data Retention)
- ✅ RACI Matrix cho tất cả mảng
- ✅ 3 key roles assigned (IM Manager, CMDB Steward, Vendor Manager)
- ✅ SLA P1-P4 defined cho IM
- ✅ CMDB tool selected
- ✅ 3 dashboards live (IM, RM, CSAT)
- ✅ 20 quick wins completed
- ✅ 3 FTE mới onboarded
- ✅ 15 người ITIL certified

**Maturity improvement Q1:**
- CM: 58% → 60% (+2%)
- IM: 44% → 50% (+6%)
- RM: 48% → 52% (+4%)
- CMDB: 9% → 25% (+16% - foundation)
- PQA: 41% → 48% (+7%)
- QC: 31% → 38% (+7%)
- 3PM: 19% → 30% (+11%)

---

#### **Q2 2026: BUILD & INTEGRATE (Apr - Jun)**

**Mục tiêu:** Xây dựng CMDB, automation, integration roadmap (OC2 + OC3 + OC4)

**Tuyển dụng bổ sung (Timeline: Apr 2026):**
- ✅ Tuyển CMDB Data Analyst - Start Date: 01/04/2026

**Hạng mục triển khai:**

| **#** | **Hạng mục** | **Mô tả** | **Owner** | **Nguồn lực** | **Finding liên quan** | **OC** | **Deliverable** | **Month** |
|-------|-------------|-----------|-----------|---------------|---------------------|--------|----------------|---------|
| **CMDB IMPLEMENTATION** |
| 2.1 | **CMDB Tool Setup & Config** | Deploy CMDB tool dev env, config | IT Architect | CMDB Admin, DBA | CMDB #2 | OC2 | CMDB dev env live | M4 |
| 2.2 | **CMDB Pilot - Core CIs** | 20-30 core CIs (servers, DBs, apps) | CMDB Admin | Infra Team, ITAM | CMDB #3 | OC2 | 30 CIs with relationships | M4-5 |
| 2.3 | **CI Master Data Framework** | Data model, attributes, relationships | IT Architect | DBA, CMDB Data Analyst | CMDB data | OC2 | Data model v1.0 | M4-5 |
| 2.4 | **CI/CD Integration Design** | Auto-create CI after deploy | DevOps | IT Architect, CMDB Admin | CMDB #14 | OC2, OC3 | Integration spec v1.0 | M5-6 |
| **AUTOMATION & INTEGRATION** |
| 2.5 | **Jira SLA Automation (IM)** | Breach alerts, warning notifications | Jira Admin | IM Manager | IM #3 | OC3 | SLA automation live | M4-5 |
| 2.6 | **Auto-priority & routing (IM)** | Rule-based priority, auto-assignment | Jira Admin | IM Manager | IM #3 | OC3 | Auto-routing 70% tickets | M5-6 |
| 2.7 | **High-Risk Approval Workflow (CM)** | Auto-escalate to CTO/Security | CM Lead | Jira Admin | CM #4 | OC3 | Approval workflow live | M4-5 |
| 2.8 | **RFC Template Simplification** | Remove redundant fields | CM Lead | BI, Dev teams | CM #4 | OC3 | Template v2.0 | M5-6 |
| **PROCESS IMPROVEMENTS** |
| 2.9 | **Test Planning Process (QC)** | Standard template, timeline, approval | QC Lead | QC Team | QC #2 | OC3 | Test planning standard | M4-6 |
| 2.10 | **Defect Management Process** | Priority/severity matrix, SLA, workflow | QC Lead | Dev Lead | QC #8 | OC3 | Defect mgmt standard | M4-6 |
| 2.11 | **RFP/RFQ Standard (3PM)** | Template & evaluation criteria | Procurement | Vendor Manager | 3PM #3 | OC1 | RFP/RFQ template | M4-5 |
| 2.12 | **Vendor Evaluation Framework** | Risk assessment, scoring | Vendor Manager | ANTT, Compliance | 3PM process | OC1 | Evaluation framework | M5-6 |
| **METRICS & REPORTING** |
| 2.13 | **CM Dashboard Auto-refresh** | Date picker, auto-query | BI Team | CM Lead | CM #15 | OC4 | CM dashboard v2.0 | M5-6 |
| 2.14 | **PQA KPI Dashboard** | Audit coverage, findings, CAPA | PQA Lead | BI Team | PQA #5 | OC4 | PQA dashboard live | M5-6 |
| 2.15 | **QC Metrics Dashboard** | Coverage, defect density, automation | QC Lead | BI Team | QC #3 | OC4 | QC dashboard live | M5-6 |
| 2.16 | **3PM Vendor Scorecard** | Performance, SLA, risk scores | Vendor Manager | BI Team | 3PM #5 | OC4 | Vendor scorecard v1.0 | M6 |
| 2.17 | **Monthly KPI Review Meetings** | Review all dashboards, trends | ITSM Lead | All leads | OC4 | OC4 | Monthly review cadence | M4-6 |
| **DATA & QUALITY** |
| 2.18 | **IM Data Quality Rules** | Mandatory fields, standardize template | IM Manager | ITAM | IM #8 | OC3 | Data quality improved | M4-6 |
| 2.19 | **Knowledge Base Top 10 Incidents** | Workarounds, fixes | IM Manager | L2/L3 | IM #8 | OC3 | KB 10 articles | M5-6 |
| 2.20 | **PQA Database Schema** | Design + Jira integration | PQA Lead | Jira Admin, PQA Junior | PQA #6 | OC1 | Schema v1.0 | M5-6 |
| **COMPLIANCE & AUDIT** |
| 2.21 | **Internal Audit Plan Q2-Q4** | Audit schedule, scope | IT Governance | PQA Lead | PQA #3, CM #3 | OC1 | Audit plan approved | M4 |
| 2.22 | **ITIL 4 Compliance Self-Assessment** | Map practices to processes | Service Manager | All leads | IM #2, compliance | OC1 | Compliance gap report | M5-6 |
| 2.23 | **Audit Trail System Design** | For CM, IM, CMDB | IT Governance | Jira Admin | CM #3, IM #2, CMDB #5 | OC1 | Audit trail spec | M6 |
| **TRAINING** |
| 2.24 | **CMDB Training** | For CMDB Admin, Infra, ITAM | CMDB Admin | IT Team | CMDB #15 | OC2 | 10 trained | M5-6 |
| 2.25 | **Test Automation Training (QC)** | Selenium, API testing | External trainer | QC Team | QC #8 | OC3 | 5 trained | M5-6 |

**Deliverables cuối Q2:**
- ✅ CMDB tool deployed (dev), 30 core CIs populated
- ✅ IM automation 70% (SLA, priority, routing)
- ✅ CM high-risk approval workflow
- ✅ 5 dashboards live (CM, IM, RM, PQA, QC)
- ✅ CSAT mechanism live
- ✅ Monthly KPI reviews established
- ✅ RFP/RFQ template deployed
- ✅ Internal audit plan approved
- ✅ 1 FTE bổ sung (CMDB Data Analyst)

**Maturity improvement Q2:**
- CM: 60% → 63% (+3%)
- IM: 50% → 56% (+6%)
- RM: 52% → 58% (+6%)
- CMDB: 25% → 45% (+20% - pilot live)
- PQA: 48% → 54% (+6%)
- QC: 38% → 45% (+7%)
- 3PM: 30% → 42% (+12%)

---

#### **Q3 2026: INTEGRATE & SCALE (Jul - Sep)**

**Mục tiêu:** CMDB integration với ITSM, expand coverage, compliance audit (OC2 + OC3)

**Hạng mục triển khai:**

| **#** | **Hạng mục** | **Mô tả** | **Owner** | **Nguồn lực** | **Finding liên quan** | **OC** | **Deliverable** | **Month** |
|-------|-------------|-----------|-----------|---------------|---------------------|--------|----------------|---------|
| **CMDB EXPANSION** |
| 3.1 | **CMDB Data Population 50%** | 250-300 CIs, relationship mapping | CMDB Admin | ITAM, IT Ops, Data Analyst | CMDB #9 | OC2 | 50% assets in CMDB | M7-9 |
| 3.2 | **Jira-CMDB Integration** | Link RFCs to CIs, impact analysis | CM Lead | DevOps, CMDB Admin | CMDB #9, CM #10 | OC2, OC3 | 50 RFCs linked to CIs | M7-9 |
| 3.3 | **CI/CD Auto-create CI (Pilot)** | Auto-create CI after deploy (staging) | DevOps | IT Architect, CMDB | CMDB #8 | OC2, OC3 | 20% deploys auto-sync | M8-9 |
| 3.4 | **Service-to-CI Mapping** | Top 10 services dependencies | Solution Architect | Service Owners, CMDB | CMDB #4 | OC2 | 10 services mapped | M8-9 |
| **ITSM INTEGRATION** |
| 3.5 | **ITSM Integration Roadmap** | Design + CMDB scope | IT Architect | IM Manager, CM Lead | IM #1, integration | OC2, OC3 | ITSM roadmap v1.0 | M7 |
| 3.6 | **Incident-Change Linkage Auto** | Auto-link incidents with changes | CM Lead | IM Manager, DevOps, PQA | CM #9 | OC3 | 50% incidents auto-linked | M8-9 |
| 3.7 | **Incident-CMDB Linkage** | Auto-link incidents with CIs | IM Manager | CMDB Admin, Tool Admin | CMDB #14 | OC2, OC3 | 80% incidents linked | M8-9 |
| **AUTOMATION & OPTIMIZATION** |
| 3.8 | **Re-enable Sonar & CI/CD** | Quality validation for changes | DevOps | Security, CM Lead | CM #11 | OC3 | Sonar integrated | M7-8 |
| 3.9 | **Test Automation Strategy** | Roadmap, tool selection, ROI targets | QC Lead | QC Team | QC #5 | OC3 | Automation strategy | M7-8 |
| 3.10 | **Multiple Test Environments** | Dev, SIT, UAT separated | QC Lead | DevOps | QC #10 | OC3 | 3 environments live | M8-9 |
| **COMPLIANCE & AUDIT** |
| 3.11 | **Internal Audit Round 1 (CM)** | Compliance audit with checklist | IT Governance | PQA Lead, CM Lead | CM #3 | OC1 | Audit report 1 | M8 |
| 3.12 | **Audit Trail Implementation** | For CM, IM, CMDB | IT Governance | Jira Admin, Tool Admin | CM #3, IM #2, CMDB #5 | OC1 | Audit trail live | M8-9 |
| 3.13 | **ITIL 4 Gap Remediation** | Fix gaps from self-assessment | Service Manager | All leads | Compliance gaps | OC1 | Remediation plan | M7-9 |
| 3.14 | **Vendor Security Assessment** | ISO/SOC2 checks for critical vendors | Vendor Manager | ANTT, Compliance | 3PM #4 | OC1 | 80% vendors assessed | M7-9 |
| **PROCESS MATURITY** |
| 3.15 | **CAB Monthly Meetings** | Regular CAB with criteria | CM Lead | CAB members | CM #6 | OC1 | 3 CAB meetings held | M7-9 |
| 3.16 | **PIR Auto-trigger** | PIR after deployment | CM Lead | DevOps, VHUD | CM #12 | OC3 | PIR automation 60% | M8-9 |
| 3.17 | **Quarterly Vendor Reviews** | QBR for top vendors | Vendor Manager | Business Units | 3PM improvement | OC4 | QBR 30% vendors | M8-9 |
| 3.18 | **Knowledge Base Expansion** | 20-30 articles | IM Manager | L2/L3 | IM #8 | OC3 | KB 30 articles | M7-9 |
| **IMPROVEMENT & OPTIMIZATION** |
| 3.19 | **CFR Root Cause Analysis** | Top 3 root causes | CM Lead | Dev teams, PQA | CM #8 | OC3 | RCA report + plan | M7-8 |
| 3.20 | **Bottleneck Analysis (RM)** | Identify and fix bottlenecks | RM Lead | BI Team | RM improvement | OC3 | Bottleneck report | M8-9 |
| 3.21 | **PQA Quarterly Audit (Q3)** | Audit 2 areas (IM, Config) | PQA Lead | PQA Junior | PQA #3 | OC1 | 2 audit reports | M7-9 |
| **TRAINING** |
| 3.22 | **ITIL 4 Specialist Training** | 5-7 key roles | HR | External trainer | People gaps | OC1 | 5 specialist certified | M8-9 |
| 3.23 | **CM Competency Training** | CM deep-dive | CM Lead | L&D | CM #18 | OC1 | CM training completed | M7-9 |

**Deliverables cuối Q3:**
- ✅ CMDB 50% populated (250-300 CIs)
- ✅ Jira-CMDB integration live
- ✅ Incident-Change-CMDB linkage 50-80%
- ✅ 3 test environments deployed
- ✅ Internal audit round 1 completed
- ✅ Audit trail system live
- ✅ 30 KB articles published
- ✅ Vendor security assessment 80%
- ✅ 5 ITIL Specialist certified

**Maturity improvement Q3:**
- CM: 63% → 66% (+3%)
- IM: 56% → 62% (+6%)
- RM: 58% → 62% (+4%)
- CMDB: 45% → 60% (+15% - 50% data + integration)
- PQA: 54% → 58% (+4%)
- QC: 45% → 50% (+5%)
- 3PM: 42% → 55% (+13%)

---

#### **Q4 2026: STABILIZE & OPTIMIZE (Oct - Dec)**

**Mục tiêu:** CMDB 100%, advanced automation, reassessment, roadmap 2027 (OC2 + OC3 + OC4)

**Hạng mục triển khai:**

| **#** | **Hạng mục** | **Mô tả** | **Owner** | **Nguồn lực** | **Finding liên quan** | **OC** | **Deliverable** | **Month** |
|-------|-------------|-----------|-----------|---------------|---------------------|--------|----------------|---------|
| **CMDB COMPLETION** |
| 4.1 | **CMDB Data Population 100%** | 500-600 CIs, relationships complete | CMDB Admin | ITAM, IT Team, Data Analyst | CMDB #12 | OC2 | 100% assets, 99% accuracy | M10-12 |
| 4.2 | **CI/CD Automation Full Deploy** | All pipelines auto-sync CMDB | DevOps | CMDB Admin | CMDB #13 | OC2, OC3 | 95%+ deploys auto-sync | M10-12 |
| 4.3 | **Business Service Mapping** | 20-30 services with dependencies | Service Owners | IT Architect, CMDB | CMDB #15 | OC2 | 20+ services mapped | M10-12 |
| 4.4 | **CMDB Auto-update from Changes** | Change approvals update CMDB | CM Lead | Tool Admin, CMDB | CMDB #13 | OC2, OC3 | Auto-update 80% CRs | M11-12 |
| **ADVANCED AUTOMATION** |
| 4.5 | **Incident Auto-creation** | From monitoring alerts | IM Manager | DevOps, Grafana Admin | IM automation | OC3 | Auto-create 60% incidents | M10-11 |
| 4.6 | **Batch Approval (CM)** | Group changes by service | CM Lead | Architecture, Service Owners | CM #16 | OC3 | Batch approval pilot | M11-12 |
| 4.7 | **Test Automation 50% Coverage** | Automated regression tests | QC Lead | QC Team | QC automation | OC3 | 50% automation coverage | M10-12 |
| **COMPLIANCE & AUDIT** |
| 4.8 | **Internal Audit Round 2 (IM, RM)** | Compliance audit | IT Governance | PQA Lead | Compliance | OC1 | 2 audit reports | M10-11 |
| 4.9 | **Remediate Audit Findings** | Fix findings from Q3 & Q4 audits | All Leads | Teams | Audit findings | OC1 | Remediation 80% complete | M11-12 |
| 4.10 | **CMDB Compliance Audit** | Config compliance, unauthorized changes | IT Governance | CMDB Admin | CMDB #5 | OC1 | CMDB audit report | M12 |
| 4.11 | **VMS Compliance Tracking** | Vendor compliance automation | Vendor Manager | BI Team | 3PM compliance | OC1 | Compliance automation 80% | M10-12 |
| **METRICS & OPTIMIZATION** |
| 4.12 | **Risk Dashboard (CM)** | Risk trends, predictions | BI Team | CM Lead | CM metrics | OC4 | Risk dashboard live | M10-11 |
| 4.13 | **CMDB Metrics Dashboard** | Coverage, quality, usage | Data Analyst | CMDB Admin | CMDB #8 | OC4 | CMDB dashboard live | M11-12 |
| 4.14 | **3PM Performance Dashboard** | Vendor performance, SLA trends | Vendor Manager | BI Team | 3PM metrics | OC4 | 3PM dashboard live | M11-12 |
| 4.15 | **PQA Trend Analysis** | Findings trends, effectiveness | PQA Lead | BI Team | PQA #5 | OC4 | Trend analysis report | M11-12 |
| **PROCESS OPTIMIZATION** |
| 4.16 | **Continuous Improvement Backlog** | Systematic backlog for all areas | ITSM Lead | All leads | All improvement | OC3 | Backlog system live | M10 |
| 4.17 | **Quarterly Business Reviews** | Review with stakeholders | All Leads | Business Units | OC4 | OC4 | QBR Q4 completed | M12 |
| 4.18 | **Lessons Learned Repository** | Capture and share lessons | Service Manager | All teams | Improvement | OC3 | LL repository live | M10-12 |
| 4.19 | **Cost Optimization Analysis** | CMDB-based cost allocation | IT Ops | Finance, CMDB | CMDB #19 | OC3 | Cost report | M12 |
| **REASSESSMENT & PLANNING** |
| 4.20 | **Maturity Reassessment All Areas** | Re-score all 7 areas | ITSM Lead | All leads, PQA | All areas | OC1 | Maturity report 2026 | M12 |
| 4.21 | **PQA Annual Report** | Comprehensive yearly report | PQA Lead | PQA team | PQA #2 | OC1 | PQA annual report | M12 |
| 4.22 | **Roadmap 2027 Planning** | Next year strategy | ITSM Lead | All leads, IT Management | All areas | OC1 | Roadmap 2027 approved | M12 |
| 4.23 | **Competency Matrix & Hiring Plan** | Skills gaps, hiring needs | HR | ITSM Lead, team leads | People gaps | OC1 | 2027 hiring plan | M12 |
| **VENDOR MANAGEMENT** |
| 4.24 | **VMS Tool Deployment (if budget)** | Centralized vendor system | Vendor Manager | IT Ops, ITAM | 3PM #2 | OC2 | VMS pilot/live | M10-12 |
| 4.25 | **Critical Vendor Risk Plans** | Backup plans for critical vendors | Vendor Manager | Risk, Business Units | 3PM #7 | OC1 | Risk plans 100% critical | M11-12 |

**Deliverables cuối Q4:**
- ✅ CMDB 100% populated (500-600 CIs)
- ✅ CI/CD auto-sync 95%+
- ✅ Business service mapping 20+ services
- ✅ 4 internal audits completed (CM, IM, RM, CMDB)
- ✅ Audit findings 80% remediated
- ✅ 8 dashboards live (all areas)
- ✅ Test automation 50% coverage
- ✅ Maturity reassessment completed
- ✅ Roadmap 2027 approved
- ✅ VMS deployed (if budget approved)

**Maturity improvement Q4:**
- CM: 66% → 70% (+4%) - **Target Level 3 ACHIEVED**
- IM: 62% → 68% (+6%) - **Target Level 3 ACHIEVED**
- RM: 62% → 65% (+3%) - **Target Level 2 HIGH ACHIEVED**
- CMDB: 60% → 75% (+15%) - **Target Level 2 HIGH EXCEEDED**
- PQA: 58% → 63% (+5%) - **Target Level 2 HIGH ACHIEVED**
- QC: 50% → 53% (+3%) - **Target Level 2 ACHIEVED**
- 3PM: 55% → 65% (+10%) - **Target Level 2 HIGH ACHIEVED**

---

### 3.3. TỔNG KẾT ROADMAP 12 THÁNG

**Maturity Evolution:**

| **Mảng** | **Hiện tại** | **Q1** | **Q2** | **Q3** | **Q4** | **Tăng trưởng** | **Target achieved?** |
|----------|--------------|--------|--------|--------|--------|----------------|---------------------|
| CM | 58% | 60% | 63% | 66% | 70% | +12% | ✅ Level 3 (60-75%) |
| IM | 44% | 50% | 56% | 62% | 68% | +24% | ✅ Level 3 (60-70%) |
| RM | 48% | 52% | 58% | 62% | 65% | +17% | ✅ Level 2 High (55-65%) |
| CMDB | 9% | 25% | 45% | 60% | 75% | +66% | ✅ Level 2+ (45-60%+) |
| PQA | 41% | 48% | 54% | 58% | 63% | +22% | ✅ Level 2 High (50-65%) |
| QC | 31% | 38% | 45% | 50% | 53% | +22% | ✅ Level 2 (45-50%+) |
| 3PM | 19% | 30% | 42% | 55% | 65% | +46% | ✅ Level 2 High (45-60%+) |

**Key Milestones:**
- ✅ Q1: Foundation - 20 policies/frameworks, 3 FTE hired, 15 ITIL certified
- ✅ Q2: Build - CMDB tool deployed, 5 dashboards, automation 70%
- ✅ Q3: Integrate - CMDB 50%, ITSM integration, audit round 1
- ✅ Q4: Optimize - CMDB 100%, reassessment, roadmap 2027

**Investment Summary:**
- **Headcount:** 3 FTE Q1, 1 FTE Q2 = **4 FTE total hired**
- **Training:** 15 ITIL Foundation, 5 ITIL Specialist = **20 certified**
- **Tools:** CMDB tool, VMS tool (optional) = **2 major tools**
- **Dashboards:** 8 dashboards deployed = **100% areas covered**
- **Audits:** 4 internal audits = **100% major areas audited**

---

## IV. PHÂN TÍCH NGUỒN LỰC CHI TIẾT

### 4.1. YÊU CẦU NGUỒN LỰC THEO QUÝ

#### **Q1 2026 - URGENT HIRING**

| **Vị trí** | **Level** | **Báo cáo cho** | **Trách nhiệm chính** | **Yêu cầu năng lực** | **Start Date** | **Lý do critical** |
|-----------|-----------|----------------|----------------------|---------------------|----------------|-------------------|
| **CMDB Administrator** | Mid-Senior | IT Architect | CMDB tool setup, data population, CI management, integration | 3+ yrs CMDB/ITAM exp, ITIL 4 Foundation, SQL, API integration | 15/01/2026 | Không có = không thể triển khai CMDB (OC2 blocker) |
| **Vendor Manager** | Mid | IT Manager | 3rd party policy, vendor evaluation, contract mgmt, risk assessment | 3+ yrs vendor mgmt, contract negotiation, risk assessment | 15/01/2026 | Rủi ro vendor cao, không tracking (compliance risk) |
| **PQA Junior Auditor** | Junior | PQA Lead | Audit execution, checklist development, findings tracking | 1-2 yrs QA exp, ITIL/ISO knowledge, audit skills | 01/02/2026 | PQA coverage thấp (3%), cần mở rộng audit |

**Total Q1:** **3 FTE**

#### **Q2 2026 - SCALING**

| **Vị trí** | **Level** | **Báo cáo cho** | **Trách nhiệm chính** | **Yêu cầu năng lực** | **Start Date** | **Lý do cần thiết** |
|-----------|-----------|----------------|----------------------|---------------------|----------------|-------------------|
| **CMDB Data Analyst** | Mid-Junior | CMDB Admin | Data quality, metrics dashboard, reporting, analytics | 2+ yrs data analysis, BI tools, SQL, CMDB knowledge | 01/04/2026 | CMDB data 50-100%, cần quality control và metrics |

**Total Q2:** **1 FTE**

#### **Q3-Q4 2026 - CONSIDER (Not urgent, can delay to 2027)**

| **Vị trí** | **Level** | **Báo cáo cho** | **Trách nhiệm chính** | **Timeline** | **Có thể hoãn?** |
|-----------|-----------|----------------|----------------------|-------------|-----------------|
| Senior Incident Manager | Senior | Head IT Ops | IM process ownership, SLA, escalation, team lead | Q3 2026 | Có - Có thể promote internal hoặc hire Q1 2027 |
| Junior QC Automation Engineer | Junior | QC Lead | Test automation development, framework maintenance | Q4 2026 | Có - Automation không urgent năm 1 |

**Total Q3-Q4:** **0-2 FTE (optional)**

### 4.2. HEADCOUNT SUMMARY

| **Timeline** | **Vị trí** | **Số lượng** | **Total FTE** | **Cumulative** |
|-------------|-----------|--------------|---------------|----------------|
| Q1 2026 | CMDB Admin, Vendor Mgr, PQA Junior | 3 | 3 | 3 |
| Q2 2026 | CMDB Data Analyst | 1 | 1 | 4 |
| Q3-Q4 2026 | (Optional) IM Manager, QC Automation | 0-2 | 0-2 | 4-6 |
| **Total Year 1** | | | **4-6 FTE** | **10-12 FTE total (current 6 + new 4-6)** |

### 4.3. TRAINING REQUIREMENTS

| **Training** | **Đối tượng** | **Số lượng** | **Timeline** | **Chi phí ước tính** | **Provider** |
|-------------|---------------|--------------|-------------|---------------------|-------------|
| **ITIL 4 Foundation** | All ITSM team | 15 người | Q1 2026 | 15 x $500 = $7,500 | PeopleCert/AXELOS |
| **ITIL 4 Specialist (HVIT, DSV, CDS)** | Key roles (CM, IM, Service Mgr) | 5 người | Q3 2026 | 5 x $1,200 = $6,000 | PeopleCert/AXELOS |
| **CMDB/ITAM Training** | CMDB team, Infra | 10 người | Q2 2026 | Internal or $3,000 | Vendor-provided |
| **Test Automation (Selenium, API)** | QC team | 5 người | Q2 2026 | 5 x $800 = $4,000 | External trainer |
| **Vendor Management** | Vendor Mgr, Procurement | 3 người | Q1-Q2 2026 | $2,000 | External trainer |
| **Audit & Compliance** | PQA team | 3 người | Q2 2026 | $2,000 | ISO/ITIL auditor |
| **TOTAL TRAINING** | | **41 người** | | **$24,500** | |

### 4.4. TOOL INVESTMENT

| **Tool** | **Purpose** | **Timeline** | **Estimated Cost** | **Alternative** |
|---------|------------|-------------|-------------------|----------------|
| **CMDB Tool** (ServiceNow, Atlassian Assets, Cherwell) | Configuration Management Database | Q1-Q2 2026 | $30,000 - $100,000/year (depends on scale) | Build custom (not recommended) |
| **VMS (Vendor Management System)** | Vendor tracking, contracts, performance | Q3-Q4 2026 | $10,000 - $30,000/year | SharePoint/Google Workspace (interim) |
| **BI/Dashboard Tool** (Tableau, Power BI, Grafana upgrade) | Metrics dashboards | Q1-Q2 2026 | $5,000 - $15,000/year | Grafana + custom (current) |
| **Test Automation Tools** (Selenium Grid, API testing) | QC automation | Q2-Q3 2026 | $5,000 - $10,000/year | Open-source (current) |
| **TOTAL TOOLS** | | | **$50,000 - $155,000/year** | Minimum: $30k (CMDB only) |

### 4.5. TOTAL INVESTMENT SUMMARY (YEAR 1)

| **Category** | **Cost Range** | **Notes** |
|-------------|---------------|-----------|
| **Headcount** (4 FTE) | $200,000 - $400,000 | Depends on market rates (mid-senior avg $50-100k) |
| **Training** | $24,500 | ITIL certs, specialist training |
| **Tools** | $50,000 - $155,000 | CMDB critical, VMS optional |
| **External Consultants** (optional) | $20,000 - $50,000 | CMDB implementation, audit support |
| **TOTAL YEAR 1** | **$294,500 - $629,500** | Conservative: ~$300k, Full: ~$600k |

**ROI Expectations:**
- **Cost savings:** Reduced downtime (MTTR -30%), fewer change failures (CFR -50%), vendor cost optimization (10-15%)
- **Quality improvements:** Defect density -40%, test coverage +50%, SLA compliance +80%
- **Compliance:** Pass external audits, reduce regulatory risks
- **Efficiency:** Automation saves 20-30% manual effort = 2-3 FTE equivalent

---

## V. RISKS & MITIGATION

### 5.1. TOP RISKS

| **#** | **Risk** | **Likelihood** | **Impact** | **Mitigation** | **Owner** |
|-------|---------|---------------|-----------|---------------|-----------|
| 1 | **CMDB tool không được approved/budget delay** | Medium | Critical | Start with Excel improvements, build business case with ROI | IT Architect |
| 2 | **Không tuyển được 3 FTE trong Q1** | High | High | Start recruitment ngay, consider contractors, promote internal | HR + ITSM Lead |
| 3 | **Team resistance to new processes** | Medium | Medium | Change management, training, communicate benefits clearly | All Leads |
| 4 | **CMDB data quality thấp** | High | High | Data governance, CI owners, validation rules, audit | CMDB Admin |
| 5 | **Integration complexity cao hơn dự kiến** | Medium | High | POC trước khi rollout, expert consultants, phased approach | IT Architect |
| 6 | **Vendor Manager không có authority** | Medium | Medium | Clear mandate from CIO, formal approval process | CIO |
| 7 | **Audit findings quá nhiều, không xử lý hết** | High | Medium | Prioritize critical findings, extend timeline, add resources | PQA Lead |
| 8 | **Training budget không đủ** | Medium | Medium | Prioritize critical roles, online training cheaper, internal trainers | HR |
| 9 | **Business không adopt ITSM processes** | Medium | High | Executive sponsorship, show value early, quick wins | ITSM Lead |
| 10 | **Scope creep - quá nhiều initiatives** | High | Medium | Strict prioritization, focus on OC1-OC4, say no to non-critical | ITSM Lead |

### 5.2. CRITICAL SUCCESS FACTORS

1. **Executive Sponsorship** - CIO/CTO active support và communication
2. **Budget Approval** - Timely approval cho tools và headcount
3. **Recruitment Success** - Hire 3 FTE trong Q1, onboard nhanh
4. **CMDB Tool Selection** - Right tool, reasonable cost, fast deployment
5. **Change Management** - Team buy-in, training, clear communication
6. **Data Quality** - CMDB data accurate, complete, maintained
7. **Integration Success** - Jira-CMDB-IM-CM integration works smoothly
8. **Quick Wins Delivery** - Show value early (Q1) để justify investment
9. **Audit Preparation** - Pass internal audits để prepare cho external
10. **Continuous Improvement** - Review monthly, adjust roadmap, học từ mistakes

---

## VI. KHUYẾN NGHỊ VÀ NEXT STEPS

### 6.1. KHUYẾN NGHỊ ƯU TIÊN CAO CHO BAN LÃNH ĐẠO

#### **Tháng 12/2025 (NGAY LẬP TỨC)**
1. ✅ **Phê duyệt headcount 3 FTE cho Q1 2026** (CMDB Admin, Vendor Mgr, PQA Junior)
2. ✅ **Phê duyệt ngân sách tools** (tối thiểu CMDB tool: $30-50k/năm)
3. ✅ **Bổ nhiệm Incident Manager** (promote internal hoặc include trong recruitment)
4. ✅ **Ban hành 5 Quick Wins cho QC** (quality gate, QC policy, defect triage, etc.)
5. ✅ **Khởi động CMDB tool selection process** (RFP to vendors)

#### **Q1 2026 (Jan - Mar)**
1. ✅ **Onboard 3 FTE mới**
2. ✅ **Ban hành 5 policies** (CMDB, 3PM, PQA, MW, Data Retention)
3. ✅ **RACI Matrix cho tất cả mảng**
4. ✅ **SLA P1-P4 cho IM**
5. ✅ **CMDB tool selected và mua**
6. ✅ **20 quick wins completed**
7. ✅ **3 dashboards live** (IM, RM, CSAT)
8. ✅ **15 người ITIL Foundation certified**

#### **Q2 2026 (Apr - Jun)**
1. ✅ **CMDB tool deployed** (dev/pilot)
2. ✅ **30 core CIs populated**
3. ✅ **IM automation 70%**
4. ✅ **5 dashboards live**
5. ✅ **Internal audit plan approved**

### 6.2. DECISION POINTS CHO BAN LÃNH ĐẠO

**Quyết định cần thiết trong 2 tuần tới:**

| **#** | **Decision** | **Options** | **Recommendation** | **Deadline** |
|-------|-------------|------------|-------------------|-------------|
| 1 | **Phê duyệt headcount 3 FTE Q1** | Approve / Delay / Reject | **APPROVE** - Critical cho roadmap | 15/12/2025 |
| 2 | **Budget CMDB tool** | $30k / $50k / $100k / Reject | **$50k** - Mid-range tool, good ROI | 15/12/2025 |
| 3 | **Budget training (ITIL)** | $7.5k (Foundation only) / $13.5k (Full) | **$13.5k** - Include Specialist | 20/12/2025 |
| 4 | **VMS tool year 1?** | Yes Q2 / Yes Q4 / Defer to 2027 | **Defer to Q4 or 2027** - Not urgent | 15/01/2026 |
| 5 | **External CMDB consultant?** | Yes / No | **Yes (Q1-Q2)** - Faster deployment | 15/01/2026 |

### 6.3. IMMEDIATE NEXT STEPS (WEEK 1-2)

**Week 1 (Dec 2-8):**
1. ✅ Present báo cáo này cho CIO/CTO và Ban Lãnh Đạo
2. ✅ Get approval cho headcount 3 FTE và budget tools
3. ✅ Kick off recruitment process (job descriptions, post jobs)
4. ✅ Start CMDB tool RFP (send to 3-5 vendors)
5. ✅ Execute 5 QC Quick Wins (quality gate, policy, etc.)

**Week 2 (Dec 9-15):**
1. ✅ Interview candidates cho 3 FTE positions
2. ✅ Review CMDB tool proposals
3. ✅ Ban hành Change Freeze Calendar 2026
4. ✅ Start RACI Matrix workshops
5. ✅ Define KPIs cho tất cả mảng (workshops)

**Week 3-4 (Dec 16-31):**
1. ✅ Hire 3 FTE (offers sent, start dates confirmed)
2. ✅ Select CMDB tool (final decision)
3. ✅ Complete 10 Quick Wins
4. ✅ Setup ITIL training schedule Q1
5. ✅ Finalize Q1 detailed plan

---

## VII. APPENDIX

### 7.1. GLOSSARY (DÀNH CHO LÃNH ĐẠO CHƯA QUEN ITSM)

| **Thuật ngữ** | **Viết tắt** | **Giải thích** | **Ví dụ** |
|--------------|-------------|---------------|-----------|
| **ITSM** | IT Service Management | Quản trị dịch vụ CNTT - Tập hợp quy trình để cung cấp và quản lý dịch vụ IT | Incident Management, Change Management |
| **ITIL** | IT Infrastructure Library | Framework quốc tế về ITSM, chuẩn best practices | ITIL 4 là phiên bản mới nhất |
| **Maturity Level** | | Mức độ trưởng thành của quy trình (1-5: Initial, Managed, Defined, Quantitatively Managed, Optimizing) | Level 1 = ad-hoc, Level 3 = chuẩn hóa |
| **CMDB** | Configuration Management Database | Cơ sở dữ liệu lưu thông tin về tất cả IT assets (servers, apps, DBs) và mối quan hệ giữa chúng | Khi có incident, tra CMDB để biết ảnh hưởng gì |
| **CI** | Configuration Item | Một thành phần IT được quản lý (server, app, database, network device) | Server "prod-web-01" là 1 CI |
| **SLA** | Service Level Agreement | Thỏa thuận mức độ dịch vụ - Cam kết thời gian phản hồi/xử lý | P1 incident phải phản hồi trong 15 phút |
| **RFC** | Request For Change | Yêu cầu thay đổi hệ thống (deploy code, config change) | Developer tạo RFC để deploy version mới |
| **CR** | Change Request | Tương tự RFC | |
| **Incident** | | Sự cố gây gián đoạn dịch vụ hoặc làm giảm chất lượng | Website down, app chậm, user không login được |
| **Change** | | Thay đổi có kế hoạch đối với IT infrastructure/application | Deploy code mới, upgrade database |
| **CAB** | Change Advisory Board | Hội đồng tư vấn thay đổi - Nhóm người review và approve changes | CAB gồm: IT Lead, Security, Business Owner |
| **PIR** | Post Implementation Review | Đánh giá sau triển khai - Review xem change có thành công không | Sau deploy, check xem có bug không |
| **RCA** | Root Cause Analysis | Phân tích nguyên nhân gốc của sự cố | Tại sao server down? → Hard disk lỗi |
| **MTTA** | Mean Time To Acknowledge | Thời gian trung bình để phản hồi incident | MTTA = 10 phút = nhận ticket sau 10 phút |
| **MTTR** | Mean Time To Resolve | Thời gian trung bình để xử lý xong incident | MTTR = 2 giờ = fix xong sau 2 giờ |
| **CFR** | Change Failure Rate | Tỷ lệ changes bị fail | CFR = 5% = 5/100 changes bị lỗi |
| **CSAT** | Customer Satisfaction | Điểm hài lòng của khách hàng | CSAT = 4.2/5.0 |
| **QA** | Quality Assurance | Đảm bảo chất lượng - Audit quy trình | PQA audit xem CM process có tuân thủ không |
| **QC** | Quality Control | Kiểm soát chất lượng - Test sản phẩm | QC test app trước khi release |
| **3PM** | 3rd Party Management | Quản lý nhà cung cấp bên thứ 3 | Quản lý vendor, contract, SLA |
| **VMS** | Vendor Management System | Hệ thống quản lý vendor | Tool để track vendors, contracts, performance |

### 7.2. MATURITY LEVEL DEFINITIONS

| **Level** | **Tên** | **Điểm** | **Đặc điểm** | **Ví dụ** |
|----------|---------|---------|-------------|-----------|
| **Level 1** | Initial | 0-40% | Ad-hoc, không có quy trình formal, phụ thuộc cá nhân | CMDB hiện tại (9%) - dùng Excel, manual |
| **Level 2** | Managed | 40-60% | Có quy trình cơ bản, documented, executed nhưng chưa chuẩn hóa hết | CM hiện tại (58%) - có RFC nhưng thiếu risk framework |
| **Level 3** | Defined | 60-75% | Quy trình chuẩn hóa, metrics, integration, compliance OK | Target cho CM, IM sau 12 tháng |
| **Level 4** | Quantitatively Managed | 75-85% | Quy trình được đo lường định lượng, predictive analytics | 2027+ target |
| **Level 5** | Optimizing | 85-100% | Continuous improvement, AI/ML, world-class | Long-term vision |

### 7.3. KEY CONTACTS & OWNERS

| **Vai trò** | **Người hiện tại** | **Vai trò mới (nếu có)** | **Responsible for** |
|-----------|-------------------|------------------------|---------------------|
| ITSM Lead | TBD | | Overall ITSM strategy, roadmap execution |
| CM Lead | 1 Mid Senior (hiện tại) | | Change Management process, CAB, CFR |
| IM Manager | 1 Mid Senior (hiện tại) | Cần bổ nhiệm formal | Incident Management, SLA, MTTA/MTTR |
| RM Lead | 1 Last Junior (hiện tại) | | Request Management, service desk |
| CMDB Administrator | **KHÔNG CÓ** | **TUYỂN Q1 2026** | CMDB tool, data population, CI management |
| CMDB Data Analyst | **KHÔNG CÓ** | **TUYỂN Q2 2026** | CMDB metrics, data quality, reporting |
| Vendor Manager | **KHÔNG CÓ** | **TUYỂN Q1 2026** | 3rd party management, vendor evaluation |
| PQA Lead | 1 Mid Senior (hiện tại) | | Process audits, compliance, findings |
| PQA Junior Auditor | **KHÔNG CÓ** | **TUYỂN Q1 2026** | Audit execution, checklist, tracking |
| QC Lead | TBD | | Quality Control, testing, defect management |

---

## KẾT LUẬN

Tổ chức hiện đang ở giai đoạn **INITIAL đến MANAGED** (Level 1-2) cho các hoạt động ITSM và QA, với nhiều điểm sáng nhưng cũng có những khoảng cách nghiêm trọng cần khắc phục.

**3 ưu tiên hàng đầu:**
1. **CMDB deployment** (OC2) - Critical foundation cho tất cả ITSM processes
2. **Governance & Compliance** (OC1) - Policies, roles, RACI, SLA, audit
3. **Metrics & Automation** (OC4 + OC3) - Dashboards, KPIs, automation để tăng hiệu quả

Với lộ trình 12 tháng này và đầu tư khoảng **4-6 FTE + $300-600k**, tổ chức có thể đạt **Level 2-3 (55-70%)** cho tất cả các mảng, đủ để pass external audits, improve service quality, và establish foundation cho long-term maturity.

**Success phụ thuộc vào:**
- ✅ Executive sponsorship và commitment
- ✅ Budget approval kịp thời
- ✅ Tuyển được đúng người trong Q1
- ✅ CMDB tool selection đúng và deploy nhanh
- ✅ Team buy-in và change management tốt

Đây là 1 năm **foundation year** - sau 12 tháng này, tổ chức sẽ có nền tảng vững chắc để scale lên Level 3-4 trong 2027-2028.

---

**Prepared by:** IT Service Management Team
**Date:** 02/12/2025
**Version:** 1.0
**Status:** For Executive Review & Approval
