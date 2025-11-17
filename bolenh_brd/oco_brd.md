# Lệnh OCO (One Cancels the Other) - Tài liệu Yêu cầu Nghiệp vụ (BRD)

---

## QUẢN LÝ TÀI LIỆU

| Thông tin | Chi tiết |
|-----------|----------|
| **Tên tài liệu** | Business Requirements Document - Lệnh OCO (One Cancels the Other) |
| **Phiên bản** | 1.2 |
| **Ngày tạo** | 17/11/2025 |
| **Người tạo** | Business Analyst |
| **Người phê duyệt** | Product Owner |
| **Trạng thái** | Draft |

### Lịch sử phiên bản

| Phiên bản | Ngày | Người thay đổi | Mô tả thay đổi |
|-----------|------|----------------|----------------|
| 1.0 | 17/11/2025 | Business Analyst | Phiên bản khởi tạo |
| 1.1 | 17/11/2025 | Business Analyst | Revise: Căn chỉnh theo template, thêm IPO Limit Match, rút gọn PROCESS sections |
| 1.2 | 17/11/2025 | Business Analyst | Loại bỏ chức năng sửa lệnh OCO theo yêu cầu nghiệp vụ |

### Danh sách phân phối

| Vai trò | Họ tên | Email |
|---------|--------|-------|
| Product Owner | [Tên PO] | [Email] |
| Business Analyst | [Tên BA] | [Email] |
| Tech Lead | [Tên Tech Lead] | [Email] |
| QA Lead | [Tên QA Lead] | [Email] |
| Trading Operations Manager | [Tên Operations] | [Email] |
| Compliance Officer | [Tên Compliance] | [Email] |

---

## TÓM TẮT ĐIỀU HÀNH

Lệnh OCO (One Cancels the Other) là tính năng giao dịch nâng cao cho phép nhà đầu tư đặt đồng thời hai lệnh điều kiện (Limit Order và Stop-Limit Order), trong đó khi một lệnh được khớp thì lệnh còn lại tự động hủy. Tính năng này giải quyết bài toán quản lý rủi ro và tối ưu hóa điểm vào/ra lệnh trong điều kiện thị trường biến động, giúp nhà đầu tư không cần theo dõi thị trường liên tục.

Giá trị kinh doanh: Tăng trải nghiệm người dùng, thu hút nhà đầu tư chuyên nghiệp, tăng tính cạnh tranh của nền tảng so với các sàn giao dịch khác. Tính năng hướng đến trader có kinh nghiệm, trader chuyên nghiệp và các nhà đầu tư muốn tự động hóa chiến lược giao dịch.

---

## 1. GIỚI THIỆU

### 1.1 Mục đích tài liệu

Tài liệu này mô tả chi tiết các yêu cầu nghiệp vụ cho tính năng **Lệnh OCO (One Cancels the Other)**. Tài liệu được sử dụng bởi các nhóm phát triển, kiểm thử, vận hành và compliance để hiểu rõ yêu cầu và triển khai chính xác tính năng giao dịch phức tạp này.

### 1.2 Phạm vi

**Trong phạm vi (In Scope):**
- Tạo lệnh OCO (chiều mua và chiều bán)
- Hủy lệnh OCO
- Theo dõi và kích hoạt tự động lệnh Stop-Limit khi điều kiện thỏa mãn
- Hủy tự động lệnh còn lại khi một lệnh được khớp
- Quản lý trạng thái lệnh OCO (Pending, Partially Filled, Filled, Cancelled, Rejected)
- Hiển thị danh sách lệnh OCO
- Thông báo trạng thái lệnh qua hệ thống notification
- Audit log đầy đủ cho các giao dịch OCO
- Validation nghiệp vụ (giá, khối lượng, điều kiện ràng buộc)

**Ngoài phạm vi (Out of Scope):**
- Lệnh OCO cho margin trading/futures
- Lệnh OCO cho thị trường phái sinh
- Lệnh OCO kết hợp với các loại lệnh khác (Trailing Stop, Iceberg)
- Mobile app implementation (phase sau)
- Backtesting và simulation OCO orders
- API public cho bên thứ ba
- OCO cho multiple symbols (basket order)

### 1.3 Định nghĩa và Thuật ngữ

| Thuật ngữ | Định nghĩa | Tiếng Anh |
|-----------|-----------|-----------|
| OCO | Lệnh kết hợp hai lệnh điều kiện, khi một lệnh khớp thì lệnh kia tự động hủy | One Cancels the Other |
| Lệnh giới hạn | Lệnh mua/bán tại mức giá cụ thể hoặc tốt hơn | Limit Order |
| Lệnh dừng giới hạn | Lệnh chỉ được kích hoạt khi giá chạm mức Stop, sau đó đặt lệnh Limit | Stop-Limit Order |
| Giá kích hoạt | Mức giá để kích hoạt lệnh Stop-Limit | Stop Price / Trigger Price |
| Giá giới hạn | Mức giá tối đa (mua) hoặc tối thiểu (bán) sau khi lệnh Stop được kích hoạt | Limit Price |
| Khớp lệnh | Quá trình thực hiện lệnh khi giá và khối lượng thỏa mãn | Order Matching |
| Giá thị trường | Giá giao dịch hiện tại của chứng khoán | Market Price |
| Sub-order | Lệnh con trong lệnh OCO (Limit hoặc Stop-Limit) | Sub-order |
| Master Order | Lệnh OCO chính quản lý 2 sub-orders | Master Order |

### 1.4 Tài liệu tham khảo

- Product Requirements Document - Lệnh OCO (oco_prd.md)
- Trading Platform Architecture Design Document
- Order Matching Engine Specification
- Risk Management Policy Document
- Quy định giao dịch chứng khoán HOSE/HNX/UPCOM
- ISO 20022 - Financial Services Messages

---

## 2. MỤC TIÊU KINH DOANH

### 2.1 Vấn đề cần giải quyết

**Vấn đề hiện tại:**
- Nhà đầu tư phải theo dõi thị trường liên tục để đặt lệnh tại thời điểm phù hợp
- Không thể đồng thời đặt lệnh chốt lời và cắt lỗ mà không bị trùng lặp khối lượng
- Khó khăn trong việc bắt cả hai cơ hội: mua giá thấp khi giảm HOẶC bắt đà tăng khi vượt kháng cự
- Thiếu công cụ tự động hóa để quản lý rủi ro hiệu quả
- Cạnh tranh với các sàn khác đã có tính năng giao dịch nâng cao

**Đối tượng bị ảnh hưởng:**
- Nhà đầu tư cá nhân: Không có công cụ quản lý rủi ro tự động
- Trader chuyên nghiệp: Thiếu tính năng để thực hiện chiến lược phức tạp
- Sàn giao dịch: Mất cạnh tranh, giảm thanh khoản và trading volume

### 2.2 Mục tiêu nghiệp vụ

| Mục tiêu | Chỉ số đo lường | Mục tiêu cụ thể | Thời hạn |
|----------|----------------|-----------------|----------|
| Tăng số lượng lệnh đặt | Số lệnh OCO/ngày | 1,000+ lệnh OCO/ngày | 3 tháng sau launch |
| Tăng trading volume | % tăng volume | +15% trading volume | 6 tháng sau launch |
| Tăng retention rate | % người dùng quay lại | +20% monthly active traders | 6 tháng sau launch |
| Giảm manual monitoring | Survey feedback | 70% users hài lòng với tính năng | 3 tháng sau launch |
| Tăng tính cạnh tranh | Market comparison | Feature parity với top 3 competitors | Ngay khi launch |

---

## 3. CÁC BÊN LIÊN QUAN

### 3.1 Stakeholders nghiệp vụ

| Vai trò | Họ tên | Trách nhiệm |
|---------|--------|-------------|
| Product Owner | [Tên PO] | Phê duyệt requirements, ưu tiên tính năng, quyết định business logic |
| Trading Operations Manager | [Tên] | Định nghĩa quy trình trading, validation rules, risk management |
| Compliance Officer | [Tên] | Đảm bảo tuân thủ quy định giao dịch, audit requirements |
| Marketing Manager | [Tên] | Go-to-market strategy, user education, feature communication |
| Customer Support Lead | [Tên] | Đào tạo support team, xử lý escalation, user feedback |

### 3.2 Stakeholders kỹ thuật

| Vai trò | Họ tên | Trách nhiệm |
|---------|--------|-------------|
| Tech Lead | [Tên] | Thiết kế kiến trúc, review technical approach, performance optimization |
| Backend Lead | [Tên] | Implement order processing logic, integration với matching engine |
| Frontend Lead | [Tên] | Implement UI/UX cho OCO order placement và management |
| QA Lead | [Tên] | Test strategy, test cases, performance testing, UAT |
| DevOps Lead | [Tên] | Deployment, monitoring, infrastructure scaling |
| Security Lead | [Tên] | Security review, penetration testing, vulnerability assessment |

### 3.3 Người dùng cuối

- **Trader chuyên nghiệp**: Có kinh nghiệm giao dịch >2 năm, sử dụng phân tích kỹ thuật, cần công cụ tự động hóa
- **Nhà đầu tư tích cực**: Giao dịch 3-5 lần/tuần, hiểu về các loại lệnh điều kiện, muốn quản lý rủi ro tốt hơn
- **Swing traders**: Giữ vị thế vài ngày đến vài tuần, cần đặt lệnh tự động để không phải theo dõi liên tục

