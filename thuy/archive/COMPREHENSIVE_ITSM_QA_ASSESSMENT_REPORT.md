# BÁO CÁO TỔNG HỢP ĐÁNH GIÁ ITSM/QA
## Đánh Giá Trưởng Thành 7 Lĩnh Vực Quản Lý Dịch Vụ CNTT

**Ngày thực hiện:** Tháng 11-12/2025
**Phiên bản:** 1.0

---

## TÓM TẮT ĐIỀU HÀNH (EXECUTIVE SUMMARY)

Báo cáo này tổng hợp kết quả đánh giá chi tiết về mức độ trưởng thành của 7 lĩnh vực quản lý dịch vụ CNTT và đảm bảo chất lượng tại tổ chức. Đánh giá được thực hiện dựa trên các tiêu chuẩn ITIL, ISO và best practices quốc tế.

### Kết Quả Tổng Quan

| Lĩnh Vực | Điểm Hiện Tại | Mức Trưởng Thành | Mức Độ Ưu Tiên |
|----------|---------------|-------------------|----------------|
| **1. PQA (Process Quality Assurance)** | 30.5/74 (41.2%) | Level 2: Managed (Low) | HIGH |
| **2. QC (Quality Control)** | 37.0/120 (30.8%) | Level 1: Initial | CRITICAL |
| **3. RM (Release Management)** | 44.0/92 (47.8%) | Level 1: Late Initial | HIGH |
| **4. CM (Change Management)** | 41.5/71 (58.5%) | Level 2: Managed | MEDIUM |
| **5. CMDB (Configuration Management)** | 5.0/53 (9.4%) | Level 1: Initial | CRITICAL |
| **6. IM (Incident Management)** | 27.0/61 (44.3%) | Level 1: Late Initial | HIGH |
| **7. 3rd Party Management** | 9.5/50 (19.4%) | Level 1: Initial | CRITICAL |

### Phát Hiện Chính

**ĐIỂM MẠNH:**
- Governance tương đối tốt ở CM (94%) và PQA (68.8%)
- Quy trình cơ bản đã được định nghĩa ở hầu hết các lĩnh vực
- Đội ngũ có kinh nghiệm và văn hóa hợp tác tốt
- Đã có công cụ quản lý cơ bản (Jira, Excel)

**ĐIỂM YẾU NGHIÊM TRỌNG:**
- **Compliance**: 0-15% ở hầu hết lĩnh vực - Chưa tuân thủ ITIL/ISO
- **CMDB**: 9.4% - Thiếu hệ thống quản lý cấu hình
- **Metrics & Measurement**: 8-23% - Chưa có KPI, dashboard
- **Tools & Automation**: 14-17% - Thủ công, chưa tích hợp
- **Integration**: 10-37% - Các hệ thống hoạt động độc lập

### Mục Tiêu 12 Tháng

**Target:** Đạt Level 2 (Managed) cho TẤT CẢ lĩnh vực với điểm số 50-65%

**Đầu tư ước tính:**
- Nhân lực: 8-12 FTE (Full Time Equivalent)
- Công cụ: $100K-150K
- Đào tạo & Tư vấn: $50K-80K

---

## PHẦN I: PHÂN TÍCH CHI TIẾT TỪNG LĨNH VỰC

### 1. PQA - PROCESS QUALITY ASSURANCE (ĐẢM BẢO CHẤT LƯỢNG QUY TRÌNH)

#### 1.1. Tình Trạng Hiện Tại

**Điểm số:** 30.5/74 = 41.2%
**Mức trưởng thành:** Level 2: MANAGED (LOW)
**Mục tiêu 12 tháng:** Level 2: MANAGED (HIGH) - 50-65%

#### 1.2. Phân Tích Theo Nhóm Tiêu Chí

| Nhóm | Điểm | Tỷ Lệ % | Đánh Giá | Điểm Mạnh | Khoảng Cách |
|------|------|---------|----------|-----------|-------------|
| **Governance** | 5.5/8 | 68.8% | Good | QA độc lập, report CIO/CTO, standards rõ | Chưa có QA Charter, RACI chưa chính thức |
| **Integration** | 3.5/6 | 58.3% | Fair | Phối hợp Security & Compliance | PQA chưa tham gia xuyên suốt quy trình |
| **People** | 3.0/6 | 50.0% | Fair | Có chứng chỉ, độc lập | Nguồn lực mỏng, chưa có competency matrix |
| **Process** | 8.5/18 | 47.2% | Fair | CAPA, RCA, escalation procedure | Tần suất audit thấp (1 lần/năm), coverage 3% |
| **Tools & Data** | 3.0/8 | 37.5% | Poor | Excel lưu trữ cơ bản | Thủ công, chưa tích hợp ITSM |
| **Improvement** | 2.5/7 | 35.7% | Poor | Có cải tiến ad-hoc | Không có backlog, không theo dõi |
| **Compliance** | 3.0/10 | 30.0% | Poor | Có nhận thức tuân thủ | Chưa ánh xạ ISO/ITIL, chưa audit |
| **Metrics** | 1.5/11 | 13.6% | CRITICAL | Ghi nhận rời rạc | Không KPI, dashboard, trending |

#### 1.3. Phát Hiện Chính (Top 10 Critical Gaps)

1. **[CRITICAL] Không có KPI Dashboard và Phân tích xu hướng**
   - Ảnh hưởng: Insight chậm, không đo được giá trị PQA
   - Action: Xác định 3-5 KPI chính, xây Dashboard, phân tích xu hướng
   - Owner: PQA Lead
   - Timeline: Q2/2026

2. **[CRITICAL] Chưa có QA checklist cho các mảng hoạt động**
   - Mảng thiếu: Change Management, Incident Management, Configuration Management, Problem Management
   - Ảnh hưởng: Audit không nhất quán, khó triển khai
   - Action: Xây dựng audit checklist theo best practices
   - Timeline: Q1/2026

3. **[CRITICAL] Tần suất và phạm vi audit hạn chế**
   - Hiện tại: 1 lần/năm, coverage 1/30 quy trình (3%)
   - Target: 1-2 audit/quý/lĩnh vực, coverage 80%
   - Timeline: Q2-Q4/2026

4. **[CRITICAL] Chưa có QA Database, chưa tích hợp ITSM**
   - Ảnh hưởng: Dữ liệu phân tán, phân tích xu hướng chậm
   - Action: Thiết kế Schema QA Database, tích hợp với Jira
   - Timeline: Q1/2026

5. **[CRITICAL] Chưa có danh sách kiểm tra tuân thủ**
   - Ảnh hưởng: Rủi ro audit bên ngoài, không đáp ứng quy định
   - Action: Xây dựng compliance checklist, xác định evidences
   - Timeline: Q1/2026

6. **[HIGH] Cơ cấu quản trị & RACI chưa rõ ràng**
   - Ảnh hưởng: Vai trò lẫn lộn
   - Action: Ban hành QA Charter, RACI matrix
   - Timeline: Q1/2026

7. **[HIGH] Chưa có tiêu chí collect bằng chứng kiểm toán**
   - Action: Xác định tiêu chí bằng chứng, framework đánh giá
   - Timeline: Q1/2026

8. **[HIGH] Chưa có cơ chế escalation**
   - Ảnh hưởng: Vấn đề nghiêm trọng xử lý chậm
   - Action: Xác định tiêu chí và thẩm quyền escalation
   - Timeline: Q1/2026

9. **[HIGH] Chưa có backlog cải tiến**
   - Ảnh hưởng: Cải tiến rời rạc, khó theo dõi
   - Timeline: Q1/2026

10. **[HIGH] Nguồn lực mỏng, chưa có competence matrix**
    - Action: Xây dựng Competency Matrix, kế hoạch tuyển dụng
    - Owner: ITSM Lead + HR
    - Timeline: Q1-Q4/2026

#### 1.4. Quick Wins (Triển Khai Ngay Q4/2025 - Q1/2026)

| # | Quick Win | Effort | Impact | Timeline | Kỳ Vọng |
|---|-----------|--------|--------|----------|---------|
| 1 | Xây dựng Checklist Audit cho CM, IM, PM, Config Mgmt | MEDIUM | HIGH | 31/01/2026 | 4 checklist chuẩn |
| 2 | Thiết kế Schema QA database và lộ trình tích hợp ITSM | MEDIUM | HIGH | 31/01/2026 | Schema & roadmap |
| 3 | Hoàn thiện QA Charter, Scope, RACI Matrix | LOW | HIGH | 15/01/2026 | RACI công bố |
| 4 | Xây dựng Competence Matrix, kế hoạch tuyển dụng | MEDIUM | HIGH | 15/01/2026 | Phê duyệt headcount |
| 5 | Backlog cải tiến | LOW | MEDIUM | 31/01/2026 | Backlog tracking |

#### 1.5. Lộ Trình 12 Tháng

**Quý 1/2026:**
- Xây dựng PQA Charter / mô tả vai trò
- Soạn và ban hành bộ nguyên tắc PQA policy
- Thiết kế quy trình PQA Review chuẩn
- Thiết kế quy trình quản lý Findings & CAPA
- Chuẩn hoá template PQA
- Thiết lập kho lưu trữ tập trung
- Bổ nhiệm vai trò PQA chính thức
- Lập kế hoạch đào tạo năng lực

**Quý 2/2026:**
- Triển khai PQA review định kỳ trên phạm vi thí điểm
- Vận hành log findings tập trung
- Áp dụng quy trình CAPA
- Thiết kế bộ KPI PQA cơ bản
- Xây dựng báo cáo định kỳ cho quản lý
- Triển khai 2-3 mini-improvement

**Quý 3/2026:**
- Rà soát, đánh giá 6 tháng đầu
- Hoàn thiện bộ KPI PQA (5-10 chỉ số)
- Thiết lập backlog cải tiến chính thức
- Mở rộng phạm vi áp dụng PQA
- Gắn checkpoint PQA vào quy trình
- Xây dựng dashboard xu hướng

**Quý 4/2026:**
- Thực hiện reassessment PQA
- Lập báo cáo tổng kết năm
- Xây dựng kế hoạch năm tiếp theo
- Tích hợp sâu hơn với ITSM
- Ánh xạ với yêu cầu tuân thủ
- Hoàn thành cải tiến từ backlog

#### 1.6. KPIs Đề Xuất

