# SLA Matrix cho từng loại Khách hàng

---

## **PHỤ LỤC F: SERVICE LEVEL AGREEMENT MATRIX**

---

## **1. TỔNG QUAN SLA FRAMEWORK**

### 1.1. Cấu trúc SLA

```
┌─────────────────────────────────────────────────────────────────────┐
│                        SLA FRAMEWORK                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    SERVICE AVAILABILITY                        │  │
│  │         Uptime commitment cho từng vertical                   │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                              │                                      │
│  ┌───────────────┬───────────┴───────────┬───────────────┐         │
│  │               │                       │               │         │
│  ▼               ▼                       ▼               ▼         │
│ ┌─────┐      ┌─────┐                 ┌─────┐         ┌─────┐       │
│ │ RTO │      │ RPO │                 │ MTT │         │ SLA │       │
│ │     │      │     │                 │     │         │Credit│      │
│ └─────┘      └─────┘                 └─────┘         └─────┘       │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                 CHANGE MANAGEMENT SLA                          │  │
│  │    Response time, approval time, implementation windows        │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    SUPPORT SLA                                 │  │
│  │         Response & resolution time theo severity              │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2. Định nghĩa Metrics

| Metric | Định nghĩa | Công thức |
|--------|------------|-----------|
| **Uptime** | Thời gian hệ thống available trong service hours | (Total Service Hours - Downtime) / Total Service Hours × 100% |
| **RTO** | Recovery Time Objective - Thời gian tối đa để khôi phục service | Từ khi incident xảy ra đến khi service restored |
| **RPO** | Recovery Point Objective - Mức độ data loss chấp nhận được | Measured in time (e.g., 15 phút = có thể mất data của 15 phút gần nhất) |
| **MTTR** | Mean Time To Repair - Thời gian trung bình để sửa lỗi | Average of all repair times |
| **MTTD** | Mean Time To Detect - Thời gian trung bình để phát hiện issue | Average time from incident occurrence to detection |
| **MTBF** | Mean Time Between Failures - Thời gian trung bình giữa các lần lỗi | Total uptime / Number of failures |

---

## **2. SLA MATRIX THEO VERTICAL**

### 2.1. Công ty Chứng khoán

#### 2.1.1. Service Availability SLA

| Metric | Trading Hours (9:00-15:00) | After Hours | Weekend |
|--------|:-------------------------:|:-----------:|:-------:|
| **Target Uptime** | 99.99% | 99.9% | 99.5% |
| **Max Downtime/tháng** | 0.44 phút | 4.32 phút | 21.6 phút |
| **RTO** | 5 phút | 30 phút | 4 giờ |
| **RPO** | 0 (zero data loss) | 5 phút | 15 phút |

#### 2.1.2. Service Hours Definition

| Period | Thời gian | Mô tả |
|--------|-----------|-------|
| **Critical Hours** | 08:30 - 15:30 (T2-T6) | Trading + pre/post market |
| **Business Hours** | 08:00 - 18:00 (T2-T6) | Full business operations |
| **Extended Hours** | 18:00 - 22:00 (T2-T6) | Report generation, settlement |
| **Maintenance Window** | 22:00 - 06:00 (T2-T6), T7-CN | Allowed maintenance |

#### 2.1.3. Incident Response SLA

| Severity | Định nghĩa | Response Time | Resolution Time | Escalation |
|----------|------------|:-------------:|:---------------:|------------|
| **P1 - Critical** | Trading bị gián đoạn, không thể đặt lệnh | 5 phút | 30 phút | Immediate to CTO |
| **P2 - High** | Một số chức năng trading bị ảnh hưởng | 15 phút | 2 giờ | 30 phút to Director |
| **P3 - Medium** | Chức năng phụ trợ bị lỗi, trading không ảnh hưởng | 30 phút | 8 giờ | 2 giờ to Manager |
| **P4 - Low** | Cosmetic issues, minor bugs | 4 giờ | 5 ngày | Next business day |

#### 2.1.4. Change Management SLA

| Change Type | Submission to Approval | Scheduling Lead Time | Implementation Window | Notification Lead Time |
|-------------|:----------------------:|:--------------------:|:---------------------:|:----------------------:|
| Standard | 4 giờ | 24 giờ | After hours only | 12 giờ |
| Normal | 3 ngày làm việc | 7 ngày | Weekend preferred | 3 ngày |
| Emergency | 1 giờ | ASAP | Any (với approval) | ASAP |

#### 2.1.5. Special Period SLA

| Event | Period | Enhanced SLA |
|-------|--------|--------------|
| Đáo hạn phái sinh | Thứ 5 tuần 3 hàng tháng | P1 response: 2 phút, RTO: 3 phút |
| Ngày chốt quyền VN30 | As scheduled | 99.999% uptime required |
| Báo cáo quý | 5 ngày cuối kỳ | No Normal changes allowed |

#### 2.1.6. SLA Credit Schedule

| Uptime Achieved | Service Credit |
|-----------------|----------------|
| 99.99% - 100% | 0% |
| 99.9% - 99.99% | 5% monthly fee |
| 99.0% - 99.9% | 15% monthly fee |
| 95.0% - 99.0% | 30% monthly fee |
| < 95.0% | 50% monthly fee |

**Ghi chú**: Credits chỉ áp dụng cho downtime trong Trading Hours. Planned maintenance không tính vào downtime nếu được thông báo trước 72 giờ.

---

### 2.2. Công ty Bảo hiểm Phi nhân thọ

#### 2.2.1. Service Availability SLA

| Metric | Core Business Hours (8:00-20:00) | Off-Peak Hours | Claim System (24/7) |
|--------|:-------------------------------:|:--------------:|:------------------:|
| **Target Uptime** | 99.95% | 99.9% | 99.99% |
| **Max Downtime/tháng** | 21.6 phút | 43.2 phút | 4.32 phút |
| **RTO** | 15 phút | 1 giờ | 10 phút |
| **RPO** | 5 phút | 15 phút | 1 phút |

#### 2.2.2. Service Hours Definition

| Period | Thời gian | Applicable Systems |
|--------|-----------|-------------------|
| **24/7 Critical** | Mọi lúc | Claim submission, Emergency hotline |
| **Core Business** | 08:00 - 20:00 (T2-T7) | Policy issuance, Customer portal |
| **Extended** | 20:00 - 08:00 | Self-service only |
| **Maintenance Window** | 02:00 - 05:00 daily | All systems (with notice) |

#### 2.2.3. Incident Response SLA

| Severity | Định nghĩa | Response Time | Resolution Time | Escalation |
|----------|------------|:-------------:|:---------------:|------------|
| **P1 - Critical** | Claim system down, không thể report claim | 10 phút | 1 giờ | Immediate to CTO |
| **P2 - High** | Policy issuance bị gián đoạn | 30 phút | 4 giờ | 1 giờ to Director |
| **P3 - Medium** | Một số chức năng bị ảnh hưởng | 2 giờ | 24 giờ | 4 giờ to Manager |
| **P4 - Low** | Minor issues, UI problems | 8 giờ | 7 ngày | Next business day |

#### 2.2.4. Change Management SLA

| Change Type | Submission to Approval | Scheduling Lead Time | Implementation Window | Notification Lead Time |
|-------------|:----------------------:|:--------------------:|:---------------------:|:----------------------:|
| Standard | 8 giờ | 48 giờ | 02:00 - 05:00 | 24 giờ |
| Normal | 5 ngày làm việc | 10 ngày | 02:00 - 05:00 (weekend preferred) | 5 ngày |
| Emergency | 2 giờ | ASAP | Any (với enhanced monitoring) | ASAP |

#### 2.2.5. Special Period SLA

| Event | Period | Enhanced SLA |
|-------|--------|--------------|
| Mùa bão (T8-T11) | Claim module | 99.999% uptime, P1 response: 5 phút |
| Lễ kéo dài | Toàn bộ | No changes, enhanced support |
| Renewal campaign | As notified | Soft freeze on Policy module |

#### 2.2.6. SLA Credit Schedule

| Uptime Achieved (24/7 system) | Service Credit |
|-------------------------------|----------------|
| 99.99% - 100% | 0% |
| 99.9% - 99.99% | 10% monthly fee |
| 99.0% - 99.9% | 25% monthly fee |
| 95.0% - 99.0% | 40% monthly fee |
| < 95.0% | 60% monthly fee |

---

### 2.3. Chuỗi F&B (Nhà hàng & Bán hàng Online/Offline)

#### 2.3.1. Service Availability SLA

| Metric | Peak Hours (11-14h, 18-21h) | Regular Hours | Night (23:00-06:00) |
|--------|:--------------------------:|:-------------:|:-------------------:|
| **Target Uptime** | 99.95% | 99.9% | 99.5% |
| **Max Downtime/tháng** | 21.6 phút | 43.2 phút | 3.6 giờ |
| **RTO** | 10 phút | 30 phút | 2 giờ |
| **RPO** | 5 phút | 15 phút | 1 giờ |

#### 2.3.2. Service Hours Definition

| Period | Thời gian | Priority |
|--------|-----------|----------|
| **Lunch Peak** | 11:00 - 14:00 daily | Critical |
| **Dinner Peak** | 18:00 - 21:00 daily | Critical |
| **Weekend All Day** | 10:00 - 22:00 (T7-CN) | Critical |
| **Regular** | 06:00 - 11:00, 14:00 - 18:00, 21:00 - 23:00 | High |
| **Maintenance Window** | 01:00 - 06:00 (T2-T5) | Allowed |

#### 2.3.3. System-Specific SLA

| System | Uptime Target | RTO | RPO | Notes |
|--------|:-------------:|:---:|:---:|-------|
| **POS System** | 99.99% | 5 phút | 0 | Zero transaction loss |
| **Online Ordering** | 99.95% | 15 phút | 5 phút | During operating hours |
| **Kitchen Display** | 99.9% | 10 phút | 5 phút | During operating hours |
| **Inventory** | 99.5% | 1 giờ | 30 phút | Non-critical hours |
| **Loyalty/CRM** | 99.5% | 2 giờ | 1 giờ | Points can be reconciled |
| **Reporting** | 99.0% | 4 giờ | 2 giờ | Can regenerate |

#### 2.3.4. Incident Response SLA

| Severity | Định nghĩa | Response Time | Resolution Time | Escalation |
|----------|------------|:-------------:|:---------------:|------------|
| **P1 - Critical** | POS down, không thể nhận order/thanh toán | 5 phút | 30 phút | Immediate to CTO |
| **P2 - High** | Online ordering down, một số cửa hàng affected | 15 phút | 2 giờ | 30 phút to Director |
| **P3 - Medium** | Loyalty không hoạt động, reporting delay | 1 giờ | 8 giờ | 2 giờ to Manager |
| **P4 - Low** | UI issues, minor bugs | 4 giờ | 5 ngày | Next business day |

#### 2.3.5. Change Management SLA

| Change Type | Submission to Approval | Scheduling Lead Time | Implementation Window | Notification Lead Time |
|-------------|:----------------------:|:--------------------:|:---------------------:|:----------------------:|
| Standard | 4 giờ | 24 giờ | 01:00 - 06:00 (T2-T5) | 12 giờ |
| Normal | 5 ngày làm việc | 7 ngày | 01:00 - 06:00 (T2-T4) | 3 ngày |
| Emergency | 1 giờ | ASAP | Any (với approval) | ASAP |

#### 2.3.6. Special Period SLA

| Event | Period | Enhanced SLA |
|-------|--------|--------------|
| Tết Nguyên đán | -15 ngày đến +7 ngày | Hard freeze, 99.999% uptime |
| Lễ 30/4-1/5, 2/9 | -3 ngày đến +1 ngày | Hard freeze |
| Flash Sale/Campaign | As notified | 99.99% uptime, P1 response: 3 phút |
| Weekend | T6 18:00 - CN 23:00 | Hard freeze |

#### 2.3.7. SLA Credit Schedule

| Uptime Achieved (Peak Hours) | Service Credit |
|------------------------------|----------------|
| 99.95% - 100% | 0% |
| 99.5% - 99.95% | 10% monthly fee |
| 99.0% - 99.5% | 20% monthly fee |
| 95.0% - 99.0% | 35% monthly fee |
| < 95.0% | 50% monthly fee |

**Bonus**: Nếu POS downtime gây mất doanh thu có bằng chứng, credit tính theo % revenue loss (cap 100% monthly fee).

---

### 2.4. Hệ thống Nội bộ

#### 2.4.1. Service Availability SLA

| Metric | Business Hours (8:00-18:00) | After Hours |
|--------|:---------------------------:|:-----------:|
| **Target Uptime** | 99.5% | 99.0% |
| **Max Downtime/tháng** | 3.6 giờ | 7.2 giờ |
| **RTO** | 2 giờ | 8 giờ |
| **RPO** | 1 giờ | 4 giờ |

#### 2.4.2. Incident Response SLA

| Severity | Response Time | Resolution Time |
|----------|:-------------:|:---------------:|
| **P1** | 30 phút | 4 giờ |
| **P2** | 2 giờ | 8 giờ |
| **P3** | 8 giờ | 3 ngày |
| **P4** | 24 giờ | 10 ngày |

#### 2.4.3. Change Management SLA

| Change Type | Submission to Approval | Implementation Window |
|-------------|:----------------------:|:---------------------:|
| Standard | 2 giờ | Any (với notice) |
| Normal | 2 ngày | After hours |
| Emergency | 30 phút | Any |

---

## **3. CONSOLIDATED SLA COMPARISON**

### 3.1. Uptime Comparison

| Vertical | Critical Period Uptime | Standard Uptime | Max Monthly Downtime (Critical) |
|----------|:----------------------:|:---------------:|:-------------------------------:|
| Securities | 99.99% | 99.9% | 0.44 phút |
| Insurance | 99.99% (Claim 24/7) | 99.95% | 4.32 phút |
| F&B | 99.95% | 99.9% | 21.6 phút |
| Internal | 99.5% | 99.0% | 3.6 giờ |

### 3.2. Response Time Comparison (P1 Incidents)

| Vertical | Response Time | Resolution Time | RTO |
|----------|:-------------:|:---------------:|:---:|
| Securities | 5 phút | 30 phút | 5 phút |
| Insurance | 10 phút | 1 giờ | 10 phút |
| F&B | 5 phút | 30 phút | 10 phút |
| Internal | 30 phút | 4 giờ | 2 giờ |

### 3.3. Change Window Comparison

| Vertical | Preferred Window | Prohibited Period |
|----------|-----------------|-------------------|
| Securities | Weekend (T7 12:00 - CN 18:00) | T2-T6: 08:30-16:30 |
| Insurance | Daily 02:00-05:00 | None (but 24/7 claim) |
| F&B | T2-T5: 01:00-06:00 | Peak hours + Weekend |
| Internal | After 22:00 | Business hours (flexible) |

---

## **4. SLA MONITORING & REPORTING**

### 4.1. Real-time Monitoring Dashboard

| Metric | Securities | Insurance | F&B | Internal |
|--------|:----------:|:---------:|:---:|:--------:|
| Current Uptime | ✅ Real-time | ✅ Real-time | ✅ Real-time | ✅ Real-time |
| Open Incidents | ✅ Real-time | ✅ Real-time | ✅ Real-time | ✅ Real-time |
| SLA Breach Risk | ✅ Alert | ✅ Alert | ✅ Alert | ⚠️ Daily |
| Change Calendar | ✅ Visible | ✅ Visible | ✅ Visible | ✅ Visible |

### 4.2. Reporting Schedule

| Report | Frequency | Recipients | Content |
|--------|-----------|------------|---------|
| **Daily Operations** | Daily 09:00 | Ops Team, Account Managers | Yesterday's incidents, today's changes |
| **Weekly SLA Report** | Monday 10:00 | Management, Customers (optional) | Uptime %, incident summary, upcoming maintenance |
| **Monthly SLA Review** | 5th of month | Leadership, Customer Executives | Full SLA metrics, trend analysis, credits due |
| **Quarterly Business Review** | Quarterly | C-level, Customer Leadership | Strategic review, improvement plans |

### 4.3. SLA Report Template

```
═══════════════════════════════════════════════════════════════════════
                    MONTHLY SLA REPORT
                    [CUSTOMER NAME] - [MONTH/YEAR]
