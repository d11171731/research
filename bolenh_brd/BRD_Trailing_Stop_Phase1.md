# Bộ Lệnh Điều Kiện - Trailing Stop (Phase 1) - Tài liệu Yêu cầu Nghiệp vụ (BRD)

---

## QUẢN LÝ TÀI LIỆU

| Thông tin | Chi tiết |
|-----------|----------|
| **Tên tài liệu** | Business Requirements Document - Bộ Lệnh Điều Kiện Trailing Stop (Phase 1) |
| **Phiên bản** | 1.0 |
| **Ngày tạo** | 17/11/2025 |
| **Người tạo** | Business Analyst Team |
| **Người phê duyệt** | Product Owner |
| **Trạng thái** | Draft |

### Lịch sử phiên bản

| Phiên bản | Ngày | Người thay đổi | Mô tả thay đổi |
|-----------|------|----------------|----------------|
| 1.0 | 17/11/2025 | BA Team | Phiên bản khởi tạo - Phase 1 Trailing Stop |

### Danh sách phân phối

| Vai trò | Họ tên | Email |
|---------|--------|-------|
| Product Owner | TBD | TBD |
| Business Analyst | TBD | TBD |
| Tech Lead | TBD | TBD |
| QA Lead | TBD | TBD |
| Trading System Team Lead | TBD | TBD |

---

## TÓM TẮT ĐIỀU HÀNH

Tài liệu này mô tả yêu cầu nghiệp vụ cho tính năng **Lệnh Trailing Stop** - một công cụ giao dịch tự động giúp nhà đầu tư bảo vệ lợi nhuận và hạn chế rủi ro. Trailing Stop tự động điều chỉnh giá kích hoạt theo biến động thị trường, cho phép nhà đầu tư "khóa" lợi nhuận khi giá di chuyển theo hướng có lợi, đồng thời giảm thiểu tổn thất khi giá đảo chiều.

Phase 1 tập trung vào các chức năng cốt lõi: Đặt lệnh Trailing Stop, xem sổ lệnh điều kiện, và hủy lệnh. Tính năng này nhằm nâng cao trải nghiệm giao dịch, giúp nhà đầu tư quản lý rủi ro hiệu quả hơn mà không cần theo dõi thị trường liên tục, đồng thời gia tăng khả năng cạnh tranh của nền tảng giao dịch.

---

## 1. GIỚI THIỆU

### 1.1 Mục đích tài liệu

Tài liệu này mô tả chi tiết các yêu cầu nghiệp vụ cho tính năng **Lệnh Trailing Stop (Phase 1)** trong hệ thống giao dịch chứng khoán. Tài liệu được sử dụng bởi các nhóm phát triển, kiểm thử, và vận hành để hiểu rõ yêu cầu và triển khai chính xác tính năng.

### 1.2 Phạm vi

**Trong phạm vi (In Scope):**
- Đặt lệnh Trailing Stop với đầy đủ tham số (chiều, khối lượng, mã CK, giá kích hoạt, biên độ trượt, bước giá kích hoạt, thời gian hiệu lực)
- Validation đầy đủ các tham số đầu vào (Error và Warning)
- Xem danh sách lệnh Trailing Stop với các trạng thái: Chờ kích hoạt, Đã kích hoạt, Đã hủy, Hết hạn, Bị từ chối
- Hủy lệnh đang ở trạng thái "Chờ kích hoạt"
- Cơ chế tự động điều chỉnh giá kích hoạt theo biến động thị trường
- Tự động kích hoạt lệnh khi thỏa điều kiện và đẩy lệnh lên sàn
- Hỗ trợ 3 sàn: HOSE, HNX, UPCOM
- Hỗ trợ loại lệnh giao dịch: LO và MTL
- Thời gian hiệu lực: Trong ngày và Đến hạn (tối đa 30 ngày)

**Ngoài phạm vi (Out of Scope):**
- Sửa lệnh Trailing Stop (không hỗ trợ do đặc thù của loại lệnh này)
- Giao dịch lô lẻ (chỉ hỗ trợ lô chẵn - bội số 100)
- Kiểm tra sức mua/sức bán tại thời điểm đặt lệnh (chỉ kiểm tra khi kích hoạt)
- Kiểm tra giá trần/sàn tại thời điểm đặt lệnh (chỉ kiểm tra khi kích hoạt)
- Quản lý danh mục đầu tư
- Báo cáo phân tích hiệu suất lệnh
- Tích hợp với hệ thống khuyến nghị (recommendation system)
- Copy/Duplicate lệnh
- Template lệnh (lưu mẫu lệnh thường dùng)

### 1.3 Định nghĩa và Thuật ngữ

| Thuật ngữ | Định nghĩa | Tiếng Anh |
|-----------|-----------|-----------|
| Trailing Stop | Lệnh điều kiện tự động điều chỉnh giá kích hoạt theo biến động thị trường để bảo vệ lợi nhuận | Trailing Stop Order |
| Giá kích hoạt | Mức giá mà khi thị trường đạt đến, lệnh điều kiện sẽ được kích hoạt và chuyển thành lệnh thường | Trigger Price / Activation Price |
| Biên độ trượt (D) | Khoảng giá chênh lệch để xác định điểm đảo chiều (tính bằng VNĐ) | Trailing Amount / Trailing Distance |
| Bước giá kích hoạt (delta) | Khoảng giá cộng/trừ so với giá kích hoạt để tăng khả năng khớp (tính bằng VNĐ) | Activation Price Offset |
| Lệnh con | Lệnh giao dịch thường (LO hoặc MTL) được tạo ra khi lệnh điều kiện được kích hoạt | Child Order |
| Lệnh điều kiện | Lệnh chờ kích hoạt khi thỏa mãn điều kiện đặt ra | Conditional Order |
| LO | Lệnh giới hạn (Limit Order) | Limit Order (LO) |
| MTL | Lệnh thị trường chờ khớp (Market to Limit) | Market to Limit (MTL) |
| Giá tham chiếu | Giá đóng cửa của phiên giao dịch trước đó | Reference Price |
| Bước giá | Đơn vị giá tối thiểu cho phép giao dịch trên sàn | Price Tick / Tick Size |
| Lô chẵn | Khối lượng giao dịch là bội số của 100 | Round Lot |
| Lô lẻ | Khối lượng giao dịch không phải bội số của 100 | Odd Lot |
| Giá thị trường | Giá giao dịch hiện tại trên sàn (có thể là giá khớp lệnh, giá mua/bán tốt nhất) | Market Price |

### 1.4 Tài liệu tham khảo

- Quy định giao dịch chứng khoán của Sở Giao dịch Chứng khoán (HOSE, HNX, UPCOM)
- Tài liệu thiết kế hệ thống lệnh điều kiện (nếu có)
- Tài liệu API tích hợp với sàn giao dịch
- Quy định về bước giá và khối lượng giao dịch tối thiểu

---

## 2. MỤC TIÊU KINH DOANH

### 2.1 Vấn đề cần giải quyết

**Vấn đề của nhà đầu tư:**
- Phải theo dõi thị trường liên tục để bảo vệ lợi nhuận khi giá đảo chiều
- Khó xác định điểm chốt lời tối ưu khi giá biến động liên tục
- Tâm lý tham lam hoặc sợ hãi dẫn đến quyết định giao dịch không tối ưu
- Mất cơ hội chốt lời khi không thể theo dõi thị trường 24/7

**Vấn đề của doanh nghiệp:**
- Thiếu công cụ giao dịch tự động nâng cao, làm giảm khả năng cạnh tranh
- Khách hàng chuyển sang các nền tảng có công cụ quản lý rủi ro tốt hơn
- Chưa tận dụng được công nghệ để nâng cao trải nghiệm giao dịch

### 2.2 Mục tiêu nghiệp vụ

1. **Tăng retention và engagement của khách hàng**
   - Tăng 20% số lượng khách hàng active sử dụng công cụ giao dịch nâng cao trong 6 tháng
   - Tăng 15% thời lượng sử dụng app/platform mỗi ngày

2. **Nâng cao khả năng cạnh tranh**
   - Cung cấp công cụ quản lý rủi ro tự động tương đương hoặc tốt hơn đối thủ
   - Thu hút 10% khách hàng mới nhờ tính năng Trailing Stop

3. **Tối ưu trải nghiệm giao dịch**
   - Giảm 30% thời gian nhà đầu tư phải theo dõi thị trường để quản lý vị thế
   - Tăng tỷ lệ thành công của các lệnh bảo vệ lợi nhuận

4. **Gia tăng khối lượng giao dịch**
   - Tăng 10% số lượng lệnh giao dịch nhờ công cụ tự động
   - Tăng doanh thu từ phí giao dịch

---

## 3. CÁC BÊN LIÊN QUAN

### 3.1 Stakeholders nghiệp vụ

| Vai trò | Họ tên | Trách nhiệm |
|---------|--------|-------------|
| Product Owner | TBD | Phê duyệt yêu cầu, ưu tiên tính năng, quyết định scope |
| Business Analyst | TBD | Phân tích yêu cầu, viết BRD, làm việc với stakeholders |
| Trading Operations Manager | TBD | Xác nhận quy trình giao dịch, quy định sàn |
| Risk Management Lead | TBD | Đảm bảo tuân thủ quy định quản lý rủi ro |
| Customer Support Lead | TBD | Cung cấp feedback từ khách hàng, xử lý khiếu nại |

### 3.2 Stakeholders kỹ thuật

| Vai trò | Họ tên | Trách nhiệm |
|---------|--------|-------------|
| Tech Lead | TBD | Thiết kế kiến trúc, review technical solution |
| Backend Developer Lead | TBD | Phát triển logic xử lý lệnh, tích hợp sàn |
| Frontend Developer Lead | TBD | Phát triển UI/UX, validation client-side |
| QA Lead | TBD | Lập kế hoạch test, đảm bảo chất lượng |
| DevOps Lead | TBD | Triển khai, monitoring, performance |
| Data Engineer | TBD | Thiết kế database schema, data migration |

### 3.3 Người dùng cuối

- **Nhà đầu tư cá nhân chủ động**: Có kiến thức về giao dịch chứng khoán, cần công cụ quản lý rủi ro tự động để tối ưu lợi nhuận mà không phải theo dõi thị trường liên tục
- **Nhà đầu tư bán chuyên nghiệp**: Quản lý nhiều vị thế giao dịch, cần công cụ nâng cao để tự động hóa chiến lược giao dịch
- **Nhà đầu tư ngắn hạn (Day Trader)**: Giao dịch nội ngày, cần bảo vệ lợi nhuận nhanh chóng khi giá biến động

---

## 4. YÊU CẦU CHỨC NĂNG

### 4.1 Tổng quan tính năng

**Lệnh Trailing Stop** là một loại lệnh điều kiện tự động giúp nhà đầu tư bảo vệ lợi nhuận khi giá di chuyển theo hướng có lợi, đồng thời hạn chế tổn thất khi giá đảo chiều.

**Cơ chế hoạt động:**

**Lệnh MUA (Trailing Stop Buy):**
- Giá kích hoạt ban đầu: Nhà đầu tư đặt mức giá mong muốn
- Khi giá thị trường GIẢM: Hệ thống tự động điều chỉnh giá kích hoạt GIẢM theo (theo khoảng cách = Biên độ trượt)
- Khi giá thị trường TĂNG trở lại: Giá kích hoạt GIỮ NGUYÊN (không tăng theo)
- Kích hoạt: Khi giá thị trường TĂNG vượt qua giá kích hoạt → Tạo lệnh mua

**Lệnh BÁN (Trailing Stop Sell):**
- Giá kích hoạt ban đầu: Nhà đầu tư đặt mức giá mong muốn
- Khi giá thị trường TĂNG: Hệ thống tự động điều chỉnh giá kích hoạt TĂNG theo (theo khoảng cách = Biên độ trượt)
- Khi giá thị trường GIẢM trở lại: Giá kích hoạt GIỮ NGUYÊN (không giảm theo)
- Kích hoạt: Khi giá thị trường GIẢM xuống dưới giá kích hoạt → Tạo lệnh bán

**Lệnh con được tạo khi kích hoạt:**
- Giá lệnh con = Giá kích hoạt + Bước giá kích hoạt (delta)
- Loại lệnh con: LO hoặc MTL (tùy lựa chọn của khách hàng)

### 4.2 User Stories

#### Epic: Quản lý lệnh Trailing Stop

