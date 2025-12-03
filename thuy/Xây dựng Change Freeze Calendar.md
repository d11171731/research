# Hướng dẫn Xây dựng Change Freeze Calendar cho Công ty Fintech

## 1. Phân tích Đặc thù Kinh doanh từng Khách hàng

### 1.1. Công ty Chứng khoán

**Khung giờ nhạy cảm (Critical Hours):**
- Giao dịch: 9:00 - 11:30 và 13:00 - 15:00 (T2-T6)
- Pre-market: 8:30 - 9:00
- Post-market settlement: 15:00 - 16:30

**Thời điểm Freeze bắt buộc:**
- Ngày đáo hạn phái sinh (thứ 5 tuần thứ 3 hàng tháng)
- Ngày chốt quyền cổ tức các mã lớn
- Kỳ báo cáo tài chính (quý)
- Ngày nghỉ lễ + 1 ngày trước/sau

**Cửa sổ Change an toàn:**
- 18:00 - 6:00 ngày làm việc
- Cuối tuần (Thứ 7 từ 12:00, CN cả ngày, hoàn thành trước 6:00 T2)

---

### 1.2. Công ty Bảo hiểm Phi nhân thọ (24/7)

**Khung giờ nhạy cảm:**
- Peak hours cấp đơn: 9:00 - 17:00 (T2-T6)
- Claim khẩn cấp: 24/7 (tai nạn, y tế)

**Thời điểm Freeze bắt buộc:**
- Mùa mưa bão (tháng 8-11): tăng cường freeze cho module claim
- Ngày nghỉ lễ kéo dài (nhiều tai nạn giao thông)
- Renewal season (nếu có đợt tái tục lớn)

**Cửa sổ Change an toàn:**
- Maintenance window: 2:00 - 5:00 (thấp traffic nhất)
- Áp dụng Blue-Green deployment hoặc Canary release
- Phải có rollback plan trong 15 phút

---

### 1.3. Chuỗi F&B (2 công ty)

**Khung giờ nhạy cảm:**
- Lunch rush: 11:00 - 13:30
- Dinner rush: 18:00 - 21:00
- Weekend peak: 11:00 - 21:00 (T7, CN)

**Thời điểm Freeze bắt buộc:**
- Các ngày lễ lớn (Tết, 30/4, 2/9, Giáng sinh...)
- Campaign marketing lớn (flash sale, anniversary)
- Mùa cao điểm: Tết Nguyên đán (trước 2 tuần - sau 1 tuần)

**Cửa sổ Change an toàn:**
- 1:00 - 6:00 hàng ngày
- Sáng T2-T5: 6:00 - 10:00 (nếu cần thiết)

---

## 2. Checklist Xây dựng Chính sách Change Freeze

### Phase 1: Chuẩn bị & Phân tích (Tuần 1-2)

| # | Công việc | Output | Owner |
|---|-----------|--------|-------|
| 1.1 | Thu thập dữ liệu peak hours từng khách hàng (logs, analytics) | Báo cáo traffic pattern | Technical Team |
| 1.2 | Xác định các sự kiện kinh doanh quan trọng năm tới | Business Event Calendar | Account Manager |
| 1.3 | Review incident history liên quan đến change | Incident Analysis Report | Operations |
| 1.4 | Mapping hệ thống/service theo mức độ critical | System Criticality Matrix | Architect |
| 1.5 | Xác định stakeholders và escalation path | RACI Matrix | PM |

---

### Phase 2: Thiết kế Policy (Tuần 3-4)

| # | Công việc | Output | Owner |
|---|-----------|--------|-------|
| 2.1 | Định nghĩa các loại Change (Standard/Normal/Emergency) | Change Classification Guide | Change Manager |
| 2.2 | Thiết lập tiêu chí đánh giá risk cho từng loại change | Risk Assessment Criteria | Technical Lead |
| 2.3 | Xây dựng Freeze Calendar template theo từng vertical | Draft Calendar | Change Manager |
| 2.4 | Định nghĩa Exception Process (khi cần change trong freeze) | Exception Procedure | Operations Manager |
| 2.5 | Thiết lập quy trình approval cho Emergency Change | Emergency Change Workflow | Director |