| KPI | Baseline | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 |
|-----|----------|---------|---------|---------|---------|
| Mức độ trưởng thành PQA | 30.5/74 (41%) | 35-40/74 (47-54%) | 40-45/74 (54-61%) | 43-47/74 (58-64%) | 45-50/74 (61-68%) |
| Checklist Audit | 0 | 4 checklist | Áp dụng 2 | Áp dụng 4 | - |
| Tần suất Audit | 1/năm | Đợt 1 | Đợt 2 | Đợt 3 | Đợt 4 |
| Phạm vi Audit | 3% | 20% | 35% | 60% | 80%+ |
| Metrics & Dashboard | 0 | 3-5 KPI, Dashboard Manual | KPI hàng tháng | Dashboard & trending | Realtime Dashboard |

---

### 2. QC - QUALITY CONTROL (KIỂM SOÁT CHẤT LƯỢNG)

#### 2.1. Tình Trạng Hiện Tại

**Điểm số:** 37.0/120 = 30.83%
**Mức trưởng thành:** Level 1: INITIAL
**Mục tiêu 12 tháng:** Level 2: MANAGED (45-50%)
**Improvement Gap:** +20%

#### 2.2. Phân Tích Theo Nhóm Tiêu Chí

| Nhóm | Điểm | Tỷ Lệ % | Đánh Giá | Điểm Mạnh | Khoảng Cách |
|------|------|---------|----------|-----------|-------------|
| **People** | 5.5/10 | 55.0% | Fair | QC-Dev collab ổn | Skills yếu automation/edge cases |
| **Governance** | 6.5/15 | 43.3% | Fair | Tổ chức rõ, 90% hiểu | Không có Strategy & Roadmap |
| **Integration** | 5.5/15 | 36.7% | Poor | CI/CD 98% coverage | 1 environment, build not enforced |
| **Process** | 11.0/35 | 31.4% | Poor | Security testing định kỳ | Planning unstd, Coverage unmeasured |
| **Measurement** | 3.5/15 | 23.3% | Poor | RCA via incident review | Không metrics/KPI, dashboard |
| **Data & Tools** | 3.5/20 | 17.5% | Poor | Jira 100% tracking | Không Automation Strategy, TDM |
| **Compliance** | 1.5/10 | 15.0% | Poor | Team organized | Không ITIL/ISO, audit, RTM |

#### 2.3. Đặc Điểm Hiện Tại

**ĐIỂM SÁNG:**
- Tổ chức rõ ràng
- Security testing định kỳ (VA 2x/năm, Pentest, Redteam)
- CI/CD 98% coverage
- QC-Dev collaboration ổn định

**VẤN ĐỀ CRITICAL:**
- Compliance 15% - Không ITIL/ISO, không audit, không traceability
- Data & Tools 17.5% - Không Automation Strategy, adoption 25-30%, không TDM
- Measurement 23% - Không metrics/KPI, reports, dashboards
- Process 31% - Test Planning/Design không chuẩn, Defect chaos, Coverage unmeasured
- Integration 37% - 1 environment, build không fail khi test fail

#### 2.4. Phát Hiện Chính (Top 11 Findings)

**CRITICAL FINDINGS:**

1. **[FC-01] Không có chiến lược và roadmap QC rõ ràng**
   - Ảnh hưởng: Thiếu định hướng dài hạn, không đo lường tiến bộ
   - Action: Xây dựng QC Strategy 3-5 năm với roadmap, KPIs
   - Owner: PQA + QC lead

2. **[FC-02] Không có quy trình test planning chuẩn**
   - Ảnh hưởng: Thiếu tính nhất quán, khó quản lý rủi ro
   - Action: Thiết lập quy trình Test Planning với template
   - Owner: QC lead

3. **[FC-03] Chưa có metrics và KPIs cho QA/QC**
   - Ảnh hưởng: Không đo lường hiệu quả, không chứng minh giá trị
   - Action: Thiết lập KPIs (Test Coverage, Defect Density, Automation Rate)
   - Owner: QC lead

4. **[FC-04] Không đo lường test coverage**
   - Ảnh hưởng: Rủi ro cao untested code
   - Action: Triển khai công cụ đo coverage, thiết lập target
   - Owner: QC lead

5. **[FC-05] Không có chiến lược test automation**
   - Ảnh hưởng: Automation không hướng đi rõ, ROI thấp
   - Action: Xây dựng Test Automation Strategy với roadmap
   - Owner: QC lead

6. **[FC-06] Không có quy trình test data management**
   - Ảnh hưởng: Test data không tin cậy, rủi ro bảo mật
   - Action: Thiết lập TDM strategy với data masking
   - Owner: QC lead

7. **[FC-07] Không tuân thủ chuẩn QC quốc tế**
   - Ảnh hưởng: Không đáp ứng compliance, rủi ro audit
   - Action: Áp dụng ISTQB, ISO 29119, thiết lập traceability
   - Owner: PQA + Compliance

8. **[FC-08] Quy trình Defect Management không chuẩn**
   - Ảnh hưởng: Bugs không xử lý nhất quán
   - Action: Chuẩn hóa với priority/severity matrix, SLA
   - Owner: QC lead

**HIGH/MEDIUM FINDINGS:**

9. **[FC-09] Quality gates không thực thi đầy đủ**
   - Action: Build fail khi test fail, mandatory coverage checks
   - Owner: DevOps + CTO

10. **[FC-10] Chỉ có 1 test environment**
    - Ảnh hưởng: Bottleneck, conflicts giữa teams
    - Action: Thiết lập Dev, SIT, UAT environments
    - Owner: QC lead

11. **[OC-01 đến OC-11]** - 11 findings mức độ LOW-MEDIUM khác

#### 2.5. Quick Wins (Thực Hiện Ngay - Dec 2025)

| # | Quick Win | Effort | Impact | Timeline | Benefit |
|---|-----------|--------|--------|----------|---------|
| 1 | Configure quality gate FAIL build khi test fail | LOW | HIGH | Dec 2025 (1w) | Enforce quality |
| 2 | Formalize QC Policy (Confluence/Wiki) | LOW | MEDIUM | Dec 2025 (2-3w) | Clear guidance |
| 3 | Formalize RCA process documentation | LOW | MEDIUM | Dec 2025 (2-3w) | Capture insights |
| 4 | Establish defect triage ceremony (weekly) | LOW | MEDIUM | Dec 2025 (1-2w) | Structured collab |
| 5 | Document security testing schedule | LOW | MEDIUM | Dec 2025 (1w) | Formalize practice |

**Total Effort:** ~9-10 tuần (phân bổ)

#### 2.6. Lộ Trình 12 Tháng

**Q4 2025 (Target: 35-40%):**
- Quick wins (5 items)
- QC Strategy & Roadmap definition
- Test Planning & Design standardization
- Defect Management process & SLA
- QC Policy formalization

**Q1 2026 (Target: 45-50%):**
- QC metrics dashboard & KPI implementation
- Test Automation Strategy (detailed)
- Test Data Management process design
- ITIL/ISO standards alignment audit
- Training program kickoff

**Q2 2026 (Target: 55-60%):**
- Test automation tool selection & POC
- Environment management enhancement
- Test coverage measurement implementation
- Advanced automation framework development
- RCA process maturity

**Q3 2026 (Target: 65-75%):**
- Full test automation framework rollout
- Performance testing benchmarks
- Regression test suite expansion (80% auto)
- QC maturity assessment (target Level 3)
- Compliance audit preparation

---

### 3. RM - RELEASE MANAGEMENT (QUẢN LÝ YÊU CẦU/PHÁT HÀNH)

#### 3.1. Tình Trạng Hiện Tại

**Điểm số:** 44.0/92 = 47.83%
**Mức trưởng thành:** Level 1: LATE INITIAL
**Mục tiêu 12 tháng:** Level 2: MANAGED (55-65%)
**Improvement Gap:** +20%

#### 3.2. Phân Tích Theo Nhóm Tiêu Chí

| Nhóm | Điểm | Tỷ Lệ % | Đánh Giá | Điểm Mạnh | Khoảng Cách |
|------|------|---------|----------|-----------|-------------|
| **People** | 5/8 | 62.5% | Good | Team đủ, training, cross-training | Chưa training SLA cho user |
| **Governance** | 7/12 | 58.3% | Good | Request types rõ, SLA defined | Vai trò chưa rõ, escalation ad-hoc |
| **Process** | 11/20 | 55.0% | Fair | Multi channels, self-service, notification | Auto categorization 0%, approval ad-hoc |
| **Tools & Data** | 6.5/12 | 54.2% | Fair | Jira workflow, SLA alerts | CMDB không update, KB không link |
| **Compliance** | 4/8 | 50.0% | Fair | Data protection, RBAC | Authorization check 0%, audit trail ad-hoc |
| **Integration** | 3.5/8 | 43.8% | Poor | Service Desk tracking | Request-incident manual, CMDB không auto |
| **Improvement** | 4.5/12 | 37.5% | Poor | Có cải tiến ad-hoc | Không review định kỳ, procedures không update |
| **Measurement** | 2.5/12 | 20.8% | CRITICAL | Dashboard tồn tại | Không KPI, volume, SLA%, cycle time |

#### 3.3. Đặc Điểm Hiện Tại

**STRENGTHS:**
- Có hệ thống quản lý request (Jira) với tracking
- Request được phân loại (2 flows chính)
- Team đủ nhân lực (62.5%)
- Real-time status tracking
- User notification khi hoàn thành

**WEAKNESSES:**
- **CRITICAL** - Measurement 20.8%: Không track volume, SLA%, cycle time, quality metrics
- **HIGH** - Process 55%: Auto categorization 0%, manual routing, ad-hoc assignment, quality check partial
- **HIGH** - Tools 54.2%: CMDB không update, KB chưa link
- **MEDIUM** - Integration 43.8%: Request-incident linking manual
- **MEDIUM** - Improvement 37.5%: Không review định kỳ

#### 3.4. Phát Hiện Chính (Top 10 Critical Gaps)

1. **[F1-F2][CRITICAL] Không có hệ thống đo lường - Thiếu KPI**
   - Metrics thiếu: volume, SLA%, cycle time, quality
   - Ảnh hưởng: Lãnh đạo không có basis quyết định
   - Action: Xây framework KPI, auto-collect từ Jira, Dashboard
   - Owner: RM lead
   - Timeline: Q1/2026

2. **[CRITICAL] Không có satisfaction survey**
   - Ảnh hưởng: Không biết quality từ user perspective
   - Action: Setup survey post-fulfillment, định kỳ phân tích
   - Timeline: Q1/2026

