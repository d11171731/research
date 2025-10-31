# IPAM Framework - Change Management System

Framework quản trị thay đổi theo mục tiêu hướng tới khách hàng (Objective to Customer) và tổ chức thay đổi (Organization Change).

## 🎯 Framework Overview

IPAM gồm 4 giai đoạn chính với 20 bước:

### 1. **IDENTIFY** (5I) - Transform, Amplify, Continue
- **I**ntention: Xác định mục đích và tầm nhìn
- **I**nterconnect: Hiểu mối quan hệ stakeholders và hệ thống
- **I**nsight: Thu thập và phân tích thông tin
- **I**nnovation: Phát triển giải pháp sáng tạo
- **I**ntegrity: Đảm bảo tính nhất quán và đạo đức

### 2. **PLAN** (5P) - OTOOB
**OTOOB**: OC Owner - Timeframe - One Team - Outputs - Biz Impact

- **P**urpose: Xác định mục đích rõ ràng
- **P**athway: Lộ trình thực hiện
- **P**erspective: Góc nhìn đa chiều
- **P**riorities: Xác định ưu tiên
- **P**erformance: Metrics đo lường

### 3. **ACCOUNTABILITY** (5A) - OMVP
**OMVP**: Objective Minimum Viable Product

- **A**lign: Liên kết mục tiêu và hành động
- **A**ssign: Phân công trách nhiệm
- **A**ction: Thực hiện hành động
- **A**ccess: Đánh giá tiến độ
- **A**dapt: Điều chỉnh dựa trên feedback

### 4. **MANAGE** (5M) - Objective Management
- **M**ap Outputs: Lập bản đồ đầu ra theo chuỗi giá trị
- **M**easure: Đo lường kết quả
- **M**onitor: Giám sát và phát hiện vấn đề
- **M**odify: Điều chỉnh chiến lược
- **M**aintain: Duy trì tính bền vững

---

## 🤖 Cách Sử dụng IPAM Agent

### Option 1: Slash Command (Recommended ⭐)

Trong Claude Code, gõ:

```bash
/ipam
```

Agent sẽ hỏi về tình huống của bạn và tư vấn theo framework.

**Ví dụ:**
```
/ipam

Sau đó trả lời:
1. Current situation: Customer support response time là 24h, quá chậm
2. Desired outcome: Giảm xuống 2h, tăng customer satisfaction
3. Main challenges: Limited budget, existing system cũ, team overwhelmed
4. Timeline: 6 months
```

### Option 2: Direct Conversation

Bạn có thể chat trực tiếp với Claude Code và reference framework:

```
@IPAM_AGENT_PROMPT.md Tôi muốn improve customer onboarding process.
Current: 2 weeks, manual, error-prone
Target: 2 days, automated, seamless
Help me plan theo IPAM framework
```

---

## 🎓 Key Concepts

### OMVP (Objective Minimum Viable Product)
Focus vào **outcome** (customer objective achieved), không phải **output** (features delivered).

**Example:**
- ❌ Output thinking: "Build customer portal with 20 features"
- ✅ Outcome thinking: "Enable 80% customers tự resolve issues without calling support"

### OTOOB Planning
- **OC Owner**: Ai chịu trách nhiệm cho organizational change
- **Timeframe**: Timeline thực tế, có buffer
- **One Team**: Cross-functional team aligned
- **Outputs**: Deliverables cụ thể
- **Biz Impact**: Measurable business impact

### TAC Framework
Categorize changes:
- **Transform**: Fundamental change (VD: Digital transformation)
- **Amplify**: Enhance existing (VD: Improve existing process)
- **Continue**: Maintain momentum (VD: Sustain improvements)

---

## 💡 Usage Examples

### Example 1: Improve Customer Support

**Situation:**
```
Current: 24h response time, manual ticketing, low CSAT (3.2/5)
Desired: 2h response time, automated routing, CSAT > 4.5/5
Constraint: $500K budget, 6 months, can't interrupt service
```

**IPAM Approach:**

**Phase 1 - IDENTIFY (Weeks 1-3)**
- Intention: Improve customer experience → retention
- Interconnect: Map support, eng, product, customers
- Insight: Analyze 1000+ tickets, identify patterns
- Innovation: AI chatbot + knowledge base + routing automation
- Integrity: Ensure quality không sacrifice, team capacity sustainable

**Phase 2 - PLAN (Weeks 4-6)**
- Purpose: 80% issues self-resolved, <2h human support
- Pathway: Phase 1 (chatbot) → Phase 2 (KB) → Phase 3 (routing)
- Perspective: Weekly stakeholder updates, change champions
- Priorities: P0 (chatbot for top 10 FAQs), P1 (KB), P2 (full automation)
- Performance: Response time, CSAT, % self-service, cost/ticket

**Phase 3 - ACCOUNTABILITY (Weeks 7-20)**
- OMVP: Chatbot answering top 10 questions (covers 60% tickets)
- RACI: Product (A), Eng (R), Support (C), Customer Success (I)
- 2-week sprints, daily standups
- Dashboard tracking metrics real-time
- Bi-weekly retros, monthly pivots

