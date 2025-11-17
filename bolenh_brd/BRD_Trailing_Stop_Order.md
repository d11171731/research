# LỆNH TRAILING STOP - Tài liệu Yêu cầu Nghiệp vụ (BRD)

---

## QUẢN LÝ TÀI LIỆU

| Thông tin | Chi tiết |
|-----------|----------|
| **Tên tài liệu** | Business Requirements Document - Lệnh Trailing Stop (Phase 1) |
| **Phiên bản** | 1.0 |
| **Ngày tạo** | 17/11/2025 |
| **Người tạo** | Business Analyst |
| **Người phê duyệt** | Product Owner |
| **Trạng thái** | Draft |

### Lịch sử phiên bản

| Phiên bản | Ngày | Người thay đổi | Mô tả thay đổi |
|-----------|------|----------------|----------------|
| 1.0 | 17/11/2025 | Business Analyst | Phiên bản khởi tạo - Phase 1 |

### Danh sách phân phối

| Vai trò | Họ tên | Email |
|---------|--------|-------|
| Product Owner | [Tên PO] | [Email] |
| Business Analyst | [Tên BA] | [Email] |
| Tech Lead | [Tên Tech Lead] | [Email] |
| QA Lead | [Tên QA Lead] | [Email] |
| Backend Developer | [Tên Dev] | [Email] |
| Frontend Developer | [Tên Dev] | [Email] |

---

## TÓM TẮT ĐIỀU HÀNH

Lệnh Trailing Stop là tính năng lệnh điều kiện cho phép nhà đầu tư tự động bảo vệ lợi nhuận bằng cách điều chỉnh giá kích hoạt theo biến động thị trường. Khi giá di chuyển theo hướng có lợi, giá kích hoạt sẽ tự động tăng (với lệnh bán) hoặc giảm (với lệnh mua) để bám sát giá thị trường. Khi giá đảo chiều vượt quá biên độ trượt cho phép, lệnh sẽ tự động kích hoạt và gửi lên sàn giao dịch. Tính năng này giúp nhà đầu tư giảm thiểu rủi ro, không cần theo dõi thị trường liên tục, đồng thời tối ưu hóa lợi nhuận trong biến động giá.

Phase 1 tập trung vào các chức năng cốt lõi: đặt lệnh, xem sổ lệnh, hủy lệnh, và xử lý tự động theo điều kiện kích hoạt. Tính năng sửa lệnh không được hỗ trợ do tính chất đặc thù của lệnh Trailing Stop với cơ chế điều chỉnh giá kích hoạt tự động.

---

## 1. GIỚI THIỆU

### 1.1 Mục đích tài liệu

Tài liệu này mô tả chi tiết các yêu cầu nghiệp vụ cho tính năng **Lệnh Trailing Stop** (Phase 1). Tài liệu được sử dụng bởi các nhóm phát triển, kiểm thử, và vận hành để hiểu rõ yêu cầu và triển khai chính xác chức năng lệnh điều kiện Trailing Stop trên hệ thống giao dịch chứng khoán.

### 1.2 Phạm vi

**Trong phạm vi (In Scope):**
- Đặt lệnh Trailing Stop với đầy đủ tham số
- Xem sổ lệnh điều kiện với các trạng thái
- Hủy lệnh ở trạng thái "Chờ kích hoạt"
- Xử lý tự động: theo dõi giá thị trường, điều chỉnh giá kích hoạt, kích hoạt lệnh
- Quản lý trạng thái lệnh (Chờ kích hoạt, Đã kích hoạt, Đã hủy, Hết hạn, Bị từ chối)
- Validation đầu vào khi đặt lệnh
- Thông báo cho khách hàng về trạng thái lệnh

**Ngoài phạm vi (Out of Scope):**
- Sửa lệnh Trailing Stop (không hỗ trợ trong Phase 1)
- Lệnh lô lẻ
- Báo cáo thống kê hiệu suất lệnh
- Tích hợp AI/ML để gợi ý tham số tối ưu
- Backtest chiến lược Trailing Stop
- Copy trade lệnh Trailing Stop

### 1.3 Định nghĩa và Thuật ngữ

| Thuật ngữ | Định nghĩa | Tiếng Anh |
|-----------|-----------|-----------|
| Lệnh Trailing Stop | Lệnh điều kiện tự động điều chỉnh giá kích hoạt theo biến động thị trường để bảo vệ lợi nhuận | Trailing Stop Order |
| Giá kích hoạt | Mức giá mà khi thị trường đạt đến, lệnh điều kiện sẽ được kích hoạt và chuyển thành lệnh thông thường | Trigger Price / Activation Price |
| Biên độ trượt (D) | Khoảng giá chênh lệch để xác định điểm đảo chiều (VNĐ) | Trailing Amount / Trailing Distance |
| Bước giá kích hoạt (delta) | Khoảng giá cộng/trừ so với giá kích hoạt khi gửi lệnh lên sàn để tăng khả năng khớp (VNĐ) | Activation Price Offset |
| Lệnh con | Lệnh thông thường (LO/MTL) được sinh ra từ lệnh điều kiện khi điều kiện kích hoạt được thỏa mãn | Child Order |
| Lệnh mẹ | Lệnh điều kiện Trailing Stop gốc | Parent Order / Conditional Order |
| Giá tham chiếu | Giá đóng cửa phiên trước, làm cơ sở tính trần/sàn | Reference Price |
| Bước giá | Đơn vị thay đổi giá tối thiểu theo quy định của sàn | Price Tick / Tick Size |
| Lô chẵn | Khối lượng là bội số của 100 | Round Lot |
| LO | Lệnh giới hạn - Limit Order | Limit Order (LO) |
| MTL | Lệnh thị trường - Market to Limit | Market to Limit (MTL) |
| HOSE | Sàn giao dịch Thành phố Hồ Chí Minh | Ho Chi Minh Stock Exchange |
| HNX | Sàn giao dịch Hà Nội | Hanoi Stock Exchange |
| UPCOM | Thị trường cổ phiếu của các công ty đại chúng chưa niêm yết | Unlisted Public Company Market |

### 1.4 Tài liệu tham khảo

- Quy định giao dịch của Sở Giao dịch Chứng khoán (HOSE, HNX, UPCOM)
- Tài liệu thiết kế hệ thống lệnh điều kiện (nếu có)
- UI/UX Design Document - Màn hình đặt lệnh Trailing Stop
- API Specification Document - Order Management Service

---

## 2. MỤC TIÊU KINH DOANH

### 2.1 Vấn đề cần giải quyết

**Vấn đề của nhà đầu tư:**
- Nhà đầu tư không thể theo dõi thị trường liên tục 24/7 để bảo vệ lợi nhuận
- Khó xác định điểm chốt lời tối ưu khi giá biến động mạnh
- Sợ bỏ lỡ xu hướng tăng/giảm tiếp khi chốt lời quá sớm
- Mất thời gian và căng thẳng tâm lý khi phải ra quyết định thủ công liên tục
- Không có công cụ tự động để "khóa lợi nhuận" khi giá di chuyển theo chiều có lợi

**Vấn đề của doanh nghiệp:**
- Khách hàng chưa có công cụ giao dịch nâng cao, dẫn đến trải nghiệm kém
- Thua kém đối thủ cạnh tranh đã cung cấp tính năng tương tự
- Khó thu hút và giữ chân nhà đầu tư chuyên nghiệp
- Doanh thu giao dịch hạn chế do thiếu công cụ hỗ trợ tự động hóa

### 2.2 Mục tiêu nghiệp vụ

| ID | Mục tiêu | Chỉ số đo lường | Giá trị mục tiêu | Thời hạn |
|----|----------|----------------|------------------|----------|
| OBJ-01 | Tăng số lượng giao dịch tự động | Số lệnh Trailing Stop đặt/tháng | 5,000 lệnh/tháng | 3 tháng sau go-live |
| OBJ-02 | Cải thiện trải nghiệm khách hàng | NPS (Net Promoter Score) | Tăng 15 điểm | 6 tháng sau go-live |
| OBJ-03 | Giữ chân khách hàng | Retention rate của active traders | Tăng 10% | 6 tháng sau go-live |
| OBJ-04 | Tăng tỷ lệ kích hoạt lệnh thành công | Tỷ lệ lệnh kích hoạt / tổng lệnh đặt | ≥ 70% | 3 tháng sau go-live |
| OBJ-05 | Giảm tải cho bộ phận hỗ trợ | Số ticket liên quan đến quản lý lệnh thủ công | Giảm 30% | 6 tháng sau go-live |

---

## 3. CÁC BÊN LIÊN QUAN

### 3.1 Stakeholders nghiệp vụ

| Vai trò | Họ tên | Trách nhiệm |
|---------|--------|-------------|
| Product Owner | [Tên] | Quyết định ưu tiên tính năng, chấp thuận yêu cầu nghiệp vụ |
| Business Analyst | [Tên] | Thu thập, phân tích yêu cầu, viết BRD |
| Compliance Officer | [Tên] | Đảm bảo tuân thủ quy định giao dịch chứng khoán |
| Customer Support Manager | [Tên] | Đào tạo đội ngũ hỗ trợ, thu thập phản hồi khách hàng |

### 3.2 Stakeholders kỹ thuật