3. **[HIGH] Vai trò/trách nhiệm không rõ**
   - Ảnh hưởng: Delay xử lý, mất efficiency
   - Action: Viết rõ vai trò, RACI matrix, approval workflow
   - Timeline: Q1/2026

4. **[HIGH] Phân loại yêu cầu 100% thủ công**
   - Ảnh hưởng: Tốn thời gian, misrouting, delay
   - Action: Analyze request types, xây auto-classification (target 80% accuracy)
   - Timeline: Q1/2026

5. **[HIGH] QA/verification không chuẩn (50% partial)**
   - Ảnh hưởng: Chất lượng không đảm bảo, rework cao
   - Action: Define acceptance criteria, verification checklist, QA stage
   - Owner: PQA
   - Timeline: Q2/2026

6. **[HIGH] Standard vs Non-Standard không phân biệt**
   - Ảnh hưởng: SLA không phù hợp
   - Action: Define tiêu chí, thiết lập SLA khác biệt
   - Timeline: Q2/2026

7. **[MEDIUM] Không có Service Review định kỳ**
   - Ảnh hưởng: Vấn đề không phát hiện hệ thống
   - Action: Service Review hàng tháng, phân tích KPI
   - Owner: ITSM lead
   - Timeline: Q1/2026

8. **[MEDIUM] Request-incident linking thủ công**
   - Ảnh hưởng: CMDB không đầy đủ, traceability yếu
   - Action: Auto-linking rules, auto-update CMDB
   - Owner: RM lead + IM lead
   - Timeline: Q3/2026

9. **[MEDIUM] Authorization check không formal (0%)**
   - Ảnh hưởng: Rủi ro bảo mật, không tuân thủ audit
   - Action: Workflow authorization formal, logging toàn diện
   - Owner: RM lead + PQA
   - Timeline: Q3/2026

10. **[MEDIUM] Knowledge Base không integrate**
    - Ảnh hưởng: User không biết self-service
    - Action: Integrate KB, gợi ý articles khi tạo request
    - Timeline: Q1/2026

#### 3.5. Quick Wins (Q4 2025 - Q1 2026)

| # | Quick Win | Effort | Impact | Timeline | Expected |
|---|-----------|--------|--------|----------|----------|
| 1 | Build metrics framework & KPI dashboard | MEDIUM | HIGH | 15/01/2026 | Dashboard operational |
| 2 | Document roles, approval workflows | LOW | HIGH | 20/12/2025 | Clarity achieved |
| 3 | Implement auto-routing & quality checklist | HIGH | HIGH | 28/02/2026 | 80% auto-routing |
| 4 | Monthly service review cadence | LOW | MEDIUM | 15/12/2025 | Regular reviews |
| 5 | Auto-linking, CMDB update, auth checks | HIGH | HIGH | 31/03/2026 | Integration live |

#### 3.6. Lộ Trình 12 Tháng

**GIAI ĐOẠN 1: XÂY DỰNG NỀN TẢNG (Dec 2025 - Jan 2026) → 48-52 điểm**

1. GOVERNANCE FORMALIZATION
   - Làm rõ vai trò (Coordinator, Approver, Fulfiller, Manager)
   - RACI matrix cho mỗi loại request
   - Approval Workflow từng loại
   - Escalation paths
   - Update Request Management Policy

2. MEASUREMENT FRAMEWORK SETUP
   - Xác định KPI (volume, SLA%, cycle time, quality, cost)
   - Thiết kế dashboard structure
   - Cấu hình Jira reports tự động
   - Collect baseline data

3. SERVICE REVIEW CADENCE
   - Lịch họp hàng tháng
   - Agenda: KPI analysis, bottleneck, improvement
   - Template documenting

4. QUALITY BASELINE
   - Verification checklist per request type
   - Acceptance criteria
   - Huấn luyện QA team

**GIAI ĐOẠN 2: TỰ ĐỘNG HÓA & CẢI THIỆN (Feb - Mar 2026) → 52-60 điểm**

1. INTELLIGENT REQUEST ROUTING
   - Phân tích patterns → categorization rules
   - Cấu hình routing logic (80% accuracy)
   - Fallback manual process
   - Monitor & adjust

2. QUALITY ASSURANCE IMPLEMENTATION
   - Deploy QA verification stage
   - Tích hợp checklist vào workflow
   - Defect/rework tracking
   - Quality metrics dashboard

3. KNOWLEDGE BASE INTEGRATION
   - Kết nối KB platform
   - Auto-suggest KB articles
   - Train team maintenance

4. SATISFACTION MEASUREMENT
   - Post-fulfillment survey
   - Integrate vào notification
   - Collect & aggregate scores
   - Analyze trends

**GIAI ĐOẠN 3: MỞ RỘNG & TỐI ƯU HÓA (Apr - Jun 2026) → 58-65 điểm**

1. SELF-SERVICE EXPANSION
   - Expand coverage (30-40% volume)
   - Improve portal UX
   - Automate more request types
   - Track success rate

2. ADVANCED ANALYTICS
   - Cost per request baseline
   - Forecasting models
   - Bottleneck analysis
   - Executive dashboard

3. INTEGRATION WITH ITSM
   - Auto-link requests to incidents
   - CMDB updates from fulfillment
   - Map to business services
   - Relationship tracking

4. PEOPLE DEVELOPMENT
   - Advanced training
   - Peer support & knowledge sharing
   - Best practices documentation
   - Performance recognition

5. CONTINUOUS IMPROVEMENT CULTURE
   - Improvement ideas submission
   - Backlog management
   - Regular optimization reviews

#### 3.7. KPIs Đề Xuất

| KPI | Hiện Tại | Q1 2026 | Q2 2026 | Cách Đo |
|-----|----------|---------|---------|---------|
| **VOLUME & CAPACITY** |
| Requests per Month | Không track | Baseline + 5% | Stabilized | Jira report (hàng tuần) |
| **SLA & TIMELINESS** |
| SLA Compliance % | 0% | 85% by Q2 | 90% by Q4 | Weekly SLA report |
| Average Cycle Time | Unknown | < 3 days | < 2.5 days | Jira metrics |
| Approval Turnaround | 1-5 days | < 1 day (90%) | < 4 hours | Workflow tracking |
| **QUALITY** |
| First Time Success % | 0% | 90% | 95% | QA verification |
| Rework Rate | ~3-5% | < 2% | < 1% | Quality analytics |
| User Satisfaction | 0% | 3.0/5 (60%) | 3.5/5 (70%) | Survey |
| **EFFICIENCY** |
| Auto-Categorization % | 0% | 80% | 90% | Routing metrics |
| Self-Service Rate | ~5-10% | 30% | 40-50% | Portal logs |

---

### 4. CM - CHANGE MANAGEMENT (QUẢN LÝ THAY ĐỔI)

#### 4.1. Tình Trạng Hiện Tại

**Điểm số:** 41.5/71 = 58.45%
**Mức trưởng thành:** Level 2: MANAGED
**Mục tiêu 12 tháng:** Level 3: DEFINED (65-70%)

#### 4.2. Phân Tích Theo Nhóm Tiêu Chí

| Nhóm | Điểm | Tỷ Lệ % | Đánh Giá | Điểm Mạnh | Khoảng Cách |
|------|------|---------|----------|-----------|-------------|
| **Governance** | 7.5/8 | 93.8% | Excellent | Quy trình rõ, RACI 90%, CAB setup | RACI chưa ban hành, CAB chưa họp định kỳ |
| **Metrics** | 8.5/11 | 77.3% | Good | SLA tracking, CFR<5%, Dashboard | Chưa tự động hóa CFR, RCA chưa quy trình |
| **Tools & Data** | 7.0/10 | 70.0% | Fair | Jira 100%, Audit trail đầy đủ | Chưa quy định backup, không DR policy |
| **Process** | 12.5/21 | 59.5% | Fair | RFC template rõ, PIR, Rollback 1-2% | Template dài, Risk chưa chuẩn, MW ad-hoc |
| **Improvement** | 0.5/1 | 50.0% | Fair | Có cải tiến từng trường hợp | Không backlog, freeze chưa document |
| **People** | 4.5/10 | 45.0% | Poor | Nhân sự nắm rõ vai trò | Training tự học, không Competency Matrix |
| **Integration** | 1.5/7 | 21.4% | Very Poor | Phối hợp DevOps, Security | RFC from Incident manual, chưa CMDB |
| **Compliance** | 0.0/4 | 0.0% | CRITICAL | Chưa có điểm mạnh | Chưa audit, không checklist |

#### 4.3. Đặc Điểm Hiện Tại

**STRENGTHS:**
- Quy trình CM chính thức & documented
- SLA tracking, CFR < 5%
- Jira tracking 100%
- Governance 94% excellent
- Metrics 77% good

**WEAKNESSES:**
- **CRITICAL** - Compliance 0%: Chưa audit, không checklist
- **Very Poor** - Integration 21%: Manual RFC, chưa CMDB
- **Poor** - People 45%: Training hạn chế, Competency matrix chưa cụ thể
- **Fair** - Process: Không MW policy, risk framework yếu, freeze ad-hoc

#### 4.4. Phát Hiện Chính (Top 19 Findings)

**CRITICAL FINDINGS:**

1. **Phân tích rủi ro chưa có thang đánh giá**
   - Ảnh hưởng: Không phân loại mức rủi ro, escalation không rõ
   - Action: Tạo thang 1-5, tiêu chí high-risk, escalation path
   - Owner: CM + CAB + PQA
   - Timeline: Q1/2026

2. **Chưa có quy định lưu trữ và backup dữ liệu CR**
   - Ảnh hưởng: Không biết thời gian lưu, không DR plan
   - Action: Chính sách retention (1-3-5 năm), backup hàng tháng, test restore
   - Owner: CM + Infra
   - Timeline: Q1/2026

3. **Chưa triển khai Audit CM**
   - Ảnh hưởng: Không track tuân thủ, không đánh giá rủi ro vi phạm
   - Action: Lịch compliance audit, scope & checklist, vi phạm & khắc phục
   - Owner: CM + PQA
   - Timeline: Q1/2026

**HIGH FINDINGS:**

4. **CR template quá dài**
   - Action: Đơn giản hóa theo loại CR, bổ sung KMS
   - Owner: CM + Dev + CAB + PQA
   - Timeline: Q1/2026