---

## 4. YÊU CẦU CHỨC NĂNG

### 4.1 Tổng quan tính năng

Lệnh OCO cho phép người dùng đặt đồng thời hai lệnh điều kiện cho cùng một mã chứng khoán với cùng khối lượng:
1. **Limit Order**: Lệnh giới hạn đợi giá chạm mức mong muốn
2. **Stop-Limit Order**: Lệnh dừng giới hạn được kích hoạt khi giá chạm mức Stop, sau đó đặt lệnh Limit

**Cơ chế hoạt động:**
- Khi Limit Order được khớp → Hủy Stop-Limit Order
- Khi Stop-Limit Order được kích hoạt và khớp → Hủy Limit Order
- Người dùng có thể chủ động hủy toàn bộ lệnh OCO
- Hệ thống theo dõi giá real-time để kích hoạt Stop-Limit Order

**Hai loại lệnh OCO:**
1. **OCO Mua**: Mua ở giá thấp (Limit) HOẶC mua khi vượt kháng cự (Stop-Limit)
2. **OCO Bán**: Bán chốt lời ở giá cao (Limit) HOẶC bán cắt lỗ khi phá hỗ trợ (Stop-Limit)

### 4.2 User Stories

#### Epic: Quản lý lệnh OCO

| ID | User Story | Độ ưu tiên | Acceptance Criteria |
|----|------------|------------|---------------------|
| US-001 | Là trader, tôi muốn đặt lệnh OCO mua để có thể mua ở giá thấp hoặc bắt đà tăng khi vượt kháng cự | Must Have | • Nhập đầy đủ symbol, volume, Price, Stop, Limit<br>• Validate Price < giá hiện tại < Stop<br>• Validate Limit >= Stop<br>• Tạo thành công 2 sub-orders<br>• Hiển thị xác nhận với chi tiết đầy đủ |
| US-002 | Là trader, tôi muốn đặt lệnh OCO bán để chốt lời hoặc cắt lỗ tự động | Must Have | • Nhập đầy đủ symbol, volume, Price, Stop, Limit<br>• Validate Price > giá hiện tại > Stop<br>• Validate Limit <= Stop<br>• Check đủ khối lượng trong tài khoản<br>• Tạo thành công 2 sub-orders |
| US-003 | Là trader, tôi muốn xem danh sách tất cả lệnh OCO đang active để theo dõi | Must Have | • Hiển thị bảng danh sách lệnh OCO<br>• Filter theo symbol, status, date range<br>• Hiển thị đầy đủ thông tin: symbol, side, prices, status<br>• Real-time update khi có thay đổi |
| US-004 | Là trader, tôi muốn hủy lệnh OCO trước khi khớp để thay đổi chiến lược | Must Have | • Button "Hủy" trên từng lệnh OCO<br>• Confirm popup trước khi hủy<br>• Hủy thành công cả 2 sub-orders<br>• Update status sang "Cancelled"<br>• Notification hủy thành công |
| US-005 | Là trader, tôi muốn nhận thông báo khi lệnh OCO được khớp hoặc hủy | Must Have | • Push notification khi Limit Order khớp<br>• Push notification khi Stop-Limit kích hoạt<br>• Push notification khi Stop-Limit khớp<br>• Email notification (optional setting)<br>• In-app notification history |
| US-006 | Là trader, tôi muốn xem chi tiết lịch sử lệnh OCO để review chiến lược | Should Have | • Màn hình Order History bao gồm OCO orders<br>• Chi tiết đầy đủ: thời gian tạo, khớp, hủy<br>• Thông tin giá tại thời điểm khớp<br>• Export history ra CSV |
| US-007 | Là operations manager, tôi muốn có audit log đầy đủ cho các lệnh OCO để compliance | Must Have | • Log tất cả hành động: create, cancel, match<br>• Log bao gồm: user_id, timestamp, action, old_value, new_value<br>• Immutable audit trail<br>• Có thể query theo user, date, order_id |
| US-008 | Là system admin, tôi muốn monitor performance của OCO matching engine | Should Have | • Dashboard hiển thị số lệnh OCO active<br>• Latency của stop trigger detection<br>• Failed orders và error rate<br>• Alert khi performance degradation |

### 4.3 Yêu cầu chi tiết

#### 4.3.1 Chức năng 1: Tạo lệnh OCO Mua

**Mô tả**: Cho phép người dùng tạo lệnh OCO mua với Limit Order (mua giá thấp) và Stop-Limit Order (mua khi vượt kháng cự)

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. User chọn symbol, nhập volume, chọn loại lệnh "OCO Buy"
2. User nhập 3 tham số giá: Price (giá giới hạn mua), Stop (giá kích hoạt), Limit (giá giới hạn sau khi kích hoạt)
3. Hệ thống validate các điều kiện nghiệp vụ
4. Hệ thống kiểm tra buying power
5. Tạo master OCO order và 2 sub-orders (Limit và Stop-Limit)
6. Gửi Limit Order vào order book
7. Lưu Stop-Limit Order ở trạng thái "Pending Trigger"
8. Bắt đầu monitor giá thị trường để kích hoạt Stop-Limit
9. Hiển thị confirmation và update UI

**Business Rules**:
- BR-001: Price phải nhỏ hơn giá thị trường hiện tại
- BR-002: Stop phải lớn hơn giá thị trường hiện tại
- BR-003: Limit phải >= Stop (có thể bằng hoặc cao hơn)
- BR-004: Price < Current Market Price < Stop
- BR-005: Buying power phải đủ cho khối lượng × max(Price, Limit)

**Validation Rules**:

| Trường | Quy tắc validate | Thông báo lỗi |
|--------|------------------|---------------|
| symbol | Mã CK hợp lệ, đang giao dịch | "Mã chứng khoán không hợp lệ hoặc tạm ngưng giao dịch" |
| volume | > 0, là bội số của 100 | "Khối lượng phải lớn hơn 0 và là bội số của 100" |
| Price | > 0, < market_price, trong biên độ dao động | "Giá Price phải nhỏ hơn giá thị trường và trong biên độ cho phép" |
| Stop | > market_price, trong biên độ dao động | "Giá Stop phải lớn hơn giá thị trường" |
| Limit | >= Stop | "Giá Limit phải lớn hơn hoặc bằng giá Stop" |

#### 4.3.2 Chức năng 2: Tạo lệnh OCO Bán

**Mô tả**: Cho phép người dùng tạo lệnh OCO bán với Limit Order (bán chốt lời) và Stop-Limit Order (bán cắt lỗ)

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. User chọn symbol, nhập volume, chọn loại lệnh "OCO Sell"
2. User nhập 3 tham số giá: Price (giá chốt lời), Stop (giá kích hoạt cắt lỗ), Limit (giá tối thiểu bán)
3. Hệ thống validate các điều kiện nghiệp vụ
4. Hệ thống kiểm tra khối lượng sở hữu
5. Tạo master OCO order và 2 sub-orders (Limit và Stop-Limit)
6. Gửi Limit Order vào order book
7. Lưu Stop-Limit Order ở trạng thái "Pending Trigger"
8. Bắt đầu monitor giá thị trường để kích hoạt Stop-Limit
9. Hold volume để tránh oversell
10. Hiển thị confirmation và update UI

**Business Rules**:
- BR-006: Price phải lớn hơn giá thị trường hiện tại
- BR-007: Stop phải nhỏ hơn giá thị trường hiện tại
- BR-008: Limit phải <= Stop (có thể bằng hoặc thấp hơn)
- BR-009: Stop < Current Market Price < Price
- BR-010: Khối lượng sở hữu phải >= volume đặt lệnh
- BR-011: Khối lượng đã hold (cho các lệnh khác) phải được tính vào

**Validation Rules**:

| Trường | Quy tắc validate | Thông báo lỗi |
|--------|------------------|---------------|
| symbol | Mã CK hợp lệ, đang giao dịch | "Mã chứng khoán không hợp lệ hoặc tạm ngưng giao dịch" |
| volume | > 0, là bội số của 100, <= available volume | "Khối lượng không hợp lệ hoặc vượt quá khối lượng sở hữu" |
| Price | > market_price, trong biên độ dao động | "Giá Price phải lớn hơn giá thị trường" |
| Stop | < market_price, trong biên độ dao động | "Giá Stop phải nhỏ hơn giá thị trường" |
| Limit | <= Stop | "Giá Limit phải nhỏ hơn hoặc bằng giá Stop" |

#### 4.3.3 Chức năng 3: Kích hoạt Stop-Limit Order

**Mô tả**: Hệ thống tự động kích hoạt Stop-Limit Order khi giá thị trường chạm hoặc vượt qua mức Stop

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. Hệ thống nhận price tick từ market data feed
2. Kiểm tra tất cả Stop-Limit orders đang "Pending Trigger"
3. So sánh giá hiện tại với Stop price
4. Nếu điều kiện trigger thỏa mãn → Kích hoạt Stop-Limit Order
5. Đặt Limit Order vào order book với giá = Limit
6. Hủy Limit Order ban đầu của OCO
7. Update trạng thái OCO master order
8. Gửi notification cho user
9. Ghi audit log

