# Hướng Dẫn Chi Tiết Lập OC (Organization Change)

## 📋 Overview - OC Document Structure

OC (Organization Change) document là backbone của mọi change initiative trong IPAM Framework. Đây là blueprint chi tiết để manage toàn bộ quá trình thay đổi.

---

## 🎯 PHẦN 1: OC HEADER - Thông Tin Cơ Bản

### 1.1 OC Identification
```
OC Code: [Mã định danh unique, VD: OC-2025-CX-001]
OC Title: [Tên ngắn gọn, clear, VD: "Improve Customer Onboarding Experience"]
OC Owner: [Tên người chịu trách nhiệm chính]
Department/Team: [Phòng ban/team thực hiện]
Creation Date: [Ngày tạo OC]
Target Go-Live: [Ngày dự kiến hoàn thành]
Status: [Draft / Planning / In Progress / Completed / On Hold]
```

### 1.2 Executive Summary (1-2 paragraphs)
- **What**: Thay đổi gì?
- **Why**: Tại sao cần thay đổi?
- **Impact**: Ảnh hưởng đến ai/cái gì?
- **Timeline**: Khi nào hoàn thành?

**Example:**
```
This OC aims to reduce customer onboarding time from 7 days to 3 days
by automating document verification and implementing self-service portal.
This will impact 5,000+ new customers monthly and reduce operational cost
by 30%. Expected completion: Q2 2025.
```

---

## 🔍 PHẦN 2: IDENTIFY PHASE (5I Framework)

### 2.1 Intention - Mục Đích Thay Đổi

**A. Change Vision**
```
Vision Statement: [1-2 câu mô tả future state lý tưởng]
VD: "Every new customer completes onboarding effortlessly within 24 hours"

Business Objective: [Link đến strategic goal của company]
- Increase customer satisfaction score from 7.2 to 8.5
- Reduce customer acquisition cost by 25%
- Improve NPS from 40 to 55
```

**B. Change Drivers (Tại sao thay đổi NGAY BÂY GIỜ?)**
- [ ] Customer complaints/feedback
- [ ] Competitive pressure
- [ ] Regulatory requirement
- [ ] Technology advancement
- [ ] Cost optimization
- [ ] Growth enablement

**C. Success Definition**
```
Success looks like:
1. [Metric 1]: 80% customers complete onboarding in <24h
2. [Metric 2]: Customer satisfaction score >8.0
3. [Metric 3]: Zero manual document verification errors
4. [Metric 4]: 50% reduction in support tickets during onboarding
```

### 2.2 Interconnect (Interbeing) - Stakeholder & System Analysis

**A. Stakeholder Matrix**

| Stakeholder Group | Role | Impact Level | Influence | Engagement Strategy |
|-------------------|------|--------------|-----------|---------------------|
| New Customers | End user | High | Low | User testing, surveys |
| Customer Service Team | Operator | High | Medium | Training, feedback loop |
| IT Department | Implementer | Medium | High | Weekly sync, requirements |
| Compliance Team | Approver | High | High | Review sessions |
| Marketing Team | Promoter | Low | Medium | Communication plan |

**B. System Dependencies**
```
Upstream Systems (Provide input):
- CRM System → Customer data
- Document Management → ID verification
- Payment Gateway → Payment processing

Downstream Systems (Receive output):
- Customer Portal → Onboarding status
- Analytics Platform → Metrics tracking
- Support Ticketing → Issue management

Integration Points:
1. API: CRM ↔ Onboarding Platform
2. Webhook: Document Verification → Status Update
3. Batch: Nightly sync with Analytics
```

**C. Change Ripple Analysis**
```
Direct Impact:
- Customer Service: New process, new tools
- IT: System development & maintenance
- Compliance: New approval workflows

Indirect Impact:
- Finance: Revenue recognition timing changes
- Product: Feature prioritization shift
- Sales: Onboarding promise in sales pitch
```

### 2.3 Insight - Data & Analysis