| ID | User Story | Độ ưu tiên | Acceptance Criteria |
|----|------------|------------|---------------------|
| US-001 | Là nhà đầu tư, tôi muốn đặt lệnh Trailing Stop Sell để tự động bảo vệ lợi nhuận khi giá cổ phiếu đảo chiều giảm | Must Have | • Điền đầy đủ tham số lệnh (chiều, khối lượng, mã CK, giá kích hoạt, biên độ trượt, bước giá kích hoạt)<br>• Chọn thời gian hiệu lực (trong ngày hoặc đến hạn)<br>• Chọn loại lệnh giao dịch (LO hoặc MTL)<br>• Nhận xác nhận đặt lệnh thành công<br>• Lệnh xuất hiện trong sổ lệnh với trạng thái "Chờ kích hoạt" |
| US-002 | Là nhà đầu tư, tôi muốn đặt lệnh Trailing Stop Buy để tự động mua vào khi giá cổ phiếu phục hồi sau khi giảm | Must Have | • Điền đầy đủ tham số lệnh<br>• Hệ thống validate đúng logic cho lệnh MUA<br>• Nhận warning nếu giá kích hoạt <= giá thị trường<br>• Lệnh được tạo thành công |
| US-003 | Là nhà đầu tư, tôi muốn hệ thống validate đầu vào để tránh đặt lệnh sai | Must Have | • Validate khối lượng là bội số 100, > 0<br>• Validate biên độ trượt > 0<br>• Validate bước giá kích hoạt > 0 và là bội số bước giá<br>• Hiển thị lỗi rõ ràng khi vi phạm<br>• Không cho submit khi có lỗi |
| US-004 | Là nhà đầu tư, tôi muốn nhận cảnh báo khi đặt lệnh có thể kích hoạt ngay lập tức | Should Have | • Hiển thị warning khi giá kích hoạt lệnh BÁN >= giá thị trường<br>• Hiển thị warning khi giá kích hoạt lệnh MUA <= giá thị trường<br>• Vẫn cho phép đặt lệnh sau khi xác nhận warning |
| US-005 | Là nhà đầu tư, tôi muốn xem danh sách tất cả lệnh Trailing Stop của mình để theo dõi trạng thái | Must Have | • Hiển thị đầy đủ thông tin lệnh: Mã CK, Loại lệnh, Chiều, Khối lượng, Giá kích hoạt hiện tại, Biên độ trượt, Trạng thái, Thời gian tạo, Thời gian hết hạn<br>• Phân biệt rõ các trạng thái: Chờ kích hoạt, Đã kích hoạt, Đã hủy, Hết hạn, Bị từ chối<br>• Hiển thị giá kích hoạt cập nhật real-time cho lệnh đang "Chờ kích hoạt" |
| US-006 | Là nhà đầu tư, tôi muốn hủy lệnh Trailing Stop đang chờ kích hoạt khi không còn nhu cầu | Must Have | • Chỉ hủy được lệnh ở trạng thái "Chờ kích hoạt"<br>• Nhận xác nhận trước khi hủy<br>• Lệnh chuyển sang trạng thái "Đã hủy" sau khi hủy thành công<br>• Không thể hủy lệnh đã kích hoạt/đã hủy/hết hạn/bị từ chối |
| US-007 | Là nhà đầu tư, tôi muốn nhận thông báo khi lệnh Trailing Stop được kích hoạt và đẩy lên sàn | Should Have | • Nhận thông báo real-time khi lệnh kích hoạt<br>• Thông báo bao gồm: Mã CK, Chiều, Khối lượng, Giá lệnh con, Trạng thái<br>• Thông báo khi lệnh bị từ chối do không đủ điều kiện |
| US-008 | Là nhà đầu tư, tôi muốn lệnh Trailing Stop tự động hết hạn khi hết thời gian hiệu lực | Must Have | • Lệnh "Trong ngày" tự động hết hạn lúc 14:45<br>• Lệnh "Đến hạn" tự động hết hạn vào ngày được chọn<br>• Lệnh chuyển sang trạng thái "Hết hạn"<br>• Hiển thị trong lịch sử lệnh |

### 4.3 Yêu cầu chi tiết

#### 4.3.1 Chức năng 1: Đặt lệnh Trailing Stop

**Mô tả**: Cho phép khách hàng đặt lệnh Trailing Stop bằng cách điền/lựa chọn các tham số và validate đầy đủ trước khi submit.

**Độ ưu tiên**: Must Have

**Input Fields:**

| Trường | Mô tả | Kiểu dữ liệu | Bắt buộc | Giá trị mặc định |
|--------|-------|--------------|----------|------------------|
| Loại lệnh | Trailing Stop | Readonly | Có | "Trailing Stop" |
| Chiều | Mua hoặc Bán | Dropdown | Có | - |
| Mã CK | Mã chứng khoán | Autocomplete/Textbox | Có | - |
| Khối lượng | Số lượng CP muốn mua/bán | Integer | Có | - |
| Giá kích hoạt | Giá để kích hoạt lệnh | Selection + Number | Có | "Giá hiện tại" |
| - Giá hiện tại | Lấy giá thị trường | Radio option | - | Selected |
| - Giá tùy chỉnh | Nhập giá mong muốn | Radio option + Number input | - | - |
| Biên độ trượt (D) | Khoảng cách điều chỉnh giá kích hoạt (VNĐ) | Number | Có | - |
| Loại lệnh giao dịch | LO hoặc MTL | Radio/Dropdown | Có | LO |
| Bước giá kích hoạt (delta) | Khoảng giá cộng/trừ để tăng khả năng khớp (VNĐ) | Number | Có (nếu chọn LO) | - |
| Thời gian hiệu lực | Trong ngày hoặc Đến hạn | Radio/Dropdown | Có | "Trong ngày" |
| - Ngày hết hạn | Chọn ngày (nếu chọn "Đến hạn") | Date picker | Có (nếu chọn "Đến hạn") | - |

**Validation Rules:**

| ID | Trường | Quy tắc validate | Loại | Thông báo |
|----|--------|------------------|------|-----------|
| VAL-001 | Khối lượng | Phải là số nguyên dương | Error | "Khối lượng phải là số nguyên dương" |
| VAL-002 | Khối lượng | Phải là bội số của 100 | Error | "Khối lượng phải là bội số của 100" |
| VAL-003 | Khối lượng | Cho phép tăng/giảm bằng nút +/- (step = 100) | - | - |
| VAL-004 | Mã CK | Chỉ chấp nhận mã thuộc HOSE, HNX, UPCOM | Error | "Mã chứng khoán không hợp lệ hoặc không được hỗ trợ" |
| VAL-005 | Biên độ trượt | Phải > 0 | Error | "Biên độ trượt phải lớn hơn 0" |
| VAL-006 | Biên độ trượt | Phải là bội số của bước giá | Error | "Biên độ trượt không đúng bước giá. Gợi ý: [giá gần nhất]" |
| VAL-007 | Biên độ trượt | Nếu > 10% giá tham chiếu | Warning | "Biên độ trượt lớn, lệnh có thể khó kích hoạt" |
| VAL-008 | Bước giá kích hoạt | Phải > 0 | Error | "Bước giá kích hoạt phải lớn hơn 0" |
| VAL-009 | Bước giá kích hoạt | Phải là bội số của bước giá | Error | "Bước giá kích hoạt không đúng bước giá. Gợi ý: [giá gần nhất]" |
| VAL-010 | Bước giá kích hoạt | Gợi ý: 100 - 1,000 VNĐ | Info | Hiển thị tooltip giải thích |
| VAL-011 | Bước giá kích hoạt | Cho phép tăng/giảm bằng nút +/- | - | - |
| VAL-012 | Giá kích hoạt (Lệnh MUA) | Nếu <= Giá thị trường | Warning | "Giá kích hoạt ≤ Giá TT, lệnh sẽ được kích hoạt ngay lập tức. Bạn có chắc muốn tiếp tục?" |
| VAL-013 | Giá kích hoạt (Lệnh BÁN) | Nếu >= Giá thị trường | Warning | "Giá kích hoạt ≥ Giá TT, lệnh sẽ được kích hoạt ngay lập tức. Bạn có chắc muốn tiếp tục?" |
| VAL-014 | Thời gian hiệu lực | Nếu chọn "Đến hạn", ngày hết hạn tối đa 30 ngày từ hôm nay | Error | "Ngày hết hạn không được vượt quá 30 ngày" |
| VAL-015 | Thời gian hiệu lực | Ngày hết hạn phải >= ngày hiện tại | Error | "Ngày hết hạn không hợp lệ" |

**Business Rules:**

| ID | Quy tắc | Hành động khi vi phạm |
|----|---------|----------------------|
| BR-001 | Hệ thống KHÔNG kiểm tra sức mua/sức bán tại thời điểm đặt lệnh | Chỉ kiểm tra khi lệnh kích hoạt |
| BR-002 | Hệ thống KHÔNG kiểm tra giá trần/sàn tại thời điểm đặt lệnh | Chỉ kiểm tra khi lệnh kích hoạt |
| BR-003 | Nếu chọn loại lệnh giao dịch = MTL, disable ô "Bước giá kích hoạt" | Không cần nhập Bước giá kích hoạt |
| BR-004 | Nếu chọn loại lệnh giao dịch = LO, enable và bắt buộc nhập ô "Bước giá kích hoạt" | Phải nhập Bước giá kích hoạt |
| BR-005 | Nếu chọn "Giá hiện tại", hệ thống tự động lấy giá thị trường làm giá kích hoạt ban đầu | Không cho nhập giá thủ công |
| BR-006 | Nếu chọn "Giá tùy chỉnh", khách hàng phải nhập giá mong muốn | Bắt buộc nhập giá |
| BR-007 | Lệnh Trailing Stop KHÔNG hỗ trợ giao dịch lô lẻ | Chỉ chấp nhận bội số 100 |

**Luồng nghiệp vụ:**

1. Khách hàng chọn "Đặt lệnh Trailing Stop"
2. Hệ thống hiển thị form nhập liệu
3. Khách hàng điền/chọn các tham số:
   - Chọn Chiều (Mua/Bán)
   - Nhập Mã CK (có autocomplete)
   - Nhập Khối lượng (có nút +/-)
   - Chọn Giá kích hoạt (Giá hiện tại hoặc Giá tùy chỉnh)
   - Nhập Biên độ trượt
   - Chọn Loại lệnh giao dịch (LO/MTL)
   - Nhập Bước giá kích hoạt (nếu chọn LO)
   - Chọn Thời gian hiệu lực (Trong ngày/Đến hạn)
   - Chọn Ngày hết hạn (nếu chọn Đến hạn)
4. Hệ thống validate real-time từng trường khi nhập
5. Hệ thống hiển thị Error (màu đỏ, chặn submit) hoặc Warning (màu vàng, cho phép submit sau xác nhận)
6. Khách hàng click "Đặt lệnh"
7. Nếu có Warning, hiển thị popup xác nhận
8. Hệ thống tạo lệnh với trạng thái "Chờ kích hoạt"
9. Hiển thị thông báo thành công với Order ID
10. Chuyển khách hàng đến màn hình "Sổ lệnh điều kiện"

#### 4.3.2 Chức năng 2: Xem Sổ lệnh Trailing Stop

**Mô tả**: Hiển thị danh sách tất cả lệnh Trailing Stop của khách hàng với đầy đủ thông tin và trạng thái.

**Độ ưu tiên**: Must Have

**Thông tin hiển thị:**

| Cột | Mô tả | Kiểu dữ liệu | Có sort | Có filter |
|-----|-------|--------------|---------|-----------|
| Thời gian | Thời gian đặt lệnh | DateTime (DD/MM/YYYY HH:mm:ss) | Có | Có (Date range) |
| Mã CK | Mã chứng khoán | String | Có | Có (Search) |
| Chiều | Mua/Bán | String | Có | Có (Dropdown) |
| Loại lệnh | Trailing Stop | String | Không | Có (Dropdown) |
| Khối lượng | Khối lượng đặt | Integer | Có | Không |
| Giá kích hoạt hiện tại | Giá kích hoạt được cập nhật real-time | Decimal | Có | Không |
| Giá kích hoạt ban đầu | Giá kích hoạt lúc đặt lệnh | Decimal | Không | Không |
| Biên độ trượt | Khoảng cách điều chỉnh (VNĐ) | Decimal | Không | Không |
| Bước giá kích hoạt | Delta (VNĐ) | Decimal | Không | Không |
| Loại lệnh giao dịch | LO/MTL | String | Không | Có (Dropdown) |
| Trạng thái | Chờ kích hoạt/Đã kích hoạt/Đã hủy/Hết hạn/Bị từ chối | String | Có | Có (Dropdown) |
| Ngày hết hạn | Ngày hết hiệu lực | Date (DD/MM/YYYY) | Có | Không |
| Kênh đặt | Web/Mobile/DBoard | String | Không | Có (Dropdown) |
| Actions | Hủy lệnh (nếu cho phép) | Button | - | - |

**Trạng thái lệnh:**