5. **Communication Plan chưa cụ thể**
   - Action: Xác định stakeholder groups, lịch pre/during/post-change
   - Owner: CM + Product + PQA
   - Timeline: Q1/2026

6. **CAB thiếu tiêu chí & họp định kỳ**
   - Action: Tiêu chí đánh giá, lịch họp định kỳ, decision log
   - Owner: CM + CAB
   - Timeline: Q1/2026

7. **RACI chưa có tài liệu chính thức**
   - Action: Ban hành RACI, cơ chế cập nhật
   - Owner: CM + PQA
   - Timeline: Q1/2026

8. **CFR Root Causes chưa phân tích**
   - Action: Phân tích top 3 nguyên nhân CFR
   - Owner: CM + Dev + PQA
   - Timeline: Q1/2026

9. **Incident-Change Linkage manual**
   - Action: Query tự động, API integration, test & train
   - Owner: CM + IM + Dev + PQA
   - Timeline: Q1/2026

10. **CMDB Integration chưa có**
    - Action: Xác định core CIs, ánh xạ CR-CIs, tích hợp Jira
    - Owner: CM + Dev + Infra
    - Timeline: Q2/2026

11. **Sonar tạm dừng**
    - Action: Restart Sonar
    - Owner: DevOps

**MEDIUM FINDINGS:**

12-19. PIR chưa CI/CD, MW chưa criticality-based, Freeze periods chưa rõ, Dashboard chưa auto, Batch Approval chưa có, Feedback chưa backlog, Training chưa chuyên sâu, Chứng chỉ CM chưa định rõ

#### 4.5. Quick Wins (Q1 2026)

| # | Quick Win | Category | Effort | Impact | Timeline |
|---|-----------|----------|--------|--------|----------|
| 1 | Risk Assessment Framework | Process | Low-Med | High | Q1 2026 |
| 2 | Maintenance Window SLA | Policy | Medium | High | Q1 2026 |
| 3 | Change Freeze Calendar 2026 | Planning | Low | Medium | Dec 2025 |
| 4 | High-Risk Approval Workflow | Automation | Medium | High | Q1 2026 |
| 5 | RACI Formal Document | Governance | Low | Medium | Q1 2026 |
| 6 | RFC Template Simplification | Tools | Low-Med | Medium | Q2 2026 |

#### 4.6. Lộ Trình 12 Tháng

**Q1 2026 (50% → 55%):**
1. Thiết kế Risk Assessment 5x5 (High/Medium/Low)
2. Policy Maintenance Window & Freeze Calendar 2026
3. Thiết kế lại RACI, CAB roles, lịch họp
4. Review & simplify RFC Template
5. Khung Competency cho Change Manager

**Q2 2026 (55% → 60%):**
6. Go-live Risk 5x5 trong Jira + training
7. Go-live Maintenance Window + dashboard
8. Chọn tool CMDB & POC 1-2 domain
9. Ban hành Data Retention Policy
10. Plan Compliance & Internal Audit lần 1

**Q3 2026 (60% → 63%):**
11. Re-enable Sonar & CI/CD validation
12. CMDB load 20-30% CI + liên kết CR
13. Thực hiện Internal Audit lần 1
14. Triển khai Incident-Change linkage

**Q4 2026 (63% → 65-70%):**
15. Mở rộng CMDB 40-50% CI
16. Tự động update CMDB từ pipeline
17. Risk Dashboard, Change KPIs
18. Khắc phục findings từ audit
19. Pilot Batch Approval theo service
20. Re-assessment & Roadmap 2027

#### 4.7. KPIs Đề Xuất

| KPI | Hiện tại (Dec 2025) | Q1 2026 | Q2 2026 | Q4 2026 |
|-----|---------------------|---------|---------|---------|
| RFC Processing Time | 2-4h | 2-3h | 1-2h | ≤2h |
| SLA Compliance % (Evaluation) | 75% | 80% | 85% | 90% |
| SLA Compliance % (Approval) | 97% | 97% | 98% | 99% |
| Change Failure Rate | 1-2% | 1-2% | ≤1% | ≤0.8% |
| Rollback Rate | 1-2% | 1-2% | ≤1% | ≤0.8% |
| On-time Implementation % | 95% | 95% | 96% | 97% |
| Emergency Change % | Ad-hoc | Track, ≤10% | ≤8% | ≤5% |
| High-Risk Changes % | 0% (không phân loại) | 10-20% | 15-25% | 20-30% |
| RFC Quality Score | 3.5/5 | 4/5 | 4.2/5 | 4.5/5 |
| CMDB Coverage % | 0% | ≥20% | 40-50% | 75%+ |
| CI/CD Automation Coverage % | 0% (stopped) | 20% | 50% | 70% |

---

### 5. CMDB - CONFIGURATION MANAGEMENT DATABASE

#### 5.1. Tình Trạng Hiện Tại

**Điểm số:** 5.0/53 = 9.34%
**Mức trưởng thành:** Level 1: INITIAL
**Mục tiêu 12 tháng:** Level 2: MANAGED (45-60%)
**Gap:** +50 điểm (~40-50%)

**ĐÂY LÀ LĨNH VỰC YẾU NHẤT - CẦN ƯU TIÊN CAO NHẤT**

#### 5.2. Phân Tích Theo Nhóm Tiêu Chí

| Nhóm | Điểm | Tỷ Lệ % | Đánh Giá |
|------|------|---------|----------|
| **Governance** | 2.5/12 | 20.8% | Fair |
| **Process** | 3.5/20 | 17.5% | Poor |
| **Tools & Data** | 0.0/16 | 0.0% | Poor |
| **Integration** | 0.0/8 | 0.0% | Poor |
| **Metrics** | 1.0/12 | 8.3% | Poor |
| **Compliance** | 0.5/8 | 6.2% | Poor |
| **People** | 0.5/8 | 6.2% | Poor |
| **Improvement** | 0.5/12 | 4.2% | Poor |

#### 5.3. Đặc Điểm Hiện Tại

**STRENGTHS (Rất Hạn Chế):**
- Có sơ bộ phân loại CIs (Servers, Apps, DBs)
- Infrastructure Team có kinh nghiệm
- Có data cơ bản trong Excel
- Có ý thức CM importance

**WEAKNESSES (Nghiêm Trọng):**
- **KHÔNG có chính sách CM formal**
- **KHÔNG có tool chuyên dụng (chỉ Excel)**
- **KHÔNG có integration Incident/Change**
- **KHÔNG có audit trail**
- **KHÔNG có accountability**
- **Coverage < 50% CIs**

#### 5.4. Phát Hiện Chính (14 Critical Gaps)

**TOP PRIORITY (CRITICAL):**

1. **Chưa có policy CMDB chính thức**
   - Ảnh hưởng: Không rõ CI types, scope, quyền hạn
   - Action: Xây dựng policy (CI types, scope, roles, approval)
   - Owner: Service Manager
   - Timeline: Q1/2026

2. **Chưa có CMDB tool chuyên dụng**
   - Hiện dùng Excel → không scale, không integrate, không audit trail
   - Action: Đánh giá và lựa chọn tool CMDB
   - Owner: IT Manager
   - Timeline: Q1/2026

3. **Không có quy trình identify & classify CIs mới**
   - Ảnh hưởng: 40% hạ tầng mới không tracked
   - Action: Tạo intake form & CI review process
   - Owner: CMDB Admin
   - Timeline: Q1/2026

**HIGH PRIORITY:**

4. **Chưa map CI relationships & dependencies**
   - Ảnh hưởng: Không tính impact được
   - Action: Map service-to-CI cho top 10 services
   - Owner: Solution Architect
   - Timeline: Q1/2026

5. **Không có audit trail & audit process**
   - Ảnh hưởng: Không track thay đổi, rủi ro compliance
   - Action: Setup audit logging, monthly audits
   - Owner: IT Operations
   - Timeline: Q2/2026

6. **Không có CMDB Steward role**
   - Ảnh hưởng: Không ai quản lý tổng thể
   - Action: Assign CMDB Steward
   - Owner: IT Manager
   - Timeline: Q1/2026

7. **CI Owners không gán rõ**
   - Ảnh hưởng: Không ai chịu trách nhiệm accuracy
   - Action: Gán CI Owner cho mỗi hệ thống
   - Owner: Service Manager
   - Timeline: Q1/2026

8. **Không có KPI đo CMDB effectiveness**
   - Action: Define metrics, create dashboard
   - Owner: Data Analyst
   - Timeline: Q2/2026

9. **CMDB không integrate Incident & Change**
   - Ảnh hưởng: Workflows không dùng data, không update
   - Action: Integrate CMDB with tools
   - Owner: Tool Admin
   - Timeline: Q3/2026

10. **Không có data quality standards**
    - Ảnh hưởng: Duplicate CIs, inconsistent data
    - Action: Define quality standards, validation
    - Owner: Data Steward
    - Timeline: Q2/2026

**MEDIUM PRIORITY:**

11-14. CMDB search slow, lifecycle management không có, Change không auto-update, không auto-population từ monitoring

**PEOPLE:**

15. **CMDB team part-time, không training**
    - Action: Assign dedicated CMDB Admin, provide training
    - Owner: HR + IT Manager
    - Timeline: Q1/2026

#### 5.5. Quick Wins (Ngay Lập Tức)

| # | Quick Win | Effort | Impact | Timeline | Success Criteria |
|---|-----------|--------|--------|----------|------------------|
| 1 | CMDB Policy Charter Document | Low (2-3 days) | High | Week 1-2 | Policy approved |
| 2 | CI Owner Assignment & CMDB Steward | Low (1 day) | High | Week 1 | 100% critical CIs have owners |
| 3 | CI Classification & Naming Convention | Low (3-4 days) | High | Week 1-2 | Convention enforced |
| 4 | Improve Excel CMDB Search | Low (2-3 days) | Medium | Week 4-6 | Search < 1 min |
| 5 | CI Metrics Dashboard Setup | Low (2 days) | Medium | Week 6-8 | Monthly report |

#### 5.6. Lộ Trình 12 Tháng (Aggressive Plan)

**Q4 2025 & Q1 2026 (Nền Tảng):**
1. Create CMDB Policy Charter (Week 1-2)
2. Assign CMDB Steward & CI Owners (Week 1)
3. Define CI Classification & Naming (Week 1-2)
4. Improve Excel CMDB (Week 4-6)
5. Create CI Metrics Dashboard (Week 6-8)
6. Establish CI Identification Process (Week 4-8)
7. Setup audit trail & process (Month 2)
8. Map CI relationships & dependencies (Month 2-3)
9. **EVALUATE CMDB TOOL (Start Week 8)**
10. **DEPLOY CMDB Tool (Month 3-4)**

