# BÁO CÁO ĐÁNH GIÁ VÀ LỘ TRÌNH TRIỂN KHAI ITSM/QA
## Dành cho Ban Lãnh Đạo

**Ngày:** 02/12/2025
**Phiên bản:** 1.0 - Executive Summary & Implementation Roadmap

---

## PHẦN A: TÓM TẮT ĐIỀU HÀNH

### 1. BỐI CẢNH VÀ MỤC ĐÍCH

Báo cáo này tổng hợp kết quả đánh giá toàn diện về **7 lĩnh vực quản lý dịch vụ CNTT (ITSM)** và **Đảm bảo chất lượng (QA)** tại tổ chức, bao gồm:

1. **PQA** - Đảm bảo Chất lượng Quy trình
2. **QC** - Kiểm soát Chất lượng Sản phẩm
3. **RM** - Quản lý Yêu cầu/Dịch vụ
4. **CM** - Quản lý Thay đổi
5. **CMDB** - Cơ sở dữ liệu Quản lý Cấu hình
6. **IM** - Quản lý Sự cố
7. **3rd Party** - Quản lý Nhà cung cấp bên thứ ba

**ITSM là gì?** ITSM (IT Service Management) là phương pháp tổ chức và quản lý các dịch vụ CNTT để đảm bảo chất lượng, giảm rủi ro, tăng hiệu quả và tiết kiệm chi phí. Các tổ chức hàng đầu thế giới áp dụng ITSM theo chuẩn ITIL và ISO 20000.

### 2. TÌNH TRẠNG HIỆN TẠI - TỔNG QUAN

| Lĩnh Vực | Điểm Hiện Tại | Trưởng Thành | Mức Độ Rủi Ro | Target 12 Tháng |
|----------|---------------|--------------|----------------|-----------------|
| **1. CM - Change Management** | 58.5% | Level 2 | 🟡 MEDIUM | 65-70% (Level 3) |
| **2. RM - Request Fulfillment** | 47.8% | Level 1+ | 🟠 HIGH | 55-65% (Level 2) |
| **3. IM - Incident Management** | 44.3% | Level 1+ | 🟠 HIGH | 60-70% (Level 3) |
| **4. PQA - Process QA** | 41.2% | Level 2- | 🟠 HIGH | 50-65% (Level 2) |
| **5. QC - Quality Control** | 30.8% | Level 1 | 🔴 CRITICAL | 45-50% (Level 2) |
| **6. 3rd Party Management** | 19.4% | Level 1 | 🔴 CRITICAL | 45-60% (Level 2) |
| **7. CMDB** | 9.4% | Level 1 | 🔴 CRITICAL | 45-60% (Level 2) |

**Điểm Trung Bình:** 35.9/100 - **Level 1: INITIAL (Chưa Chuẩn Hóa)**

### 3. PHÁT HIỆN CHÍNH

#### ✅ ĐIỂM MẠNH

1. **Change Management hoạt động tốt** (58.5%)
   - Quy trình quản lý thay đổi đã được thiết lập
   - Tỷ lệ thất bại thấp (< 5%)
   - Có công cụ tracking (Jira)

2. **Nguồn lực cam kết và nhiệt tình**
   - Team có kinh nghiệm, văn hóa hợp tác tốt
   - Sẵn sàng cải tiến

3. **Hạ tầng công cụ cơ bản đã có**
   - Jira, Grafana, CI/CD pipeline

#### ⚠️ RỦI RO NGHIÊM TRỌNG

| Vấn Đề | Ảnh Hưởng Kinh Doanh | Tỷ Lệ |
|--------|----------------------|-------|
| **1. CMDB không tồn tại (9.4%)** | - Không biết hệ thống nào phụ thuộc hệ thống nào<br>- Thay đổi/sự cố không đánh giá được tác động<br>- Rủi ro gián đoạn dịch vụ cao | 🔴 CRITICAL |
| **2. Quản lý nhà cung cấp yếu (19.4%)** | - Rủi ro vendor lock-in<br>- Không đánh giá được hiệu suất đối tác<br>- Chi phí không tối ưu | 🔴 CRITICAL |
| **3. Không tuân thủ chuẩn (0-15%)** | - Rủi ro audit bên ngoài<br>- Không chứng minh compliance ISO/ITIL<br>- Rủi ro pháp lý | 🔴 CRITICAL |
| **4. Không đo lường KPI (8-23%)** | - Không chứng minh giá trị CNTT<br>- Quyết định thiếu căn cứ<br>- Không phát hiện vấn đề sớm | 🔴 CRITICAL |
| **5. Hệ thống không liên thông (10-37%)** | - Làm việc thủ công, lãng phí thời gian<br>- Dữ liệu không nhất quán<br>- Khó phân tích xu hướng | 🟠 HIGH |

### 4. NGUỒN LỰC HIỆN TẠI VÀ KHOẢNG CÁCH

**Nguồn lực hiện có:**
- Change Management: **1 Mid Senior** ✅
- Incident Management: **1 Mid Senior + 1 Part-time** ✅
- Request Fulfillment: **3 FTE** (1 Late Junior, 2 Mid Junior) ✅
- Process QA: **1 Mid Senior** ✅
- **3rd Party Management: 0 FTE** ❌
- **Configuration Management (CMDB): 0 FTE** ❌

**Tổng hiện có: 6.5 FTE**

**Khoảng cách nguồn lực cần bổ sung: 5.5 FTE**

---

## PHẦN B: CÁC MỤC TIÊU CHIẾN LƯỢC (OBJECTIVES)

### OC1: Thiết Lập Framework Quản Trị ITSM với Policies, Roles, RACI và SLA

**Mục tiêu:**
- Xây dựng bộ chính sách (policies) đầy đủ cho 7 lĩnh vực ITSM
- Định nghĩa rõ vai trò, trách nhiệm (RACI matrix)
- Thiết lập SLA (Service Level Agreement - Cam kết mức độ dịch vụ) cho từng quy trình
- Đảm bảo tuân thủ ITIL và ISO 20000

**Phạm vi:**
- 7 ITSM Policy Documents
- 7 RACI Matrices
- 15+ SLA Definitions
- Compliance Framework & Checklist

**Timeline:** Q1-Q2/2026 (6 tháng)

---

### OC2: Xây Dựng CMDB Chuẩn Hóa

**Mục tiêu:**
- Triển khai hệ thống CMDB (Configuration Management Database) chuyên dụng
- Ghi nhận 75%+ tài sản CNTT (servers, applications, databases, network devices)
- Thiết lập quan hệ phụ thuộc giữa các thành phần
- Tích hợp CMDB với Incident, Change, Request Management