| Trạng thái | Mô tả | Icon/Color | Cho phép hủy | Nơi hiển thị |
|-----------|-------|------------|--------------|--------------|
| Chờ kích hoạt | Lệnh đang chờ điều kiện kích hoạt, giá kích hoạt được cập nhật real-time | 🟡 Vàng | Có | Sổ lệnh điều kiện |
| Đã kích hoạt | Lệnh đã thỏa điều kiện, lệnh con đã được gửi lên sàn | 🟢 Xanh lá | Không | Sổ lệnh điều kiện |
| Đã hủy | Lệnh được hủy bởi khách hàng | ⚫ Xám | Không | Sổ lệnh điều kiện |
| Hết hạn | Lệnh hết thời gian hiệu lực | 🔴 Đỏ | Không | Lịch sử lệnh điều kiện |
| Bị từ chối | Lệnh kích hoạt nhưng không đủ điều kiện để đẩy lên sàn | 🔴 Đỏ | Không | Sổ lệnh điều kiện |

**Business Rules:**

| ID | Quy tắc |
|----|---------|
| BR-008 | Giá kích hoạt hiện tại được cập nhật real-time khi lệnh ở trạng thái "Chờ kích hoạt" |
| BR-009 | Lệnh "Hết hạn" chỉ hiển thị trong "Lịch sử lệnh điều kiện", không hiển thị trong "Sổ lệnh điều kiện" |
| BR-010 | Lệnh "Đã kích hoạt" hiển thị thông tin lệnh con (Order ID, Giá, Trạng thái lệnh con) |
| BR-011 | Mặc định sắp xếp theo thời gian đặt lệnh (mới nhất lên đầu) |
| BR-012 | Pagination: 20 lệnh/trang |

**Luồng nghiệp vụ:**

1. Khách hàng truy cập "Sổ lệnh điều kiện"
2. Hệ thống hiển thị danh sách lệnh Trailing Stop
3. Cập nhật real-time "Giá kích hoạt hiện tại" cho lệnh "Chờ kích hoạt"
4. Khách hàng có thể:
   - Xem chi tiết lệnh (click vào dòng)
   - Hủy lệnh (nếu trạng thái = "Chờ kích hoạt")
   - Filter/Sort theo các tiêu chí
5. Khi lệnh thay đổi trạng thái, cập nhật ngay lập tức

#### 4.3.3 Chức năng 3: Hủy lệnh Trailing Stop

**Mô tả**: Cho phép khách hàng hủy lệnh Trailing Stop đang ở trạng thái "Chờ kích hoạt".

**Độ ưu tiên**: Must Have

**Business Rules:**

| ID | Quy tắc | Hành động khi vi phạm |
|----|---------|----------------------|
| BR-013 | Chỉ được hủy lệnh có trạng thái "Chờ kích hoạt" | Hiển thị lỗi: "Không thể hủy lệnh này. Chỉ hủy được lệnh đang chờ kích hoạt." |
| BR-014 | Phải xác nhận trước khi hủy | Hiển thị popup xác nhận |
| BR-015 | Sau khi hủy, lệnh chuyển sang trạng thái "Đã hủy" và không thể khôi phục | - |

**Luồng nghiệp vụ:**

1. Khách hàng click nút "Hủy" trên lệnh có trạng thái "Chờ kích hoạt"
2. Hệ thống hiển thị popup xác nhận:
   - Tiêu đề: "Xác nhận hủy lệnh"
   - Nội dung: "Bạn có chắc muốn hủy lệnh Trailing Stop [Chiều] [Mã CK] - Khối lượng [KL]?"
   - Buttons: "Hủy lệnh" (màu đỏ), "Không" (màu xám)
3. Nếu khách hàng click "Hủy lệnh":
   - Hệ thống gửi request hủy lệnh
   - Cập nhật trạng thái lệnh = "Đã hủy"
   - Hiển thị thông báo: "Hủy lệnh thành công"
4. Nếu khách hàng click "Không":
   - Đóng popup, không thực hiện hành động

### 4.4 Quy tắc nghiệp vụ tổng quát

| ID | Quy tắc | Hành động khi vi phạm |
|----|---------|----------------------|
| BR-016 | Lệnh Trailing Stop KHÔNG hỗ trợ sửa lệnh vì cơ chế tự động điều chỉnh giá kích hoạt theo thị trường | Không hiển thị nút "Sửa" |
| BR-017 | Lệnh "Trong ngày" tự động hết hạn lúc 14:45 | Chuyển trạng thái = "Hết hạn" |
| BR-018 | Lệnh "Đến hạn" tự động hết hạn vào cuối ngày được chọn (23:59:59) | Chuyển trạng thái = "Hết hạn" |
| BR-019 | Giá kích hoạt chỉ điều chỉnh theo một chiều (tăng với lệnh BÁN, giảm với lệnh MUA), không đảo chiều | Theo logic Trailing Stop |
| BR-020 | Khi lệnh kích hoạt, hệ thống tạo lệnh con với Giá = Giá kích hoạt + Bước giá kích hoạt (cho lệnh BÁN) hoặc Giá kích hoạt - Bước giá kích hoạt (cho lệnh MUA) | - |
| BR-021 | Nếu lệnh con bị từ chối (không đủ sức mua/bán, giá trần/sàn), lệnh Trailing Stop chuyển sang trạng thái "Bị từ chối" | Gửi thông báo cho khách hàng |
| BR-022 | Hệ thống monitor giá thị trường real-time để điều chỉnh giá kích hoạt | Tần suất cập nhật tối thiểu: mỗi giây |
| BR-023 | Một khách hàng có thể đặt tối đa [TBD] lệnh Trailing Stop cùng lúc | Hiển thị lỗi khi vượt giới hạn |

### 4.5 Workflow & Process Flow

```
LUỒNG XỬ LÝ LỆNH TRAILING STOP

[Khách hàng đặt lệnh]
         ↓
[Validate đầu vào] → [Có lỗi] → [Hiển thị lỗi, không cho submit]
         ↓ [Pass]
[Tạo lệnh điều kiện với trạng thái "Chờ kích hoạt"]
         ↓
[Lưu vào Database]
         ↓
[Monitor giá thị trường real-time]
         ↓
[Điều chỉnh giá kích hoạt theo logic Trailing Stop]
         ↓
    ┌────┴────┐
    ↓         ↓
[Giá chưa    [Giá thị trường thỏa điều kiện kích hoạt]
 kích hoạt]       ↓
    ↓         [Validate sức mua/bán, giá trần/sàn]
[Continue         ↓
 monitor]    ┌────┴────┐
    ↑        ↓         ↓
    │   [Pass]    [Fail]
    │        ↓         ↓
    │   [Tạo lệnh con]  [Trạng thái = "Bị từ chối"]
    │        ↓         ↓
    │   [Gửi lệnh con   [Thông báo khách hàng]
    │    lên sàn]
    │        ↓
    │   [Trạng thái = "Đã kích hoạt"]
    │        ↓
    │   [Thông báo khách hàng]
    │
    └──── [Hết hạn] → [Trạng thái = "Hết hạn"]
         [Khách hàng hủy] → [Trạng thái = "Đã hủy"]
```

---

## 5. YÊU CẦU DỮ LIỆU

### 5.1 Input Specification

#### Input từ khách hàng khi đặt lệnh

| Trường Input | Nguồn | Kiểu dữ liệu | Bắt buộc | Validation | Giá trị mặc định |
|--------------|-------|--------------|----------|------------|------------------|
| order_type | User | String (Enum) | Có | "TRAILING_STOP" | "TRAILING_STOP" |
| side | User | String (Enum) | Có | "BUY" hoặc "SELL" | - |
| symbol | User | String | Có | Regex: ^[A-Z]{3}$, thuộc danh sách mã CK hợp lệ | - |
| volume | User | Integer | Có | > 0, % 100 == 0 | - |
| trigger_price_method | User | String (Enum) | Có | "MARKET" hoặc "CUSTOM" | "MARKET" |
| trigger_price | User/System | Decimal | Có (nếu CUSTOM) | > 0, là bội số bước giá | Giá thị trường (nếu MARKET) |
| trailing_amount | User | Decimal | Có | > 0, là bội số bước giá, <= 10% giá tham chiếu (warning nếu vượt) | - |
| child_order_type | User | String (Enum) | Có | "LO" hoặc "MTL" | "LO" |
| activation_price_offset | User | Decimal | Có (nếu LO) | > 0, là bội số bước giá, gợi ý 100-1000 VNĐ | - |
| validity_type | User | String (Enum) | Có | "DAY" hoặc "GTD" (Good Till Date) | "DAY" |
| expiry_date | User | Date | Có (nếu GTD) | >= Ngày hiện tại, <= Ngày hiện tại + 30 ngày | - |
| channel | System | String | Có | "WEB", "MOBILE", "DBOARD" | Tự động xác định |
| customer_id | System | String | Có | ID khách hàng từ session | Tự động lấy |
| account_number | System | String | Có | Số tài khoản giao dịch | Tự động lấy |

#### Input từ hệ thống khi monitor lệnh

| Trường Input | Nguồn | Kiểu dữ liệu | Bắt buộc | Validation | Frequency |
|--------------|-------|--------------|----------|------------|-----------|
| market_price | Market Data Feed | Decimal | Có | > 0 | Real-time (mỗi giây) |
| reference_price | Market Data | Decimal | Có | Giá đóng cửa phiên trước | Mỗi ngày |
| tick_size | Market Data | Decimal | Có | Bước giá theo quy định sàn | Mỗi ngày |
| ceiling_price | Market Data | Decimal | Có | Giá trần | Mỗi ngày |
| floor_price | Market Data | Decimal | Có | Giá sàn | Mỗi ngày |
| trading_status | Market Data | String | Có | "TRADING", "HALTED", "CLOSED" | Real-time |

### 5.2 Output Specification

#### Output khi đặt lệnh thành công

| Trường Output | Kiểu dữ liệu | Mô tả | Ví dụ |
|---------------|--------------|-------|-------|
| order_id | String (UUID) | ID duy nhất của lệnh Trailing Stop | "TS-20251117-000001" |
| status | String | Trạng thái lệnh | "PENDING_ACTIVATION" |
| created_at | DateTime | Thời gian tạo lệnh | "2025-11-17T11:00:00Z" |
| message | String | Thông báo thành công | "Đặt lệnh Trailing Stop thành công" |

#### Output khi kích hoạt lệnh

| Trường Output | Kiểu dữ liệu | Mô tả | Ví dụ |
|---------------|--------------|-------|-------|
| parent_order_id | String | ID lệnh Trailing Stop | "TS-20251117-000001" |
| child_order_id | String | ID lệnh con (lệnh thường) | "LO-20251117-123456" |
| status | String | Trạng thái | "ACTIVATED" |
| activation_time | DateTime | Thời gian kích hoạt | "2025-11-17T13:25:30Z" |
| activation_price | Decimal | Giá kích hoạt tại thời điểm kích hoạt | 35800 |
| child_order_price | Decimal | Giá lệnh con | 36300 |
| message | String | Thông báo | "Lệnh Trailing Stop đã được kích hoạt và gửi lên sàn" |

#### Output khi lệnh bị từ chối

| Trường Output | Kiểu dữ liệu | Mô tả | Ví dụ |
|---------------|--------------|-------|-------|
| order_id | String | ID lệnh Trailing Stop | "TS-20251117-000001" |
| status | String | Trạng thái | "REJECTED" |
| rejection_reason | String | Lý do từ chối | "INSUFFICIENT_BUYING_POWER" |
| rejection_time | DateTime | Thời gian từ chối | "2025-11-17T13:25:31Z" |
| message | String | Thông báo chi tiết | "Lệnh không được kích hoạt do không đủ sức mua" |

### 5.3 Data Validation Rules