**Phase 4 - MANAGE (Weeks 21-26)**
- Map: Customer journey from issue → resolution
- Measure: Track all KPIs, A/B test chatbot responses
- Monitor: Alert if response time > 4h, CSAT < 4.0
- Modify: Adjust chatbot based on user feedback
- Maintain: Train team, document learnings, plan v2

---

### Example 2: Product Feature Rollout

**Situation:**
```
Launch new payment feature for 1M users
Risk: High - impacts revenue
Stakeholders: Product, Eng, Finance, Legal, Customers
Timeline: Q2 launch deadline
```

**Quick IPAM Guide:**

1. **IDENTIFY**:
   - WHY this feature? Customer pain = multiple payment methods
   - WHO affected? All users, especially international
   - DATA? 40% cart abandonment due to limited payment options

2. **PLAN**:
   - OMVP: Credit card + PayPal (covers 80% users)
   - Phase 1: Domestic users → Phase 2: International
   - KPI: Conversion rate +15%, cart abandonment -30%

3. **ACCOUNTABILITY**:
   - Product (owns outcome), Eng (builds), Legal (approves), Finance (integrates)
   - Sprint 1-4: Build, Sprint 5: Beta (10K users), Sprint 6: Full rollout
   - Daily health checks, weekly stakeholder reviews

4. **MANAGE**:
   - Monitor: Transaction success rate, payment errors, fraud rate
   - A/B test: 50% users get new feature, track metrics
   - If metrics good → Full rollout, if not → Modify approach

---

## 🛠️ Tools & Templates

Agent có thể generate các templates:

- ✅ RACI Matrix
- ✅ Stakeholder Analysis
- ✅ Risk Register
- ✅ OMVP Canvas
- ✅ Sprint Planning Template
- ✅ Retrospective Format
- ✅ KPI Dashboard Structure

**Usage:**
```
/ipam

"Tôi cần RACI matrix template cho digital transformation project"
```

---

## 🚀 Best Practices

### 1. Always Start with Customer
- Mọi initiative phải answer: "Customer gets gì từ đây?"
- Define success qua customer metrics, không chỉ internal metrics

### 2. Think OMVP, Not Perfection
- Deliver smallest scope that achieves objective
- Iterate based on feedback
- 80/20 rule: 20% effort → 80% value

### 3. Data > Opinions
- Establish baseline metrics
- Make decisions based on data
- Measure everything

### 4. Communicate, Communicate, Communicate
- Over-communicate than under
- Transparent về challenges và changes
- Regular updates to all stakeholders

### 5. Build Feedback Loops
- Retrospectives after every sprint
- Customer feedback channels
- Team pulse checks

### 6. Plan for Sustainability
- Don't just deliver project, build capability
- Document learnings
- Transfer knowledge
- Plan for ongoing support

---

## 🎯 When to Use Each Phase

### Use IDENTIFY when:
- Unclear về root cause của problem
- Multiple solutions possible, cần evaluate
- Need stakeholder buy-in
- Starting new initiative from scratch

### Use PLAN when:
- Đã biết WHAT to do, cần figure out HOW
- Need roadmap và resource planning
- Multiple teams involved
- Need to communicate vision

### Use ACCOUNTABILITY when:
- Have plan, ready to execute
- Need clear ownership
- Starting sprints/iterations
- Need to track progress

### Use MANAGE when:
- Already executing
- Need to optimize performance
- Want to measure impact
- Ensuring sustainability

---

## 📞 Getting Help

### Ask Agent:
```
/ipam "Tôi đang stuck ở [situation], không biết next step"
```

### Common Questions:

**Q: Làm sao biết mình ở phase nào?**
A: Gõ `/ipam` và mô tả situation, agent sẽ diagnose

**Q: Có thể skip phases không?**
A: Không nên. Mỗi phase builds on previous. Nhưng có thể fast-track nếu low complexity.

**Q: Làm sao define OMVP?**
A: Ask agent: "Help me define OMVP for [your objective]"

**Q: Timeline cho mỗi phase?**
A: Depends on complexity:
- Low: 1-2 weeks per phase
- Medium: 2-4 weeks per phase
- High: 4-8 weeks per phase

---

## 📝 Quick Start Checklist

Starting a new change initiative:

- [ ] Define customer objective clearly
- [ ] Estimate business impact (revenue, cost, satisfaction)
- [ ] List all stakeholders
- [ ] Identify constraints (budget, time, resources)
- [ ] Gõ `/ipam` và start conversation
- [ ] Follow agent guidance qua từng phase
- [ ] Document decisions và learnings
- [ ] Measure và iterate

---

## 🔄 Continuous Improvement

Framework này là living document. Khi bạn apply:
- Document what works / doesn't work
- Share learnings với team
- Adapt framework cho context của bạn
- Contribute improvements back

---

**Happy Change Management! 🚀**

For questions or feedback, start a conversation với IPAM Agent:
```
/ipam "I need help with..."
```