**Lý do quan trọng:** CMDB là "xương sống" của ITSM - giúp:
- Đánh giá tác động trước khi thay đổi
- Xác định nguyên nhân sự cố nhanh hơn
- Quản lý rủi ro tốt hơn
- Giảm thời gian xử lý sự cố 30-60%

**Timeline:** Q1-Q4/2026 (12 tháng)

---

### OC3: Nâng Cao Mức Độ Trưởng Thành ITSM - Cải Thiện Chất Lượng, Tăng Tốc Release & Tiết Kiệm Chi Phí

**Mục tiêu:**
- Đạt Level 2 (Managed) cho TẤT CẢ lĩnh vực (50-65%)
- Tự động hóa 70%+ quy trình thủ công
- Giảm 30% thời gian xử lý incident
- Tăng 40% tốc độ triển khai tính năng mới
- Giảm 20-30% chi phí vận hành

**Các sáng kiến chính:**
- Test Automation Strategy (QC)
- Intelligent Request Routing (RM)
- CMDB-driven Impact Analysis (CM)
- 3rd Party Performance Management

**Timeline:** Q2-Q4/2026 (9 tháng)

---

### OC4: Thiết Lập Key Metrics Dashboards, CSAT Mechanism và Monthly Reviews

**Mục tiêu:**
- Xây dựng 50+ KPIs theo dõi hiệu suất ITSM/QA
- Dashboard thời gian thực cho leadership
- Khảo sát hài lòng khách hàng (CSAT) tự động
- Quy trình review hàng tháng với executive reporting

**Metrics chính:**
- SLA Compliance Rate
- Change Failure Rate
- Incident MTTR (Mean Time To Resolve)
- Customer Satisfaction Score
- Cost per Ticket/Change/Request

**Timeline:** Q1-Q3/2026 (9 tháng)

---

## PHẦN C: ROADMAP TRIỂN KHAI 12 THÁNG CHI TIẾT

### TỔNG QUAN LỘ TRÌNH

```
Q1/2026 (Jan-Mar):  FOUNDATION - Policies, Roles, SLA, CMDB Planning
Q2/2026 (Apr-Jun):  BUILD - CMDB Deployment, Automation, KPI Dashboards
Q3/2026 (Jul-Sep):  SCALE - Integration, 3rd Party Mgmt, Compliance
Q4/2026 (Oct-Dec):  OPTIMIZE - Advanced Analytics, Re-assessment
```

---

### Q1 2026: NỀN TẢNG (FOUNDATION)
**Mục tiêu:** Thiết lập framework quản trị và chuẩn bị triển khai CMDB

#### THÁNG 1-2: GOVERNANCE & POLICIES (OC1)

| # | Đầu Mục Công Việc | Owner | Nguồn Lực | Mapping | Timeline |
|---|-------------------|-------|-----------|---------|----------|
| 1.1 | **Xây dựng ITSM Governance Framework** | ITSM Lead | 1 FTE (100%) | OC1 | Week 1-4 |
| | - ITSM Strategy & Vision Document<br>- 7 Policy Documents (CM, IM, RM, PQA, QC, CMDB, 3rd Party)<br>- Service Management Principles | | | | |
| 1.2 | **Xây dựng RACI Matrix cho 7 lĩnh vực** | ITSM Lead + 7 Process Owners | Workshop 2 ngày | OC1 | Week 3-4 |
| | - CM RACI (Từ Finding CM-7)<br>- IM RACI (Từ Finding IM-4)<br>- RM RACI (Từ Finding RM-3)<br>- PQA RACI (Từ Finding PQA-6)<br>- CMDB RACI<br>- QC RACI<br>- 3rd Party RACI | | | | |
| 1.3 | **Thiết lập SLA Framework** | Service Manager | 0.5 FTE | OC1 | Week 5-6 |
| | - IM SLA P1-P4 (Từ Finding IM-5)<br>- RM SLA Standard/Non-Standard (Từ Finding RM-6)<br>- CM Maintenance Window SLA (Từ Quickwin CM-2)<br>- 3rd Party Response SLA | | | | |
| 1.4 | **Bổ nhiệm vai trò chính thức** | CIO/CTO | HR Process | OC1 | Week 1-2 |
| | - Incident Manager (Từ Finding IM-4)<br>- CMDB Steward (Từ Finding CMDB-6)<br>- 3rd Party Manager (Mới tuyển)<br>- CMDB Admin (Mới tuyển) | | **+2 Headcount** | | |

**QUICK WINS THÁNG 1-2:**

| QW | Quick Win | Effort | Impact | Owner | Mapping |
|----|-----------|--------|--------|-------|---------|
| QW1 | Configure quality gate: FAIL build khi test fail | 1 tuần | HIGH | DevOps Lead | QC-1 → OC3 |
| QW2 | Xây dựng Audit Checklist cho CM, IM, PM, Config Mgmt | 2 tuần | HIGH | PQA Lead | PQA-1 → OC1 |
| QW3 | Hoàn thiện QA Charter, Scope, RACI Matrix | 1 tuần | HIGH | PQA Lead | PQA-3 → OC1 |
| QW4 | Change Freeze Calendar 2026 | 3 ngày | MEDIUM | CM Lead | CM-3 → OC1 |
| QW5 | Document roles & approval workflows (RM) | 1 tuần | HIGH | RM Lead | RM-2 → OC1 |

#### THÁNG 2-3: CMDB PLANNING & MEASUREMENT (OC2 + OC4)

| # | Đầu Mục Công Việc | Owner | Nguồn Lực | Mapping | Timeline |
|---|-------------------|-------|-----------|---------|----------|
| 2.1 | **CMDB Policy & Strategy** | CMDB Steward | 0.5 FTE | OC2 | Week 7-8 |
| | - CMDB Policy Charter (Từ Quickwin CMDB-1)<br>- CI Classification & Naming Convention (Quickwin CMDB-3)<br>- CI Owner Assignment (Quickwin CMDB-2)<br>- Data Quality Standards (Từ Finding CMDB-10) | | | | |
| 2.2 | **CMDB Tool Evaluation & Selection** | IT Manager + Architect | RFP Process | OC2 | Week 8-12 |
| | - Requirements gathering<br>- Vendor evaluation (ServiceNow, Jira Assets, iTop, Device42)<br>- POC (Proof of Concept)<br>- Procurement approval | | Budget: $50K-80K | | |
| 2.3 | **CI Identification Process** | CMDB Admin | 1 FTE | OC2 | Week 9-12 |
| | - Intake form cho CI mới (Từ Finding CMDB-3)<br>- CI Audit Trail setup (Từ Finding CMDB-5)<br>- Map CI relationships - Top 10 services (Từ Finding CMDB-4) | | | | |
| 2.4 | **KPI Framework & Dashboard Design** | BI Analyst + Process Owners | 1 FTE | OC4 | Week 7-12 |
| | - Define 50+ KPIs cho 7 lĩnh vực<br>- Dashboard wireframes<br>- Data collection automation (Jira API)<br>- Executive Dashboard template | | Require: BI Team | | |