| Validation | Mô tả | Điều kiện | Loại | Thông báo |
|------------|-------|-----------|------|-----------|
| VAL-016 | Volume must be positive integer | volume > 0 AND volume is integer | Error | "Khối lượng phải là số nguyên dương" |
| VAL-017 | Volume must be round lot | volume % 100 == 0 | Error | "Khối lượng phải là bội số của 100" |
| VAL-018 | Symbol must be valid | symbol matches ^[A-Z]{3}$ AND exists in valid symbol list | Error | "Mã chứng khoán không hợp lệ hoặc không được hỗ trợ" |
| VAL-019 | Trailing amount must be positive | trailing_amount > 0 | Error | "Biên độ trượt phải lớn hơn 0" |
| VAL-020 | Trailing amount must be multiple of tick size | trailing_amount % tick_size == 0 | Error | "Biên độ trượt không đúng bước giá. Gợi ý: [nearest_valid_value]" |
| VAL-021 | Trailing amount should not be too large | trailing_amount <= reference_price * 0.1 | Warning | "Biên độ trượt lớn, lệnh có thể khó kích hoạt" |
| VAL-022 | Activation price offset must be positive | activation_price_offset > 0 | Error | "Bước giá kích hoạt phải lớn hơn 0" |
| VAL-023 | Activation price offset must be multiple of tick size | activation_price_offset % tick_size == 0 | Error | "Bước giá kích hoạt không đúng bước giá. Gợi ý: [nearest_valid_value]" |
| VAL-024 | Trigger price warning for BUY order | side == "BUY" AND trigger_price <= market_price | Warning | "Giá kích hoạt ≤ Giá TT, lệnh sẽ được kích hoạt ngay lập tức. Bạn có chắc muốn tiếp tục?" |
| VAL-025 | Trigger price warning for SELL order | side == "SELL" AND trigger_price >= market_price | Warning | "Giá kích hoạt ≥ Giá TT, lệnh sẽ được kích hoạt ngay lập tức. Bạn có chắc muốn tiếp tục?" |
| VAL-026 | Expiry date must be within 30 days | expiry_date <= current_date + 30 days | Error | "Ngày hết hạn không được vượt quá 30 ngày" |
| VAL-027 | Expiry date must be future date | expiry_date >= current_date | Error | "Ngày hết hạn không hợp lệ" |

---

## 6. CHI TIẾT IPO (INPUT - PROCESS - OUTPUT)

### 6.1 IPO Flow cho Đặt lệnh Trailing Stop

#### INPUT

**User Input:**

| Tham số | Mô tả | Kiểu | Bắt buộc | Ví dụ |
|---------|-------|------|----------|-------|
| side | Chiều mua/bán | String (ENUM: "BUY", "SELL") | Có | "SELL" |
| symbol | Mã chứng khoán | String | Có | "KBC" |
| volume | Khối lượng | Integer | Có | 100 |
| trigger_price_method | Phương thức chọn giá kích hoạt | String (ENUM: "MARKET", "CUSTOM") | Có | "CUSTOM" |
| trigger_price | Giá kích hoạt ban đầu | Decimal | Có (nếu CUSTOM) | 35300 |
| trailing_amount | Biên độ trượt (VNĐ) | Decimal | Có | 600 |
| child_order_type | Loại lệnh giao dịch | String (ENUM: "LO", "MTL") | Có | "LO" |
| activation_price_offset | Bước giá kích hoạt (VNĐ) | Decimal | Có (nếu LO) | 500 |
| validity_type | Thời gian hiệu lực | String (ENUM: "DAY", "GTD") | Có | "GTD" |
| expiry_date | Ngày hết hạn | Date | Có (nếu GTD) | "2025-11-19" |

**System Input:**

| Tham số | Mô tả | Kiểu | Nguồn | Ví dụ |
|---------|-------|------|-------|-------|
| customer_id | ID khách hàng | String | Session | "CUST123456" |
| account_number | Số tài khoản | String | Session | "0001234567" |
| channel | Kênh đặt lệnh | String | System | "DBOARD" |
| current_time | Thời gian hiện tại | DateTime | System | "2025-11-17T11:00:00Z" |
| market_price | Giá thị trường hiện tại | Decimal | Market Data | 35000 |
| reference_price | Giá tham chiếu | Decimal | Market Data | 35000 |
| tick_size | Bước giá | Decimal | Market Data Config | 100 |

#### PROCESS

**Bước 1: Validate Input từ khách hàng**

```
1.1. Validate Khối lượng
    IF volume <= 0 OR volume NOT integer THEN
        RETURN Error "Khối lượng phải là số nguyên dương"
    END IF

    IF volume % 100 != 0 THEN
        RETURN Error "Khối lượng phải là bội số của 100"
    END IF

1.2. Validate Mã CK
    IF symbol NOT matches regex ^[A-Z]{3}$ THEN
        RETURN Error "Mã chứng khoán không hợp lệ"
    END IF

    IF symbol NOT in valid_symbol_list(HOSE, HNX, UPCOM) THEN
        RETURN Error "Mã chứng khoán không được hỗ trợ"
    END IF

    # Lấy thông tin thị trường (tick_size, reference_price, market_price)
    market_info = GET_MARKET_INFO(symbol)

1.3. Validate Biên độ trượt
    IF trailing_amount <= 0 THEN
        RETURN Error "Biên độ trượt phải lớn hơn 0"
    END IF

    IF trailing_amount % tick_size != 0 THEN
        nearest_value = ROUND(trailing_amount / tick_size) * tick_size
        RETURN Error "Biên độ trượt không đúng bước giá. Gợi ý: " + nearest_value
    END IF

    IF trailing_amount > reference_price * 0.1 THEN
        ADD Warning "Biên độ trượt lớn, lệnh có thể khó kích hoạt"
    END IF

1.4. Validate Giá kích hoạt
    IF trigger_price_method == "MARKET" THEN
        trigger_price = market_price
    ELSE IF trigger_price_method == "CUSTOM" THEN
        IF trigger_price <= 0 THEN
            RETURN Error "Giá kích hoạt phải lớn hơn 0"
        END IF

        IF trigger_price % tick_size != 0 THEN
            nearest_value = ROUND(trigger_price / tick_size) * tick_size
            RETURN Error "Giá kích hoạt không đúng bước giá. Gợi ý: " + nearest_value
        END IF
    END IF

    # Warning nếu lệnh có thể kích hoạt ngay
    IF side == "BUY" AND trigger_price <= market_price THEN
        ADD Warning "Giá kích hoạt ≤ Giá TT, lệnh sẽ được kích hoạt ngay lập tức. Bạn có chắc muốn tiếp tục?"
    END IF

    IF side == "SELL" AND trigger_price >= market_price THEN
        ADD Warning "Giá kích hoạt ≥ Giá TT, lệnh sẽ được kích hoạt ngay lập tức. Bạn có chắc muốn tiếp tục?"
    END IF

1.5. Validate Bước giá kích hoạt
    IF child_order_type == "LO" THEN
        IF activation_price_offset <= 0 THEN
            RETURN Error "Bước giá kích hoạt phải lớn hơn 0"
        END IF

        IF activation_price_offset % tick_size != 0 THEN
            nearest_value = ROUND(activation_price_offset / tick_size) * tick_size
            RETURN Error "Bước giá kích hoạt không đúng bước giá. Gợi ý: " + nearest_value
        END IF
    ELSE IF child_order_type == "MTL" THEN
        activation_price_offset = NULL  # Không cần với MTL
    END IF

1.6. Validate Thời gian hiệu lực
    IF validity_type == "GTD" THEN
        IF expiry_date < current_date THEN
            RETURN Error "Ngày hết hạn không hợp lệ"
        END IF

        IF expiry_date > current_date + 30 days THEN
            RETURN Error "Ngày hết hạn không được vượt quá 30 ngày"
        END IF
    ELSE IF validity_type == "DAY" THEN
        expiry_date = current_date  # Hết hạn trong ngày
        expiry_time = "14:45:00"
    END IF
```

**Bước 2: Tạo bản ghi lệnh Trailing Stop**

```
2.1. Generate Order ID
    order_id = GENERATE_ORDER_ID("TS")  # Format: TS-YYYYMMDD-XXXXXX

2.2. Tạo bản ghi lệnh
    trailing_stop_order = {
        order_id: order_id,
        order_type: "TRAILING_STOP",
        customer_id: customer_id,
        account_number: account_number,
        symbol: symbol,
        side: side,
        volume: volume,
        initial_trigger_price: trigger_price,
        current_trigger_price: trigger_price,
        trailing_amount: trailing_amount,
        child_order_type: child_order_type,
        activation_price_offset: activation_price_offset,
        validity_type: validity_type,
        expiry_date: expiry_date,
        status: "PENDING_ACTIVATION",
        created_at: current_time,
        updated_at: current_time,
        channel: channel,
        tick_size: tick_size,
        reference_price: reference_price,
        child_order_id: NULL,
        activated_at: NULL,
        cancelled_at: NULL,
        rejected_reason: NULL
    }

2.3. Lưu vào Database
    INSERT INTO trailing_stop_orders VALUES (trailing_stop_order)

2.4. Đăng ký lệnh vào Monitor Queue
    REGISTER_TO_MONITOR_QUEUE(order_id, symbol)
```

**Bước 3: Gửi phản hồi cho khách hàng**

```
3.1. Tạo Success Response
    response = {
        order_id: order_id,
        status: "PENDING_ACTIVATION",
        created_at: current_time,
        message: "Đặt lệnh Trailing Stop thành công"
    }

3.2. Gửi thông báo
    SEND_NOTIFICATION(customer_id, "ORDER_CREATED", order_id)

3.3. Return response
    RETURN HTTP 201 with response
```

**Business Logic:**

- Không kiểm tra sức mua/sức bán tại thời điểm đặt lệnh
- Không kiểm tra giá trần/sàn tại thời điểm đặt lệnh
- Chỉ validate format và business rules cơ bản
- Lưu giá kích hoạt ban đầu và giá kích hoạt hiện tại (ban đầu giống nhau)

**Error Handling:**

- Nếu validation fail → Trả về HTTP 400 với danh sách lỗi
- Nếu mã CK không tồn tại → HTTP 400 "Mã chứng khoán không hợp lệ"
- Nếu database error → HTTP 500 "Lỗi hệ thống, vui lòng thử lại"
- Nếu market data unavailable → HTTP 503 "Dữ liệu thị trường tạm thời không khả dụng"

#### OUTPUT

**Success Response (HTTP 201):**

```json
{
  "order_id": "TS-20251117-000001",
  "status": "PENDING_ACTIVATION",
  "created_at": "2025-11-17T11:00:00Z",
  "message": "Đặt lệnh Trailing Stop thành công"
}
```

**Error Response (HTTP 400):**

```json
{
  "error_code": "VALIDATION_ERROR",
  "message": "Dữ liệu đầu vào không hợp lệ",
  "errors": [
    {
      "field": "volume",
      "message": "Khối lượng phải là bội số của 100"
    },
    {
      "field": "trailing_amount",
      "message": "Biên độ trượt không đúng bước giá. Gợi ý: 600"
    }
  ]
}
```

**Warning Response (HTTP 200 with warnings):**

```json
{
  "warnings": [
    {
      "field": "trigger_price",
      "message": "Giá kích hoạt ≥ Giá TT, lệnh sẽ được kích hoạt ngay lập tức. Bạn có chắc muốn tiếp tục?"
    }
  ],
  "requires_confirmation": true
}
```

### 6.2 IPO Flow cho Monitor và Kích hoạt lệnh

#### INPUT

**System Input (Real-time Market Data):**

| Tham số | Mô tả | Kiểu | Frequency | Ví dụ |
|---------|-------|------|-----------|-------|
| symbol | Mã chứng khoán | String | Per tick | "KBC" |
| market_price | Giá thị trường hiện tại | Decimal | Real-time (1s) | 35800 |
| trading_status | Trạng thái giao dịch | String | Real-time | "TRADING" |
| current_time | Thời gian hiện tại | DateTime | Per second | "2025-11-17T13:25:30Z" |

**Order Data từ Database:**

| Tham số | Mô tả | Kiểu | Ví dụ |
|---------|-------|------|-------|
| order_id | ID lệnh | String | "TS-20251117-000001" |
| side | Chiều | String | "SELL" |
| symbol | Mã CK | String | "KBC" |
| volume | Khối lượng | Integer | 100 |
| current_trigger_price | Giá kích hoạt hiện tại | Decimal | 35300 |
| trailing_amount | Biên độ trượt | Decimal | 600 |
| child_order_type | Loại lệnh con | String | "LO" |
| activation_price_offset | Bước giá kích hoạt | Decimal | 500 |
| status | Trạng thái | String | "PENDING_ACTIVATION" |
| expiry_date | Ngày hết hạn | Date | "2025-11-19" |
| tick_size | Bước giá | Decimal | 100 |

#### PROCESS

**Bước 1: Monitor và điều chỉnh giá kích hoạt (Background Process - chạy liên tục)**