**Q2 2026 (Tool Deployment):**
11. Integrate CMDB with Incident Management (Month 4)
12. Integrate CMDB with Change Management (Month 4-5)
13. Load 20-30% critical CIs
14. Define data quality standards
15. Setup CI lifecycle management

**Q3 2026 (Scale Up):**
16. Expand CMDB to 40-50% CIs
17. Auto-population from monitoring tools
18. Improve CMDB search & reporting
19. Compliance audit preparation

**Q4 2026 (Optimization):**
20. CMDB coverage 75%+
21. Auto-update from Change pipeline
22. Performance optimization
23. Re-assessment
24. Roadmap 2027

#### 5.7. KPIs Đề Xuất (28 KPIs Toàn Diện)

| KPI | Dec 2025 | Q4 2026 (12M) | Q4 2027 (24M) | Category |
|-----|----------|---------------|---------------|----------|
| **DATA QUALITY** |
| CMDB CI Coverage % | 0% | 80%+ | 95%+ | Data |
| IT Assets in CMDB | 0 | 500-600 | 650+ | Data |
| CI Data Quality Score | 0% | 95%+ | 99%+ | Data |
| CI Relationship Completeness | 0% | 85%+ | 98%+ | Data |
| Dependency Mapping Coverage | 0% | 75%+ | 95%+ | Data |
| **INTEGRATION** |
| Auto CI Creation % | 0% | 70%+ | 95%+ | Integration |
| CI/CD Sync Latency | - | <100ms | <20ms | Integration |
| RFC-CI Linkage % | 0% | 85%+ | 99%+ | Integration |
| Incident-CI Auto-Link % | 0% | 80%+ | 95%+ | Integration |
| Auto RFC Generation % | 0% | 70%+ | 95%+ | Integration |
| **BUSINESS VALUE** |
| Service Mapping Coverage | 0% | 70%+ | 95%+ | Business |
| Impact Analysis Accuracy | 0% | 85%+ | 95%+ | Business |
| Change Decision Time Reduction | 0% | 40%+ | 60%+ | Business |
| MTTR Improvement from CMDB | 0% | 35%+ | 60%+ | Business |
| **COMPLIANCE** |
| CMDB Compliance Score | 0% | 85%+ | 98%+ | Compliance |
| Unauthorized Change Detection | 0 | 35-40/mo | 50+/mo | Compliance |
| Audit Trail Completeness | 0% | 95%+ | 99%+ | Compliance |
| Config Drift Detection | 0 | 30-35/mo | 50+/mo | Compliance |
| **PERFORMANCE** |
| CMDB Query Performance | - | <200ms | <50ms | Performance |
| CMDB System Availability | 0% | 99% | 99.9% | Performance |
| Import/Sync Automation % | 0% | 85%+ | 99%+ | Performance |
| **ADOPTION** |
| CMDB User Adoption % | 0% | 85%+ | 98%+ | Adoption |
| CMDB Maturity Level | 0 | 3 | 4+ | Adoption |
| **RESOURCE** |
| Implementation Cost | TBD | $100-120K | $130K+ | Resource |
| CMDB Effort Allocation | 0 | 1-2 man-mo | 0.3-0.5 | Resource |
| ROI from CMDB | 0% | 40%+ | 150%+ | Resource |
| **PEOPLE** |
| Staff Training Completion % | 0% | 70%+ | 95%+ | People |
| Team CMDB Certification % | 0% | 50%+ | 95%+ | People |

---

### 6. IM - INCIDENT MANAGEMENT (QUẢN LÝ SỰ CỐ)

#### 6.1. Tình Trạng Hiện Tại

**Điểm số:** 27.0/61 = 44.3%
**Mức trưởng thành:** Level 1.8: LATE INITIAL
**Mục tiêu 12 tháng:** Level 3: DEFINED (60-70%)

#### 6.2. Phân Tích Theo Nhóm Tiêu Chí

| Nhóm | Tỷ Lệ % | Đánh Giá | Điểm Mạnh | Điểm Yếu |
|------|---------|----------|-----------|----------|
| **Improvement** | 66.7% | Good | Review, RCA, action tracking | - |
| **Process** | 50.0% | Fair | Quy trình defined, phân loại tốt | Escalation ad-hoc |
| **People** | 50.0% | Fair | Team engaged, blame-free culture | Training & cert thiếu |
| **Measurement** | 50.0% | Fair | Volume tracking, exec reporting | KPI & CSAT chưa có |
| **Tools** | 40.9% | Fair | Jira multi-channel, Dashboard Grafana | Automation thiếu |
| **Compliance/ITIL** | 33.3% | Poor | - | ITIL=0%, audit yếu |
| **Governance** | 17.0% | Very Poor | - | IM role chưa rõ |
| **Integration** | 16.7% | Very Poor | - | Chưa CMDB, link thủ công |

#### 6.3. Đặc Điểm Hiện Tại

**STRENGTHS:**
- Hệ thống IM chính thức (Jira + Grafana) - 100%
- Quy trình IM end-to-end - 83%
- Phân biệt Incident vs Request - 100%
- Có review & RCA - 67%
- Good culture (blame-free) - 62%

**WEAKNESSES:**
- KHÔNG có Incident Manager role (17%)
- KHÔNG approve SLA formal (25%)
- Escalation path ad-hoc (25%)
- KHÔNG có workflow automation (20%)
- KHÔNG integrate ITSM (17%)
- KHÔNG có ITIL compliance (0%)
- KHÔNG có audit trail

#### 6.4. Phát Hiện Chính (8 Key Findings)

1. **[CRITICAL] Integration ITSM ≈ 0**
   - Ảnh hưởng: Không link Incident-Problem-Change, khó trace root cause
   - Action: ITSM roadmap, CMDB scope, workflow chuẩn
   - Owner: IT Architect
   - Timeline: Q3-Q4/2026

2. **[CRITICAL] Chưa khung tuân thủ ITIL/ISO, audit trail yếu**
   - Ảnh hưởng: Không chứng minh compliance, khó pass audit
   - Action: Map ITIL 4, compliance checklist, audit trail system
   - Owner: Service Manager
   - Timeline: Q2-Q3/2026

3. **[HIGH] Automation = 0 (manual routing, priority, creation)**
   - Ảnh hưởng: MTTA/MTTR cao, dễ miss alert
   - Action: Jira auto: tạo incident, priority, assignment, notification
   - Owner: IM Manager + Jira Admin
   - Timeline: Q2-Q3/2026

4. **[HIGH] Roles & escalation chưa rõ (17%)**
   - Ảnh hưởng: Sự cố lớn không rõ ai quyết định
   - Action: Incident Manager, RACI, escalation path 3 cấp + authority
   - Owner: Head IT Ops
   - Timeline: Q1/2026

5. **[HIGH] SLA severity chưa rõ & chưa đồng thuận (25%)**
   - Ảnh hưởng: Không expectation, khó ưu tiên
   - Action: Workshop SLA P1-P4 (Response/Diagnosis/Resolution)
   - Owner: IM Manager
   - Timeline: Q1/2026

6. **[MEDIUM] Chưa có KPI IM formal & CSAT = 0**
   - Ảnh hưởng: Dashboard nhưng không target
   - Action: Chốt 10-12 KPI, define công thức, dashboard
   - Owner: IM Manager + BI
   - Timeline: Q1-Q2/2026

7. **[MEDIUM] Đào tạo ITIL/IM chưa có, IM Manager chưa rõ**
   - Ảnh hưởng: Team theo kinh nghiệm, khó scale
   - Action: ITIL training, xác định IM role & career path
   - Owner: HR + Service Manager
   - Timeline: Q2-Q3/2026

8. **[MEDIUM] Data quality & knowledge base yếu (37.5%)**
   - Ảnh hưởng: Báo cáo khó tin, khó tra cứu, lặp lỗi
   - Action: Rule mandatory fields, standardize template, xây KB/FAQ
   - Owner: IM Manager + Knowledge Mgr
   - Timeline: Q2/2026

#### 6.5. Lộ Trình 12 Tháng

**PHASE 1: 0-3 THÁNG (Dec 2025 - Mar 2026)**
1. Định nghĩa & phê duyệt SLA P1-P4
2. Thiết kế Escalation path 3 cấp
3. Xác định & bổ nhiệm Incident Manager
4. Xây RACI cho toàn bộ quy trình IM
5. Chốt bộ KPI IM & dashboard

**PHASE 2: 3-6 THÁNG (Apr - Jun 2026)**
6. Cấu hình Jira SLA automation (breach, warning)
7. Cài rule auto-priority & auto-routing
8. Triển khai quy trình đo & báo cáo KPI
9. Rollout CSAT survey
10. Chuẩn hóa template ticket & data quality

**PHASE 3: 6-12 THÁNG (Jul - Dec 2026)**
11. Thiết kế ITSM integration roadmap + CMDB
12. Tích hợp Incident-Problem-Change
13. Thiết kế audit trail cho IM
14. Xây ITIL 4 compliance checklist
15. Xây & mở rộng Knowledge Base
16. Đào tạo ITIL Foundation

#### 6.6. KPIs (Cần Định Nghĩa Q1/2026)

**Chỉ số cần track:**
- Incident Volume by Severity (P1/P2/P3/P4)
- MTTA (Mean Time to Acknowledge)
- MTTD (Mean Time to Diagnose)
- MTTR (Mean Time to Resolve)
- SLA Compliance % by Severity
- Escalation Rate
- First Call Resolution %
- Incident Reopen Rate
- Major Incident Count
- CSAT Score
- Automation Rate
- Knowledge Base Usage

---

### 7. 3RD PARTY MANAGEMENT (QUẢN LÝ ĐỐI TÁC BÊN THỨ BA)

#### 7.1. Tình Trạng Hiện Tại

**Điểm số:** 9.5/50 = 19.4%
**Mức trưởng thành:** Level 1: INITIAL
**Mục tiêu 12 tháng:** Level 2: MANAGED (45-60%)

#### 7.2. Phân Tích Theo Nhóm Tiêu Chí

