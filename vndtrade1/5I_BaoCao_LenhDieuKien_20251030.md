## IDENTIFY - 5I Framework
### SOC: Trao quyền cho Nhà đầu tư (Empowering Traders)
### OC: Xây dựng bộ lệnh điều kiện chứng khoán cơ sở #1 thị trường

---

## Tóm Tắt Tổng Quan

VNDIRECT hướng tới mục tiêu xây dựng **hệ thống lệnh điều kiện số 1** trên thị trường chứng khoán Việt Nam trong vòng 3 tháng. Sáng kiến này sẽ chuyển đổi VNDIRECT từ việc có khả năng lệnh điều kiện cơ bản (~3 loại lệnh, hiệu lực trong ngày) sang nền tảng dẫn đầu thị trường với:

- **15+ loại lệnh điều kiện** (so với 10+ của SSI, 8 của TCBS)
- **Hiệu lực 30 ngày** (ngang bằng TCBS)
- **API công khai**
- **UX tốt nhất thị trường** với công cụ tạo lệnh trực quan và tài liệu hướng dẫn

**Yếu Tố Thành Công Chính:**
1. Kiến trúc hiện đại cho khả năng mở rộng (microservice) kết hợp hiệu suất (core monolith)
2. Giáo dục người dùng toàn diện (HDSD, hướng dẫn, mô phỏng)
3. Cân bằng chiến lược giữa tính năng phong phú và dễ sử dụng
4. API công khai để thu hút traders sử dụng thuật toán
5. Khung tuân thủ và quản lý rủi ro mạnh mẽ

**Kết Quả Kỳ Vọng:**
- **Khách hàng**: Tỷ lệ sử dụng 30%+, công cụ chuyên nghiệp cho nhà đầu tư cá nhân
- **Kinh doanh**: Tăng độ giữ chân/gắn kết khách hàng, xây dựng lợi thế cạnh tranh, định vị công nghệ
- **Doanh thu**: Tăng 15-20% từ hoạt động giao dịch cao hơn

**Đầu Tư Yêu Cầu:** Công nghệ hiện đại, chu kỳ phát triển 3 tháng, đội ngũ full-stack

**Rủi Ro:** Thách thức về tỷ lệ sử dụng (Trung bình), ràng buộc thời gian (Trung bình)

---

## 1. INTENTION - Mục Đích & Tầm Nhìn

### 1.1 Tại Sao Cần Thay Đổi?

**Tình Hình Hiện Tại:**
- VNDIRECT có ~3 loại lệnh điều kiện chứng khoán cơ sở (Conditional Stop/TP Order, GTD)
- Hiệu lực trong ngày (trừ GTD) hạn chế cho chiến lược nhiều ngày
- Đang mất lợi thế cạnh tranh trước SSI (10+ loại lệnh) và TCBS (hiệu lực 30 ngày)

**Pain Points:**
- Traders cần nhiều loại lệnh phức tạp hơn cho chiến lược nâng cao
- Hiệu lực trong ngày yêu cầu gia hạn thủ công hàng ngày (bất tiện)
- Nhà đầu tư cá nhân thiếu quyền truy cập công cụ giao dịch thuật toán chuyên nghiệp
- Vị thế công nghệ của VNDIRECT đang có rủi ro

**Yêu Cầu Chiến Lược:**
- "Trao quyền cho Nhà đầu tư" đòi hỏi cung cấp công cụ cấp chuyên nghiệp
- Thị trường yêu cầu bắt kịp và vượt qua đối thủ cạnh tranh
- Xây dựng lợi thế cạnh tranh thông qua khác biệt hóa công nghệ

### 1.2 Mục Tiêu Cuối Cùng

**Tuyên Bố Tầm Nhìn:**
"Xây dựng hệ thống lệnh điều kiện toàn diện, thân thiện người dùng và mạnh mẽ nhất Việt Nam, trao quyền cho cả nhà đầu tư cá nhân và chuyên nghiệp với công cụ tự động hóa cấp tổ chức."

**"Số 1 Thị Trường" Được Định Nghĩa Bởi 4 Trụ Cột:**