| Vai trò | Họ tên | Trách nhiệm |
|---------|--------|-------------|
| Tech Lead | [Tên] | Thiết kế kiến trúc hệ thống, review technical solution |
| Backend Lead | [Tên] | Phát triển API, xử lý logic nghiệp vụ, tích hợp sàn |
| Frontend Lead | [Tên] | Phát triển UI đặt lệnh, sổ lệnh |
| QA Lead | [Tên] | Thiết kế test case, đảm bảo chất lượng |
| DevOps Engineer | [Tên] | Triển khai, giám sát hệ thống |

### 3.3 Người dùng cuối

- **Nhà đầu tư cá nhân (Retail Investors)**: Người dùng phổ thông, giao dịch qua mobile app/web, cần công cụ đơn giản để bảo vệ lợi nhuận
- **Nhà đầu tư chuyên nghiệp (Professional Traders)**: Trader có kinh nghiệm, sử dụng các chiến lược giao dịch nâng cao, cần tính năng tùy chỉnh chi tiết
- **Nhà đầu tư tổ chức (Institutional Investors)**: Quỹ đầu tư, công ty chứng khoán, cần công cụ quản lý danh mục tự động

---

## 4. YÊU CẦU CHỨC NĂNG

### 4.1 Tổng quan tính năng

Lệnh Trailing Stop là lệnh điều kiện cho phép nhà đầu tư đặt lệnh mua/bán với cơ chế tự động điều chỉnh giá kích hoạt theo biến động thị trường.

**Cơ chế hoạt động:**

**Với lệnh MUA Trailing Stop:**
- Giá kích hoạt ban đầu được đặt cao hơn giá thị trường hiện tại
- Khi giá thị trường giảm (có lợi cho người mua), giá kích hoạt tự động giảm theo để bám sát giá thị trường với khoảng cách = Biên độ trượt (D)
- Khi giá thị trường tăng trở lại (đảo chiều), giá kích hoạt giữ nguyên
- Khi giá thị trường tăng và chạm giá kích hoạt, lệnh được kích hoạt và gửi lệnh mua lên sàn

**Với lệnh BÁN Trailing Stop:**
- Giá kích hoạt ban đầu được đặt thấp hơn giá thị trường hiện tại
- Khi giá thị trường tăng (có lợi cho người bán), giá kích hoạt tự động tăng theo để bám sát giá thị trường với khoảng cách = Biên độ trượt (D)
- Khi giá thị trường giảm trở lại (đảo chiều), giá kích hoạt giữ nguyên
- Khi giá thị trường giảm và chạm giá kích hoạt, lệnh được kích hoạt và gửi lệnh bán lên sàn

**Ví dụ lệnh BÁN Trailing Stop:**
- Khách hàng nắm giữ cổ phiếu KBC, giá hiện tại: 35,000 VNĐ
- Đặt lệnh Bán Trailing Stop:
  - Giá kích hoạt ban đầu: 35,300 VNĐ
  - Biên độ trượt: 600 VNĐ
  - Bước giá kích hoạt: 500 VNĐ
  - Loại lệnh giao dịch: LO

| Thời điểm | Giá thị trường | Giá kích hoạt | Hành động hệ thống |
|-----------|----------------|---------------|--------------------|
| T0 | 35,000 | 35,300 | Lệnh ở trạng thái "Chờ kích hoạt" |
| T1 | 35,500 | 35,800 | Giá tăng 500 → Giá kích hoạt tăng 500 (35,800) |
| T2 | 36,000 | 36,300 | Giá tăng 500 → Giá kích hoạt tăng 500 (36,300) |
| T3 | 35,800 | 36,300 | Giá giảm 200 → Giá kích hoạt giữ nguyên (36,300) |
| T4 | 35,700 | 36,300 | Giá giảm xuống 35,700 → Chạm giá kích hoạt (35,700 < 36,300) |
|    |        |        | → Hệ thống kích hoạt lệnh, gửi lệnh bán LO giá 35,800 (= 36,300 + 500) lên sàn |

### 4.2 User Stories

#### Epic: Quản lý Lệnh Trailing Stop

| ID | User Story | Độ ưu tiên | Acceptance Criteria |
|----|------------|------------|---------------------|
| US-001 | Là nhà đầu tư, tôi muốn đặt lệnh Trailing Stop để tự động bảo vệ lợi nhuận khi giá đảo chiều | Must Have | • Điền đầy đủ các trường: Loại lệnh, Chiều, Khối lượng, Mã CK, Giá kích hoạt, Biên độ trượt, Bước giá kích hoạt, Thời gian hiệu lực, Loại lệnh giao dịch<br>• Hệ thống validate đầu vào theo đúng quy tắc<br>• Hiển thị cảnh báo nếu tham số không hợp lý (nhưng vẫn cho đặt)<br>• Lệnh được lưu với trạng thái "Chờ kích hoạt"<br>• Hiển thị thông báo thành công với mã lệnh |
| US-002 | Là nhà đầu tư, tôi muốn xem danh sách các lệnh Trailing Stop đã đặt để theo dõi trạng thái | Must Have | • Hiển thị sổ lệnh với các cột: Thời gian, Loại lệnh, Mã CK, Chiều, Khối lượng, Giá kích hoạt hiện tại, Biên độ trượt, Bước giá kích hoạt, Trạng thái, Ngày hết hạn<br>• Phân biệt rõ ràng các trạng thái bằng màu sắc/icon<br>• Cho phép filter theo trạng thái, mã CK, thời gian<br>• Cập nhật giá kích hoạt real-time cho lệnh đang "Chờ kích hoạt" |
| US-003 | Là nhà đầu tư, tôi muốn hủy lệnh Trailing Stop đang chờ kích hoạt để thay đổi chiến lược | Must Have | • Chỉ cho phép hủy lệnh có trạng thái "Chờ kích hoạt"<br>• Hiển thị dialog xác nhận trước khi hủy<br>• Lệnh chuyển sang trạng thái "Đã hủy" sau khi hủy thành công<br>• Hiển thị thông báo thành công/thất bại |
| US-004 | Là nhà đầu tư, tôi muốn nhận thông báo khi lệnh Trailing Stop được kích hoạt để biết lệnh đã được gửi lên sàn | Should Have | • Nhận thông báo push/email khi lệnh chuyển sang trạng thái "Đã kích hoạt"<br>• Thông báo chứa: Mã CK, Chiều, Khối lượng, Giá đặt lệnh con, Thời gian kích hoạt<br>• Nhận thông báo khi lệnh bị "Từ chối" với lý do cụ thể |
| US-005 | Là nhà đầu tư, tôi muốn hệ thống gợi ý khi tham số đặt lệnh không hợp lý để tránh sai sót | Should Have | • Hiển thị cảnh báo (warning) khi giá kích hoạt ban đầu không hợp lý (có thể kích hoạt ngay)<br>• Hiển thị cảnh báo khi biên độ trượt quá lớn (> 10% giá tham chiếu)<br>• Gợi ý giá trị phù hợp trong tooltip |
| US-006 | Là nhà đầu tư, tôi muốn xem lịch sử các lệnh Trailing Stop đã hết hạn để đánh giá chiến lược | Could Have | • Hiển thị danh sách lệnh có trạng thái "Hết hạn"<br>• Cho phép filter theo khoảng thời gian, mã CK<br>• Hiển thị đầy đủ thông tin lệnh và lý do hết hạn |

### 4.3 Yêu cầu chi tiết

#### 4.3.1 Chức năng 1: Đặt lệnh Trailing Stop

**Mô tả**: Cho phép khách hàng đặt lệnh Trailing Stop bằng cách điền/lựa chọn các tham số. Hệ thống validate đầu vào, lưu lệnh và bắt đầu theo dõi thị trường.

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. Khách hàng truy cập màn hình đặt lệnh Trailing Stop
2. Khách hàng chọn/điền các trường thông tin:
   - Loại lệnh: Trailing Stop (mặc định)
   - Chiều: Mua hoặc Bán
   - Mã CK: Nhập hoặc chọn từ danh sách
   - Khối lượng: Nhập số lượng cổ phiếu
   - Giá kích hoạt: Chọn "Giá hiện tại" hoặc "Nhập giá"
   - Biên độ trượt (D): Nhập giá trị (VNĐ)
   - Bước giá kích hoạt (delta): Nhập giá trị (VNĐ)
   - Thời gian hiệu lực: Chọn "Trong ngày" hoặc "Đến hạn" (chọn ngày)
   - Loại lệnh giao dịch: Chọn LO hoặc MTL
3. Hệ thống validate theo thời gian thực khi khách hàng nhập liệu
4. Hiển thị warning nếu tham số không hợp lý (nhưng vẫn cho tiếp tục)
5. Khách hàng nhấn "Đặt lệnh"
6. Hệ thống validate toàn bộ, nếu có lỗi hiển thị thông báo lỗi
7. Nếu hợp lệ, lưu lệnh với trạng thái "Chờ kích hoạt"
8. Hiển thị thông báo thành công với mã lệnh
9. Hệ thống bắt đầu theo dõi giá thị trường cho lệnh này