═══════════════════════════════════════════════════════════════════════

EXECUTIVE SUMMARY
─────────────────────────────────────────────────────────────────────
Overall SLA Achievement: [XX.XX%]
Service Credits Due: [Amount/None]
Major Incidents: [Count]
Successful Changes: [Count/Total]

AVAILABILITY METRICS
─────────────────────────────────────────────────────────────────────
┌─────────────────┬──────────┬──────────┬──────────┬─────────────────┐
│ Period          │ Target   │ Achieved │ Downtime │ Status          │
├─────────────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Critical Hours  │ 99.99%   │ [XX.XX%] │ [X min]  │ [✅/⚠️/❌]     │
│ Business Hours  │ 99.95%   │ [XX.XX%] │ [X min]  │ [✅/⚠️/❌]     │
│ Off-Peak        │ 99.90%   │ [XX.XX%] │ [X min]  │ [✅/⚠️/❌]     │
└─────────────────┴──────────┴──────────┴──────────┴─────────────────┘

INCIDENT METRICS
─────────────────────────────────────────────────────────────────────
┌──────────┬───────┬─────────────────┬─────────────────┬─────────────┐
│ Severity │ Count │ Avg Response    │ Avg Resolution  │ SLA Met     │
├──────────┼───────┼─────────────────┼─────────────────┼─────────────┤
│ P1       │ [X]   │ [X min]         │ [X min]         │ [X/X]       │
│ P2       │ [X]   │ [X min]         │ [X hrs]         │ [X/X]       │
│ P3       │ [X]   │ [X hrs]         │ [X hrs]         │ [X/X]       │
│ P4       │ [X]   │ [X hrs]         │ [X days]        │ [X/X]       │
└──────────┴───────┴─────────────────┴─────────────────┴─────────────┘