**Business Rules**:
- BR-012: OCO Mua - Trigger khi market_price >= Stop
- BR-013: OCO Bán - Trigger khi market_price <= Stop
- BR-014: Sau khi trigger, Stop-Limit trở thành Limit Order bình thường
- BR-015: Phải hủy Limit Order còn lại trước khi đặt Stop-Limit Order
- BR-016: Nếu hủy Limit Order thất bại → Rollback, không trigger Stop-Limit

**Validation Rules**:

| Điều kiện | Quy tắc | Hành động khi lỗi |
|-----------|---------|-------------------|
| Order status | OCO phải ở trạng thái Active | Bỏ qua trigger |
| Limit Order status | Limit Order phải đang Pending hoặc Partial Filled | Xử lý partial fill, hủy phần còn lại |
| Market status | Thị trường đang mở cửa | Delay trigger đến khi market mở lại |

#### 4.3.4 Chức năng 4: Hủy lệnh OCO

**Mô tả**: Cho phép người dùng hủy lệnh OCO và tất cả sub-orders liên quan

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. User click "Hủy" trên lệnh OCO
2. Hiển thị confirmation dialog
3. User xác nhận hủy
4. Hệ thống hủy Limit Order (nếu đang pending)
5. Hệ thống hủy Stop-Limit Order (nếu đang pending trigger)
6. Nếu một order đã partially filled → Chỉ hủy phần còn lại
7. Release held volume (đối với lệnh bán)
8. Update trạng thái OCO master order sang "Cancelled"
9. Gửi notification
10. Ghi audit log

**Business Rules**:
- BR-017: Chỉ có thể hủy lệnh OCO ở trạng thái "Pending" hoặc "Partially Filled"
- BR-018: Không thể hủy lệnh đã "Filled" hoặc "Rejected"
- BR-019: Nếu một sub-order đã filled → Chỉ hủy sub-order còn lại
- BR-020: Phải hủy thành công cả 2 sub-orders, nếu một cái fail → Rollback

**Validation Rules**:

| Điều kiện | Quy tắc | Thông báo lỗi |
|-----------|---------|---------------|
| Order status | Phải là Pending hoặc Partially Filled | "Không thể hủy lệnh đã hoàn thành hoặc bị từ chối" |
| Market status | Thị trường đang mở cửa (hoặc ATO/ATC) | "Không thể hủy lệnh ngoài giờ giao dịch" |
| User permission | User phải là owner của lệnh | "Không có quyền hủy lệnh này" |

### 4.4 Quy tắc nghiệp vụ tổng quát

| ID | Quy tắc | Hành động khi vi phạm |
|----|---------|----------------------|
| BR-001 | OCO Mua: Price < Market Price | Từ chối tạo lệnh, hiển thị error message |
| BR-002 | OCO Mua: Stop > Market Price | Từ chối tạo lệnh, hiển thị error message |
| BR-003 | OCO Mua: Limit >= Stop | Từ chối tạo lệnh, hiển thị error message |
| BR-004 | OCO Mua: Price < Market < Stop | Từ chối tạo lệnh, hiển thị error message |
| BR-005 | Buying power đủ cho max(Price, Limit) × Volume | Từ chối tạo lệnh, thông báo "Không đủ sức mua" |
| BR-006 | OCO Bán: Price > Market Price | Từ chối tạo lệnh, hiển thị error message |
| BR-007 | OCO Bán: Stop < Market Price | Từ chối tạo lệnh, hiển thị error message |
| BR-008 | OCO Bán: Limit <= Stop | Từ chối tạo lệnh, hiển thị error message |
| BR-009 | OCO Bán: Stop < Market < Price | Từ chối tạo lệnh, hiển thị error message |
| BR-010 | Available volume >= Order volume | Từ chối tạo lệnh, thông báo "Không đủ khối lượng" |
| BR-011 | Tính held volume cho các lệnh khác | Include trong available volume calculation |
| BR-012 | Trigger OCO Mua khi Market >= Stop | Kích hoạt Stop-Limit Order |
| BR-013 | Trigger OCO Bán khi Market <= Stop | Kích hoạt Stop-Limit Order |
| BR-014 | Stop-Limit sau khi trigger = Limit Order | Đặt vào order book như lệnh thường |
| BR-015 | Hủy Limit Order trước khi trigger Stop-Limit | Đảm bảo atomicity |
| BR-016 | Rollback nếu hủy Limit thất bại | Giữ nguyên trạng thái, log error |
| BR-017 | Chỉ hủy được lệnh Pending/Partially Filled | Từ chối request, thông báo lý do |
| BR-018 | Không hủy được lệnh Filled/Rejected | Từ chối request |
| BR-019 | Một sub-order filled → Hủy sub-order còn lại | Tự động hủy, gửi notification |
| BR-020 | Cancel phải atomic cho cả 2 sub-orders | Rollback nếu một cái fail |
| BR-021 | Một symbol chỉ có tối đa 10 lệnh OCO active | Từ chối tạo mới, thông báo "Vượt quá giới hạn lệnh" |
| BR-022 | OCO order expiry: End of trading day (EOD) | Tự động hủy lệnh chưa khớp vào cuối phiên |
| BR-023 | Matching priority: Time priority | FIFO - First In First Out |
| BR-024 | Market halted → Pause trigger monitoring | Resume khi market mở lại |

### 4.5 Workflow & Process Flow

```
=== LUỒNG TẠO LỆNH OCO MUA ===

User Input
    ↓
Validate Input (symbol, volume, Price, Stop, Limit)
    ↓
Check Business Rules (BR-001 đến BR-005)
    ↓
Check Buying Power
    ↓
[Pass] → Create OCO Master Order
    ↓
Create Limit Order (Price) → Submit to Order Book
    ↓
Create Stop-Limit Order (Stop, Limit) → Status: Pending Trigger
    ↓
Start Market Price Monitoring
    ↓
Return Success Response + Order Details

[Fail tại bất kỳ bước nào] → Return Error → Rollback


=== LUỒNG KÍCH HOẠT STOP-LIMIT ===

Market Price Update Event
    ↓
Query all OCO orders with Pending Trigger Stop-Limit
    ↓
For each Stop-Limit:
    If (Side = BUY AND Market Price >= Stop) OR
       (Side = SELL AND Market Price <= Stop)
    ↓
    Cancel Limit Order (sub-order còn lại)
        ↓ [Success]
    Submit Stop-Limit as regular Limit Order to Order Book
        ↓
    Update OCO Master Status
        ↓
    Send Notification
        ↓
    Write Audit Log


=== LUỒNG KHỚP LỆNH VÀ TỰ ĐỘNG HỦY ===

Limit Order Matched (Full or Partial)
    ↓
Check if order belongs to OCO
    ↓ [Yes]
Get OCO Master Order
    ↓
If (Fully Filled)
    ↓
    Cancel other sub-order (Stop-Limit)
    ↓
    Update OCO Master Status = "Filled"
    ↓
    Release held resources
    ↓
    Send Notification
    ↓
    Write Audit Log
Else (Partially Filled)
    ↓
    Update Filled Quantity
    ↓
    Keep monitoring


=== LUỒNG HỦY THỦ CÔNG ===

User Click "Cancel OCO"
    ↓
Show Confirmation Dialog
    ↓
User Confirm
    ↓
Begin Transaction
    ↓
Cancel Limit Order
    ↓ [Success]
Cancel Stop-Limit Order
    ↓ [Success]
Update OCO Master Status = "Cancelled"
    ↓
Release Held Volume (if sell order)
    ↓
Commit Transaction
    ↓
Send Notification
    ↓
Write Audit Log

[Fail at any step] → Rollback Transaction → Return Error
```

---

## 5. YÊU CẦU DỮ LIỆU

### 5.1 Input Specification

#### 5.1.1 Input cho tạo lệnh OCO

| Trường Input | Nguồn | Kiểu dữ liệu | Bắt buộc | Validation | Giá trị mặc định |
|--------------|-------|--------------|----------|------------|------------------|
| symbol | User | String | Có | Mã CK hợp lệ, max 10 ký tự | - |
| side | User | Enum | Có | "BUY" hoặc "SELL" | - |
| volume | User | Integer | Có | > 0, bội số 100, max 999,999,900 | - |
| price | User | Decimal | Có | > 0, 2 chữ số thập phân, trong biên độ | - |
| stop_price | User | Decimal | Có | > 0, 2 chữ số thập phân, trong biên độ | - |
| limit_price | User | Decimal | Có | > 0, 2 chữ số thập phân, trong biên độ | - |
| account_id | System | String | Có | UUID format | Current user account |
| user_id | System | String | Có | UUID format | Current logged-in user |
| order_source | System | Enum | Có | "WEB", "MOBILE", "API" | "WEB" |
| created_at | System | Timestamp | Có | ISO 8601 format | Server timestamp |

#### 5.1.2 Input cho hủy lệnh OCO

| Trường Input | Nguồn | Kiểu dữ liệu | Bắt buộc | Validation | Giá trị mặc định |
|--------------|-------|--------------|----------|------------|------------------|
| oco_order_id | User/System | String | Có | UUID, must exist | - |
| cancelled_by | System | String | Có | UUID format | Current user |
| cancellation_reason | User | String | Không | Max 500 ký tự | "User cancelled" |

### 5.2 Output Specification