1. **Tính Đầy Đủ Tính Năng** - Nhiều loại lệnh điều kiện nhất (15+ so với 10 của đối thủ)
2. **Tính Tiện Dụng & Linh Hoạt** - Dễ dàng cho người mới, mạnh mẽ cho chuyên gia
3. **Xuất Sắc Về UX** - UI/UX trực quan, công cụ tạo lệnh trực quan
4. **Giáo Dục** - HDSD toàn diện với hướng dẫn, video, mô phỏng

### 1.3 Tiêu Chí Thành Công

| Tiêu Chí | Hiện Tại | Mục Tiêu (3 tháng) | Mục Tiêu Cao | Phương Pháp Đo Lường |
|----------|----------|-------------------|--------------|---------------------|
| **Số loại lệnh điều kiện** | ~5 loại | 12-15 loại | 20+ loại | Đếm tính năng |
| **% KH sử dụng lệnh ĐK** | ~10-15% (ước tính) | 30% | 40% | KH có lệnh active / Tổng KH active |
| **Số lệnh ĐK active/ngày** | ~1,000-2,000 (ước tính) | 15,000 | 25,000 | Lệnh điều kiện active hàng ngày |
| **Số lệnh triggered/ngày** | Chưa rõ | 5,000 | 10,000 | Số lượng thực thi hàng ngày |
| **Độ trễ thực thi lệnh** | Chưa rõ | <50ms | <20ms | Độ trễ phân vị 95 |
| **Tỷ lệ thành công thực thi** | Chưa rõ | 99.5% | 99.9% | Thực thi thành công / Tổng kích hoạt |
| **Hài lòng khách hàng (CSAT)** | Chưa rõ | 4.5/5 | 4.7/5 | Khảo sát sau thực thi |
| **Hiệu lực lệnh** | Trong ngày | 30 ngày | 90 ngày | Thời gian hiệu lực tối đa |

**Lưu ý:** Cần thu thập số liệu baseline từ hệ thống hiện tại.

### 1.4 Kết Quả Kỳ Vọng

#### **Kết Quả Khách Hàng** - "Trao Quyền Cho Nhà Đầu Tư"

**Tự Động Hóa & Tự Do:**
- Giao dịch "đặt và quên" (không cần theo dõi màn hình cả ngày)
- Khả năng đặt lệnh 24/7
- Chiến lược nhiều ngày không cần gia hạn hàng ngày

**Quản Lý Rủi Ro Xuất Sắc:**
- Cắt lỗ tự động để bảo vệ vốn
- Chốt lời tự động để khóa lợi nhuận
- Lệnh OCO (một hủy cái kia) cho cân bằng rủi ro/lợi nhuận
- Trailing stop để bảo vệ lợi nhuận trong khi theo xu hướng

**Chiến Lược Nâng Cao:**
- Lệnh Bracket (vào lệnh + stop + mục tiêu trong một lệnh)
- Giao dịch phá vỡ với lệnh Up/Down
- Theo xu hướng với trailing stop động
- Chiến lược nhiều chặng qua chuỗi điều kiện

**Kiểm Soát Cảm Xúc:**
- Loại bỏ cảm xúc khỏi quyết định giao dịch
- Thực thi kỷ luật thông qua lệnh lập kế hoạch trước
- Giảm FOMO và giao dịch hoảng loạn

**Hiệu Quả Thời Gian:**
- Tiết kiệm hàng giờ theo dõi màn hình
- Cân bằng công việc-cuộc sống tốt hơn cho trader bán thời gian
- Thiết lập lệnh nhanh với mẫu có sẵn

**Công Cụ Chuyên Nghiệp Cho Mọi Người:**
- San bằng sân chơi (nhà đầu tư cá nhân tiếp cận công cụ chuyên nghiệp)
- Học chiến lược nâng cao qua giáo dục
- Khả năng backtesting (tương lai)

#### **Kết Quả Kinh Doanh**

1. **Tăng Độ Giữ Chân & Gắn Kết**
   - Tính năng dính (khó chuyển sang đối thủ)
   - Tần suất giao dịch cao hơn từ người dùng tích cực

2. **Xây Dựng Lợi Thế Cạnh Tranh**
   - Khác biệt rõ ràng vs. SSI, TCBS, VPS
   - Thu hút traders từ đối thủ
   - Lợi thế người đi trước trong một số tính năng