**DELIVERABLES Q1:**
- ✅ 7 Policy Documents
- ✅ 7 RACI Matrices
- ✅ 15+ SLA Definitions
- ✅ CMDB Tool selected & purchased
- ✅ KPI Framework defined
- ✅ 2 new hires onboarded (CMDB Admin, 3rd Party Manager)
- ✅ 5 Quick Wins completed

**RESOURCE REQUIRED Q1:**
- Internal: 3-4 FTE effort (existing + new hires)
- New Hires: **+2 FTE** (CMDB Admin, 3rd Party Manager)
- External: Consultant for ITSM Policy review (2 weeks, $15K-20K)
- Tools: CMDB Tool purchase ($50K-80K)

---

### Q2 2026: XÂY DỰNG (BUILD)
**Mục tiêu:** Deploy CMDB, triển khai automation, launch KPI dashboards

#### THÁNG 4-5: CMDB DEPLOYMENT & AUTOMATION (OC2 + OC3)

| # | Đầu Mục Công Việc | Owner | Nguồn Lực | Mapping | Timeline |
|---|-------------------|-------|-----------|---------|----------|
| 3.1 | **CMDB Tool Implementation Phase 1** | CMDB Admin + Vendor | 2 FTE | OC2 | Week 13-20 |
| | - Installation & Configuration<br>- Load 20-30% critical CIs (Top 50 applications)<br>- Setup CI relationships<br>- Integration với Jira (Incident/Change)<br>- User training (20 people) | | Implementation Services: $30K | | |
| 3.2 | **Intelligent Request Routing** | RM Lead + Dev | 1.5 FTE | OC3 | Week 13-16 |
| | - Phân tích request patterns<br>- Xây auto-categorization rules (Target 80% accuracy)<br>- Auto-routing logic<br>- Quality verification checklist (Từ Finding RM-5) | | Từ Finding RM-4 | | |
| 3.3 | **Test Automation Strategy Implementation** | QC Lead | 1 FTE | OC3 | Week 13-20 |
| | - Tool selection (Selenium, Cypress, etc.)<br>- Framework setup<br>- Pilot automation (10 test cases)<br>- CI/CD integration | | Từ Finding QC-5 | | |
| 3.4 | **Incident Management Automation** | IM Lead + Jira Admin | 1 FTE | OC3 | Week 17-20 |
| | - Auto-create incident từ monitoring alerts<br>- Auto-priority assignment<br>- Auto-routing rules<br>- SLA breach notifications | | Từ Finding IM-3 | | |

#### THÁNG 5-6: METRICS & DASHBOARDS GO-LIVE (OC4)

| # | Đầu Mục Công Việc | Owner | Nguồn Lực | Mapping | Timeline |
|---|-------------------|-------|-----------|---------|----------|
| 4.1 | **KPI Dashboards Development** | BI Analyst | 1 FTE | OC4 | Week 17-24 |
| | - Build KPI Dashboard cho 7 lĩnh vực<br>- Integrate data sources (Jira, CMDB, CI/CD)<br>- Setup auto-refresh (daily/weekly)<br>- Executive Summary Dashboard | | Grafana/Tableau/PowerBI | | |
| 4.2 | **CSAT Mechanism Launch** | Service Manager | 0.5 FTE | OC4 | Week 21-24 |
| | - Survey design (5-point scale)<br>- Integration vào RM/IM workflows<br>- Post-fulfillment trigger<br>- Analytics & reporting | | Từ Finding RM-2, IM-6 | | |
| 4.3 | **Monthly Service Review Process** | ITSM Lead | Process | OC4 | Week 22 |
| | - Review meeting template<br>- Agenda: KPI analysis, trends, actions<br>- Stakeholder list<br>- First review meeting | | Từ Finding RM-7 | | |

**DELIVERABLES Q2:**
- ✅ CMDB operational với 20-30% CIs
- ✅ Request auto-routing 80% accuracy
- ✅ Test automation framework deployed
- ✅ Incident auto-creation live
- ✅ 50+ KPIs tracking
- ✅ Live dashboards
- ✅ CSAT surveys active
- ✅ Monthly review cadence established

**RESOURCE REQUIRED Q2:**
- Internal: 5-6 FTE effort
- External: CMDB implementation services ($30K)
- Tools: Test automation licenses ($10K-15K)

---

### Q3 2026: MỞ RỘNG (SCALE)
**Mục tiêu:** Scale CMDB, triển khai 3rd Party Management, strengthen compliance

#### THÁNG 7-8: CMDB SCALE-UP & INTEGRATION (OC2 + OC3)

| # | Đầu Mục Công Việc | Owner | Nguồn Lực | Mapping | Timeline |
|---|-------------------|-------|-----------|---------|----------|
| 5.1 | **CMDB Expansion to 40-50% Coverage** | CMDB Admin | 1.5 FTE | OC2 | Week 25-32 |
| | - Load additional 200-300 CIs<br>- Auto-population từ monitoring tools (Zabbix/Prometheus)<br>- Enhanced dependency mapping<br>- Service-to-CI mapping cho 20 services | | | | |
| 5.2 | **Request-Incident-Change Linking Automation** | RM Lead + IM Lead + CM Lead | 1 FTE | OC3 | Week 25-28 |
| | - Auto-linking rules<br>- API integration giữa workflows<br>- CMDB auto-update từ changes<br>- Traceability reporting | | Từ Finding RM-8, CM-9 | | |
| 5.3 | **CM Risk Assessment Framework Go-Live** | CM Lead + CAB | 0.5 FTE | OC1 + OC3 | Week 25-28 |
| | - Risk scoring 5x5 matrix trong Jira<br>- High-risk approval workflow<br>- CAB review criteria<br>- Risk dashboard | | Từ Finding CM-1, Quickwin CM-1 | | |

#### THÁNG 8-9: 3RD PARTY MANAGEMENT & COMPLIANCE (OC1 + OC3)

