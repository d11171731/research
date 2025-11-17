# Mô tả thiết kế sản phẩm: Bộ lệnh điều kiện (phase 1)

## C. Mô tả Sản phẩm (Phase 1)

### 1. Mô tả CURD Rule Lệnh Trailing Stop

**Đặt lệnh**: Cho phép khách hàng đặt lệnh bằng việc điền/lựa chọn các điều kiện trong bảng dưới đây

| Trường | Mô tả | Điều kiện validate |
|--------|-------|-------------------|
| Loại lệnh | Trailing Stop | |
| Chiều | Mua hoặc Bán | |
| Khối lượng | Khối lượng đặt (CP) | • Chỉ cho phép nhập số nguyên dương, viết liền không dấu<br>• Hệ thống tự động phân cách đơn vị<br>• Là bội số của bước KL lô chẵn (100)<br>(Không hỗ trợ đặt lô lẻ)<br>• Cho phép tăng/giảm bằng nút +/- |
| Mã CK | Mã chứng khoán | • Các mã thuộc 3 sàn HOSE, HNX, UPCOM |
| Giá kích hoạt | Mức giá mà khi thị trường đạt đến, lệnh điều kiện sẽ được kích hoạt và chuyển thành lệnh thông thường. | 2 trường hợp: để KH chọn:<br>1. Giá hiện tại: Hệ thống lấy theo giá thị trường<br>2. Giá KH điền |
| Biên độ trượt (D) | Khoảng giá chênh lệch (theo % hoặc theo giá trị) để xác định điểm đảo chiều (VNĐ) |  |
| Bước giá kích hoạt (delta) | Khoảng giá cộng/trừ so với giá kích hoạt để tăng khả năng khớp (VNĐ) | • Phải > 0<br>• Là bội số của bước giá<br>• Gợi ý: 100 - 1,000 VNĐ<br>• Cho phép tăng/giảm bằng nút +/-<br>• Hiển thị tooltip giải thích |
| Thời gian hiệu lực | Thời hạn hiệu lực của lệnh | • Trong ngày: Hết hiệu lực cuối phiên (14:45)<br>• Đến hạn: Hiển thị lịch chọn cho KH → Tối đa 30 ngày.<br>• Mặc định: Trong ngày |
| Loại lệnh giao dịch | LO hoặc MTL | • Nếu KH chọn giá LO → Enable ô Bước giá kích hoạt<br>• Nếu KH chọn MTL → Disable ô Bước giá kích hoạt |

#### Các nguyên tắc khi đặt lệnh

| Nguyên tắc | Mô tả | Hành động khi vi phạm |
|------------|-------|----------------------|
| Biên độ trượt > 0 | Biên độ trượt phải lớn hơn 0 | Hiển thị lỗi: "Biên độ trượt phải lớn hơn 0" Không cho đặt lệnh |
| Bước giá kích hoạt > 0 | Bước giá kích hoạt phải lớn hơn 0 | Hiển thị lỗi: "Bước giá kích hoạt phải lớn hơn 0" Không cho đặt lệnh |
| Bội số bước giá | Biên độ trượt và Bước giá kích hoạt phải là bội số của bước giá | Hiển thị lỗi: "Giá trị không đúng bước giá. Gợi ý: [giá gần nhất]" Không cho đặt lệnh |
| Giá kích hoạt hợp lý (Lệnh MUA) | KH nên đặt Giá kích hoạt ban đầu > Giá thị trường | Hiển thị cảnh báo: "Giá kích hoạt ≤ Giá TT, lệnh sẽ được kích hoạt ngay lập tức" Vẫn cho đặt lệnh |
| Giá kích hoạt hợp lý (Lệnh BÁN) | KH nên đặt Giá kích hoạt ban đầu < Giá thị trường | Hiển thị cảnh báo: "Giá kích hoạt ≥ Giá TT, lệnh sẽ được kích hoạt ngay lập tức" Vẫn cho đặt lệnh |
| Biên độ trượt hợp lý | Biên độ trượt không nên quá lớn (> 10% giá tham chiếu) | Hiển thị cảnh báo: "Biên độ trượt lớn, lệnh có thể khó kích hoạt" Vẫn cho đặt lệnh |