**A. Current State Assessment**
```
Current Process:
1. Customer submits paper forms (Day 0)
2. Manual data entry (Day 1-2)
3. Document verification (Day 3-5)
4. Manual approval (Day 6)
5. Account activation (Day 7)

Pain Points:
- 70% customers complain about slow process
- 30% error rate in manual data entry
- 25% documents require resubmission
- 5 FTE dedicated to manual processing

Current Metrics (Baseline):
- Average onboarding time: 7 days
- Customer satisfaction: 7.2/10
- Cost per onboarding: $45
- Manual processing time: 3.5 hours per customer
```

**B. Root Cause Analysis (5 Whys)**
```
Problem: Onboarding takes 7 days

Why? → Manual document verification is slow
Why? → Staff must manually check each document
Why? → No automated verification system
Why? → Previous automation project failed
Why? → Lack of clear requirements & poor vendor selection

Root Cause: Inadequate planning & execution of previous automation effort
```

**C. Benchmarking**
```
Industry Best Practice:
- Top quartile: 1-2 days onboarding
- Automation rate: 85%+
- Customer satisfaction: 8.5+

Competitor Analysis:
- Competitor A: 2-day onboarding, AI-powered verification
- Competitor B: 1-day onboarding, mobile-first experience
- Competitor C: 3-day onboarding, white-glove service
```

### 2.4 Innovation - Solution Design

**A. Solution Options Analysis**

| Option | Pros | Cons | Cost | Timeline | Risk |
|--------|------|------|------|----------|------|
| Build in-house | Full control, customization | High cost, long time | $500K | 9 months | High |
| Buy SaaS platform | Fast, proven | Vendor dependency | $120K/yr | 3 months | Medium |
| Hybrid (Buy + Customize) | Balance speed & flexibility | Integration complexity | $250K | 5 months | Low |

**Recommended Solution: Hybrid Approach**

**B. Solution Architecture**
```
Customer Journey:
1. Online form (5 min) → Auto-save, validation
2. Document upload (3 min) → OCR + AI verification
3. Identity check (instant) → 3rd party API
4. Auto-approval (instant) → Rule engine
5. Welcome email (instant) → Triggered automation

Technology Stack:
- Frontend: React + Mobile app
- Backend: Node.js microservices
- AI/ML: Document OCR (AWS Textract)
- Identity: IDnow API integration
- Database: PostgreSQL + Redis cache
```

**C. Innovation Elements**
- AI-powered document verification (99% accuracy)
- Real-time status updates via mobile app
- Chatbot for instant support during onboarding
- Predictive analytics to prevent drop-offs

### 2.5 Integrity - Ethics & Alignment

**A. Values Alignment Check**
```
Company Value: Customer First
→ Solution: Prioritizes customer convenience & speed ✓

Company Value: Data Security
→ Solution: End-to-end encryption, compliance with GDPR ✓

Company Value: Employee Empowerment
→ Solution: Frees staff from manual work for higher-value tasks ✓
```

**B. Ethical Considerations**
- [ ] Data privacy: Ensure GDPR/local law compliance
- [ ] Accessibility: Support for disabled users (WCAG 2.1 AA)
- [ ] Fairness: No algorithmic bias in verification
- [ ] Transparency: Clear communication about data usage
- [ ] Security: Penetration testing, secure storage

**C. Risk & Compliance**
```
Regulatory Requirements:
- KYC (Know Your Customer) compliance
- AML (Anti-Money Laundering) checks
- Data protection regulations

Risk Mitigation:
- Legal review of new process
- Compliance sign-off before go-live
- Audit trail for all decisions
```

---

## 📝 PHẦN 3: PLAN PHASE (5P Framework) - OTOOB

### 3.1 Purpose - Define Clear Objectives

**A. SMART Objectives**
```
1. Reduce average onboarding time from 7 days to 3 days by Q2 2025
2. Achieve 85% customer satisfaction score by Q3 2025
3. Decrease cost per onboarding from $45 to $20 by Q4 2025
4. Automate 80% of verification tasks by Q2 2025
5. Reduce onboarding-related support tickets by 60% by Q3 2025
```

**B. OTOOB Framework**

