# Các Loại Lệnh Điều Kiện Chứng Khoán Tại Việt Nam

**Ngày nghiên cứu:** 01/12/2025
**Phạm vi:** Giao dịch chứng khoán cơ sở tại thị trường Việt Nam

---

## TÓM TẮT ĐIỀU HÀNH

Công ty chứng khoán tại Việt Nam cần hỗ trợ 3 nhóm lệnh chính cho giao dịch chứng khoán cơ sở:
1. **Lệnh cơ bản** (bắt buộc theo quy định sàn): LO, MP, ATO, ATC, MTL, MOK, MAK, PLO
2. **Lệnh điều kiện nâng cao** (tùy chọn, tăng tính cạnh tranh): TCO, PRO, Stop Loss/Take Profit, Trailing Stop
3. **Lệnh nâng cao đặc biệt** (xu hướng quốc tế): OCO, Bracket Orders, Iceberg Orders

---

## I. LỆNH CƠ BẢN (BẮT BUỘC)

### 1. Lệnh LO (Limit Order - Lệnh Giới Hạn)

**Định nghĩa:** Lệnh mua/bán tại mức giá xác định hoặc tốt hơn.

**Đặc điểm:**
- Chiếm ~95% tổng số lệnh trên thị trường Việt Nam
- Áp dụng cho tất cả các phiên giao dịch (định kỳ, liên tục, sau giờ)
- Sử dụng trên cả 3 sàn: HOSE, HNX, UPCOM

**Cơ chế hoạt động:**
- **Lệnh mua:** Mua tại giá ≤ giá đặt lệnh
- **Lệnh bán:** Bán tại giá ≥ giá đặt lệnh
- Nếu có giá tốt hơn → khớp lệnh tại giá tốt hơn

**Ứng dụng:**
- Kiểm soát giá mua/bán chính xác
- Phù hợp với nhà đầu tư muốn chủ động về giá