#### 5.2.1 Response khi tạo lệnh OCO thành công

| Trường Output | Kiểu dữ liệu | Mô tả | Ví dụ |
|---------------|--------------|-------|-------|
| oco_order_id | String | ID của OCO master order | "OCO-20251117-001234" |
| status | String | Trạng thái lệnh OCO | "PENDING" |
| symbol | String | Mã chứng khoán | "VN30F2312" |
| side | String | Chiều lệnh | "BUY" |
| volume | Integer | Khối lượng | 500 |
| limit_order | Object | Thông tin Limit Order | {...} |
| limit_order.order_id | String | ID của Limit Order | "LO-20251117-001234-1" |
| limit_order.price | Decimal | Giá Limit Order | 40000.00 |
| limit_order.status | String | Trạng thái | "PENDING" |
| stop_limit_order | Object | Thông tin Stop-Limit Order | {...} |
| stop_limit_order.order_id | String | ID của Stop-Limit Order | "SL-20251117-001234-2" |
| stop_limit_order.stop_price | Decimal | Giá kích hoạt | 42000.00 |
| stop_limit_order.limit_price | Decimal | Giá giới hạn sau kích hoạt | 42500.00 |
| stop_limit_order.status | String | Trạng thái | "PENDING_TRIGGER" |
| created_at | Timestamp | Thời gian tạo | "2025-11-17T10:30:45Z" |
| estimated_value | Decimal | Giá trị ước tính | 20000000.00 |

#### 5.2.2 Response khi query danh sách lệnh OCO

| Trường Output | Kiểu dữ liệu | Mô tả | Ví dụ |
|---------------|--------------|-------|-------|
| data | Array | Mảng các lệnh OCO | [{...}, {...}] |
| data[].oco_order_id | String | ID lệnh OCO | "OCO-20251117-001234" |
| data[].symbol | String | Mã CK | "VN30F2312" |
| data[].side | String | Chiều | "BUY" / "SELL" |
| data[].volume | Integer | Khối lượng | 500 |
| data[].filled_volume | Integer | Khối lượng đã khớp | 200 |
| data[].status | String | Trạng thái | "PENDING", "PARTIALLY_FILLED", "FILLED", "CANCELLED" |
| data[].limit_order | Object | Chi tiết Limit Order | {...} |
| data[].stop_limit_order | Object | Chi tiết Stop-Limit Order | {...} |
| data[].created_at | Timestamp | Thời gian tạo | "2025-11-17T10:30:45Z" |
| pagination | Object | Thông tin phân trang | {...} |
| pagination.page | Integer | Trang hiện tại | 1 |
| pagination.page_size | Integer | Số bản ghi/trang | 20 |
| pagination.total_records | Integer | Tổng số bản ghi | 156 |
| pagination.total_pages | Integer | Tổng số trang | 8 |

### 5.3 Data Validation Rules

| Validation | Mô tả | Điều kiện | Thông báo |
|------------|-------|-----------|-----------|
| VAL-001 | Symbol hợp lệ | Symbol tồn tại trong danh sách CK, không bị suspend | "Mã chứng khoán không hợp lệ hoặc tạm ngưng giao dịch" |
| VAL-002 | Volume hợp lệ | Volume > 0 AND volume % 100 == 0 AND volume <= 999,999,900 | "Khối lượng phải lớn hơn 0, là bội số 100 và không vượt quá 999,999,900" |
| VAL-003 | Price format | Price > 0 AND có tối đa 2 chữ số thập phân | "Giá phải lớn hơn 0 và có tối đa 2 chữ số thập phân" |
| VAL-004 | Price range | Price trong biên độ cho phép (±7% hoặc ±15% tùy sàn) | "Giá vượt quá biên độ dao động cho phép" |
| VAL-005 | OCO Buy Price | Price < current_market_price | "Giá Price phải nhỏ hơn giá thị trường hiện tại" |
| VAL-006 | OCO Buy Stop | Stop > current_market_price | "Giá Stop phải lớn hơn giá thị trường hiện tại" |
| VAL-007 | OCO Buy Limit | Limit >= Stop | "Giá Limit phải lớn hơn hoặc bằng giá Stop" |
| VAL-008 | OCO Sell Price | Price > current_market_price | "Giá Price phải lớn hơn giá thị trường hiện tại" |
| VAL-009 | OCO Sell Stop | Stop < current_market_price | "Giá Stop phải nhỏ hơn giá thị trường hiện tại" |
| VAL-010 | OCO Sell Limit | Limit <= Stop | "Giá Limit phải nhỏ hơn hoặc bằng giá Stop" |
| VAL-011 | Buying power | available_cash >= volume × max(price, limit_price) | "Không đủ sức mua. Cần {required_amount} VNĐ" |
| VAL-012 | Available volume | available_volume >= volume | "Không đủ khối lượng. Khối lượng khả dụng: {available}" |
| VAL-013 | Order limit | Số lệnh OCO active cho symbol < 10 | "Vượt quá giới hạn 10 lệnh OCO cho một mã chứng khoán" |
| VAL-014 | Trading session | Hiện tại trong giờ giao dịch hoặc ATO/ATC | "Ngoài giờ giao dịch. Vui lòng đặt lệnh trong phiên giao dịch" |
| VAL-015 | Account status | Account status = "ACTIVE" | "Tài khoản không ở trạng thái hoạt động" |

---

## 6. CHI TIẾT IPO (INPUT - PROCESS - OUTPUT)

### 6.1 IPO Flow cho Tạo lệnh OCO Mua

#### INPUT

**User Input:**
| Tham số | Mô tả | Kiểu | Bắt buộc | Ví dụ |
|---------|-------|------|----------|-------|
| symbol | Mã chứng khoán | String | Có | "VN30F2312" |
| volume | Khối lượng đặt | Integer | Có | 500 |
| price | Giá Limit Order (mua giá thấp) | Decimal | Có | 40000.00 |
| stop_price | Giá kích hoạt Stop-Limit | Decimal | Có | 42000.00 |
| limit_price | Giá Limit sau khi Stop kích hoạt | Decimal | Có | 42500.00 |

**System Input:**
| Tham số | Mô tả | Nguồn | Ví dụ |
|---------|-------|-------|-------|
| current_market_price | Giá thị trường hiện tại | Market data feed | 41000.00 |
| account_info | Thông tin tài khoản user | Account service | {account_id, available_cash, ...} |
| symbol_info | Thông tin mã CK | Symbol master data | {trading_status, price_ceiling, price_floor, ...} |
| active_oco_count | Số lệnh OCO đang active cho symbol | Database query | 3 |

**Context Data:**
- User session information (user_id, account_id, session_id)
- Trading session status (is_market_open, session_type)
- System timestamp

#### PROCESS

**Mô tả nghiệp vụ:** Tạo lệnh OCO Mua với validation đầy đủ, reserve buying power, tạo 2 sub-orders và bắt đầu monitoring

**Các bước xử lý:**

1. **Validate Input Data**
   - Kiểm tra symbol có hợp lệ và đang giao dịch
   - Kiểm tra volume > 0, là bội số 100
   - Kiểm tra tất cả giá > 0 và có 2 chữ số thập phân
   - Nếu vi phạm → Trả về lỗi tương ứng theo validation rules (VAL-001 đến VAL-003)

2. **Validate Business Rules cho OCO Buy**
   - Lấy giá thị trường hiện tại từ market data feed
   - Kiểm tra điều kiện: Price < Current Market Price < Stop Price
   - Kiểm tra: Limit Price >= Stop Price
   - Kiểm tra tất cả giá trong biên độ dao động cho phép
   - Nếu vi phạm → Trả về lỗi business rules (BR-001 đến BR-004, VAL-004)

3. **Check Trading Session và Order Limit**
   - Kiểm tra đang trong giờ giao dịch
   - Kiểm tra số lệnh OCO active cho symbol < 10
   - Kiểm tra account status = ACTIVE
   - Nếu vi phạm → Trả về lỗi VAL-013, VAL-014, VAL-015

4. **Check Buying Power**
   - Lấy available_cash từ account service
   - Tính required_cash = volume × max(price, limit_price)
   - So sánh available_cash >= required_cash
   - Nếu không đủ → Trả về lỗi VAL-011 với số tiền cần thiết

5. **Create OCO Master Order và Sub-orders**
   - Begin database transaction
   - Tạo OCO Master Order với status PENDING
   - Tạo Limit Order với giá = price, status = PENDING
   - Tạo Stop-Limit Order với stop_price, limit_price, status = PENDING_TRIGGER
   - Insert vào database
   - Nếu lỗi database → Rollback, trả về lỗi hệ thống

6. **Submit Limit Order to Matching Engine**
   - Gửi Limit Order vào matching engine
   - Nếu thành công → Tiếp tục
   - Nếu thất bại → Rollback transaction, trả về lỗi ERR-OCO-010

7. **Reserve Buying Power và Finalize**
   - Reserve cash = required_cash trong account
   - Update available_cash, reserved_cash
   - Commit database transaction
   - Register price monitoring cho Stop-Limit trigger
   - Send notification cho user
   - Write audit log

8. **Return Success Response**
   - Trả về OCO order details với đầy đủ thông tin 2 sub-orders
   - Include: oco_order_id, status, symbol, volume, prices, created_at