3. **Khẳng Định Vị Thế Công Nghệ**
   - Định vị là công ty chứng khoán "hướng công nghệ"
   - API hiện đại thu hút algo traders
   - Hình ảnh thương hiệu: Innovation leader

**Chỉ Số Kinh Doanh Đo Lường Được:**
- Khối lượng giao dịch qua lệnh điều kiện: **20-30% tổng khối lượng**
- Thu hút khách hàng: **+10% thị phần**
- Doanh thu môi giới: **+15-20%** từ hoạt động tăng cao
- Cải thiện NPS: **+10 điểm**

### 1.5 Bối Cảnh Cạnh Tranh

**Bức Tranh Thị Trường:**

| Công ty CK | Loại Lệnh | Hiệu Lực | API | Điểm Mạnh | Điểm Yếu |
|-----------|-----------|----------|-----|-----------|----------|
| **SSI** | 10+ (cổ phiếu + phái sinh) | 1 ngày | API công khai | Nhiều tính năng, phái sinh | Kiểm tra theo lịch, UI phức tạp |
| **TCBS** | ~8 loại | 30 ngày | Hạn chế/tổ chức | Hiệu lực dài, 24/7 | Ít loại hơn, không có phái sinh |
| **VPS** | 4 loại cơ bản | 1 ngày | Không có API công khai | Đơn giản, rõ ràng | Đa dạng hạn chế |
| **VNDIRECT (Hiện tại)** | ~5 loại | Trong ngày | API công khai nhưng không chính thức public | 24/7, mobile, tích hợp TA | Loại hạn chế, hiệu lực ngắn |

**Khoảng Trống Cạnh Tranh Cần Khai Thác:**
- **vs. SSI**: UX tốt hơn, giám sát thời gian thực, hiệu lực dài hơn
- **vs. TCBS**: Nhiều loại lệnh hơn + giữ hiệu lực dài
- **vs. VPS**: Nhiều tính năng hơn trong khi duy trì sự đơn giản

**Vị Trí Mục Tiêu:**
"Hệ thống lệnh điều kiện toàn diện nhất với UX và giáo dục tốt nhất"

---

## 2. INTERCONNECT - Các Bên Liên Quan & Mối Quan Hệ

### 2.1 Ma Trận Các Bên Liên Quan

| Bên Liên Quan | Vai Trò | Mức Quan Tâm | Mức Ảnh Hưởng | Chiến Lược Gắn Kết |
|---------------|---------|--------------|---------------|-------------------|
| **Business Owner** | Định hướng chiến lược | Cao | Rất Cao | Hội đồng điều hành hàng tháng |
| **Product Management** | Tầm nhìn sản phẩm | Rất Cao | Cao | Cộng tác hàng ngày |
| **Technical Product Owner** | Cầu nối kinh doanh-kỹ thuật | Rất Cao | Cao | Tham gia hàng ngày |
| **DTO** | Kiến trúc & thực thi | Rất Cao | Cao | Hàng ngày |
| **IPAS - Hạ Tầng** | Nền tảng & APIs | Cao | Cao | Đồng bộ hàng tuần |
| **Tuân Thủ/Pháp Lý** | Phê duyệt quy định | Cao | Cao | Xem xét hàng tháng |
| **Quản Lý Rủi Ro** | Kiểm soát rủi ro | Cao | Cao | Xem xét khung rủi ro |
| **Thiết Kế UX/UI** | Trải nghiệm người dùng | Cao | Trung Bình | Sprint thiết kế |
| **Nhóm QA/Kiểm Thử** | Đảm bảo chất lượng | Cao | Trung Bình | Lập kế hoạch kiểm thử |
| **DevOps/SRE** | Độ tin cậy hệ thống | Cao | Trung Bình | Thiết lập CI/CD |
| **Hỗ Trợ Khách Hàng** | Hỗ trợ người dùng | Trung Bình | Thấp | Buổi đào tạo |
| **Marketing** | Quảng bá ra mắt | Trung Bình | Trung Bình | Lập kế hoạch chiến dịch |

### 2.2 Các Phụ Thuộc Chính

**Phụ Thuộc Kỹ Thuật:**
- Hệ thống core lệnh
- BoAPI - check permission & các thông tin giao dịch trong BO@
- Nguồn giá thời gian thực - độ trễ thấp quan trọng cho thực thi => Kafka (FINFO)
- APIs của FINFO