| Element | Details |
|---------|---------|
| **OC Owner** | John Smith (VP Customer Experience) |
| **Timeframe** | Jan 2025 - Jun 2025 (6 months) |
| **One Team** | 12 people: 3 PM, 4 Dev, 2 QA, 2 Customer Service, 1 Compliance |
| **Outputs** | Automated onboarding platform, mobile app, training materials |
| **Biz Impact** | $500K annual savings, 20% increase in customer acquisition |

### 3.2 Pathway - Roadmap & Milestones

**A. Phase Breakdown**

```
PHASE 1: Foundation (Jan - Feb 2025)
Milestones:
□ Requirements finalized (Week 2)
□ Vendor selected (Week 4)
□ Architecture approved (Week 6)
□ Team onboarded (Week 8)

PHASE 2: OMVP Development (Mar - Apr 2025)
Milestones:
□ Core onboarding flow (Week 12)
□ Document verification integration (Week 14)
□ Customer portal beta (Week 16)
□ Internal testing complete (Week 18)

PHASE 3: Pilot Launch (May 2025)
Milestones:
□ Soft launch to 10% users (Week 20)
□ Feedback collection & fixes (Week 22)
□ Compliance audit passed (Week 24)

PHASE 4: Full Rollout (Jun 2025)
Milestones:
□ 50% traffic (Week 26)
□ 100% traffic (Week 28)
□ Old system decommissioned (Week 30)
```

**B. Dependency Map**
```
Critical Path:
Requirements → Architecture → Development → Testing → Pilot → Rollout

Dependencies:
- Compliance approval BEFORE pilot launch
- IT infrastructure BEFORE development starts
- Training materials BEFORE pilot launch
- Marketing assets BEFORE full rollout

Risks:
- Vendor delay: Mitigation = backup vendor shortlist
- Integration issues: Mitigation = early POC with test data
- User adoption: Mitigation = change management plan
```

### 3.3 Perspective - Stakeholder Management

**A. Communication Plan**

| Stakeholder | Frequency | Channel | Content | Owner |
|-------------|-----------|---------|---------|-------|
| Customers | Weekly | Email/Portal | Progress updates | Marketing |
| Customer Service | Daily | Slack | Status & issues | Product Manager |
| Leadership | Bi-weekly | Presentation | Metrics & risks | OC Owner |
| IT Team | Daily | Standup | Technical sync | Tech Lead |
| Compliance | Monthly | Meeting | Audit & compliance | Legal |

**B. Change Impact Assessment**

| Group | Change Type | Impact Level | Resistance Risk | Mitigation |
|-------|-------------|--------------|-----------------|------------|
| Customers | Process change | Medium | Low | Clear communication, support |
| Customer Service | Tool & process | High | Medium | Extensive training, champions |
| IT | New system to maintain | Medium | Low | Technical documentation |
| Compliance | New approval workflow | Medium | Medium | Early involvement, co-design |

**C. Resistance Management**
```
Anticipated Resistance:
1. "Current process works fine"
   → Show data on customer complaints & competitor advantage

2. "Too complex to learn new system"
   → Provide hands-on training, user-friendly design

3. "Job security concerns"
   → Communicate upskilling opportunities, no layoffs

4. "Not enough time to change"
   → Phase rollout, provide adequate preparation time
```

### 3.4 Priorities - Resource Allocation

**A. Priority Matrix**

| Initiative | Impact | Effort | Priority | Sequence |
|------------|--------|--------|----------|----------|
| Core onboarding flow | High | High | P1 | Phase 2.1 |
| Document verification | High | Medium | P1 | Phase 2.2 |
| Mobile app | Medium | High | P2 | Phase 3.1 |
| Chatbot support | Low | Medium | P3 | Phase 4.1 |
| Analytics dashboard | Medium | Low | P2 | Phase 3.2 |

**B. Resource Plan**

```
Team Allocation:
- Product Manager (100%): 1 Senior PM
- Development (80%): 4 developers (2 frontend, 2 backend)
- QA (60%): 2 QA engineers
- Customer Service (20%): 2 representatives (feedback & training)
- Compliance (15%): 1 compliance officer

Budget Breakdown:
- Software licenses: $50K
- Development cost: $180K (labor)
- Vendor services: $80K
- Training: $20K
- Marketing: $15K
- Contingency (15%): $50K
Total: $395K
```