**Business Logic:**
- Buying power calculation: Sử dụng max(price, limit_price) để reserve đủ tiền cho cả 2 trường hợp
- Transaction atomicity: Tất cả bước phải thành công, nếu fail 1 bước → rollback toàn bộ
- Price validation: Đảm bảo giá nằm trong biên độ và thỏa mãn logic OCO Buy

**Error Handling:**
- Database error → Rollback transaction, log error, return "Lỗi hệ thống, vui lòng thử lại"
- Matching engine timeout → Retry 3 lần với exponential backoff, nếu fail → rollback và return error
- Insufficient balance → Return error ngay sau validation step 4
- Market halted → Queue order, process khi market mở lại
- Duplicate order ID → Retry generate new ID, max 5 lần

#### OUTPUT

**Success Response:**
```json
{
  "status": "SUCCESS",
  "oco_order_id": "OCO-20251117-001234",
  "symbol": "VN30F2312",
  "side": "BUY",
  "volume": 500,
  "filled_volume": 0,
  "status_description": "PENDING",
  "limit_order": {
    "order_id": "LO-20251117-001234-1",
    "order_type": "LIMIT",
    "price": 40000.00,
    "status": "PENDING",
    "created_at": "2025-11-17T10:30:45Z"
  },
  "stop_limit_order": {
    "order_id": "SL-20251117-001234-2",
    "order_type": "STOP_LIMIT",
    "stop_price": 42000.00,
    "limit_price": 42500.00,
    "status": "PENDING_TRIGGER",
    "created_at": "2025-11-17T10:30:45Z"
  },
  "estimated_value": 20000000.00,
  "reserved_amount": 21250000.00,
  "created_at": "2025-11-17T10:30:45Z",
  "message": "Lệnh OCO đã được tạo thành công"
}
```

**Error Response:**

| Error Code | Mô tả | HTTP Status | Message |
|------------|-------|-------------|---------|
| ERR-OCO-001 | Symbol không hợp lệ | 400 | "Mã chứng khoán không hợp lệ hoặc tạm ngưng giao dịch" |
| ERR-OCO-002 | Volume không hợp lệ | 400 | "Khối lượng phải lớn hơn 0 và là bội số của 100" |
| ERR-OCO-003 | Price validation failed | 400 | "Giá Price phải nhỏ hơn giá thị trường hiện tại" |
| ERR-OCO-004 | Stop price validation failed | 400 | "Giá Stop phải lớn hơn giá thị trường hiện tại" |
| ERR-OCO-005 | Limit price validation failed | 400 | "Giá Limit phải lớn hơn hoặc bằng giá Stop" |
| ERR-OCO-006 | Insufficient buying power | 400 | "Không đủ sức mua. Cần {amount} VNĐ" |
| ERR-OCO-007 | Vượt quá giới hạn lệnh | 400 | "Vượt quá giới hạn 10 lệnh OCO cho một mã chứng khoán" |
| ERR-OCO-008 | Ngoài giờ giao dịch | 400 | "Ngoài giờ giao dịch. Vui lòng đặt lệnh trong phiên giao dịch" |
| ERR-OCO-009 | Account không active | 403 | "Tài khoản không ở trạng thái hoạt động" |
| ERR-OCO-010 | Matching engine error | 500 | "Lỗi hệ thống khớp lệnh. Vui lòng thử lại sau" |
| ERR-OCO-011 | Database error | 500 | "Lỗi hệ thống. Vui lòng thử lại sau" |

**Side Effects:**
- OCO Master Order record created trong database
- 2 Sub-order records created (Limit và Stop-Limit)
- Buying power reserved trong account
- Price monitoring registered cho Stop-Limit trigger
- Notification sent cho user
- Audit log written

### 6.2 IPO Flow cho Limit Order Matched → Cancel Stop-Limit

#### INPUT

**Matching Engine Event:**
| Tham số | Mô tả | Nguồn | Ví dụ |
|---------|-------|-------|-------|
| order_id | ID của lệnh vừa khớp | Matching engine | "LO-20251117-001234-1" |
| matched_volume | Khối lượng khớp | Matching engine | 500 |
| matched_price | Giá khớp | Matching engine | 40000.00 |
| match_timestamp | Thời điểm khớp | Matching engine | "2025-11-17T11:15:30.123Z" |
| match_type | Loại khớp | Matching engine | "FULL" / "PARTIAL" |

**System Input:**
| Tham số | Mô tả | Nguồn | Ví dụ |
|---------|-------|-------|-------|
| order_details | Chi tiết lệnh vừa khớp | Database query | {order_id, oco_order_id, order_type, volume, ...} |
| oco_master | OCO Master Order | Database query | {oco_order_id, status, user_id, ...} |
| stop_limit_order | Stop-Limit Order còn lại | Database query | {order_id, status, ...} |

**Context Data:**
- Transaction ID
- System timestamp
- User information

#### PROCESS

**Mô tả nghiệp vụ:** Khi Limit Order của lệnh OCO được khớp (full hoặc partial), hệ thống tự động hủy Stop-Limit Order còn lại, update trạng thái OCO, release resources và thông báo user

**Các bước xử lý:**

1. **Receive Order Match Event**
   - Nhận event từ matching engine khi có lệnh khớp
   - Parse order_id, matched_volume, matched_price, match_type
   - Log event nhận được

2. **Check if Order Belongs to OCO**
   - Query database để lấy order details
   - Kiểm tra order có thuộc OCO không (oco_order_id != null)
   - Nếu không thuộc OCO → End process, không xử lý gì thêm
   - Nếu thuộc OCO → Tiếp tục

3. **Validate OCO Status**
   - Query OCO Master Order theo oco_order_id
   - Kiểm tra OCO status = PENDING hoặc PARTIALLY_FILLED
   - Nếu status = CANCELLED/FILLED/REJECTED → End process (đã xử lý rồi)
   - Nếu status hợp lệ → Tiếp tục

4. **Determine Match Completion**
   - Kiểm tra match_type = FULL (khớp hết) hay PARTIAL (khớp một phần)
   - Nếu PARTIAL:
     - Update filled_volume trong OCO Master
     - Update OCO status = PARTIALLY_FILLED
     - End process, giữ nguyên Stop-Limit Order
   - Nếu FULL → Tiếp tục xử lý cancel Stop-Limit

5. **Get Stop-Limit Order to Cancel**
   - Query Stop-Limit Order còn lại theo oco_order_id
   - Kiểm tra Stop-Limit status = PENDING_TRIGGER hoặc PENDING
   - Nếu không tìm thấy hoặc status không hợp lệ → Log warning, tiếp tục update OCO status

6. **Cancel Stop-Limit Order**
   - Begin database transaction
   - Nếu Stop-Limit đã được submit vào matching engine → Gửi cancel request
   - Nếu Stop-Limit đang PENDING_TRIGGER → Chỉ update status trong database
   - Update Stop-Limit status = CANCELLED
   - Set cancellation_reason = "OCO - Limit Order matched"
   - Set cancelled_at = current_timestamp
   - Nếu cancel matching engine thất bại → Log error, vẫn update database (best effort)

7. **Update OCO Master Order**
   - Update OCO status = FILLED
   - Update filled_volume = total matched volume
   - Update filled_at = match_timestamp
   - Update matched_price = matched_price
   - Commit database transaction

8. **Release Reserved Resources**
   - Nếu là OCO BUY → Release reserved cash chưa dùng
   - Nếu là OCO SELL → Release held volume
   - Update account balance

9. **Send Notifications**
   - Send notification "Lệnh OCO đã khớp hoàn toàn" cho user
   - Include: symbol, matched_price, matched_volume, total_value
   - Send push notification, email (nếu user bật setting)

10. **Write Audit Log**
    - Log event: OCO_LIMIT_MATCHED_STOP_CANCELLED
    - Include: oco_order_id, limit_order_id, stop_limit_order_id, matched_price, matched_volume
    - Timestamp, user_id, transaction_id

**Business Logic:**
- Chỉ cancel Stop-Limit khi Limit Order khớp FULL, không cancel khi PARTIAL
- Cancel là best-effort: Nếu cancel matching engine fail, vẫn update database và notify user
- Transaction isolation: Đảm bảo không có race condition khi 2 orders cùng khớp
- Resource cleanup: Release reserved cash/volume ngay sau khi khớp

**Error Handling:**
- Cancel matching engine failed → Log error, continue với database update, alert ops team
- Database error → Retry transaction 3 lần, nếu fail → Alert critical, manual intervention
- OCO not found hoặc status invalid → Log warning, end process gracefully
- Race condition (cả 2 orders cùng khớp) → Sử dụng database lock, xử lý theo thứ tự timestamp

#### OUTPUT

**Success Side Effects:**
- Limit Order status = FILLED trong database
- Stop-Limit Order status = CANCELLED trong database
- OCO Master status = FILLED
- Reserved resources released (cash hoặc volume)
- User notification sent
- Audit log written

**Event Published:**
```json
{
  "event_type": "OCO_LIMIT_MATCHED_STOP_CANCELLED",
  "oco_order_id": "OCO-20251117-001234",
  "limit_order_id": "LO-20251117-001234-1",
  "stop_limit_order_id": "SL-20251117-001234-2",
  "symbol": "VN30F2312",
  "side": "BUY",
  "matched_price": 40000.00,
  "matched_volume": 500,
  "total_value": 20000000.00,
  "matched_at": "2025-11-17T11:15:30.123Z",
  "user_id": "user-12345",
  "account_id": "account-67890"
}
```