**Phụ Thuộc Thời Gian:**
- Tháng 1: Kiến trúc + Backend + Tích hợp bảng giá lệnh đơn giản
- Tháng 2-Tháng 3: Rollout dần các lệnh advance, thay thế các service lệnh điều kiện cũ

### 2.3 Ma Trận RACI

TODO

**Chú thích:** R=Chịu trách nhiệm, A=Phê duyệt, C=Tham vấn, I=Thông báo

---

## 3. INSIGHT - Dữ Liệu & Phân Tích

### 3.1 Phân Tích Tình Trạng Hiện Tại

**Khả Năng Hiện Tại Của VNDIRECT:**
- ~3 loại lệnh điều kiện
- Hiệu lực trong ngày (tự động đóng)
- Đặt lệnh 24/7
- Đa nền tảng (Web + Mobile qua DBOARD)
- Tích hợp phân tích kỹ thuật
- Lệnh một cú nhấp

**Khoảng Trống So Với Dẫn Đầu Thị Trường:**
- Ít loại lệnh hơn (3 vs. 10+ của SSI)
- Hiệu lực ngắn hơn (trong ngày vs. 30 ngày của TCBS)
- Không có Open API công khai (vs. SSI)
- Thiếu loại nâng cao: OCO, Bracket, Bull&Bear

**Số Liệu Baseline (Cần Thu Thập):**
- Lệnh điều kiện hàng ngày hiện tại: ~1,000-2,000 (ước tính)
- Tỷ lệ sử dụng người dùng: ~10-15% (ước tính)
- Độ trễ thực thi: Chưa rõ
- Tỷ lệ thành công: Chưa rõ

### 3.2 Phân Tích Nguyên Nhân Gốc

**Tại Sao Chưa Là #1?**

1. **Bộ Tính Năng Hạn Chế** → Ít loại lệnh
2. **Thời Hạn Hiệu Lực Ngắn** → Chỉ trong ngày là bất tiện
3. **Không Có Open API Công Khai** → Không thể thu hút algo/quant traders
5. **Ràng Buộc Hệ Thống Cũ** → Giới hạn hiệu suất và khả năng mở rộng

### 3.3 Thông Tin Khách Hàng

**Phân Loại Trader:**

**1. Nhà Đầu Tư Cá Nhân Thông Thường**
- Làm toàn thời gian, giao dịch bán thời gian
- Cần: Cắt lỗ/chốt lời đơn giản, UI rõ ràng, hướng dẫn tốt
- Loại lệnh: TCO, Stop Loss, Take Profit

**2. Nhà Đầu Tư Cá Nhân Tích Cực**
- Giao dịch thường xuyên, kiến thức trung cấp
- Cần: Trailing stop, hiệu lực nhiều ngày, mobile-first
- Loại lệnh: Tất cả cơ bản + Trailing Stop, OCO

**3. Trader Chuyên Nghiệp/Thuật Toán**
- Giao dịch toàn thời gian, sử dụng thuật toán
- Cần: API công khai, loại lệnh nâng cao, độ trễ thấp
- Loại lệnh: Tất cả bao gồm Bracket, chuỗi

**Pain Points:**
- Gia hạn lệnh hàng ngày là tẻ nhạt (hiệu lực trong ngày)
- Loại lệnh hạn chế vs. đối thủ
- Không có Open API (công khai) cho giao dịch tự động
- UI phức tạp cho người mới

### 3.4 Chuẩn Mực Ngành

**Thực Hành Tốt Nhất Toàn Cầu:**
- **Interactive Brokers**: 50+ loại lệnh, GTC chuẩn, API công khai
- **Charles Schwab**: Công cụ tạo lệnh trực quan, giáo dục rộng rãi
- **Tiger Brokers (Châu Á)**: Đa thị trường, <50ms độ trễ, API công khai

**Bài Học Chính:**
1. Giáo dục là then chốt (video, mô phỏng)
2. Mobile-first cho nhà đầu tư cá nhân
3. API-first cho algo traders
4. Công cụ trực quan đơn giản hóa độ phức tạp
5. GTC (hiệu lực nhiều ngày) là chuẩn

---

## 4. INNOVATION - Giải Pháp & Cách Tiếp Cận