**Business Rules**:
- BR-001: Biên độ trượt phải > 0
- BR-002: Bước giá kích hoạt phải > 0 (khi chọn loại lệnh LO)
- BR-003: Biên độ trượt và Bước giá kích hoạt phải là bội số của bước giá
- BR-004: Khối lượng phải là bội số của 100 (lô chẵn)
- BR-005: Khối lượng phải > 0
- BR-006: Mã CK phải thuộc 3 sàn HOSE, HNX, UPCOM
- BR-007: Thời gian hiệu lực "Đến hạn" tối đa 30 ngày kể từ ngày đặt lệnh
- BR-008: Khi chọn MTL, bước giá kích hoạt = 0 (disable input)
- BR-009: Hệ thống KHÔNG kiểm tra sức mua/bán, giá trần/sàn khi đặt lệnh (chỉ kiểm tra khi kích hoạt)
- BR-010: Giá kích hoạt ban đầu (nếu KH chọn "Giá hiện tại") = Giá thị trường tại thời điểm đặt lệnh

**Validation Rules**:

| Trường | Quy tắc validate | Loại | Thông báo |
|--------|------------------|------|-----------|
| Khối lượng | Phải là số nguyên dương | Error | "Khối lượng phải là số nguyên dương" |
| Khối lượng | Phải là bội số của 100 | Error | "Khối lượng phải là bội số của 100 (lô chẵn)" |
| Mã CK | Phải nằm trong danh sách mã hợp lệ | Error | "Mã chứng khoán không hợp lệ" |
| Biên độ trượt | Phải > 0 | Error | "Biên độ trượt phải lớn hơn 0" |
| Biên độ trượt | Phải là bội số của bước giá | Error | "Biên độ trượt không đúng bước giá. Gợi ý: [giá gần nhất]" |
| Biên độ trượt | Không nên > 10% giá tham chiếu | Warning | "Biên độ trượt lớn (> 10% giá TC), lệnh có thể khó kích hoạt" |
| Bước giá kích hoạt | Phải > 0 (nếu chọn LO) | Error | "Bước giá kích hoạt phải lớn hơn 0" |
| Bước giá kích hoạt | Phải là bội số của bước giá | Error | "Bước giá kích hoạt không đúng bước giá. Gợi ý: [giá gần nhất]" |
| Giá kích hoạt (lệnh MUA) | Nên > Giá thị trường | Warning | "Giá kích hoạt ≤ Giá thị trường, lệnh có thể được kích hoạt ngay lập tức" |
| Giá kích hoạt (lệnh BÁN) | Nên < Giá thị trường | Warning | "Giá kích hoạt ≥ Giá thị trường, lệnh có thể được kích hoạt ngay lập tức" |
| Thời gian hiệu lực | Ngày hết hạn ≤ Ngày đặt lệnh + 30 ngày | Error | "Thời gian hiệu lực tối đa 30 ngày" |

**⚠️ Lưu ý về Error vs Warning:**
- **Error**: Chặn không cho đặt lệnh, khách hàng BẮT BUỘC phải sửa
- **Warning**: Cảnh báo, khách hàng có thể tiếp tục đặt lệnh sau khi xem cảnh báo

#### 4.3.2 Chức năng 2: Xem Sổ lệnh Trailing Stop

**Mô tả**: Hiển thị danh sách các lệnh Trailing Stop của khách hàng với đầy đủ thông tin và trạng thái. Giá kích hoạt được cập nhật real-time cho lệnh đang "Chờ kích hoạt".

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. Khách hàng truy cập màn hình "Sổ lệnh điều kiện"
2. Hệ thống hiển thị danh sách lệnh Trailing Stop, sắp xếp theo thời gian đặt lệnh (mới nhất trước)
3. Mỗi dòng hiển thị: Thời gian, Loại lệnh, Mã CK, Chiều, Khối lượng, Giá kích hoạt hiện tại, Biên độ trượt, Bước giá kích hoạt, Trạng thái, Ngày hết hạn, Actions
4. Giá kích hoạt của lệnh "Chờ kích hoạt" được cập nhật real-time khi giá thị trường thay đổi
5. Khách hàng có thể filter theo: Trạng thái, Mã CK, Khoảng thời gian
6. Khách hàng có thể sort theo: Thời gian, Mã CK, Trạng thái
7. Actions hiển thị tùy theo trạng thái: "Hủy lệnh" (chỉ với trạng thái "Chờ kích hoạt")

**Business Rules**:
- BR-011: Chỉ hiển thị lệnh của khách hàng đang đăng nhập
- BR-012: Giá kích hoạt hiển thị là giá hiện tại (đã được hệ thống điều chỉnh), không phải giá ban đầu
- BR-013: Lệnh "Hết hạn" không hiển thị trong Sổ lệnh chính, chỉ hiển thị trong "Lịch sử lệnh"
- BR-014: Trạng thái được phân biệt bằng màu sắc: Chờ kích hoạt (Vàng), Đã kích hoạt (Xanh), Đã hủy (Xám), Bị từ chối (Đỏ)

**Các trạng thái lệnh**:

| Trạng thái | Mô tả | Nơi hiển thị | Cho phép hủy | Cho phép sửa |
|-----------|-------|--------------|--------------|--------------|
| Chờ kích hoạt | Lệnh đang chờ điều kiện kích hoạt, hệ thống liên tục tính toán giá kích hoạt | Sổ lệnh điều kiện | Có | Không |
| Đã kích hoạt | Lệnh đã thỏa mãn điều kiện, lệnh con đã được sinh và gửi lên sàn | Sổ lệnh điều kiện | Không | Không |
| Đã hủy | Lệnh được hủy thành công bởi khách hàng | Sổ lệnh điều kiện | Không | Không |
| Hết hạn | Lệnh hết thời gian hiệu lực (cuối phiên nếu "Trong ngày", hoặc đến ngày hết hạn) | Lịch sử lệnh điều kiện | Không | Không |
| Bị từ chối | Lệnh thỏa mãn điều kiện kích hoạt nhưng lệnh con không được đẩy lên sàn thành công do không thỏa mãn điều kiện về sức mua/sức bán, giá trần/sàn, etc. | Sổ lệnh điều kiện | Không | Không |

#### 4.3.3 Chức năng 3: Hủy lệnh Trailing Stop

**Mô tả**: Cho phép khách hàng hủy lệnh Trailing Stop đang ở trạng thái "Chờ kích hoạt".

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. Khách hàng truy cập Sổ lệnh điều kiện
2. Với lệnh có trạng thái "Chờ kích hoạt", hiển thị nút "Hủy lệnh"
3. Khách hàng nhấn "Hủy lệnh"
4. Hệ thống hiển thị dialog xác nhận: "Bạn có chắc chắn muốn hủy lệnh [Mã lệnh] - [Mã CK] - [Chiều] [Khối lượng]?"
5. Khách hàng xác nhận "Đồng ý"
6. Hệ thống xử lý hủy lệnh:
   - Dừng theo dõi giá thị trường cho lệnh này
   - Cập nhật trạng thái lệnh thành "Đã hủy"
   - Lưu thời gian hủy
7. Hiển thị thông báo thành công: "Hủy lệnh thành công"
8. Cập nhật Sổ lệnh, lệnh hiển thị với trạng thái "Đã hủy"

**Business Rules**:
- BR-015: Chỉ cho phép hủy lệnh có trạng thái "Chờ kích hoạt"
- BR-016: Không thể hủy lệnh đã "Đã kích hoạt", "Đã hủy", "Hết hạn", "Bị từ chối"
- BR-017: Sau khi hủy thành công, lệnh không thể khôi phục
- BR-018: Nếu lệnh đang được xử lý (đang chuyển trạng thái), không cho phép hủy và hiển thị thông báo: "Lệnh đang được xử lý, vui lòng thử lại sau"

#### 4.3.4 Chức năng 4: Xử lý tự động - Theo dõi và điều chỉnh giá kích hoạt

**Mô tả**: Hệ thống tự động theo dõi giá thị trường, điều chỉnh giá kích hoạt theo cơ chế Trailing Stop, và kích hoạt lệnh khi điều kiện thỏa mãn.

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. Hệ thống liên tục lấy giá thị trường (realtime) cho tất cả lệnh đang "Chờ kích hoạt"
2. Với mỗi lệnh, so sánh giá thị trường hiện tại với giá kích hoạt hiện tại
3. Áp dụng logic điều chỉnh giá kích hoạt theo cơ chế Trailing Stop (chi tiết xem mục 6.1)
4. Nếu điều kiện kích hoạt được thỏa mãn:
   - Sinh lệnh con (LO hoặc MTL) với giá = Giá kích hoạt + Bước giá kích hoạt (với lệnh MUA) hoặc Giá kích hoạt - Bước giá kích hoạt (với lệnh BÁN)
   - Validate lệnh con (sức mua/bán, giá trần/sàn, trạng thái tài khoản)
   - Nếu hợp lệ: Gửi lệnh con lên sàn, cập nhật trạng thái lệnh mẹ thành "Đã kích hoạt"
   - Nếu không hợp lệ: Cập nhật trạng thái lệnh mẹ thành "Bị từ chối", lưu lý do
5. Gửi thông báo cho khách hàng về trạng thái lệnh
6. Nếu lệnh hết hạn: Cập nhật trạng thái thành "Hết hạn"