```
1.1. Lấy danh sách lệnh cần monitor
    active_orders = SELECT * FROM trailing_stop_orders
                    WHERE status = "PENDING_ACTIVATION"
                    AND expiry_date >= current_date

1.2. Với mỗi lệnh, kiểm tra và điều chỉnh giá kích hoạt
    FOR EACH order IN active_orders DO

        # Lấy giá thị trường hiện tại
        market_price = GET_MARKET_PRICE(order.symbol)

        # Kiểm tra trạng thái giao dịch
        IF trading_status == "HALTED" OR trading_status == "CLOSED" THEN
            CONTINUE  # Bỏ qua lệnh này, chờ thị trường mở lại
        END IF

        # Logic điều chỉnh giá kích hoạt
        new_trigger_price = order.current_trigger_price

        IF order.side == "SELL" THEN
            # Lệnh BÁN: Giá kích hoạt chỉ TĂNG khi giá thị trường TĂNG
            IF market_price > order.current_trigger_price THEN
                new_trigger_price = market_price - order.trailing_amount
                new_trigger_price = ROUND_TO_TICK(new_trigger_price, order.tick_size)
            END IF

            # Kiểm tra điều kiện kích hoạt: Giá thị trường GIẢM xuống dưới giá kích hoạt
            IF market_price <= order.current_trigger_price THEN
                TRIGGER_ORDER(order, market_price)
                CONTINUE  # Bỏ qua các bước tiếp theo
            END IF

        ELSE IF order.side == "BUY" THEN
            # Lệnh MUA: Giá kích hoạt chỉ GIẢM khi giá thị trường GIẢM
            IF market_price < order.current_trigger_price THEN
                new_trigger_price = market_price + order.trailing_amount
                new_trigger_price = ROUND_TO_TICK(new_trigger_price, order.tick_size)
            END IF

            # Kiểm tra điều kiện kích hoạt: Giá thị trường TĂNG vượt giá kích hoạt
            IF market_price >= order.current_trigger_price THEN
                TRIGGER_ORDER(order, market_price)
                CONTINUE  # Bỏ qua các bước tiếp theo
            END IF
        END IF

        # Cập nhật giá kích hoạt mới (nếu thay đổi)
        IF new_trigger_price != order.current_trigger_price THEN
            UPDATE trailing_stop_orders
            SET current_trigger_price = new_trigger_price,
                updated_at = current_time
            WHERE order_id = order.order_id
        END IF

    END FOR

1.3. Kiểm tra lệnh hết hạn
    FOR EACH order IN active_orders DO
        is_expired = FALSE

        IF order.validity_type == "DAY" AND current_time >= "14:45:00" THEN
            is_expired = TRUE
        END IF

        IF order.validity_type == "GTD" AND current_date > order.expiry_date THEN
            is_expired = TRUE
        END IF

        IF is_expired THEN
            UPDATE trailing_stop_orders
            SET status = "EXPIRED",
                updated_at = current_time
            WHERE order_id = order.order_id

            SEND_NOTIFICATION(order.customer_id, "ORDER_EXPIRED", order.order_id)
        END IF
    END FOR
```

**Bước 2: Kích hoạt lệnh (Function TRIGGER_ORDER)**

```
Function TRIGGER_ORDER(order, current_market_price):

    2.1. Tính giá lệnh con
        IF order.side == "SELL" THEN
            # Lệnh BÁN: Giá lệnh con = Giá kích hoạt - Bước giá kích hoạt
            child_order_price = order.current_trigger_price - order.activation_price_offset
        ELSE IF order.side == "BUY" THEN
            # Lệnh MUA: Giá lệnh con = Giá kích hoạt + Bước giá kích hoạt
            child_order_price = order.current_trigger_price + order.activation_price_offset
        END IF

        # Làm tròn theo bước giá
        child_order_price = ROUND_TO_TICK(child_order_price, order.tick_size)

        # Nếu chọn MTL, không cần giá (hoặc giá = NULL)
        IF order.child_order_type == "MTL" THEN
            child_order_price = NULL
        END IF

    2.2. Validate điều kiện trước khi đẩy lệnh lên sàn
        validation_result = VALIDATE_ORDER_ACTIVATION(
            customer_id: order.customer_id,
            account_number: order.account_number,
            side: order.side,
            symbol: order.symbol,
            volume: order.volume,
            price: child_order_price
        )

        IF validation_result.is_valid == FALSE THEN
            # Lệnh bị từ chối do không đủ điều kiện
            UPDATE trailing_stop_orders
            SET status = "REJECTED",
                rejected_reason = validation_result.reason,
                updated_at = current_time
            WHERE order_id = order.order_id

            SEND_NOTIFICATION(order.customer_id, "ORDER_REJECTED", {
                order_id: order.order_id,
                reason: validation_result.reason
            })

            RETURN
        END IF

    2.3. Tạo lệnh con và gửi lên sàn
        child_order_id = GENERATE_ORDER_ID(order.child_order_type)  # LO-xxx hoặc MTL-xxx

        child_order = {
            order_id: child_order_id,
            parent_order_id: order.order_id,
            order_type: order.child_order_type,
            customer_id: order.customer_id,
            account_number: order.account_number,
            symbol: order.symbol,
            side: order.side,
            volume: order.volume,
            price: child_order_price,
            status: "PENDING_SEND",
            created_at: current_time
        }

        # Lưu lệnh con vào database
        INSERT INTO orders VALUES (child_order)

        # Gửi lệnh con lên sàn
        exchange_response = SEND_ORDER_TO_EXCHANGE(child_order)

        IF exchange_response.success == TRUE THEN
            # Cập nhật trạng thái lệnh Trailing Stop
            UPDATE trailing_stop_orders
            SET status = "ACTIVATED",
                child_order_id = child_order_id,
                activated_at = current_time,
                updated_at = current_time
            WHERE order_id = order.order_id

            # Cập nhật trạng thái lệnh con
            UPDATE orders
            SET status = "SENT_TO_EXCHANGE",
                exchange_order_id = exchange_response.exchange_order_id
            WHERE order_id = child_order_id

            # Thông báo khách hàng
            SEND_NOTIFICATION(order.customer_id, "ORDER_ACTIVATED", {
                parent_order_id: order.order_id,
                child_order_id: child_order_id,
                activation_price: order.current_trigger_price,
                child_order_price: child_order_price
            })

        ELSE
            # Gửi lệnh lên sàn thất bại
            UPDATE trailing_stop_orders
            SET status = "REJECTED",
                rejected_reason = "EXCHANGE_ERROR: " + exchange_response.error_message,
                updated_at = current_time
            WHERE order_id = order.order_id

            SEND_NOTIFICATION(order.customer_id, "ORDER_REJECTED", {
                order_id: order.order_id,
                reason: exchange_response.error_message
            })
        END IF

    RETURN
```

**Function VALIDATE_ORDER_ACTIVATION (Kiểm tra điều kiện khi kích hoạt):**

```
Function VALIDATE_ORDER_ACTIVATION(customer_id, account_number, side, symbol, volume, price):

    # Lấy thông tin tài khoản
    account = GET_ACCOUNT_INFO(customer_id, account_number)

    # Lấy thông tin thị trường
    market_info = GET_MARKET_INFO(symbol)
    ceiling_price = market_info.ceiling_price
    floor_price = market_info.floor_price

    # Kiểm tra sức mua/bán
    IF side == "BUY" THEN
        required_amount = volume * price
        IF account.buying_power < required_amount THEN
            RETURN {
                is_valid: FALSE,
                reason: "INSUFFICIENT_BUYING_POWER"
            }
        END IF
    ELSE IF side == "SELL" THEN
        available_volume = GET_AVAILABLE_VOLUME(account_number, symbol)
        IF available_volume < volume THEN
            RETURN {
                is_valid: FALSE,
                reason: "INSUFFICIENT_SELLING_VOLUME"
            }
        END IF
    END IF

    # Kiểm tra giá trần/sàn (nếu là lệnh LO)
    IF price != NULL THEN
        IF price > ceiling_price THEN
            RETURN {
                is_valid: FALSE,
                reason: "PRICE_EXCEEDS_CEILING"
            }
        END IF

        IF price < floor_price THEN
            RETURN {
                is_valid: FALSE,
                reason: "PRICE_BELOW_FLOOR"
            }
        END IF
    END IF

    # Kiểm tra trạng thái tài khoản
    IF account.status != "ACTIVE" THEN
        RETURN {
            is_valid: FALSE,
            reason: "ACCOUNT_INACTIVE"
        }
    END IF

    # Tất cả validation pass
    RETURN {
        is_valid: TRUE,
        reason: NULL
    }
```

**Business Logic:**

- Monitor giá thị trường với tần suất tối thiểu 1 giây/lần
- Giá kích hoạt chỉ điều chỉnh theo một chiều:
  - Lệnh BÁN: Chỉ TĂNG khi giá thị trường TĂNG
  - Lệnh MUA: Chỉ GIẢM khi giá thị trường GIẢM
- Làm tròn giá kích hoạt theo bước giá
- Kích hoạt khi:
  - Lệnh BÁN: market_price <= current_trigger_price
  - Lệnh MUA: market_price >= current_trigger_price
- Validate đầy đủ (sức mua/bán, giá trần/sàn) TRƯỚC KHI gửi lệnh lên sàn

**Error Handling:**

- Nếu không đủ sức mua/bán → Trạng thái = "REJECTED", lý do = "INSUFFICIENT_BUYING_POWER" hoặc "INSUFFICIENT_SELLING_VOLUME"
- Nếu giá vượt trần/sàn → Trạng thái = "REJECTED", lý do = "PRICE_EXCEEDS_CEILING" hoặc "PRICE_BELOW_FLOOR"
- Nếu gửi lệnh lên sàn thất bại → Trạng thái = "REJECTED", lý do = "EXCHANGE_ERROR"
- Nếu thị trường tạm dừng → Tiếp tục monitor, không kích hoạt

#### OUTPUT

**Success Output khi kích hoạt:**

```json
{
  "parent_order_id": "TS-20251117-000001",
  "child_order_id": "LO-20251117-123456",
  "status": "ACTIVATED",
  "activation_time": "2025-11-17T13:25:30Z",
  "activation_price": 35300,
  "child_order_price": 35800,
  "message": "Lệnh Trailing Stop đã được kích hoạt và gửi lên sàn"
}
```

**Rejection Output:**

```json
{
  "order_id": "TS-20251117-000001",
  "status": "REJECTED",
  "rejection_reason": "INSUFFICIENT_BUYING_POWER",
  "rejection_time": "2025-11-17T13:25:31Z",
  "message": "Lệnh không được kích hoạt do không đủ sức mua"
}
```

**Side Effects:**
- Cập nhật `trailing_stop_orders.current_trigger_price` mỗi khi giá kích hoạt thay đổi
- Tạo bản ghi `orders` mới khi lệnh kích hoạt
- Gửi notification cho khách hàng khi lệnh kích hoạt hoặc bị từ chối
- Gửi lệnh đến exchange system

### 6.3 IPO Flow cho Hủy lệnh Trailing Stop

#### INPUT

**User Input:**

| Tham số | Mô tả | Kiểu | Bắt buộc | Ví dụ |
|---------|-------|------|----------|-------|
| order_id | ID lệnh cần hủy | String | Có | "TS-20251117-000001" |

**System Input:**

| Tham số | Mô tả | Kiểu | Nguồn | Ví dụ |
|---------|-------|------|-------|-------|
| customer_id | ID khách hàng | String | Session | "CUST123456" |
| current_time | Thời gian hiện tại | DateTime | System | "2025-11-17T12:00:00Z" |

#### PROCESS

```
Bước 1: Validate quyền hủy lệnh
    order = SELECT * FROM trailing_stop_orders WHERE order_id = input.order_id

    IF order NOT FOUND THEN
        RETURN Error "Không tìm thấy lệnh"
    END IF

    IF order.customer_id != customer_id THEN
        RETURN Error "Bạn không có quyền hủy lệnh này"
    END IF

    IF order.status != "PENDING_ACTIVATION" THEN
        RETURN Error "Không thể hủy lệnh này. Chỉ hủy được lệnh đang chờ kích hoạt."
    END IF

Bước 2: Hủy lệnh
    UPDATE trailing_stop_orders
    SET status = "CANCELLED",
        cancelled_at = current_time,
        updated_at = current_time
    WHERE order_id = input.order_id

    # Xóa khỏi monitor queue
    REMOVE_FROM_MONITOR_QUEUE(input.order_id)

Bước 3: Thông báo khách hàng
    SEND_NOTIFICATION(customer_id, "ORDER_CANCELLED", input.order_id)

    RETURN Success Response
```

**Business Logic:**
- Chỉ hủy được lệnh ở trạng thái "PENDING_ACTIVATION"
- Lệnh đã kích hoạt/hết hạn/bị từ chối không thể hủy
- Sau khi hủy, lệnh không thể khôi phục

**Error Handling:**
- Order không tồn tại → HTTP 404 "Không tìm thấy lệnh"
- Không có quyền → HTTP 403 "Bạn không có quyền hủy lệnh này"
- Trạng thái không cho phép hủy → HTTP 400 "Không thể hủy lệnh này"

#### OUTPUT

**Success Response (HTTP 200):**

```json
{
  "order_id": "TS-20251117-000001",
  "status": "CANCELLED",
  "cancelled_at": "2025-11-17T12:00:00Z",
  "message": "Hủy lệnh thành công"
}
```

**Error Response (HTTP 400):**