**Notification Message:**
```
Lệnh OCO đã khớp thành công
- Mã CK: VN30F2312
- Loại: Mua
- Khối lượng: 500
- Giá khớp: 40,000 VNĐ
- Tổng giá trị: 20,000,000 VNĐ
- Lệnh Stop-Limit đã được tự động hủy
```

**Error Scenarios:**

| Scenario | Handling | Alert Level |
|----------|----------|-------------|
| Stop-Limit cancel failed (matching engine) | Log error, update database anyway, notify user | Warning |
| Database update failed | Retry 3 lần, alert ops team, queue for manual fix | Critical |
| OCO already processed | Log warning, end gracefully | Info |
| Race condition detected | Use optimistic locking, retry | Warning |
| Notification service down | Queue notification for retry | Low |

### 6.3 IPO Flow cho Kích hoạt Stop-Limit Order

#### INPUT

**Market Data Input:**
| Tham số | Mô tả | Nguồn | Ví dụ |
|---------|-------|-------|-------|
| symbol | Mã chứng khoán | Market data feed | "VN30F2312" |
| price | Giá giao dịch mới nhất | Market data feed | 42000.00 |
| timestamp | Thời điểm price tick | Market data feed | "2025-11-17T11:25:30.123Z" |

**System Input:**
| Tham số | Mô tả | Nguồn | Ví dụ |
|---------|-------|-------|-------|
| pending_stop_orders | Danh sách Stop-Limit orders chờ trigger | Database query | [{order_id, stop_price, side, ...}] |

**Context Data:**
- Market session status
- System health metrics

#### PROCESS

**Mô tả nghiệp vụ:** Hệ thống monitoring giá thị trường real-time, khi giá chạm điều kiện trigger của Stop-Limit Order, tự động hủy Limit Order và kích hoạt Stop-Limit Order

**Các bước xử lý:**

1. **Receive Price Tick Event**
   - Nhận price update từ market data feed
   - Extract symbol, price, timestamp
   - Validate data integrity

2. **Query Pending Stop-Limit Orders**
   - Query tất cả Stop-Limit Orders theo symbol
   - Filter status = PENDING_TRIGGER
   - Order by created_at ASC (FIFO priority)

3. **Check Trigger Condition for Each Order**
   - Với mỗi Stop-Limit Order, kiểm tra điều kiện trigger:
     - OCO Mua: Trigger khi market_price >= stop_price
     - OCO Bán: Trigger khi market_price <= stop_price
   - Nếu thỏa mãn → Đánh dấu để xử lý trigger
   - Nếu không thỏa mãn → Bỏ qua

4. **Validate OCO Status Before Trigger**
   - Với mỗi order cần trigger, query OCO Master
   - Kiểm tra OCO status = PENDING
   - Nếu status khác (CANCELLED/FILLED) → Bỏ qua, không trigger
   - Nếu status hợp lệ → Tiếp tục

5. **Cancel Limit Order**
   - Begin database transaction
   - Query Limit Order (sub-order còn lại) theo oco_order_id
   - Gửi cancel request đến matching engine
   - Nếu cancel thành công → Update Limit Order status = CANCELLED
   - Nếu cancel thất bại → Rollback transaction, log error, không trigger Stop-Limit

6. **Activate Stop-Limit Order**
   - Update Stop-Limit Order status từ PENDING_TRIGGER → PENDING
   - Set activated_at = current_timestamp
   - Set trigger_price_actual = current market price
   - Submit Stop-Limit vào matching engine như Limit Order với price = limit_price

7. **Update OCO Master Status**
   - Update OCO status = STOP_TRIGGERED
   - Update triggered_at = timestamp
   - Update trigger_price = actual trigger price
   - Commit database transaction

8. **Send Notification**
   - Send notification "Stop-Limit đã được kích hoạt" cho user
   - Include: symbol, trigger_price, limit_price submitted
   - Push notification + email (optional)

9. **Write Audit Log**
   - Log event: OCO_STOP_TRIGGERED
   - Include: oco_order_id, trigger_price, limit_price, timestamp

10. **Monitor Performance**
    - Measure latency từ price tick đến trigger completion
    - Nếu > 100ms → Log warning, alert ops team
    - Track trigger accuracy rate

**Business Logic:**
- Trigger detection phải real-time (< 100ms latency)
- Cancel Limit Order phải thành công trước khi activate Stop-Limit (atomicity)
- FIFO priority khi nhiều orders cùng trigger
- Market halt → Pause monitoring, resume khi market mở

**Error Handling:**
- Cancel Limit Order failed → Rollback, không trigger Stop-Limit, log error, retry sau 1s
- Submit Stop-Limit failed → Rollback, giữ nguyên trạng thái, alert ops team
- Database deadlock → Retry transaction max 3 lần
- Market halted → Queue trigger event, process khi market resume
- Matching engine timeout → Retry với exponential backoff

#### OUTPUT

**Success Side Effects:**
- Limit Order status = CANCELLED trong matching engine và database
- Stop-Limit Order status = PENDING và submitted vào matching engine
- OCO Master status = STOP_TRIGGERED
- Notification sent to user
- Audit log written

**Event Published:**
```json
{
  "event_type": "OCO_STOP_TRIGGERED",
  "oco_order_id": "OCO-20251117-001234",
  "stop_order_id": "SL-20251117-001234-2",
  "cancelled_order_id": "LO-20251117-001234-1",
  "symbol": "VN30F2312",
  "side": "BUY",
  "trigger_price": 42000.00,
  "limit_price": 42500.00,
  "triggered_at": "2025-11-17T11:25:30.456Z"
}
```

**Notification Message:**
```
Lệnh Stop-Limit đã được kích hoạt
- Mã CK: VN30F2312
- Giá kích hoạt: 42,000 VNĐ
- Lệnh Limit đã đặt tại giá: 42,500 VNĐ
- Khối lượng: 500
```

### 6.4 State Diagram

```
                    ┌─────────────────┐
                    │   ORDER CREATED │
                    │     (PENDING)   │
                    └────────┬────────┘
                             │
                    ┌────────▼─────────────────────────────┐
                    │  Monitoring Market Price             │
                    │  - Limit Order: In Order Book        │
                    │  - Stop-Limit: Waiting for Trigger   │
                    └────┬──────────────────┬──────────────┘
                         │                  │
        ┌────────────────┼──────────────────┼────────────────┐
        │                │                  │                │
        │                │                  │                │
  ┌─────▼─────┐    ┌────▼──────┐    ┌─────▼──────┐   ┌────▼────────┐
  │  Limit    │    │   Stop    │    │   User     │   │  End of Day │
  │  Order    │    │ Triggered │    │  Manual    │   │   (EOD)     │
  │  Matched  │    │           │    │  Cancel    │   │   Auto      │
  └─────┬─────┘    └────┬──────┘    └─────┬──────┘   │   Cancel    │
        │               │                  │          └────┬────────┘
        │               │                  │               │
        │       ┌───────▼───────┐          │               │
        │       │ Cancel Other  │          │               │
        │       │  Sub-Order    │          │               │
        │       └───────┬───────┘          │               │
        │               │                  │               │
        │       ┌───────▼────────┐         │               │
        │       │ Submit Stop-   │         │               │
        │       │ Limit as Limit │         │               │
        │       └───────┬────────┘         │               │
        │               │                  │               │
        │       ┌───────▼─────────┐        │               │
        │       │ STOP_TRIGGERED  │        │               │
        │       │   (Waiting      │        │               │
        │       │    for Match)   │        │               │
        │       └───────┬─────────┘        │               │
        │               │                  │               │
        │       ┌───────▼─────────┐        │               │
        │       │ Stop-Limit      │        │               │
        │       │   Matched       │        │               │
        │       └───────┬─────────┘        │               │
        │               │                  │               │
        ▼               ▼                  ▼               ▼
    ┌───────────────────────────────────────────────────────┐
    │                    FILLED / CANCELLED                 │
    │                   (Terminal State)                    │
    └───────────────────────────────────────────────────────┘
```

**Trạng thái (States):**

| Trạng thái | Mô tả | Trạng thái tiếp theo có thể | Terminal State |
|------------|-------|----------------------------|----------------|
| PENDING | OCO vừa tạo, Limit Order trong order book, Stop-Limit đang chờ trigger | PARTIALLY_FILLED, FILLED, STOP_TRIGGERED, CANCELLED | No |
| PARTIALLY_FILLED | Limit Order đã khớp một phần | FILLED, CANCELLED | No |
| STOP_TRIGGERED | Stop-Limit đã kích hoạt, Limit Order đã hủy, Stop-Limit đang chờ khớp | FILLED, CANCELLED | No |
| FILLED | Một trong hai sub-order đã khớp hoàn toàn, order kia đã hủy | - | Yes |
| CANCELLED | User hủy hoặc hệ thống tự động hủy (EOD) | - | Yes |
| REJECTED | Lệnh bị từ chối do vi phạm business rules | - | Yes |

**Chuyển trạng thái (Transitions):**