| # | Đầu Mục Công Việc | Owner | Nguồn Lực | Mapping | Timeline |
|---|-------------------|-------|-----------|---------|----------|
| 6.1 | **3rd Party Management Framework Setup** | 3rd Party Manager | 1 FTE (New Hire) | OC1 + OC3 | Week 29-36 |
| | - Vendor registry & classification<br>- SLA framework cho vendors<br>- Performance scorecard design<br>- Contract management process<br>- Risk assessment template | | Từ 3rd Party Assessment | | |
| 6.2 | **Compliance Audit Preparation** | PQA Lead + Process Owners | 2 FTE | OC1 | Week 33-36 |
| | - ITIL/ISO 20000 gap analysis<br>- Evidence collection (policies, records, logs)<br>- Internal audit checklist<br>- Conduct internal audit round 1<br>- Remediation plan | | Từ Findings về Compliance | | |
| 6.3 | **Test Coverage Measurement Implementation** | QC Lead | 0.5 FTE | OC3 | Week 29-32 |
| | - Coverage tool integration (SonarQube)<br>- Target: 70% unit test coverage<br>- Dashboard & reporting<br>- Coverage gates trong CI/CD | | Từ Finding QC-4 | | |

**DELIVERABLES Q3:**
- ✅ CMDB at 40-50% coverage
- ✅ Full ITSM integration (IM-CM-RM-CMDB)
- ✅ 3rd Party Management operational
- ✅ Compliance audit completed
- ✅ Test coverage measurement live
- ✅ Risk-based change management

**RESOURCE REQUIRED Q3:**
- Internal: 5-6 FTE effort
- New Hire: **+1 FTE** (3rd Party Manager) - if not hired in Q1
- External: Compliance consultant ($15K-20K)

---

### Q4 2026: TỐI ƯU HÓA (OPTIMIZE)
**Mục tiêu:** Achieve Level 2 maturity, advanced analytics, continuous improvement

#### THÁNG 10-11: ADVANCED AUTOMATION & ANALYTICS (OC3 + OC4)

| # | Đầu Mục Công Việc | Owner | Nguồn Lực | Mapping | Timeline |
|---|-------------------|-------|-----------|---------|----------|
| 7.1 | **CMDB Reach 75%+ Coverage** | CMDB Admin | 1 FTE | OC2 | Week 37-44 |
| | - Final CI loading push<br>- Auto-update từ Change pipeline<br>- Advanced dependency visualization<br>- CMDB maturity assessment | | | | |
| 7.2 | **Advanced Test Automation Rollout** | QC Lead | 1 FTE | OC3 | Week 37-44 |
| | - Expand automation to 80% regression suite<br>- Performance testing framework<br>- API test automation<br>- Parallel execution setup | | Từ QC Roadmap | | |
| 7.3 | **Predictive Analytics & Forecasting** | BI Analyst + Data Scientist | 1 FTE | OC4 | Week 37-44 |
| | - Incident trend prediction<br>- Capacity forecasting<br>- Change success prediction<br>- Cost optimization insights | | Require: Data Science support | | |
| 7.4 | **Knowledge Base & Self-Service Enhancement** | RM Lead + IM Lead | 1 FTE | OC3 | Week 37-44 |
| | - KB integration với RM/IM portals<br>- Auto-suggest articles<br>- Self-service rate target: 40%<br>- Chatbot POC | | Từ Finding RM-10, IM-8 | | |

#### THÁNG 12: ASSESSMENT & 2027 PLANNING

| # | Đầu Mục Công Việc | Owner | Nguồn Lực | Mapping | Timeline |
|---|-------------------|-------|-----------|---------|----------|
| 8.1 | **Re-Assessment of 7 ITSM Areas** | External Consultant + ITSM Lead | Workshop | ALL OC | Week 45-48 |
| | - Maturity re-assessment<br>- Verify targets achieved<br>- Identify remaining gaps<br>- ROI calculation & reporting | | External Assessment: $10K | | |
| 8.2 | **2027 Roadmap Development** | ITSM Lead + Leadership | Workshop | ALL OC | Week 49-52 |
| | - Review 2026 outcomes<br>- Define 2027 objectives<br>- Resource planning<br>- Budget proposal 2027 | | | | |
| 8.3 | **Executive Summary Report & Presentation** | ITSM Lead | Report | OC4 | Week 50 |
| | - Year-end executive report<br>- KPI achievements<br>- Business impact quantified<br>- Leadership presentation | | | | |

**DELIVERABLES Q4:**
- ✅ CMDB at 75%+ coverage
- ✅ All 7 areas reach Level 2 (50-65%)
- ✅ Test automation 80%
- ✅ Self-service rate 40%
- ✅ Predictive analytics operational
- ✅ 2027 roadmap approved

**RESOURCE REQUIRED Q4:**
- Internal: 4-5 FTE effort
- External: Re-assessment ($10K)

---

## PHẦN D: MAPPING CHI TIẾT - FINDINGS/QUICKWINS ⟷ OBJECTIVES

### OC1: Thiết Lập Framework Quản Trị ITSM

| Lĩnh Vực | Finding/Quickwin | Deliverable | Timeline |
|----------|------------------|-------------|----------|
| **PQA** | Finding PQA-6: Cơ cấu quản trị chưa rõ | PQA Charter, RACI Matrix | Q1 |
| | Quickwin PQA-3: Hoàn thiện QA Charter | QA Charter approved | Q1 |
| **QC** | Finding QC-1: Không có chiến lược QC | QC Strategy & Policy | Q1 |
| | Finding QC-7: Không tuân thủ chuẩn | ITIL/ISO mapping | Q1 |
| **RM** | Finding RM-3: Vai trò không rõ | RM RACI, Approval workflow | Q1 |
| | Finding RM-6: Standard vs Non-Standard | SLA definition | Q1 |
| | Quickwin RM-2: Document roles | Role documentation | Q1 |
| **CM** | Finding CM-7: RACI chưa chính thức | CM RACI Matrix | Q1 |
| | Finding CM-6: CAB thiếu tiêu chí | CAB Charter, Criteria | Q1 |
| | Quickwin CM-5: RACI Formal Doc | RACI published | Q1 |
| **CMDB** | Finding CMDB-1: Chưa có policy | CMDB Policy Charter | Q1 |
| | Finding CMDB-6: Không có CMDB Steward | CMDB Steward assigned | Q1 |
| | Quickwin CMDB-1: Policy Charter | Policy approved | Q1 |
| **IM** | Finding IM-4: Roles chưa rõ | IM RACI, IM Manager role | Q1 |
| | Finding IM-5: SLA chưa đồng thuận | IM SLA P1-P4 | Q1 |
| **3rd Party** | Finding 3PT-1: Không có framework | 3PT Policy & Framework | Q3 |

**OC1 TỔNG KẾT:**
- **7 Policy Documents** (Q1)
- **7 RACI Matrices** (Q1)
- **15+ SLA Definitions** (Q1-Q2)
- **Compliance Framework** (Q3)