```json
{
  "error_code": "INVALID_ORDER_STATUS",
  "message": "Không thể hủy lệnh này. Chỉ hủy được lệnh đang chờ kích hoạt.",
  "order_id": "TS-20251117-000001",
  "current_status": "ACTIVATED"
}
```

### 6.4 State Diagram

```
STATE MACHINE - TRAILING STOP ORDER

[PENDING_ACTIVATION] (Chờ kích hoạt)
         |
         |--[Market price meets trigger condition + Validation Pass]--> [ACTIVATED] (Đã kích hoạt) ✓
         |
         |--[Market price meets trigger condition + Validation Fail]--> [REJECTED] (Bị từ chối) ✓
         |
         |--[User cancels]--> [CANCELLED] (Đã hủy) ✓
         |
         |--[Expiry time reached]--> [EXPIRED] (Hết hạn) ✓
```

**Trạng thái (States):**

| Trạng thái | Mô tả | Trạng thái tiếp theo có thể | Terminal State |
|------------|-------|----------------------------|----------------|
| PENDING_ACTIVATION | Lệnh đang chờ kích hoạt, hệ thống monitor giá real-time | ACTIVATED, REJECTED, CANCELLED, EXPIRED | No |
| ACTIVATED | Lệnh đã kích hoạt, lệnh con đã được gửi lên sàn | - | Yes |
| REJECTED | Lệnh kích hoạt nhưng không đủ điều kiện để gửi lên sàn | - | Yes |
| CANCELLED | Lệnh bị hủy bởi khách hàng | - | Yes |
| EXPIRED | Lệnh hết thời gian hiệu lực | - | Yes |

**Chuyển trạng thái (Transitions):**

| Từ trạng thái | Sự kiện | Điều kiện | Đến trạng thái | Side Effects |
|---------------|---------|-----------|----------------|--------------|
| PENDING_ACTIVATION | Market price triggers | (side=BUY AND market_price >= trigger_price) OR (side=SELL AND market_price <= trigger_price), AND validation pass | ACTIVATED | • Tạo lệnh con<br>• Gửi lệnh lên sàn<br>• Gửi notification<br>• Ghi log |
| PENDING_ACTIVATION | Market price triggers but validation fails | Trigger condition met BUT (insufficient buying power OR insufficient selling volume OR price exceeds ceiling/floor) | REJECTED | • Ghi lý do từ chối<br>• Gửi notification<br>• Ghi log |
| PENDING_ACTIVATION | User cancels order | User action AND status = PENDING_ACTIVATION | CANCELLED | • Xóa khỏi monitor queue<br>• Gửi notification<br>• Ghi log |
| PENDING_ACTIVATION | Expiry time reached | (validity_type=DAY AND current_time >= 14:45) OR (validity_type=GTD AND current_date > expiry_date) | EXPIRED | • Xóa khỏi monitor queue<br>• Gửi notification<br>• Ghi log |

---

## 7. YÊU CẦU GIAO DIỆN NGƯỜI DÙNG

### 7.1 Màn hình đặt lệnh Trailing Stop

**Tên màn hình**: Đặt lệnh Trailing Stop

**Mục đích**: Cho phép khách hàng đặt lệnh Trailing Stop với đầy đủ tham số và validation

**Layout (Text-based wireframe):**

```
+---------------------------------------------------------------+
|  ← Quay lại                    ĐẶT LỆNH TRAILING STOP         |
+---------------------------------------------------------------+
|                                                               |
|  Loại lệnh: [Trailing Stop] (readonly, disabled)            |
|                                                               |
|  Chiều: (*) Mua  ( ) Bán                                     |
|                                                               |
|  Mã chứng khoán: [________] (autocomplete)                   |
|                                                               |
|  Khối lượng (CP): [- ] [______] [ +]                         |
|                   (100)          (step: 100)                  |
|                                                               |
|  Giá kích hoạt:                                              |
|    (*) Giá hiện tại (35,000 VNĐ)                             |
|    ( ) Giá tùy chỉnh: [________] VNĐ                         |
|                                                               |
|  Biên độ trượt (D): [________] VNĐ         [?] (tooltip)    |
|                                                               |
|  Loại lệnh giao dịch: (*) LO  ( ) MTL                       |
|                                                               |
|  Bước giá kích hoạt (delta): [- ] [______] [ +]             |
|                               (100) (step: 100) [?] (tooltip)|
|    Gợi ý: 100 - 1,000 VNĐ                                   |
|                                                               |
|  Thời gian hiệu lực:                                         |
|    (*) Trong ngày (hết hạn lúc 14:45)                       |
|    ( ) Đến hạn: [___/___/____] (date picker)                |
|        Tối đa 30 ngày từ hôm nay                             |
|                                                               |
|  ⚠ Warning (nếu có):                                         |
|  • Giá kích hoạt ≥ Giá TT, lệnh sẽ được kích hoạt ngay      |
|                                                               |
|                                                               |
|  [      HỦY      ]              [    ĐẶT LỆNH    ]          |
|                                                               |
+---------------------------------------------------------------+
```

**Các trường dữ liệu:**

| Tên trường | Loại control | Bắt buộc | Giá trị mặc định | Ghi chú |
|------------|--------------|----------|------------------|---------|
| Loại lệnh | Label (readonly) | - | "Trailing Stop" | Không cho chỉnh sửa |
| Chiều | Radio button | Có | - | 2 options: "Mua", "Bán" |
| Mã chứng khoán | Autocomplete textbox | Có | - | Gợi ý danh sách mã CK khi gõ |
| Khối lượng | Number input với nút +/- | Có | - | Step = 100, min = 100 |
| Giá kích hoạt | Radio + Number input | Có | "Giá hiện tại" | 2 options: "Giá hiện tại", "Giá tùy chỉnh" |
| Biên độ trượt | Number input | Có | - | Hiển thị tooltip giải thích |
| Loại lệnh giao dịch | Radio button | Có | "LO" | 2 options: "LO", "MTL" |
| Bước giá kích hoạt | Number input với nút +/- | Có (nếu LO) | - | Step = 100, min = 100, hiển thị tooltip |
| Thời gian hiệu lực | Radio + Date picker | Có | "Trong ngày" | 2 options: "Trong ngày", "Đến hạn" |
| Ngày hết hạn | Date picker | Có (nếu "Đến hạn") | - | Min = Hôm nay, Max = Hôm nay + 30 ngày |

**Actions:**

- Button "Hủy": Đóng màn hình, không lưu dữ liệu
- Button "Đặt lệnh":
  - Validate tất cả trường
  - Nếu có Error → Hiển thị lỗi, không cho submit
  - Nếu có Warning → Hiển thị popup xác nhận, cho phép submit sau khi xác nhận
  - Nếu Pass → Submit lệnh, hiển thị loading, chuyển sang màn hình Sổ lệnh sau khi thành công

**Validation & Error Display:**

- Hiển thị lỗi real-time khi rời khỏi trường (onBlur)
- Error: Hiển thị màu đỏ dưới trường, icon ✗, không cho submit
- Warning: Hiển thị màu vàng/cam, icon ⚠, cho phép submit sau xác nhận
- Tooltip: Icon [?] bên cạnh trường, hiển thị giải thích khi hover

**Tooltip content:**

- **Biên độ trượt**: "Khoảng giá chênh lệch để xác định điểm đảo chiều. Khi giá thị trường thay đổi theo hướng có lợi, giá kích hoạt sẽ tự động điều chỉnh theo, duy trì khoảng cách = Biên độ trượt."
- **Bước giá kích hoạt**: "Khoảng giá cộng/trừ vào giá kích hoạt để tạo giá lệnh con, giúp tăng khả năng khớp. Gợi ý: 100 - 1,000 VNĐ."

### 7.2 Màn hình Sổ lệnh Trailing Stop

**Tên màn hình**: Sổ lệnh điều kiện - Trailing Stop

**Mục đích**: Hiển thị danh sách lệnh Trailing Stop với đầy đủ thông tin và cho phép hủy lệnh

**Layout:**

```
+---------------------------------------------------------------+
|  SỔ LỆNH ĐIỀU KIỆN - TRAILING STOP          [+ Đặt lệnh mới] |
+---------------------------------------------------------------+
|  Filter: [Mã CK: ____] [Chiều: All ▼] [Trạng thái: All ▼]   |
|          [Từ ngày: __/__/__] [Đến ngày: __/__/__]  [Lọc]    |
+---------------------------------------------------------------+
|  Tổng: 15 lệnh     [Chờ kích hoạt: 8] [Đã kích hoạt: 5]     |
|                    [Đã hủy: 1] [Bị từ chối: 1]               |
+---------------------------------------------------------------+
| Thời gian | Mã | Chiều | KL | Giá KH | Giá KH | Biên | Trạng | Action |
|           | CK |       |    | ban đầu| hiện tại| độ  | thái  |        |
+---------------------------------------------------------------+
| 17/11/25  |KBC | Bán  |100 | 35,300 | 35,800 | 600  | 🟡Chờ | [Hủy]  |
| 11:00:00  |    |      |    |        |(↑)     |      | kích  | [Chi   |
|           |    |      |    |        |        |      | hoạt  | tiết]  |
+---------------------------------------------------------------+
| 17/11/25  |VNM | Mua  |200 | 82,500 | 82,200 | 300  | 🟡Chờ | [Hủy]  |
| 10:30:15  |    |      |    |        |(↓)     |      | kích  | [Chi   |
|           |    |      |    |        |        |      | hoạt  | tiết]  |
+---------------------------------------------------------------+
| 16/11/25  |HPG | Bán  |500 | 28,700 | 28,700 | 500  | 🟢Đã  |  -     |
| 14:22:10  |    |      |    |        |        |      | kích  | [Chi   |
|           |    |      |    |        |        |      | hoạt  | tiết]  |
+---------------------------------------------------------------+
| 16/11/25  |VIC | Mua  |100 | 45,000 | -      | 1000 | 🔴Bị  |  -     |
| 13:15:20  |    |      |    |        |        |      | từ    | [Chi   |
|           |    |      |    |        |        |      | chối  | tiết]  |
+---------------------------------------------------------------+
|  [< Trước]              Trang 1/1              [Tiếp >]      |
+---------------------------------------------------------------+
```

**Các cột hiển thị:**

| Tên cột | Kiểu dữ liệu | Có thể sort | Có thể filter | Mô tả |
|---------|--------------|-------------|---------------|-------|
| Thời gian | DateTime | Có | Có (Date range) | Thời gian đặt lệnh (DD/MM/YYYY HH:mm:ss) |
| Mã CK | String | Có | Có (Search) | Mã chứng khoán |
| Chiều | String | Có | Có (Dropdown: All/Mua/Bán) | Mua hoặc Bán |
| KL | Integer | Có | Không | Khối lượng |
| Giá KH ban đầu | Decimal | Không | Không | Giá kích hoạt lúc đặt lệnh |
| Giá KH hiện tại | Decimal | Có | Không | Giá kích hoạt được cập nhật real-time (chỉ với lệnh "Chờ kích hoạt"). Hiển thị mũi tên ↑↓ khi thay đổi |
| Biên độ | Decimal | Không | Không | Biên độ trượt (VNĐ) |
| Bước giá | Decimal | Không | Không | Bước giá kích hoạt (VNĐ) |
| Loại lệnh GD | String | Không | Có (Dropdown: All/LO/MTL) | LO hoặc MTL |
| Trạng thái | String | Có | Có (Dropdown: All/Chờ kích hoạt/Đã kích hoạt/Đã hủy/Bị từ chối) | Trạng thái lệnh với icon màu sắc |
| Ngày hết hạn | Date | Có | Không | Ngày hết hiệu lực |
| Kênh | String | Không | Có (Dropdown) | Web/Mobile/DBoard |
| Action | Button | - | - | Hủy (nếu cho phép), Chi tiết |

**Actions trên dòng:**

- **Nút "Hủy"**: Chỉ hiển thị khi trạng thái = "Chờ kích hoạt"
  - Click → Hiển thị popup xác nhận
  - Sau khi xác nhận → Hủy lệnh, cập nhật trạng thái ngay lập tức
- **Nút "Chi tiết"**: Hiển thị popup/modal với đầy đủ thông tin lệnh và lịch sử thay đổi giá kích hoạt

**Pagination:**
- Số bản ghi mỗi trang: 20
- Loại pagination: Server-side (do có real-time update)
- Hiển thị tổng số lệnh và số lệnh theo từng trạng thái

**Real-time update:**
- Cột "Giá KH hiện tại" cập nhật real-time cho lệnh "Chờ kích hoạt"
- Hiển thị mũi tên ↑ (màu xanh) khi giá tăng, ↓ (màu đỏ) khi giá giảm
- Trạng thái lệnh cập nhật ngay khi thay đổi (kích hoạt, hết hạn, bị từ chối)

---

## 8. PHỤ LỤC

