# IPAM Framework - Quick Reference Card

## 🚀 TL;DR

Gõ `/ipam` trong Claude Code → Describe situation → Get guidance

---

## 📋 Framework Cheat Sheet

### 4 Phases (IPAM)

```
┌─────────────┐
│  IDENTIFY   │ → WHY change? WHAT is the real problem?
│    (5I)     │   Intention, Interconnect, Insight, Innovation, Integrity
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    PLAN     │ → HOW to change? WHAT is the roadmap?
│    (5P)     │   Purpose, Pathway, Perspective, Priorities, Performance
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ACCOUNTABILITY│ → WHO does WHAT? WHEN to deliver?
│    (5A)     │   Align, Assign, Action, Access, Adapt
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   MANAGE    │ → How to SUSTAIN? Are we WINNING?
│    (5M)     │   Map, Measure, Monitor, Modify, Maintain
└─────────────┘
```

---

## 🎯 Key Acronyms

| Acronym | Meaning | Usage |
|---------|---------|-------|
| **OMVP** | Objective Minimum Viable Product | Focus on outcome, not output |
| **OTOOB** | OC Owner - Timeframe - One Team - Outputs - Biz Impact | Planning framework |
| **TAC** | Transform - Amplify - Continue | Categorize change types |
| **RACI** | Responsible - Accountable - Consulted - Informed | Ownership matrix |

---

## ⚡ Quick Decision Tree

```
Starting a change initiative?
│
├─ Clear on problem?
│  ├─ NO → IDENTIFY phase
│  └─ YES ↓
│
├─ Have detailed plan?
│  ├─ NO → PLAN phase
│  └─ YES ↓
│
├─ Ready to execute?
│  ├─ NO → PLAN phase (detail out)
│  └─ YES → ACCOUNTABILITY phase
│
└─ Already executing?
   └─ YES → MANAGE phase
```

---

## 🔑 5 Most Important Questions

Before starting ANY change:

1. **Customer**: What does customer get from this?
2. **Outcome**: How do we measure success?
3. **OMVP**: What's the smallest scope that achieves the objective?
4. **Owner**: Who is accountable for the result?
5. **Sustainability**: How do we maintain this long-term?

---

## 📊 Essential Templates

### 1. OMVP One-Pager

```markdown
## [Initiative Name]

**Customer Objective**: [In 1 sentence]

**Success Metrics**:
- Metric 1: [Current → Target]
- Metric 2: [Current → Target]

**MVP Scope** (Must Have):
1.
2.
3.

**Out of Scope** (v2+):
-

**Timeline**: [X weeks]

**Risks**:
- Risk 1 → Mitigation
```

### 2. Phase Checklist

```markdown
IDENTIFY ☐
  ☐ Clear intention defined
  ☐ Stakeholders mapped
  ☐ Data collected
  ☐ Solutions brainstormed
  ☐ Values alignment checked

PLAN ☐
  ☐ Purpose statement written
  ☐ Roadmap with milestones
  ☐ Stakeholder plan created
  ☐ Priorities set
  ☐ KPIs defined

ACCOUNTABILITY ☐
  ☐ Team aligned
  ☐ RACI created
  ☐ OMVP scoped
  ☐ Tracking setup
  ☐ Review cadence set

MANAGE ☐
  ☐ Value stream mapped
  ☐ Metrics tracking
  ☐ Monitoring active
  ☐ Retros scheduled
  ☐ Sustainability plan
```

---

## 🎨 Color Codes for Priority

Use in planning:

- 🔴 **P0 (Critical)**: Must have for launch, blocks everything
- 🟡 **P1 (High)**: Important, deliver in first phase
- 🟢 **P2 (Medium)**: Nice to have, v2
- ⚪ **P3 (Low)**: Future consideration

---

## 💬 Common Agent Commands