---

### OC2: Xây Dựng CMDB Chuẩn Hóa

| Lĩnh Vực | Finding/Quickwin | Deliverable | Timeline |
|----------|------------------|-------------|----------|
| **CMDB** | Finding CMDB-2: Không có tool | CMDB tool deployed | Q2 |
| | Finding CMDB-3: Không có quy trình identify CI | CI intake process | Q1 |
| | Finding CMDB-4: Chưa map relationships | Dependency mapping | Q1-Q2 |
| | Finding CMDB-5: Không audit trail | Audit logging | Q2 |
| | Finding CMDB-7: CI Owners không gán | CI ownership | Q1 |
| | Finding CMDB-8: Không có KPI | CMDB KPI dashboard | Q2 |
| | Finding CMDB-9: Không integrate IM/CM | ITSM integration | Q2-Q3 |
| | Finding CMDB-10: Không data quality standards | Quality standards | Q2 |
| | Quickwin CMDB-2: CI Owner Assignment | 100% critical CIs owned | Q1 |
| | Quickwin CMDB-3: CI Classification | Classification standard | Q1 |
| **CM** | Finding CM-10: CMDB Integration chưa có | Xác định core CIs cho CM | Q2 |
| | | CR-CI mapping | Q2-Q3 |
| **IM** | Finding IM-1: Integration ITSM = 0 | Incident-CI linking | Q3 |
| **RM** | Finding RM-8: Request-CMDB manual | Request-CI update | Q3 |

**OC2 MILESTONES:**
- **Q1:** CMDB Policy, Tool selected, CI Classification
- **Q2:** CMDB deployed, 20-30% CIs loaded, IM/CM integration
- **Q3:** 40-50% CIs, Full ITSM integration
- **Q4:** 75%+ CIs, Auto-update, Maturity Level 2

---

### OC3: Nâng Cao Trưởng Thành ITSM - Chất Lượng, Tốc Độ, Tiết Kiệm

| Lĩnh Vực | Finding/Quickwin | Deliverable | Improvement Target | Timeline |
|----------|------------------|-------------|-------------------|----------|
| **QC** | Finding QC-4: Không đo test coverage | Coverage tool + gate 70% | +20% maturity | Q3 |
| | Finding QC-5: Không có automation strategy | Test automation framework | Automation 80% | Q2-Q4 |
| | Quickwin QC-1: Quality gate fail build | Build enforcement | Defect ↓30% | Q1 |
| **RM** | Finding RM-1: Không đo KPI | KPI framework + dashboard | Visibility 100% | Q2 |
| | Finding RM-4: Phân loại 100% manual | Auto-classification 80% | Time ↓50% | Q2 |
| | Finding RM-5: QA không chuẩn | Verification checklist | Quality ↑40% | Q2 |
| | Quickwin RM-1: Build metrics dashboard | Dashboard live | - | Q1 |
| | Quickwin RM-3: Auto-routing | 80% auto-routing | Efficiency ↑60% | Q2 |
| **CM** | Finding CM-1: Rủi ro chưa có thang | Risk 5x5 matrix | Risk visibility | Q3 |
| | Finding CM-11: Sonar tạm dừng | Re-enable Sonar | Code quality ↑ | Q3 |
| | Quickwin CM-1: Risk Assessment | Risk framework | - | Q1 |
| **IM** | Finding IM-3: Automation = 0 | Auto-create, route, priority | MTTA ↓40% | Q2 |
| | | | MTTR ↓30% | Q2 |
| **PQA** | Finding PQA-1: Không KPI Dashboard | PQA KPI dashboard | Coverage ↑80% | Q2 |
| | Finding PQA-3: Tần suất audit thấp | 1-2 audit/quý/lĩnh vực | Quality ↑50% | Q2-Q4 |
| | Quickwin PQA-1: Audit Checklist | 4 checklists | - | Q1 |
| **3rd Party** | 3PT Assessment gaps | Vendor scorecard + SLA | Cost ↓20% | Q3-Q4 |

**OC3 EXPECTED OUTCOMES:**
- **Defect Rate:** ↓30%
- **Release Cycle Time:** ↓40%
- **Incident MTTR:** ↓30%
- **Request Cycle Time:** ↓50%
- **Operational Cost:** ↓20-30%
- **Change Failure Rate:** ≤1%

---

### OC4: Thiết Lập Key Metrics, CSAT và Reviews

| Lĩnh Vực | Finding/Quickwin | Deliverable | Metrics Count | Timeline |
|----------|------------------|-------------|--------------|----------|
| **PQA** | Finding PQA-1: Không KPI | PQA KPI dashboard | 5-10 KPIs | Q2 |
| **QC** | Finding QC-3: Chưa có metrics | QC KPI (coverage, density, auto) | 8-10 KPIs | Q2 |
| **RM** | Finding RM-1,2: Không KPI, không CSAT | RM KPI + CSAT survey | 10-12 KPIs | Q1-Q2 |
| | Quickwin RM-1: Metrics framework | Dashboard operational | - | Q1 |
| **CM** | CM Metrics 77% | Enhance CM dashboard | 8-10 KPIs | Q2 |
| **CMDB** | Finding CMDB-8: Không KPI | CMDB effectiveness metrics | 28 KPIs | Q2 |
| **IM** | Finding IM-6: KPI không formal, CSAT=0 | IM KPI + CSAT | 10-12 KPIs | Q1-Q2 |
| **3rd Party** | 3PT Measurement 8% | Vendor performance scorecard | 6-8 KPIs | Q3 |
| **ALL** | Finding RM-7: Không service review | Monthly review process | Meeting cadence | Q1 |

**OC4 DELIVERABLES:**
- **Q1:** 50+ KPIs defined, Review cadence
- **Q2:** Live dashboards, CSAT launch, First reviews
- **Q3:** Advanced analytics, Trending reports
- **Q4:** Predictive analytics, Executive reporting

**DASHBOARD HIERARCHY:**
1. **Executive Dashboard** - Top 15 KPIs, Monthly
2. **Process Dashboards** (x7) - Real-time, Daily/Weekly
3. **Operational Dashboards** - Team level, Real-time

---

## PHẦN E: PHÂN BỔ NGUỒN LỰC CHI TIẾT

### 1. NGUỒN LỰC HIỆN TẠI (6.5 FTE)