**C. Quick Wins (First 30 days)**
```
1. Digital form instead of paper (Week 2)
   → Immediate UX improvement, low effort

2. Email status updates (Week 3)
   → Reduces "where is my application" calls

3. FAQ chatbot (Week 4)
   → 24/7 support, reduces ticket volume
```

### 3.5 Performance - Measurement Framework

**A. KPI Dashboard**

| KPI Category | Metric | Baseline | Target | Measurement |
|--------------|--------|----------|--------|-------------|
| **Speed** | Avg onboarding time | 7 days | 3 days | Daily |
| **Quality** | Error rate | 30% | <5% | Weekly |
| **Satisfaction** | CSAT score | 7.2 | 8.5 | After each onboarding |
| **Efficiency** | Cost per onboarding | $45 | $20 | Monthly |
| **Adoption** | Automation rate | 0% | 80% | Weekly |
| **Support** | Tickets volume | 500/mo | 200/mo | Weekly |

**B. Leading vs Lagging Indicators**

```
Leading Indicators (Predictive):
- System uptime %
- Form completion rate
- Document upload success rate
- User drop-off points
- API response time

Lagging Indicators (Results):
- Average onboarding time
- Customer satisfaction score
- Cost per onboarding
- Revenue impact
- NPS change
```

**C. Reporting Cadence**
```
Daily: Operational metrics (system health, errors)
Weekly: Team standup (progress, blockers)
Bi-weekly: Steering committee (KPIs, risks)
Monthly: Leadership review (ROI, strategic alignment)
Quarterly: Board update (business impact)
```

---

## ✅ PHẦN 4: ACCOUNTABILITY PHASE (5A Framework) - OMVP

### 4.1 Align - Goal Alignment

**A. Alignment Workshop Agenda**
```
Session 1: Vision Alignment (2 hours)
- Review OC objectives
- Q&A on strategy
- Concerns & clarifications
- Commitment from all stakeholders

Session 2: Goal Cascading (2 hours)
- Break down OC goals to team/individual level
- Define success for each role
- Identify interdependencies
```

**B. Goal Cascade Example**
```
OC Goal: Reduce onboarding time to 3 days

↓ Product Team Goal:
  Deliver automated verification by Week 12

  ↓ Frontend Dev Goal:
    Build upload interface by Week 10

  ↓ Backend Dev Goal:
    Integrate OCR API by Week 11

  ↓ QA Goal:
    Test 50 document types by Week 12
```

### 4.2 Assign - RACI Matrix

**A. RACI for Key Deliverables**

| Deliverable | OC Owner | Product | Dev | QA | Compliance | Customer Service |
|-------------|----------|---------|-----|----|-----------:|------------------|
| Requirements | A | R | C | C | C | I |
| Architecture | A | R | R | C | C | I |
| Development | A | A | R | C | I | I |
| Testing | A | A | C | R | C | I |
| Compliance Review | A | C | I | I | R | I |
| Training Materials | A | C | C | I | I | R |
| Go-Live Decision | R | A | I | A | A | C |

**Legend:**
- R = Responsible (does the work)
- A = Accountable (final approval)
- C = Consulted (provides input)
- I = Informed (kept in loop)

**B. Role Definitions**
```
OC Owner (John Smith):
- Overall accountability for OC success
- Escalation point for blockers
- Stakeholder management
- Budget & resource decisions

Product Manager (Sarah Lee):
- Requirements & backlog management
- Sprint planning & prioritization
- User acceptance criteria
- Feature delivery

Tech Lead (Mike Chen):
- Technical architecture
- Code quality & standards
- Technical risk management
- Team technical guidance
```

### 4.3 Action - Sprint Execution (OMVP Focus)

**A. OMVP Definition**
```
Objective Minimum Viable Product:
"Enable new customers to complete onboarding online in <24 hours
with automated document verification, achieving 80% satisfaction"

OMVP Scope (Phase 2 - Week 12):
✅ Include:
- Online registration form
- Document upload (ID, proof of address)
- OCR + basic AI verification
- Email status notifications
- Basic customer portal (check status)

❌ Exclude (Post-OMVP):
- Mobile app
- Chatbot support
- Advanced analytics
- Gamification
- Video KYC
```