**Business Rules**:
- BR-019: Hệ thống kiểm tra giá thị trường với tần suất cao (recommend: mỗi giây hoặc mỗi tick giá)
- BR-020: Giá kích hoạt chỉ được điều chỉnh theo hướng có lợi cho khách hàng, không bao giờ điều chỉnh ngược lại
- BR-021: Khi kích hoạt lệnh, giá đặt lệnh con = Giá kích hoạt ± Bước giá kích hoạt (để tăng khả năng khớp)
- BR-022: Lệnh MTL không cần Bước giá kích hoạt (delta = 0)
- BR-023: Kiểm tra thời gian hiệu lực:
  - "Trong ngày": Hết hạn vào 14:45 (cuối phiên giao dịch)
  - "Đến hạn": Hết hạn vào 14:45 của ngày được chọn
- BR-024: Lệnh hết hạn chuyển sang trạng thái "Hết hạn" và dừng theo dõi
- BR-025: Khi kích hoạt lệnh, kiểm tra:
  - Sức mua/bán (margin available)
  - Giá trần/sàn
  - Trạng thái tài khoản (active/suspended)
  - Trạng thái mã CK (đang giao dịch/bị tạm ngừng)

### 4.4 Quy tắc nghiệp vụ tổng quát

| ID | Quy tắc | Hành động khi vi phạm |
|----|---------|----------------------|
| BR-001 | Biên độ trượt phải > 0 | Hiển thị lỗi, không cho đặt lệnh |
| BR-002 | Bước giá kích hoạt phải > 0 (khi chọn LO) | Hiển thị lỗi, không cho đặt lệnh |
| BR-003 | Biên độ trượt và Bước giá kích hoạt phải là bội số của bước giá | Hiển thị lỗi, không cho đặt lệnh |
| BR-004 | Khối lượng phải là bội số của 100 (lô chẵn) | Hiển thị lỗi, không cho đặt lệnh |
| BR-005 | Khối lượng phải > 0 | Hiển thị lỗi, không cho đặt lệnh |
| BR-006 | Mã CK phải thuộc 3 sàn HOSE, HNX, UPCOM | Hiển thị lỗi, không cho đặt lệnh |
| BR-007 | Thời gian hiệu lực "Đến hạn" tối đa 30 ngày | Hiển thị lỗi, không cho đặt lệnh |
| BR-008 | Khi chọn MTL, bước giá kích hoạt = 0 | Tự động disable input field |
| BR-009 | KHÔNG kiểm tra sức mua/bán, giá trần/sàn khi đặt lệnh | Chỉ kiểm tra khi kích hoạt lệnh |
| BR-010 | Giá kích hoạt ban đầu (nếu chọn "Giá hiện tại") = Giá thị trường | Lấy giá thị trường tại thời điểm đặt lệnh |
| BR-011 | Chỉ hiển thị lệnh của khách hàng đang đăng nhập | Filter theo customer_id |
| BR-012 | Giá kích hoạt hiển thị là giá hiện tại (đã điều chỉnh) | Không hiển thị giá ban đầu |
| BR-013 | Lệnh "Hết hạn" chỉ hiển thị trong "Lịch sử" | Không hiển thị trong Sổ lệnh chính |
| BR-014 | Trạng thái phân biệt bằng màu sắc | Chờ KH: Vàng, Đã KH: Xanh, Đã hủy: Xám, Bị TN: Đỏ |
| BR-015 | Chỉ cho phép hủy lệnh "Chờ kích hoạt" | Ẩn nút "Hủy" với các trạng thái khác |
| BR-016 | Không thể hủy lệnh đã kích hoạt/hủy/hết hạn/từ chối | Hiển thị thông báo lỗi nếu cố hủy |
| BR-017 | Sau khi hủy, lệnh không thể khôi phục | Soft delete trong DB |
| BR-018 | Không cho hủy nếu lệnh đang xử lý | Hiển thị: "Lệnh đang xử lý, vui lòng thử lại" |
| BR-019 | Kiểm tra giá thị trường với tần suất cao | Recommend: mỗi giây hoặc mỗi tick |
| BR-020 | Giá kích hoạt chỉ điều chỉnh theo hướng có lợi | Không bao giờ điều chỉnh ngược lại |
| BR-021 | Giá đặt lệnh con = Giá kích hoạt ± delta | Công thức cụ thể xem mục 6.1 |
| BR-022 | Lệnh MTL không cần Bước giá kích hoạt | delta = 0 cho MTL |
| BR-023 | Kiểm tra thời gian hiệu lực | "Trong ngày": 14:45, "Đến hạn": 14:45 ngày chọn |
| BR-024 | Lệnh hết hạn chuyển trạng thái "Hết hạn" | Dừng theo dõi giá |
| BR-025 | Kiểm tra điều kiện giao dịch khi kích hoạt | Sức mua/bán, trần/sàn, trạng thái TK, trạng thái CK |

### 4.5 Workflow & Process Flow

```
[Khách hàng đặt lệnh]
         ↓
[Validate đầu vào] ──→ Lỗi ──→ [Hiển thị thông báo lỗi]
         ↓ Hợp lệ
[Lưu lệnh với trạng thái "Chờ kích hoạt"]
         ↓
[Bắt đầu theo dõi giá thị trường]
         ↓
┌────────────────────────────────────┐
│   Loop: Mỗi giây (hoặc mỗi tick)   │
│                                     │
│  [Lấy giá thị trường hiện tại]     │
│           ↓                         │
│  [So sánh với giá kích hoạt]       │
│           ↓                         │
│  [Điều chỉnh giá kích hoạt nếu cần]│
│           ↓                         │
│  Có thỏa mãn điều kiện kích hoạt?  │
│      /        \                     │
│    Có        Không                  │
│    ↓           ↓                    │
│  [Kích hoạt] [Tiếp tục theo dõi]   │
│    ↓           ↓                    │
│    ↓      Hết hạn?                  │
│    ↓         / \                    │
│    ↓       Có  Không                │
│    ↓       ↓    ↓                   │
│    ↓   [Hết hạn] [Continue loop]   │
│    ↓                                │
└────┼────────────────────────────────┘
     ↓
[Validate điều kiện giao dịch]
     ↓
Hợp lệ?
  /    \
Có    Không
 ↓      ↓
[Gửi lệnh con lên sàn]  [Trạng thái: Bị từ chối]
 ↓
[Trạng thái: Đã kích hoạt]
 ↓
[Gửi thông báo cho KH]
```

**Workflow hủy lệnh:**
```
[KH nhấn "Hủy lệnh"]
         ↓
[Kiểm tra trạng thái]
         ↓
Trạng thái = "Chờ kích hoạt"?
      /        \
    Có         Không
     ↓           ↓
[Hiển thị dialog xác nhận] [Hiển thị lỗi: "Không thể hủy lệnh"]
     ↓
[KH xác nhận "Đồng ý"]
     ↓
[Dừng theo dõi giá]
     ↓
[Cập nhật trạng thái: "Đã hủy"]
     ↓
[Hiển thị thông báo thành công]
```

---

## 5. YÊU CẦU DỮ LIỆU

### 5.1 Input Specification

#### Đặt lệnh Trailing Stop

| Trường Input | Nguồn | Kiểu dữ liệu | Bắt buộc | Validation | Giá trị mặc định |
|--------------|-------|--------------|----------|------------|------------------|
| order_type | User | String | Y | Giá trị cố định: "TRAILING_STOP" | "TRAILING_STOP" |
| side | User | String (Enum) | Y | "BUY" hoặc "SELL" | - |
| symbol | User | String | Y | Mã CK thuộc HOSE, HNX, UPCOM | - |
| volume | User | Integer | Y | > 0, bội số của 100 | - |
| trigger_price_method | User | String (Enum) | Y | "MARKET" hoặc "MANUAL" | "MARKET" |
| trigger_price | User/System | Decimal | Y | > 0, bội số của bước giá | Giá thị trường (nếu method = "MARKET") |
| trailing_amount | User | Decimal | Y | > 0, bội số của bước giá | - |
| activation_price_offset | User | Decimal | Y (nếu LO) | ≥ 0, bội số của bước giá | 0 (nếu MTL) |
| validity_type | User | String (Enum) | Y | "DAY" hoặc "GTD" (Good Till Date) | "DAY" |
| expiry_date | User | Date | Y (nếu GTD) | ≤ Ngày đặt + 30 ngày | - |
| child_order_type | User | String (Enum) | Y | "LO" hoặc "MTL" | "LO" |
| customer_id | System | String | Y | Lấy từ session | - |
| account_number | System | String | Y | Lấy từ session | - |
| created_at | System | Timestamp | Y | Tự động sinh | Current timestamp |

### 5.2 Output Specification

#### Response: Đặt lệnh thành công

| Trường Output | Kiểu dữ liệu | Mô tả | Ví dụ |
|---------------|--------------|-------|-------|
| order_id | String (UUID) | Mã lệnh điều kiện duy nhất | "TS-20251117-000001" |
| status | String | Trạng thái lệnh | "ACTIVE" |
| message | String | Thông báo | "Đặt lệnh Trailing Stop thành công" |
| order_details | Object | Thông tin lệnh chi tiết | {...} |

#### Response: Sổ lệnh