### 8.1 Wireframes/Mockups

⚠️ **Assumption**: Wireframes/Mockups sẽ được thiết kế bởi UI/UX team dựa trên mô tả trong Section 7.

### 8.2 Data Samples

#### Sample 1: Lệnh Trailing Stop Sell

```json
{
  "order_id": "TS-20251117-000001",
  "order_type": "TRAILING_STOP",
  "customer_id": "CUST123456",
  "account_number": "0001234567",
  "symbol": "KBC",
  "side": "SELL",
  "volume": 100,
  "initial_trigger_price": 35300,
  "current_trigger_price": 35800,
  "trailing_amount": 600,
  "child_order_type": "LO",
  "activation_price_offset": 500,
  "validity_type": "GTD",
  "expiry_date": "2025-11-19",
  "status": "PENDING_ACTIVATION",
  "created_at": "2025-11-17T11:00:00Z",
  "updated_at": "2025-11-17T13:20:15Z",
  "channel": "DBOARD",
  "tick_size": 100,
  "reference_price": 35000,
  "child_order_id": null,
  "activated_at": null,
  "cancelled_at": null,
  "rejected_reason": null
}
```

#### Sample 2: Lệnh Trailing Stop Buy đã kích hoạt

```json
{
  "order_id": "TS-20251116-000045",
  "order_type": "TRAILING_STOP",
  "customer_id": "CUST654321",
  "account_number": "0009876543",
  "symbol": "HPG",
  "side": "BUY",
  "volume": 500,
  "initial_trigger_price": 28500,
  "current_trigger_price": 28200,
  "trailing_amount": 500,
  "child_order_type": "MTL",
  "activation_price_offset": null,
  "validity_type": "DAY",
  "expiry_date": "2025-11-16",
  "status": "ACTIVATED",
  "created_at": "2025-11-16T09:15:00Z",
  "updated_at": "2025-11-16T14:22:10Z",
  "channel": "MOBILE",
  "tick_size": 100,
  "reference_price": 28700,
  "child_order_id": "MTL-20251116-123456",
  "activated_at": "2025-11-16T14:22:10Z",
  "cancelled_at": null,
  "rejected_reason": null
}
```

#### Sample 3: Lệnh bị từ chối

```json
{
  "order_id": "TS-20251116-000030",
  "order_type": "TRAILING_STOP",
  "customer_id": "CUST111222",
  "account_number": "0001112223",
  "symbol": "VIC",
  "side": "BUY",
  "volume": 100,
  "initial_trigger_price": 45000,
  "current_trigger_price": 45000,
  "trailing_amount": 1000,
  "child_order_type": "LO",
  "activation_price_offset": 500,
  "validity_type": "DAY",
  "expiry_date": "2025-11-16",
  "status": "REJECTED",
  "created_at": "2025-11-16T10:00:00Z",
  "updated_at": "2025-11-16T13:15:20Z",
  "channel": "WEB",
  "tick_size": 100,
  "reference_price": 44500,
  "child_order_id": null,
  "activated_at": null,
  "cancelled_at": null,
  "rejected_reason": "INSUFFICIENT_BUYING_POWER"
}
```

### 8.3 Error Code Reference

| Error Code | HTTP Status | Mô tả | Message (Tiếng Việt) |
|------------|-------------|-------|---------------------|
| VALIDATION_ERROR | 400 | Dữ liệu đầu vào không hợp lệ | "Dữ liệu đầu vào không hợp lệ" |
| INVALID_VOLUME | 400 | Khối lượng không hợp lệ | "Khối lượng phải là số nguyên dương và là bội số của 100" |
| INVALID_SYMBOL | 400 | Mã CK không hợp lệ | "Mã chứng khoán không hợp lệ hoặc không được hỗ trợ" |
| INVALID_TRAILING_AMOUNT | 400 | Biên độ trượt không hợp lệ | "Biên độ trượt phải lớn hơn 0 và là bội số của bước giá" |
| INVALID_ACTIVATION_OFFSET | 400 | Bước giá kích hoạt không hợp lệ | "Bước giá kích hoạt phải lớn hơn 0 và là bội số của bước giá" |
| INVALID_EXPIRY_DATE | 400 | Ngày hết hạn không hợp lệ | "Ngày hết hạn không hợp lệ hoặc vượt quá 30 ngày" |
| ORDER_NOT_FOUND | 404 | Không tìm thấy lệnh | "Không tìm thấy lệnh" |
| UNAUTHORIZED | 403 | Không có quyền | "Bạn không có quyền thực hiện hành động này" |
| INVALID_ORDER_STATUS | 400 | Trạng thái lệnh không cho phép hành động | "Không thể hủy lệnh này. Chỉ hủy được lệnh đang chờ kích hoạt." |
| INSUFFICIENT_BUYING_POWER | 400 | Không đủ sức mua | "Không đủ sức mua để kích hoạt lệnh" |
| INSUFFICIENT_SELLING_VOLUME | 400 | Không đủ khối lượng bán | "Không đủ khối lượng chứng khoán để bán" |
| PRICE_EXCEEDS_CEILING | 400 | Giá vượt trần | "Giá lệnh vượt quá giá trần" |
| PRICE_BELOW_FLOOR | 400 | Giá dưới sàn | "Giá lệnh thấp hơn giá sàn" |
| ACCOUNT_INACTIVE | 400 | Tài khoản không hoạt động | "Tài khoản không ở trạng thái hoạt động" |
| EXCHANGE_ERROR | 500 | Lỗi kết nối sàn | "Lỗi khi gửi lệnh lên sàn giao dịch" |
| SYSTEM_ERROR | 500 | Lỗi hệ thống | "Lỗi hệ thống, vui lòng thử lại sau" |
| MARKET_DATA_UNAVAILABLE | 503 | Dữ liệu thị trường không khả dụng | "Dữ liệu thị trường tạm thời không khả dụng" |

### 8.4 Business Rules Summary

| BR-ID | Quy tắc | Loại |
|-------|---------|------|
| BR-001 | Không kiểm tra sức mua/bán khi đặt lệnh | Must Have |
| BR-002 | Không kiểm tra giá trần/sàn khi đặt lệnh | Must Have |
| BR-003 | Disable "Bước giá kích hoạt" khi chọn MTL | Must Have |
| BR-004 | Enable và bắt buộc "Bước giá kích hoạt" khi chọn LO | Must Have |
| BR-005 | Tự động lấy giá thị trường khi chọn "Giá hiện tại" | Must Have |
| BR-006 | Bắt buộc nhập giá khi chọn "Giá tùy chỉnh" | Must Have |
| BR-007 | Không hỗ trợ lô lẻ | Must Have |
| BR-008 | Cập nhật giá kích hoạt real-time cho lệnh "Chờ kích hoạt" | Must Have |
| BR-009 | Lệnh "Hết hạn" chỉ hiển thị trong "Lịch sử lệnh" | Must Have |
| BR-010 | Hiển thị thông tin lệnh con khi lệnh "Đã kích hoạt" | Should Have |
| BR-011 | Sắp xếp mặc định: Thời gian mới nhất lên đầu | Should Have |
| BR-012 | Pagination: 20 lệnh/trang | Should Have |
| BR-013 | Chỉ hủy được lệnh "Chờ kích hoạt" | Must Have |
| BR-014 | Xác nhận trước khi hủy | Must Have |
| BR-015 | Lệnh đã hủy không thể khôi phục | Must Have |
| BR-016 | Không hỗ trợ sửa lệnh Trailing Stop | Must Have |
| BR-017 | Lệnh "Trong ngày" hết hạn lúc 14:45 | Must Have |
| BR-018 | Lệnh "Đến hạn" hết hạn vào cuối ngày được chọn | Must Have |
| BR-019 | Giá kích hoạt chỉ điều chỉnh một chiều | Must Have |
| BR-020 | Tính giá lệnh con = Giá kích hoạt ± Bước giá kích hoạt | Must Have |
| BR-021 | Chuyển "Bị từ chối" khi lệnh con không đẩy được lên sàn | Must Have |
| BR-022 | Monitor giá tối thiểu mỗi giây | Must Have |
| BR-023 | Giới hạn số lệnh tối đa (TBD) | Should Have |

### 8.5 Non-Functional Requirements

⚠️ **Note**: Các yêu cầu phi chức năng sau đây cần được xác nhận với Tech Lead và Infrastructure team.

#### Performance

| NFR-ID | Requirement | Target | Priority |
|--------|-------------|--------|----------|
| NFR-001 | Response time cho API đặt lệnh | < 1 giây (P95) | Must Have |
| NFR-002 | Response time cho API xem sổ lệnh | < 2 giây (P95) | Must Have |
| NFR-003 | Response time cho API hủy lệnh | < 500ms (P95) | Must Have |
| NFR-004 | Tần suất cập nhật giá kích hoạt | Tối thiểu mỗi giây | Must Have |
| NFR-005 | Latency từ khi giá thị trường thay đổi đến khi cập nhật giá kích hoạt | < 2 giây | Must Have |
| NFR-006 | Latency từ khi thỏa điều kiện kích hoạt đến khi gửi lệnh lên sàn | < 5 giây | Must Have |
| NFR-007 | Hỗ trợ đồng thời | 10,000 lệnh Trailing Stop active cùng lúc | Should Have |
| NFR-008 | Throughput cho monitor service | Xử lý 1,000 lệnh/giây | Should Have |

#### Availability & Reliability

| NFR-ID | Requirement | Target | Priority |
|--------|-------------|--------|----------|
| NFR-009 | Uptime | 99.9% (business hours: 8:30-15:00) | Must Have |
| NFR-010 | Data consistency | 100% (không được mất lệnh) | Must Have |
| NFR-011 | Recovery time khi hệ thống crash | < 5 phút | Must Have |

#### Security

| NFR-ID | Requirement | Target | Priority |
|--------|-------------|--------|----------|
| NFR-012 | Authentication | Bắt buộc với mỗi request | Must Have |
| NFR-013 | Authorization | Chỉ xem/hủy được lệnh của chính mình | Must Have |
| NFR-014 | Audit logging | Ghi log đầy đủ mọi thao tác (đặt, hủy, kích hoạt) | Must Have |
| NFR-015 | Data encryption | Encrypt sensitive data (customer_id, account_number) | Should Have |

#### Scalability

| NFR-ID | Requirement | Target | Priority |
|--------|-------------|--------|----------|
| NFR-016 | Horizontal scaling | Support thêm server khi tải tăng | Should Have |
| NFR-017 | Database scalability | Support sharding/partitioning | Could Have |

#### Monitoring & Alerting

| NFR-ID | Requirement | Target | Priority |
|--------|-------------|--------|----------|
| NFR-018 | Real-time monitoring | Dashboard hiển thị số lệnh active, rate kích hoạt, error rate | Must Have |
| NFR-019 | Alerting | Cảnh báo khi error rate > 5%, latency > threshold | Must Have |
| NFR-020 | Logging | Ghi log chi tiết mọi transaction (đặt lệnh, điều chỉnh giá, kích hoạt, hủy) | Must Have |

### 8.6 Assumptions & Constraints

#### Assumptions (Giả định)

| Assumption ID | Giả định | Impact nếu sai |
|---------------|----------|----------------|
| ASSUM-001 | Market data feed cung cấp giá thị trường real-time với độ trễ < 1 giây | Ảnh hưởng đến độ chính xác của giá kích hoạt và thời điểm kích hoạt lệnh |
| ASSUM-002 | API tích hợp sàn giao dịch có response time < 2 giây | Ảnh hưởng đến latency khi gửi lệnh con lên sàn |
| ASSUM-003 | Hệ thống có thể lưu trữ lịch sử lệnh tối thiểu 90 ngày | Cần điều chỉnh database storage và archiving strategy |
| ASSUM-004 | Bước giá (tick size) không thay đổi trong ngày giao dịch | Cần thêm logic cập nhật bước giá real-time |
| ASSUM-005 | Giá tham chiếu được cập nhật đúng vào đầu mỗi phiên giao dịch | Ảnh hưởng đến validation biên độ trượt |
| ASSUM-006 | Khách hàng không thể đặt lệnh Trailing Stop ngoài giờ giao dịch (trước 8:30 hoặc sau 15:00) | Cần thêm chức năng đặt lệnh trước giờ giao dịch |

#### Constraints (Ràng buộc)

| Constraint ID | Ràng buộc | Lý do |
|---------------|-----------|-------|
| CONST-001 | Chỉ hỗ trợ 3 sàn: HOSE, HNX, UPCOM | Giới hạn theo quy định tích hợp hiện tại |
| CONST-002 | Không hỗ trợ lô lẻ | Quy định giao dịch của sàn |
| CONST-003 | Thời gian hiệu lực tối đa: 30 ngày | Giảm thiểu rủi ro và complexity trong việc quản lý lệnh dài hạn |
| CONST-004 | Không hỗ trợ sửa lệnh | Do đặc thù của Trailing Stop (giá kích hoạt tự động điều chỉnh) |
| CONST-005 | Monitor frequency tối thiểu: 1 giây | Giới hạn bởi performance của market data feed |
| CONST-006 | Không kiểm tra sức mua/bán khi đặt lệnh | Quyết định nghiệp vụ để đơn giản hóa flow đặt lệnh |