### 4.1 Các Phương Án Giải Pháp

TODO

### 4.2 Công Nghệ Đề Xuất

**Backend:**
- Java/Spring Boot
- Apache Kafka cho event streaming
- Redis cho caching
- PostgreSQL cho trạng thái lệnh

**Hạ Tầng:**
- Giám sát Prometheus + Grafana
- Tự động hóa CI/CD

### 4.3 Lộ Trình Loại Lệnh

TODO 

**Giai Đoạn 1: Cốt Lõi (Tháng 1-2)** - BẮT BUỘC PHẢI CÓ
1. Lệnh Cắt Lỗ (Stop Loss)
2. Lệnh Chốt Lời (Take Profit)
3. Lệnh Theo Thời Gian (TCO)
4. Lệnh Trailing Stop

**Giai Đoạn 2: Nâng Cao (Tháng 3)** - LỢI THẾ CẠNH TRANH
5. OCO (Một Hủy Cái Kia)
6. Lệnh Bracket
7. Chuỗi Điều Kiện

**Giai Đoạn 3: Chuyên Nghiệp (Tháng 4+)** - KHÁC BIỆT HÓA
8. Lệnh kích hoạt bởi TA (RSI, MACD)
9. Lệnh cấp danh mục
10. Trailing nâng cao (dựa trên ATR)

### 4.4 Đổi Mới Dài Hạn (6-12 tháng)

**Tính Năng AI/ML:**
- Gợi ý giá chốt lời, cắt lỗ thông minh dựa trên các đường kháng cự, hỗ trợ
- Cảnh báo kích hoạt dự đoán
- Backtesting chiến lược

**Tính Năng Xã Hội:**
- Chợ chiến lược
- Copy trading
- Chiến lược chuyên gia

**Hệ Sinh Thái Developer:**
- API công khai + SDK (Python, JS, Java)
- Hỗ trợ webhook
- Nền tảng algo trading

---

## 5. INTEGRITY - Giá Trị & Đạo Đức

### 5.1 Căn Chỉnh Giá Trị Công Ty

**Khách Hàng Là Trên Hết:** ✅ Công cụ chuyên nghiệp cho mọi trader
**Đổi Mới:** ✅ Kiến trúc hiện đại, API công khai
**Chính Trực:** ✅ Thực thi minh bạch, audit trail
**Xuất Sắc:** ✅ Tiêu chuẩn chất lượng "#1 thị trường"

### 5.2 Cân Nhắc Đạo Đức

**Bảo Vệ Trader:**
- Cảnh báo rủi ro rõ ràng trước khi đặt lệnh
- Hộp thoại xác nhận cho lệnh rủi ro cao
- Xem trước lệnh: "Lệnh của bạn sẽ kích hoạt khi..."
- Pop-up giáo dục cho người dùng lần đầu

**Ngăn Chặn Thao Túng Thị Trường:**
- Giới hạn kích thước lệnh
- Giới hạn tốc độ
- Phát hiện mẫu đáng ngờ
- Giám sát tuân thủ

**Công Bằng:**
- Tính năng ngang nhau giữa UI và API
- Giới hạn tốc độ bằng nhau cho tất cả người dùng
- Không có tính năng cao cấp tạo lợi thế không công bằng
- Giáo dục để san bằng sân chơi

### 5.3 Danh Sách Kiểm Tra Tuân Thủ

**Quy Định (SSC):**
- [ ] Xác nhận phê duyệt loại lệnh
- [ ] Công bố rủi ro bằng tiếng Việt
- [ ] Cập nhật Điều khoản & Điều kiện
- [ ] Audit trail đầy đủ
- [ ] Giám sát thao túng
- [ ] Khả năng báo cáo

**Sàn Giao Dịch (HOSE/HNX):**
- [ ] Tuân thủ API
- [ ] Tôn trọng giới hạn tốc độ
- [ ] Chỉ loại lệnh được hỗ trợ
- [ ] Tôn trọng giờ giao dịch

**Kiểm Soát Rủi Ro Nội Bộ:**
- [ ] Giới hạn vị thế mỗi người dùng
- [ ] Giới hạn lỗ hàng ngày
- [ ] Giới hạn tập trung
- [ ] Nút dừng khẩn cấp

### 5.4 Tính Bền Vững