| Nhóm | Điểm | Tỷ Lệ % | Đánh Giá | Điểm Mạnh | Khoảng Cách |
|------|------|---------|----------|-----------|-------------|
| **Process** | 2.5/9 | 27.8% | Poor | SLA definition, contract negotiation | Evaluation ad-hoc, tracking manual |
| **Governance** | 1.5/6 | 25.0% | Poor | Vendor classification cơ bản | Policy, roles chưa rõ |
| **Compliance** | 1.5/6 | 25.0% | Poor | Security assessment first-time | ISO/SOC2 chưa enforce |
| **People** | 1.0/4 | 25.0% | Poor | Ownership mindset bắt đầu | Không dedicated, competency chưa defined |
| **Improvement** | 1.0/6 | 16.7% | Poor | - | Risk mitigation chưa documented |
| **Tools & Data** | 1.0/7 | 14.3% | Poor | - | Không VMS, hợp đồng scattered |
| **Integration** | 0.5/5 | 10.0% | Poor | - | Vendor incidents không ITSM |
| **Measurement** | 0.5/6 | 8.3% | Poor | - | KPI/metric=0, dashboard=0 |

#### 7.3. Đặc Điểm Hiện Tại

**STRENGTHS (Rất Hạn Chế):**
- Có phân loại vendor cơ bản (nội bộ/bên ngoài)
- Có NDA nhưng chưa rõ ràng
- Có SLA definition
- Có security assessment ban đầu

**WEAKNESSES (Toàn Diện):**
- Policy chính thức chưa có
- Tools & Data 14% - Không VMS
- Measurement 8% - Chưa có KPI
- Integration 10% - Manual tracking
- Process 28% - Ad-hoc evaluation
- Compliance 25% - Chưa enforce standards

#### 7.4. Phát Hiện Chính (8 Critical Gaps)

1. **[CRITICAL] Chưa có 3rd party policy chính thức**
   - Ảnh hưởng: Không rõ scope, quyền hạn, escalation
   - Action: Xây dựng policy
   - Owner: Governance/ITAM
   - Timeline: 01/2026

2. **[CRITICAL] Chưa có VMS (Vendor Management System)**
   - Ảnh hưởng: Data scattered, no centralized tracking
   - Action: Lựa chọn/setup VMS
   - Owner: IT Ops/ITAM
   - Timeline: 03/2026

3. **[CRITICAL] Vendor evaluation ad-hoc, chưa RFP/RFQ**
   - Ảnh hưởng: Lựa chọn không minh bạch
   - Action: RFP/RFQ standard
   - Owner: Procurement/ITAM
   - Timeline: 02/2026

4. **[CRITICAL] Chưa enforce ISO/SOC2 standards**
   - Ảnh hưởng: Vendor security không kiểm chứng
   - Action: Compliance checklist
   - Owner: ANTT/Compliance
   - Timeline: 01/2026

5. **[CRITICAL] Chưa có KPI/metric vendor**
   - Ảnh hưởng: Không monitoring performance
   - Action: Define KPI, dashboard
   - Owner: ITAM/BI
   - Timeline: 02/2026

6. **[CRITICAL] SLA tracking manual, escalation = 0**
   - Ảnh hưởng: Không track performance
   - Action: Formal SLA monitoring
   - Owner: IT Ops/VM
   - Timeline: 02/2026

7. **[CRITICAL] Risk mitigation plan = 0**
   - Ảnh hưởng: Không sẵn sàng vendor failures
   - Action: Identify critical vendors
   - Owner: ITAM/Risk
   - Timeline: 03/2026

8. **[CRITICAL] Vendor incidents không ITSM**
   - Ảnh hưởng: Không truy xuất vendor-related issues
   - Action: ITSM integration
   - Owner: IT Ops/ITSM
   - Timeline: 04/2026

#### 7.5. Quick Wins (Dec 2025 - Q1 2026)

| # | Quick Win | Effort | Impact | Owner |
|---|-----------|--------|--------|-------|
| 1 | 3rd party management policy | MEDIUM | CRITICAL | Governance/ITAM |
| 2 | Compliance & security checklist (ISO/SOC2) | LOW | CRITICAL | ANTT/Compliance |
| 3 | RFP/RFQ standard template | MEDIUM | HIGH | Procurement |
| 4 | Vendor KPI definition & scorecard | MEDIUM | HIGH | ITAM/BI |
| 5 | SLA monitoring & escalation process | LOW | HIGH | IT Ops |

#### 7.6. Target 12 Tháng

**Mục tiêu:** Tất cả groups ≥40%

| Nhóm | Hiện tại | Target 12M | Actions |
|------|----------|------------|---------|
| Tools & Data | 14% | 43%+ | Centralized contract repo, SharePoint |
| Measurement | 8% | 42%+ | KPI template, Scorecard, Dashboard |
| Governance | 25% | 50%+ | Policy approved, Roles/RACI, Classification |
| Integration | 10% | 40%+ | ITSM incident tag, Service mapping |
| Process | 28% | 50%+ | RFP/RFQ standard, SLA monitoring |
| Compliance | 25% | 50%+ | ISO/SOC2 checklist, Audit process |
| People | 25% | 45%+ | Dedicated team, Training |
| Improvement | 17% | 40%+ | Risk register, Quarterly review |

---

## PHẦN II: TỔNG HỢP & ƯU TIÊN

### 1. Ma Trận Ưu Tiên (Priority Matrix)

| Mức Độ | Lĩnh Vực | Điểm Hiện Tại | Target 12M | Gap | Ưu Tiên |
|--------|----------|---------------|------------|-----|---------|
| **CRITICAL** | **CMDB** | 9.4% | 50% | +40.6% | **P0 - Highest** |
| **CRITICAL** | **3rd Party** | 19.4% | 50% | +30.6% | **P0 - Highest** |
| **CRITICAL** | **QC** | 30.8% | 50% | +19.2% | **P1 - High** |
| **HIGH** | **PQA** | 41.2% | 55% | +13.8% | **P1 - High** |
| **HIGH** | **IM** | 44.3% | 65% | +20.7% | **P1 - High** |
| **HIGH** | **RM** | 47.8% | 60% | +12.2% | **P2 - Medium** |
| **MEDIUM** | **CM** | 58.5% | 65% | +6.5% | **P3 - Low** |

### 2. Phân Tích Cross-Cutting Issues (Vấn Đề Xuyên Suốt)

#### 2.1. COMPLIANCE & AUDIT (Nghiêm Trọng Nhất)

**Điểm yếu chung:**
- PQA: 30% - Chưa có compliance checklist
- QC: 15% - Không ITIL/ISO, không audit
- CM: 0% - Chưa triển khai audit
- CMDB: 6.2% - Không audit trail
- IM: 33% - ITIL=0%, audit yếu
- 3rd Party: 25% - Chưa enforce ISO/SOC2

**Ảnh hưởng:**
- Rủi ro cao khi audit bên ngoài
- Không chứng minh tuân thủ quy định
- Không đáp ứng yêu cầu khách hàng/đối tác
- Rủi ro pháp lý và tài chính

**Actions cần thực hiện:**
1. Xây dựng ITIL/ISO compliance framework chung
2. Thiết lập audit process cho tất cả lĩnh vực
3. Implement audit trail system
4. Đào tạo ITIL Foundation cho toàn bộ team
5. Chuẩn bị external audit (mục tiêu Q3-Q4/2026)

#### 2.2. METRICS & MEASUREMENT (Yếu Toàn Diện)

**Điểm yếu chung:**
- PQA: 13.6% - CRITICAL
- QC: 23% - Không metrics/KPI
- RM: 20.8% - CRITICAL
- CM: 77% - Tốt nhưng chưa tự động
- CMDB: 8.3% - Không KPI
- IM: 50% - Có dashboard, chưa KPI formal
- 3rd Party: 8% - KPI=0

**Ảnh hưởng:**
- Lãnh đạo không có data để quyết định
- Không đo lường được tiến bộ
- Không chứng minh giá trị của hoạt động
- Khó identify bottlenecks và cải tiến

**Actions cần thực hiện:**
1. Xây dựng KPI framework chung cho ITSM
2. Implement metrics collection automation
3. Build unified ITSM dashboard
4. Establish monthly/quarterly reporting
5. Define targets và benchmarks

#### 2.3. TOOLS & AUTOMATION (Thủ Công Quá Mức)

**Điểm yếu chung:**
- PQA: 37.5% - Excel thủ công
- QC: 17.5% - Không Automation Strategy
- RM: 54.2% - Jira OK nhưng chưa CMDB
- CM: 70% - Jira OK nhưng chưa tích hợp
- CMDB: 0% - Chỉ Excel
- IM: 40.9% - Automation=0
- 3rd Party: 14% - Không VMS

**Ảnh hưởng:**
- Tốn nhiều thời gian manual work
- Dễ sai sót do thủ công
- Không scale được
- Dữ liệu phân tán, khó tổng hợp

**Actions cần thực hiện:**
1. **CMDB tool deployment (P0)** - Foundation cho tất cả
2. Jira workflow automation enhancement
3. ITSM tools integration (Incident-Problem-Change-CMDB)
4. VMS selection và deployment
5. Test automation framework (QC)
6. Reporting automation

#### 2.4. INTEGRATION (Các Hệ Thống Độc Lập)

**Điểm yếu chung:**
- PQA: 58.3% - Tốt nhưng chưa xuyên suốt
- QC: 36.7% - 1 environment
- RM: 43.8% - Request-incident manual
- CM: 21% - RFC from Incident manual, chưa CMDB
- CMDB: 0% - Không integrate
- IM: 16.7% - Chưa CMDB, link thủ công
- 3rd Party: 10% - Không ITSM

**Ảnh hưởng:**
- Không trace được end-to-end
- Duplicate data entry
- Inconsistent data
- Khó phân tích root cause
- Không impact analysis được

**Actions cần thực hiện:**
1. **CMDB làm trung tâm integration**
2. Implement Incident-Problem-Change linkage
3. Auto-link Request-Incident
4. Integrate Vendor incidents vào ITSM
5. PQA integrate với tất cả quy trình
6. Service mapping

#### 2.5. PEOPLE & COMPETENCY (Nguồn Lực & Năng Lực)

**Điểm yếu chung:**
- PQA: 50% - Nguồn lực mỏng, chưa competency matrix
- QC: 55% - Skills yếu automation
- RM: 62.5% - Tốt nhưng chưa training SLA
- CM: 45% - Training tự học
- CMDB: 6.2% - Part-time, không training
- IM: 50% - Training & cert thiếu
- 3rd Party: 25% - Không dedicated team