### 8.7 Risks & Mitigation

| Risk ID | Rủi ro | Mức độ | Impact | Mitigation |
|---------|--------|--------|--------|-----------|
| RISK-001 | Market data feed bị delay hoặc gián đoạn → Giá kích hoạt không cập nhật đúng | High | Lệnh kích hoạt sai thời điểm, khách hàng mất lợi nhuận/thua lỗ | • Implement fallback mechanism<br>• Monitor latency và alert khi > threshold<br>• Tạm dừng monitor nếu data feed unavailable > 30s |
| RISK-002 | Hệ thống quá tải khi có quá nhiều lệnh active cùng lúc | Medium | Latency tăng, lệnh kích hoạt chậm | • Implement queue system<br>• Horizontal scaling<br>• Giới hạn số lệnh tối đa/khách hàng |
| RISK-003 | Lệnh con bị sàn từ chối sau khi kích hoạt → Khách hàng không hiểu lý do | Medium | Khiếu nại, mất niềm tin | • Hiển thị rõ lý do từ chối<br>• Thông báo rõ ràng khi đặt lệnh rằng hệ thống không kiểm tra sức mua/bán trước |
| RISK-004 | Race condition khi nhiều lệnh kích hoạt cùng lúc cho cùng tài khoản | Medium | Oversell hoặc overdraw | • Implement distributed lock<br>• Transaction-level isolation<br>• Re-validate sức mua/bán trước khi gửi lệnh |
| RISK-005 | Database crash → Mất dữ liệu lệnh active | High | Mất lệnh khách hàng, mất niềm tin nghiêm trọng | • Database replication (Master-Slave)<br>• Backup mỗi giờ<br>• Point-in-time recovery |
| RISK-006 | Khách hàng không hiểu cách hoạt động của Trailing Stop → Đặt lệnh sai | High | Khiếu nại, mất niềm tin | • Thêm tutorial/guide rõ ràng<br>• Hiển thị ví dụ minh họa<br>• Warning khi đặt lệnh có thể kích hoạt ngay |
| RISK-007 | Giá kích hoạt thay đổi quá nhanh → Khách hàng bối rối | Low | Khiếu nại nhỏ | • Hiển thị lịch sử thay đổi giá kích hoạt<br>• Visualization (chart) |
| RISK-008 | Lỗi trong logic điều chỉnh giá kích hoạt → Lệnh kích hoạt sai | High | Thua lỗ cho khách hàng, trách nhiệm pháp lý | • Code review kỹ lưỡng<br>• Unit test coverage > 90%<br>• Integration test với nhiều scenarios<br>• UAT với khách hàng pilot |

### 8.8 Acceptance Criteria (Tổng hợp)

#### AC-001: Đặt lệnh Trailing Stop thành công

**Scenario 1: Đặt lệnh BÁN với giá tùy chỉnh**

```
Given: Khách hàng đã đăng nhập và có tài khoản hoạt động
And: Giá thị trường KBC = 35,000 VNĐ
When: Khách hàng đặt lệnh Trailing Stop với:
  - Chiều: Bán
  - Mã CK: KBC
  - Khối lượng: 100
  - Giá kích hoạt: Giá tùy chỉnh = 35,300
  - Biên độ trượt: 600
  - Loại lệnh GD: LO
  - Bước giá kích hoạt: 500
  - Thời gian hiệu lực: Đến hạn 19/11/2025
And: Click "Đặt lệnh"
Then: Hệ thống tạo lệnh thành công
And: Hiển thị thông báo "Đặt lệnh Trailing Stop thành công"
And: Lệnh xuất hiện trong Sổ lệnh với trạng thái "Chờ kích hoạt"
And: Giá kích hoạt hiện tại = 35,300
```

**Scenario 2: Validation lỗi khối lượng không phải bội số 100**

```
Given: Khách hàng đang trên màn hình đặt lệnh
When: Nhập Khối lượng = 150
And: Rời khỏi trường Khối lượng (onBlur)
Then: Hiển thị lỗi màu đỏ: "Khối lượng phải là bội số của 100"
And: Nút "Đặt lệnh" bị disable
```

**Scenario 3: Warning giá kích hoạt ngay lập tức (Lệnh BÁN)**

```
Given: Giá thị trường VNM = 82,000 VNĐ
When: Khách hàng đặt lệnh Trailing Stop BÁN với:
  - Giá kích hoạt = 82,000 (bằng giá thị trường)
And: Click "Đặt lệnh"
Then: Hiển thị popup warning: "Giá kích hoạt ≥ Giá TT, lệnh sẽ được kích hoạt ngay lập tức. Bạn có chắc muốn tiếp tục?"
And: Có 2 nút: "Tiếp tục" và "Hủy"
When: Click "Tiếp tục"
Then: Lệnh được tạo thành công
```

#### AC-002: Monitor và điều chỉnh giá kích hoạt

**Scenario 1: Lệnh BÁN - Giá thị trường TĂNG → Giá kích hoạt TĂNG**

```
Given: Lệnh Trailing Stop BÁN với:
  - Giá kích hoạt hiện tại = 35,300
  - Biên độ trượt = 600
  - Trạng thái = "Chờ kích hoạt"
When: Giá thị trường tăng từ 35,000 → 36,000
Then: Giá kích hoạt được điều chỉnh lên 36,000 - 600 = 35,400
And: Cập nhật real-time trên Sổ lệnh
And: Hiển thị mũi tên ↑ màu xanh
```

**Scenario 2: Lệnh BÁN - Giá thị trường GIẢM → Giá kích hoạt GIỮ NGUYÊN**

```
Given: Lệnh Trailing Stop BÁN với:
  - Giá kích hoạt hiện tại = 35,400
  - Biên độ trượt = 600
  - Trạng thái = "Chờ kích hoạt"
When: Giá thị trường giảm từ 36,000 → 35,500
Then: Giá kích hoạt vẫn là 35,400 (không thay đổi)
```

**Scenario 3: Lệnh MUA - Giá thị trường GIẢM → Giá kích hoạt GIẢM**

```
Given: Lệnh Trailing Stop MUA với:
  - Giá kích hoạt hiện tại = 82,500
  - Biên độ trượt = 300
  - Trạng thái = "Chờ kích hoạt"
When: Giá thị trường giảm từ 83,000 → 82,000
Then: Giá kích hoạt được điều chỉnh xuống 82,000 + 300 = 82,300
And: Cập nhật real-time trên Sổ lệnh
And: Hiển thị mũi tên ↓ màu đỏ
```

#### AC-003: Kích hoạt lệnh thành công

**Scenario 1: Lệnh BÁN kích hoạt khi giá thị trường giảm xuống dưới giá kích hoạt**

```
Given: Lệnh Trailing Stop BÁN với:
  - Giá kích hoạt hiện tại = 35,400
  - Bước giá kích hoạt = 500
  - Loại lệnh GD = LO
  - Khối lượng = 100
  - Khách hàng có đủ khối lượng KBC để bán
When: Giá thị trường giảm từ 35,500 → 35,400
Then: Hệ thống kích hoạt lệnh
And: Tạo lệnh con LO với:
  - Giá = 35,400 - 500 = 34,900
  - Khối lượng = 100
And: Gửi lệnh con lên sàn thành công
And: Cập nhật trạng thái lệnh Trailing Stop = "Đã kích hoạt"
And: Gửi thông báo cho khách hàng: "Lệnh Trailing Stop đã được kích hoạt và gửi lên sàn"
```

**Scenario 2: Lệnh MUA kích hoạt với loại lệnh MTL**

```
Given: Lệnh Trailing Stop MUA với:
  - Giá kích hoạt hiện tại = 82,200
  - Loại lệnh GD = MTL
  - Khối lượng = 200
  - Khách hàng có đủ sức mua
When: Giá thị trường tăng từ 82,100 → 82,200
Then: Hệ thống kích hoạt lệnh
And: Tạo lệnh con MTL với:
  - Giá = NULL (MTL không cần giá)
  - Khối lượng = 200
And: Gửi lệnh con lên sàn thành công
And: Cập nhật trạng thái = "Đã kích hoạt"
```

#### AC-004: Lệnh bị từ chối khi kích hoạt

**Scenario: Không đủ sức mua khi kích hoạt lệnh MUA**

```
Given: Lệnh Trailing Stop MUA với:
  - Giá kích hoạt = 45,000
  - Bước giá kích hoạt = 500
  - Khối lượng = 100
  - Giá lệnh con sẽ là 45,500
  - Khách hàng có sức mua chỉ đủ mua 50 CP
When: Giá thị trường đạt điều kiện kích hoạt
And: Hệ thống validate sức mua
Then: Validation fail: Không đủ sức mua
And: Cập nhật trạng thái lệnh = "Bị từ chối"
And: Lưu lý do từ chối = "INSUFFICIENT_BUYING_POWER"
And: Gửi thông báo: "Lệnh không được kích hoạt do không đủ sức mua"
And: Không tạo lệnh con, không gửi lệnh lên sàn
```

#### AC-005: Hủy lệnh thành công

**Scenario: Hủy lệnh đang Chờ kích hoạt**

```
Given: Lệnh Trailing Stop với trạng thái = "Chờ kích hoạt"
And: Khách hàng đang xem Sổ lệnh
When: Click nút "Hủy" trên lệnh đó
Then: Hiển thị popup xác nhận: "Bạn có chắc muốn hủy lệnh Trailing Stop BÁN KBC - Khối lượng 100?"
When: Click "Hủy lệnh"
Then: Lệnh được hủy thành công
And: Cập nhật trạng thái = "Đã hủy"
And: Hiển thị thông báo: "Hủy lệnh thành công"
And: Không thể hủy lại được nữa
```

#### AC-006: Lệnh hết hạn tự động

**Scenario 1: Lệnh "Trong ngày" hết hạn lúc 14:45**

```
Given: Lệnh Trailing Stop với:
  - Thời gian hiệu lực = "Trong ngày"
  - Trạng thái = "Chờ kích hoạt"
  - Ngày tạo = 17/11/2025
When: Thời gian hiện tại = 17/11/2025 14:45:00
Then: Hệ thống tự động cập nhật trạng thái = "Hết hạn"
And: Gửi thông báo: "Lệnh Trailing Stop đã hết hạn"
And: Lệnh chuyển sang "Lịch sử lệnh điều kiện"
```

**Scenario 2: Lệnh "Đến hạn" hết hạn vào ngày được chọn**

```
Given: Lệnh Trailing Stop với:
  - Thời gian hiệu lực = "Đến hạn"
  - Ngày hết hạn = 19/11/2025
  - Trạng thái = "Chờ kích hoạt"
When: Thời gian hiện tại = 20/11/2025 00:00:00
Then: Hệ thống tự động cập nhật trạng thái = "Hết hạn"
```

### 8.9 Additional Documents

- Quy định giao dịch chứng khoán HOSE: [Link TBD]
- Quy định giao dịch chứng khoán HNX: [Link TBD]
- Quy định giao dịch chứng khoán UPCOM: [Link TBD]
- API Documentation - Market Data Feed: [Link TBD]
- API Documentation - Exchange Integration: [Link TBD]
- Database Schema Design: [Link TBD]
- System Architecture Diagram: [Link TBD]

---

**END OF DOCUMENT**

---

**Ghi chú về tài liệu:**

Tài liệu này được tạo dựa trên tài liệu yêu cầu ban đầu và bổ sung các phần còn thiếu (Input, Process trong IPO). Một số thông tin được đánh dấu **TBD** (To Be Determined) cần được xác nhận với các stakeholders:

- Tên và email của các stakeholders (Product Owner, BA, Tech Lead, etc.)
- Số lượng lệnh Trailing Stop tối đa mỗi khách hàng có thể đặt (BR-023)
- Link đến các tài liệu tham khảo (Quy định sàn, API docs, etc.)
- Non-functional requirements cụ thể (cần xác nhận với Tech Lead)

**Giả định (Assumptions) quan trọng cần xác nhận:**

1. Market data feed có độ trễ < 1 giây
2. API sàn giao dịch có response time < 2 giây
3. Hệ thống lưu trữ lịch sử lệnh tối thiểu 90 ngày
4. Khách hàng không thể đặt lệnh ngoài giờ giao dịch

Vui lòng review và xác nhận các phần TBD và Assumptions trước khi bắt đầu phát triển.
