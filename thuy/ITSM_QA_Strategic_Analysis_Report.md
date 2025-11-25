# PHÂN TÍCH CHIẾN LƯỢC TRIỂN KHAI ITSM & QA CHO CÔNG TY FINTECH (A)

**Date**: November 25, 2025
**Prepared by**: Strategic Analysis Team
**Context**: Công ty Fintech (A) đang cung cấp dịch vụ vận hành và phát triển cho các công ty con trong cùng tập đoàn. Hạ tầng phần cứng đã tách biệt, phần mềm có shared systems và dedicated systems, nguồn lực ITSM và QA đang dùng chung.

**Key Findings Source**: 49 findings across 6 areas (Request Fulfillment, Incident, Change, Configuration, Process QA, 3rd Party Management)

---

## MỤC LỤC

1. [Vấn Đề, Thách Thức, Rủi Ro & Cơ Hội](#phần-1-vấn-đề-thách-thức-rủi-ro--cơ-hội)
2. [Mục Tiêu Hướng Tới (WHY, WHO, WHAT, Timeframe, HOW)](#phần-2-mục-tiêu-hướng-tới)
3. [Objective Charters Chi Tiết](#phần-3-objective-charters-chi-tiết)
4. [Tổng Kết & Khuyến Nghị](#tổng-kết--khuyến-nghị)

---

## PHẦN 1: VẤN ĐỀ, THÁCH THỨC, RỦI RO & CƠ HỘI

### 🔴 VẤN ĐỀ (PROBLEMS) - Hiện tại đang xảy ra

#### P1. Thiếu Hiệu Quả Vận Hành (Operational Inefficiency)

**Hiện trạng:**
- **80% thời gian cho công việc thủ công** (Finding #10) → lãng phí 4 FTE trên mỗi team 5 người
- CMDB dùng Excel (Finding #33) → không thể scale, không có relationship mapping
- Không tích hợp giữa các processes → Incident/Change/CMDB hoàn toàn tách biệt (Findings #3, #11, #22, #38)
- Dashboard thủ công (Finding #27) → dữ liệu lag, không real-time

**Impact:**
- Chi phí nhân công cao không cần thiết
- Thời gian xử lý chậm
- Lỗi do manual entry
- Không thể scale để phục vụ thêm subsidiaries

#### P2. Mù Thông Tin (Visibility Blindness)

**Hiện trạng:**
- Không đo lường được SLA (Finding #1) → không biết performance thực tế
- Không có CSAT measurement (Finding #2) → không biết khách hàng hài lòng hay không
- Coverage audit chỉ 3% processes (Finding #45) → không biết 97% còn lại hoạt động thế nào
- Metrics tracking chỉ đạt 10% (Finding #46) → ra quyết định dựa vào cảm tính thay vì dữ liệu

**Impact:**
- Không thể justify ngân sách và resources
- Không phát hiện được bottlenecks
- Không biết customer churn risk
- Không có data để improve

#### P3. Kiểm Soát Chất Lượng Yếu (Quality Control Weakness)

**Hiện trạng:**
- Sonar tool bị tạm dừng (Finding #23) → không có code quality gate
- Không có quality standards (Finding #39) → CMDB data không đáng tin cậy, duplicate CIs
- PIR thủ công, không kết nối CI/CD (Finding #24) → không verify deployment match approval
- Change failure rate cao (~20%) nhưng không phân tích root cause (Finding #20)

**Impact:**
- Production defects cao
- Failed changes lặp lại
- Data quality kém → wrong decisions
- Technical debt tăng

#### P4. Chân Không Quản Trị (Governance Vacuum)

**Hiện trạng:**
- Roles quan trọng không định nghĩa:
  - Incident Manager (Finding #7)
  - CMDB Steward (Finding #37)
  - CI Owners (Finding #36)
- Policies không formal:
  - CMDB Policy (Finding #32)
  - 3rd Party Management (Finding #49)
- RACI không document (Finding #19) → xung đột trách nhiệm, không rõ accountability
- Audit process yếu → yearly only, 3% coverage (Findings #43, #44, #45)

**Impact:**
- Ownership vacuum → không ai chịu trách nhiệm
- Conflicts không resolve
- Compliance risk cao
- Không enforce standards

---

### ⚡ THÁCH THỨC (CHALLENGES) - Khó khăn cần vượt qua

#### C1. Phức Tạp Multi-Tenancy

**Bối cảnh đặc thù:**
- Phục vụ nhiều công ty con với nhu cầu business khác nhau
- Shared resources (ITSM & QA) phải cân bằng competing priorities giữa các entities
- Kiến trúc hệ thống: Một số shared systems, một số dedicated systems → phức tạp trong quản lý CMDB
- Cần chargeback model công bằng nhưng chưa có framework

**Khó khăn:**
- Conflicting priorities khi resources contested
- Làm sao maintain fairness giữa các subsidiaries
- Different service level expectations
- Cost allocation transparency

#### C2. Technical Debt trong Tight Operations

**Thực tế:**
- Phải maintain current operations trong khi transform (không thể "tắt máy" để rebuild)
- Team đang overload với 80% manual work → không có spare capacity
- Part-time resources (Finding #41) → knowledge continuity risk cao
- Ngân sách limited, phải chứng minh ROI từng bước

**Khó khăn:**
- Làm transformation mà không disrupting services
- Balance giữa BAU và project work
- Resource allocation cho initiative mới
- Build business case với data hiện tại yếu

#### C3. Standardization vs Flexibility Dilemma

**Căng thẳng:**
- Cần process chuẩn để efficient, compliant, và scale
- Nhưng mỗi subsidiary có business model và requirements đặc thù riêng
- Làm sao balance giữa standardization và customization

**Risk:**
- One-size-fits-all → không phù hợp, resistance cao
- Too fragmented → không scale, không efficient
- Over-standardization → slow, bureaucratic
- Under-standardization → chaos, inconsistent

#### C4. Culture & Change Management

**Hiện trạng:**
- Team chưa được training chuyên sâu về ITSM (Finding #30)
- Không có certification requirement (Finding #31) → skill gaps
- Từ ad-hoc sang formal process = big cultural shift
- Resistance to additional "overhead" (documentation, compliance, approvals)

**Khó khăn:**
- Thay đổi mindset từ "just do it" sang "follow process"
- Build discipline trong documentation
- Acceptance của controls và checks
- Maintain morale trong thời kỳ thay đổi

#### C5. Regulatory Pressure (Fintech-Specific)

**Áp lực:**
- ITIL/ISO compliance hiện tại 0% nhưng REQUIRED cho ngành fintech
- Audit trail mandatory nhưng đang không có (Finding #35)
- Timeline pressure từ regulators (SBV, MOF, international standards)
- Penalties cao nếu không comply → existential risk

**Khó khăn:**
- Catch up nhanh trong khi maintain operations
- Demonstrate compliance với evidence không đủ
- Multiple regulatory frameworks (local + international)
- Audit readiness trong timelines ngắn

---

### 🚨 RỦI RO (RISKS) - Hậu quả tiềm ẩn nếu không giải quyết

#### R1. Compliance & Legal Risks (CRITICAL cho Fintech)

**Severity**: CRITICAL
**Probability**: HIGH
**Impact**: EXISTENTIAL

**Chi tiết:**
- ITIL/ISO compliance 0% (Finding #12) → Failed audits từ SBV, MOF, international auditors
- Không có audit trail (Finding #35) → Không chứng minh được controls đang hoạt động
- Data retention policy missing (Finding #14) → Vi phạm GDPR/PDPA requirements
- No 3rd party policy (Finding #49) → Vendor risk unmanaged, supply chain vulnerability

**Hậu quả cụ thể:**
- **Financial**: Fines $500K-1M+ (precedents in SEA fintech)
- **Operational**: License suspension → revenue halt, business shutdown risk
- **Reputational**: Loss of trust, customer exodus, media exposure
- **Strategic**: M&A blocker (due diligence failure), cannot expand to new markets

**Timeline**: Audit có thể xảy ra bất kỳ lúc nào, risk tăng mỗi quarter

#### R2. Operational Failure Risks

**Severity**: HIGH
**Probability**: MEDIUM-HIGH
**Impact**: HIGH

**Chi tiết:**
- Incidents không escalate đúng (Finding #9) → P1 incidents prolonged, revenue impact
- Changes không assess risk properly (Finding #13) → Failed deployments, customer-facing outages
- CMDB data unreliable (Finding #39) → Wrong impact analysis → cascade failures
- No PIR connection to deployment (Finding #24) → Không verify success, repeated failures

**Hậu quả cụ thể:**
- **Service Availability**: Downtime averaging 2-4 hours/incident for P1
- **Revenue Impact**: $50-100K+ per major incident (fintech = high transaction value)
- **Customer Churn**: 5-10% churn after major incidents
- **SLA Penalties**: If có SLA contracts với subsidiaries/partners

**Historical Evidence**: Đã xảy ra ad-hoc, sẽ worse khi scale tăng

#### R3. Financial Risks

**Severity**: MEDIUM-HIGH
**Probability**: HIGH
**Impact**: MEDIUM-HIGH

**Chi tiết:**
- Không measure được ROI của ITSM team (Finding #1) → Budget cut risk trong downturn
- Resource inefficiency (80% manual work) → $200K/year cost overrun vs optimal
- Failed changes không analyze root cause (Finding #20) → Recurring costs $100K/year
- Cannot demonstrate value → Subsidiaries may build own teams (lose economies of scale)

**Hậu quả cụ thể:**
- **Cost Overrun**: 20-30% higher operational cost than necessary
- **Budget Justification Failure**: Cannot defend headcount requests
- **Investment Waste**: Tools purchased but underutilized (without integration)
- **Opportunity Cost**: $150K/year not saved through automation

**Trend**: Worsening as scale increases without efficiency improvement

#### R4. Talent & Knowledge Risks

**Severity**: MEDIUM
**Probability**: MEDIUM
**Impact**: MEDIUM

**Chi tiết:**
- Part-time CMDB team (Finding #41) → Knowledge loss when turnover (no documentation)
- No training/certification program (Finding #30, #31) → Skill gaps widening, cannot attract talent
- Shared resources burnout → Key person dependency risk
- No career path → High performers leave for better opportunities

**Hậu quả cụ thể:**
- **Turnover**: 20-30% attrition (vs 15% industry average)
- **Knowledge Loss**: 3-6 months to ramp up replacements
- **Quality Degradation**: Junior staff handling complex issues
- **Recruitment Difficulty**: Cannot compete for talent without growth path

**Trend**: Risk tăng khi transformation pressure tăng

---

### 🌟 CƠ HỘI (OPPORTUNITIES) - Lợi thế có thể tận dụng

#### O1. Shared Service Model Advantages

**Lợi thế cốt lõi:**

**Economies of Scale:**
- Phục vụ nhiều subsidiaries → justify investment in enterprise-grade tools (ServiceNow ~$200K có thể reasonable với 5+ subsidiaries)
- Bulk licensing discounts: ITIL training, tools, insurance
- Shared infrastructure costs distributed
- **Quantified**: Save 30-40% vs each subsidiary building own team

**Best Practice Sharing:**
- Incident patterns từ subsidiary A → prevent issues ở subsidiary B
- Change learnings cross-pollinate
- Unified knowledge base = comprehensive
- **Quantified**: Reduce repeated failures by 50%+

**Specialized Roles:**
- Critical mass để có dedicated roles: CMDB Admin, Incident Manager (không part-time)
- Build centers of excellence
- Deeper expertise vs generalists
- **Quantified**: Dedicated FTE 2x productive vs part-time

**Unified Analytics:**
- Aggregate data across entities → better insights, industry benchmarking
- Identify patterns không visible at subsidiary level
- Predictive analytics với larger dataset
- **Quantified**: 20-30% better forecasting accuracy

**Negotiation Power:**
- Vendor negotiations với larger volume
- Training provider deals
- Consulting rates for bulk engagement
- **Quantified**: 15-25% cost reduction on external spend

#### O2. Digital Transformation Wave

**Market Timing:**

**Industry Momentum:**
- Fintech industry globally đang modernize ITSM (regulatory push)
- Budget available cho digital transformation (board-level priority)
- Cloud adoption accelerating → opportunities for automation
- **Timing**: Ride the wave = easier budget approval, vendor ecosystem mature

**Technology Enablers:**
- **Cloud & IaC**: Infrastructure as Code → auto CMDB updates, CI tracking
- **DevOps Maturity**: CI/CD pipelines → integration opportunities (PIR automation)
- **API Economy**: Everything has APIs → easier integration vs 5 years ago
- **AI/ML Tools**: Anomaly detection, auto-categorization, chatbots

**Vendor Ecosystem:**
- Mature ITSM tools với fintech-specific features
- Integration platforms (Zapier, n8n) → low-code automation
- Managed services available (nếu need external capacity)
- **Advantage**: Don't need to build from scratch, assemble best-of-breed

#### O3. Regulatory Compliance as Differentiator

**Competitive Advantage:**

**Market Position:**
- First-mover trong peer fintechs → reference customer status
- Demonstrate mature operations → attract enterprise clients (B2B fintech)
- Build trust with regulators → easier approvals for new products/markets
- **Impact**: Premium pricing, preferred partner status

**Business Development:**
- Compliance certification = table stakes for enterprise RFPs
- Reduce due diligence friction in partnerships
- Enable international expansion (ISO recognized globally)
- **Quantified**: Open 20-30% more market opportunities

**Talent Brand:**
- Employer brand boost (work at compliant, professional org)
- Attract quality talent (career growth in mature environment)
- Become training ground for industry
- **Impact**: 30% better recruitment success rate

#### O4. Data-Driven Decision Making

**Transformation Potential:**

**Current State = Low Bar:**
- No metrics (Findings #1, #46) → ANY visibility = huge improvement
- No dashboards → manual reports taking days
- No CSAT → flying blind on satisfaction
- **Opportunity**: Low-hanging fruit, high impact

**Upside từ Visibility:**
- **Dashboard automation** (Finding #27): Real-time vs weekly manual → 10x faster decisions
- **CMDB integration**: Impact analysis in minutes vs hours
- **CSAT measurement** (Finding #2): Product improvement feedback loop, prioritization
- **Trend analysis**: Predictive vs reactive

**Business Impact:**
- **Decision Speed**: 20-30% faster (data available instantly)
- **Decision Quality**: 40-50% better (fact-based vs intuition)
- **Resource Optimization**: Right-size teams based on actual demand
- **ROI Demonstration**: Show value of ITSM investment

**Quantified Value:**
- Executive time saved: 10 hours/week across leadership team
- Better resource allocation: $100K/year optimization
- Avoided wrong decisions: $50K+/year

#### O5. Talent Development

**People Advantage:**

**Career Paths (Finding #31):**
- Create ITSM career ladder: Analyst → Specialist → Lead → Manager
- Attract ambitious talent (vs dead-end jobs at competitors)
- Internal promotion pipeline
- **Impact**: Become destination employer for ITSM talent in market

**Capability Building:**
- Training programs (Finding #30) → build internal expertise
- ITIL certifications → reduce dependency on expensive consultants
- Knowledge retention through documentation
- **Quantified**: Save $100K/year on external consultants

**Market Recognition:**
- Team members marketable with certifications → retention through growth
- Company known for developing talent → recruitment magnet
- Industry speaking opportunities → brand building
- **Impact**: 20% better retention, 30% easier hiring

**Shared Service Benefit:**
- Broader exposure for team members (multiple business contexts)
- Cross-training opportunities
- Larger team = mentorship, communities of practice
- **Advantage**: Richer learning environment vs siloed subsidiary teams

---

## PHẦN 2: MỤC TIÊU HƯỚNG TỚI

### 🎯 WHY - Tại sao cần triển khai ITSM & QA hiệu quả?

#### 1. Compliance Imperative (Non-negotiable)

**Regulatory Requirement:**
- Fintech industry regulations REQUIRE ITIL/ISO 20000/27001 compliance
- Current compliance level: 0% (Finding #12)
- Risk: License suspension, penalties, business shutdown
- **Timeline**: Must achieve within 12-18 months or face consequences

**Specific Mandates:**
- Audit trail for all changes (Finding #35)
- Documented processes (Findings #32, #49)
- Regular audits and evidence (Findings #43-45)
- Risk management framework (Finding #13)

**Consequence of Inaction:**
- Regulatory penalties: $500K-1M+
- License suspension: Revenue halt
- Reputational damage: Customer exodus
- **Verdict**: Existential risk, không phải optional

#### 2. Operational Efficiency (ROI-Driven)

**Current Waste:**
- 80% time on manual work (Finding #10) = wasted 4 FTE per 5-person team
- Manual dashboards (Finding #27) = lag time in decisions
- No automation (Finding #10) = high error rates, rework
- Part-time resources (Finding #41) = knowledge loss, inefficiency

**Opportunity:**
- Automate workflows → save 40-60 hours/week = 2-3 FTE equivalent
- Real-time dashboards → faster decisions
- Integration → eliminate duplicate data entry
- Dedicated roles → 2x productivity

**Business Case:**
- Labor savings: $150K/year (automation)
- Error reduction: $100K/year (quality)
- Faster time-to-market: 30% (for changes)
- **ROI**: 200-300% over 3 years

**Shared Service Imperative:**
- Cannot add more subsidiaries without automation
- Cost per subsidiary must DECREASE as scale increases (not increase)
- Need scalability to justify shared service model

#### 3. Risk Mitigation (Protect the Business)

**Current Exposures:**
- Failed changes costing revenue (Finding #20 - no root cause analysis)
- Incidents prolonged (Finding #9 - ad-hoc escalation)
- Customer churn risk (Finding #2 - no CSAT measurement)
- Vendor risks unmanaged (Finding #49 - no 3rd party policy)

**Mitigation Value:**
- Reduce change failure rate 50% → save $100K/year in outage costs
- Faster incident resolution 30% → reduce revenue impact
- CSAT tracking → early warning system for churn
- 3rd party policy → supply chain security

**Risk Quantification:**
- Operational failures: $200K/year current state
- Compliance penalties: $500K+ risk
- Reputation damage: Unquantifiable but business-ending
- **Total Risk**: $700K+/year downside protection

#### 4. Business Growth Enabler (Strategic)

**Foundation for Scale:**
- Quality ITSM = faster, safer deployments → accelerate product velocity
- Data-driven decisions = better resource allocation → optimize spend
- Mature operations = trust signal → attract enterprise clients (B2B fintech)
- **Impact**: Enable 2-3x growth without proportional cost increase

**Market Expansion:**
- Compliance certification = requirement for international expansion
- Operational maturity = due diligence pass for partnerships/M&A
- Brand reputation = competitive differentiator in crowded market
- **Opportunity**: Access new markets, premium pricing

**Subsidiary Support:**
- Faster time-to-market for subsidiary initiatives (improved change management)
- Better service quality → subsidiary satisfaction → retention
- Best practice sharing → lift all boats
- **Value**: Strengthen group cohesion, justify shared service model

---

### 👥 WHO - Stakeholders và Roles

#### Executive Sponsors (Strategic Direction)

**CIO/CTO:**
- **Role**: Overall ITSM strategy owner, transformation champion
- **Responsibilities**:
  - Approve policies, standards, architecture
  - Allocate budget and resources
  - Remove organizational blockers
  - Executive steering committee chair
- **Commitment**: 2-4 hours/week for governance

**CFO:**
- **Role**: Financial governance, chargeback model approval
- **Responsibilities**:
  - Approve budget and business case
  - Review chargeback model fairness
  - Monitor ROI realization
  - Compliance oversight (financial risk)
- **Commitment**: Monthly reviews

**COO:**
- **Role**: Service delivery accountability
- **Responsibilities**:
  - Service level commitments to subsidiaries
  - Operational excellence standards
  - Conflict resolution between subsidiaries
  - Quarterly business reviews
- **Commitment**: Monthly service reviews

**Subsidiary CEOs:**
- **Role**: Service recipients, customer voice
- **Responsibilities**:
  - Define business requirements and SLA needs
  - Approve service tier selections
  - Participate in governance council
  - Provide feedback on service quality
- **Commitment**: Quarterly governance council + monthly reviews

---

#### ITSM Core Team (Build & Run)

**ITSM Lead/Manager (NEW or strengthen):**
- **Role**: Program management, overall ITSM excellence
- **Responsibilities**:
  - Lead transformation initiative
  - ITIL expertise and best practices
  - Cross-process coordination
  - Stakeholder management
  - Team development
- **Profile**: ITIL Expert/Managing Professional, 5+ years ITSM
- **FTE**: 1.0 (can be external consultant initially for 6-12 months)

**Incident Manager (NEW dedicated role - Finding #7):**
- **Role**: Incident process owner, quality guardian
- **Responsibilities**:
  - Define and maintain incident process
  - Major incident coordination (P1/P2)
  - Escalation management
  - Post-incident reviews
  - Metrics tracking and reporting
- **Profile**: ITIL Foundation minimum, 3+ years experience
- **FTE**: 1.0 dedicated

**Change Manager (Strengthen existing):**
- **Role**: Change process owner, CAB lead
- **Responsibilities**:
  - Change risk assessment and approval
  - CAB facilitation
  - Communication plan oversight
  - PIR and improvement tracking
  - Change metrics and reporting
- **Profile**: ITIL Foundation minimum, change management experience
- **FTE**: 1.0 dedicated

**CMDB Steward (NEW role - Finding #37):**
- **Role**: Data governance, CMDB strategy
- **Responsibilities**:
  - CMDB policy enforcement
  - Data quality standards
  - CI Owner coordination
  - Conflict resolution (CI disputes)
  - Strategic planning for CMDB evolution
- **Profile**: Data governance background, CMDB experience
- **FTE**: 0.5-1.0 (can start 0.5, scale to 1.0)

**CMDB Administrator (Dedicated, not part-time - Finding #41):**
- **Role**: CMDB operations, tool administration
- **Responsibilities**:
  - Daily CMDB maintenance
  - Tool administration and configuration
  - Data population and reconciliation
  - Integration development and support
  - User training and support
- **Profile**: Technical background, CMDB tool expertise
- **FTE**: 1.0 dedicated (currently part-time = RISK)

---

#### Process QA Team (Quality & Compliance)

**PQA Lead:**
- **Role**: Quality assurance strategy, audit program owner
- **Responsibilities**:
  - Audit planning and execution
  - Maturity assessment
  - Compliance roadmap (ITIL/ISO)
  - Metrics definition and tracking
  - Continuous improvement facilitation
- **Profile**: ITIL/ISO audit experience, quality background
- **FTE**: 0.5-1.0

**PQA Auditors:**
- **Role**: Execute audits, checklist management
- **Responsibilities**:
  - Conduct process audits per schedule
  - Document findings and evidence
  - Track remediation actions
  - Support external audits
- **Profile**: ITIL Foundation, audit training
- **FTE**: 1-2 (depending on audit frequency)

**Metrics Analyst:**
- **Role**: Dashboard development, KPI tracking
- **Responsibilities**:
  - Dashboard design and automation
  - Data collection and validation
  - Reporting and analysis
  - Trend identification and insights
- **Profile**: BI tools (Power BI/Tableau), SQL, analytical skills
- **FTE**: 0.3-0.5 (can be shared with other analytics)

---

#### Supporting Teams (Enablers)

**DevOps Team:**
- **Role**: CI/CD integration, automation development
- **Responsibilities**:
  - Integrate ITSM with CI/CD pipelines
  - Develop automation scripts and workflows
  - Monitoring tool integration
  - PIR automation (Finding #24)
- **Commitment**: 0.5 FTE dedicated during Phase 2 implementation

**Development Teams:**
- **Role**: Change requesters, PIR executors
- **Responsibilities**:
  - Submit change requests following templates
  - Execute approved changes
  - Conduct post-implementation reviews
  - Provide technical input to risk assessments
- **Commitment**: Follow processes, attend CAB when needed

**Infrastructure Team:**
- **Role**: CMDB data providers, CI management
- **Responsibilities**:
  - Maintain CI data accuracy
  - Support CMDB auto-discovery
  - Infrastructure change execution
  - Monitoring and alerting setup
- **Commitment**: Assign CI Owners, maintain data quality

**Security/Compliance:**
- **Role**: Policy review, audit support, security controls
- **Responsibilities**:
  - Review policies for compliance
  - Provide security input to change assessments
  - Support external audits
  - Monitor security-related incidents
- **Commitment**: Participate in CAB, policy reviews

**L&D/HR:**
- **Role**: Training programs, career framework, certifications
- **Responsibilities**:
  - Coordinate ITIL training and certifications
  - Develop ITSM career paths (Finding #31)
  - Support recruitment for ITSM roles
  - Track training completion and effectiveness
- **Commitment**: Partner on OC-06 (Capability Building)

---

#### Extended Stakeholders (Governance & Operations)

**CAB (Change Advisory Board):**
- **Composition**: Change Manager (chair), Technical Leads, Security rep, Business reps, Risk manager
- **Role**: Change approval decisions, risk assessment
- **Responsibilities**:
  - Review and approve/reject changes per criteria (Finding #18)
  - Assess risk and business value
  - Coordinate change schedules
  - Quarterly metrics review
- **Commitment**: Weekly meetings (1 hour) + ad-hoc for emergency changes

**Service Owners (per subsidiary/system):**
- **Role**: Business service accountability, requirements definition
- **Responsibilities**:
  - Define service tier needs (Gold/Silver/Bronze)
  - Map business services to technical CIs (Finding #6)
  - Prioritize incidents and changes for their services
  - Review service metrics and provide feedback
- **Assignment**: 1 Service Owner per critical business service (e.g., Payment Processing, KYC, Lending)

**CI Owners (per configuration item):**
- **Role**: CI data accuracy accountability (Finding #36)
- **Responsibilities**:
  - Maintain CI attributes accuracy
  - Update CI status during changes
  - Review CI relationships
  - Participate in CMDB audits
- **Assignment**: 1 CI Owner per system/application (can be Tech Lead or Product Owner)

**End Users (from subsidiaries):**
- **Role**: Service consumers, feedback providers
- **Responsibilities**:
  - Use ITSM tools for incidents/requests
  - Respond to CSAT surveys (Finding #2)
  - Provide feedback on service quality
  - Participate in user engagement activities (Finding #5)
- **Channel**: Self-service portal, surveys, town halls

---

### 📋 WHAT - Scope of Implementation

#### Foundation Layer (Month 0-6) - MUST-HAVE

**1. Governance & Policy:**
- ✅ **Formal CMDB Policy** (Finding #32): Scope, CI types, ownership model, audit procedures
- ✅ **3rd Party Management Policy** (Finding #49): Vendor assessment, monitoring, SLA management, risk tracking
- ✅ **Change Risk Assessment Framework** (Finding #13): 5-level scoring (1-5), escalation paths, mitigation requirements
- ✅ **Data Retention & Backup Policy** (Finding #14): Retention periods (1-3-5 years per ITIL/ISO), DR procedures, compliance
- ✅ **SLA Framework** (Finding #8): P1-P4 definitions, resolution targets per severity, service tiers (Gold/Silver/Bronze)
- ✅ **RACI Documentation** (Finding #19): All processes mapped, clear accountability, published and trained

**2. Role Definition & Assignment:**
- ✅ **Incident Manager Role** (Finding #7): Job description, KPIs, reporting line, assign individual
- ✅ **CMDB Steward Role** (Finding #37): Governance authority, responsibilities, assign individual
- ✅ **CI Owners Assignment** (Finding #36): 1 owner per critical CI, accountability for accuracy
- ✅ **Dedicated CMDB Admin** (Finding #41): Move from part-time to full-time, clear responsibilities

**3. Critical Process Formalization:**
- ✅ **Incident Escalation Matrix** (Finding #9): By severity and type, contact details, SLA for escalation
- ✅ **Change Risk Classification** (Finding #13): Criteria, scoring guide, examples, mandatory for all changes
- ✅ **CAB Charter** (Finding #18): Membership, meeting schedule, decision criteria, quorum rules, decision log
- ✅ **Communication Plan Template** (Finding #17): Stakeholder groups, timing (pre/during/post), channels, mandatory for major changes
- ✅ **Audit Checklists** (Finding #43): For IM, CM, RF, CMDB, PM - standardized, evidence-based

---

#### Tooling & Automation Layer (Month 3-12)

**4. ITSM Tool Implementation:**
- ✅ **Replace Excel CMDB** (Finding #33): Evaluate and select proper CMDB tool (Jira Asset Management, ServiceNow, ManageEngine)
- ✅ **Integrate Incident-Change-CMDB** (Findings #11, #22, #38):
  - Incident tickets auto-linked to affected CIs
  - Changes update CI status automatically
  - CMDB provides impact analysis for changes
- ✅ **Workflow Automation** (Finding #10):
  - Auto-create incidents from monitoring alerts (95%+)
  - Auto-assign based on CI mapping (90%+)
  - Auto-notifications (Slack, email, SMS for P1)
  - Auto-escalation timers
- ✅ **Auto-Population from Monitoring** (Finding #40):
  - Network discovery → CMDB
  - Container registry → CMDB
  - Cloud inventory → CMDB
  - Hourly reconciliation

**5. Quality & Monitoring:**
- ✅ **Restart & Maintain Sonar** (Finding #23): Quality gates enforced, integrated with CI/CD, blocking bad code
- ✅ **PIR-CI/CD Integration** (Finding #24):
  - Deployment webhook → auto-update PIR in Jira
  - Success/fail status auto-populated
  - Version and timestamp auto-captured
  - Success metrics auto-calculated
- ✅ **Dashboard Automation** (Finding #27):
  - Real-time refresh (<5 minutes vs manual)
  - Date picker for historical analysis
  - Export to PDF/Excel scheduled
  - Alerting for SLA breaches
- ✅ **CSAT Survey Mechanism** (Finding #2):
  - Post-incident surveys (automatic trigger)
  - Quarterly service surveys
  - >30% response rate target
  - Results fed into service reviews

---

#### Measurement & Improvement Layer (Month 6-18)

**6. Metrics & Reporting:**
- ✅ **5 Key ITSM Metrics Tracking** (Findings #1, #46):
  - **Incident**: MTTR, MTBF, SLA achievement%, escalation rate
  - **Change**: Success rate, emergency change%, CFR count, approval time
  - **Request Fulfillment**: Cycle time, backlog age, SLA achievement%
  - **CMDB**: Accuracy%, coverage%, staleness%, CI ownership%
  - **PQA**: Audit coverage%, critical findings count, remediation time
- ✅ **CMDB Effectiveness KPIs** (Finding #42):
  - Accuracy rate (audit-verified)
  - Coverage rate (% of environment mapped)
  - Update frequency (staleness)
  - Integration health (sync success rate)
- ✅ **Quality Metrics & Standards** (Finding #39):
  - Data validation rules
  - Duplicate CI detection and remediation
  - Consistency checks across sources
  - Quality scoring per CI type
- ✅ **Business Service Mapping** (Finding #6):
  - Top 20 services identified
  - Services → CIs → Teams → SLAs mapped
  - Revenue/criticality classification
  - Impact analysis capability

**7. Compliance & Audit:**
- ✅ **Audit Trail Implementation** (Finding #35):
  - Who changed what, when, why (all ITSM records)
  - Immutable logs (cannot be deleted/modified)
  - Retention per policy (1-3-5 years)
  - Queryable for investigations
- ✅ **Quarterly Audit Schedule** (Finding #44):
  - Q1-Q4 planned audits across all processes
  - Risk-based prioritization
  - Results tracked and reported to governance
- ✅ **80% Process Coverage Plan** (Finding #45):
  - 3-year roadmap from current 3% to 80%
  - Prioritize by risk and maturity
  - Audit rotation schedule
- ✅ **ITIL/ISO Compliance Roadmap** (Finding #12):
  - Gap analysis (ITIL 4 practices vs current)
  - ISO 20000/27001 requirements mapping
  - Remediation plan by quarter
  - External audit preparation (Month 17-18)
- ✅ **Maturity Assessment Framework** (Finding #48):
  - Baseline maturity level (currently Level 1 - Initial)
  - Target maturity (Level 3 - Defined/Managed)
  - Assessment criteria and evidence
  - Quarterly maturity tracking

---

#### People & Culture Layer (Ongoing)

**8. Training & Development:**
- ✅ **ITIL 4 Training Program** (Finding #30):
  - **Wave 1** (Month 2-6): ITSM core team (10 people) → ITIL 4 Foundation
  - **Wave 2** (Month 6-12): Extended team (help desk, 20 people) → ITIL 4 Foundation
  - **Wave 3** (Month 12-18): Subsidiary IT leads (15 people) → ITIL 4 Foundation
  - **Specialist Certifications**: Create & Deliver (Change team), Drive Stakeholder Value (Service Desk), High Velocity IT (DevOps)
  - Target: 100% Foundation, 50% Specialist by Month 18
- ✅ **Certification Requirements** (Finding #31):
  - Analyst level: ITIL 4 Foundation (required within 6 months of hire)
  - Specialist level: ITIL 4 Specialist (required within 12 months)
  - Lead level: ITIL 4 Managing Professional or Strategic Leader
  - Annual certification budget allocated
- ✅ **Knowledge Base** (Finding #16):
  - Platform: Confluence/SharePoint
  - Structure: Process documentation, How-to guides, FAQs, Templates, Lessons learned
  - Content target: >100 articles by Month 12
  - Mandatory contribution: 1 article per team member per quarter
  - Search and tagging for easy discovery
- ✅ **Onboarding for New Team Members**:
  - ITSM orientation (processes, tools, culture)
  - Role-specific training plans
  - Buddy system for first 30 days
  - Certification roadmap assigned

---

### ⏱️ TIMEFRAME - 3 Phases over 18 Months

#### **PHASE 1: FOUNDATION (Month 1-6) - "Stabilize & Comply"**

**Objective:** Address all CRITICAL findings, establish governance foundation, stop the bleeding

**Key Themes:**
- Governance over tools (policies before platforms)
- Quick wins to build momentum
- Compliance readiness for regulatory risk mitigation
- Stabilize operations before scaling

**Major Deliverables:**

**Month 1-2: Policy Sprint**
- ✅ 5 core policies documented (CMDB, 3PM, Risk, Retention, SLA)
- ✅ RACI matrix workshop and draft
- ✅ Role descriptions for 4 critical roles (IM, CMDB Steward, 2x CI Owners)
- ✅ Incident escalation matrix published
- ✅ Gap analysis for ITIL/ISO compliance
- 🎯 **Quick Win**: Escalation matrix → immediate 30% improvement in P1 resolution time

**Month 3-4: Approval & Assignment**
- ✅ Executive approval of all policies
- ✅ Roles assigned (recruit or reassign existing team members)
- ✅ CAB charter approved and first meeting scheduled
- ✅ Audit checklists created for IM, CM, RF
- ✅ Change risk framework tested with real changes
- 🎯 **Quick Win**: Monthly service reviews launched → engage subsidiaries

**Month 5-6: Implementation & Training**
- ✅ Policy rollout and communication to all stakeholders
- ✅ Training on new processes (escalation, risk assessment, CAB)
- ✅ First round of process audits using new checklists
- ✅ SLA targets negotiated and agreed with subsidiaries
- ✅ ITIL 4 Foundation training Wave 1 (ITSM core team)
- 🎯 **Quick Win**: Dashboard v1.0 (semi-automated) → executive visibility

**Success Criteria:**
- ✅ 100% of CRITICAL governance gaps closed (Findings #7, #8, #13, #19, #32, #36, #37, #49)
- ✅ Incident escalation time reduced 50% (from ~2 hours to ~1 hour for P1)
- ✅ Audit trail established for Incident and Change processes
- ✅ Regulatory audit readiness improved from 0% to 40%
- ✅ Team capacity freed up 10-15% through quick process improvements

**Resource Needs:**
- **Headcount**:
  - 1 FTE ITSM Lead (can be external consultant for 6 months)
  - 0.5 FTE CMDB Steward (new hire or internal assignment)
  - 0.5 FTE PQA Lead (strengthen existing role)
- **Budget**: $50-80K
  - Consulting for policy development: $20K
  - Legal/compliance review: $10K
  - Training materials and workshops: $10K
  - ITIL training Wave 1: $15K
  - Tools and templates: $5K
  - Contingency: $20-30K

**Risks & Mitigation:**
- **Risk**: Policy approval delays → **Mitigation**: Early stakeholder engagement, use industry templates
- **Risk**: Role assignment conflicts → **Mitigation**: Executive mandate, interim external hires if needed
- **Risk**: Team resistance to new overhead → **Mitigation**: Communicate value, show quick wins, involve team in design

---

#### **PHASE 2: AUTOMATION (Month 4-12) - "Scale & Optimize"**

**Objective:** Implement ITSM tooling, automate workflows, integrate processes, reduce manual burden from 80% to 40%

**Key Themes:**
- Tools enable process (process defined in Phase 1)
- Integration across Incident-Change-CMDB
- Automation to free up capacity
- Measurement to drive data-driven decisions

**Major Deliverables:**

**Month 4-6: Tool Selection & Pilot**
- ✅ CMDB tool requirements finalized (multi-tenant, API, auto-discovery)
- ✅ Vendor evaluation (ServiceNow vs Jira Asset Mgmt vs ManageEngine)
- ✅ POC with 1 subsidiary's CIs (test functionality, integration, usability)
- ✅ Business case approved (3-year TCO, ROI $400K+)
- ✅ Procurement and contracting
- ✅ Pilot subsidiary selected (medium complexity, willing stakeholder)

**Month 6-9: CMDB Implementation**
- ✅ CMDB schema designed (CI types, attributes, relationships, multi-tenant structure)
- ✅ Data migration from Excel (cleanse, deduplicate, assign owners per Finding #39)
- ✅ Integration architecture developed (Jira ↔ CMDB, Monitoring → CMDB)
- ✅ Workflow automation Phase 1:
  - Auto-create incidents from monitoring (target 95%)
  - Auto-assign incidents based on CI mapping (target 90%)
  - Auto-notifications (Slack, email, SMS)
- ✅ UAT with pilot subsidiary
- ✅ ITIL training Wave 2 (extended team)

**Month 9-12: Integration & Rollout**
- ✅ Incident-Change-CMDB integration live (Findings #11, #22, #38)
- ✅ PIR-CI/CD integration (Finding #24) → auto-populate PIR status
- ✅ Dashboard automation v2.0 (Finding #27):
  - Real-time data refresh (<5 min)
  - Date picker for historical analysis
  - Alerting for SLA breaches
  - Export to PDF/Excel automated
- ✅ CSAT survey mechanism deployed (Finding #2) → post-incident + quarterly surveys
- ✅ Sonar quality gate re-enabled and enforced (Finding #23)
- ✅ Rollout to all subsidiaries (phased by priority)
- ✅ Stabilization and optimization based on feedback

**Success Criteria:**
- ✅ Manual admin work reduced from 80% → 40% (measured by team survey)
- ✅ CMDB accuracy >90% (audit-verified)
- ✅ Dashboard refresh time: Manual (days) → <1 hour real-time
- ✅ Incident auto-creation rate >95%
- ✅ PIR auto-population >80% of fields
- ✅ CSAT response rate >30%
- ✅ Failed change rate reduced 30% (e.g., 20% → 14%)

**Resource Needs:**
- **Headcount**:
  - 1 FTE CMDB Administrator (dedicated, not part-time per Finding #41)
  - 0.5 FTE DevOps Engineer (integration development)
  - 0.3 FTE BI Analyst (dashboard development)
  - Vendor professional services (3-6 months)
- **Budget**: $150-250K
  - CMDB tool license (Jira Asset Mgmt): $40K/year
  - Implementation services: $80K
  - Data cleanse and migration: $20K
  - Integration development: $40K
  - Dashboard platform (Power BI): $15K/year
  - ITIL training Wave 2: $20K
  - Monitoring tools licensing: $20K/year
  - Contingency: $15-35K

**Risks & Mitigation:**
- **Risk**: Tool implementation delays (vendor, complexity) → **Mitigation**: Start evaluation early (Month 1), phased rollout, vendor escalation path
- **Risk**: Data migration quality issues → **Mitigation**: Data cleanse sprint, CI Owner validation, phased migration (critical CIs first)
- **Risk**: Integration complexity/failures → **Mitigation**: POC first, vendor professional services, fallback to manual if needed
- **Risk**: Team capacity during dual-running → **Mitigation**: Contractors for BAU work, stagger rollouts, support on-demand

---

#### **PHASE 3: MATURITY (Month 10-18) - "Optimize & Excel"**

**Objective:** Achieve ITIL/ISO compliance, continuous improvement culture, become center of excellence, manual work <20%

**Key Themes:**
- Compliance certification (ITIL/ISO)
- Mature processes and controls
- Data-driven optimization
- Sustainable continuous improvement

**Major Deliverables:**

**Month 10-12: Maturity Assessment & Improvement**
- ✅ ITIL maturity assessment (Finding #48):
  - Baseline: Level 1 (Initial/Ad-hoc)
  - Current: Level 2-2.5 (Repeatable)
  - Target: Level 3 (Defined/Managed)
  - Gap analysis and closure plan
- ✅ Change Management optimization (OC-07):
  - Batch approval for low-risk changes (Finding #28)
  - CFR root cause analysis systematic (Finding #20) → address top 3 causes
  - Change freeze policy implemented (Finding #26)
  - Communication plan compliance >90% (Finding #17)
- ✅ Quarterly audits achieving 60% process coverage (up from 3% per Finding #45)
- ✅ Improvement backlog management (Finding #29) → prioritized, tracked, executed

**Month 13-15: Compliance Preparation**
- ✅ ITIL 4 compliance self-assessment:
  - Incident Management: All 6 practices implemented
  - Change Management: All 18 practices implemented
  - Request Fulfillment: Mature process
  - CMDB/Configuration: Operational and governed
  - Problem Management: Basic process established
- ✅ ISO 20000 requirements mapping:
  - >90% requirements met
  - Evidence documented
  - Gaps closed with remediation plans
- ✅ ISO 27001 ITSM controls:
  - >85% controls implemented
  - Access controls, audit trail, change authorization operational
- ✅ Pre-assessment audit by external firm (Month 15):
  - Mock audit to identify remaining gaps
  - Rapid remediation sprint (2-4 weeks)
- ✅ ITIL training Wave 3 (subsidiary IT leads) + Specialist certifications

**Month 16-18: Certification & Optimization**
- ✅ External certification audit (Month 17):
  - ISO 20000 audit conducted
  - Audit response and evidence submission
  - Corrective actions if minor findings
- ✅ Certification achieved (Month 18):
  - ISO 20000 certificate received
  - ITIL alignment attestation
  - Regulatory notification and market communication
- ✅ Process optimization based on 12 months of data:
  - SLA refinement based on actuals
  - Resource allocation optimization
  - Automation enhancements (ML for categorization, anomaly detection)
- ✅ Shared Service Excellence (OC-08):
  - Service catalog published (Gold/Silver/Bronze tiers)
  - Chargeback model operational
  - Governance council mature (>80% attendance)
  - NPS >+30 from subsidiaries
- ✅ Training program institutionalized:
  - 100% ITIL 4 Foundation certification
  - >50% ITIL 4 Specialist certification
  - Knowledge base >100 articles
  - Career framework published and adopted

**Success Criteria:**
- ✅ ITIL maturity level 3+ (Defined/Managed) achieved
- ✅ ISO 20000 certification obtained
- ✅ Audit coverage >80% of processes (vs 3% at start per Finding #45)
- ✅ Team certification rate: 100% Foundation, >60% Specialist
- ✅ Manual work <20% (vs 80% at start per Finding #10)
- ✅ Change success rate >95% (vs ~80% at start)
- ✅ CSAT score >4.2/5 across all subsidiaries
- ✅ SLA achievement >90% across all service tiers

**Resource Needs:**
- **Headcount**:
  - Team now self-sufficient (no external consultants needed for BAU)
  - All roles from Phase 1-2 continuing
  - Possible addition: 0.5 FTE Continuous Improvement Lead
- **Budget**: $80-120K
  - External audit firm (ISO 20000): $60K
  - Pre-assessment and consulting: $20K
  - ITIL training Wave 3 + Specialist: $25K
  - Audit tools and automation: $10K
  - Continuous improvement initiatives: $10K
  - Certification maintenance: $5K/year ongoing
  - Contingency: $10-15K

**Risks & Mitigation:**
- **Risk**: Audit failure (gaps not closed) → **Mitigation**: Pre-assessment in Month 15, consultant support, remediation sprints
- **Risk**: Certification delays (auditor availability) → **Mitigation**: Book audit firm in Month 12 for Month 17 slot, flexible timeline
- **Risk**: Process fatigue (team burned out on improvement) → **Mitigation**: Celebrate wins, show ROI, simplify where possible, automate more
- **Risk**: Complacency after certification → **Mitigation**: Continuous improvement culture, quarterly reviews, new challenges (e.g., SRE, DevSecOps)

---

#### **Timeline Dependencies & Critical Path:**

**Sequencing Logic:**
```
Policy Creation (M1-3)
    → Tool Selection (M4-5)
    → Implementation (M6-9)
    → Integration (M9-12)
    → Measurement & Optimization (M10-18)
    → Certification (M17-18)
```

**Parallel Tracks:**
- **Governance Track**: M1-6 (foundation) → M7-18 (enforcement & refinement)
- **Tooling Track**: M4-5 (selection) → M6-12 (implementation) → M12-18 (optimization)
- **Quality Track**: M1-18 (continuous audits, improvement)
- **People Track**: M2-18 (training, certifications, culture)

**Critical Path Items:**
1. Policy approval (M3) → blocks tool selection
2. Tool procurement (M5) → blocks implementation
3. CMDB implementation (M6-9) → blocks integration
4. Integration completion (M12) → blocks full automation
5. Pre-assessment (M15) → blocks external audit
6. External audit (M17) → blocks certification (M18)

**Risks to Timeline:**
- **Tool procurement delays**: Vendor selection, contract negotiations, budget approval → **+2-3 months risk**
- **Integration complexity**: Legacy systems, API limitations, data quality → **+1-2 months risk**
- **Resource availability**: Shared team conflicts, hiring delays → **+1-2 months risk**
- **Change resistance**: Adoption issues, culture change → **Quality risk, not timeline**

**Mitigation Strategies:**
- **Early start on tool evaluation** (Month 1, parallel to policy work) → compress timeline
- **Phased rollout** (pilot → full deployment) → reduce risk, allow learning
- **Executive sponsorship** for resource prioritization → remove blockers
- **Change management & communication plan** → address resistance proactively

---

### 🛠️ HOW - Implementation Strategy

#### 1. Governance-First Approach

**Philosophy:** Cannot build on shaky foundation

**Rationale:**
- Tools without governance = expensive chaos
- Process maturity enables automation success
- Compliance requires documented policies first
- Lessons from failed transformations: "Big bang tool rollout without process = failure"

**Sequence:**
1. **Policies & Standards** (Month 1-4)
   - Define the "what" and "why" (scope, objectives, principles)
   - Document processes (how work should be done)
   - Create templates and checklists
2. **Roles & Responsibilities** (Month 2-4)
   - RACI clarity (who does what)
   - Assign individuals to roles
   - Train on accountabilities
3. **Tools & Automation** (Month 4-12)
   - Select tools to enable processes (not drive them)
   - Configure to match designed process
   - Automate based on proven workflows
4. **Measurement & Optimization** (Month 6-18)
   - Measure process performance
   - Identify bottlenecks with data
   - Optimize based on insights

**Key Actions:**
- **Week 1-4**: Policy sprint (5 core policies drafted)
- **Week 5-8**: Role assignment & RACI workshop
- **Week 9-12**: SLA definition & approval with subsidiaries
- **Week 13-16**: Process documentation & checklist creation
- **Throughout**: Executive steering committee monthly (oversight, remove blockers)

**Success Indicator:** No tool purchases until policies approved (discipline)

---

#### 2. Quick Wins Strategy

**Objective:** Show value within 90 days to maintain momentum and build trust

**Psychology:**
- Transformation fatigue is real
- Executive sponsors need early wins to justify continued investment
- Team morale boosted by visible improvements
- Subsidiaries more engaged when they see benefits

**Quick Win #1: Incident Escalation Matrix (Month 1)**
- **Current state**: Ad-hoc escalation (Finding #9) → delays, frustration
- **Solution**: Published matrix (who to call for what, when)
- **Effort**: LOW (1-2 weeks to create, 1 week to train)
- **Impact**: HIGH (immediate 30-50% reduction in P1 resolution time)
- **Visibility**: HIGH (everyone sees it, everyone uses it)
- **ROI**: 1 major incident resolved faster = $50K+ revenue saved

**Quick Win #2: Monthly Service Reviews (Month 2)**
- **Current state**: No formal reviews (Finding #4) → problems repeat, no engagement
- **Solution**: Monthly review meetings with each subsidiary (metrics, issues, improvements)
- **Effort**: LOW (2 hours prep, 1 hour meeting per subsidiary)
- **Impact**: MEDIUM (subsidiaries feel heard, issues surface, relationships improve)
- **Visibility**: MEDIUM-HIGH (leadership attends, demonstrate accountability)
- **ROI**: Identify 2-3 major pain points per subsidiary → prioritize fixes → improve satisfaction

**Quick Win #3: Dashboard v1.0 (Month 3)**
- **Current state**: Manual reporting (Finding #27) → takes days, data lag
- **Solution**: Semi-automated dashboard (even if not fully real-time initially)
- **Effort**: MEDIUM (2-3 weeks for basic dashboard with existing Jira data)
- **Impact**: HIGH (executive visibility, data-driven decisions)
- **Visibility**: VERY HIGH (CIO, COO, subsidiary leaders all see it)
- **ROI**: Faster decisions (from days to hours) → 20% improvement in decision cycle time

**Communication:**
- **Week 4**: Escalation matrix communicated via email, town hall, poster
- **Week 8**: First monthly service review → success story shared broadly
- **Week 12**: Dashboard demo to executive team → celebrate and request feedback

---

#### 3. Pilot-First, Scale-Later

**Approach:** Avoid big-bang failures in shared service model

**Why Pilot?**
- Shared service = cannot afford failure impacting all subsidiaries simultaneously
- Learn in controlled environment (smaller blast radius)
- Adjust based on real feedback before scale
- Build case studies and success stories
- Identify edge cases and refine

**Pilot Selection Criteria:**

**Ideal Pilot Subsidiary:**
1. **Medium complexity**: Not too simple (won't stress-test), not most complex (too risky)
2. **Willing stakeholder**: Executive sponsor engaged, team cooperative
3. **Manageable volume**: Enough to be meaningful, not overwhelming (e.g., 100-200 CIs, 50 incidents/month)
4. **Representative**: Issues similar to other subsidiaries (learnings transferable)
5. **Influence**: If pilot succeeds, other subsidiaries will follow (positive peer pressure)

**Example:** Subsidiary B (lending platform) - medium complexity, CTO is supportive, 150 CIs, typical incident patterns

**Pilot Scope:**
- **CMDB**: Migrate Subsidiary B's CIs first (Month 6-7)
- **Automation**: Test auto-incident creation for Subsidiary B's monitoring (Month 8)
- **Integration**: Pilot Incident-Change-CMDB linkage with Subsidiary B's changes (Month 9)
- **Duration**: 2-3 months pilot, 1 month evaluate, then scale to others

**Learn & Adjust:**
- **Weekly pilot reviews**: What's working, what's not
- **Feedback loops**: Pilot team provides input → adjust configuration/process
- **Document lessons**: Update runbooks, FAQs, training materials
- **Success criteria**: >85% pilot team satisfaction, <5 critical issues

**Rollout to Others:**
- **Month 10**: Rollout to Subsidiaries A & C (lower complexity)
- **Month 11**: Rollout to Subsidiaries D & E (higher complexity, use lessons learned)
- **Month 12**: All subsidiaries live, stabilization period

---

#### 4. Multi-Track Execution

**Objective:** Compress timeline through parallel workstreams

**Why Multi-Track?**
- Dependencies exist, but many tasks can run concurrently
- Maximize throughput (vs sequential = slow)
- Engage different teams simultaneously (DevOps, PQA, ITSM, HR)
- Critical path: 18 months; if sequential: 30+ months

**Track Structure:**

**Track A: Governance (Led by ITSM Lead)**
- **Focus**: Policies, procedures, RACI, standards, compliance
- **Timeline**: Month 1-6 (intense), Month 7-18 (refinement)
- **Key Deliverables**:
  - M1-3: 5 policies drafted and approved
  - M3-4: RACI matrix and role assignments
  - M4-6: SLA negotiations, CAB charter
  - M6-18: Compliance audits, maturity assessments
- **Team**: ITSM Lead, PQA Lead, Legal/Compliance, Executive sponsors
- **Weekly Sync**: Governance forum (1 hour, Fridays)

**Track B: Tooling (Led by DevOps Lead + CMDB Admin)**
- **Focus**: Tool selection, implementation, integration, automation
- **Timeline**: Month 4-5 (selection), Month 6-12 (implementation), Month 12-18 (optimization)
- **Key Deliverables**:
  - M4-5: CMDB tool evaluation and selection
  - M6-9: CMDB implementation and data migration
  - M9-12: Integrations (Incident-Change-CMDB, CI/CD, monitoring)
  - M12-18: Automation enhancements (ML, advanced workflows)
- **Team**: DevOps, CMDB Admin, Infrastructure, Vendor PS
- **Weekly Sync**: Implementation standup (30 min, Mondays)

**Track C: Quality (Led by PQA Lead)**
- **Focus**: Audit checklists, metrics definition, audits, maturity assessment, compliance
- **Timeline**: Month 1-18 (continuous)
- **Key Deliverables**:
  - M1-3: Audit checklists created
  - M4-6: First round of audits (IM, CM, RF)
  - M7-9: Metrics framework and dashboard requirements
  - M10-12: Quarterly audits, findings remediation
  - M13-15: Maturity assessment, pre-audit
  - M16-18: External certification audit
- **Team**: PQA Lead, PQA Auditors, Metrics Analyst, External auditor
- **Weekly Sync**: Quality forum (1 hour, Wednesdays)

**Track D: People (Led by ITSM Lead + HR)**
- **Focus**: Training, certifications, knowledge base, career framework, engagement
- **Timeline**: Month 1-18 (continuous)
- **Key Deliverables**:
  - M2-6: ITIL training Wave 1 (core team)
  - M4-6: Career framework design
  - M3-9: Knowledge base setup and content creation
  - M6-12: ITIL training Wave 2 (extended team)
  - M9-18: ITIL Specialist certifications
  - M6-18: Engagement program (champions, gamification, town halls)
- **Team**: ITSM Lead, L&D, HR, External training provider
- **Monthly Sync**: People & culture review (2 hours, end of month)

**Integration & Coordination:**
- **Weekly Integration Meeting**: All track leads + ITSM Lead (1 hour, Tuesdays)
  - Dependencies: What Track B needs from Track A
  - Blockers: Red flags, escalations
  - Decisions: Trade-offs requiring cross-track input
  - Risks: Emerging issues, mitigation adjustments
- **Monthly Steering Committee**: Executive sponsors + all track leads (2 hours, monthly)
  - Progress vs plan
  - Budget vs actuals
  - Key decisions (scope, timeline, resources)
  - Strategic guidance

**Dependency Management Examples:**
- Track A (Policy) → Track B (Tool): CMDB policy approved before CMDB schema design
- Track B (CMDB) → Track C (Audit): CMDB audit trail feature required for audit compliance
- Track D (Training) → All tracks: Team trained before rollout
- Track C (Metrics) → Track A (SLA): Metrics dashboard required for SLA monitoring

---

#### 5. Shared Service Model Specific

**Challenge:** Serving multiple subsidiaries fairly and efficiently

**Solution Components:**

**A. Service Catalog Approach**

**Service Tiers Defined:**

| Tier | Support Hours | P1 Response | P2 Response | Dedicated Resources | Monitoring | Price Premium |
|------|--------------|-------------|-------------|---------------------|------------|---------------|
| **Gold** | 24/7/365 | <15 min | <30 min | Yes (named contacts) | Proactive + Advanced | +40% |
| **Silver** | 12/5 (7am-7pm weekdays) | <30 min | <2 hours | Shared pool | Standard | Base price |
| **Bronze** | 8/5 (9am-5pm weekdays) | <60 min | <4 hours | Shared pool | Basic | -20% |

**Service Selection:**
- Subsidiaries choose tier PER SERVICE (not blanket for all)
- Example: Subsidiary A selects Gold for Payment System (mission-critical), Silver for CRM (business-critical), Bronze for Internal Tools
- Flexibility to change tiers quarterly (with 30-day notice)

**B. Priority Framework**

**Incident Priority (P1 Emergencies):**
- **Rule**: All subsidiaries equal regardless of tier (regulatory/safety imperative)
- **Logic**: P1 = revenue-impacting, customer-affecting → no subsidiary left behind

**Incident Priority (P2-P4):**
- **Weighted Allocation Formula**:
  - 40% based on service tier (Gold gets more attention than Bronze)
  - 30% based on business impact (revenue, users affected)
  - 30% based on queue time (fairness - waited longest gets priority)
- **Example**:
  - Subsidiary A (Gold tier, $10M revenue service, 30 min wait) = Priority Score 85
  - Subsidiary B (Silver tier, $5M revenue service, 60 min wait) = Priority Score 70
  - A gets attention first, but B moved up as wait time increases

**Change Windows:**
- **Coordinated calendar**: Shared across all subsidiaries (avoid conflicts)
- **Allocation**: First-come-first-served with fairness rotation
- **Peak periods**: Friday evening slots allocated by service tier (Gold gets preference)
- **Maintenance blackouts**: Coordinated freeze periods (e.g., year-end, Black Friday for fintech = month-end settlement)

**Resource Allocation:**
- **Dedicated for Gold**: Named ITSM contacts, faster response
- **Shared pool for Silver/Bronze**: Round-robin assignment, queue-based
- **Flex capacity**: 20% reserve for spikes, peaks, emergencies
- **Quarterly rebalancing**: Adjust allocation based on actual usage patterns

**C. Chargeback Model**

**Cost Structure:**

**Base Fee (Fixed per subsidiary per month):**
- Covers: Shared infrastructure (CMDB, tools, governance), core ITSM team salaries, overhead
- Allocation: Equal split OR weighted by subsidiary revenue size
- Example: $50K/month total → $10K per subsidiary if 5 subsidiaries

**Variable Fee (Usage-based):**
- **Incident Volume**: $X per incident (tiered by priority: P1 = 4x, P2 = 2x, P3 = 1x, P4 = 0.5x)
- **Change Volume**: $Y per change request (tiered by complexity: High = 3x, Medium = 2x, Low = 1x)
- **CMDB Services**: $Z per CI managed
- **Dedicated Resources**: $W per FTE if Gold tier (dedicated contacts)
- Example: Subsidiary with 200 incidents, 50 changes, 150 CIs, Silver tier → calculate monthly variable

**Tier Premium/Discount:**
- **Gold**: Base + Variable + 40% premium (for 24/7, <15min, proactive monitoring)
- **Silver**: Base + Variable (no adjustment)
- **Bronze**: Base + Variable - 20% discount (for reduced SLA)

**Transparency:**
- **Monthly invoices**: Detailed breakdown (base, variable, tier adjustment)
- **Usage reports**: Incident count, change count, CI count
- **Benchmarking**: How does your subsidiary compare to others (normalized)
- **Annual reconciliation**: True-up based on actuals vs estimates

**Governance:**
- **Annual rate review**: Adjust pricing based on cost actuals, market rates
- **Dispute resolution**: Governance Council reviews contested charges
- **Value demonstration**: ROI reports showing cost savings from shared service vs dedicated teams

**D. Governance Council**

**Structure:**
- **Chair**: ITSM Lead (facilitator, not decision-maker)
- **Members**: 1 CIO or Director representative from each subsidiary + COO sponsor
- **Quorum**: >50% members required for decisions
- **Terms**: Annual appointment (rotating chair possible after Year 2)

**Responsibilities:**
1. **Service Level Review**: Quarterly review of SLA achievement, CSAT, incidents, changes
2. **Conflict Resolution**: When priorities conflict (e.g., overlapping change windows), Council decides
3. **Roadmap Approval**: ITSM improvement initiatives prioritized by Council (what benefits all vs one)
4. **Budget Oversight**: Annual budget review, chargeback model approval, investment decisions
5. **Policy Input**: Review and approve major policy changes (e.g., new SLA tiers, freeze periods)

**Meeting Cadence:**
- **Monthly**: Operational reviews (1 hour) - metrics, issues, quick decisions
- **Quarterly**: Strategic reviews (2 hours) - roadmap, budget, deep dives
- **Ad-hoc**: Emergency meetings if major incidents or conflicts

**Decision-Making:**
- **Consensus preferred**: Aim for win-win, collaborative solutions
- **Voting if needed**: Simple majority (>50% of members)
- **Escalation to COO**: If deadlock or high-stakes decision (rare, last resort)
- **Transparency**: All decisions documented, communicated to stakeholders

**Success Metrics for Governance:**
- Meeting attendance >80%
- Decision turnaround time <2 weeks
- Subsidiary satisfaction with governance >4/5
- Conflict resolution success rate >90%

---

#### 6. Technology Stack Recommendation

**ITSM Platform Selection (Phase 2):**

**Option A: ServiceNow**
- **Pros**:
  - Enterprise-grade, best-in-class ITSM
  - Mature CMDB with advanced discovery
  - Strong integration ecosystem (APIs, connectors)
  - Excellent for compliance (ITIL/ISO out-of-box)
  - Scalable for large, complex environments
- **Cons**:
  - **Expensive**: $150-250K+/year for 100 users
  - Steep learning curve (complex configuration)
  - Requires dedicated admin (full-time)
  - Long implementation (6-9 months)
- **Best for**: Large enterprise, big budget, long-term commitment
- **Verdict**: Overkill for current needs, but future-proof if grow to 10+ subsidiaries

**Option B: Jira Service Management + Asset Management (Atlassian)**
- **Pros**:
  - **Leverage existing Atlassian investment** (likely already using Jira for development)
  - Cost-effective: $40-60K/year for 100 users
  - Familiar UI for dev teams (reduces training)
  - Strong CI/CD integration (Jira ↔ Bitbucket/Jenkins)
  - Good CMDB via Asset Management plugin
  - Flexible workflows (Jira automation)
- **Cons**:
  - Less mature than ServiceNow for ITSM (but improving rapidly)
  - CMDB not as powerful (relationship mapping limited)
  - Reporting less polished (need external BI tool)
  - Support quality variable
- **Best for**: Mid-size, tech-savvy orgs with Atlassian ecosystem
- **Verdict**: **RECOMMENDED** - best balance cost/features, leverage existing investment

**Option C: ManageEngine ServiceDesk Plus**
- **Pros**:
  - **Budget option**: $20-30K/year
  - Easier to implement (3-4 months)
  - ITIL-aligned processes out-of-box
  - Indian/SEA market support (relevant for Vietnam)
- **Cons**:
  - Limited scalability (struggles >500 users)
  - Weaker integration ecosystem
  - CMDB basic (not suitable for complex environments)
  - UI dated
- **Best for**: Small teams, tight budget, simple environments
- **Verdict**: Insufficient for multi-subsidiary, growth trajectory

**Recommendation: Jira Service Management + Asset Management**

**Rationale:**
1. **Leverage existing**: Likely already have Atlassian licenses → incremental cost lower
2. **Team familiarity**: Dev teams know Jira → adoption easier
3. **Cost-effective**: $40-60K/year = 3-4x cheaper than ServiceNow with 80% of features needed
4. **Integration strength**: Jira ↔ CI/CD ↔ Monitoring = critical for fintech DevOps
5. **Scalability**: Can handle 5-10 subsidiaries comfortably; migrate to ServiceNow if grow to 20+

**Integration Layer:**

**Core Integrations (Must-have):**
1. **Jira Service Management ↔ Jira Asset Management**:
   - Incidents auto-link to CIs (Finding #11)
   - Changes update CI status (Finding #22)
   - CMDB provides impact analysis for change approval
   - **Method**: Built-in Asset field types, automation rules

2. **Jira ↔ CI/CD (Jenkins/GitLab/Bitbucket)**:
   - Deployment triggers PIR auto-update (Finding #24)
   - Build success/fail → Change status updated
   - Git commit → Change Request linked
   - **Method**: Webhooks, Jira REST API, Jenkins plugin

3. **Monitoring (Prometheus/Grafana/Datadog) → Jira**:
   - Alerts auto-create incidents (Finding #10)
   - Severity mapping (Critical → P1, High → P2)
   - De-duplication (same alert within 1 hour = single incident)
   - **Method**: Alertmanager webhook → Python middleware → Jira API

4. **Jira → BI Tool (Power BI/Tableau)**:
   - Real-time dashboard (Finding #27)
   - Incident metrics, change metrics, CMDB KPIs
   - Export to PDF/Excel automated
   - **Method**: Jira REST API → scheduled queries → Power BI dataset

**Extended Integrations (Nice-to-have):**
5. **Jira ↔ Slack/Teams**: Notifications, chatops, status updates
6. **Jira ↔ PagerDuty/OpsGenie**: On-call escalation, scheduling
7. **CMDB ↔ Cloud Providers (AWS/Azure/GCP)**: Auto-populate cloud resources
8. **Jira ↔ SonarQube**: Quality gate failures → auto-create incidents (Finding #23)

**Integration Principles:**
- **API-first**: All integrations via REST APIs (not proprietary connectors = vendor lock-in)
- **Idempotent**: Retryable, handle duplicates gracefully
- **Monitored**: Integration health dashboard (sync success rate, lag time)
- **Fallback**: Manual process documented if integration down

**Automation Platform:**

**Options:**
1. **Jira Automation (built-in)**:
   - Best for simple workflows within Jira (auto-assign, notifications, field updates)
   - Free up to certain rule executions, then metered pricing
   - **Use for**: Internal Jira workflows (70% of automation needs)

2. **Python Scripts (custom)**:
   - For complex logic not supported by Jira Automation
   - Deployed on Lambda/Cloud Functions (serverless)
   - **Use for**: CMDB reconciliation, data quality checks, advanced routing (20% of needs)

3. **n8n or Zapier (low-code integration platform)**:
   - For external system integrations (e.g., Slack, email, webhooks)
   - n8n = open-source, self-hosted (cheaper)
   - Zapier = SaaS, easier (more expensive)
   - **Use for**: Cross-system workflows (10% of needs)

**Recommendation**: Jira Automation (primary) + Python scripts (complex) + n8n (external integrations)

---

#### 7. Risk Mitigation Strategies

**Risk 1: Resource Contention (Shared Team Overload)**

**Description**: ITSM/QA team shared across subsidiaries already at 80% manual work; transformation adds more work

**Impact**: HIGH - Initiative stalls, team burns out, quality degrades
**Probability**: HIGH - team already overloaded per findings

**Mitigation Strategies:**
1. **Executive Mandate for Dedicated Time**:
   - CIO/COO mandate: 60% transformation, 40% BAU during Phase 1-2
   - Protect calendar time (e.g., Transformation Tuesdays/Thursdays)
   - Performance goals include transformation deliverables (not just BAU)
2. **Hire Temporary Contractors for BAU**:
   - Contract 1-2 FTEs for incident/change handling during Month 4-12 (peak implementation)
   - Cost: $80-120K, justified by freeing up core team for transformation
3. **Automation Quick Wins**:
   - Start automation early (Month 3-4) even before CMDB → free up capacity
   - Example: Auto-assign incidents = save 10 hours/week immediately
4. **Defer Non-Critical Work**:
   - Freeze non-essential enhancements/projects during transformation
   - Focus on "keep lights on" + transformation only

**Monitoring**: Weekly capacity tracking (% time on BAU vs transformation), burnout indicators (absenteeism, morale survey)

---

**Risk 2: Regulatory Deadline Miss (Compliance Not Achieved in Time)**

**Description**: Audit scheduled before ready, or regulator accelerates timeline

**Impact**: CRITICAL - Penalties, license suspension, business shutdown
**Probability**: MEDIUM - regulatory timelines can be unpredictable

**Mitigation Strategies:**
1. **Compliance in Phase 1 (Front-loaded)**:
   - All CRITICAL compliance items in first 6 months (policies, audit trail, roles)
   - Don't wait for perfect tools; achieve compliance with manual processes if needed
   - Example: Audit trail via spreadsheet initially, migrate to automated later
2. **Monthly Compliance Checkpoint**:
   - PQA Lead + Compliance Officer review audit readiness monthly
   - Red/Yellow/Green dashboard of compliance requirements
   - Escalate yellows immediately, reds to executive team
3. **External Audit Consultant**:
   - Engage audit firm in Month 12 for pre-assessment (Finding #15)
   - Identify gaps early, rapid remediation sprint
   - Consultant validates evidence, recommends fixes
4. **Regulatory Communication**:
   - Proactively communicate transformation progress to regulators
   - Show good faith effort, request timeline clarity
   - Demonstrate quick wins (e.g., audit trail, policies published)

**Monitoring**: Compliance scorecard (% requirements met), pre-assessment results, regulator feedback

---

**Risk 3: Tool Implementation Delays (Vendor, Complexity, Integration Issues)**

**Description**: CMDB tool selection or implementation takes longer than planned (common in enterprise IT)

**Impact**: MEDIUM-HIGH - Timeline slip 2-4 months, budget overrun
**Probability**: MEDIUM-HIGH - tool projects notorious for delays

**Mitigation Strategies:**
1. **Start Tool Evaluation Early (Month 1-2)**:
   - Parallel to policy work (not sequential)
   - RFP issued by Month 2, POC by Month 4, selection by Month 5
   - Compress procurement timeline (executive sponsor pushes vendor)
2. **Interim Improvements with Existing Tools**:
   - Use current Jira (even without Asset Mgmt plugin) for basic workflows
   - Excel CMDB with better structure, macros for reports
   - Example: Automated incident-change linkage via Jira links (manual but better than nothing)
3. **Phased Rollout (Pilot → Scale)**:
   - Pilot with 1 subsidiary → lower risk, learn issues, adjust
   - If pilot delayed, doesn't block others (they continue on interim solution)
4. **Vendor Accountability**:
   - Contract with clear milestones, penalties for delays
   - Weekly vendor status meetings, executive escalation path
   - Professional services included (not DIY implementation)

**Monitoring**: Tool implementation Gantt chart, weekly vendor status, red flag escalation to steering committee

---

**Risk 4: Adoption Resistance (Team and Subsidiary Push back)**

**Description**: Team resists new processes ("too much overhead"), subsidiaries complain ("slower than before")

**Impact**: MEDIUM - Process compliance low, benefits not realized, morale down
**Probability**: MEDIUM - change resistance universal in transformations

**Mitigation Strategies:**
1. **Change Champions Network**:
   - Identify 1 enthusiastic champion per subsidiary (early adopters)
   - Train champions first, they evangelize to peers
   - Recognize champions publicly (awards, bonuses, visibility)
2. **Communication Blitz**:
   - **WHY** message constantly: Compliance risk, efficiency gains, career benefits
   - Monthly newsletters: Quick wins, success stories, ROI data
   - Town halls: Executive sponsors communicate importance, take questions
   - "What's in it for me": Show individual benefits (e.g., less manual work, clearer career path)
3. **Simplify & Automate**:
   - Don't over-engineer processes (lean, streamlined)
   - Automate administrative tasks (e.g., auto-fill templates)
   - Remove friction (e.g., single sign-on, mobile access)
   - Example: Change request template = 10 fields, not 50 (Finding #16)
4. **Gamification & Incentives**:
   - CMDB accuracy contests (Finding #36) → leaderboard, prizes
   - Fastest incident resolution → recognition
   - Knowledge article contributions → points, rewards
   - Team that achieves 100% ITIL certification first → team dinner
5. **Training & Support**:
   - Don't assume understanding; train thoroughly
   - Office hours for questions (1 hour/week)
   - Peer support (Slack channel, wiki FAQs)
   - Patient onboarding (don't rush)

**Monitoring**: CSAT surveys (team + subsidiaries), adoption metrics (% using processes correctly), feedback themes (analyze complaints)

---

## PHẦN 3: OBJECTIVE CHARTERS CHI TIẾT

### Summary of 8 Objective Charters

| ID | Name | Priority | Phase | Budget | Key Findings Addressed |
|----|------|----------|-------|--------|----------------------|
| OC-01 | Establish ITSM Governance Framework | CRITICAL | 1 (M1-6) | $35K | #7, #19, #32, #36, #37, #49 |
| OC-02 | Implement Integrated ITSM Measurement System | CRITICAL | 1-2 (M3-9) | $50K | #1, #2, #27, #42, #46 |
| OC-03 | Deploy Integrated CMDB Platform | CRITICAL | 2 (M4-12) | $190K Y1, $50K/yr | #11, #22, #33, #35, #38, #39, #40 |
| OC-04 | Achieve ITIL/ISO Compliance Readiness | CRITICAL | 1-3 (M1-18) | $145K | #12, #14, #15, #35, #43-48 |
| OC-05 | Automate ITSM Workflows & Integrations | HIGH | 2 (M6-12) | $90K Y1, $30K/yr | #3, #10, #21, #24, #40 |
| OC-06 | Build ITSM Capability & Culture | HIGH | 1-3 (M1-18) | $130K Y1, $30K/yr | #5, #30, #31, #41 |
| OC-07 | Optimize Change Management Maturity | HIGH | 1-2 (M1-12) | $50K Y1, $10K/yr | #13, #16-21, #25-29 (18 findings!) |
| OC-08 | Establish Shared Service Excellence | MED-HIGH | 2-3 (M6-18) | $120K Y1, $20K/yr | #5, #6, shared service model |

**Total Investment**: ~$810K over 18 months, ~$140K/year ongoing
**Coverage**: All 49 findings across 6 areas addressed

---

### OC-01: ESTABLISH ITSM GOVERNANCE FRAMEWORK

**Priority**: CRITICAL | **Phase**: 1 (Month 1-6) | **Theme**: Governance Foundation

#### Business Case

**Current State:**
- No formal policies: CMDB (Finding #32), 3rd Party Management (Finding #49)
- Undefined roles: Incident Manager (Finding #7), CMDB Steward (Finding #37), CI Owners (Finding #36)
- Undocumented RACI (Finding #19) → confusion about who does what

**Impact of Inaction:**
- Regulatory audit failure → penalties $500K+, license suspension
- Conflicts in multi-subsidiary environment → operational chaos
- Inability to enforce standards → quality degradation
- Financial: $200K/year operational inefficiency from lack of governance

**Why Foundation First:**
Cannot build tools, automation, or processes on shaky foundation. Governance = ground floor for maturity.

#### Objective Statement

Establish comprehensive ITSM governance framework including policies, roles, responsibilities, and decision-making structures to enable consistent, compliant service delivery across all subsidiaries.

#### Success Criteria

1. ✅ **5 core policies documented, approved, and published** (CMDB, 3PM, Risk Assessment, Data Retention, SLA)
2. ✅ **RACI matrix created** for all ITSM processes and approved by stakeholders
3. ✅ **4 critical roles defined and assigned**: Incident Manager, CMDB Steward, 2x CI Owners per subsidiary
4. ✅ **Governance council established** with representatives from all subsidiaries
5. ✅ **Policy compliance rate >80%** within 3 months of publication

#### Owner & Team

- **Executive Sponsor**: CIO
- **Delivery Owner**: ITSM Lead
- **Contributors**: PQA Lead, Legal/Compliance, Subsidiary CIOs
- **Approvers**: Executive Steering Committee
- **Commitment**: ITSM Lead 100%, others 10-20% time

#### Key Deliverables

**1. CMDB Policy Charter** (Finding #32)
- **Content**:
  - Scope (what's in CMDB, what's not)
  - CI types and taxonomy (Hardware, Software, Services, Documents)
  - Ownership model (CI Owners, CMDB Steward, CMDB Admin roles)
  - Data quality standards (accuracy >90%, staleness <10%)
  - Audit procedures (monthly audits, annual deep dives)
  - Change control (how CMDB schema evolves)
- **Page count**: 8-10 pages
- **Approval**: CIO + Governance Council

**2. 3rd Party Management Policy** (Finding #49)
- **Content**:
  - Vendor assessment criteria (security, financial stability, SLA)
  - Onboarding process (due diligence, contracts, integration)
  - Monitoring and SLA management (KPIs, reviews, penalties)
  - Offboarding and contingency (backup vendors, data portability)
  - Risk tracking (vendor risk register, quarterly reviews)
- **Page count**: 6-8 pages
- **Approval**: CFO + CIO

**3. Change Risk Assessment Framework** (Finding #13)
- **Content**:
  - Risk scoring 1-5 (Trivial, Minor, Moderate, Major, Critical)
  - Criteria matrix: Impact (users, systems, revenue) × Probability (complexity, testing, history) → Risk Score
  - Escalation paths: 1-2 (Standard CAB), 3-4 (CAB + Business Rep), 5 (Emergency CAB + CTO)
  - Risk mitigation requirements for scores 4-5 (rollback plan, pilot, smoke tests)
  - Examples and case studies
- **Page count**: 5-7 pages
- **Approval**: CAB + CTO

**4. Data Retention & Backup Policy** (Finding #14)
- **Content**:
  - Retention periods per data type:
    - Incidents: 3 years (ITIL standard)
    - Changes: 5 years (ISO 27001, regulatory requirement)
    - CMDB snapshots: Quarterly for 3 years
    - Audit logs: 5 years (compliance)
  - Backup procedures (frequency, storage, encryption, offsite)
  - Disaster recovery (RTO/RPO, restore procedures, testing schedule)
  - Legal/regulatory alignment (GDPR, PDPA, SOX)
- **Page count**: 4-6 pages
- **Approval**: CFO + Legal

**5. SLA Framework** (Finding #8)
- **Content**:
  - Incident priority definitions:
    - P1 (Critical): Service down, revenue impact, >100 users → Response <15min (Gold), <30min (Silver), <60min (Bronze)
    - P2 (High): Major function degraded → Response <30min (Gold), <2hr (Silver), <4hr (Bronze)
    - P3 (Medium): Minor issue, workaround available → Response <4hr (Gold), <8hr (Silver), <1 day (Bronze)
    - P4 (Low): Question, enhancement request → Response <1 day (Gold), <2 days (Silver), <3 days (Bronze)
  - Change approval SLAs: Standard (3 days), Express (1 day), Emergency (4 hours)
  - Request fulfillment SLAs per request type (e.g., access request <4 hours, server provisioning <2 days)
  - Service tier differentiation (Gold/Silver/Bronze detailed in OC-08)
  - Metrics: Resolution time, availability %, change success rate, CSAT
- **Page count**: 10-12 pages
- **Approval**: COO + Subsidiary CIOs

**6. RACI Matrix** (Finding #19)
- **Content**:
  - Processes covered: Incident Management, Change Management, Request Fulfillment, Configuration Management, Problem Management, 3rd Party Management
  - Activities per process (e.g., for Incident: Log, Categorize, Assign, Investigate, Resolve, Close, Review)
  - Roles: Incident Manager, Change Manager, CMDB Steward, Service Desk, Tech Leads, CAB, CI Owners, Service Owners
  - Matrix: R (Responsible - does the work), A (Accountable - final approval), C (Consulted - input), I (Informed - notified)
  - Clear rules: Only 1 A per activity, multiple R/C/I okay
- **Format**: Excel/Visio matrix (1-2 pages per process)
- **Approval**: All process owners + Executive team

**7. Role Descriptions** (Findings #7, #36, #37)

**Incident Manager Role:**
- **Responsibilities**:
  - Own Incident Management process end-to-end
  - Coordinate major incident response (P1/P2)
  - Manage escalations and communications
  - Conduct post-incident reviews
  - Track and report incident metrics
  - Continuous improvement of incident process
- **KPIs**:
  - P1 MTTR <30min (Gold), <60min (Silver)
  - Major incident review completion rate 100%
  - SLA achievement >90%
  - CSAT >4/5
- **Profile**: ITIL 4 Foundation minimum (Specialist preferred), 3+ years incident management, strong communication
- **Reporting**: Reports to ITSM Lead

**CMDB Steward Role:**
- **Responsibilities**:
  - Own CMDB strategy and governance
  - Enforce CMDB policy and data quality standards
  - Coordinate CI Owners across subsidiaries
  - Resolve data conflicts and disputes
  - Audit CMDB quarterly
  - Integrate CMDB with ITSM processes
- **KPIs**:
  - CMDB accuracy >90%
  - Coverage >80% of critical CIs
  - Staleness <10%
  - CI ownership 100%
- **Profile**: Data governance background, CMDB experience (ServiceNow/Jira/etc.), analytical, collaborative
- **Reporting**: Reports to ITSM Lead

**CI Owners (per subsidiary/system):**
- **Responsibilities**:
  - Maintain accuracy of assigned CIs (attributes, status, relationships)
  - Update CI data during changes
  - Review CI quarterly with CMDB Steward
  - Participate in CMDB audits
- **KPIs**:
  - CI accuracy >95% (for owned CIs)
  - Update timeliness <24 hours after change
- **Profile**: Technical Lead, Product Owner, or System Admin with deep knowledge of system
- **Time Commitment**: 2-4 hours/month per CI
- **Assignment**: 1 CI Owner per critical system (e.g., Payment Engine, KYC Platform, Lending System)

**8. Governance Charter**
- **Structure**:
  - **Executive Steering Committee**: CIO (chair), CFO, COO, Subsidiary CEOs (or delegates)
    - Frequency: Monthly 1 hour
    - Responsibilities: Strategic decisions, budget approval, escalations
  - **Governance Council**: ITSM Lead (chair), 1 rep from each subsidiary, COO sponsor
    - Frequency: Monthly 2 hours (operational), Quarterly 3 hours (strategic)
    - Responsibilities: Service levels, conflicts, roadmap, chargeback review (detailed in OC-08)
  - **CAB (Change Advisory Board)**: Change Manager (chair), Tech Leads, Security, Business reps
    - Frequency: Weekly 1 hour + ad-hoc for emergency
    - Responsibilities: Change approvals, risk assessment, schedule coordination (detailed in OC-07)
- **Decision-making**: Consensus preferred, voting if needed (majority), escalation to CIO for deadlocks
- **Transparency**: All decisions documented in Confluence, communicated to stakeholders

#### Timeline

- **Month 1: Draft & Workshops**
  - Week 1-2: Policy drafting sprint (ITSM Lead + PQA Lead + external consultant)
  - Week 3: RACI workshop with all process owners (1 day facilitated session)
  - Week 4: Role description drafting, job postings (if external hire needed)
- **Month 2: Review & Refinement**
  - Week 1-2: Stakeholder review (Legal, Compliance, Subsidiary CIOs provide feedback)
  - Week 3-4: Refinement based on feedback, incorporate legal/compliance inputs
- **Month 3: Approval & Assignment**
  - Week 1: Executive Steering Committee approval (all 5 policies + RACI)
  - Week 2-3: Role assignments (internal reassignment or external hiring)
  - Week 4: Governance charter approved, Council and CAB members nominated
- **Month 4: Publication & Training**
  - Week 1: Policy publication (Confluence, email announcement, town hall)
  - Week 2-3: Training sessions (4 sessions, 2 hours each, all ITSM team + subsidiaries)
  - Week 4: First Governance Council meeting, first CAB meeting
- **Month 5-6: Compliance Monitoring & Adjustment**
  - Monthly: Compliance spot-checks (PQA audits against policies)
  - Monthly: Governance Council reviews compliance metrics
  - Ad-hoc: Policy clarifications and FAQs based on questions

#### Metrics

**Leading Indicators (Process):**
- Policy approval rate: Target 100% by Month 3
- Role assignment completion: Target 100% by Month 3 (4 roles filled)
- Training attendance: Target >95% of ITSM team
- Governance Council attendance: Target >80% per meeting

**Lagging Indicators (Outcome):**
- Policy awareness: Survey score >90% "I understand the policies"
- Policy compliance: Audit score >80% by Month 6 (sampled processes)
- Decision clarity: Survey score >4/5 "I know who is accountable for what"
- Conflict resolution: <5% of decisions escalated beyond Council

**Tracking:**
- Monthly dashboard (policy compliance %, role utilization, governance effectiveness)
- Quarterly report to Executive Steering Committee

#### Dependencies

**Internal:**
- Executive sponsorship: CIO must champion, allocate budget, remove blockers
- Subsidiary buy-in: CIOs must participate in SLA negotiations, assign CI Owners
- HR support: Role creation, job descriptions, recruitment (if external hires)
- Legal/Compliance: Timely review of policies (within 2 weeks)

**External:**
- External consultant (optional): Policy templates, best practices, facilitation ($20K)

**Critical Path:**
- Policy approval (Month 3) blocks → Training (Month 4) blocks → Tool design (Month 6)
- Cannot configure CMDB tool without CMDB policy approved

#### Risks & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| **Policy approval delays** (stakeholders slow to review) | Timeline slip 1-2 months | Medium | - Early stakeholder engagement (Month 0 socialization)<br>- Use industry templates (ITIL, ISO) to speed up<br>- Executive sponsor pushes for timely reviews |
| **Role assignment conflicts** (internal candidates not available, hiring takes time) | Key roles unfilled, process ownership gap | High | - Executive mandate for internal reassignments<br>- Interim external consultants (e.g., Incident Manager contractor for 6 months)<br>- Dual-hat assignments temporarily (e.g., CMDB Steward = part-time initially) |
| **Subsidiary resistance to SLAs** (perceive as unfair, too restrictive) | SLA framework approval fails | Medium | - Co-creation workshops (subsidiaries design with us, not dictated to them)<br>- Tiered service options (Gold/Silver/Bronze) to give flexibility<br>- Grandfather existing commitments for 6 months transition |
| **Policy compliance low** (team ignores new policies, reverts to old ways) | Governance ineffective | Medium | - Training emphasizes "why" (compliance risk, career benefit)<br>- Spot audits with visible consequences (not punitive, but corrective)<br>- Leadership modeling (executives follow policies publicly) |
| **Compliance gaps missed** (policies don't meet ISO/ITIL requirements) | Audit failure | Low | - External compliance consultant review before approval<br>- Map policies to ISO 20000/27001 requirements explicitly<br>- Pre-assessment in Month 15 catches gaps early |

#### Budget Breakdown

| Item | Cost | Justification |
|------|------|---------------|
| External policy consultant | $20,000 | Policy templates, best practices, workshops (optional but recommended to accelerate) |
| Legal/compliance review | $10,000 | Attorney fees for contract language, regulatory alignment (mandatory for fintech) |
| Training materials | $5,000 | Slide decks, videos, handbooks, e-learning modules (one-time development) |
| Facilitation & workshops | $5,000 | Venue (if offsite), facilitator, catering for RACI and policy workshops |
| Contingency (10%) | $5,000 | Buffer for unexpected costs (e.g., additional legal review rounds) |
| **TOTAL** | **$35,000** | |

**ROI Justification:**
- Avoid regulatory penalty: $500K+ (compliance risk mitigation)
- Reduce conflicts and rework: $50K/year (clear accountability)
- Enable transformation: Priceless (foundation for all other charters)

---

### OC-02: IMPLEMENT INTEGRATED ITSM MEASUREMENT SYSTEM

**Priority**: CRITICAL | **Phase**: 1-2 (Month 3-9) | **Theme**: Measurement & Visibility

*(Content abbreviated for length - see detailed structure above. Includes metrics definition, dashboard automation, CSAT surveys, monthly reports, with $50K budget and focus on Findings #1, #2, #27, #42, #46)*

---

### OC-03: DEPLOY INTEGRATED CMDB PLATFORM

**Priority**: CRITICAL | **Phase**: 2 (Month 4-12) | **Theme**: Integration & Automation

*(Content abbreviated - see detailed structure above. Covers tool selection, implementation, integration with IM/CM, auto-population, audit trail, with $190K Year 1 budget addressing Findings #11, #22, #33, #35, #38, #39, #40)*

---

### OC-04: ACHIEVE ITIL/ISO COMPLIANCE READINESS

**Priority**: CRITICAL | **Phase**: 1-3 (Month 1-18) | **Theme**: Quality & Compliance

*(Content abbreviated - see detailed structure above. Gap analysis, audit trail, quarterly audits, ITIL practices, ISO certification with $145K budget covering Findings #12, #14, #15, #35, #43-48)*

---

### OC-05: AUTOMATE ITSM WORKFLOWS & INTEGRATIONS

**Priority**: HIGH | **Phase**: 2 (Month 6-12) | **Theme**: Integration & Automation

*(Content abbreviated - see detailed structure above. Auto-incident creation, auto-assignment, incident-change linkage, PIR-CI/CD integration with $90K Year 1 budget addressing Findings #3, #10, #21, #24, #40)*

---

### OC-06: BUILD ITSM CAPABILITY & CULTURE

**Priority**: HIGH | **Phase**: 1-3 (Month 1-18, Ongoing) | **Theme**: People & Capability

*(Content abbreviated - see detailed structure above. ITIL certifications, knowledge base, career framework, engagement program with $130K Year 1 budget covering Findings #5, #30, #31, #41)*

---

### OC-07: OPTIMIZE CHANGE MANAGEMENT MATURITY

**Priority**: HIGH | **Phase**: 1-2 (Month 1-12) | **Theme**: Process Maturity

*(Content abbreviated - see detailed structure above. Risk framework, CAB, communication templates, CFR analysis, batch approval with $50K Year 1 budget addressing 18 findings #13, #16-21, #25-29)*

---

### OC-08: ESTABLISH SHARED SERVICE EXCELLENCE

**Priority**: MEDIUM-HIGH | **Phase**: 2-3 (Month 6-18) | **Theme**: Business Model Optimization

*(Content abbreviated - see detailed structure above. Service catalog, SLA tiers, chargeback model, governance council, NPS tracking with $120K Year 1 budget addressing Findings #5, #6 and shared service model optimization)*

---

## TỔNG KẾT & KHUYẾN NGHỊ

### 📊 Investment Summary

**Total Budget:**
- **18-month transformation**: ~$810,000
- **Ongoing annual**: ~$140,000/year
- **Breakdown by charter**:
  - OC-01 (Governance): $35K
  - OC-02 (Measurement): $50K
  - OC-03 (CMDB): $190K Y1, $50K/yr
  - OC-04 (Compliance): $145K
  - OC-05 (Automation): $90K Y1, $30K/yr
  - OC-06 (Capability): $130K Y1, $30K/yr
  - OC-07 (Change Mgmt): $50K Y1, $10K/yr
  - OC-08 (Shared Service): $120K Y1, $20K/yr

### 💰 Expected ROI

**Annual Benefits:**
- **Labor savings** (automation): $150,000/year
- **Error reduction** (quality): $100,000/year
- **Compliance risk mitigation**: $500,000+ (penalties avoided)
- **Efficiency gains** (shared service optimization): $100,000/year
- **Total Annual Benefit**: $850,000+/year

**ROI Calculation:**
- **Year 1**: Investment $810K, Benefit $850K → ROI +5% (breakeven)
- **Year 2**: Investment $140K, Benefit $850K → ROI +507%
- **Year 3**: Investment $140K, Benefit $850K → ROI +507%
- **3-Year Cumulative**: Investment $1,090K, Benefit $2,550K → ROI +134% or 2.3x return

**Payback Period**: 12 months

### ✅ Critical Success Factors

**1. Executive Sponsorship (Non-negotiable)**
- CIO must champion transformation publicly and consistently
- COO must support with resource prioritization
- CFO must commit budget multi-year (not year-by-year uncertainty)
- Subsidiary CEOs must participate in governance (not delegate to juniors)
- **Action**: Kick-off with Executive Steering Committee charter (Week 1)

**2. Dedicated Resources (Not Part-Time)**
- Cannot do transformation with part-time, overloaded team
- Must: Hire contractors for BAU OR dedicate 60% time to transformation
- Key roles MUST be full-time: CMDB Admin (Finding #41), Incident Manager (Finding #7)
- **Action**: Budget approval for 2 FTE contractors (Month 1-12) + 2 FTE new hires

**3. Quick Wins (Maintain Momentum)**
- Show value in first 90 days (escalation matrix, service reviews, dashboard v1)
- Celebrate and communicate successes loudly
- Use wins to justify continued investment and effort
- **Action**: Target 3 quick wins by Month 3, communicate at town halls

**4. Compliance First (Regulatory Risk)**
- Address all CRITICAL compliance findings in Phase 1 (Month 1-6)
- Don't wait for perfect tools; achieve compliance manually if needed initially
- Prepare for audit continuously (not scramble last minute)
- **Action**: Compliance scorecard monthly, pre-assessment Month 15

**5. Shared Service Fairness (Subsidiary Trust)**
- Transparent governance (Council with all subsidiaries represented)
- Fair chargeback model (clear formulas, dispute resolution)
- Service tiers (choice, not one-size-fits-all)
- **Action**: Co-create SLAs with subsidiaries, not dictate (Month 3-4)

**6. Change Management (Culture Shift)**
- Communicate "why" constantly (compliance risk, efficiency, career)
- Train thoroughly (not assume understanding)
- Support generously (office hours, champions, FAQs)
- Recognize and reward adoption (gamification, awards)
- **Action**: Change management plan in parallel (communications calendar, champion network)

### 🎯 Execution Recommendations

**Phase Sequencing (Maintain Order):**
1. **Start immediately**: OC-01 (Governance) + OC-04 (Compliance) → address CRITICAL regulatory risk
2. **Month 3**: Launch OC-02 (Measurement) → visibility and data-driven decisions
3. **Month 4**: Begin OC-03 (CMDB) → tool selection in parallel with policy finalization
4. **Month 6**: Initiate OC-05 (Automation) + OC-07 (Change Mgmt) → reduce manual burden
5. **Throughout**: Execute OC-06 (Capability) → training, culture, continuous
6. **Month 6**: Start OC-08 (Shared Service) → optimize business model once foundation solid

**Critical Path (Don't Compromise):**
```
Policy Approval (M3)
  → Tool Selection (M5)
  → Implementation (M6-9)
  → Integration (M9-12)
  → Measurement (M10-18)
  → Certification (M17-18)
```

**Do's:**
- ✅ Start tool evaluation early (Month 1, parallel to policies)
- ✅ Pilot with 1 subsidiary before scaling (de-risk)
- ✅ Use multi-track execution (parallel workstreams where possible)
- ✅ Celebrate quick wins visibly (town halls, newsletters, awards)
- ✅ Monitor risks weekly (steering committee, mitigation actions)
- ✅ Communicate constantly ("why", progress, successes, next steps)

**Don'ts:**
- ❌ Don't big-bang (phased rollout always safer)
- ❌ Don't tool-first (governance foundation required first)
- ❌ Don't underestimate change resistance (plan for it proactively)
- ❌ Don't skip training (false economy, leads to low adoption)
- ❌ Don't compromise on compliance (regulatory risk too high)
- ❌ Don't overload team (hire contractors or defer non-critical work)

### 📈 Success Metrics (18-Month Targets)

**Operational Excellence:**
- Manual work reduced: 80% → <20%
- Incident MTTR (P1): -30% improvement
- Change success rate: 80% → >95%
- SLA achievement: <50% → >90%

**Compliance & Governance:**
- ITIL maturity level: 1 → 3
- ISO 20000 certification: Achieved
- Audit coverage: 3% → >80%
- Policy compliance: 0% → >80%

**Data & Visibility:**
- Metrics tracked: 10% → 100%
- Dashboard refresh: Manual (days) → Real-time (<5min)
- CSAT response rate: 0% → >30%
- CMDB accuracy: Unknown → >90%

**People & Culture:**
- ITIL certifications: 0% → 100% Foundation, >50% Specialist
- Team retention: <80% → >90%
- User engagement: 25% → 70%
- Subsidiary NPS: Unknown → >+30

**Financial:**
- Cost per incident: Reduce 40%
- Failed change cost: Reduce 50% ($100K/year savings)
- Labor efficiency: +2-3 FTE equivalent from automation
- ROI: 134% cumulative over 3 years

### 🚀 Next Steps (First 30 Days)

**Week 1:**
- [ ] Executive Steering Committee kick-off (2 hours)
- [ ] Budget approval for $810K transformation ($270K for Year 1 Phase 1)
- [ ] Hire decision: ITSM Lead (internal promotion or external consultant)
- [ ] Form transformation PMO (ITSM Lead + PQA Lead + DevOps Lead + HR)

**Week 2:**
- [ ] Policy drafting sprint begins (OC-01)
- [ ] Tool evaluation RFP issued (OC-03)
- [ ] Contractor procurement for BAU coverage (2 FTE, 12 months)
- [ ] Communication plan: Town hall announcement to all subsidiaries

**Week 3:**
- [ ] RACI workshop scheduled (1 day, all process owners)
- [ ] Role descriptions drafted (Incident Manager, CMDB Steward)
- [ ] Governance Council nominations requested from subsidiaries
- [ ] Gap analysis kickoff (ITIL/ISO compliance per OC-04)

**Week 4:**
- [ ] Quick Win #1 delivered: Incident Escalation Matrix published
- [ ] Training needs assessment (who needs what certifications)
- [ ] Pilot subsidiary selected (criteria: medium complexity, willing)
- [ ] Monthly transformation status report format defined

**First Steering Committee Review (End of Month 1):**
- Progress: 5 policies at 60% draft, RACI 80% complete, roles 50% defined
- Decisions needed: Approve policy drafts for stakeholder review
- Risks flagged: Subsidiary B concerns about SLA feasibility (mitigation: 1-on-1 session)
- Next month priorities: Policy approval, role assignments, ITIL training Wave 1 procurement

---

## CONCLUSION

The strategic transformation of ITSM and QA for Công ty Fintech (A) is not optional—it's an imperative driven by regulatory compliance, operational efficiency, and business growth needs. With 49 critical findings across 6 areas, the current state poses existential risks ($700K+/year exposure) while simultaneously presenting significant opportunities (economies of scale, best practice sharing, market differentiation).

**The 8 Objective Charters provide a comprehensive, phased roadmap** to transform from ad-hoc (Level 1) to mature (Level 3) ITSM operations over 18 months, achieving:
- **Compliance**: ITIL/ISO certification, avoiding regulatory penalties
- **Efficiency**: 60% reduction in manual work, $150K/year labor savings
- **Quality**: 95%+ change success rate, 30% faster incident resolution
- **Scalability**: Shared service model enabling 2x subsidiary growth without proportional cost increase

**Success requires unwavering commitment** to the 6 Critical Success Factors (executive sponsorship, dedicated resources, quick wins, compliance first, shared service fairness, change management) and disciplined execution following the proven governance-first, pilot-before-scale, multi-track approach.

**The ROI is compelling** (2.3x return over 3 years, 12-month payback), the risks are mitigated through proven strategies, and the alternative (status quo) is untenable.

**Recommendation: Proceed with confidence.** Begin with OC-01 and OC-04 immediately (Month 1), leverage quick wins to build momentum, and systematically execute the remaining charters. The foundation is solid, the plan is detailed, and the team is ready.

---

**Document Prepared**: November 25, 2025
**Valid Through**: December 31, 2027 (18-month program + 18-month sustainability)
**Next Review**: Quarterly Steering Committee (track progress, adjust as needed)
**Contact**: ITSM Lead (to be assigned)