**Ảnh hưởng:**
- Phụ thuộc cá nhân
- Khó scale
- Knowledge loss khi nhân sự nghỉ
- Không có career path rõ ràng

**Actions cần thực hiện:**
1. **Xây dựng ITSM Competency Framework**
2. ITIL Foundation training cho toàn bộ team (target 80%)
3. Specialized training per domain
4. Certification program (ITIL, ISTQB, etc.)
5. Assign dedicated roles:
   - CMDB Admin (1 FTE)
   - Incident Manager (1 FTE)
   - Change Manager (1 FTE)
   - PQA Lead (1 FTE)
   - Vendor Manager (0.5 FTE)
6. Succession planning
7. Career path definition

### 3. Dependencies & Sequencing (Phụ Thuộc & Thứ Tự)

**CRITICAL PATH:**

```
Phase 1 (Q4 2025 - Q1 2026): Foundation
├─ CMDB Tool Selection & Deployment (P0)
│  └─ Blocks: All ITSM integration
├─ Policy & Governance (All domains)
│  └─ RACI, Roles, Escalation
├─ Quick Wins (All domains)
└─ Training Kickoff

Phase 2 (Q2 2026): Integration
├─ CMDB Population (20-30% CIs)
│  └─ Enables: Impact analysis, Change-CI mapping
├─ Incident-Problem-Change Linking
│  └─ Depends: CMDB
├─ Request-Incident Auto-linking
├─ Automation Implementation
│  ├─ Jira workflows
│  ├─ QC automation framework
│  └─ Metrics collection
└─ KPI Dashboards Go-Live

Phase 3 (Q3 2026): Scale & Optimize
├─ CMDB Expansion (40-50% CIs)
├─ Compliance Audit (All domains)
│  └─ Depends: All policies & processes documented
├─ Advanced Automation
├─ Performance Optimization
└─ ITIL Compliance Validation

Phase 4 (Q4 2026): Consolidation
├─ CMDB 75%+ Coverage
├─ All Integrations Complete
├─ Re-assessment (All domains)
└─ 2027 Roadmap
```

### 4. Tổng Đầu Tư Ước Tính (Investment Estimate)

#### 4.1. Nhân Lực (Headcount)

**Dedicated Roles Cần Bổ Sung:**
- CMDB Admin: 1 FTE (Q1/2026)
- Incident Manager: 1 FTE (Q1/2026)
- PQA Additional: 1 FTE (Q2/2026)
- QC Automation Engineer: 1 FTE (Q2/2026)
- Vendor Manager: 0.5 FTE (Q2/2026)
- ITSM Architect/Integration Lead: 1 FTE (Q1/2026)

**Total: 5.5 FTE mới**

**Chi phí nhân lực:** $300K-450K/năm

#### 4.2. Công Cụ (Tools)

| Tool | Cost Estimate | Timeline | Priority |
|------|---------------|----------|----------|
| **CMDB Tool** | $80K-120K (license + setup) | Q1/2026 | P0 |
| **VMS (Vendor Management)** | $20K-30K | Q1/2026 | P0 |
| **Test Automation Tools** | $15K-25K | Q2/2026 | P1 |
| **Monitoring & Analytics** | $10K-20K | Q2/2026 | P1 |
| **ITSM Enhancement** | $10K-15K | Q1/2026 | P1 |

**Total Tools:** $135K-210K

#### 4.3. Đào Tạo & Tư Vấn (Training & Consulting)

| Item | Cost | Timeline |
|------|------|----------|
| ITIL Foundation Training (40 người) | $20K-30K | Q1-Q2/2026 |
| ITIL Practitioner/Expert (5 người) | $10K-15K | Q2-Q3/2026 |
| ISTQB Certification (10 người) | $5K-8K | Q2/2026 |
| Specialized Training (Automation, CMDB) | $10K-15K | Q1-Q3/2026 |
| External Consulting (CMDB, ITSM) | $30K-50K | Q1-Q2/2026 |

**Total Training:** $75K-118K

#### 4.4. Tổng Đầu Tư 12 Tháng

| Category | Estimate |
|----------|----------|
| Nhân lực (5.5 FTE) | $300K-450K |
| Công cụ | $135K-210K |
| Đào tạo & Tư vấn | $75K-118K |
| **TOTAL** | **$510K-778K** |

**Phân bổ theo quý:**
- Q1 2026: $200K-280K (40%)
- Q2 2026: $150K-210K (30%)
- Q3 2026: $100K-140K (20%)
- Q4 2026: $60K-148K (10%)

---

## PHẦN III: LỘ TRÌNH TỔNG HỢP 12 THÁNG

### Quý 1/2026 (Tháng 1-3): NỀN TẢNG & CHÍNH SÁCH

**Mục tiêu:** Xây dựng foundation cho tất cả lĩnh vực

**CRITICAL ACTIONS:**

**1. CMDB (P0 - Highest Priority)**
- Week 1-2: CMDB Policy Charter, CI Classification
- Week 1: Assign CMDB Steward & CI Owners
- Week 4-8: CMDB tool evaluation & selection
- Month 3-4: CMDB tool deployment & initial load

**2. Governance & Policies (All Domains)**
- PQA: QA Charter, RACI matrix, audit checklists
- QC: QC Policy, Strategy & Roadmap, Test Planning standards
- RM: Roles documentation, Approval workflows, RACI
- CM: Risk Assessment 5x5, RACI formal, CAB criteria
- IM: SLA P1-P4 definition, Escalation path, IM Manager role
- 3rd Party: Policy, Compliance checklist, RFP/RFQ templates

**3. Metrics Framework Setup (All Domains)**
- Define KPIs cho từng lĩnh vực
- Thiết kế dashboard structure
- Cấu hình collection tự động từ Jira
- Baseline data collection

**4. Quick Wins (All Domains)**
- PQA: Checklist audit, QA database schema
- QC: Quality gate, Defect triage, RCA documentation
- RM: Metrics framework, Service review cadence
- CM: MW SLA, Freeze calendar, RFC simplification
- IM: SLA approval, Escalation, RACI
- CMDB: CI Owners, Excel improvements
- 3rd Party: Vendor KPI, SLA monitoring

**5. People & Training**
- ITIL Foundation kickoff (first batch 20 người)
- Competency Matrix development
- Recruitment plan for 5.5 FTE
- Onboarding programs

**DELIVERABLES Q1:**
- 7 Policy documents approved
- 7 RACI matrices published
- CMDB tool selected & deployed
- 30+ Quick Wins completed
- 20 staff ITIL trained
- Baseline metrics established

**EXPECTED SCORES END Q1:**
- CMDB: 9% → 25-30%
- 3rd Party: 19% → 30-35%
- QC: 31% → 38-42%
- RM: 48% → 52-55%
- IM: 44% → 50-52%
- PQA: 41% → 48-52%
- CM: 58% → 60-62%

---

### Quý 2/2026 (Tháng 4-6): TỰ ĐỘNG HÓA & TÍCH HỢP

**Mục tiêu:** Automation & Integration implementation

**CRITICAL ACTIONS:**

**1. CMDB Expansion**
- Load 20-30% critical CIs
- CI-Service mapping cho top 10 services
- CMDB-Incident integration
- CMDB-Change integration (initial)

**2. Automation Implementation**
- QC: Test automation framework POC, Tool selection
- RM: Auto-routing rules (80% accuracy), Quality verification
- CM: Risk 5x5 go-live, MW dashboard, Sonar re-enable
- IM: Jira SLA automation, Auto-priority, Auto-routing
- PQA: QA database integration với Jira

**3. Quality & Process**
- QC: Test coverage measurement, Test Data Management
- RM: KB integration, CSAT survey
- CM: CMDB POC, Data retention policy
- IM: Data quality rules, Template standardization
- PQA: QA review process trên phạm vi thí điểm

**4. Measurement & Dashboards**
- All domains: KPI dashboards go-live
- Monthly reporting process
- Trend analysis begins
- Executive dashboard

**5. Training Wave 2**
- ITIL Foundation (additional 20 người)
- Specialized training:
  - CMDB administration
  - Test automation
  - ITSM integration
  - Metrics & analytics

**DELIVERABLES Q2:**
- CMDB 20-30% populated
- 5 automation workflows live
- All KPI dashboards operational
- Monthly reports established
- 40 staff ITIL trained (cumulative)

**EXPECTED SCORES END Q2:**
- CMDB: 30% → 38-42%
- 3rd Party: 35% → 42-45%
- QC: 42% → 48-52%
- RM: 55% → 58-62%
- IM: 52% → 56-60%
- PQA: 52% → 56-60%
- CM: 62% → 63-65%

---

### Quý 3/2026 (Tháng 7-9): MỞ RỘNG & TUÂN THỦ

**Mục tiêu:** Scale up & Compliance preparation

**CRITICAL ACTIONS:**

**1. CMDB Scale Up**
- Expand to 40-50% CI coverage
- Relationship & dependency mapping
- Auto-population from monitoring tools
- Performance optimization

**2. ITSM Integration**
- Incident-Problem-Change full linkage
- Request-Incident auto-linking
- Vendor incidents integration
- Service mapping completion

**3. Compliance & Audit**
- PQA: Compliance audit lần 1
- CM: Internal audit lần 1
- IM: ITIL 4 compliance checklist
- QC: ITIL/ISO alignment
- 3rd Party: Compliance audit
- All: Audit findings remediation

**4. Advanced Features**
- QC: Regression test 80% automated
- RM: Self-service expansion 30-40%
- CM: Incident-Change linkage, CMDB 20-30%
- IM: Knowledge Base expansion
- PQA: Dashboard xu hướng

**5. Optimization**
- Process improvements based on data
- Bottleneck elimination
- Performance tuning
- User feedback implementation

**DELIVERABLES Q3:**
- CMDB 40-50% populated
- Full ITSM integration live
- Compliance audits completed
- Findings remediation plans
- Optimization initiatives

**EXPECTED SCORES END Q3:**
- CMDB: 42% → 48-52%
- 3rd Party: 45% → 48-52%
- QC: 52% → 58-62%
- RM: 62% → 63-65%
- IM: 60% → 63-66%
- PQA: 60% → 62-65%
- CM: 65% → 66-68%

---

### Quý 4/2026 (Tháng 10-12): CONSOLIDATION & MATURITY

**Mục tiêu:** Achieve targets & Plan 2027

**CRITICAL ACTIONS:**