**B. Sprint Structure (2-week sprints)**

```
SPRINT 1-2 (Week 1-4): Foundation
Sprint Goal: Setup infrastructure & basic flow
Stories:
- Setup dev environment
- Database schema design
- Basic registration form
- User authentication

SPRINT 3-4 (Week 5-8): Core Features
Sprint Goal: Build main onboarding flow
Stories:
- Document upload UI
- OCR integration (AWS Textract)
- Verification rule engine
- Status tracking backend

SPRINT 5-6 (Week 9-12): OMVP Completion
Sprint Goal: Complete end-to-end flow
Stories:
- Customer portal (status check)
- Email notifications
- Error handling
- Security hardening
- OMVP testing & fixes
```

**C. Daily Standup Format**
```
Each team member answers:
1. What did I complete yesterday toward OMVP?
2. What will I do today toward OMVP?
3. Any blockers preventing OMVP progress?

Timebox: 15 minutes
Focus: Remove blockers, maintain OMVP alignment
```

### 4.4 Access - Progress Tracking

**A. Sprint Health Metrics**

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Sprint Velocity | 40 points | 38 points | 🟢 |
| Story Completion | 90% | 85% | 🟡 |
| Bug Count | <10 | 12 | 🟡 |
| Code Coverage | >80% | 76% | 🟡 |
| OMVP Progress | 50% | 48% | 🟢 |

**B. Risk & Issue Log**

| ID | Risk/Issue | Impact | Probability | Mitigation | Owner | Status |
|----|------------|--------|-------------|------------|-------|--------|
| R1 | OCR accuracy <95% | High | Medium | Test multiple vendors | Tech Lead | Open |
| R2 | Compliance delay | High | Low | Early engagement | OC Owner | Mitigated |
| I1 | Dev resource on leave | Medium | - | Hire contractor | Product | Resolved |

**C. Feedback Collection**

```
Sprint Review (Every 2 weeks):
- Demo working features to stakeholders
- Collect feedback on OMVP direction
- Adjust backlog priorities

Retrospective (Every 2 weeks):
- What went well?
- What didn't go well?
- What to improve next sprint?
- Action items (max 3 per retro)
```

### 4.5 Adapt - Continuous Improvement

**A. Feedback Loop**

```
Internal Testing (Week 10-12):
→ Customer Service team tests OMVP
→ Log usability issues
→ Prioritize fixes

Pilot Users (Week 20-24):
→ 500 real customers use OMVP
→ Collect satisfaction scores & feedback
→ A/B test variations
→ Iterate on pain points

Full Rollout (Week 26-28):
→ Monitor metrics daily
→ Weekly review sessions
→ Fast response to issues
```

**B. Pivot Criteria**
```
IF OMVP satisfaction <70% AFTER 2 weeks pilot
THEN pause rollout & conduct user research

IF Technical issues cause >10% transaction failures
THEN rollback & fix

IF Compliance issues discovered
THEN immediate halt until resolved
```

**C. Retrospective Action Items Tracker**

| Sprint | Action Item | Owner | Due Date | Status |
|--------|-------------|-------|----------|--------|
| Sprint 2 | Improve test automation | QA Lead | Week 6 | ✅ Done |
| Sprint 3 | Better API documentation | Backend Dev | Week 8 | 🔄 In Progress |
| Sprint 4 | Reduce code review time | Tech Lead | Week 10 | ⏳ Pending |

---

## 📊 PHẦN 5: MANAGE PHASE (5M Framework)

### 5.1 Map Outputs - Value Stream to OMVP

**A. Output-to-Outcome Mapping**

```
OUTPUT 1: Automated onboarding platform
↓
OUTCOME: Customers complete onboarding in 24h
↓
CUSTOMER VALUE: Fast access to services, less frustration
↓
BUSINESS VALUE: Higher conversion rate, lower CAC

OUTPUT 2: AI document verification
↓
OUTCOME: 95% accuracy, instant verification
↓
CUSTOMER VALUE: No need to resubmit documents
↓
BUSINESS VALUE: Lower operational cost, better compliance

OUTPUT 3: Customer portal
↓
OUTCOME: Real-time status visibility
↓
CUSTOMER VALUE: Peace of mind, self-service
↓
BUSINESS VALUE: Reduced support ticket volume
```