---

### Phase 3: Cấu hình Jira Cloud (Tuần 5-6)

| # | Công việc | Output | Owner |
|---|-----------|--------|-------|
| 3.1 | Tạo Custom Fields cho Change Request | - Change Type<br>- Risk Level<br>- Affected Systems<br>- Customer/Vertical | Jira Admin |
| 3.2 | Cấu hình Workflow với Freeze validation | Workflow với automation rules | Jira Admin |
| 3.3 | Tạo Calendar view/Dashboard | Freeze Calendar Dashboard | Jira Admin |
| 3.4 | Setup automation rules chặn change trong freeze period | Automation Rules | Jira Admin |
| 3.5 | Tích hợp notification (Slack/Email/Teams) | Alert Configuration | DevOps |

---

### Phase 4: Triển khai & Training (Tuần 7-8)

| # | Công việc | Output | Owner |
|---|-----------|--------|-------|
| 4.1 | Soạn tài liệu hướng dẫn sử dụng | User Guide, SOP | Technical Writer |
| 4.2 | Training cho internal team | Training sessions | Change Manager |
| 4.3 | Training cho khách hàng (nếu cần) | Customer onboarding | Account Manager |
| 4.4 | Pilot với 1 khách hàng | Pilot Report | PM |
| 4.5 | Rollout toàn bộ | Go-live | PM |

---

## 3. Chi tiết Cấu hình Jira Cloud

### 3.1. Custom Fields cần tạo

```
1. Change Type (Select List)
   - Standard (Pre-approved, low risk)
   - Normal (Requires CAB approval)
   - Emergency (Critical fix, expedited)

2. Risk Level (Select List)
   - Low (No customer impact)
   - Medium (Limited impact, reversible)
   - High (Significant impact)
   - Critical (Service affecting)

3. Target Customer/Vertical (Multi-select)
   - Securities Company
   - Insurance Company  
   - F&B Chain A
   - F&B Chain B
   - Internal Systems

4. Planned Start DateTime (DateTime picker)

5. Planned End DateTime (DateTime picker)

6. Rollback Plan (Text - Required)

7. Freeze Override Approval (User picker - for exceptions)
```

### 3.2. Automation Rules

**Rule 1: Block Change trong Freeze Period**
```
WHEN: Issue transitioned to "Scheduled"
IF: 
  - Planned Start DateTime falls within Freeze Period 
  - AND Change Type != "Emergency"
  - AND Freeze Override Approval is EMPTY
THEN:
  - Transition back to "Pending Review"
  - Add comment: "⚠️ Change blocked: Falls within freeze period for [Customer]. 
    Please reschedule or request exception approval."
  - Send notification to Change Manager
```

**Rule 2: Emergency Change Alert**
```
WHEN: Change Type = "Emergency"
THEN:
  - Send Slack/Teams notification to On-call channel
  - Add watchers: Change Manager, Technical Lead, Account Manager
  - Set Due Date = Created + 4 hours
```

**Rule 3: Reminder trước Freeze**
```
WHEN: 7 days before Freeze Period starts
THEN:
  - Send bulk notification to all assignees with open changes
  - Create summary report of pending changes
```

### 3.3. Dashboard Components

Tạo Dashboard "Change Freeze Calendar" với các gadgets:

1. **Calendar View**: Hiển thị tất cả freeze periods theo màu
   - Đỏ: Hard Freeze (no changes)
   - Vàng: Soft Freeze (Standard only)
   - Xanh: Open window

2. **Filter Results**: Changes scheduled trong 14 ngày tới

3. **Pie Chart**: Changes by Risk Level

4. **Two-Dimensional Filter**: Customer vs Change Status

---

## 4. Ma trận Change Freeze theo Vertical

