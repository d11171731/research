# Template Chính sách Quản lý Change Freeze

---

## **CHÍNH SÁCH QUẢN LÝ CHANGE FREEZE**

**[TÊN CÔNG TY FINTECH]**

---

| Thông tin tài liệu | |
|---|---|
| **Mã tài liệu** | POL-CHG-001 |
| **Phiên bản** | 1.0 |
| **Ngày hiệu lực** | [DD/MM/YYYY] |
| **Ngày xem xét tiếp theo** | [DD/MM/YYYY] (12 tháng sau) |
| **Chủ sở hữu tài liệu** | [Tên] - Change Manager |
| **Phê duyệt bởi** | [Tên] - [Chức vụ Director/VP] |
| **Phân loại** | Nội bộ / Chia sẻ với Khách hàng |

---

### **Lịch sử thay đổi tài liệu**

| Phiên bản | Ngày | Người thực hiện | Mô tả thay đổi |
|-----------|------|-----------------|----------------|
| 0.1 | [Date] | [Name] | Bản thảo đầu tiên |
| 0.2 | [Date] | [Name] | Cập nhật sau review |
| 1.0 | [Date] | [Name] | Phê duyệt chính thức |

---

## **MỤC LỤC**

1. [Mục đích và Phạm vi](#1-mục-đích-và-phạm-vi)
2. [Định nghĩa và Thuật ngữ](#2-định-nghĩa-và-thuật-ngữ)
3. [Phân loại Change](#3-phân-loại-change)
4. [Chính sách Change Freeze](#4-chính-sách-change-freeze)
5. [Lịch Change Freeze theo Vertical](#5-lịch-change-freeze-theo-vertical)
6. [Quy trình Exception](#6-quy-trình-exception)
7. [Vai trò và Trách nhiệm](#7-vai-trò-và-trách-nhiệm)
8. [Quy trình Thực hiện Change](#8-quy-trình-thực-hiện-change)
9. [Giám sát và Báo cáo](#9-giám-sát-và-báo-cáo)
10. [Vi phạm và Xử lý](#10-vi-phạm-và-xử-lý)
11. [Phụ lục](#11-phụ-lục)

---

## **1. MỤC ĐÍCH VÀ PHẠM VI**

### 1.1. Mục đích

Chính sách này được thiết lập nhằm:

- Đảm bảo tính ổn định và liên tục của các hệ thống production trong các giai đoạn kinh doanh quan trọng của khách hàng
- Giảm thiểu rủi ro gián đoạn dịch vụ do các thay đổi hệ thống gây ra
- Thiết lập quy trình rõ ràng cho việc quản lý change trong các giai đoạn nhạy cảm
- Đảm bảo tuân thủ các cam kết SLA với khách hàng

### 1.2. Phạm vi áp dụng

**Đối tượng áp dụng:**
- Tất cả nhân viên kỹ thuật của [Tên Công ty]
- Các đối tác/vendor thực hiện thay đổi trên hệ thống
- Các hệ thống phục vụ khách hàng sau:
  - Công ty Chứng khoán [Tên]
  - Công ty Bảo hiểm [Tên]
  - Chuỗi F&B [Tên A]
  - Chuỗi F&B [Tên B]
  - Hệ thống nội bộ [Tên Công ty]

**Hệ thống áp dụng:**
- Production environment
- Staging environment (khi có kết nối với Production)
- Database servers
- Network infrastructure
- Third-party integrations

**Ngoại lệ:** Môi trường Development và Testing độc lập không thuộc phạm vi của chính sách này.

---

## **2. ĐỊNH NGHĨA VÀ THUẬT NGỮ**

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| **Change** | Bất kỳ sự thay đổi nào đối với hệ thống IT bao gồm: cấu hình, code, database, infrastructure, network, hoặc các thành phần liên quan |
| **Change Freeze** | Giai đoạn mà các thay đổi hệ thống bị hạn chế hoặc cấm hoàn toàn để đảm bảo ổn định hệ thống |
| **Hard Freeze** | Cấm hoàn toàn mọi thay đổi, chỉ cho phép Emergency Change với phê duyệt đặc biệt |
| **Soft Freeze** | Chỉ cho phép Standard Change (đã pre-approved) và Emergency Change |
| **Change Window** | Khung thời gian được phép thực hiện thay đổi |
| **CAB** | Change Advisory Board - Hội đồng tư vấn thay đổi |
| **Rollback** | Quy trình hoàn tác thay đổi về trạng thái trước đó |
| **Lead Time** | Thời gian tối thiểu từ khi submit request đến khi thực hiện change |
| **RTO** | Recovery Time Objective - Thời gian tối đa để khôi phục dịch vụ |
| **RPO** | Recovery Point Objective - Mức độ dữ liệu tối đa có thể mất |

---

## **3. PHÂN LOẠI CHANGE**

### 3.1. Standard Change

| Tiêu chí | Mô tả |
|----------|-------|
| **Định nghĩa** | Các thay đổi đã được pre-approved, có rủi ro thấp và quy trình đã được document |
| **Ví dụ** | - Cập nhật SSL certificate theo lịch<br>- Thêm user account<br>- Cập nhật minor version của thư viện<br>- Thay đổi cấu hình logging |
| **Approval** | Pre-approved (không cần CAB) |
| **Lead Time** | Tối thiểu 24 giờ |
| **Trong Soft Freeze** | ✅ Được phép |
| **Trong Hard Freeze** | ❌ Không được phép |

### 3.2. Normal Change

| Tiêu chí | Mô tả |
|----------|-------|
| **Định nghĩa** | Các thay đổi có rủi ro trung bình đến cao, yêu cầu đánh giá và phê duyệt |
| **Ví dụ** | - Deploy tính năng mới<br>- Thay đổi database schema<br>- Cập nhật major version<br>- Thay đổi cấu hình network |
| **Approval** | CAB approval required |
| **Lead Time** | Tối thiểu 5 ngày làm việc |
| **Trong Soft Freeze** | ❌ Không được phép |
| **Trong Hard Freeze** | ❌ Không được phép |

### 3.3. Emergency Change

| Tiêu chí | Mô tả |
|----------|-------|
| **Định nghĩa** | Các thay đổi khẩn cấp để khắc phục sự cố nghiêm trọng đang ảnh hưởng đến dịch vụ |
| **Ví dụ** | - Hotfix cho security vulnerability đang bị khai thác<br>- Khắc phục sự cố gây downtime<br>- Patch khẩn cấp từ vendor |
| **Approval** | Emergency CAB (Change Manager + Technical Lead + On-call Manager) |
| **Lead Time** | Không áp dụng (ASAP) |
| **Trong Soft Freeze** | ✅ Được phép (với approval) |
| **Trong Hard Freeze** | ✅ Được phép (với approval cấp cao) |

---

## **4. CHÍNH SÁCH CHANGE FREEZE**

### 4.1. Nguyên tắc Chung

**4.1.1.** Tất cả Change Freeze periods phải được công bố trước ít nhất **30 ngày** trên Jira Calendar và thông báo qua email.

**4.1.2.** Change Freeze Calendar được review và cập nhật **hàng quý** bởi Change Manager với sự tham vấn của Account Managers.

**4.1.3.** Mọi thay đổi trong Freeze period đều phải tuân thủ Exception Process được quy định tại Mục 6.

**4.1.4.** Không có cá nhân nào được phép bypass quy trình Freeze mà không có phê duyệt bằng văn bản.

### 4.2. Các loại Freeze Period

#### 4.2.1. Hard Freeze

**Áp dụng khi:**
- Các sự kiện kinh doanh quan trọng nhất của khách hàng
- Ngày lễ lớn có traffic cao
- Các giai đoạn báo cáo tài chính bắt buộc

**Quy định:**
- Cấm hoàn toàn Normal Change và Standard Change
- Chỉ Emergency Change được xem xét với approval từ Director/VP trở lên
- Tất cả team phải có on-call coverage
- Không thực hiện maintenance định kỳ

#### 4.2.2. Soft Freeze

**Áp dụng khi:**
- Các ngày có traffic cao hơn bình thường
- Giai đoạn chuẩn bị trước Hard Freeze
- Các chiến dịch marketing quan trọng

**Quy định:**
- Cho phép Standard Change (pre-approved)
- Normal Change yêu cầu Exception approval
- Emergency Change được phép với approval thông thường
- Khuyến khích hoãn các thay đổi không khẩn cấp

### 4.3. Change Window (Cửa sổ thực hiện Change)

Ngoài các giai đoạn Freeze, việc thực hiện change phải tuân thủ các Change Window sau:

| Vertical | Preferred Window | Acceptable Window | Prohibited Window |
|----------|------------------|-------------------|-------------------|
| Securities | T7 12:00 - CN 18:00 | T2-T6: 18:00-06:00 | T2-T6: 08:30-16:30 |
| Insurance | Hàng ngày 02:00-05:00 | 23:00-06:00 | Không có (24/7 nhưng cần approval) |
| F&B | T2-T5: 02:00-06:00 | T2-T5: 06:00-10:00 | 11:00-14:00 và 18:00-21:00 hàng ngày; T7-CN cả ngày |
| Internal | Hàng ngày 22:00-06:00 | Bất kỳ | Không có |

---

## **5. LỊCH CHANGE FREEZE THEO VERTICAL**

### 5.1. Công ty Chứng khoán

#### 5.1.1. Hard Freeze cố định

| Sự kiện | Thời gian Freeze | Tần suất |
|---------|------------------|----------|
| Ngày giao dịch | 08:30 - 16:30 | T2-T6 hàng tuần |
| Ngày đáo hạn phái sinh | 00:00 ngày đáo hạn - 18:00 cùng ngày | Thứ 5 tuần thứ 3 hàng tháng |
| Kỳ báo cáo quý | 3 ngày làm việc cuối kỳ | Q1, Q2, Q3, Q4 |

#### 5.1.2. Soft Freeze

| Sự kiện | Thời gian Freeze |
|---------|------------------|
| Ngày chốt quyền (record date) mã VN30 | Ngày chốt quyền |
| IPO/Listing mới | Ngày giao dịch đầu tiên |

### 5.2. Công ty Bảo hiểm Phi nhân thọ

#### 5.2.1. Hard Freeze cố định

| Sự kiện | Thời gian Freeze | Ghi chú |
|---------|------------------|---------|
| Ngày lễ kéo dài (≥3 ngày) | 1 ngày trước - hết ngày lễ | Claim volume tăng cao |
| Mùa mưa bão | T8-T11: Soft freeze cho Claim module | Chỉ Standard Change |

#### 5.2.2. Soft Freeze

| Sự kiện | Thời gian Freeze |
|---------|------------------|
| Renewal campaign | Theo thông báo từ Customer |
| Cuối tháng | Ngày 28-31 hàng tháng (closing) |

### 5.3. Chuỗi F&B

#### 5.3.1. Hard Freeze cố định

| Sự kiện | Thời gian Freeze |
|---------|------------------|
| Tết Nguyên đán | 15 ngày trước - 7 ngày sau Tết |
| Lễ 30/4-1/5 | 28/4 - 2/5 |
| Lễ 2/9 | 1/9 - 3/9 |
| Giáng sinh & Năm mới | 22/12 - 2/1 |
| Cuối tuần | T6 18:00 - CN 23:00 |

#### 5.3.2. Soft Freeze

| Sự kiện | Thời gian Freeze |
|---------|------------------|
| Flash Sale/Campaign | Theo thông báo từ Customer (thường 3 ngày) |
| Peak hours hàng ngày | 11:00-14:00 và 18:00-21:00 |

### 5.4. Hệ thống Nội bộ

#### 5.4.1. Hard Freeze

| Sự kiện | Thời gian Freeze |
|---------|------------------|
| Kỳ quyết toán lương | Ngày 25-cuối tháng |
| Audit period | Theo thông báo từ Finance |

### 5.5. Lịch Freeze Hợp nhất năm [YYYY]

*(Đính kèm Phụ lục A: Calendar chi tiết)*

---

## **6. QUY TRÌNH EXCEPTION**

### 6.1. Điều kiện Áp dụng Exception

Exception chỉ được xem xét khi đáp ứng **ÍT NHẤT MỘT** trong các điều kiện sau:

1. **Security Critical**: Lỗ hổng bảo mật đang bị khai thác hoặc có nguy cơ cao
2. **Service Impact**: Sự cố đang gây ảnh hưởng đến dịch vụ khách hàng
3. **Regulatory Compliance**: Yêu cầu tuân thủ pháp luật có deadline cụ thể
4. **Customer Contractual**: Cam kết hợp đồng với khách hàng có deadline
5. **Revenue Critical**: Ảnh hưởng trực tiếp đến doanh thu với bằng chứng cụ thể

### 6.2. Quy trình Phê duyệt Exception

```
┌────────────────────────────────────────────────────────────────────┐
│                      QUY TRÌNH EXCEPTION                           │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  BƯỚC 1: Khởi tạo Request                                         │
│  ────────────────────────                                         │
│  • Requestor tạo Change Request trên Jira                         │
│  • Chọn "Exception Request" = Yes                                 │
│  • Điền đầy đủ Exception Justification Form (Phụ lục B)          │
│  • Timeline: Ngay khi xác định cần Exception                      │
│                         ↓                                          │
│  BƯỚC 2: Technical Review                                         │
│  ────────────────────────                                         │
│  • Technical Lead đánh giá Risk Assessment                        │
│  • Xác nhận Rollback Plan khả thi                                 │
│  • Estimate thời gian thực hiện và rollback                       │
│  • Timeline: Tối đa 4 giờ                                         │
│                         ↓                                          │
│  BƯỚC 3: Business Impact Review                                   │
│  ────────────────────────────                                     │
│  • Account Manager đánh giá Business Impact                       │
│  • Liên hệ Customer (nếu cần)                                     │
│  • Xác nhận Customer Notification Plan                            │
│  • Timeline: Tối đa 4 giờ                                         │
│                         ↓                                          │
│  BƯỚC 4: Approval                                                 │
│  ───────────────                                                  │
│  │ Soft Freeze Period │ Hard Freeze Period │                      │
│  │ Change Manager     │ Director/VP        │                      │
│  │ approval           │ approval required  │                      │
│  • Timeline: Tối đa 2 giờ                                         │
│                         ↓                                          │
│  BƯỚC 5: Pre-Implementation Checklist                             │
│  ───────────────────────────────────                              │
│  ☐ Rollback plan documented và tested                             │
│  ☐ On-call team notified và standby                               │
│  ☐ Customer notified (nếu applicable)                             │
│  ☐ Monitoring dashboard prepared                                  │
│  ☐ Communication channel established                              │
│                         ↓                                          │
│  BƯỚC 6: Implementation                                           │
│  ──────────────────────                                           │
│  • Thực hiện change với enhanced monitoring                       │
│  • Real-time update trên designated channel                       │
│  • Immediate rollback nếu có issue                                │
│                         ↓                                          │
│  BƯỚC 7: Post-Implementation                                      │
│  ───────────────────────────                                      │
│  • Verify change successful                                       │
│  • Monitor 30 phút sau change                                     │
│  • Update Jira ticket với kết quả                                 │
│  • Post-Implementation Review trong 24 giờ                        │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

### 6.3. Ma trận Phê duyệt

| Loại Freeze | Risk Level | Approver(s) Required | Max Approval Time |
|-------------|------------|---------------------|-------------------|
| Soft Freeze | Low | Change Manager | 2 giờ |
| Soft Freeze | Medium | Change Manager + Technical Lead | 4 giờ |
| Soft Freeze | High/Critical | Change Manager + Director | 4 giờ |
| Hard Freeze | Low | Director | 4 giờ |
| Hard Freeze | Medium | Director + CTO | 6 giờ |
| Hard Freeze | High/Critical | VP/CEO + CTO | 8 giờ |

### 6.4. Escalation Path

Nếu Approver không phản hồi trong thời gian quy định:

| Level | Contact | Escalate sau |
|-------|---------|--------------|
| L1 | Change Manager | - |
| L2 | Technical Director | 2 giờ |
| L3 | CTO | 4 giờ |
| L4 | CEO | 6 giờ |

---

## **7. VAI TRÒ VÀ TRÁCH NHIỆM**

### 7.1. RACI Matrix

| Hoạt động | Change Manager | Technical Lead | Account Manager | Developer | Director | Customer |
|-----------|:-------------:|:-------------:|:---------------:|:---------:|:--------:|:--------:|
| Xây dựng Change Freeze Calendar | **A/R** | C | C | I | A | C |
| Review và cập nhật Calendar | **A/R** | C | **R** | I | A | I |
| Submit Change Request | I | C | I | **R** | I | I |
| Technical Risk Assessment | C | **A/R** | I | C | I | I |
| Business Impact Assessment | C | I | **A/R** | I | C | C |
| Approve Standard Change | **A/R** | I | I | I | I | I |
| Approve Normal Change | **A/R** | **R** | **R** | I | I | I |
| Approve Emergency Change | **R** | **R** | C | I | **A** | I |
| Approve Exception Request | **R** | C | C | I | **A** | C |
| Implement Change | I | C | I | **A/R** | I | I |
| Monitor Change | C | **R** | I | **R** | I | I |
| Rollback Decision | **R** | **A/R** | C | R | I | I |
| Customer Communication | I | I | **A/R** | I | C | **R** |
| Post-Implementation Review | **A/R** | **R** | C | **R** | I | I |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

### 7.2. Chi tiết Trách nhiệm

#### 7.2.1. Change Manager

- Duy trì và cập nhật Change Freeze Calendar
- Chủ trì CAB meetings
- Phê duyệt Standard và Normal Changes
- Giám sát tuân thủ Change Policy
- Báo cáo Change metrics hàng tháng
- Điều phối Exception requests

#### 7.2.2. Technical Lead

- Thực hiện Technical Risk Assessment cho tất cả changes
- Review và approve Rollback Plans
- Đảm bảo technical feasibility
- Tham gia CAB cho Normal và Emergency Changes
- On-call escalation point

#### 7.2.3. Account Manager

- Thu thập Business Event Calendar từ khách hàng
- Đánh giá Business Impact của changes
- Điều phối Customer Communication
- Thu thập Customer Sign-off (khi cần)
- Cập nhật customer-specific freeze requirements

#### 7.2.4. Developer/Engineer

- Submit Change Requests đầy đủ thông tin
- Chuẩn bị và test Rollback Plan
- Thực hiện changes trong approved windows
- Monitor changes sau implementation
- Báo cáo issues ngay lập tức

#### 7.2.5. Director/VP

- Phê duyệt Exception Requests trong Hard Freeze
- Final escalation point
- Review và approve Policy changes
- Quarterly review của Change effectiveness

---

## **8. QUY TRÌNH THỰC HIỆN CHANGE**

### 8.1. Workflow tổng quan

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CHANGE REQUEST WORKFLOW                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐  │
│   │  Draft   │────▶│ Submitted│────▶│ Assessing│────▶│ Approved │  │
│   └──────────┘     └──────────┘     └──────────┘     └──────────┘  │
│                          │                │               │         │
│                          ▼                ▼               ▼         │
│                    ┌──────────┐     ┌──────────┐   ┌──────────┐    │
│                    │ Rejected │     │More Info │   │ Scheduled│    │
│                    └──────────┘     │ Required │   └──────────┘    │
│                                     └──────────┘         │         │
│                                                          ▼         │
│                                                    ┌──────────┐    │
│                                                    │Implementing   │
│                                                    └──────────┘    │
│                                                     │    │         │
│                                          ┌─────────┘    └────────┐ │
│                                          ▼                       ▼ │
│                                    ┌──────────┐           ┌──────────┐
│                                    │ Completed│           │ Rolled   │
│                                    └──────────┘           │  Back    │
│                                          │                └──────────┘
│                                          ▼                           │
│                                    ┌──────────┐                      │
│                                    │  Closed  │                      │
│                                    └──────────┘                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 8.2. Thông tin Bắt buộc trong Change Request

| Field | Bắt buộc | Mô tả |
|-------|:--------:|-------|
| Change Title | ✅ | Mô tả ngắn gọn về change |
| Change Type | ✅ | Standard / Normal / Emergency |
| Description | ✅ | Mô tả chi tiết về change |
| Reason/Justification | ✅ | Lý do cần thực hiện change |
| Affected Systems | ✅ | Hệ thống bị ảnh hưởng |
| Affected Customers | ✅ | Khách hàng bị ảnh hưởng |
| Risk Level | ✅ | Low / Medium / High / Critical |
| Risk Assessment Details | ✅ | Chi tiết đánh giá rủi ro |
| Planned Start Date/Time | ✅ | Thời gian bắt đầu dự kiến |
| Planned End Date/Time | ✅ | Thời gian kết thúc dự kiến |
| Implementation Plan | ✅ | Các bước thực hiện |
| Rollback Plan | ✅ | Các bước rollback |
| Rollback Time Estimate | ✅ | Thời gian dự kiến để rollback |
| Testing Evidence | ✅ (Normal/Emergency) | Link đến test results |
| Customer Notification | Conditional | Required nếu có customer impact |
| Exception Request | Conditional | Required nếu trong Freeze period |

### 8.3. Lead Time Requirements

| Change Type | Minimum Lead Time | Recommended Lead Time |
|-------------|-------------------|----------------------|
| Standard | 24 giờ | 3 ngày |
| Normal | 5 ngày làm việc | 10 ngày làm việc |
| Emergency | N/A | ASAP |
| Exception (Soft Freeze) | 12 giờ | 24 giờ |
| Exception (Hard Freeze) | 24 giờ | 48 giờ |

---

## **9. GIÁM SÁT VÀ BÁO CÁO**

### 9.1. Key Performance Indicators (KPIs)

| KPI | Mục tiêu | Đo lường | Tần suất |
|-----|----------|----------|----------|
| Change Success Rate | ≥ 95% | Successful Changes / Total Changes | Hàng tháng |
| Failed Change Rate | ≤ 5% | Failed Changes / Total Changes | Hàng tháng |
| Emergency Change Rate | ≤ 10% | Emergency Changes / Total Changes | Hàng tháng |
| Freeze Violation Rate | 0% | Unauthorized Changes in Freeze / Total | Hàng tháng |
| Exception Approval Rate | ≤ 5% | Approved Exceptions / Total Changes | Hàng tháng |
| Mean Time to Implement | ≤ 2 giờ (Standard) | Average implementation time | Hàng tháng |
| Rollback Rate | ≤ 3% | Rolled Back Changes / Total Changes | Hàng tháng |
| Change-Related Incidents | ≤ 2% | Incidents from Changes / Total Incidents | Hàng tháng |
| Lead Time Compliance | ≥ 90% | Changes meeting lead time / Total | Hàng tháng |

### 9.2. Báo cáo Định kỳ

| Báo cáo | Tần suất | Đối tượng | Nội dung |
|---------|----------|-----------|----------|
| Daily Change Summary | Hàng ngày | Operations Team | Changes scheduled/completed today |
| Weekly Change Report | Hàng tuần | Management | KPIs, upcoming freeze periods |
| Monthly Change Analysis | Hàng tháng | Leadership | Trend analysis, improvements |
| Quarterly Review | Hàng quý | Board/Stakeholders | Strategic review, policy updates |

### 9.3. Audit Trail

Tất cả các hoạt động sau phải được log và lưu trữ tối thiểu **3 năm**:
- Change request submissions
- Approval/rejection decisions
- Status transitions
- Exception requests và approvals
- Implementation start/end times
- Rollback events
- All comments và attachments

---

## **10. VI PHẠM VÀ XỬ LÝ**

### 10.1. Các Hành vi Vi phạm

| Mức độ | Hành vi | Ví dụ |
|--------|---------|-------|
| **Nghiêm trọng** | Thực hiện change trong Hard Freeze không có approval | Deploy code trong ngày đáo hạn phái sinh |
| **Nghiêm trọng** | Cố tình bypass quy trình approval | Trực tiếp deploy mà không tạo CR |
| **Trung bình** | Thực hiện change trong Soft Freeze không đúng loại | Deploy Normal Change trong Soft Freeze |
| **Trung bình** | Không tuân thủ Change Window | Deploy trong prohibited hours |
| **Nhẹ** | Submit CR không đủ thông tin | Thiếu rollback plan |
| **Nhẹ** | Không tuân thủ lead time | Submit CR muộn hơn quy định |

### 10.2. Hình thức Xử lý

| Mức độ Vi phạm | Lần 1 | Lần 2 | Lần 3+ |
|----------------|-------|-------|--------|
| Nghiêm trọng | Cảnh cáo bằng văn bản + Training bắt buộc | Đánh giá hiệu suất + Hạn chế quyền access | Xử lý kỷ luật theo quy định công ty |
| Trung bình | Nhắc nhở + Giải thích quy trình | Cảnh cáo bằng văn bản | Training bắt buộc + Review định kỳ |
| Nhẹ | Nhắc nhở miệng | Nhắc nhở bằng email | Cảnh cáo + Training |

### 10.3. Incident Response

Khi phát hiện vi phạm Freeze policy:

1. **Immediate**: Đánh giá impact và quyết định có cần rollback
2. **Within 1 hour**: Thông báo Change Manager và relevant stakeholders
3. **Within 4 hours**: Document incident trong Jira
4. **Within 24 hours**: Root cause analysis
5. **Within 1 week**: Corrective actions và preventive measures

---

## **11. PHỤ LỤC**

### Phụ lục A: Change Freeze Calendar năm [YYYY]

*(Đính kèm file Excel hoặc link đến Jira Calendar)*

### Phụ lục B: Exception Request Form

```
═══════════════════════════════════════════════════════════════════
                    EXCEPTION REQUEST FORM
═══════════════════════════════════════════════════════════════════

PHẦN 1: THÔNG TIN CHUNG
───────────────────────────────────────────────────────────────────
Change Request ID:      [________________]
Requestor:              [________________]
Date:                   [________________]
Freeze Period:          [________________]
Freeze Type:            [ ] Hard Freeze    [ ] Soft Freeze

PHẦN 2: JUSTIFICATION
───────────────────────────────────────────────────────────────────
Lý do cần Exception (chọn ít nhất 1):
[ ] Security Critical - Mô tả: ________________________________
[ ] Service Impact - Mô tả: ___________________________________
[ ] Regulatory Compliance - Deadline: _________________________
[ ] Customer Contractual - Contract ref: ______________________
[ ] Revenue Critical - Estimated impact: ______________________

Chi tiết giải thích:
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________

PHẦN 3: RISK MITIGATION
───────────────────────────────────────────────────────────────────
Rollback Plan đã tested:           [ ] Yes  [ ] No
Estimated Rollback Time:           [____] phút
On-call team confirmed:            [ ] Yes  [ ] No
Customer notified:                 [ ] Yes  [ ] No  [ ] N/A
Monitoring prepared:               [ ] Yes  [ ] No

PHẦN 4: APPROVAL
───────────────────────────────────────────────────────────────────
Technical Lead:
  Name: _________________ Signature: _________ Date: __________
  [ ] Approved  [ ] Rejected  
  Comments: ________________________________________________

Account Manager:
  Name: _________________ Signature: _________ Date: __________
  [ ] Approved  [ ] Rejected
  Comments: ________________________________________________

Change Manager:
  Name: _________________ Signature: _________ Date: __________
  [ ] Approved  [ ] Rejected
  Comments: ________________________________________________

Director/VP (Hard Freeze only):
  Name: _________________ Signature: _________ Date: __________
  [ ] Approved  [ ] Rejected
  Comments: ________________________________________________

═══════════════════════════════════════════════════════════════════
```

### Phụ lục C: Risk Assessment Matrix

| Impact ↓ / Likelihood → | Rare (1) | Unlikely (2) | Possible (3) | Likely (4) | Almost Certain (5) |
|-------------------------|:--------:|:------------:|:------------:|:----------:|:------------------:|
| **Critical (5)** | Medium | Medium | High | Critical | Critical |
| **Major (4)** | Low | Medium | Medium | High | Critical |
| **Moderate (3)** | Low | Low | Medium | Medium | High |
| **Minor (2)** | Low | Low | Low | Medium | Medium |
| **Negligible (1)** | Low | Low | Low | Low | Medium |

**Risk Level Actions:**
- **Low**: Standard approval process
- **Medium**: Technical Lead review required
- **High**: CAB approval + enhanced monitoring
- **Critical**: Director approval + customer notification + dedicated support

### Phụ lục D: Customer Communication Templates

#### Template 1: Planned Maintenance Notification

```
Subject: [COMPANY] Scheduled Maintenance Notification - [DATE]

Kính gửi Quý Khách hàng,

Chúng tôi xin thông báo về kế hoạch bảo trì hệ thống như sau:

Thời gian: [START TIME] - [END TIME] ngày [DATE]
Hệ thống ảnh hưởng: [SYSTEMS]
Mức độ ảnh hưởng: [IMPACT DESCRIPTION]

Trong thời gian này, [DESCRIBE IMPACT TO CUSTOMER].

Chúng tôi sẽ nỗ lực hoàn thành sớm nhất có thể và thông báo 
ngay khi hệ thống hoạt động bình thường trở lại.

Mọi thắc mắc xin liên hệ: [CONTACT]

Trân trọng,
[COMPANY NAME]
```

#### Template 2: Emergency Change Notification

```
Subject: [URGENT] Emergency Maintenance - [SYSTEM] - [DATE/TIME]

Kính gửi Quý Khách hàng,

Do [BRIEF REASON], chúng tôi cần thực hiện bảo trì khẩn cấp:

Thời gian: [START TIME] (dự kiến [DURATION])
Ảnh hưởng: [IMPACT]

Chúng tôi sẽ cập nhật tình hình liên tục qua [CHANNEL].

Hotline hỗ trợ: [NUMBER]

Trân trọng,
[COMPANY NAME]
```

### Phụ lục E: Checklist Pre-Implementation

```
PRE-IMPLEMENTATION CHECKLIST
═══════════════════════════════════════════════════════════════

Change Request ID: ________________
Implementer: ________________
Date/Time: ________________

TRƯỚC KHI BẮT ĐẦU:
[ ] Change Request đã được Approved
[ ] Planned time nằm trong Change Window
[ ] Không trong Freeze Period (hoặc có Exception approval)
[ ] Rollback plan đã review và test
[ ] Backup đã thực hiện (nếu applicable)
[ ] Team members đã notify và standby
[ ] Customer đã notify (nếu required)
[ ] Monitoring dashboard đã mở
[ ] Communication channel đã setup
[ ] Emergency contacts đã xác nhận available

TRONG KHI THỰC HIỆN:
[ ] Update status trên Jira = "Implementing"
[ ] Follow implementation plan từng bước
[ ] Log mọi actions và observations
[ ] Monitor system health continuously
[ ] Report progress theo schedule

SAU KHI HOÀN THÀNH:
[ ] Verify change thành công
[ ] Run smoke tests
[ ] Monitor 30 phút post-change
[ ] Update Jira với kết quả
[ ] Notify stakeholders
[ ] Close change request

Implementer Sign-off: ________________ Date: ________________
Reviewer Sign-off: ________________ Date: ________________
```

---

## **PHÊ DUYỆT TÀI LIỆU**

| Vai trò | Họ tên | Chữ ký | Ngày |
|---------|--------|--------|------|
| Soạn thảo | | | |
| Review kỹ thuật | | | |
| Review nghiệp vụ | | | |
| Phê duyệt | | | |

---

**--- HẾT TÀI LIỆU ---**

---

Bạn có cần tôi bổ sung thêm phần nào không? Ví dụ như chi tiết hơn về Jira workflow configuration, hoặc các template email tiếng Anh, hoặc SLA matrix cho từng loại khách hàng?