| Vai Trò | FTE | Phân Bổ 2026 |
|---------|-----|--------------|
| **CM Lead** (Mid Senior) | 1.0 | 60% CM operations + 40% CM improvement roadmap |
| **IM Lead** (Mid Senior) | 1.0 | 50% IM operations + 30% automation + 20% integration |
| **IM Operations** (Part-time) | 0.5 | 100% IM operations support |
| **PQA Lead** (Mid Senior) | 1.0 | 50% PQA + 30% ITSM compliance + 20% audit |
| **RM Team** (1 Late Junior, 2 Mid Junior) | 3.0 | 70% RM operations + 30% automation & improvement |
| **TỔNG HIỆN CÓ** | **6.5** | |

### 2. NGUỒN LỰC CẦN BỔ SUNG (5.5 FTE)

#### A. TUYỂN DỤNG MỚI (4 FTE)

| # | Vai Trò | Level | Timeline | Chi Phí/Năm | Phân Bổ Công Việc | Báo Cáo Cho |
|---|---------|-------|----------|-------------|-------------------|-------------|
| 1 | **CMDB Administrator** | Mid | Q1 W1 | $60K-80K | 100% CMDB deployment, CI management, integration, training | ITSM Lead |
| 2 | **3rd Party Manager** | Mid Senior | Q1 W1 | $70K-90K | 100% Vendor management, contract, SLA, performance tracking | Service Manager |
| 3 | **QC Automation Engineer** | Mid | Q2 | $65K-85K | 80% Test automation + 20% QC strategy | QC Lead |
| 4 | **BI/Data Analyst** | Mid | Q1 | $65K-80K | 70% Dashboard + 20% KPI analysis + 10% reporting | ITSM Lead |

**Subtotal:** 4 FTE = $260K-335K/năm

#### B. REQUIRE TỪ BỘ PHẬN KHÁC (1.5 FTE Equivalent)

| # | Vai Trò | FTE | Thời Gian | Công Việc | Bộ Phận |
|---|---------|-----|-----------|-----------|---------|
| 5 | **DevOps Engineer** | 0.3 | Q1-Q4 | CI/CD integration, automation, Jira config | DevOps Team |
| 6 | **Infrastructure Team** | 0.3 | Q1-Q2 | CMDB tool deployment, server setup | Infrastructure |
| 7 | **Security Team** | 0.2 | Q2-Q3 | Compliance audit, security validation | Security Team |
| 8 | **Data Science** | 0.2 | Q4 | Predictive analytics, forecasting models | Data Team |
| 9 | **HR Partner** | 0.1 | Q1 | Recruitment, competency framework | HR |
| 10 | **Solution Architect** | 0.4 | Q1-Q2 | CMDB design, service mapping, integration architecture | Architecture Team |

**Subtotal:** 1.5 FTE equivalent

#### C. EXTERNAL CONSULTANT (Temporary)

| # | Dịch Vụ | Timeline | Chi Phí | Mục Đích |
|---|---------|----------|---------|----------|
| 1 | ITSM Framework Consultant | Q1 (2 weeks) | $15K-20K | Policy review, RACI workshop, best practices |
| 2 | CMDB Implementation Services | Q2 (6 weeks) | $30K | Tool deployment, training, data migration |
| 3 | Compliance Consultant | Q3 (2 weeks) | $15K-20K | ITIL/ISO audit, gap analysis, remediation |
| 4 | Re-Assessment Consultant | Q4 (1 week) | $10K | Maturity re-assessment, validation |

**Subtotal:** $70K-80K

### 3. TỔNG NGUỒN LỰC 2026

| Loại | FTE/Chi Phí | Chi Tiết |
|------|-------------|----------|
| **Existing Team** | 6.5 FTE | Operations + Improvement |
| **New Hires** | 4.0 FTE | $260K-335K |
| **Cross-functional** | 1.5 FTE eq | Part-time from other teams |
| **External Consultants** | $70K-80K | Temporary expertise |
| **TỔNG LỰC LƯỢNG** | **12 FTE equivalent** | |

### 4. TIMELINE TUYỂN DỤNG

```
Q1 2026:
  Week 1: Post job descriptions (CMDB Admin, 3PT Manager, BI Analyst)
  Week 2-3: Screening & interviews
  Week 4: Offers extended
  Week 5-6: Onboarding

Q2 2026:
  Week 13: Post QC Automation Engineer
  Week 14-15: Screening & interviews
  Week 16: Offer extended
  Week 17-18: Onboarding
```

### 5. TRAINING & DEVELOPMENT

| Đối Tượng | Training | Timeline | Chi Phí |
|-----------|----------|----------|---------|
| **All ITSM Team** | ITIL 4 Foundation (12 people) | Q2 | $8K |
| **Process Leads** | ITIL 4 Practitioner (5 people) | Q3 | $10K |
| **CMDB Admin** | CMDB Tools Training | Q1-Q2 | $5K |
| **QC Team** | Test Automation Certification | Q2-Q3 | $6K |
| **All Staff** | ITSM Awareness Workshop | Q1 | $3K |

**Total Training:** $32K

---

## PHẦN F: ĐẦU TƯ VÀ NGÂN SÁCH

### 1. CHI PHÍ NHÂN LỰC

| Hạng Mục | Chi Phí | Ghi Chú |
|----------|---------|---------|
| **4 FTE Mới** | $260K-335K | Bao gồm salary + benefits (30%) |
| **Training** | $32K | ITIL, Tools, Certifications |
| **External Consultants** | $70K-80K | Framework, Implementation, Audit |
| **Tổng Nhân Lực** | **$362K-447K** | |

### 2. CHI PHÍ CÔNG CỤ & HẠ TẦNG

| Công Cụ | Chi Phí | Loại | Ghi Chú |
|---------|---------|------|---------|
| **CMDB Tool** (ServiceNow/Jira Assets) | $50K-80K | One-time + Annual | 200-300 CIs, integration |
| **Test Automation Tools** | $10K-15K | Annual licenses | Selenium Grid, BrowserStack |
| **BI/Dashboard Tool** | $15K-20K | Annual licenses | Grafana Enterprise/Tableau |
| **ITSM Tool Enhancement** (Jira) | $10K | Plugins, add-ons | Automation, SLA, workflows |
| **Monitoring Integration** | $5K | Integration | Prometheus, Zabbix connectors |
| **Survey Tool** | $2K | Annual | CSAT surveys (SurveyMonkey/Qualtrics) |
| **CMDB Implementation Services** | $30K | One-time | Data migration, training |
| **Tổng Công Cụ** | **$122K-162K** | |

### 3. CHI PHÍ KHÁC

| Hạng Mục | Chi Phí |
|----------|---------|
| **Travel & Workshops** | $8K |
| **Documentation & Templates** | $3K |
| **Certification Exams** | $5K |
| **Contingency (10%)** | $50K |
| **Tổng Khác** | **$66K** | |

### 4. TỔNG NGÂN SÁCH 2026