| Trường Output | Kiểu dữ liệu | Mô tả | Ví dụ |
|---------------|--------------|-------|-------|
| orders | Array | Danh sách lệnh | [...] |
| total | Integer | Tổng số lệnh | 15 |
| page | Integer | Trang hiện tại | 1 |
| page_size | Integer | Số lệnh mỗi trang | 20 |

**Order Object:**

| Trường | Kiểu | Mô tả | Ví dụ |
|--------|------|-------|-------|
| order_id | String | Mã lệnh | "TS-20251117-000001" |
| created_at | Timestamp | Thời gian đặt lệnh | "2025-11-17 11:00:00" |
| order_type | String | Loại lệnh | "TRAILING_STOP" |
| side | String | Chiều | "BUY" / "SELL" |
| symbol | String | Mã CK | "KBC" |
| volume | Integer | Khối lượng | 100 |
| current_trigger_price | Decimal | Giá kích hoạt hiện tại | 35800.0 |
| initial_trigger_price | Decimal | Giá kích hoạt ban đầu | 35300.0 |
| trailing_amount | Decimal | Biên độ trượt | 600.0 |
| activation_price_offset | Decimal | Bước giá kích hoạt | 500.0 |
| child_order_type | String | Loại lệnh giao dịch | "LO" / "MTL" |
| status | String | Trạng thái | "ACTIVE" / "TRIGGERED" / "CANCELLED" / "EXPIRED" / "REJECTED" |
| expiry_date | Date | Ngày hết hạn | "2025-11-19" |
| reason | String | Lý do (với trạng thái REJECTED) | "Insufficient buying power" |

#### Response: Hủy lệnh thành công

| Trường Output | Kiểu dữ liệu | Mô tả | Ví dụ |
|---------------|--------------|-------|-------|
| order_id | String | Mã lệnh đã hủy | "TS-20251117-000001" |
| status | String | Trạng thái mới | "CANCELLED" |
| message | String | Thông báo | "Hủy lệnh thành công" |
| cancelled_at | Timestamp | Thời gian hủy | "2025-11-17 13:30:00" |

### 5.3 Data Validation Rules

| Validation | Mô tả | Điều kiện | Thông báo |
|------------|-------|-----------|-----------|
| VAL-001 | Khối lượng hợp lệ | volume > 0 AND volume % 100 == 0 | "Khối lượng phải là số nguyên dương và là bội số của 100" |
| VAL-002 | Mã CK hợp lệ | symbol IN (danh_sach_ma_hop_le) | "Mã chứng khoán không hợp lệ hoặc không được hỗ trợ" |
| VAL-003 | Biên độ trượt hợp lệ | trailing_amount > 0 AND trailing_amount % tick_size == 0 | "Biên độ trượt phải > 0 và là bội số của bước giá" |
| VAL-004 | Bước giá kích hoạt hợp lệ (LO) | activation_price_offset > 0 AND activation_price_offset % tick_size == 0 (nếu child_order_type == "LO") | "Bước giá kích hoạt phải > 0 và là bội số của bước giá" |
| VAL-005 | Thời gian hiệu lực hợp lệ | expiry_date <= created_date + 30 (nếu validity_type == "GTD") | "Thời gian hiệu lực tối đa 30 ngày" |
| VAL-006 | Giá kích hoạt hợp lệ | trigger_price > 0 AND trigger_price % tick_size == 0 | "Giá kích hoạt phải > 0 và là bội số của bước giá" |
| VAL-007 | Biên độ trượt không quá lớn (Warning) | trailing_amount <= reference_price * 0.1 | "Biên độ trượt lớn (> 10% giá tham chiếu), lệnh có thể khó kích hoạt" |
| VAL-008 | Giá kích hoạt hợp lý - Lệnh MUA (Warning) | trigger_price > market_price (nếu side == "BUY") | "Giá kích hoạt ≤ Giá thị trường, lệnh có thể được kích hoạt ngay lập tức" |
| VAL-009 | Giá kích hoạt hợp lý - Lệnh BÁN (Warning) | trigger_price < market_price (nếu side == "SELL") | "Giá kích hoạt ≥ Giá thị trường, lệnh có thể được kích hoạt ngay lập tức" |
| VAL-010 | Trạng thái cho phép hủy | status == "ACTIVE" | "Chỉ có thể hủy lệnh đang ở trạng thái 'Chờ kích hoạt'" |

---

## 6. CHI TIẾT IPO (INPUT - PROCESS - OUTPUT)

### 6.1 IPO Flow cho Đặt lệnh Trailing Stop

#### INPUT

**User Input:**

| Tham số | Mô tả | Kiểu | Bắt buộc | Ví dụ |
|---------|-------|------|----------|-------|
| side | Chiều lệnh (Mua/Bán) | String | Y | "BUY" |
| symbol | Mã chứng khoán | String | Y | "KBC" |
| volume | Khối lượng | Integer | Y | 100 |
| trigger_price_method | Phương thức xác định giá kích hoạt | String | Y | "MARKET" / "MANUAL" |
| trigger_price | Giá kích hoạt ban đầu (nếu MANUAL) | Decimal | Y (nếu MANUAL) | 35300 |
| trailing_amount | Biên độ trượt (VNĐ) | Decimal | Y | 600 |
| activation_price_offset | Bước giá kích hoạt (VNĐ) | Decimal | Y (nếu LO) | 500 |
| validity_type | Loại thời gian hiệu lực | String | Y | "DAY" / "GTD" |
| expiry_date | Ngày hết hạn (nếu GTD) | Date | Y (nếu GTD) | "2025-11-19" |
| child_order_type | Loại lệnh giao dịch (LO/MTL) | String | Y | "LO" |

**System Input:**

| Tham số | Mô tả | Nguồn | Ví dụ |
|---------|-------|-------|-------|
| customer_id | Mã khách hàng | Session | "KH123456" |
| account_number | Số tài khoản | Session | "0001234567" |
| market_price | Giá thị trường hiện tại | Market data service | 35000 |
| reference_price | Giá tham chiếu (TC) | Market data service | 34500 |
| tick_size | Bước giá của mã CK | Stock info service | 100 |
| created_at | Thời gian đặt lệnh | System clock | "2025-11-17 11:00:00" |

#### PROCESS

**Các bước xử lý:**

**Bước 1: Validate Input**
- Validate khối lượng: Phải > 0, là bội số của 100 (lô chẵn)
- Validate mã CK: Phải thuộc danh sách mã hợp lệ (HOSE, HNX, UPCOM)
- Validate biên độ trượt: Phải > 0, là bội số của bước giá
- Validate bước giá kích hoạt: Phải > 0, là bội số của bước giá (chỉ với LO), disable với MTL
- Validate giá kích hoạt: Nếu MARKET thì lấy giá thị trường, nếu MANUAL thì validate > 0 và đúng bước giá
- Validate thời gian hiệu lực: Tối đa 30 ngày (GTD), hoặc cuối phiên (DAY)

**Bước 2: Kiểm tra Cảnh báo (Warning)**
- Cảnh báo nếu biên độ trượt > 10% giá tham chiếu
- Cảnh báo nếu lệnh MUA có giá kích hoạt ≤ giá thị trường
- Cảnh báo nếu lệnh BÁN có giá kích hoạt ≥ giá thị trường
- Hiển thị warning cho user nhưng vẫn cho phép đặt lệnh nếu user xác nhận

**Bước 3: Tạo Order Record**
- Generate order_id theo format: TS-YYYYMMDD-NNNNNN
- Tạo order object với đầy đủ thông tin: giá kích hoạt ban đầu, giá kích hoạt hiện tại, giá đỉnh/đáy
- Set trạng thái: ACTIVE

**Bước 4: Lưu Database**
- Insert order vào bảng `conditional_orders` (trong transaction)
- Log audit trail vào bảng `order_audit_log`
- Rollback nếu có lỗi

**Bước 5: Đăng ký Market Data**
- Đưa order vào hàng đợi theo dõi: `market_monitoring_queue`
- Subscribe market data stream cho symbol

**Business Logic:**

- Giá kích hoạt ban đầu: Giá thị trường (MARKET) hoặc giá khách hàng nhập (MANUAL)
- Lưu cả `initial_trigger_price` và `current_trigger_price` (sẽ được cập nhật liên tục)
- Lưu `highest_price` (lệnh BÁN) hoặc `lowest_price` (lệnh MUA) để theo dõi giá đỉnh/đáy
- Không kiểm tra sức mua/bán tại thời điểm đặt lệnh (chỉ kiểm tra khi kích hoạt)

**Error Handling:**

- Lỗi validate: Trả về error code và message, không cho đặt lệnh
- Lỗi database: Rollback transaction, trả về error 500
- Lỗi market data: Trả về error 503

#### OUTPUT

**Success Response:**

```json
{
    "status": "success",
    "code": 200,
    "message": "Đặt lệnh Trailing Stop thành công",
    "data": {
        "order_id": "TS-20251117-000001",
        "status": "ACTIVE",
        "symbol": "KBC",
        "side": "BUY",
        "volume": 100,
        "initial_trigger_price": 35300,
        "current_trigger_price": 35300,
        "trailing_amount": 600,
        "activation_price_offset": 500,
        "child_order_type": "LO",
        "expiry_date": "2025-11-19 14:45:00",
        "created_at": "2025-11-17 11:00:00"
    },
    "warnings": [
        "Giá kích hoạt ≤ Giá thị trường, lệnh có thể được kích hoạt ngay lập tức"
    ]
}
```