CHANGE MANAGEMENT METRICS
─────────────────────────────────────────────────────────────────────
Total Changes: [X]
Successful: [X] ([XX%])
Failed/Rolled Back: [X] ([XX%])
Emergency Changes: [X] ([XX%] of total)
Freeze Violations: [X]

SERVICE CREDITS CALCULATION
─────────────────────────────────────────────────────────────────────
[If applicable, detailed calculation]

IMPROVEMENT ACTIONS
─────────────────────────────────────────────────────────────────────
1. [Action item from incidents]
2. [Planned improvements]
3. [Next month focus areas]

═══════════════════════════════════════════════════════════════════════
```

---

## **5. SLA ESCALATION MATRIX**

### 5.1. Escalation by Time Elapsed

| Time Since Incident | Securities | Insurance | F&B | Internal |
|---------------------|------------|-----------|-----|----------|
| **+5 min (P1)** | On-call Engineer | On-call Engineer | On-call Engineer | - |
| **+15 min (P1)** | Technical Lead | Technical Lead | Technical Lead | On-call Engineer |
| **+30 min (P1)** | Director + Account Mgr | Director + Account Mgr | Director + Account Mgr | Technical Lead |
| **+1 hour (P1)** | CTO + Customer Exec | CTO + Customer Exec | CTO + Customer Exec | Director |
| **+2 hours (P1)** | CEO | CEO | CEO | CTO |

### 5.2. Escalation Contacts

| Level | Role | Contact Method | Availability |
|-------|------|----------------|--------------|
| L1 | On-call Engineer | PagerDuty, Phone | 24/7 |
| L2 | Technical Lead | Phone, Slack | 24/7 for P1 |
| L3 | Director | Phone | 24/7 for P1 |
| L4 | CTO | Phone | 24/7 for P1 |
| L5 | CEO | Phone | P1 > 1 hour |

---

## **6. SLA EXCLUSIONS**

Các trường hợp sau **KHÔNG** tính vào SLA downtime:

| Exclusion | Điều kiện |
|-----------|-----------|
| **Planned Maintenance** | Thông báo trước ≥72 giờ, trong maintenance window |
| **Customer-caused Issues** | Lỗi do customer configuration, data, hoặc actions |
| **Third-party Failures** | Internet provider, payment gateway (ngoài tầm kiểm soát) |
| **Force Majeure** | Thiên tai, chiến tranh, pandemic |
| **Customer Request** | Customer yêu cầu downtime |
| **Security Response** | Emergency security patch theo customer approval |

**Lưu ý**: Tất cả exclusions phải được document và customer acknowledge trong vòng 24 giờ.

---

## **7. SLA REVIEW & AMENDMENT**

### 7.1. Review Schedule

| Review Type | Frequency | Participants | Output |
|-------------|-----------|--------------|--------|
| Operational Review | Weekly | Ops Team | Action items |
| SLA Performance Review | Monthly | Management + Account Mgr | Monthly report |
| Contract Review | Annually | Leadership + Customer | SLA amendments |
| Emergency Review | As needed | All stakeholders | Immediate changes |

### 7.2. Amendment Process

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SLA AMENDMENT PROCESS                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. Identify Need for Amendment                                     │
│     • Business requirement change                                   │
│     • Technology change                                             │
│     • Repeated SLA misses                                          │
│                         ↓                                           │
│  2. Draft Amendment Proposal                                        │
│     • Current vs Proposed SLA                                       │
│     • Impact analysis                                               │
│     • Cost implications                                             │
│                         ↓                                           │
│  3. Internal Review                                                 │
│     • Technical feasibility                                         │
│     • Financial approval                                            │
│                         ↓                                           │
│  4. Customer Negotiation                                            │
│     • Present proposal                                              │
│     • Negotiate terms                                               │
│                         ↓                                           │
│  5. Legal Review & Sign-off                                         │
│                         ↓                                           │
│  6. Implementation                                                  │
│     • Update monitoring                                             │
│     • Update documentation                                          │
│     • Communicate to all teams                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## **8. APPENDIX: QUICK REFERENCE CARDS**

### 8.1. Securities Quick Reference

```
╔═══════════════════════════════════════════════════════════════╗
║              SECURITIES SLA QUICK REFERENCE                   ║
╠═══════════════════════════════════════════════════════════════╣
║  TRADING HOURS: 09:00-15:00 (T2-T6)                          ║
║  UPTIME TARGET: 99.99%                                        ║
║  MAX DOWNTIME: 0.44 min/month                                 ║
║                                                               ║
║  P1 RESPONSE: 5 min | RESOLUTION: 30 min                      ║
║  RTO: 5 min | RPO: 0 (zero loss)                             ║
║                                                               ║
║  CHANGE WINDOW: T7 12:00 - CN 18:00                          ║
║  HARD FREEZE: Trading hours, Đáo hạn phái sinh               ║
║                                                               ║
║  ESCALATION: +15min→TechLead | +30min→Director | +1h→CTO     ║
╚═══════════════════════════════════════════════════════════════╝
```

### 8.2. Insurance Quick Reference

```
╔═══════════════════════════════════════════════════════════════╗
║              INSURANCE SLA QUICK REFERENCE                    ║
╠═══════════════════════════════════════════════════════════════╣
║  CLAIM SYSTEM: 24/7                                           ║
║  UPTIME TARGET: 99.99% (Claim) | 99.95% (Others)             ║
║  MAX DOWNTIME: 4.32 min/month (Claim)                        ║
║                                                               ║
║  P1 RESPONSE: 10 min | RESOLUTION: 1 hour                     ║
║  RTO: 10 min | RPO: 1 min                                     ║
║                                                               ║
║  CHANGE WINDOW: Daily 02:00-05:00                            ║
║  HARD FREEZE: Lễ kéo dài, Mùa bão (Claim module)             ║
║                                                               ║
║  ESCALATION: +30min→TechLead | +1h→Director | +2h→CTO        ║
╚═══════════════════════════════════════════════════════════════╝
```

### 8.3. F&B Quick Reference

```
╔═══════════════════════════════════════════════════════════════╗
║                 F&B SLA QUICK REFERENCE                       ║
╠═══════════════════════════════════════════════════════════════╣
║  PEAK HOURS: 11-14h, 18-21h daily | All day weekend          ║
║  UPTIME TARGET: 99.95% (Peak) | 99.9% (Regular)              ║
║  MAX DOWNTIME: 21.6 min/month (Peak)                         ║
║                                                               ║
║  P1 RESPONSE: 5 min | RESOLUTION: 30 min                      ║
║  RTO: 10 min | RPO: 5 min (POS: 0)                           ║
║                                                               ║
║  CHANGE WINDOW: T2-T5 01:00-06:00                            ║
║  HARD FREEZE: Weekend, Tết (-15d to +7d), Peak hours         ║
║                                                               ║
║  ESCALATION: +15min→TechLead | +30min→Director | +1h→CTO     ║
╚═══════════════════════════════════════════════════════════════╝
```

---

**--- HẾT PHỤ LỤC F ---**

---

Bạn có cần tôi bổ sung thêm phần nào không? Ví dụ như:
- Chi tiết Penalty/Bonus clauses cho từng vertical
- Template SLA Agreement để ký với khách hàng
- Runbook cho từng loại incident theo vertical