**B. Customer Journey Mapping**

```
BEFORE (Current State):
1. Download PDF form → Print → Fill manually (30 min) 😞
2. Scan documents → Email (15 min) 😞
3. Wait for confirmation email (1-2 days) 😤
4. Receive request for re-submission (3-5 days) 😡
5. Re-submit → Wait again (2 days) 😤
6. Approval notification (7 days total) 😐

AFTER (OMVP Future State):
1. Fill online form → Auto-validation (5 min) 😊
2. Upload docs → Instant OCR check (3 min) 😊
3. AI verification → Real-time status (instant) 😃
4. Auto-approval → Welcome email (instant) 😍
5. Start using service (24 hours total) 🎉
```

### 5.2 Measure - Performance Tracking

**A. KPI Dashboard Design**

```
EXECUTIVE DASHBOARD (Weekly Email):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 Onboarding Performance - Week 28

🎯 Key Wins:
  • Avg Time: 2.8 days (Target: 3 days) ✅
  • CSAT: 8.6/10 (Target: 8.5) ✅
  • Cost: $22/onboarding (Target: $20) 🟡

⚠️ Attention Needed:
  • Support tickets: 180/week (down 40% from baseline)
  • Error rate: 7% (Target: <5%)

📊 Trend: Improving week-over-week
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**B. Data Collection Methods**

| Metric | Source | Collection Method | Frequency |
|--------|--------|-------------------|-----------|
| Onboarding time | Application DB | Automated query | Real-time |
| CSAT | Post-onboarding survey | Email survey (Medallia) | Per transaction |
| Cost | Finance system | Manual calculation | Monthly |
| Error rate | Application logs | Automated monitoring (Datadog) | Real-time |
| Support tickets | Zendesk | API integration | Real-time |

**C. ROI Calculation**

```
INVESTMENT:
- Development: $180K
- Vendor: $80K
- Other: $85K
Total: $395K

ANNUAL SAVINGS:
- Labor cost reduction: $420K (9 FTE → 3 FTE)
- Error cost reduction: $80K
- Support cost reduction: $60K
Total: $560K/year

ROI = (560K - 395K) / 395K = 42% first year
Payback period: 8.5 months
3-year NPV: $1.2M
```

### 5.3 Monitor - Early Warning System

**A. Monitoring Dashboard (Real-time)**

```
TECHNICAL HEALTH:
🟢 System Uptime: 99.8%
🟢 API Response Time: 180ms (avg)
🟡 Error Rate: 2.1% (spike detected)
🟢 Database CPU: 45%

BUSINESS HEALTH:
🟢 Daily Onboardings: 185 (normal)
🟡 Completion Rate: 82% (down from 88%)
🟢 CSAT: 8.4 (stable)
🔴 Drop-off at Document Upload: 15% (unusual)

ALERTS:
⚠️ Alert #1: Document upload failures increased 3x (last hour)
   → Action: DevOps investigating

⚠️ Alert #2: Completion rate dropped below threshold
   → Action: Product team analyzing user journey
```

**B. Alert Configuration**

```
CRITICAL (Immediate escalation to OC Owner):
- System downtime >5 minutes
- Data breach detected
- Compliance violation
- Transaction failure rate >10%

HIGH (Escalate to Tech Lead within 1 hour):
- API response time >1 second
- Error rate >5%
- Drop-off rate >20%

MEDIUM (Team handles, report daily):
- Error rate >2%
- CSAT drops below 8.0
- Support ticket spike
```

**C. Issue Response Playbook**

```
IF Document Verification Fails:
1. Check OCR service status
2. Review recent failed documents
3. Test with sample documents
4. If vendor issue → switch to backup OCR
5. If logic issue → hotfix deployment
6. Communicate to affected customers