| Loại Chi Phí | Q1 | Q2 | Q3 | Q4 | Tổng |
|--------------|-------|-------|-------|-------|---------|
| **Nhân Lực** | $110K | $120K | $110K | $107K | **$447K** |
| **Công Cụ** | $90K | $40K | $22K | $10K | **$162K** |
| **Khác** | $30K | $15K | $15K | $6K | **$66K** |
| **TỔNG** | **$230K** | **$175K** | **$147K** | **$123K** | **$675K** |

### 5. BREAKDOWN THEO OBJECTIVE

| Objective | % Ngân Sách | Chi Phí | Deliverables |
|-----------|-------------|---------|--------------|
| **OC1: Framework Quản Trị** | 20% | $135K | Policies, RACI, SLA, Governance |
| **OC2: CMDB** | 35% | $236K | CMDB tool, implementation, 75% CIs |
| **OC3: Nâng Cao Trưởng Thành** | 30% | $203K | Automation, integration, quality |
| **OC4: Metrics & Dashboards** | 15% | $101K | KPIs, dashboards, CSAT, reviews |
| **TỔNG** | **100%** | **$675K** | |

---

## PHẦN G: RỦI RO VÀ GIẢM THIỂU

### 1. RỦI RO CHÍNH

| # | Rủi Ro | Xác Suất | Ảnh Hưởng | Giảm Thiểu |
|---|---------|----------|-----------|------------|
| 1 | **Không tuyển đủ nhân lực đúng hạn** | MEDIUM | HIGH | - Start recruitment Q4 2025<br>- Use contractors if needed<br>- Internal mobility program |
| 2 | **CMDB tool deployment chậm** | MEDIUM | HIGH | - Choose proven tool (ServiceNow/Jira Assets)<br>- Engage vendor professional services<br>- Phased rollout plan |
| 3 | **Resistance to change từ teams** | HIGH | MEDIUM | - Change management program<br>- Show early wins (Quick Wins Q1)<br>- Executive sponsorship<br>- Training comprehensive |
| 4 | **Budget không được phê duyệt đầy đủ** | MEDIUM | HIGH | - Present ROI analysis<br>- Phased budget approval<br>- Start with critical items (CMDB, hires) |
| 5 | **Integration complexity cao hơn dự kiến** | MEDIUM | MEDIUM | - POC trước khi commit<br>- Buffer 20% timeline<br>- Engage architects early |
| 6 | **Scope creep** | HIGH | MEDIUM | - Strict change control<br>- Focus on 4 objectives<br>- Defer non-critical items to 2027 |
| 7 | **Key person dependency** | MEDIUM | HIGH | - Cross-training<br>- Documentation<br>- Knowledge sharing sessions |
| 8 | **External audit fail** | LOW | HIGH | - Internal audit Q3<br>- Compliance consultant<br>- Gap remediation buffer |

### 2. SUCCESS FACTORS

✅ **Critical Success Factors:**
1. Executive sponsorship & budget approval
2. Recruitment success (4 FTE onboarded Q1-Q2)
3. CMDB tool deployed by Q2
4. Quick Wins delivered Q1 (builds momentum)
5. Cross-functional collaboration (DevOps, Infra, Security)
6. Change management & training effectiveness

---

## PHẦN H: LỢI ÍCH KINH DOANH & ROI

### 1. LỢI ÍCH ĐỊNH TÍNH

| Lĩnh Vực | Lợi Ích |
|----------|---------|
| **Chất Lượng** | - Giảm 30% defects trong production<br>- Tăng 40% test coverage<br>- Giảm 50% rework |
| **Tốc Độ** | - Giảm 40% release cycle time<br>- Giảm 30% incident MTTR<br>- Giảm 50% request fulfillment time |
| **Rủi Ro** | - Giảm 60% change failures<br>- Tăng visibility 100% về dependencies<br>- Compliance với ITIL/ISO |
| **Chi Phí** | - Giảm 20-30% operational cost<br>- Tối ưu vendor spend<br>- Giảm overtime |
| **Khách Hàng** | - Tăng CSAT từ 0 → 70%<br>- Giảm complaints<br>- Tăng trust với business |

### 2. ROI DỰ KIẾN

#### A. ĐẦU TƯ (2026)
- **Total Investment:** $675K

#### B. LỢI ÍCH ĐỊNH LƯỢNG (Annual Savings from 2027)

| Hạng Mục | Tiết Kiệm/Năm | Cách Tính |
|----------|---------------|-----------|
| **Giảm downtime** | $180K | 30% MTTR reduction × 100 incidents/yr × $6K avg business impact |
| **Giảm rework** | $120K | 50% rework reduction × 2,000 hours/yr × $60/hour |
| **Tăng tốc release** | $150K | 40% faster release × 24 releases/yr × $6.25K opportunity cost |
| **Tối ưu vendor** | $100K | 20% vendor cost reduction × $500K vendor spend |
| **Giảm operational effort** | $90K | Automation saves 30% manual work × 3,000 hours/yr × $30/hour |
| **Tránh compliance penalty** | $50K | Risk mitigation (audit fail penalty avoided) |
| **TỔNG TIẾT KIỆM** | **$690K/năm** | |

#### C. ROI CALCULATION

| Metric | Value |
|--------|-------|
| **Investment (2026)** | $675K |
| **Annual Benefit (2027+)** | $690K |
| **Payback Period** | **11.7 months** |
| **3-Year ROI** | **207%** |
| **NPV (3 years, 10% discount)** | **$990K** |

### 3. KẾT QUẢ KINH DOANH DỰ KIẾN (2027)

| Metric | Baseline | Target 2027 | Improvement |
|--------|----------|-------------|-------------|
| **System Availability** | 98.5% | 99.5% | +1.0% |
| **Incident MTTR** | 6 hours | 4 hours | -33% |
| **Change Failure Rate** | 3-5% | <1% | -80% |
| **Release Frequency** | 24/year | 36/year | +50% |
| **Customer Satisfaction** | N/A | 70% | New |
| **Compliance Score** | 20% | 85% | +325% |

---

## PHẦN I: ĐỀ XUẤT VÀ QUYẾT ĐỊNH CẦN THIẾT

### ĐỀ XUẤT TRƯỚC MẮT (Q4 2025 - TRONG THÁNG 12)

#### 1. PHÊ DUYỆT NGÂN SÁCH

📊 **Yêu cầu phê duyệt:**
- **Ngân sách 2026:** $675K
- **Breakdown:**
  - Q1 2026: $230K (Critical - CMDB tool, 2 hires, consultants)
  - Q2-Q4: $445K (Phased implementation)

#### 2. PHÉP TUYỂN DỤNG