| Từ trạng thái | Sự kiện | Đến trạng thái | Side Effects |
|---------------|---------|----------------|--------------|
| PENDING | Limit Order matched (full) | FILLED | Cancel Stop-Limit, Release reserved cash, Send notification |
| PENDING | Limit Order matched (partial) | PARTIALLY_FILLED | Update filled_volume |
| PARTIALLY_FILLED | Limit Order matched (remaining) | FILLED | Cancel Stop-Limit, Release reserved cash |
| PENDING | Market price hits Stop | STOP_TRIGGERED | Cancel Limit Order, Submit Stop-Limit as Limit, Send notification |
| STOP_TRIGGERED | Stop-Limit matched (full) | FILLED | Release reserved cash, Send notification |
| PENDING | User cancels | CANCELLED | Cancel both sub-orders, Release reserved resources |
| PARTIALLY_FILLED | User cancels | CANCELLED | Cancel remaining volume, Release reserved resources |
| STOP_TRIGGERED | User cancels | CANCELLED | Cancel Stop-Limit order, Release reserved resources |
| PENDING | End of Day (EOD) | CANCELLED | Auto cancel both sub-orders, Release resources, Send notification |
| STOP_TRIGGERED | End of Day (EOD) | CANCELLED | Auto cancel Stop-Limit, Send notification |
| PENDING | Validation failed | REJECTED | Send error notification, Log error |

---

## 7. YÊU CẦU GIAO DIỆN NGƯỜI DÙNG

### 7.1 Màn hình tạo lệnh OCO

**Tên màn hình**: OCO Order Placement Form

**Mục đích**: Cho phép người dùng nhập thông tin và tạo lệnh OCO

**Layout**:
```
+------------------------------------------------------------------+
|  Đặt Lệnh OCO (One Cancels the Other)                [X] Close  |
+------------------------------------------------------------------+
|                                                                  |
|  Loại lệnh: ( ) Mua  ( ) Bán                                   |
|                                                                  |
|  Mã chứng khoán: [____________] [Search Icon]                  |
|                  Giá hiện tại: 41,000 VNĐ  ▲ +1.23%            |
|                                                                  |
|  Khối lượng:     [____________] (bội số 100)                    |
|                                                                  |
|  ┌────────────────────────────────────────────────────────────┐ |
|  │  LIMIT ORDER (Lệnh giới hạn)                               │ |
|  │  Giá Price: [____________] VNĐ                             │ |
|  │  💡 Giá mua thấp khi thị trường giảm                       │ |
|  └────────────────────────────────────────────────────────────┘ |
|                                                                  |
|  ┌────────────────────────────────────────────────────────────┐ |
|  │  STOP-LIMIT ORDER (Lệnh dừng giới hạn)                    │ |
|  │  Giá Stop:  [____________] VNĐ                             │ |
|  │  💡 Kích hoạt khi giá vượt kháng cự                        │ |
|  │                                                              │ |
|  │  Giá Limit: [____________] VNĐ                             │ |
|  │  💡 Giá tối đa chấp nhận mua sau khi kích hoạt             │ |
|  └────────────────────────────────────────────────────────────┘ |
|                                                                  |
|  ┌────────────────────────────────────────────────────────────┐ |
|  │  THÔNG TIN ƯỚC TÍNH                                        │ |
|  │  • Sức mua cần thiết: 21,250,000 VNĐ                       │ |
|  │  • Sức mua khả dụng:  35,000,000 VNĐ                       │ |
|  │  • Phí giao dịch:         ~53,125 VNĐ                      │ |
|  └────────────────────────────────────────────────────────────┘ |
|                                                                  |
|  [Hủy]                              [Xem trước]  [Đặt lệnh]    |
|                                                                  |
+------------------------------------------------------------------+
```

**Các trường dữ liệu**:

| Tên trường | Loại control | Bắt buộc | Giá trị mặc định | Ghi chú |
|------------|--------------|----------|------------------|---------|
| order_type | Radio button | Có | Mua | "Mua" hoặc "Bán" |
| symbol | Autocomplete textbox | Có | - | Search mã CK, hiển thị gợi ý |
| volume | Number input | Có | - | Step = 100, min = 100 |
| price | Number input | Có | - | 2 decimal places, format VNĐ |
| stop_price | Number input | Có | - | 2 decimal places, format VNĐ |
| limit_price | Number input | Có | - | 2 decimal places, format VNĐ |

**Actions**:
- **Button "Hủy"**: Đóng form, clear tất cả inputs
- **Button "Xem trước"**: Hiển thị preview dialog với chi tiết đầy đủ, cho phép user xác nhận lại
- **Button "Đặt lệnh"**: Submit form, validate, tạo lệnh OCO
  - Disable button khi đang submit (loading state)
  - Hiển thị success message hoặc error message
  - Nếu thành công → Redirect sang Order Management screen

**Validation & Error Display**:
- **Real-time validation**: Validate ngay khi user blur khỏi field
- **Error hiển thị**: Dưới field bị lỗi, màu đỏ, icon warning
- **Success indicator**: Border màu xanh khi field hợp lệ
- **Tooltip**: Hiển thị gợi ý khi hover vào icon "💡"

**Dynamic Behavior**:
- Khi chọn "Mua":
  - Label change: "Giá mua thấp", "Kích hoạt khi vượt kháng cự"
  - Validation: Price < Market < Stop, Limit >= Stop
- Khi chọn "Bán":
  - Label change: "Giá bán cao (chốt lời)", "Kích hoạt khi phá hỗ trợ (cắt lỗ)"
  - Validation: Stop < Market < Price, Limit <= Stop
- Auto-calculate "Sức mua cần thiết" khi user nhập đủ volume và prices

### 7.2 Màn hình quản lý lệnh OCO

**Tên màn hình**: OCO Order Management

**Mục đích**: Hiển thị danh sách lệnh OCO, cho phép filter, view details, cancel

**Layout**:
```
+------------------------------------------------------------------+
|  Quản lý Lệnh OCO                                   [+ Tạo mới] |
+------------------------------------------------------------------+
|  Filter: Mã CK [________] | Trạng thái [All ▼] | Từ ngày [__] Đến [__] [Tìm kiếm] |
+------------------------------------------------------------------+
|  ID Lệnh    | Mã CK | Loại | Khối lượng | Giá Price | Stop | Limit | Trạng thái | Ngày tạo      | Actions    |
|-------------|-------|------|------------|-----------|------|-------|------------|---------------|------------|
| OCO-001234  | VN30  | Mua  | 500        | 40,000    |42,000|42,500 | Pending    | 17/11 10:30  | [Xem][Hủy] |
| OCO-001235  | VCB   | Bán  | 300        | 95,000    |90,000|89,500 | Stop Trig. | 17/11 09:15  | [Xem][Hủy] |
| OCO-001236  | FPT   | Mua  | 1,000      | 68,000    |70,000|70,200 | Filled     | 16/11 14:20  | [Xem]      |
| OCO-001237  | VHM   | Bán  | 500        | 82,000    |78,000|77,800 | Cancelled  | 16/11 11:05  | [Xem]      |
|-------------|-------|------|------------|-----------|------|-------|------------|---------------|---------------|
|  Trang 1 / 8                                   [< Prev]  [Next >]                                                |
+------------------------------------------------------------------+
```

**Các cột hiển thị**:

| Tên cột | Kiểu dữ liệu | Có thể sort | Có thể filter | Mô tả |
|---------|--------------|-------------|---------------|-------|
| ID Lệnh | String | Có | Có | Clickable → Chi tiết lệnh |
| Mã CK | String | Có | Có | Symbol |
| Loại | String | Có | Có | "Mua" hoặc "Bán" |
| Khối lượng | Integer | Có | Không | Tổng volume |
| Giá Price | Decimal | Có | Không | Giá Limit Order |
| Stop | Decimal | Có | Không | Giá Stop trigger |
| Limit | Decimal | Có | Không | Giá Limit sau khi trigger |
| Trạng thái | String | Có | Có | Badge với màu khác nhau |
| Ngày tạo | Datetime | Có | Có | Format: DD/MM HH:mm |
| Actions | Buttons | Không | Không | Xem, Hủy |

**Actions trên dòng**:
- **Xem**: Mở dialog hiển thị chi tiết đầy đủ lệnh OCO (cả 2 sub-orders, history, audit log)
- **Hủy**: Chỉ hiển thị nếu status = "Pending" hoặc "Partially Filled", confirm trước khi hủy

**Pagination**:
- Số bản ghi mỗi trang: 20 (default), có thể chọn 10/20/50/100
- Loại pagination: Server-side (do có thể có hàng nghìn lệnh)

**Real-time Update**:
- Sử dụng WebSocket để nhận update real-time
- Khi có lệnh mới/update → Highlight dòng 3s (màu vàng nhạt)
- Auto refresh mỗi 10s nếu WebSocket disconnect

**Status Badge Colors**:
- Pending: Màu xanh dương
- Partially Filled: Màu cam
- Stop Triggered: Màu tím
- Filled: Màu xanh lá
- Cancelled: Màu xám
- Rejected: Màu đỏ

---

## 8. PHỤ LỤC

### 8.1 Ví dụ Scenarios

#### Scenario 1: OCO Mua thành công - Limit Order khớp

**Given:**
- User có sức mua 30,000,000 VNĐ
- Giá VN30 hiện tại: 41,000 VNĐ