**Error Response:**

| Error Code | Mô tả | HTTP Status | Message |
|------------|-------|-------------|---------|
| VAL-001 | Khối lượng không hợp lệ | 400 | "Khối lượng phải là số nguyên dương và là bội số của 100" |
| VAL-002 | Mã CK không hợp lệ | 400 | "Mã chứng khoán không hợp lệ hoặc không được hỗ trợ" |
| VAL-003 | Biên độ trượt không hợp lệ | 400 | "Biên độ trượt phải > 0 và là bội số của bước giá. Gợi ý: [giá]" |
| VAL-004 | Bước giá kích hoạt không hợp lệ | 400 | "Bước giá kích hoạt phải > 0 và là bội số của bước giá. Gợi ý: [giá]" |
| VAL-005 | Thời gian hiệu lực không hợp lệ | 400 | "Thời gian hiệu lực tối đa 30 ngày" |
| VAL-006 | Giá kích hoạt không hợp lệ | 400 | "Giá kích hoạt phải > 0 và là bội số của bước giá. Gợi ý: [giá]" |
| SYS-001 | Lỗi hệ thống | 500 | "Không thể tạo lệnh, vui lòng thử lại sau" |
| SYS-002 | Lỗi lấy giá thị trường | 503 | "Không lấy được giá thị trường, vui lòng thử lại" |

---

### 6.2 IPO Flow cho Theo dõi và Kích hoạt lệnh Trailing Stop

#### INPUT

**System Input (Real-time):**

| Tham số | Mô tả | Nguồn | Ví dụ |
|---------|-------|-------|-------|
| order_id | Mã lệnh đang theo dõi | Database | "TS-20251117-000001" |
| current_market_price | Giá thị trường hiện tại | Market data stream | 35800 |
| current_trigger_price | Giá kích hoạt hiện tại | Database | 36300 |
| trailing_amount | Biên độ trượt | Database | 600 |
| side | Chiều lệnh | Database | "SELL" |
| highest_price | Giá cao nhất (với lệnh BÁN) | Database | 36000 |
| lowest_price | Giá thấp nhất (với lệnh MUA) | Database | null |
| expiry_date | Ngày hết hạn | Database | "2025-11-19 14:45:00" |
| current_time | Thời gian hiện tại | System clock | "2025-11-17 13:30:00" |

#### PROCESS

**Các bước xử lý (chạy liên tục cho mỗi lệnh ACTIVE):**

**Bước 1: Kiểm tra Thời gian Hiệu lực**
- Nếu `current_time >= expiry_date`:
  - Cập nhật trạng thái → EXPIRED
  - Dừng theo dõi market data
  - Gửi thông báo ORDER_EXPIRED

**Bước 2: Cập nhật Giá Đỉnh/Đáy và Điều chỉnh Giá Kích hoạt**

**Với lệnh BÁN:**
- Theo dõi giá cao nhất: Nếu giá thị trường > `highest_price` → cập nhật `highest_price`
- Điều chỉnh giá kích hoạt lên: `new_trigger_price = market_price - trailing_amount`
- Chỉ tăng giá kích hoạt (không giảm): Nếu `new_trigger_price > current_trigger_price` → cập nhật
- Điều kiện kích hoạt: `market_price <= current_trigger_price`

**Với lệnh MUA:**
- Theo dõi giá thấp nhất: Nếu giá thị trường < `lowest_price` → cập nhật `lowest_price`
- Điều chỉnh giá kích hoạt xuống: `new_trigger_price = market_price + trailing_amount`
- Chỉ giảm giá kích hoạt (không tăng): Nếu `new_trigger_price < current_trigger_price` → cập nhật
- Điều kiện kích hoạt: `market_price >= current_trigger_price`

**Bước 3: Kích hoạt Lệnh (nếu điều kiện thỏa mãn)**
- Tính giá lệnh con:
  - Lệnh MUA: `child_price = trigger_price + activation_offset`
  - Lệnh BÁN: `child_price = trigger_price - activation_offset`
  - Lệnh MTL: `child_price = 0` (market order)
- Validate điều kiện giao dịch:
  - Trạng thái tài khoản: Phải ACTIVE
  - Trạng thái mã CK: Không bị HALTED/SUSPENDED
  - Giá trần/sàn: Giá lệnh con không vượt giá trần/sàn
  - Sức mua/bán: Đủ sức mua (BUY) hoặc đủ khối lượng CK (SELL)
- Nếu validation FAIL → Cập nhật trạng thái REJECTED, gửi thông báo
- Nếu validation OK:
  - Tạo lệnh con và gửi lên sàn
  - Nếu gửi thành công → Cập nhật trạng thái TRIGGERED, gửi thông báo
  - Nếu gửi thất bại → Cập nhật trạng thái REJECTED, gửi thông báo

**Business Logic:**

- Giá kích hoạt chỉ được điều chỉnh theo hướng có lợi (BÁN: chỉ TĂNG, MUA: chỉ GIẢM)
- Điều kiện kích hoạt: BÁN (giá TT ≤ giá kích hoạt), MUA (giá TT ≥ giá kích hoạt)
- Giá lệnh con = Giá kích hoạt ± Bước giá (để tăng khả năng khớp)
- MTL: Không cần bước giá kích hoạt

**Error Handling:**

- Lỗi market data: Log error, retry sau 5 giây
- Lỗi validation: Trạng thái REJECTED, lưu lý do, gửi thông báo
- Lỗi gửi lệnh: Trạng thái REJECTED, lưu lý do, gửi thông báo
- Lỗi database: Log error, retry sau 1 giây

#### OUTPUT

**Success - Lệnh được kích hoạt:**

```json
{
    "event": "ORDER_TRIGGERED",
    "order_id": "TS-20251117-000001",
    "child_order_id": "LO-20251117-000123",
    "status": "TRIGGERED",
    "triggered_at": "2025-11-17 13:30:00",
    "child_order_details": {
        "symbol": "KBC",
        "side": "SELL",
        "volume": 100,
        "order_type": "LO",
        "price": 35800,
        "status": "PENDING"
    }
}
```

**Success - Giá kích hoạt được cập nhật:**

```json
{
    "event": "TRIGGER_PRICE_UPDATED",
    "order_id": "TS-20251117-000001",
    "old_trigger_price": 35800,
    "new_trigger_price": 36300,
    "highest_price": 36000,
    "updated_at": "2025-11-17 13:25:00"
}
```

**Error - Lệnh bị từ chối:**

```json
{
    "event": "ORDER_REJECTED",
    "order_id": "TS-20251117-000001",
    "status": "REJECTED",
    "reason": "Sức mua không đủ",
    "rejected_at": "2025-11-17 13:30:00"
}
```

**Error - Lệnh hết hạn:**

```json
{
    "event": "ORDER_EXPIRED",
    "order_id": "TS-20251117-000001",
    "status": "EXPIRED",
    "expired_at": "2025-11-19 14:45:00"
}
```

---

### 6.3 IPO Flow cho Hủy lệnh Trailing Stop

#### INPUT

**User Input:**

| Tham số | Mô tả | Kiểu | Bắt buộc | Ví dụ |
|---------|-------|------|----------|-------|
| order_id | Mã lệnh cần hủy | String | Y | "TS-20251117-000001" |

**System Input:**

| Tham số | Mô tả | Nguồn | Ví dụ |
|---------|-------|-------|-------|
| customer_id | Mã khách hàng | Session | "KH123456" |
| current_status | Trạng thái lệnh hiện tại | Database | "ACTIVE" |
| current_time | Thời gian hủy | System clock | "2025-11-17 13:30:00" |

#### PROCESS

**Các bước xử lý:**

**Bước 1: Validate Quyền Hủy lệnh**
- Kiểm tra lệnh tồn tại: `GET_ORDER_BY_ID(order_id)` → Nếu NULL → Error 404
- Kiểm tra quyền sở hữu: `order.customer_id == customer_id` → Nếu khác → Error 403
- Kiểm tra trạng thái: `order.status == "ACTIVE"` → Nếu khác → Error 400
- Kiểm tra lock: `order.is_processing == FALSE` → Nếu TRUE → Error 409 (đang xử lý)

**Bước 2: Lock Lệnh**
- Set `is_processing = TRUE` (trong transaction) để tránh race condition

**Bước 3: Hủy Lệnh**
- Cập nhật trạng thái → CANCELLED
- Set `cancelled_at`, `cancellation_reason = "Cancelled by user"`
- Unlock: Set `is_processing = FALSE`
- Log audit trail (trong transaction)
- Rollback nếu có lỗi

**Bước 4: Dừng Theo dõi Market Data**
- Unsubscribe market data: `market_data_service.unsubscribe()`
- Xóa khỏi hàng đợi: `market_monitoring_queue.remove()`

**Bước 5: Gửi Thông báo**
- Gửi notification ORDER_CANCELLED cho customer

**Business Logic:**