| Thời điểm | Securities | Insurance | F&B | Internal |
|-----------|------------|-----------|-----|----------|
| T2-T6: 9:00-15:00 | 🔴 Hard | 🟡 Soft | 🟢 Open | 🟢 Open |
| T2-T6: 15:00-18:00 | 🟡 Soft | 🟡 Soft | 🟡 Soft | 🟢 Open |
| T2-T6: 18:00-9:00 | 🟢 Open | 🟡 Soft | 🟢 Open* | 🟢 Open |
| T7-CN | 🟢 Open | 🟡 Soft | 🔴 Hard (peak) | 🟢 Open |
| Ngày lễ | 🔴 Hard | 🔴 Hard | 🔴 Hard | 🟡 Soft |
| Đáo hạn phái sinh | 🔴 Hard | 🟢 Open | 🟢 Open | 🟢 Open |
| Mùa bão (T8-T11) | 🟢 Open | 🔴 Hard (claim) | 🟢 Open | 🟢 Open |

*F&B: Tránh 18:00-21:00

---

## 5. Quy trình Exception (Change trong Freeze)

```
┌─────────────────────────────────────────────────────────────┐
│                    EXCEPTION REQUEST                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Requestor tạo Change Request với justification          │
│           ↓                                                 │
│  2. Technical Lead review: Risk Assessment                  │
│           ↓                                                 │
│  3. Account Manager confirm: Business Impact                │
│           ↓                                                 │
│  4. Customer Sign-off (nếu cần)                            │
│           ↓                                                 │
│  5. Director/VP Approval                                    │
│           ↓                                                 │
│  6. Mandatory requirements:                                 │
│     ✓ Rollback plan tested                                 │
│     ✓ On-call team standby                                 │
│     ✓ Customer notified                                    │
│     ✓ Monitoring dashboard ready                           │
│           ↓                                                 │
│  7. Execute với enhanced monitoring                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. Lịch Freeze mẫu năm 2025

### Q1/2025

| Ngày | Sự kiện | Affected Verticals | Freeze Type |
|------|---------|-------------------|-------------|
| 25/1 - 5/2 | Tết Nguyên đán | ALL | 🔴 Hard Freeze |
| 16/1 | Đáo hạn phái sinh | Securities | 🔴 Hard Freeze |
| 20/2 | Đáo hạn phái sinh | Securities | 🔴 Hard Freeze |
| 20/3 | Đáo hạn phái sinh | Securities | 🔴 Hard Freeze |

### Q2/2025

| Ngày | Sự kiện | Affected Verticals | Freeze Type |
|------|---------|-------------------|-------------|
| 30/4 - 1/5 | Lễ 30/4-1/5 | ALL | 🔴 Hard Freeze |
| 17/4, 15/5, 19/6 | Đáo hạn phái sinh | Securities | 🔴 Hard Freeze |
| 15/4-20/4 | Báo cáo Q1 | Securities | 🟡 Soft Freeze |

*(Tiếp tục cho Q3, Q4)*

---

## 7. KPIs Đo lường Hiệu quả

| Metric | Mục tiêu | Đo lường |
|--------|----------|----------|
| Change Success Rate | > 95% | (Successful changes / Total changes) |
| Freeze Violation Rate | < 2% | (Unauthorized changes in freeze / Total) |
| Exception Approval Time | < 4 hours | Từ request đến approval |
| Incident từ Change | < 5% | (Change-related incidents / Total changes) |
| Customer Complaint về Downtime | 0 | Số complaint trong freeze period |

---

## 8. Checklist Pre-Go-Live

- [ ] Policy document đã được approve bởi Management
- [ ] Jira workflow và automation đã test đầy đủ
- [ ] Tất cả stakeholders đã được training
- [ ] Calendar năm 2025 đã được sync với tất cả team
- [ ] Escalation contacts đã cập nhật và verified
- [ ] Rollback procedures đã documented cho từng hệ thống
- [ ] Monitoring/alerting đã setup cho freeze periods
- [ ] Customer communication templates đã chuẩn bị
- [ ] Exception request form đã live trên Jira

---

Bạn cần tôi đi sâu vào phần nào cụ thể hơn không? Ví dụ như chi tiết cấu hình Jira automation rules, hoặc template cho policy document?