**When:**
- User đặt OCO Mua: Volume=500, Price=40,000, Stop=42,000, Limit=42,500

**Then:**
- Hệ thống tạo OCO với 2 sub-orders
- Limit Order (40,000) vào order book
- Stop-Limit (42,000/42,500) chờ trigger
- Giá giảm xuống 40,000 → Limit Order khớp
- Hệ thống tự động hủy Stop-Limit Order
- OCO status = "Filled"
- User nhận notification "Lệnh OCO đã khớp tại giá 40,000"

#### Scenario 2: OCO Mua thành công - Stop-Limit kích hoạt

**Given:**
- User có sức mua 30,000,000 VNĐ
- Giá VN30 hiện tại: 41,000 VNĐ

**When:**
- User đặt OCO Mua: Volume=500, Price=40,000, Stop=42,000, Limit=42,500

**Then:**
- Hệ thống tạo OCO với 2 sub-orders
- Giá tăng lên 42,000 → Stop-Limit trigger
- Hệ thống hủy Limit Order (40,000)
- Submit Stop-Limit như Limit Order (42,500) vào order book
- OCO status = "Stop Triggered"
- Giá tiếp tục tăng, Stop-Limit khớp tại 42,500
- OCO status = "Filled"
- User nhận 2 notifications: "Stop triggered" và "Lệnh khớp"

#### Scenario 3: OCO Bán để chốt lời và cắt lỗ

**Given:**
- User đang nắm giữ 500 VCB
- Giá VCB hiện tại: 92,000 VNĐ
- User mua vào giá: 90,000 VNĐ

**When:**
- User đặt OCO Bán: Volume=500, Price=95,000 (chốt lời), Stop=89,000, Limit=88,500 (cắt lỗ)

**Scenario 3a - Chốt lời:**
- Giá tăng lên 95,000 → Limit Order khớp
- Hệ thống hủy Stop-Limit
- User chốt lời 5,000/CP

**Scenario 3b - Cắt lỗ:**
- Giá giảm xuống 89,000 → Stop-Limit trigger
- Hệ thống hủy Limit Order (95,000)
- Submit Stop-Limit (88,500)
- Giá tiếp tục giảm, khớp tại 88,500
- User cắt lỗ 1,500/CP

### 8.2 Non-Functional Requirements

#### 8.2.1 Performance

| Yêu cầu | Target | Measure |
|---------|--------|---------|
| Order creation response time | < 1s (p95) | API response time từ submit đến confirm |
| Stop trigger detection latency | < 100ms | Thời gian từ price tick đến trigger decision |
| Order cancellation response time | < 500ms | Thời gian từ cancel request đến confirm |
| Concurrent order handling | 1,000+ orders/second | Throughput của matching engine |
| WebSocket notification delay | < 200ms | Thời gian từ event đến user nhận notification |
| Database query time | < 50ms (p95) | Query time cho order list, order details |

#### 8.2.2 Scalability

- Hỗ trợ tối thiểu 10,000 lệnh OCO active đồng thời
- Hệ thống phải scale horizontal để xử lý load tăng
- Database sharding theo user_id hoặc symbol nếu cần

#### 8.2.3 Availability

- System uptime: 99.9% (downtime < 8.76 giờ/năm)
- Planned maintenance: Ngoài giờ giao dịch (17:00-08:30)
- Disaster recovery: RPO < 5 phút, RTO < 30 phút

#### 8.2.4 Security

- **Authentication**: OAuth 2.0 + JWT token
- **Authorization**: Role-based access control (RBAC)
- **API Security**: Rate limiting (100 requests/minute/user)
- **Data Encryption**:
  - In transit: TLS 1.3
  - At rest: AES-256 cho sensitive data
- **Audit Log**: Immutable audit trail cho tất cả transactions
- **Input Validation**: Server-side validation cho tất cả inputs
- **SQL Injection Prevention**: Parameterized queries
- **XSS Prevention**: Content Security Policy, output encoding

#### 8.2.5 Compliance

- **Quy định HOSE/HNX**: Tuân thủ quy định giao dịch chứng khoán Việt Nam
- **Audit Trail**: Lưu trữ tối thiểu 7 năm theo quy định
- **Transaction Reporting**: Báo cáo giao dịch cho cơ quan quản lý
- **Anti-Money Laundering (AML)**: Giám sát giao dịch bất thường
- **Data Privacy**: Tuân thủ luật bảo vệ dữ liệu cá nhân

#### 8.2.6 Monitoring & Alerting

**Metrics:**
- Order creation success rate
- Stop trigger accuracy rate
- Average order processing time
- Error rate by error code
- Active OCO orders count
- Matching engine queue depth

**Alerts:**
- Error rate > 1%
- Response time > 2s (p95)
- Stop trigger latency > 200ms
- Database connection pool exhausted
- Matching engine unavailable

### 8.3 Assumptions & Constraints

#### Assumptions (Giả định)

⚠️ **Assumption 1**: Market data feed có độ trễ < 100ms so với thời gian thực
⚠️ **Assumption 2**: Matching engine có thể xử lý order cancellation/submission trong < 500ms
⚠️ **Assumption 3**: User hiểu rõ cơ chế lệnh OCO và rủi ro (cần training material)
⚠️ **Assumption 4**: Database có thể handle 100,000 orders active đồng thời
⚠️ **Assumption 5**: Network giữa trading system và matching engine stable (< 1% packet loss)
⚠️ **Assumption 6**: User có đủ kiến thức về phân tích kỹ thuật để đặt giá hợp lý
⚠️ **Assumption 7**: Phase 1 chỉ support web platform, mobile sẽ có ở phase sau

#### Constraints (Ràng buộc)

**Business Constraints:**
- Tối đa 10 lệnh OCO active cho một symbol/user
- Lệnh OCO tự động hủy vào End of Day (EOD) nếu chưa khớp
- Không hỗ trợ OCO cho margin trading trong phase 1
- Không hỗ trợ sửa đổi lệnh OCO sau khi tạo (user phải hủy và tạo lại)

**Technical Constraints:**
- Phải tích hợp với matching engine hiện tại (không thay đổi core matching logic)
- Phải sử dụng database hiện tại (PostgreSQL)
- Front-end phải tương thích với browsers: Chrome 90+, Firefox 88+, Safari 14+
- Mobile responsive không bắt buộc trong phase 1

**Regulatory Constraints:**
- Tuân thủ quy định biên độ dao động của HOSE/HNX
- Tuân thủ quy tắc khối lượng tối thiểu (bội số 100)
- Phải có audit log đầy đủ cho compliance
- Báo cáo giao dịch cho SSC (State Securities Commission)

### 8.4 Dependencies

**System Dependencies:**
- **Matching Engine**: Core dependency - xử lý order matching
- **Market Data Feed**: Cung cấp real-time price để trigger Stop-Limit
- **Account Service**: Kiểm tra buying power, available volume
- **Notification Service**: Gửi push notification, email, SMS
- **Audit Log Service**: Ghi immutable audit trail
- **Symbol Master Data Service**: Validate symbol, price ceiling/floor

**External Dependencies:**
- **HOSE/HNX Trading System**: Nguồn market data chính thức
- **Bank Integration**: Nếu cần auto top-up buying power
- **SMS Gateway**: Gửi notification qua SMS

**Integration Points:**
- REST API cho order submission
- WebSocket cho real-time updates
- Message Queue (Kafka/RabbitMQ) cho event processing
- Redis cho caching market data

### 8.5 Risks & Mitigation

| Risk | Probability | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| Stop trigger miss do latency cao | Medium | High | Implement redundant price monitoring, alert nếu latency > 100ms |
| Race condition khi 2 orders cùng khớp | Low | Critical | Sử dụng database transaction isolation, optimistic locking |
| Matching engine downtime | Low | High | Implement circuit breaker, queue orders, retry mechanism |
| Market data feed delay | Medium | High | Có backup feed, monitor lag, alert nếu lag > 200ms |
| User không hiểu cơ chế OCO | High | Medium | User education material, tooltip, example trong UI |
| Database performance degradation | Medium | High | Index optimization, query optimization, read replica |
| Security breach | Low | Critical | Penetration testing, security audit, rate limiting, WAF |
| Regulatory change | Medium | High | Flexible design, monitor regulatory updates |

### 8.6 Success Metrics (KPIs)

| KPI | Target | Measurement Method | Review Frequency |
|-----|--------|-------------------|------------------|
| Adoption Rate | 15% users sử dụng OCO trong 3 tháng | % users có ≥1 OCO order / Total active users | Monthly |
| Order Success Rate | > 99% | (Successful orders / Total orders) × 100% | Daily |
| Stop Trigger Accuracy | > 99.9% | (Correct triggers / Total triggers) × 100% | Daily |
| User Satisfaction | NPS > 50 | Survey sau khi sử dụng tính năng | Quarterly |
| Trading Volume Increase | +15% trong 6 tháng | Compare volume before/after OCO launch | Monthly |
| Average Response Time | < 1s (p95) | Monitor API response time | Real-time |
| Error Rate | < 0.5% | (Failed orders / Total orders) × 100% | Daily |
| Support Ticket Reduction | -20% câu hỏi về đặt lệnh | Compare support tickets before/after | Monthly |

---

**END OF DOCUMENT**