> **Lưu ý**: Hệ thống KHÔNG kiểm tra sức mua/bán, giá trần/sàn, trạng thái tài khoản khi đặt lệnh Trailing Stop. Chỉ kiểm tra khi lệnh thỏa mãn điều kiện kích hoạt để đẩy lệnh lên Sàn. Do đó, lệnh có thể bị từ chối tại thời điểm kích hoạt nếu không đủ điều kiện.

### 2. Xem Sổ lệnh

Hệ thống hiển thị danh sách các lệnh Trailing Stop với các trạng thái như bảng dưới đây:

| Trạng thái | Mô tả | Nơi hiển thị | Cho phép hủy | Cho phép sửa |
|-----------|-------|--------------|--------------|--------------|
| Chờ kích hoạt | Lệnh đang chờ điều kiện kích hoạt, hệ thống liên tục tính toán giá kích hoạt | Sổ lệnh điều kiện | Có | Không |
| Đã kích hoạt | Lệnh đã thỏa mãn điều kiện, lệnh con đã được sinh và gửi lên sàn | Sổ lệnh điều kiện | Không | Không |
| Đã hủy | Lệnh được hủy thành công | Sổ lệnh điều kiện | Không | Không |
| Hết hạn | Lệnh hết thời gian hiệu lực (cuối phiên nếu "Trong ngày", hoặc đến ngày hết hạn) | Lịch sử lệnh điều kiện | Không | Không |
| Bị từ chối | Lệnh thỏa mãn điều kiện kích hoạt nhưng lệnh con không được đẩy lên Sở thành công do không thỏa mãn điều kiện về sức mua/sức bán, giá trần/sàn... | Sổ lệnh điều kiện | Không | Không |

**Sổ lệnh Trailing Stop sẽ hiển thị các thông tin dưới đây**

### 3. Hủy lệnh

- Chỉ được hủy lệnh với lệnh có trạng thái **Chờ kích hoạt**

### 4. Sửa lệnh

Lệnh Trailing Stop sẽ **không hỗ trợ Sửa lệnh** vì:

- Lệnh Trailing Stop là loại lệnh điều kiện có cơ chế tự động **điều chỉnh giá kích hoạt theo biến động thị trường** nên việc cho phép khách hàng sửa lệnh sẽ làm khách hàng hiểu lầm về giá kích hoạt của lệnh, xảy ra tại thời điểm khách hàng sửa hay tại thời điểm KH đặt lệnh.

## D. Mô tả nguyên tắc hoạt động & xử lý lệnh

### 1. Luồng IPO lệnh điều kiện

#### Trailing Stop

| Thời gian | Lệnh | Loại lệnh | Mã CK | Điều kiện | KL | Giá | Trạng thái | Ngày hết hạn | Kênh đặt |
|-----------|------|-----------|-------|-----------|----|----|-----------|--------------|----------|
| 11:00:000 | Mua | Trailing Stop | KBC | Bước giá trượt: 500<br>Giá kích hoạt ban đầu: 35,300<br>Biên trượt: 600 | 100 | Giá kích hoạt + 500 | Chờ kích hoạt | 19/11/2025 | DBoard |

| Giai đoạn | Mô tả chi tiết |
|-----------|----------------|
| Input | TODO |
| Process | TODO |
| Output | • Lệnh điều kiện được cập nhật trạng thái (ACTIVE, TRIGGERED, EXPIRED).<br>• Một lệnh thường được tạo và gửi vào sàn khi lệnh được kích hoạt.<br>• Thông báo (Notification) cho khách hàng về trạng thái lệnh đã được đẩy lên Sàn. |