**1. CMDB Finalization**
- 75%+ CI coverage
- Auto-update from Change pipeline
- Full relationship mapping
- CMDB maturity Level 3

**2. Compliance Validation**
- External audit preparation
- All findings closed
- Compliance score 85%+
- ISO/ITIL alignment complete

**3. Advanced Automation**
- QC: Performance testing benchmarks
- RM: Advanced analytics, Forecasting
- CM: Batch approval pilot, Auto-CMDB update
- IM: Advanced auto-assignment
- All: Reporting full automation

**4. Re-assessment**
- All 7 domains: Maturity re-assessment
- Compare baseline vs current
- Validate target achievement
- Identify Level 3 roadmap items

**5. 2027 Planning**
- Detailed roadmap 2027
- Budget planning
- Resource planning
- Target: Level 3 (Defined) for all domains

**DELIVERABLES Q4:**
- CMDB 75%+ coverage
- All domains Level 2 achieved
- Compliance ready for external audit
- 2027 Roadmap approved
- All teams ITIL trained

**EXPECTED SCORES END Q4 (12 MONTHS):**
- CMDB: 52% → **55-60%** ✓ (Target 50%)
- 3rd Party: 52% → **50-55%** ✓ (Target 50%)
- QC: 62% → **65-70%** ✓ (Target 50%)
- RM: 65% → **65-68%** ✓ (Target 60%)
- IM: 66% → **68-72%** ✓ (Target 65%)
- PQA: 65% → **65-68%** ✓ (Target 55%)
- CM: 68% → **68-72%** ✓ (Target 65%)

**ALL TARGETS ACHIEVED ✓**

---

## PHẦN IV: RISKS & MITIGATION (RỦI RO & GIẢM THIỂU)

### 1. Rủi Ro Chính

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| **CMDB tool deployment delay** | CRITICAL | MEDIUM | - Start evaluation immediately<br>- Parallel Excel improvements<br>- Phased rollout plan |
| **Insufficient budget** | HIGH | MEDIUM | - Prioritize P0/P1<br>- Phased investment<br>- ROI justification strong |
| **Resistance to change** | HIGH | HIGH | - Change management program<br>- Early wins communication<br>- Training & support<br>- Executive sponsorship |
| **Resource constraints** | HIGH | HIGH | - Phased hiring<br>- External consulting<br>- Prioritization strict |
| **Competing priorities** | HIGH | MEDIUM | - Executive alignment<br>- Dedicated resources<br>- Clear roadmap |
| **Skills gap** | MEDIUM | HIGH | - Aggressive training<br>- Knowledge transfer<br>- External expertise |
| **Tool integration complexity** | MEDIUM | HIGH | - Phased integration<br>- API-first approach<br>- Vendor support |
| **Data quality issues** | MEDIUM | HIGH | - Data cleansing projects<br>- Quality rules<br>- Validation gates |

### 2. Success Factors

**CRITICAL SUCCESS FACTORS:**
1. **Executive Sponsorship** - CIO/CTO commitment & support
2. **Dedicated Resources** - 5.5 FTE secured on time
3. **CMDB Foundation** - Tool deployed Q1/2026
4. **Budget Approval** - $510K-778K committed
5. **Change Management** - User adoption program
6. **Training Investment** - ITIL certification program
7. **Quick Wins** - Early success demonstration
8. **Metrics Driven** - Data-based decision making

**ENABLERS:**
- Project governance structure (Steering Committee)
- Regular progress reviews (monthly)
- Risk management process
- Communication plan
- Knowledge management
- Vendor partnerships
- External consulting support

---

## PHẦN V: KẾT LUẬN & KHUYẾN NGHỊ

### 1. Tóm Tắt Tình Trạng

**TÌNH TRẠNG TỔNG QUAN:**
- **7/7 lĩnh vực** đều ở mức trưởng thành thấp (Level 1-2)
- **3 lĩnh vực CRITICAL** cần ưu tiên cao nhất: CMDB (9%), 3rd Party (19%), QC (31%)
- **Vấn đề xuyên suốt:** Compliance (0-33%), Metrics (8-23%), Tools (0-37%), Integration (10-43%)
- **Điểm mạnh:** Governance tương đối tốt, Team có kinh nghiệm, Văn hóa hợp tác

**RỦI RO NẾU KHÔNG HÀNH ĐỘNG:**
- Không pass được external audit
- Không đáp ứng compliance requirements
- Incidents & changes không kiểm soát được
- Quality issues tăng cao
- Không scale được khi tổ chức phát triển
- Mất kiểm soát vendors
- Reputation risk

### 2. Khuyến Nghị Ưu Tiên

**NGAY LẬP TỨC (Q4 2025):**

1. **Xin phê duyệt ngân sách $510K-778K cho 12 tháng**
   - Trình Executive Committee/Board
   - Justify bằng risk analysis & ROI
   - Phân bổ theo quý

2. **Bắt đầu tuyển dụng 5.5 FTE**
   - CMDB Admin (P0)
   - Incident Manager (P0)
   - ITSM Architect (P0)
   - Others theo roadmap

3. **Kickoff CMDB tool selection**
   - RFP/RFQ preparation
   - Vendor evaluation criteria
   - POC planning
   - Target: Decision by end Jan 2026

4. **Execute Quick Wins (30+ items)**
   - All domains simultaneously
   - Demonstrate momentum
   - Build confidence

5. **Policy development sprint**
   - 7 policies in parallel
   - Approval by end Q1/2026

**Q1 2026 - FOUNDATION:**
- CMDB tool deployed
- All policies approved
- Metrics framework live
- Training started
- Quick Wins completed

**Q2 2026 - AUTOMATION:**
- Automation go-live
- Integrations started
- Dashboards operational
- CMDB 20-30% populated

**Q3 2026 - SCALE:**
- CMDB 40-50%
- Full integration
- Compliance audits
- Optimization

**Q4 2026 - MATURITY:**
- All targets achieved
- CMDB 75%+
- Compliance ready
- Level 2 for all

### 3. Lời Khuyên Quản Trị

**ĐỂ THÀNH CÔNG, CẦN:**

1. **Executive Commitment** - Đây là chương trình chuyển đổi, không phải project nhỏ
2. **Sufficient Resources** - 5.5 FTE + $510K-778K là minimum
3. **Patience** - 12 tháng là aggressive, cần kiên nhẫn
4. **Data-Driven** - Quyết định dựa trên metrics, không assumption
5. **Communication** - Thường xuyên, minh bạch
6. **Change Management** - Đầu tư vào people & culture
7. **Vendor Partnerships** - Chọn vendors đúng, support tốt
8. **Continuous Improvement** - Không dừng lại ở Level 2

**KHÔNG NÊN:**
- Cut corners trên Critical items (CMDB, Compliance)
- Delay training & certification
- Skimp on resources
- Treat as IT project only (cần Business involvement)
- Ignore quick wins (momentum quan trọng)
- Over-customize tools (standard first)

### 4. Expected Benefits (12 Months)

**TANGIBLE BENEFITS:**
- **MTTR reduction:** 30-40% (nhờ CMDB & automation)
- **Change success rate:** 98%+ (từ 97%)
- **SLA compliance:** 90%+ (từ 75%)
- **Automation rate:** 70%+ (từ 0-20%)
- **First-time success:** 90%+ (từ unknown)
- **Manual effort reduction:** 40-50%

**INTANGIBLE BENEFITS:**
- Compliance readiness
- Audit confidence
- Quality culture
- Team morale & engagement
- Career development
- Vendor accountability
- Business trust

**ROI ESTIMATE:**
- Investment: $510K-778K
- Annual savings: $200K-350K (efficiency gains)
- Risk mitigation: $500K-1M+ (avoid incidents, fines)
- **ROI: 40-150% trong 24 tháng**

---

## PHỤ LỤC

### A. Danh Sách Tài Liệu Tham Khảo

1. ITIL 4 Foundation
2. ISO 20000 - IT Service Management
3. ISO 27001 - Information Security
4. COBIT 2019
5. CMMI for Services
6. ISTQB - International Software Testing Qualifications Board

### B. Glossary (Thuật Ngữ)

| Thuật Ngữ | Định Nghĩa |
|-----------|------------|
| **CAB** | Change Advisory Board - Hội đồng tư vấn thay đổi |
| **CAPA** | Corrective Action Preventive Action - Hành động khắc phục & phòng ngừa |
| **CFR** | Change Failure Rate - Tỷ lệ thay đổi thất bại |
| **CI** | Configuration Item - Hạng mục cấu hình |
| **CMDB** | Configuration Management Database - Cơ sở dữ liệu quản lý cấu hình |
| **CSAT** | Customer Satisfaction - Mức độ hài lòng khách hàng |
| **FTE** | Full Time Equivalent - Nhân lực tương đương toàn thời gian |
| **IM** | Incident Management - Quản lý sự cố |
| **ITIL** | Information Technology Infrastructure Library |
| **ITSM** | IT Service Management - Quản lý dịch vụ CNTT |
| **KB** | Knowledge Base - Kho tri thức |
| **KPI** | Key Performance Indicator - Chỉ số đo lường hiệu suất chính |
| **MTTR** | Mean Time To Resolve - Thời gian trung bình để giải quyết |
| **PIR** | Post Implementation Review - Đánh giá sau triển khai |
| **PQA** | Process Quality Assurance - Đảm bảo chất lượng quy trình |
| **QC** | Quality Control - Kiểm soát chất lượng |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **RCA** | Root Cause Analysis - Phân tích nguyên nhân gốc rễ |
| **RFC** | Request For Change - Yêu cầu thay đổi |
| **RM** | Release Management - Quản lý phát hành/yêu cầu |
| **ROI** | Return On Investment - Lợi tức đầu tư |
| **SLA** | Service Level Agreement - Thỏa thuận mức độ dịch vụ |
| **VMS** | Vendor Management System - Hệ thống quản lý nhà cung cấp |

### C. Contact & Support

**Project Team:**
- Program Director: [TBD]
- CMDB Lead: [TBD]
- PQA Lead: [Current PQA Lead]
- QC Lead: [Current QC Lead]
- ITSM Lead: [TBD]

**External Support:**
- ITSM Consulting: [Vendor TBD]
- CMDB Tool Vendor: [TBD]
- Training Provider: [TBD]

---

**END OF REPORT**

**Ngày tạo:** Ngày 2 tháng 12, 2025
**Phiên bản:** 1.0
**Trạng thái:** FINAL
**Phân loại:** INTERNAL USE ONLY