- Chỉ cho phép hủy lệnh trạng thái ACTIVE (Chờ kích hoạt)
- Sử dụng optimistic locking (`is_processing` flag) để tránh race condition
- Soft delete: Lưu lại lệnh với trạng thái CANCELLED (không xóa)
- Log audit trail đầy đủ

**Error Handling:**

- Lỗi không tìm thấy lệnh: Error 404
- Lỗi không có quyền: Error 403
- Lỗi trạng thái không hợp lệ: Error 400
- Lỗi race condition: Error 409 (retry)
- Lỗi database: Rollback, Error 500

#### OUTPUT

**Success Response:**

```json
{
    "status": "success",
    "code": 200,
    "message": "Hủy lệnh thành công",
    "data": {
        "order_id": "TS-20251117-000001",
        "status": "CANCELLED",
        "cancelled_at": "2025-11-17 13:30:00"
    }
}
```

**Error Response:**

| Error Code | Mô tả | HTTP Status | Message |
|------------|-------|-------------|---------|
| ORD-001 | Không tìm thấy lệnh | 404 | "Không tìm thấy lệnh" |
| ORD-002 | Không có quyền | 403 | "Bạn không có quyền hủy lệnh này" |
| ORD-003 | Trạng thái không hợp lệ | 400 | "Chỉ có thể hủy lệnh đang ở trạng thái 'Chờ kích hoạt'" |
| ORD-004 | Lệnh đang xử lý | 409 | "Lệnh đang được xử lý, vui lòng thử lại sau" |
| SYS-001 | Lỗi hệ thống | 500 | "Không thể hủy lệnh, vui lòng thử lại sau" |

---

### 6.4 State Diagram

```
[START] → [ACTIVE] ────────────────────────┐
           │                                │
           │ (Điều kiện kích hoạt thỏa mãn) │
           │ AND Validate thành công        │
           ↓                                │
       [TRIGGERED] (Terminal)               │
                                            │
[ACTIVE] ──────────────────────────────────┤
           │                                │
           │ (Khách hàng hủy lệnh)          │
           ↓                                │
       [CANCELLED] (Terminal)               │
                                            │
[ACTIVE] ──────────────────────────────────┤
           │                                │
           │ (Hết thời gian hiệu lực)       │
           ↓                                │
       [EXPIRED] (Terminal)                 │
                                            │
[ACTIVE] ──────────────────────────────────┘
           │
           │ (Điều kiện kích hoạt thỏa mãn)
           │ BUT Validate thất bại
           ↓
       [REJECTED] (Terminal)
```

**Trạng thái (States):**

| Trạng thái | Mô tả | Trạng thái tiếp theo có thể | Terminal State |
|------------|-------|----------------------------|----------------|
| ACTIVE | Lệnh đang chờ điều kiện kích hoạt, hệ thống theo dõi giá thị trường và điều chỉnh giá kích hoạt liên tục | TRIGGERED, CANCELLED, EXPIRED, REJECTED | No |
| TRIGGERED | Lệnh đã thỏa mãn điều kiện kích hoạt, lệnh con đã được tạo và gửi lên sàn thành công | - | Yes |
| CANCELLED | Lệnh đã được khách hàng hủy | - | Yes |
| EXPIRED | Lệnh hết thời gian hiệu lực mà chưa kích hoạt | - | Yes |
| REJECTED | Lệnh thỏa mãn điều kiện kích hoạt nhưng bị từ chối do không đủ điều kiện giao dịch (sức mua/bán, giá trần/sàn, etc.) | - | Yes |

**Chuyển trạng thái (Transitions):**

| Từ trạng thái | Sự kiện | Điều kiện | Đến trạng thái | Side Effects |
|---------------|---------|-----------|----------------|--------------|
| ACTIVE | Market price triggers condition | (Lệnh BÁN: market_price <= trigger_price) OR (Lệnh MUA: market_price >= trigger_price) AND Validation thành công | TRIGGERED | • Tạo lệnh con (LO/MTL)<br>• Gửi lệnh con lên sàn<br>• Dừng theo dõi giá<br>• Gửi thông báo cho KH |
| ACTIVE | Market price triggers condition | (Lệnh BÁN: market_price <= trigger_price) OR (Lệnh MUA: market_price >= trigger_price) AND Validation thất bại | REJECTED | • Dừng theo dõi giá<br>• Lưu lý do từ chối<br>• Gửi thông báo cho KH |
| ACTIVE | Customer cancels order | Status == "ACTIVE" AND customer có quyền | CANCELLED | • Dừng theo dõi giá<br>• Lưu thời gian hủy<br>• Gửi thông báo cho KH |
| ACTIVE | Expiry time reached | current_time >= expiry_date | EXPIRED | • Dừng theo dõi giá<br>• Gửi thông báo cho KH |
| ACTIVE | Market price moves favorably | (Lệnh BÁN: market_price tăng) OR (Lệnh MUA: market_price giảm) | ACTIVE | • Cập nhật current_trigger_price<br>• Cập nhật highest_price/lowest_price<br>• Lưu vào database |

---

## 7. YÊU CẦU GIAO DIỆN NGƯỜI DÙNG

### 7.1 Màn hình đặt lệnh Trailing Stop

**Tên màn hình**: Đặt lệnh Trailing Stop

**Mục đích**: Cho phép khách hàng đặt lệnh Trailing Stop với đầy đủ tham số

**Layout**:
```
+------------------------------------------------------------------+
|  HEADER: Đặt lệnh Trailing Stop                        [X Close] |
+------------------------------------------------------------------+
|                                                                  |
|  Loại lệnh: [Trailing Stop ▼]  (Dropdown, disabled)             |
|                                                                  |
|  Chiều:  ( ) Mua   (•) Bán      (Radio buttons)                  |
|                                                                  |
|  Mã chứng khoán:  [KBC        ▼]  (Autocomplete dropdown)       |
|                   Giá TC: 34,500 | Trần: 36,200 | Sàn: 32,800    |
|                   Giá hiện tại: 35,000 | +500 (+1.45%)           |
|                                                                  |
|  Khối lượng:      [100    ] [+] [-]                              |
|                   (Input number with +/- buttons)                |
|                                                                  |
|  Giá kích hoạt:   ( ) Giá hiện tại  (•) Nhập giá                 |
|                   [35,300    ]  VNĐ                              |
|                   ⓘ Giá mà khi thị trường đạt đến, lệnh sẽ kích |
|                      hoạt và chuyển thành lệnh thông thường      |
|                                                                  |
|  Biên độ trượt:   [600      ]  VNĐ                               |
|                   ⓘ Khoảng cách giá để xác định điểm đảo chiều   |
|                   ⚠️ Biên độ trượt lớn (> 10% giá TC)             |
|                                                                  |
|  Bước giá kích hoạt: [500   ]  VNĐ                               |
|                   ⓘ Khoảng giá cộng/trừ khi đặt lệnh lên sàn    |
|                      để tăng khả năng khớp (Gợi ý: 100-1,000)    |
|                                                                  |
|  Thời gian hiệu lực:  (•) Trong ngày   ( ) Đến hạn               |
|                   [ Chọn ngày ]  (Date picker, disabled)         |
|                                                                  |
|  Loại lệnh giao dịch:  (•) LO   ( ) MTL                          |
|                                                                  |
|  ┌────────────────────────────────────────────────────────────┐ |
|  │  TÓM TẮT LỆNH                                              │ |
|  │                                                            │ |
|  │  Bán 100 CP KBC                                           │ |
|  │  Giá kích hoạt: 35,300 VNĐ                                │ |
|  │  Biên độ trượt: 600 VNĐ                                   │ |
|  │  Khi kích hoạt, gửi lệnh LO bán giá: 34,800 VNĐ           │ |
|  │  (= 35,300 - 500)                                         │ |
|  │                                                            │ |
|  │  ⚠️ CẢNH BÁO:                                              │ |
|  │  • Giá kích hoạt ≥ Giá TT, lệnh có thể kích hoạt ngay    │ |
|  │  • Biên độ trượt lớn (> 10% giá TC)                       │ |
|  └────────────────────────────────────────────────────────────┘ |
|                                                                  |
|                       [Hủy]    [Đặt lệnh]                        |
|                                                                  |
+------------------------------------------------------------------+
```

**Các trường dữ liệu**:

| Tên trường | Loại control | Bắt buộc | Giá trị mặc định | Ghi chú |
|------------|--------------|----------|------------------|---------|
| Loại lệnh | Dropdown | Y | "Trailing Stop" | Disabled (cố định) |
| Chiều | Radio button | Y | - | Mua / Bán |
| Mã CK | Autocomplete dropdown | Y | - | Gợi ý khi gõ, hiển thị giá TC/trần/sàn/hiện tại |
| Khối lượng | Number input + +/- buttons | Y | - | Cho phép tăng/giảm 100 mỗi lần nhấn |
| Giá kích hoạt | Radio + Number input | Y | "Giá hiện tại" | Radio: Giá hiện tại / Nhập giá |
| Biên độ trượt | Number input | Y | - | Đơn vị VNĐ |
| Bước giá kích hoạt | Number input | Y | - | Đơn vị VNĐ, Disabled nếu chọn MTL |
| Thời gian hiệu lực | Radio + Date picker | Y | "Trong ngày" | Radio: Trong ngày / Đến hạn |
| Ngày hết hạn | Date picker | Y (nếu chọn GTD) | - | Tối đa +30 ngày |
| Loại lệnh giao dịch | Radio button | Y | "LO" | LO / MTL |