IF CSAT Drops Below 8.0:
1. Pull recent feedback comments
2. Identify common themes
3. Prioritize top 3 pain points
4. Create immediate improvement backlog
5. Deploy fixes within 1 week
```

### 5.4 Modify - Strategy Adjustment

**A. Review Cadence**

```
WEEKLY (Tactical):
- Review KPI dashboard
- Address operational issues
- Adjust sprint priorities if needed

MONTHLY (Strategic):
- Review trend analysis
- Assess goal progress
- Adjust resource allocation
- Update risk register

QUARTERLY (Strategic):
- Comprehensive OC review
- ROI validation
- Scope adjustment discussion
- Roadmap refinement for next quarter
```

**B. Modification Decision Framework**

```
SCENARIO 1: Ahead of schedule, under budget
Decision: ✅ Add scope (mobile app from P2 to P1)

SCENARIO 2: Behind schedule, budget OK
Decision: 🔄 Add resources OR reduce scope

SCENARIO 3: On schedule, over budget
Decision: 💰 Seek additional budget OR reduce scope

SCENARIO 4: Customer feedback reveals new pain point
Decision: 🎯 Re-prioritize backlog, address pain point

SCENARIO 5: Regulatory change mid-project
Decision: ⚠️ Pause, assess impact, adjust plan
```

**C. Change Request Process**

```
Change Request Template:
━━━━━━━━━━━━━━━━━━━━━━━━━━
CR-001: Add Biometric Verification

Requestor: Compliance Team
Reason: New regulatory requirement
Impact:
  - Timeline: +3 weeks
  - Budget: +$40K
  - Resources: 1 additional developer
  - Risk: Medium (new technology)

Alternatives Considered:
1. Partner with 3rd party (faster, more expensive)
2. Phase 2 implementation (non-compliant for 6 months)

Recommendation: Approve CR-001, adjust go-live to Week 33

Approvers:
□ OC Owner
□ Product Lead
□ Finance
□ Compliance
━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 5.5 Maintain - Sustainability Plan

**A. Change Embedding Activities**

```
MONTH 1-3 (Stabilization):
- Daily monitoring
- Weekly team check-ins
- Rapid bug fixes
- User support ramp-up

MONTH 4-6 (Optimization):
- Bi-weekly monitoring
- Monthly review
- Feature enhancements based on feedback
- Process documentation

MONTH 7-12 (BAU Transition):
- Monthly monitoring
- Quarterly review
- Continuous improvement backlog
- Handover to BAU team
```

**B. Knowledge Transfer Plan**

```
TO BAU SUPPORT TEAM:
□ Technical documentation (architecture, APIs)
□ User guides (admin, customer)
□ Troubleshooting playbooks
□ Monitoring dashboard training
□ Shadowing sessions (2 weeks)
□ On-call handover

TO CUSTOMER SERVICE TEAM:
□ New process training (2-day workshop)
□ FAQ database
□ Escalation procedures
□ Success stories for customer communication
□ Ongoing coaching (first month)
```

**C. Continuous Improvement Pipeline**

```
FEEDBACK CHANNELS:
- Customer surveys (post-onboarding)
- Support ticket analysis (weekly)
- Internal team retrospectives (bi-weekly)
- Compliance audits (quarterly)
- Industry benchmarking (annually)

IMPROVEMENT BACKLOG (Post-OMVP):
P1: Mobile app (Q3 2025)
P2: Video KYC for high-value customers (Q4 2025)
P3: Gamification to increase completion rate (Q1 2026)
P4: AI chatbot for 24/7 support (Q2 2026)
```

**D. Success Celebration & Recognition**

```
MILESTONE CELEBRATIONS:
✓ OMVP Launch: Team lunch, OC Owner recognition email
✓ Pilot Success: Company all-hands shoutout
✓ Full Rollout: Success story published internally
✓ 6-Month Post-Launch: Case study, team awards

RECOGNITION PLAN:
- Spotlight team members in company newsletter
- Peer recognition awards
- Lessons learned presentation to wider org
- Add to portfolio for future OC references
```

---

## 📑 PHẦN 6: OC DOCUMENT MANAGEMENT

### 6.1 Document Version Control