**Nguồn:** [ChungKhoanOnline](https://www.chungkhoanonline.com.vn/kien-thuc-kinh-nghiem-chung-khoan-online/cac-loai-lenh-chung-khoan-lo-mp-ato-atc-mtl-mok-mak/)

---

### 2. Lệnh ATO/ATC (At The Opening/Closing)

**Lệnh ATO (At The Opening):**
- Giao dịch tại giá mở cửa
- Phiên định kỳ mở cửa: 9h00-9h15 (HOSE)
- Mua/bán bằng mọi giá trong phiên định kỳ

**Lệnh ATC (At The Closing):**
- Giao dịch tại giá đóng cửa
- Phiên định kỳ đóng cửa: 14h30-14h45 (HOSE, HNX)
- Quan trọng vì tạo giá tham chiếu phiên tiếp theo

**Tỷ trọng:** ~4% tổng số lệnh trên thị trường

**Ứng dụng:**
- Tranh giá mở/đóng cửa
- Tránh biến động trong phiên liên tục
- Định giá cuối ngày cho danh mục

**Nguồn:** [ChungKhoanOnline](https://www.chungkhoanonline.com.vn/kien-thuc-kinh-nghiem-chung-khoan-online/cac-loai-lenh-chung-khoan-lo-mp-ato-atc-mtl-mok-mak/)

---

### 3. Lệnh MP (Market Price - Lệnh Thị Trường - HOSE)

**Định nghĩa:** Lệnh mua/bán tại giá thị trường tốt nhất hiện tại.

**Đặc điểm:**
- Chỉ áp dụng tại sàn HOSE
- Sử dụng trong phiên khớp lệnh liên tục
- Tỷ trọng: ~1% tổng số lệnh

**Cơ chế hoạt động:**
1. Mua/bán tại giá tốt nhất hiện có
2. Nếu còn dư → chuyển thành lệnh LO ± 1 bước giá
3. Ngoại trừ: giá trần/sàn → giữ nguyên giá trần/sàn
4. Không cho phép đặt nếu không có lệnh đối ứng

**Ưu điểm:**
- Khớp lệnh ngay lập tức
- Đảm bảo thanh khoản

**Nhược điểm:**
- Không kiểm soát được giá
- Rủi ro trượt giá cao khi thị trường biến động

**Nguồn:** [ChungKhoanOnline](https://www.chungkhoanonline.com.vn/kien-thuc-kinh-nghiem-chung-khoan-online/cac-loai-lenh-chung-khoan-lo-mp-ato-atc-mtl-mok-mak/)

---

### 4. Lệnh MTL, MOK, MAK (Market Orders - HNX)

Sàn HNX có 3 loại lệnh thị trường thay vì 1 lệnh MP như HOSE:

**MTL (Market To Limit):**
- Sau khi khớp, phần dư → chuyển thành lệnh LO tại giá cuối cùng
- Tương đương MP của HOSE khi ở giá trần/sàn

**MOK (Match Or Kill):**
- Phải khớp toàn bộ khối lượng
- Nếu không đủ đối ứng → hủy toàn bộ lệnh
- Không để lại lệnh dư

**MAK (Match And Kill):**
- Khớp được bao nhiêu thì khớp
- Phần dư → hủy ngay lập tức
- Không chuyển thành lệnh LO

**Tình trạng sử dụng:** Hiếm khi được sử dụng trong thực tế

**Nguồn:** [ChungKhoanOnline](https://www.chungkhoanonline.com.vn/kien-thuc-kinh-nghiem-chung-khoan-online/cac-loai-lenh-chung-khoan-lo-mp-ato-atc-mtl-mok-mak/)

---

### 5. Lệnh PLO (Post Limit Order - Giao Dịch Sau Giờ)

**Định nghĩa:** Lệnh giao dịch tại giá đóng cửa trong phiên sau giờ.

**Đặc điểm:**
- Chỉ áp dụng tại sàn HNX
- Thời gian: 14h45-15h00
- Áp dụng từ ngày 05/11/2018
- Chỉ giao dịch tại giá đóng cửa của ngày

**Ứng dụng:**
- Giao dịch khối lượng lớn sau giờ chính thức
- Tránh tác động giá trong phiên chính

**Nguồn:** [ChungKhoanOnline](https://www.chungkhoanonline.com.vn/kien-thuc-kinh-nghiem-chung-khoan-online/cac-loai-lenh-chung-khoan-lo-mp-ato-atc-mtl-mok-mak/)

---

## II. LỆNH ĐIỀU KIỆN NÂNG CAO (TÙY CHỌN)

Các lệnh điều kiện nâng cao không bắt buộc theo quy định sàn, nhưng được các công ty chứng khoán hàng đầu cung cấp để tăng tính cạnh tranh và phục vụ nhà đầu tư tốt hơn.

### 6. TCO (Time Conditional Order - Lệnh Điều Kiện Thời Gian)

**Định nghĩa:** Lệnh được đặt trước và tự động kích hoạt vào thời điểm đã định.

**Đặc điểm:**
- Đặt lệnh trước nhiều ngày (có thể đến vài tuần)
- Tự động kích hoạt khi đến thời gian thiết lập
- Hiệu lực: theo ngày, tuần, hoặc GTC (Good Till Canceled)

**Ứng dụng:**
- Phù hợp nhà đầu tư bận rộn
- Đầu tư dài hạn theo kế hoạch
- Không cần theo dõi thị trường liên tục

**Nguồn:** [SSI](https://www.ssi.com.vn/en/individual-customer/order-entry-equity-market), [WFS](https://wfs.vn/kien-thuc/cac-loai-lenh-chung-khoan-ato-atc-lo-mp-plo-huong-dan-chi-tiet-danh-cho-nha-dau-tu-f0)

---

### 7. PRO (Priority Order - Lệnh Ưu Tiên)

**Định nghĩa:** Lệnh tranh mua/bán giá ATO, ATC, trần, sàn.

**Ứng dụng:**
- Tranh mua giá trần trong phiên đua
- Tranh bán giá sàn khi cắt lỗ
- Tranh giá mở/đóng cửa với ưu tiên cao

**Nguồn:** [WFS](https://wfs.vn/kien-thuc/cac-loai-lenh-chung-khoan-ato-atc-lo-mp-plo-huong-dan-chi-tiet-danh-cho-nha-dau-tu-f0)

---

### 8. PMO (Pre-Market Order - Lệnh Đặt Trước)

**Định nghĩa:** Lệnh đặt cho phiên giao dịch tiếp theo.

**Đặc điểm:**
- Đặt từ 16h00 của ngày T cho phiên T+1
- Cho phép ATO, ATC, LO (không cho MP, MTL, MOK, MAK)
- Tự động chuyển vào hệ thống lúc 8h30
- Giá trần/sàn ước tính tự động cập nhật

**Ưu điểm so với TCO:**
- Đặt lệnh dễ dàng hơn trên giao diện mua/bán thông thường
- Kiểm tra trạng thái ngay trên màn hình đặt lệnh
- Cập nhật giá trần/sàn tự động

**Ứng dụng:**
- Chuẩn bị lệnh cho ngày hôm sau
- Không bỏ lỡ cơ hội vào đầu phiên

**Nguồn:** [SSI](https://www.ssi.com.vn/en/individual-customer/order-entry-equity-market)

---

### 9. Stop Loss / Take Profit (SL/TP)

**Định nghĩa:** Lệnh tự động chốt lời hoặc cắt lỗ khi giá đạt mức kích hoạt.

**Cơ chế hoạt động:**

**Stop Loss (Cắt lỗ):**
- Đặt giá kích hoạt < giá hiện tại (đối với lệnh bán)
- Khi giá thị trường ≤ giá kích hoạt → lệnh bán được đẩy vào hệ thống
- Giá đặt = Giá thị trường tại thời điểm kích hoạt - Biên độ giá

**Take Profit (Chốt lời):**
- Đặt giá kích hoạt > giá hiện tại (đối với lệnh bán)
- Khi giá thị trường ≥ giá kích hoạt → lệnh bán được đẩy vào hệ thống
- Giá đặt = Giá thị trường tại thời điểm kích hoạt + Biên độ giá

**Tham số:**
- Giá kích hoạt (Trigger Price)
- Biên độ giá (Price Offset)
- Khối lượng

**Ưu điểm:**
- Tự động bảo vệ lợi nhuận
- Hạn chế tổn thất
- Không cần theo dõi liên tục

**Nhược điểm:**
- Có thể bị kích hoạt do biến động ngắn hạn
- Không linh hoạt khi thị trường đảo chiều nhanh

**Công ty triển khai:** VPS, SSI (một số công ty lớn)

**Nguồn:** [Nududo - Hướng dẫn VPS](https://nududo.com/huong-dan-dat-lenh-dieu-kien-vps-stop-loss-take-profit/)

---

### 10. Trailing Stop (TS - Lệnh Dừng Theo Dõi)

**Định nghĩa:** Lệnh stop loss linh hoạt, tự động điều chỉnh giá kích hoạt theo xu hướng có lợi.

**Cơ chế hoạt động:**

**Trailing Stop Bán (Bám theo xu hướng tăng):**
- Khi giá thị trường tăng → giá kích hoạt tăng theo (giữ khoảng cách = biên trượt giá)
- Khi giá thị trường giảm → giá kích hoạt không đổi
- Kích hoạt khi: Giá thị trường ≤ Giá kích hoạt

**Trailing Stop Mua (Bám theo xu hướng giảm):**
- Khi giá thị trường giảm → giá kích hoạt giảm theo (giữ khoảng cách = biên trượt giá)
- Khi giá thị trường tăng → giá kích hoạt không đổi
- Kích hoạt khi: Giá thị trường ≥ Giá kích hoạt

**Tham số:**
- Biên trượt giá (Trailing Amount): Khoảng cách giữa giá thị trường và giá kích hoạt
- Biên độ giá (Price Offset): Khoảng điều chỉnh khi đẩy lệnh vào hệ thống
- Khối lượng

**Ví dụ thực tế:**
```
Mua cổ phiếu ABC tại 100,000đ
Đặt Trailing Stop Bán với biên trượt = 5,000đ

Kịch bản 1: Giá tăng
- Giá lên 110,000đ → Giá kích hoạt = 105,000đ (110k - 5k)
- Giá lên 120,000đ → Giá kích hoạt = 115,000đ (120k - 5k)
- Giá giảm về 115,000đ → Kích hoạt bán → Chốt lời 15,000đ/cp

Kịch bản 2: Giá giảm ngay
- Giá xuống 95,000đ → Giá kích hoạt = 95,000đ (ban đầu)
- Giá xuống 95,000đ → Kích hoạt bán → Cắt lỗ 5,000đ/cp
```

**Ưu điểm:**
- Tự động bảo vệ lợi nhuận khi giá tăng
- Không giới hạn mức lời tối đa
- Linh hoạt theo xu hướng thị trường
- Rất hiệu quả trong thị trường có xu hướng rõ ràng

**Nhược điểm:**
- Dễ bị kích hoạt sớm trong thị trường sideway
- Không phù hợp với cổ phiếu biến động mạnh, không có xu hướng

**Ứng dụng:**
- Bám sát xu hướng tăng/giảm
- Bảo vệ lợi nhuận tự động
- Phù hợp trading ngắn hạn và swing trading

**Công ty triển khai:** VPS, một số công ty chứng khoán hàng đầu

**Nguồn:** [Nududo - Hướng dẫn VPS](https://nududo.com/huong-dan-dat-lenh-dieu-kien-vps-stop-loss-take-profit/)

---

## III. LỆNH NÂNG CAO ĐẶC BIỆT (XU HƯỚNG QUỐC TẾ)

Các loại lệnh này phổ biến tại thị trường quốc tế nhưng chưa được triển khai rộng rãi tại Việt Nam. Tuy nhiên, đây là xu hướng phát triển tương lai.

### 11. OCO (One-Cancels-Other Order)

**Định nghĩa:** Nhóm 2 lệnh, khi 1 lệnh khớp → lệnh còn lại tự động hủy.

**Cơ chế:**
- Đặt đồng thời: Stop Loss và Take Profit
- Khi giá chạm Stop Loss → lệnh Take Profit bị hủy
- Khi giá chạm Take Profit → lệnh Stop Loss bị hủy

**Ví dụ:**
```
Mua ABC tại 100,000đ
OCO Order:
- Take Profit: Bán tại 110,000đ (+10%)
- Stop Loss: Bán tại 95,000đ (-5%)

→ Lệnh nào khớp trước, lệnh kia tự động hủy
```

**Ưu điểm:**
- Quản lý rủi ro tự động 2 chiều
- Đảm bảo tỷ lệ Risk/Reward rõ ràng
- Giảm thao tác thủ công

**Tình trạng tại VN:** Chưa được triển khai chính thức, đang trong nghiên cứu

**Nguồn:** Kinh nghiệm thị trường quốc tế

---

### 12. Bracket Orders (Lệnh Khung)

**Định nghĩa:** Kết hợp 3 lệnh: Entry + Take Profit + Stop Loss.

**Cơ chế:**
- Lệnh vào lệnh (Entry Order)
- Khi Entry khớp → tự động tạo Take Profit và Stop Loss
- OCO giữa Take Profit và Stop Loss

**Ví dụ:**
```
Bracket Order:
- Entry: Mua ABC tại 100,000đ
- Take Profit: Bán tại 110,000đ
- Stop Loss: Bán tại 95,000đ

→ Khi mua được ABC 100k, hệ thống tự tạo 2 lệnh bán OCO
```

**Ưu điểm:**
- Thiết lập đầy đủ kế hoạch giao dịch trong 1 lệnh
- Tự động hóa hoàn toàn
- Phù hợp trading có kỷ luật

**Tình trạng tại VN:** Chưa triển khai

---

### 13. Iceberg Orders (Lệnh Ẩn)

**Định nghĩa:** Lệnh lớn được chia nhỏ, chỉ hiện một phần trên bảng giá.

**Cơ chế:**
- Tổng khối lượng: 100,000 cp
- Hiển thị: 10,000 cp/lần
- Khi 10,000 cp khớp → tự động hiện 10,000 cp tiếp theo

**Ứng dụng:**
- Giao dịch khối lượng lớn không làm ảnh hưởng giá
- Tránh lộ chiến lược với thị trường
- Phù hợp nhà đầu tư tổ chức, quỹ

**Tình trạng tại VN:** Chưa triển khai, cần hạ tầng KRX hoàn thiện hơn

---

## IV. SO SÁNH VÀ PHÂN TÍCH

### Bảng So Sánh Các Loại Lệnh

| Loại Lệnh | Mức Độ | Kiểm Soát Giá | Tốc Độ Khớp | Rủi Ro | Phổ Biến VN |
|-----------|--------|---------------|-------------|--------|-------------|
| **LO** | Cơ bản | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Thấp | 95% |
| **MP/MTL/MAK/MOK** | Cơ bản | ⭐ | ⭐⭐⭐⭐⭐ | Cao | 1% |
| **ATO/ATC** | Cơ bản | ⭐⭐⭐ | ⭐⭐⭐⭐ | Trung bình | 4% |
| **PLO** | Cơ bản | ⭐⭐ | ⭐⭐ | Trung bình | Hiếm |
| **TCO** | Nâng cao | ⭐⭐⭐⭐ | ⭐⭐⭐ | Thấp | Trung bình |
| **PMO** | Nâng cao | ⭐⭐⭐⭐ | ⭐⭐⭐ | Thấp | Cao |
| **Stop Loss/Take Profit** | Nâng cao | ⭐⭐⭐⭐ | ⭐⭐⭐ | Trung bình | Đang tăng |
| **Trailing Stop** | Nâng cao | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Trung bình | Thấp |
| **OCO** | Chuyên sâu | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Thấp | Chưa có |
| **Bracket** | Chuyên sâu | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Thấp | Chưa có |
| **Iceberg** | Chuyên sâu | ⭐⭐⭐ | ⭐⭐⭐⭐ | Thấp | Chưa có |

---

### Phân Tích Theo Nhóm Nhà Đầu Tư

**1. Nhà đầu tư mới/Cá nhân nhỏ lẻ:**
- **Cần:** LO, ATO, ATC
- **Nên có:** PMO, Stop Loss/Take Profit
- **Không cần thiết:** OCO, Bracket, Iceberg

**2. Nhà đầu tư cá nhân tích cực:**
- **Cần:** LO, ATO, ATC, PMO
- **Nên có:** Stop Loss/Take Profit, Trailing Stop, TCO
- **Có thể cần:** OCO

**3. Nhà đầu tư chuyên nghiệp/Quỹ:**
- **Cần:** Tất cả lệnh cơ bản + nâng cao
- **Nên có:** OCO, Bracket Orders
- **Rất cần:** Iceberg Orders cho giao dịch khối lượng lớn

---

## V. YÊU CẦU VÀ KHUYẾN NGHỊ

### Yêu Cầu Bắt Buộc (Theo Quy Định Sàn)

**HOSE:**
- LO (Limit Order)
- MP (Market Price)
- ATO (At The Opening)
- ATC (At The Closing)

**HNX:**
- LO (Limit Order)
- MTL, MOK, MAK (Market Orders)
- ATO (At The Opening)
- ATC (At The Closing)
- PLO (Post Limit Order - Sau giờ)

**UPCOM:**
- LO (Limit Order)
- ATO, ATC (theo quy định HNX)

---

### Khuyến Nghị Để Tăng Tính Cạnh Tranh

**Mức 1 - Cơ Bản (Bắt Buộc Cạnh Tranh):**
1. PMO (Pre-Market Order) - Đặt lệnh trước cho phiên sau
2. TCO (Time Conditional Order) - Lệnh theo thời gian

**Mức 2 - Nâng Cao (Tăng Lợi Thế):**
3. Stop Loss / Take Profit - Quản lý rủi ro tự động
4. Trailing Stop - Bám theo xu hướng
5. PRO (Priority Order) - Tranh giá ưu tiên

**Mức 3 - Chuyên Nghiệp (Dẫn Đầu Thị Trường):**
6. OCO (One-Cancels-Other)
7. Bracket Orders
8. Iceberg Orders (cần hạ tầng KRX mạnh)

---

### Lộ Trình Triển Khai Đề Xuất

**Giai đoạn 1 (0-6 tháng): Lệnh Cơ Bản + PMO**
- Hoàn thiện tất cả lệnh cơ bản theo quy định sàn
- Triển khai PMO (Pre-Market Order)
- Đảm bảo tích hợp với hệ thống KRX

**Giai đoạn 2 (6-12 tháng): Lệnh Điều Kiện Nâng Cao**
- Triển khai Stop Loss / Take Profit
- Triển khai Trailing Stop
- Triển khai TCO (Time Conditional Order)
- Nâng cấp hệ thống giám sát và kích hoạt lệnh

**Giai đoạn 3 (12-24 tháng): Lệnh Chuyên Nghiệp**
- Nghiên cứu triển khai OCO
- Nghiên cứu triển khai Bracket Orders
- Đánh giá khả năng triển khai Iceberg Orders
- Phối hợp với SSC và sàn giao dịch về quy định

---

## VI. THAM KHẢO QUỐC TẾ

### So Sánh Với Thị Trường Phát Triển

**NYSE/NASDAQ (Mỹ):**
- Có đầy đủ: Stop, Stop-Limit, Trailing Stop, OCO, Bracket, Iceberg
- Algo trading và advanced orders rất phổ biến
- Quy định chặt chẽ về công bố lệnh lớn

**SGX (Singapore):**
- Có Stop, Stop-Limit, OCO
- Iceberg Orders cho nhà đầu tư tổ chức
- Tích hợp tốt với các nền tảng quốc tế

**Bài học cho Việt Nam:**
- Cần lộ trình rõ ràng từ cơ bản → nâng cao
- Giáo dục nhà đầu tư song song với triển khai công nghệ
- Quy định minh bạch về từng loại lệnh
- Đảm bảo hạ tầng công nghệ đủ mạnh

---

## VII. KẾT LUẬN

### Tóm Tắt

Công ty chứng khoán tại Việt Nam cần hỗ trợ 3 cấp độ lệnh:

1. **Lệnh Cơ Bản (Bắt buộc):** 8 loại
   - LO, MP, ATO, ATC, MTL, MOK, MAK, PLO

2. **Lệnh Nâng Cao (Tăng cạnh tranh):** 5 loại
   - PMO, TCO, PRO, Stop Loss/Take Profit, Trailing Stop

3. **Lệnh Chuyên Nghiệp (Dẫn đầu):** 3 loại
   - OCO, Bracket Orders, Iceberg Orders

### Ưu Tiên Triển Khai

**Ngay lập tức:**
- Đảm bảo tất cả lệnh cơ bản hoạt động tốt trên hệ thống KRX
- Triển khai PMO (Pre-Market Order)

**Trong 6-12 tháng tới:**
- Stop Loss / Take Profit
- Trailing Stop
- TCO (Time Conditional Order)

**Dài hạn (1-2 năm):**
- OCO, Bracket Orders
- Nghiên cứu Iceberg Orders

### Lưu Ý Quan Trọng

1. **Công nghệ:** Cần hệ thống giám sát giá và kích hoạt lệnh realtime
2. **Quy định:** Tuân thủ quy định SSC và sàn giao dịch
3. **Giáo dục:** Đào tạo nhà đầu tư sử dụng đúng cách
4. **Quản lý rủi ro:** Thiết lập giới hạn, cảnh báo rủi ro
5. **Hạ tầng:** Đảm bảo hệ thống KRX đủ mạnh để xử lý

---

## NGUỒN THAM KHẢO

1. **ChungKhoanOnline.com** - Các loại Lệnh Đặt trong Chứng khoán LO, MP, ATO, ATC, MTL, MOK, MAK, PLO
   https://www.chungkhoanonline.com.vn/kien-thuc-kinh-nghiem-chung-khoan-online/cac-loai-lenh-chung-khoan-lo-mp-ato-atc-mtl-mok-mak/

2. **SSI** - Order Entry (Equity Market)
   https://www.ssi.com.vn/en/individual-customer/order-entry-equity-market

3. **ChungKhoanVPS.org** - Đặt Lệnh Chứng Khoán: Các Loại Lệnh, Cách Đặt & Thời Điểm
   https://chungkhoanvps.org/kien-thuc/dat-lenh-chung-khoan/

4. **Nududo.com** - Hướng dẫn đặt lệnh điều kiện VPS Stop Loss / Take Profit
   https://nududo.com/huong-dan-dat-lenh-dieu-kien-vps-stop-loss-take-profit/

5. **WFS** - Các loại lệnh chứng khoán: ATO, ATC, LO, MP, PLO
   https://wfs.vn/kien-thuc/cac-loai-lenh-chung-khoan-ato-atc-lo-mp-plo-huong-dan-chi-tiet-danh-cho-nha-dau-tu-f0

6. **Bartra Wealth Advisors** - Tổng Quan Về Thuật Ngữ Đầu Tư Chứng Khoán Cơ Bản
   https://bartrawealthadvisors.com.vn/tong-quan-ve-thuat-ngu-dau-tu-chung-khoan-co-ban/

7. **VietnamBiz** - Bảng xếp hạng dịch vụ bán lẻ tốt nhất thị trường chứng khoán Việt Nam (Best Retail Brokers 2025)
   https://vietnambiz.vn/chinh-thuc-cong-bo-bang-xep-hang-dich-vu-ban-le-tot-nhat-thi-truong-chung-khoan-viet-nam-best-retail-brokers-2025-2025114144754108.htm

---

**Ghi chú:** Nghiên cứu này dựa trên thông tin công khai từ các công ty chứng khoán, sàn giao dịch và các nguồn tin cậy tại Việt Nam. Quy định có thể thay đổi theo thời gian và cần cập nhật định kỳ.