**Actions**:
- Button "Hủy": Đóng dialog, không lưu dữ liệu
- Button "Đặt lệnh":
  - Validate toàn bộ input
  - Nếu có warning, hiển thị dialog xác nhận trước khi đặt
  - Nếu hợp lệ, gửi request đặt lệnh
  - Hiển thị loading state khi đang xử lý
  - Hiển thị thông báo thành công/thất bại
  - Đóng dialog sau khi thành công

**Validation & Error Display**:
- Validate real-time khi user nhập liệu
- Hiển thị error message màu đỏ bên dưới trường nhập có lỗi
- Warning hiển thị màu vàng trong khung "TÓM TẮT LỆNH"
- Tooltip (ⓘ) giải thích ý nghĩa của từng trường
- Khi có lỗi, disable nút "Đặt lệnh"

**Tương tác động (Dynamic behavior):**
- Khi chọn mã CK: Hiển thị giá TC, trần, sàn, giá hiện tại
- Khi chọn "Giá hiện tại": Tự động điền giá thị trường vào ô "Giá kích hoạt"
- Khi chọn MTL: Disable ô "Bước giá kích hoạt", set giá trị = 0
- Khi chọn LO: Enable ô "Bước giá kích hoạt"
- Khi chọn "Đến hạn": Enable date picker
- Khi chọn "Trong ngày": Disable date picker
- Tự động tính và hiển thị giá đặt lệnh con trong "TÓM TẮT LỆNH"
- Hiển thị warning real-time khi nhập tham số không hợp lý

### 7.2 Bảng Sổ lệnh Trailing Stop

**Tên bảng**: Sổ lệnh điều kiện Trailing Stop

**Các cột hiển thị**:

| Tên cột | Kiểu dữ liệu | Có thể sort | Có thể filter | Mô tả |
|---------|--------------|-------------|---------------|-------|
| Thời gian | Timestamp | Y | Y (range) | Thời gian đặt lệnh (DD/MM/YYYY HH:mm:ss) |
| Loại lệnh | String | N | Y (dropdown) | "Trailing Stop" |
| Mã CK | String | Y | Y (search) | Mã chứng khoán |
| Chiều | String | N | Y (dropdown) | "Mua" / "Bán" (màu xanh/đỏ) |
| Khối lượng | Integer | Y | N | Khối lượng đặt |
| Giá KH ban đầu | Decimal | Y | N | Giá kích hoạt ban đầu (VNĐ) |
| Giá KH hiện tại | Decimal | Y | N | Giá kích hoạt hiện tại (VNĐ) - **Real-time update** |
| Biên độ trượt | Decimal | Y | N | Biên độ trượt (VNĐ) |
| Bước giá KH | Decimal | Y | N | Bước giá kích hoạt (VNĐ) |
| Loại lệnh GD | String | N | Y (dropdown) | "LO" / "MTL" |
| Trạng thái | String | N | Y (dropdown) | Chờ KH / Đã KH / Đã hủy / Bị TN (với màu sắc) |
| Ngày hết hạn | Date | Y | Y (range) | Ngày hết hạn hiệu lực |
| Actions | Buttons | N | N | Nút "Hủy lệnh" (nếu trạng thái = Chờ KH) |

**Actions trên dòng**:
- **Hủy lệnh**:
  - Chỉ hiển thị với lệnh có trạng thái "Chờ kích hoạt"
  - Khi nhấn, hiển thị dialog xác nhận
  - Sau khi xác nhận, gửi request hủy lệnh
  - Hiển thị loading state trên nút
  - Cập nhật trạng thái sau khi hủy thành công

**Màu sắc trạng thái**:
- **Chờ kích hoạt**: Nền vàng nhạt, text vàng đậm
- **Đã kích hoạt**: Nền xanh nhạt, text xanh đậm
- **Đã hủy**: Nền xám nhạt, text xám đậm
- **Bị từ chối**: Nền đỏ nhạt, text đỏ đậm

**Pagination**:
- Số bản ghi mỗi trang: 20 (có thể chọn 10/20/50/100)
- Loại pagination: Server-side (do dữ liệu có thể lớn)
- Hiển thị: "Hiển thị 1-20 của 150 lệnh" + Previous/Next buttons

**Filter panel**:
```
+------------------------------------------------------------------+
| BỘ LỌC                                                [Thu gọn] |
+------------------------------------------------------------------+
| Trạng thái:     [ ] Chờ kích hoạt  [ ] Đã kích hoạt             |
|                 [ ] Đã hủy  [ ] Bị từ chối                      |
|                                                                  |
| Mã CK:          [_____________] (Search input)                   |
|                                                                  |
| Thời gian:      [__/__/____] đến [__/__/____]                   |
|                                                                  |
| Loại lệnh GD:   [ ] LO  [ ] MTL                                  |
|                                                                  |
|                       [Xóa bộ lọc]    [Áp dụng]                 |
+------------------------------------------------------------------+
```

**Real-time update**:
- Cột "Giá KH hiện tại" được cập nhật real-time qua WebSocket
- Khi giá thay đổi, highlight dòng trong 2 giây (hiệu ứng fade)
- Khi trạng thái thay đổi (ví dụ: Chờ KH → Đã KH), highlight dòng và hiển thị notification

---

## 8. PHỤ LỤC

### 8.1 Wireframes/Mockups

**⚠️ Lưu ý**: Wireframes chi tiết sẽ được cung cấp bởi UI/UX team trong tài liệu riêng.

Tham khảo:
- Link Figma: [Sẽ cập nhật]
- Folder: [Sẽ cập nhật]

### 8.2 Ví dụ Kịch bản Sử dụng (Use Case Examples)

#### Kịch bản 1: Đặt lệnh Bán Trailing Stop để bảo vệ lợi nhuận

**Context**:
- Khách hàng đang nắm giữ 1,000 cổ phiếu KBC
- Giá mua ban đầu: 32,000 VNĐ
- Giá hiện tại: 35,000 VNĐ (đã lãi 3,000 VNĐ/CP)
- Khách hàng muốn bảo vệ lợi nhuận, cho phép giá tăng thêm nhưng bán nếu giá giảm 600 VNĐ từ đỉnh

**Hành động**:
1. KH truy cập màn hình đặt lệnh Trailing Stop
2. Chọn:
   - Chiều: Bán
   - Mã CK: KBC
   - Khối lượng: 1000
   - Giá kích hoạt: Giá hiện tại (35,000)
   - Biên độ trượt: 600 VNĐ
   - Bước giá kích hoạt: 500 VNĐ
   - Thời gian hiệu lực: Trong ngày
   - Loại lệnh GD: LO
3. Hệ thống hiển thị warning: "Giá kích hoạt ≥ Giá TT, lệnh có thể kích hoạt ngay"
4. KH xác nhận và đặt lệnh thành công

**Kết quả**:
- Lệnh được lưu với trạng thái "Chờ kích hoạt"
- Giá kích hoạt ban đầu: 35,000 VNĐ

**Diễn biến giá**:
- 10:30 - Giá tăng lên 35,500 → Giá kích hoạt tăng lên 35,500 (bám theo giá)
- 11:00 - Giá tăng lên 36,000 → Giá kích hoạt tăng lên 36,000
- 11:30 - Giá giảm xuống 35,800 → Giá kích hoạt giữ nguyên 36,000 (không giảm)
- 13:00 - Giá giảm xuống 35,400 → Giá kích hoạt giữ nguyên 36,000
- 13:30 - Giá giảm xuống 35,300 → **Chạm điều kiện kích hoạt!** (35,300 < 36,000 - 600)
- Hệ thống gửi lệnh bán LO giá 35,500 (= 36,000 - 500) lên sàn
- KH nhận thông báo: "Lệnh Trailing Stop đã kích hoạt, lệnh bán LO 1,000 CP KBC giá 35,500 đã được gửi lên sàn"

**Lợi nhuận**:
- Giá bán: 35,500 (giả sử khớp)
- Lãi: 3,500 VNĐ/CP (so với giá mua 32,000)
- Tổng lãi: 3,500 x 1,000 = 3,500,000 VNĐ

#### Kịch bản 2: Hủy lệnh Trailing Stop

**Context**:
- KH đã đặt lệnh Trailing Stop vào 10:00
- Lệnh đang ở trạng thái "Chờ kích hoạt"
- KH thay đổi chiến lược, muốn hủy lệnh

**Hành động**:
1. KH truy cập Sổ lệnh điều kiện
2. Tìm thấy lệnh với trạng thái "Chờ kích hoạt"
3. Nhấn nút "Hủy lệnh"
4. Hệ thống hiển thị dialog xác nhận: "Bạn có chắc chắn muốn hủy lệnh TS-20251117-000001 - KBC - Bán 1000?"
5. KH xác nhận "Đồng ý"
6. Hệ thống hủy lệnh thành công

**Kết quả**:
- Lệnh chuyển sang trạng thái "Đã hủy"
- Hệ thống dừng theo dõi giá thị trường cho lệnh này
- KH nhận thông báo: "Hủy lệnh thành công"

---

**END OF DOCUMENT**