```
Version History:
v1.0 - 2025-01-15 - Initial draft (IDENTIFY complete)
v1.1 - 2025-02-01 - PLAN phase added
v2.0 - 2025-03-15 - ACCOUNTABILITY phase updated post-OMVP
v2.1 - 2025-05-01 - MANAGE metrics updated post-pilot
v3.0 - 2025-06-30 - Final version post-rollout
```

### 6.2 OC Storage & Access

```
Document Location:
- Master: Confluence/SharePoint
- Backup: Google Drive (OC folder)
- Access: Stakeholders only (RACI matrix defines access level)

Related Documents:
- Business Case: [link]
- Technical Architecture: [link]
- RACI Matrix: [link]
- Risk Register: [link]
- Sprint Backlogs: [Jira board link]
```

### 6.3 OC Review Checkpoints

```
CHECKPOINT 1: IDENTIFY Phase Complete
Approval needed from:
□ OC Owner
□ Business Sponsor
□ Key Stakeholders

CHECKPOINT 2: PLAN Phase Complete (Before ACCOUNTABILITY)
Approval needed from:
□ OC Owner
□ Finance (budget)
□ IT (technical feasibility)
□ Compliance (regulatory)

CHECKPOINT 3: OMVP Ready (Before Pilot)
Approval needed from:
□ OC Owner
□ Product Lead
□ QA (testing sign-off)
□ Compliance (audit passed)

CHECKPOINT 4: Full Rollout Decision
Approval needed from:
□ OC Owner
□ Executive Sponsor
□ Pilot results review
```

---

## 🎯 CHECKLIST: OC Document Completion

### Must-Have Sections ✅

**IDENTIFY Phase:**
- [ ] Intention: Clear vision & business objectives
- [ ] Interconnect: Stakeholder matrix & system dependencies
- [ ] Insight: Current state analysis & root cause
- [ ] Innovation: Solution options & architecture
- [ ] Integrity: Ethics & compliance check

**PLAN Phase:**
- [ ] Purpose: SMART objectives & OTOOB
- [ ] Pathway: Roadmap with milestones & dependencies
- [ ] Perspective: Communication plan & change impact
- [ ] Priorities: Resource allocation & quick wins
- [ ] Performance: KPI dashboard & measurement plan

**ACCOUNTABILITY Phase:**
- [ ] Align: Goal cascading & alignment workshop
- [ ] Assign: RACI matrix & role definitions
- [ ] Action: OMVP definition & sprint plan
- [ ] Access: Progress tracking & issue log
- [ ] Adapt: Feedback loops & retrospectives

**MANAGE Phase:**
- [ ] Map Outputs: Value stream & customer journey
- [ ] Measure: KPI tracking & ROI calculation
- [ ] Monitor: Real-time dashboard & alerts
- [ ] Modify: Review cadence & change request process
- [ ] Maintain: Knowledge transfer & continuous improvement

### Quality Check ✅
- [ ] All sections follow IPAM framework structure
- [ ] OMVP clearly defined with success criteria
- [ ] Metrics have baseline, target, and measurement method
- [ ] Risks identified with mitigation plans
- [ ] Stakeholders engaged appropriately (RACI)
- [ ] Timeline realistic with buffer for unknowns
- [ ] Budget detailed with contingency
- [ ] Compliance requirements addressed
- [ ] Sustainability plan for post-launch

---

## 💡 TIPS FOR GREAT OC DOCUMENTS

1. **Start with Why**: Always clarify the business objective and customer impact upfront

2. **OMVP Focus**: Don't boil the ocean. Define minimum viable scope that delivers objective

3. **Data-Driven**: Use metrics, not opinions. Baseline → Target → Actual

4. **Stakeholder Buy-in**: Involve stakeholders early and often. No surprises at go-live

5. **Clear Ownership**: Every action item has ONE owner (RACI)

6. **Realistic Timeline**: Add 20-30% buffer for unknowns

7. **Risk Proactive**: Identify risks early, plan mitigation BEFORE they happen

8. **Celebrate Wins**: Recognize team efforts at every milestone

9. **Iterate**: OC is living document. Update as you learn

10. **Think Long-term**: Plan for sustainability from day 1, not afterthought