**Kỹ Thuật:**
- Mở rộng đến 10x tăng trưởng
- Mở rộng đàn hồi cloud-native
- Kiểm thử toàn diện
- Kiểm toán bảo mật

**Kinh Doanh:**
- Cùng phí môi giới (không tăng giá)
- Doanh thu từ khối lượng tăng
- Hiệu ứng mạng tạo lợi thế

**Xã Hội:**
- Bao trùm tài chính (công cụ chuyên nghiệp cho cá nhân)
- Dân chủ hóa giáo dục
- Cải thiện hiệu quả thị trường

---

## Phân Tích TAC

### TRANSFORM - Thay Đổi Hoàn Toàn

| Lĩnh Vực | Hiện Tại | Mục Tiêu | Thời Gian |
|----------|----------|----------|-----------|
| **Loại Lệnh** | 5 loại | 15+ loại | 3 tháng |
| **Hiệu Lực** | Trong ngày | 30 ngày | 2 tháng |
| **API** | Chỉ tổ chức | Công khai + docs + SDK | 3 tháng |
| **Giám Sát** | Batch/theo lịch | Thời gian thực | 2 tháng |
| **Giáo Dục** | Tối thiểu | HDSD toàn diện + video | Liên tục |
| **UI/UX** | Form cơ bản | Trực quan + mẫu | 3 tháng |

### AMPLIFY - Phát Huy Điểm Mạnh

| Điểm Mạnh | Hiện Tại | Phát Huy Đến |
|-----------|----------|--------------|
| **Đặt Lệnh 24/7** | Cơ bản | Xem lịch, lập lịch |
| **Đa Nền Tảng** | Tốt | UX mobile xuất sắc, thông báo |
| **Tích Hợp TA** | Đã tích hợp | Lệnh kích hoạt bởi TA |
| **Lệnh Một Cú Nhấp** | Có sẵn | Mẫu cho lệnh điều kiện |
| **Trải Nghiệm Mobile** | Mạnh | Dẫn đầu ngành |
| **Hỗ Trợ** | Tốt | Đội chuyên biệt lệnh điều kiện |

### CONTINUE - Giữ Nguyên

| Yếu Tố | Tại Sao Giữ Nguyên |
|--------|-------------------|
| **Cấu Trúc Phí Không Đổi** | Công bằng, không tăng giá |
| **Nền Tảng Tích Hợp** | Trải nghiệm thống nhất |
| **Tuân Thủ Quy Định** | Thiết yếu cho hoạt động |
| **Văn Hóa Khách Hàng Trên Hết** | Giá trị cốt lõi |
| **Tiêu Chuẩn Bảo Mật** | Thiết yếu cho niềm tin |

---

## RỦI RO & GIẢM THIỂU

### Rủi Ro Kỹ Thuật Hàng Đầu

| Rủi Ro | Khả Năng | Tác Động | Giảm Thiểu |
|--------|----------|----------|------------|
| **Độ trễ cao (>100ms)** | Trung bình | Cao | Kiểm thử tải, caching, tối ưu hóa |
| **Ngừng hoạt động hệ thống** | Thấp | Nghiêm trọng | Tự động mở rộng, circuit breaker |
| **Giới hạn tốc độ sàn** | Trung bình | Cao | Gom yêu cầu, điều tiết |
| **Vấn đề tích hợp OMS** | Cao | Cao | Kiểm thử toàn diện, dự phòng |
| **Vi phạm bảo mật** | Thấp | Nghiêm trọng | MFA, xoay khóa, giám sát |

### Rủi Ro Kinh Doanh Hàng Đầu

| Rủi Ro | Khả Năng | Tác Động | Giảm Thiểu |
|--------|----------|----------|------------|
| **Sử dụng thấp (<20%)** | Trung bình | Cao | Giáo dục, khuyến khích, UX |
| **Đối thủ ra mắt tốt hơn** | Trung bình | Cao | Lặp nhanh, đổi mới |
| **Người dùng mất tiền** | Cao | Cao | Cảnh báo, xem trước, giáo dục |
| **Hỗ trợ quá tải** | Cao | Trung bình | HDSD, chatbot, đào tạo |
| **Chậm tiến độ** | Trung bình | Trung bình | Đệm, ưu tiên |

---