👥 **Yêu cầu phê duyệt tuyển dụng:**
- **CMDB Administrator** (Mid level) - Start date: Jan 2026
- **3rd Party Manager** (Mid-Senior) - Start date: Jan 2026
- **BI/Data Analyst** (Mid level) - Start date: Feb 2026
- **QC Automation Engineer** (Mid level) - Start date: Apr 2026

**Total: 4 FTE - $260K-335K annual cost**

#### 3. PHÂN BỔ NGUỒN LỰC TỪ CÁC BỘ PHẬN

🤝 **Yêu cầu commitment từ:**
- **DevOps Team:** 0.3 FTE (Q1-Q4)
- **Infrastructure Team:** 0.3 FTE (Q1-Q2)
- **Solution Architect:** 0.4 FTE (Q1-Q2)
- **Security Team:** 0.2 FTE (Q2-Q3)
- **Data Science:** 0.2 FTE (Q4)

#### 4. EXECUTIVE SPONSORSHIP

🎯 **Yêu cầu:**
- **Executive Sponsor:** CIO/CTO
- **Steering Committee:** CIO, CTO, CFO, Head of Operations
- **Monthly review meetings:** 1 hour/month
- **Go/No-Go decisions:** Q1 (CMDB tool), Q2 (Budget review)

### YÊU CẦU QUYẾT ĐỊNH

| # | Quyết Định | Người Phê Duyệt | Deadline |
|---|------------|-----------------|----------|
| 1 | Phê duyệt ngân sách $675K | CFO + BOD | 15/12/2025 |
| 2 | Phê duyệt 4 headcount | CEO + HR | 15/12/2025 |
| 3 | CMDB tool selection criteria | CTO + IT Manager | 20/12/2025 |
| 4 | Executive sponsor assignment | CEO | 10/12/2025 |
| 5 | Cross-functional resource commitment | Department Heads | 20/12/2025 |

---

## PHẦN J: KẾT LUẬN

### 1. TẠI SAO CẦN HÀNH ĐỘNG NGAY

🚨 **3 lý do cấp bách:**

1. **Rủi ro kinh doanh cao**
   - CMDB 9% = Không biết hệ thống phụ thuộc → Rủi ro gián đoạn dịch vụ
   - Compliance 0-15% = Rủi ro audit fail → Phạt + tổn hại uy tín
   - 3rd Party 19% = Rủi ro vendor → Chi phí không tối ưu + dependency

2. **Cơ hội cải thiện lớn**
   - Quick wins có thể deliver trong 3 tháng
   - ROI payback 12 tháng
   - Tiết kiệm $690K/năm từ 2027

3. **Đội ngũ sẵn sàng**
   - Team có kinh nghiệm, cam kết
   - Hạ tầng cơ bản đã có (Jira, CI/CD)
   - Chỉ cần bổ sung 4 FTE + framework

### 2. ROADMAP TỔNG QUAN

```
DEC 2025:  Approval & Planning
Q1 2026:   Foundation (Policies, RACI, SLA, CMDB Selection, Hires)
Q2 2026:   Build (CMDB Deploy, Automation, KPI Dashboards)
Q3 2026:   Scale (Integration, 3rd Party, Compliance)
Q4 2026:   Optimize (75% CMDB, Analytics, Assessment)

RESULT:    All 7 areas Level 2 (50-65%), ROI positive
```

### 3. CAM KẾT

Với việc phê duyệt kế hoạch này, chúng tôi cam kết:

✅ **Deliverables:**
- 7 lĩnh vực đạt Level 2 maturity (50-65%)
- CMDB operational với 75%+ coverage
- 50+ KPIs tracking real-time
- Compliance với ITIL/ISO standards
- 5 Quick Wins delivered Q1

✅ **Business Outcomes:**
- Giảm 30% incident resolution time
- Giảm 20-30% operational cost
- Tăng 40% release velocity
- Customer satisfaction 70%
- Zero compliance violations

✅ **Governance:**
- Monthly progress reports to leadership
- Quarterly steering committee reviews
- Transparent budget tracking
- Risk management & escalation

---

## PHỤ LỤC

### A. DANH SÁCH VIẾT TẮT

| Viết Tắt | Nghĩa Đầy Đủ |
|----------|--------------|
| ITSM | IT Service Management - Quản lý Dịch vụ CNTT |
| ITIL | IT Infrastructure Library - Thư viện Hạ tầng CNTT |
| PQA | Process Quality Assurance - Đảm bảo Chất lượng Quy trình |
| QC | Quality Control - Kiểm soát Chất lượng |
| RM | Request Management / Request Fulfillment - Quản lý Yêu cầu |
| CM | Change Management - Quản lý Thay đổi |
| IM | Incident Management - Quản lý Sự cố |
| CMDB | Configuration Management Database - Cơ sở dữ liệu Quản lý Cấu hình |
| CI | Configuration Item - Hạng mục Cấu hình |
| SLA | Service Level Agreement - Thỏa thuận Mức độ Dịch vụ |
| RACI | Responsible, Accountable, Consulted, Informed - Ma trận Trách nhiệm |
| KPI | Key Performance Indicator - Chỉ số Hiệu suất Chính |
| CSAT | Customer Satisfaction - Hài lòng Khách hàng |
| MTTR | Mean Time To Resolve - Thời gian Trung bình Giải quyết |
| MTTA | Mean Time To Acknowledge - Thời gian Trung bình Phản hồi |
| CFR | Change Failure Rate - Tỷ lệ Thất bại Thay đổi |
| RCA | Root Cause Analysis - Phân tích Nguyên nhân Gốc rễ |
| CAB | Change Advisory Board - Hội đồng Tư vấn Thay đổi |
| RFC | Request for Change - Yêu cầu Thay đổi |
| FTE | Full Time Equivalent - Tương đương Toàn thời gian |
| POC | Proof of Concept - Chứng minh Khái niệm |
| ROI | Return on Investment - Lợi nhuận Đầu tư |

### B. LIÊN HỆ VÀ ESCALATION

**Steering Committee:**
- Executive Sponsor: [CIO/CTO Name]
- Project Lead: [ITSM Lead Name]
- Finance: [CFO/Finance Manager Name]

**Escalation Path:**
- Level 1: ITSM Lead
- Level 2: CTO
- Level 3: Executive Sponsor (CIO)

**Monthly Review Schedule:**
- **Day:** Last Friday of each month
- **Time:** 10:00-11:00 AM
- **Attendees:** Steering Committee + Process Owners

---

**BÁO CÁO KẾT THÚC**

**Prepared by:** ITSM Assessment Team
**Date:** 02/12/2025
**Next Review:** 31/01/2026 (Q1 Progress Review)