```bash
# Start new initiative
/ipam

# Get phase-specific help
/ipam "I'm in PLAN phase, need help với stakeholder analysis"

# Template request
/ipam "Generate RACI matrix template for my project"

# Quick advice
/ipam "Quick question: Nên prioritize feature A hay B?"

# Risk assessment
/ipam "Help me identify risks cho [initiative]"

# OMVP definition
/ipam "Help me scope OMVP for [objective]"
```

---

## 📈 Success Metrics Examples

| Initiative Type | Key Metrics |
|----------------|-------------|
| **Customer Experience** | CSAT, NPS, Response Time, Resolution Rate |
| **Product Launch** | Adoption Rate, Activation %, Time-to-Value, Retention |
| **Process Improvement** | Cycle Time, Error Rate, Cost per Transaction, Throughput |
| **System Migration** | Downtime, Data Accuracy, User Adoption, Incident Rate |
| **Team Transformation** | Velocity, Quality (bugs), Time-to-Market, Team Satisfaction |

---

## 🚨 Red Flags

Stop and re-evaluate if:

- ❌ Customer objective không clear sau 30 min discussion
- ❌ Success metrics chỉ là vanity metrics (VD: "users happy")
- ❌ Timeline là "ASAP" hoặc "as fast as possible"
- ❌ No one willing to be Accountable
- ❌ Scope keeps growing (scope creep)
- ❌ Team không align về priorities
- ❌ No plan for what happens after launch
- ❌ Stakeholder resistance được ignore

---

## 🧭 Phase Duration Guidelines

| Complexity | Identify | Plan | Accountability | Manage |
|-----------|----------|------|----------------|--------|
| **Low** | 3-5 days | 1 week | 2-4 weeks | Ongoing |
| **Medium** | 1-2 weeks | 2-3 weeks | 4-8 weeks | Ongoing |
| **High** | 3-4 weeks | 4-6 weeks | 8-16 weeks | Ongoing |

**Rule of thumb**: Don't spend > 30% of total timeline on IDENTIFY + PLAN

---

## 💡 Pro Tips

1. **Document as you go**: Không để đến cuối mới document
2. **Celebrate small wins**: Maintain momentum
3. **Over-communicate**: Better than surprising people
4. **Data over opinions**: But use judgment too
5. **OMVP is your friend**: Don't overbuild
6. **Retrospectives are gold**: Actually implement learnings
7. **Customer feedback loop**: Talk to customers weekly
8. **Sustainability from day 1**: Don't defer it

---

## 📞 Emergency Triage

**Project is failing? Quick diagnosis:**

```
Problem: Nobody knows what we're building
→ Back to IDENTIFY - clarify intention & innovation

Problem: Plan keeps changing
→ PLAN phase incomplete - redo priorities & pathway

Problem: Execution is chaos
→ ACCOUNTABILITY issue - create RACI, align team

Problem: Can't tell if we're succeeding
→ MANAGE phase - define metrics, set up monitoring

Problem: All of the above
→ Start over with IDENTIFY, don't skip phases
```

---

## 🎓 Learning Path

**Week 1**: Understand framework
- Read framework.md
- Review examples trong README
- Practice với 1 small initiative

**Week 2**: Apply IDENTIFY + PLAN
- Pick real project
- Go through IDENTIFY questions
- Create plan với OTOOB

**Week 3**: Execute ACCOUNTABILITY
- Define OMVP
- Create RACI
- Start first sprint

**Week 4+**: MANAGE & Iterate
- Track metrics
- Weekly retros
- Continuous improvement

---

## 🔗 Quick Links

- Full Framework: `framework.md`
- Detailed Guide: `README.md`
- Agent Prompt: `IPAM_AGENT_PROMPT.md`
- Python Tools: `ipam_*.py`

---

## ⌨️ Keyboard Shortcuts (Mental Models)

Remember: **I-P-A-M**

- **I**: "I need to **I**dentify the real problem first"
- **P**: "I need to **P**lan the roadmap"
- **A**: "I'm **A**ccountable for execution"
- **M**: "I **M**ust manage and sustain this"

---

Print this và stick on your monitor! 📌
