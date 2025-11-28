# Bảng Phân Tích Giá Chứng Quyền - Tài liệu Yêu cầu Nghiệp vụ (BRD)

---

## QUẢN LÝ TÀI LIỆU

| Thông tin | Chi tiết |
|-----------|----------|
| **Tên tài liệu** | Business Requirements Document - Bảng Phân Tích Giá Chứng Quyền |
| **Phiên bản** | 1.0 |
| **Ngày tạo** | 28/11/2025 |
| **Người tạo** | Business Analyst |
| **Người phê duyệt** | Product Owner |
| **Trạng thái** | Draft |

### Lịch sử phiên bản

| Phiên bản | Ngày | Người thay đổi | Mô tả thay đổi |
|-----------|------|----------------|----------------|
| 1.0 | 28/11/2025 | BA Team | Phiên bản khởi tạo - Tích hợp bảng giá CW với chỉ số phân tích chuyên sâu |

### Danh sách phân phối

| Vai trò | Phạm vi trách nhiệm |
|---------|---------------------|
| Product Owner | Phê duyệt yêu cầu nghiệp vụ và ưu tiên phát triển |
| Business Analyst | Phân tích và viết tài liệu yêu cầu |
| Tech Lead | Đánh giá tính khả thi kỹ thuật và thiết kế kiến trúc |
| QA Lead | Xây dựng test plan và acceptance criteria |
| Quant Team | Review công thức định giá và tính toán Greeks |
| Marketing Team | Chuẩn bị kế hoạch truyền thông khi ra mắt tính năng |

---

## TÓM TẮT ĐIỀU HÀNH

VNDIRECT đang phát triển **Bảng Phân Tích Giá Chứng Quyền** tích hợp 7-9 chỉ số kỹ thuật chuyên sâu nhằm thu hẹp khoảng cách với đối thủ cạnh tranh (TCBS, VPBankS) và hỗ trợ đợt phát hành CW mới dự kiến tháng 09/2025. Hiện tại bảng giá CW của VNDIRECT chỉ hiển thị thông tin giao dịch cơ bản (giá, khối lượng), hoàn toàn thiếu các chỉ số định giá quan trọng như Giá lý thuyết (Black-Scholes), Implied Volatility, Greeks (Delta, Theta, Vega), điểm hòa vốn, và đòn bẩy hiệu dụng. Điều này khiến nhà đầu tư không thể đánh giá CW đắt/rẻ, buộc phải sử dụng công cụ bên ngoài, tạo rào cản giao dịch.

Tính năng mới bao gồm: (1) Nâng cấp bảng giá CW với 7-9 chỉ số phân tích tự động tính toán; (2) Bổ sung tab "Chứng quyền liên quan" trên trang Sức khỏe Cổ phiếu để kết nối CKCS và CW. Mục tiêu: tăng khả năng cạnh tranh, giảm rào cản ra quyết định, hỗ trợ marketing CW mới, tăng khối lượng giao dịch và thu phí. Đối tượng thưởng lợi: nhà đầu tư Retail (cần bộ chỉ số rút gọn, dễ hiểu) và nhà đầu tư chuyên nghiệp (cần full bộ Greeks để tối ưu vốn).

---

## 1. GIỚI THIỆU

### 1.1 Mục đích tài liệu

Tài liệu này mô tả chi tiết các yêu cầu nghiệp vụ cho tính năng **Bảng Phân Tích Giá Chứng Quyền** tích hợp trên nền tảng DBoard của VNDIRECT. Tài liệu được sử dụng bởi các nhóm phát triển (Dev, Quant, Data), kiểm thử (QA), và vận hành để:

- Hiểu rõ yêu cầu nghiệp vụ và giá trị kinh doanh
- Thiết kế và triển khai chính xác các chỉ số phân tích chứng quyền
- Đảm bảo độ chính xác của mô hình định giá Black-Scholes và tính toán Greeks
- Xây dựng test case và acceptance criteria phù hợp
- Chuẩn bị kế hoạch triển khai và truyền thông

### 1.2 Phạm vi

**Trong phạm vi (In Scope):**

- Nâng cấp bảng giá Chứng quyền trên DBoard với 7-9 chỉ số kỹ thuật:
  - Giá lý thuyết (Black-Scholes)
  - Chênh lệch giá lý thuyết
  - Điểm hòa vốn
  - Đòn bẩy hiệu dụng
  - Implied Volatility (IV)
  - Delta, Theta, Vega
  - Time to Maturity (TTM)
- Tính toán tự động các chỉ số dựa trên dữ liệu real-time
- Bổ sung tab "Chứng quyền liên quan" trên trang Sức khỏe Cổ phiếu
- Tooltip giáo dục cho từng chỉ số để hỗ trợ nhà đầu tư Retail
- Export dữ liệu bảng giá CW ra Excel

**Ngoài phạm vi (Out of Scope):**

- Chức năng backtest chiến lược giao dịch CW
- Tính năng alert/notification khi CW đạt điều kiện định giá
- Công cụ so sánh tự động nhiều mã CW (sẽ triển khai phase 2)
- Tính toán Gamma và Rho (ít sử dụng trong thực tế)
- Quản lý danh mục và báo cáo P&L cho CW
- Tính năng mô phỏng kịch bản (scenario analysis)

### 1.3 Định nghĩa và Thuật ngữ

| Thuật ngữ | Định nghĩa | Tiếng Anh |
|-----------|-----------|-----------|
| CW | Chứng quyền có bảo đảm - công cụ phái sinh cho phép mua/bán CKCS ở giá xác định | Covered Warrant |
| CKCS | Chứng khoán cơ sở - tài sản nền của chứng quyền | Underlying Asset |
| TLCĐ | Tỷ lệ chuyển đổi - số CW cần để đổi 1 cổ phiếu cơ sở | Conversion Ratio |
| Strike Price | Giá thực hiện quyền của chứng quyền | Strike Price |
| IV | Biến động hàm ý - mức biến động kỳ vọng được tính ngược từ giá thị trường | Implied Volatility |
| Greeks | Các hệ số đo độ nhạy của giá CW với các yếu tố (Delta, Theta, Vega, Gamma) | Greeks |
| Delta | Độ nhạy giá CW khi CKCS thay đổi 1 đơn vị | Delta |
| Theta | Tốc độ giảm giá CW theo thời gian (time decay) | Theta |
| Vega | Độ nhạy giá CW khi IV thay đổi 1% | Vega |
| TTM | Thời gian còn lại đến ngày đáo hạn (tính theo năm) | Time to Maturity |
| ITM | In-the-money - CW có giá trị nội tại dương | ITM |
| ATM | At-the-money - CW có giá trị nội tại bằng 0 | ATM |
| OTM | Out-of-the-money - CW có giá trị nội tại âm | OTM |
| Black-Scholes | Mô hình toán học định giá quyền chọn | Black-Scholes Model |

### 1.4 Tài liệu tham khảo

- Bảng giá Chứng quyền TCBS: https://www.tcbs.com.vn/bang-gia-chung-quyen
- Bảng giá Chứng quyền VPBankS: https://www.vpbanks.com.vn
- "Options, Futures, and Other Derivatives" - John C. Hull (tham khảo Black-Scholes)
- Confluence: "8. BRD bổ sung bảng thông tin phân tích giá Chứng quyền" (source document)
- Quy định của SSI/HNX về giao dịch chứng quyền có bảo đảm

---

## 2. MỤC TIÊU KINH DOANH

### 2.1 Vấn đề cần giải quyết

**Vấn đề hiện tại:**

Bảng giá Chứng quyền của VNDIRECT chỉ hiển thị thông tin giao dịch cơ bản (mã CW, giá khớp, khối lượng, % thay đổi) tương tự cổ phiếu, hoàn toàn thiếu lớp dữ liệu định giá và rủi ro đặc thù của CW. Điều này tạo ra các vấn đề:

**Đối với Khách hàng:**

- Không thể đánh giá CW đang đắt hay rẻ so với giá trị hợp lý
- Không biết cần giá CKCS tăng/giảm bao nhiêu để hòa vốn
- Không quản lý được rủi ro time decay (mất giá theo thời gian)
- Buộc phải sử dụng Excel hoặc website đối thủ (TCBS, VPBankS) để phân tích
- Rào cản lớn khi ra quyết định giao dịch nhanh

**Đối với Công ty:**

- Bảng giá CW kém cạnh tranh so với TCBS, VPBankS
- Mất cơ hội thu hút nhà đầu tư chuyên nghiệp giao dịch CW
- Thiếu công cụ hỗ trợ marketing cho đợt phát hành CW mới (09/2025)
- Khối lượng giao dịch CW thấp → thu phí giao dịch hạn chế

**Cơ hội:**

- Tháng 09/2025: VNDIRECT có đợt phát hành CW đầu tiên sau 1 năm tạm dừng
- Tạo "bộ sản phẩm truyền thông" kết hợp: Phát hành CW + Công cụ phân tích CW chuyên sâu
- Thu hút nhà đầu tư từ đối thủ nhờ công cụ vượt trội

### 2.2 Mục tiêu nghiệp vụ

| ID | Mục tiêu | Chỉ số đo lường (KPI) | Target | Thời hạn |
|----|----------|----------------------|--------|----------|
| BG-01 | Tăng khả năng cạnh tranh bảng giá CW | Số chỉ số phân tích hiển thị so với đối thủ | ≥ 7 chỉ số (ngang bằng TCBS) | Q3/2025 |
| BG-02 | Giảm rào cản ra quyết định giao dịch | % KH sử dụng công cụ bên ngoài để phân tích CW | Giảm 50% (từ survey) | Q4/2025 |
| BG-03 | Hỗ trợ marketing đợt phát hành CW mới | Tỷ lệ CW do VND phát hành được giao dịch qua DBoard | ≥ 70% khối lượng | 09/2025 |
| BG-04 | Tăng khối lượng giao dịch CW | Khối lượng giao dịch CW/tháng | Tăng 30% so với baseline | Q4/2025 |
| BG-05 | Thu hút KH chuyên nghiệp | Số KH Active trader giao dịch CW ≥ 5 lần/tháng | Tăng 20% | Q4/2025 |

**Alignment với chiến lược công ty:**

- **Trading Platform Strategy**: Nâng cao trải nghiệm người dùng, cung cấp công cụ phân tích chuyên sâu
- **Revenue Growth**: Tăng thu phí giao dịch từ segment CW
- **Competitive Positioning**: Thu hẹp khoảng cách với TCBS/VPBankS về công cụ phái sinh

---

## 3. CÁC BÊN LIÊN QUAN

### 3.1 Stakeholders nghiệp vụ

| Vai trò | Trách nhiệm | Mức độ quan tâm |
|---------|-------------|-----------------|
| Product Owner (Trading Platform) | Phê duyệt yêu cầu, ưu tiên backlog, quyết định scope | Cao |
| Head of Derivatives | Cung cấp insight về nhu cầu KH giao dịch CW, review logic nghiệp vụ | Cao |
| Marketing Manager | Lên kế hoạch truyền thông tính năng khi phát hành CW mới | Trung bình |
| Compliance Officer | Đảm bảo công bố thông tin tuân thủ quy định SSI/HNX | Trung bình |
| Customer Service Lead | Chuẩn bị tài liệu hướng dẫn KH, xử lý phản hồi | Trung bình |

### 3.2 Stakeholders kỹ thuật

| Vai trò | Trách nhiệm | Mức độ quan tâm |
|---------|-------------|-----------------|
| Tech Lead (DBoard) | Thiết kế kiến trúc, review technical feasibility | Cao |
| Quant Team Lead | Review công thức Black-Scholes, Greeks, IV calculation | Cao |
| Data Engineer | Cung cấp dữ liệu real-time (giá CKCS, lãi suất, thông số CW) | Cao |
| Backend Developer | Implement API tính toán chỉ số, xử lý performance | Cao |
| Frontend Developer | Hiển thị bảng giá, tooltip, export Excel | Cao |
| QA Engineer | Thiết kế test case, validate độ chính xác tính toán | Cao |
| DevOps | Deploy, monitor performance, alerting | Trung bình |

### 3.3 Người dùng cuối

**Phân loại theo đặc điểm:**

| Nhóm | Đặc điểm | Mục tiêu | Vấn đề gặp phải | Nhu cầu |
|------|----------|----------|-----------------|---------|
| **KH Retail / F0-Bán chuyên** | Vốn nhỏ, tần suất vừa, chưa hiểu sâu Greeks | Mua CW ăn biên độ ngắn hoặc hold đến hạn nếu đúng xu hướng | Không biết đắt/rẻ, không rõ cần giá CKCS tăng bao nhiêu để hòa vốn | Bộ chỉ số rút gọn (7 chỉ số), dễ hiểu, có tooltip giáo dục |
| **KH Active / Semi-pro** | Theo dõi nhiều mã, so sánh nhanh, xoay vòng vốn | Tối ưu hiệu suất vốn, chọn cấu trúc rủi ro hợp lý, khai thác chênh lệch IV | Phải export Excel / dùng nền tảng khác để lọc & định giá | Full bộ Greeks, có thể export Excel, sort/filter nhanh |

**Phân loại theo chiến lược thời gian:**

| Chiến lược | Khung thời gian | Trọng tâm quyết định | Chỉ số cốt lõi |
|------------|-----------------|----------------------|----------------|
| **Ngắn-Trung hạn (Trading CW)** | Trong ngày → vài tuần | Giá CW đắt/rẻ? Biên độ kỳ vọng vs phí thời gian? Thanh khoản? | Chênh lệch giá lý thuyết, IV, Delta, Theta, Khối lượng GD |
| **Dài hạn (Hold đến hạn)** | 1-3 tháng hoặc đến Expiry | Khả năng đạt Break-even / vượt Strike; rủi ro Time Decay tăng cuối kỳ | Điểm hòa vốn, TTM, Delta (ổn định?), IV, Theta |

---

## 4. YÊU CẦU CHỨC NĂNG

### 4.1 Tổng quan tính năng

Tính năng bao gồm 2 module chính:

**Module 1: Bảng giá Chứng quyền nâng cao**
- Hiển thị bảng giá CW với 7-9 chỉ số kỹ thuật tự động tính toán
- Chỉ số được cập nhật real-time hoặc near real-time (tùy độ phức tạp tính toán)
- Tooltip giáo dục cho từng chỉ số
- Chức năng sort, filter, export Excel

**Module 2: Tab "Chứng quyền liên quan" trên Sức khỏe Cổ phiếu**
- Hiển thị danh sách CW có CKCS là mã cổ phiếu đang xem
- Hiển thị subset các chỉ số quan trọng nhất (rút gọn)
- Link nhanh đến bảng giá CW chi tiết
- Nút MUA/BÁN trực tiếp từ bảng

### 4.2 User Stories

#### Epic 1: Nâng cấp Bảng giá Chứng quyền với chỉ số phân tích

| ID | User Story | Độ ưu tiên | Acceptance Criteria |
|----|------------|------------|---------------------|
| US-001 | Là **nhà đầu tư Retail**, tôi muốn xem **Giá lý thuyết** của CW để biết mức giá hợp lý và so sánh với giá thị trường | Must Have | • Giá lý thuyết tính theo Black-Scholes hiển thị trên bảng<br>• Có tooltip giải thích "Giá hợp lý theo mô hình toán học"<br>• Độ chính xác ±2% so với tính toán manual |
| US-002 | Là **nhà đầu tư Retail**, tôi muốn xem **Chênh lệch giá lý thuyết** để biết CW đang đắt hay rẻ | Must Have | • Hiển thị chênh lệch = Giá thị trường - Giá lý thuyết<br>• Màu sắc: Dương (đỏ) = đắt, Âm (xanh) = rẻ<br>• Tooltip: "Dương = đắt hơn fair value, Âm = rẻ hơn" |
| US-003 | Là **nhà đầu tư Retail**, tôi muốn xem **Điểm hòa vốn** để biết giá CKCS cần đạt bao nhiêu khi exercise | Must Have | • Công thức: Strike + (Giá CW × TLCĐ)<br>• Hiển thị với 2 chữ số thập phân<br>• Tooltip có ví dụ cụ thể |
| US-004 | Là **nhà đầu tư chuyên nghiệp**, tôi muốn xem **Đòn bẩy hiệu dụng** để đánh giá hiệu quả vốn | Must Have | • Công thức: Giá CKCS / (Giá CW × TLCĐ)<br>• Hiển thị với 2 chữ số thập phân<br>• Tooltip giải thích ý nghĩa rủi ro-lợi nhuận |
| US-005 | Là **nhà đầu tư chuyên nghiệp**, tôi muốn xem **Implied Volatility** để đánh giá kỳ vọng biến động của thị trường | Must Have | • Tính bằng phương pháp Bisection hoặc Newton-Raphson<br>• Hiển thị dưới dạng % (VD: 25.5%)<br>• Tooltip: "Biến động kỳ vọng của CKCS" |
| US-006 | Là **nhà đầu tư chuyên nghiệp**, tôi muốn xem **Delta** để biết độ nhạy giá CW với CKCS | Should Have | • Công thức: N(d1) từ Black-Scholes<br>• Hiển thị 0.00 - 1.00 (VD: 0.65)<br>• Tooltip có ví dụ: "0.6 = nếu CKCS tăng 100đ, CW tăng ~60đ" |
| US-007 | Là **nhà đầu tư chuyên nghiệp**, tôi muốn xem **Theta** để quản lý rủi ro time decay | Should Have | • Công thức Theta chuẩn, chuyển đổi sang đơn vị ngày<br>• Hiển thị số âm (VD: -50 VNĐ/ngày)<br>• Tooltip: "Mất giá ước tính mỗi ngày do yếu tố thời gian" |
| US-008 | Là **nhà đầu tư chuyên nghiệp**, tôi muốn xem **Vega** để đánh giá độ nhạy với IV | Should Have | • Công thức: S × N'(d1) × √T<br>• Hiển thị thay đổi giá trên mỗi 1% IV<br>• Tooltip giải thích ý nghĩa |
| US-009 | Là **nhà đầu tư**, tôi muốn xem **TTM** để biết thời gian còn lại đến đáo hạn | Must Have | • Hiển thị số ngày còn lại (VD: "45 ngày")<br>• Màu cảnh báo nếu TTM < 30 ngày (vàng), < 7 ngày (đỏ)<br>• Tooltip: "Thời gian còn lại ảnh hưởng đến giá trị thời gian" |
| US-010 | Là **nhà đầu tư**, tôi muốn **sort bảng giá** theo các chỉ số để tìm cơ hội | Should Have | • Cho phép sort theo bất kỳ cột nào<br>• Sort 2 chiều (tăng/giảm dần)<br>• Icon mũi tên hiển thị trạng thái sort |
| US-011 | Là **nhà đầu tư chuyên nghiệp**, tôi muốn **export bảng giá ra Excel** để phân tích offline | Should Have | • Nút "Export Excel" ở đầu bảng<br>• File .xlsx chứa tất cả chỉ số hiển thị<br>• Tên file: "CW_Analysis_YYYYMMDD_HHMMSS.xlsx" |

#### Epic 2: Tab "Chứng quyền liên quan" trên Sức khỏe Cổ phiếu

| ID | User Story | Độ ưu tiên | Acceptance Criteria |
|----|------------|------------|---------------------|
| US-012 | Là **nhà đầu tư**, khi xem chi tiết 1 cổ phiếu, tôi muốn biết có những **CW nào liên quan** đến cổ phiếu này | Must Have | • Tab "Chứng quyền" xuất hiện trên trang Sức khỏe CP<br>• Chỉ hiển thị khi có CW với CKCS = mã CP đang xem<br>• Danh sách CW hiển thị đầy đủ |
| US-013 | Là **nhà đầu tư**, tôi muốn xem **thông tin tóm tắt** của các CW liên quan để so sánh nhanh | Must Have | • Hiển thị 10-12 cột quan trọng nhất (rút gọn từ bảng đầy đủ)<br>• Bao gồm: Mã CW, Giá TT, Thay đổi, KL, Strike, Gap, Hòa vốn, GTNT, Tổ chức phát hành, TTM<br>• Cập nhật real-time |
| US-014 | Là **nhà đầu tư**, tôi muốn **giao dịch CW trực tiếp** từ tab này | Should Have | • Nút MUA/BÁN trên mỗi dòng<br>• Click vào mở popup đặt lệnh với mã CW đã chọn<br>• Popup tương tự đặt lệnh cổ phiếu |
| US-015 | Là **nhà đầu tư**, tôi muốn **xem chi tiết CW** khi cần thêm thông tin | Should Have | • Click vào Mã CW → mở trang chi tiết CW<br>• Click vào "Xem đầy đủ" → chuyển đến bảng giá CW với filter sẵn CKCS |

### 4.3 Yêu cầu chi tiết

#### 4.3.1 Chức năng 1: Tính toán và hiển thị Giá lý thuyết (Black-Scholes)

**Mô tả**: Tính giá hợp lý của CW theo mô hình Black-Scholes, hiển thị trên bảng giá để nhà đầu tư so sánh với giá thị trường.

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. Hệ thống thu thập các tham số đầu vào (S, K, T, r, C) từ data feed
2. Tính IV bằng phương pháp Bisection (mục 6.1.1)
3. Tính giá lý thuyết C_theo_lý_thuyết bằng công thức Black-Scholes
4. Hiển thị trên bảng giá, cập nhật mỗi khi giá CKCS hoặc giá CW thay đổi

**Business Rules**:
- BR-001: Sử dụng lãi suất phi rủi ro r = 2.5% (cố định, có thể điều chỉnh bởi Quant Team)
- BR-002: TTM tính theo công thức: (Ngày đáo hạn - Ngày hiện tại) / 365
- BR-003: Nếu TTM ≤ 0 (đã đáo hạn), hiển thị "N/A" cho tất cả chỉ số dựa trên Black-Scholes
- BR-004: Nếu không tính được IV (vì giá thị trường bất thường), hiển thị "N/A" cho Giá lý thuyết

**Validation Rules**:

| Trường | Quy tắc validate | Thông báo/Xử lý |
|--------|------------------|-----------------|
| S (Giá CKCS) | S > 0 | Nếu S ≤ 0, skip tính toán, hiển thị "N/A" |
| K (Strike Price) | K > 0 | Lấy từ master data CW, không validate runtime |
| T (TTM) | T > 0 | Nếu T ≤ 0, hiển thị "Đã đáo hạn" |
| r (Lãi suất) | 0 ≤ r ≤ 1 | Cố định = 0.025 (2.5%) |
| C (Giá CW thị trường) | C > 0 | Nếu C ≤ 0, skip tính IV, hiển thị "N/A" |

#### 4.3.2 Chức năng 2: Tính toán Chênh lệch giá lý thuyết

**Mô tả**: Tính chênh lệch giữa giá thị trường và giá lý thuyết để đánh giá CW đắt/rẻ.

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. Lấy Giá thị trường (C_market) và Giá lý thuyết (C_theory) từ bước trước
2. Tính: `Chênh lệch = C_market - C_theory`
3. Hiển thị với định dạng màu:
   - Nếu Chênh lệch > 0: màu đỏ (đắt)
   - Nếu Chênh lệch < 0: màu xanh (rẻ)
   - Nếu Chênh lệch = 0: màu xám (hợp lý)

**Business Rules**:
- BR-005: Chênh lệch trong khoảng [-5%, +5%] so với Giá lý thuyết được coi là hợp lý
- BR-006: Chênh lệch > +10% → cảnh báo "CW đang rất đắt" (warning, không block)
- BR-007: Nếu Giá lý thuyết = "N/A", Chênh lệch cũng hiển thị "N/A"

**Validation Rules**:

| Trường | Quy tắc validate | Thông báo |
|--------|------------------|-----------|
| C_market | > 0 | Nếu ≤ 0, hiển thị "N/A" |
| C_theory | > 0 hoặc = "N/A" | Nếu "N/A", Chênh lệch = "N/A" |

#### 4.3.3 Chức năng 3: Tính toán Điểm hòa vốn

**Mô tả**: Tính mức giá CKCS cần đạt để nhà đầu tư hòa vốn khi exercise CW.

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. Lấy K (Strike Price), C_market (Giá CW), TLCĐ từ master data
2. Tính: `Điểm hòa vốn = K + (C_market × TLCĐ)`
3. Hiển thị với 2 chữ số thập phân

**Business Rules**:
- BR-008: Áp dụng cho CW Call (quyền mua). Nếu có CW Put trong tương lai, công thức: `K - (C_market × TLCĐ)`
- BR-009: Tooltip hiển thị ví dụ cụ thể với số liệu của dòng đó

**Validation Rules**:

| Trường | Quy tắc validate | Thông báo |
|--------|------------------|-----------|
| K | > 0 | Lấy từ master data, không validate runtime |
| C_market | > 0 | Nếu ≤ 0, hiển thị "N/A" |
| TLCĐ | > 0 | Lấy từ master data (thường 1, 2, 5, 10) |

#### 4.3.4 Chức năng 4: Tính toán Đòn bẩy hiệu dụng

**Mô tả**: Đo lường mức độ khuếch đại của CW so với CKCS.

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. Lấy S (Giá CKCS), C_market (Giá CW), TLCĐ
2. Tính: `Đòn bẩy = S / (C_market × TLCĐ)`
3. Hiển thị với 2 chữ số thập phân

**Business Rules**:
- BR-010: Đòn bẩy thường trong khoảng 3-20. Nếu > 50, cảnh báo "Đòn bẩy rất cao, rủi ro lớn"
- BR-011: Tooltip: "Đòn bẩy 10 = 1 đồng CW tương đương 10 đồng CKCS"

**Validation Rules**:

| Trường | Quy tắc validate | Thông báo |
|--------|------------------|-----------|
| S | > 0 | Nếu ≤ 0, hiển thị "N/A" |
| C_market | > 0 | Nếu ≤ 0, hiển thị "N/A" |
| TLCĐ | > 0 | Lấy từ master data |

#### 4.3.5 Chức năng 5: Tính toán Implied Volatility (IV)

**Mô tả**: Tính độ biến động hàm ý bằng phương pháp Bisection hoặc Newton-Raphson.

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. Lấy S, K, T, r, C_market
2. Sử dụng phương pháp Bisection với:
   - σ_min = 0.01 (1%)
   - σ_max = 2.00 (200%)
   - Tolerance = 0.0001
   - Max iterations = 100
3. Tìm σ sao cho: `Black_Scholes(S, K, T, r, σ) ≈ C_market`
4. Hiển thị IV dưới dạng % (VD: 25.5%)

**Business Rules**:
- BR-012: Nếu không tìm được IV sau 100 iterations, hiển thị "N/A" (có thể do giá thị trường bất thường)
- BR-013: IV trong khoảng [10%, 60%] được coi là hợp lý cho thị trường VN. Nếu IV > 80%, cảnh báo "IV bất thường"

**Validation Rules**:

| Trường | Quy tắc validate | Thông báo |
|--------|------------------|-----------|
| C_market | > 0 | Nếu ≤ 0, skip IV calculation, hiển thị "N/A" |
| Convergence | &#124;C_calc - C_market&#124; < 0.0001 | Nếu không converge, hiển thị "N/A" |

#### 4.3.6 Chức năng 6: Tính toán Delta

**Mô tả**: Tính độ nhạy của giá CW theo giá CKCS.

**Độ ưu tiên**: Should Have

**Luồng nghiệp vụ**:
1. Lấy IV từ bước 4.3.5
2. Tính d1 theo công thức Black-Scholes
3. Tính Delta = N(d1)
4. Hiển thị với 2 chữ số thập phân (0.00 - 1.00)

**Business Rules**:
- BR-014: Delta càng gần 1 = CW càng ITM (trong tiền)
- BR-015: Delta càng gần 0 = CW càng OTM (ngoài tiền)
- BR-016: Nếu IV = "N/A", Delta cũng hiển thị "N/A"

#### 4.3.7 Chức năng 7: Tính toán Theta

**Mô tả**: Tính tốc độ giảm giá CW theo thời gian (time decay).

**Độ ưu tiên**: Should Have

**Luồng nghiệp vụ**:
1. Lấy IV từ bước 4.3.5
2. Tính Theta_năm theo công thức Black-Scholes
3. Chuyển đổi: `Theta_ngày = Theta_năm / 365`
4. Hiển thị với đơn vị VNĐ/ngày (VD: -50 VNĐ/ngày)

**Business Rules**:
- BR-017: Theta luôn âm (time decay)
- BR-018: Theta tăng nhanh (giảm giá nhanh hơn) khi gần đáo hạn (TTM < 30 ngày)
- BR-019: Tooltip có ví dụ: "Theta = -50 → mỗi ngày CW mất ~50đ do yếu tố thời gian"

#### 4.3.8 Chức năng 8: Tính toán Vega

**Mô tả**: Tính độ nhạy của giá CW theo IV.

**Độ ưu tiên**: Should Have

**Luồng nghiệp vụ**:
1. Lấy IV từ bước 4.3.5
2. Tính Vega = S × N'(d1) × √T
3. Hiển thị thay đổi giá trên mỗi 1% IV (VD: 120 VNĐ/1% IV)

**Business Rules**:
- BR-020: Vega cao = giá CW rất nhạy với thay đổi biến động
- BR-021: Vega thấp gần đáo hạn (TTM → 0)

#### 4.3.9 Chức năng 9: Hiển thị Time to Maturity (TTM)

**Mô tả**: Hiển thị số ngày còn lại đến đáo hạn.

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. Tính: `TTM_ngày = Ngày đáo hạn - Ngày hiện tại`
2. Hiển thị: "45 ngày"
3. Áp dụng màu cảnh báo:
   - TTM ≥ 30 ngày: màu đen (bình thường)
   - 7 ≤ TTM < 30 ngày: màu vàng (cảnh báo)
   - TTM < 7 ngày: màu đỏ (nguy hiểm - time decay rất nhanh)

**Business Rules**:
- BR-022: Nếu TTM ≤ 0, hiển thị "Đã đáo hạn"
- BR-023: Tooltip: "Thời gian còn lại ảnh hưởng đến Theta (time decay)"

#### 4.3.10 Chức năng 10: Sort bảng giá theo chỉ số

**Mô tả**: Cho phép sắp xếp bảng giá theo bất kỳ cột nào.

**Độ ưu tiên**: Should Have

**Luồng nghiệp vụ**:
1. Click vào header cột → sort tăng dần
2. Click lần 2 → sort giảm dần
3. Click lần 3 → bỏ sort, về trạng thái mặc định

**Business Rules**:
- BR-024: Mặc định sort theo "Khối lượng GD" giảm dần
- BR-025: Các cột có giá trị "N/A" luôn xếp cuối cùng khi sort

#### 4.3.11 Chức năng 11: Export Excel

**Mô tả**: Export toàn bộ bảng giá với các chỉ số ra file Excel.

**Độ ưu tiên**: Should Have

**Luồng nghiệp vụ**:
1. Click nút "Export Excel" ở đầu bảng
2. Hệ thống tạo file .xlsx chứa:
   - Tất cả các cột đang hiển thị
   - Dữ liệu tại thời điểm export (không real-time)
   - Header có timestamp: "Dữ liệu tại: DD/MM/YYYY HH:MM:SS"
3. Download file tên: `CW_Analysis_YYYYMMDD_HHMMSS.xlsx`

**Business Rules**:
- BR-026: Giới hạn 500 dòng/lần export (tránh quá tải)
- BR-027: File Excel bao gồm sheet "Metadata" với thông tin: Công thức các chỉ số, Giả định (r=2.5%), Disclaimer

#### 4.3.12 Chức năng 12: Tab "Chứng quyền liên quan" trên Sức khỏe CP

**Mô tả**: Hiển thị danh sách CW có CKCS là mã CP đang xem.

**Độ ưu tiên**: Must Have

**Luồng nghiệp vụ**:
1. KH truy cập trang Sức khỏe Cổ phiếu (VD: STB)
2. Hệ thống query danh sách CW có underlying = "STB"
3. Nếu có CW, hiển thị tab "Chứng quyền" (nếu không có, ẩn tab)
4. Click vào tab → hiển thị bảng CW với 10-12 cột quan trọng

**Business Rules**:
- BR-028: Chỉ hiển thị CW còn hiệu lực (chưa đáo hạn)
- BR-029: Sắp xếp mặc định: TTM giảm dần (CW sắp hết hạn lên đầu)
- BR-030: Hiển thị tối đa 20 CW, nếu nhiều hơn có pagination

**Các cột hiển thị (rút gọn)**:

| Cột | Ý nghĩa | Nguồn |
|-----|---------|-------|
| Mã CW | Mã định danh CW | Master data |
| Giá thị trường | Giá khớp lệnh hiện tại | Real-time feed |
| Thay đổi | % thay đổi so với phiên trước | Tính toán |
| Khối lượng | Khối lượng GD trong phiên | Real-time feed |
| Giá thực hiện | Strike Price | Master data |
| Gap | (Giá CKCS - Strike) / Strike × 100% | Tính toán |
| Hòa vốn | Strike + (Giá CW × TLCĐ) | Tính toán |
| Giá trị nội tại | max(0, (S - K) / TLCĐ) | Tính toán |
| Tổ chức phát hành | Issuer (BSC, SSI, VND...) | Master data |
| Thời hạn | Số ngày còn lại (TTM) | Tính toán |
| Thao tác | Nút MUA/BÁN | UI component |

### 4.4 Quy tắc nghiệp vụ tổng quát

| ID | Quy tắc | Hành động khi vi phạm |
|----|---------|----------------------|
| BR-001 | Lãi suất phi rủi ro r = 2.5% (cố định) | Quant Team có thể điều chỉnh qua config, không hardcode |
| BR-002 | TTM tính theo công thức: (Expiry Date - Current Date) / 365 | Nếu TTM ≤ 0, hiển thị "Đã đáo hạn" |
| BR-003 | Chỉ hiển thị CW còn hiệu lực (TTM > 0) trên bảng giá | CW đã đáo hạn tự động ẩn |
| BR-004 | Nếu tính toán lỗi (missing data, calculation error), hiển thị "N/A" cho chỉ số đó | Không block hiển thị toàn bảng, log error để debug |
| BR-005 | Chênh lệch giá lý thuyết trong [-5%, +5%] là hợp lý | Nếu > +10%, tooltip cảnh báo "Đang rất đắt" |
| BR-006 | IV trong [10%, 60%] là hợp lý cho thị trường VN | Nếu IV > 80%, tooltip cảnh báo "IV bất thường" |
| BR-007 | Đòn bẩy thường 3-20 | Nếu > 50, tooltip cảnh báo "Rủi ro rất cao" |
| BR-008 | Công thức hòa vốn cho Call: K + (C × TLCĐ) | Nếu có Put trong tương lai: K - (C × TLCĐ) |
| BR-009 | Theta luôn âm (time decay) | Nếu Theta > 0 (lỗi tính toán), hiển thị "N/A" và log error |
| BR-010 | Update frequency: Real-time cho giá thị trường, Near real-time (5-10s) cho các chỉ số tính toán | Balance giữa độ chính xác và performance |

### 4.5 Workflow & Process Flow

**Workflow tính toán chỉ số CW (High-level):**

```
[Data Feed] → [Validation] → [Calculation Engine] → [Cache] → [Display]
     ↓
  - Giá CKCS (S)
  - Giá CW (C)
  - Master data (K, TLCĐ, Expiry)
  - Lãi suất (r)
                   ↓
             Validate inputs
             (S>0, K>0, T>0, C>0)
                   ↓
            [IV Calculation]
            (Bisection method)
                   ↓
        [Black-Scholes Pricing]
        [Greeks Calculation]
                   ↓
           Cache 5-10s
           (reduce load)
                   ↓
         Display on UI
         (với tooltip)
```

**Workflow chi tiết - Tính Giá lý thuyết và IV:**

```
Bước 1: Thu thập Input
  ├─ Lấy giá CKCS (S) từ real-time feed
  ├─ Lấy giá CW (C_market) từ real-time feed
  ├─ Lấy Strike (K), TLCĐ, Expiry từ master data
  ├─ Tính TTM = (Expiry - Today) / 365
  └─ Lấy r = 2.5% (config)

Bước 2: Validate
  IF S ≤ 0 OR K ≤ 0 OR TTM ≤ 0 OR C_market ≤ 0 THEN
    Hiển thị "N/A" cho tất cả chỉ số
    RETURN
  END IF

Bước 3: Tính IV (Bisection method)
  SET σ_min = 0.01, σ_max = 2.0, tolerance = 0.0001
  FOR iteration = 1 TO 100:
    σ_mid = (σ_min + σ_max) / 2
    C_calc = Black_Scholes(S, K, TTM, r, σ_mid)
    IF |C_calc - C_market| < tolerance THEN
      IV = σ_mid
      BREAK
    ELSE IF C_calc > C_market THEN
      σ_max = σ_mid
    ELSE
      σ_min = σ_mid
    END IF
  END FOR
  IF iteration > 100 THEN
    IV = "N/A"
  END IF

Bước 4: Tính Giá lý thuyết
  IF IV != "N/A" THEN
    C_theory = Black_Scholes(S, K, TTM, r, IV)
  ELSE
    C_theory = "N/A"
  END IF

Bước 5: Tính các chỉ số khác
  Chênh lệch = C_market - C_theory
  Điểm hòa vốn = K + (C_market × TLCĐ)
  Đòn bẩy = S / (C_market × TLCĐ)
  Delta = N(d1)
  Theta_ngày = Theta_năm / 365
  Vega = S × N'(d1) × √T

Bước 6: Cache & Display
  Cache kết quả 5-10s
  Hiển thị trên UI với tooltip
```

---

## 5. YÊU CẦU DỮ LIỆU

### 5.1 Input Specification

| Trường Input | Nguồn | Kiểu dữ liệu | Bắt buộc | Validation | Giá trị mặc định |
|--------------|-------|--------------|----------|------------|------------------|
| symbol_cw | User/System | String | Y | Regex: `^[A-Z]{4}[0-9]{4}$` | N/A |
| S (Giá CKCS) | Real-time feed | Decimal(10,2) | Y | S > 0 | N/A (phải có data) |
| K (Strike Price) | Master data CW | Decimal(10,2) | Y | K > 0 | Từ master data |
| TLCĐ | Master data CW | Integer | Y | TLCĐ ∈ {1, 2, 5, 10} | Từ master data |
| Expiry_Date | Master data CW | Date | Y | Expiry > Today | Từ master data |
| C_market (Giá CW) | Real-time feed | Decimal(10,3) | Y | C > 0 | N/A (phải có data) |
| r (Lãi suất) | Config | Decimal(4,4) | Y | 0 ≤ r ≤ 1 | 0.025 (2.5%) |
| Underlying_Symbol | Master data CW | String | Y | Mã CKCS hợp lệ | Từ master data |
| Issuer | Master data CW | String | Y | Tổ chức phát hành | Từ master data |

### 5.2 Output Specification

| Trường Output | Kiểu dữ liệu | Mô tả | Ví dụ | Format hiển thị |
|---------------|--------------|-------|-------|-----------------|
| symbol_cw | String | Mã chứng quyền | CACB2505 | Uppercase |
| price_market | Decimal(10,3) | Giá thị trường CW | 1.350 | #,##0.000 VNĐ |
| price_change_pct | Decimal(5,2) | % thay đổi giá | +0.70 | +#,##0.00% (màu đỏ/xanh) |
| volume | Integer | Khối lượng GD | 65300 | #,### (nghìn CW) |
| price_theory | Decimal(10,3) | Giá lý thuyết | 1.320 | #,##0.000 VNĐ |
| price_diff | Decimal(10,3) | Chênh lệch = Market - Theory | +0.030 | +#,##0.000 VNĐ (màu) |
| breakeven | Decimal(10,2) | Điểm hòa vốn | 25.370 | #,##0.00 VNĐ |
| leverage | Decimal(5,2) | Đòn bẩy hiệu dụng | 8.50 | #,##0.00 |
| iv | Decimal(5,2) | Implied Volatility | 25.50 | #,##0.00% |
| delta | Decimal(4,2) | Delta | 0.65 | 0.00 - 1.00 |
| theta | Decimal(10,2) | Theta (VNĐ/ngày) | -50.00 | -#,##0.00 VNĐ/ngày |
| vega | Decimal(10,2) | Vega (VNĐ/1% IV) | 120.00 | #,##0.00 VNĐ |
| ttm_days | Integer | Số ngày còn lại | 45 | # ngày (màu cảnh báo) |
| strike | Decimal(10,2) | Giá thực hiện | 23.397 | #,##0.000 VNĐ |
| conversion_ratio | Integer | Tỷ lệ chuyển đổi | 2 | # |
| issuer | String | Tổ chức phát hành | BSC | Uppercase |

### 5.3 Data Validation Rules

| Validation | Mô tả | Điều kiện | Thông báo/Hành động |
|------------|-------|-----------|---------------------|
| VAL-001 | Giá CKCS hợp lệ | S > 0 | Nếu S ≤ 0, hiển thị "N/A" cho tất cả chỉ số |
| VAL-002 | Giá CW hợp lệ | C > 0 | Nếu C ≤ 0, hiển thị "N/A" cho tất cả chỉ số |
| VAL-003 | TTM hợp lệ | T > 0 | Nếu T ≤ 0, hiển thị "Đã đáo hạn" |
| VAL-004 | Strike Price hợp lệ | K > 0 | Lấy từ master data, log error nếu K ≤ 0 |
| VAL-005 | TLCĐ hợp lệ | TLCĐ ∈ {1, 2, 5, 10} | Lấy từ master data, log error nếu không hợp lệ |
| VAL-006 | IV convergence | &#124;C_calc - C_market&#124; < 0.0001 sau ≤100 iter | Nếu không converge, IV = "N/A" |
| VAL-007 | IV trong khoảng hợp lý | 0.01 ≤ IV ≤ 2.0 | Nếu IV > 0.8, tooltip cảnh báo "IV bất thường" |
| VAL-008 | Chênh lệch giá hợp lý | &#124;Chênh lệch&#124; / Giá lý thuyết < 0.3 | Nếu > 0.3, log warning (data quality issue) |
| VAL-009 | Delta trong khoảng [0,1] | 0 ≤ Delta ≤ 1 | Nếu ngoài khoảng, Delta = "N/A", log error |
| VAL-010 | Theta âm | Theta < 0 | Nếu Theta ≥ 0, Theta = "N/A", log error |

---

## 6. CHI TIẾT IPO (INPUT - PROCESS - OUTPUT)

### 6.1 IPO Flow cho Tính toán Giá lý thuyết và IV

#### INPUT

**User Input:** (Không có - chức năng tự động tính toán)

**System Input:**

| Tham số | Mô tả | Kiểu | Nguồn | Ví dụ |
|---------|-------|------|-------|-------|
| S | Giá hiện tại của CKCS | Decimal(10,2) | Real-time price feed | 24.30 VNĐ |
| K | Giá thực hiện (Strike Price) | Decimal(10,2) | Master data CW | 23.397 VNĐ |
| Expiry_Date | Ngày đáo hạn | Date | Master data CW | 2025-05-15 |
| C_market | Giá CW trên thị trường | Decimal(10,3) | Real-time price feed | 1.350 VNĐ |
| TLCĐ | Tỷ lệ chuyển đổi | Integer | Master data CW | 2 |
| r | Lãi suất phi rủi ro | Decimal(4,4) | Config | 0.025 (2.5%) |

**Context Data:**
- Current_Date: Ngày hiện tại hệ thống (để tính TTM)
- CW_Master_Data: Bảng master chứa thông tin cố định của CW (K, TLCĐ, Expiry, Underlying)

#### PROCESS

**Thuật toán xử lý:**

**Bước 1: Validate Input**

```
IF S ≤ 0 THEN
  LOG error "Giá CKCS không hợp lệ: S = {S}"
  RETURN {all_indicators: "N/A"}
END IF

IF C_market ≤ 0 THEN
  LOG error "Giá CW không hợp lệ: C = {C_market}"
  RETURN {all_indicators: "N/A"}
END IF

IF K ≤ 0 THEN
  LOG error "Strike Price không hợp lệ: K = {K} cho CW {symbol}"
  RETURN {all_indicators: "N/A"}
END IF

T = (Expiry_Date - Current_Date) / 365
IF T ≤ 0 THEN
  LOG info "CW đã đáo hạn: {symbol}"
  RETURN {status: "Expired", all_indicators: "Đã đáo hạn"}
END IF

IF r < 0 OR r > 1 THEN
  LOG error "Lãi suất không hợp lệ: r = {r}"
  r = 0.025  // Sử dụng default
END IF
```

**Bước 2: Tính Implied Volatility (IV) bằng Bisection Method**

```
FUNCTION calculate_IV(S, K, T, r, C_market):
  σ_min = 0.01      // 1% volatility
  σ_max = 2.00      // 200% volatility
  tolerance = 0.0001
  max_iterations = 100

  FOR iteration = 1 TO max_iterations:
    σ_mid = (σ_min + σ_max) / 2

    // Tính giá lý thuyết với σ_mid
    d1 = [ln(S/K) + (r + σ_mid²/2) × T] / (σ_mid × √T)
    d2 = d1 - σ_mid × √T
    C_calc = S × N(d1) - K × e^(-r×T) × N(d2)

    // Kiểm tra convergence
    IF |C_calc - C_market| < tolerance THEN
      LOG info "IV converged at iteration {iteration}: σ = {σ_mid}"
      RETURN σ_mid
    END IF

    // Điều chỉnh khoảng tìm kiếm
    IF C_calc > C_market THEN
      σ_max = σ_mid  // Giá tính cao quá → giảm volatility
    ELSE
      σ_min = σ_mid  // Giá tính thấp quá → tăng volatility
    END IF
  END FOR

  // Không converge sau 100 iterations
  LOG warning "IV không converge cho CW {symbol}: C_market={C_market}, S={S}, K={K}, T={T}"
  RETURN NULL
END FUNCTION

IV = calculate_IV(S, K, T, r, C_market)

IF IV = NULL THEN
  RETURN {
    iv: "N/A",
    price_theory: "N/A",
    price_diff: "N/A",
    delta: "N/A",
    theta: "N/A",
    vega: "N/A"
  }
END IF
```

**⚠️ Assumption**: Sử dụng Bisection method vì đơn giản, ổn định. Có thể nâng cấp sang Newton-Raphson (nhanh hơn nhưng phức tạp hơn) trong phase 2 nếu cần optimize performance.

**Bước 3: Tính Giá lý thuyết (Black-Scholes)**

```
FUNCTION black_scholes_call(S, K, T, r, σ):
  d1 = [ln(S/K) + (r + σ²/2) × T] / (σ × √T)
  d2 = d1 - σ × √T

  // N(x) là hàm phân phối tích lũy chuẩn (CDF of standard normal distribution)
  C = S × N(d1) - K × e^(-r×T) × N(d2)

  RETURN C
END FUNCTION

C_theory = black_scholes_call(S, K, T, r, IV)
```

**⚠️ Assumption**:
- Sử dụng mô hình Black-Scholes chuẩn cho European Call Option
- Giả định thị trường hiệu quả, không có chi phí giao dịch
- Giả định không có cổ tức (nếu CKCS có cổ tức, cần điều chỉnh công thức → phase 2)

**Bước 4: Tính các chỉ số khác**

```
// Chênh lệch giá lý thuyết
price_diff = C_market - C_theory

// Điểm hòa vốn
breakeven = K + (C_market × TLCĐ)

// Đòn bẩy hiệu dụng
leverage = S / (C_market × TLCĐ)

// Delta
d1 = [ln(S/K) + (r + IV²/2) × T] / (IV × √T)
delta = N(d1)

// Theta (tính theo năm rồi chuyển sang ngày)
d2 = d1 - IV × √T
theta_year = -[(S × N'(d1) × IV) / (2 × √T)] - [r × K × e^(-r×T) × N(d2)]
theta_day = theta_year / 365

// Vega
vega = S × N'(d1) × √T

// TTM
ttm_days = (Expiry_Date - Current_Date).days

// Validate kết quả
IF delta < 0 OR delta > 1 THEN
  LOG error "Delta ngoài khoảng [0,1]: {delta} cho CW {symbol}"
  delta = "N/A"
END IF

IF theta_day ≥ 0 THEN
  LOG error "Theta không âm: {theta_day} cho CW {symbol}"
  theta_day = "N/A"
END IF
```

**Hàm phụ trợ:**

```
FUNCTION N(x):
  // Cumulative Distribution Function của phân phối chuẩn
  // Sử dụng thư viện toán học (VD: scipy.stats.norm.cdf trong Python)
  // Hoặc công thức xấp xỉ nếu không có thư viện
  RETURN cdf_standard_normal(x)
END FUNCTION

FUNCTION N_prime(x):
  // Probability Density Function của phân phối chuẩn
  // N'(x) = (1/√(2π)) × e^(-x²/2)
  RETURN (1 / √(2π)) × e^(-x²/2)
END FUNCTION
```

**Business Logic đặc biệt:**

- **Xử lý CW gần đáo hạn (TTM < 7 ngày):**
  - Theta tăng rất nhanh (time decay cực mạnh)
  - Vega giảm về gần 0
  - Cần cảnh báo màu đỏ cho TTM

- **Xử lý CW Deep ITM (S >> K) hoặc Deep OTM (S << K):**
  - Deep ITM: Delta → 1, Theta nhỏ
  - Deep OTM: Delta → 0, giá CW rất thấp, có thể bị lỗi tính IV
  - Cần validation đặc biệt

**Error Handling:**

```
ERROR 1: IV không converge (sau 100 iterations)
  → LOG warning với chi tiết (S, K, T, C_market)
  → RETURN {iv: "N/A", và tất cả chỉ số phụ thuộc IV}
  → Hiển thị "N/A" trên UI với tooltip "Không tính được (dữ liệu bất thường)"

ERROR 2: Giá CKCS hoặc Giá CW ≤ 0
  → LOG error
  → RETURN {all_indicators: "N/A"}
  → Hiển thị "N/A" cho toàn bộ dòng

ERROR 3: CW đã đáo hạn (T ≤ 0)
  → LOG info
  → RETURN {status: "Expired"}
  → Ẩn dòng khỏi bảng giá (theo BR-003)

ERROR 4: Master data thiếu (K, TLCĐ, Expiry = NULL)
  → LOG critical error
  → Alert DevOps/Data team
  → RETURN {all_indicators: "N/A"}

ERROR 5: Calculation exception (division by zero, overflow)
  → LOG error với stack trace
  → RETURN "N/A" cho chỉ số bị lỗi
  → Tiếp tục tính các chỉ số khác nếu có thể
```

#### OUTPUT

**Success Response:**

| Trường | Kiểu | Mô tả | Ví dụ |
|--------|------|-------|-------|
| symbol_cw | String | Mã chứng quyền | CACB2505 |
| price_theory | Decimal(10,3) | Giá lý thuyết | 1.320 |
| price_diff | Decimal(10,3) | Chênh lệch giá | +0.030 |
| breakeven | Decimal(10,2) | Điểm hòa vốn | 25.37 |
| leverage | Decimal(5,2) | Đòn bẩy | 8.50 |
| iv | Decimal(5,2) | IV (%) | 25.50 |
| delta | Decimal(4,2) | Delta | 0.65 |
| theta_day | Decimal(10,2) | Theta (VNĐ/ngày) | -50.00 |
| vega | Decimal(10,2) | Vega (VNĐ/1% IV) | 120.00 |
| ttm_days | Integer | Ngày còn lại | 45 |
| calculation_timestamp | Timestamp | Thời điểm tính toán | 2025-11-28 10:30:15 |
| status | String | Trạng thái | "SUCCESS" |

**Error Response:**

| Error Code | Mô tả | Condition | Displayed Value |
|------------|-------|-----------|-----------------|
| ERR-CW-001 | Giá CKCS không hợp lệ | S ≤ 0 | all_indicators = "N/A" |
| ERR-CW-002 | Giá CW không hợp lệ | C ≤ 0 | all_indicators = "N/A" |
| ERR-CW-003 | CW đã đáo hạn | T ≤ 0 | status = "Expired", ẩn khỏi bảng |
| ERR-CW-004 | IV không converge | Bisection không hội tụ | iv = "N/A", các Greeks = "N/A" |
| ERR-CW-005 | Master data thiếu | K, TLCĐ, Expiry = NULL | all_indicators = "N/A", log critical |
| ERR-CW-006 | Calculation error | Exception trong tính toán | chỉ số bị lỗi = "N/A", log error |

**Side Effects:**
- Cache kết quả tính toán 5-10s để giảm tải (sử dụng Redis hoặc in-memory cache)
- Log calculation time để monitor performance
- Increment counter metric cho monitoring (success/error count, latency)
- Nếu IV bất thường (> 80%), trigger alert cho Quant team review

### 6.2 State Diagram

Chức năng này không có state machine phức tạp (là calculation stateless). Tuy nhiên, có thể mô tả trạng thái của **dữ liệu CW**:

```
[Active CW] → (T = 0) → [Expired CW] → (Archive after 30 days) → [Archived]
     ↓
   (Tính toán định kỳ)
     ↓
[Calculated Indicators]
     ↓
   (Cache 5-10s)
     ↓
[Displayed on UI]
```

**Trạng thái (States):**

| Trạng thái | Mô tả | Điều kiện | Terminal State |
|------------|-------|-----------|----------------|
| ACTIVE | CW đang hoạt động, chưa đáo hạn | TTM > 0 | No |
| NEAR_EXPIRY | CW sắp đáo hạn (cảnh báo) | 0 < TTM < 7 | No |
| EXPIRED | CW đã đáo hạn | TTM ≤ 0 | No |
| ARCHIVED | CW đã đáo hạn > 30 ngày, lưu trữ | Expiry + 30 days < Today | Yes |

**Chuyển trạng thái (Transitions):**

| Từ trạng thái | Sự kiện | Đến trạng thái | Side Effects |
|---------------|---------|----------------|--------------|
| ACTIVE | TTM giảm xuống < 7 ngày | NEAR_EXPIRY | Hiển thị màu cảnh báo vàng/đỏ |
| NEAR_EXPIRY | Đến ngày đáo hạn (T = 0) | EXPIRED | Ẩn khỏi bảng giá, ngưng tính toán |
| EXPIRED | Sau 30 ngày kể từ Expiry | ARCHIVED | Chuyển sang DB archive, xóa khỏi cache |

---

## 7. YÊU CẦU GIAO DIỆN NGƯỜI DÙNG

### 7.1 Màn hình chính: Bảng giá Chứng quyền nâng cao

**Tên màn hình**: Bảng giá Chứng quyền (DBoard Warrants Table)

**Mục đích**: Hiển thị danh sách CW với đầy đủ thông tin giao dịch và chỉ số phân tích chuyên sâu, cho phép nhà đầu tư đánh giá, so sánh và ra quyết định giao dịch.

**Layout**:
```
+-----------------------------------------------------------------------------------------+
|  BẢNG GIÁ CHỨNG QUYỀN                              [Export Excel] [Tooltip: ?]          |
+-----------------------------------------------------------------------------------------+
| Mã CW ↕ | Giá TT ↕ | Thay đổi ↕ | KL ↕ | Giá LT ↕ | Chênh lệch ↕ | Hòa vốn ↕ | ... ↕ |
|---------|----------|------------|------|----------|--------------|-----------|-------|
| CACB2505| 1.350    | +0.01(0.7%)| 65.3K| 1.320    | +0.030 🔴    | 25.37     | ...   |
| CACB2502| 2.060    | -0.04(-1.9%)| 38.3K| 2.100   | -0.040 🟢    | 26.81     | ...   |
| ...     | ...      | ...        | ...  | ...      | ...          | ...       | ...   |
+-----------------------------------------------------------------------------------------+
| Tooltip khi hover cột header:                                                           |
| "Giá lý thuyết: Giá hợp lý theo mô hình Black-Scholes. So sánh với Giá TT để đánh giá  |
|  CW đang đắt hay rẻ."                                                                   |
+-----------------------------------------------------------------------------------------+
```

**Các cột hiển thị (full bảng giá):**

| STT | Tên cột | Loại control | Sortable | Filterable | Tooltip (rút gọn) |
|-----|---------|--------------|----------|------------|-------------------|
| 1 | Mã CW | Text + Link | Yes | Yes | Mã định danh chứng quyền. Click để xem chi tiết. |
| 2 | Giá thị trường | Number | Yes | No | Giá khớp lệnh hiện tại (real-time) |
| 3 | Thay đổi | Number + Color | Yes | No | % thay đổi so với phiên trước. Đỏ=tăng, Xanh=giảm |
| 4 | Khối lượng | Number | Yes | Yes | Khối lượng giao dịch trong phiên (nghìn CW) |
| 5 | Giá lý thuyết | Number | Yes | No | Giá hợp lý theo Black-Scholes. So sánh với Giá TT để đánh giá đắt/rẻ. |
| 6 | Chênh lệch | Number + Color | Yes | Yes | Giá TT - Giá LT. Dương(đỏ)=đắt, Âm(xanh)=rẻ so với fair value. |
| 7 | Điểm hòa vốn | Number | Yes | No | Giá CKCS cần đạt để hòa vốn khi exercise. Quan trọng cho hold-to-expiry. |
| 8 | Đòn bẩy | Number | Yes | Yes | Đo hiệu quả vốn. Đòn bẩy 10 = 1đ CW tương đương 10đ CKCS. |
| 9 | IV (%) | Number | Yes | Yes | Biến động hàm ý. Kỳ vọng biến động của CKCS. Cao = kỳ vọng biến mạnh. |
| 10 | Delta | Number | Yes | No | Độ nhạy giá CW theo CKCS. Delta 0.6 = CKCS tăng 100đ → CW tăng ~60đ. |
| 11 | Theta (VNĐ/ngày) | Number | Yes | No | Time decay. Theta -50 = mỗi ngày mất ~50đ do yếu tố thời gian. |
| 12 | Vega | Number | Yes | No | Độ nhạy theo IV. Vega 120 = IV tăng 1% → giá CW tăng ~120đ. |
| 13 | Strike | Number | Yes | No | Giá thực hiện quyền |
| 14 | TLCĐ | Number | Yes | Yes | Tỷ lệ chuyển đổi (CW:CP cơ sở) |
| 15 | TTM (ngày) | Number + Color | Yes | Yes | Số ngày còn lại. Màu cảnh báo: <30 ngày=vàng, <7 ngày=đỏ. |
| 16 | Tổ chức phát hành | Text | Yes | Yes | Issuer (VND, BSC, SSI...) |
| 17 | Thao tác | Button | No | No | Nút MUA/BÁN |

**Actions**:
- **Button "Export Excel"**: Export toàn bộ bảng ra file .xlsx
- **Button "MUA/BÁN"** trên mỗi dòng: Mở popup đặt lệnh với mã CW đã chọn
- **Click vào Mã CW**: Chuyển đến trang chi tiết CW
- **Click header cột**: Sort tăng/giảm dần
- **Hover vào icon "?" ở header cột**: Hiển thị tooltip giải thích chỉ số

**Validation & Error Display**:
- Nếu chỉ số = "N/A": Hiển thị "N/A" với màu xám, tooltip "Không tính được (dữ liệu bất thường)"
- Nếu toàn bộ bảng không load được: Hiển thị "Không thể tải dữ liệu. Vui lòng thử lại sau." với nút Refresh
- Nếu IV > 80%: Hiển thị icon cảnh báo ⚠️ với tooltip "IV bất thường cao"
- Nếu Chênh lệch > +10%: Hiển thị đậm màu đỏ với tooltip "CW đang rất đắt"

**Performance Requirements**:
- Initial load: < 2s (load 50 CW với tất cả chỉ số)
- Real-time update: Giá thị trường, Thay đổi, Khối lượng update mỗi giây
- Calculation update: IV, Greeks update mỗi 5-10s (cached)
- Sort/Filter: < 0.5s

### 7.2 Màn hình phụ: Tab "Chứng quyền liên quan" trên Sức khỏe Cổ phiếu

**Tên màn hình**: Tab Chứng quyền (Related Warrants Tab)

**Mục đích**: Hiển thị danh sách CW có CKCS là mã cổ phiếu đang xem, giúp nhà đầu tư dễ dàng khám phá cơ hội giao dịch CW.

**Layout**:
```
+-----------------------------------------------------------------------------------------+
|  Chi tiết Cổ phiếu: STB                                                                 |
|  [Tab: Tổng quan] [Tab: Phân tích] [Tab: Tin tức] [Tab: Chứng quyền] ← Active          |
+-----------------------------------------------------------------------------------------+
|  CHỨNG QUYỀN LIÊN QUAN ĐÊN STB                                    [Xem đầy đủ →]        |
+-----------------------------------------------------------------------------------------+
| Mã CW   | Giá TT | Thay đổi  | KL   | Strike | Gap   | Hòa vốn | GTNT  | Issuer | TTM    |
|---------|--------|-----------|------|--------|-------|---------|-------|--------|--------|
| CSTB2505| 0.850  | +0.02(2.4%)| 120K | 22.50  | +8.0% | 24.20   | 0.30  | VND    | 45 ngày|
| CSTB2508| 1.200  | -0.01(-0.8%)| 80K | 24.00  | +1.3% | 26.40   | 0.15  | BSC    | 120 ngày|
| ...     | ...    | ...       | ...  | ...    | ...   | ...     | ...   | ...    | ...    |
+-----------------------------------------------------------------------------------------+
| [Nút MUA] [Nút BÁN]                                                                      |
+-----------------------------------------------------------------------------------------+
```

**Các cột hiển thị (rút gọn - 10 cột):**

| Tên cột | Kiểu | Sortable | Mô tả |
|---------|------|----------|-------|
| Mã CW | Text + Link | Yes | Mã CW, click để xem chi tiết |
| Giá thị trường | Number | Yes | Giá khớp lệnh real-time |
| Thay đổi | Number + Color | Yes | % thay đổi giá |
| Khối lượng | Number | Yes | KL giao dịch (nghìn CW) |
| Strike | Number | Yes | Giá thực hiện |
| Gap | Number + Color | Yes | (Giá CKCS - Strike) / Strike × 100%. Dương=ITM, Âm=OTM |
| Hòa vốn | Number | Yes | Điểm hòa vốn |
| Giá trị nội tại | Number | Yes | max(0, (S-K)/TLCĐ) |
| Tổ chức phát hành | Text | Yes | Issuer |
| TTM | Number + Color | Yes | Ngày còn lại, màu cảnh báo |
| **Thao tác** | Button | No | Nút MUA/BÁN |

**Actions**:
- **Click "Xem đầy đủ"**: Chuyển đến Bảng giá CW với filter sẵn Underlying = STB
- **Click Mã CW**: Mở trang chi tiết CW
- **Click nút MUA/BÁN**: Mở popup đặt lệnh

**Validation & Error Display**:
- Nếu không có CW liên quan: Ẩn tab "Chứng quyền" (theo BR-028)
- Nếu CW đã đáo hạn: Không hiển thị trong danh sách (theo BR-028)

**Pagination**:
- Hiển thị tối đa 20 CW/trang
- Nếu > 20 CW, có pagination ở cuối bảng
- Mặc định sort theo TTM tăng dần (CW sắp hết hạn lên đầu)

---

## 8. PHỤ LỤC

### 8.1 Công thức Chi tiết

#### Black-Scholes Model (European Call Option)

```
C = S × N(d1) - K × e^(-r×T) × N(d2)

Trong đó:
  d1 = [ln(S/K) + (r + σ²/2) × T] / (σ × √T)
  d2 = d1 - σ × √T

  C  = Giá call option (giá lý thuyết CW)
  S  = Giá hiện tại của tài sản cơ sở (CKCS)
  K  = Giá thực hiện (Strike Price)
  T  = Thời gian đến đáo hạn (tính theo năm)
  r  = Lãi suất phi rủi ro
  σ  = Implied Volatility (IV)
  N(x) = Cumulative Distribution Function của phân phối chuẩn
  e  = Hằng số Euler (≈ 2.71828)
  ln = Logarit tự nhiên
```

#### Greeks Formulas

**Delta (Δ):**
```
Δ = N(d1)

Ý nghĩa:
- Độ nhạy của giá CW khi giá CKCS thay đổi 1 đơn vị
- Phạm vi: 0 ≤ Δ ≤ 1
- Δ = 0.6 → nếu S tăng 100đ, C tăng ~60đ
```

**Theta (Θ):**
```
Θ_năm = -[(S × N'(d1) × σ) / (2 × √T)] - [r × K × e^(-r×T) × N(d2)]
Θ_ngày = Θ_năm / 365

Trong đó:
  N'(d1) = (1/√(2π)) × e^(-d1²/2)  (PDF của phân phối chuẩn)

Ý nghĩa:
- Time decay - tốc độ giảm giá CW theo thời gian
- Θ luôn âm (CW mất giá theo thời gian)
- Θ = -50 VNĐ/ngày → mỗi ngày mất ~50đ
```

**Vega (ν):**
```
ν = S × N'(d1) × √T

Ý nghĩa:
- Độ nhạy của giá CW khi IV thay đổi 1%
- ν = 120 → nếu IV tăng từ 25% lên 26%, C tăng ~120đ
```

#### Bisection Method for IV

```
Mục tiêu: Tìm σ sao cho Black_Scholes(S, K, T, r, σ) = C_market

Pseudo-code:
  σ_min = 0.01
  σ_max = 2.00
  tolerance = 0.0001

  WHILE |σ_max - σ_min| > tolerance:
    σ_mid = (σ_min + σ_max) / 2
    C_calc = Black_Scholes(S, K, T, r, σ_mid)

    IF |C_calc - C_market| < tolerance:
      RETURN σ_mid

    IF C_calc > C_market:
      σ_max = σ_mid
    ELSE:
      σ_min = σ_mid

  RETURN σ_mid
```

### 8.2 Wireframes/Mockups

**Wireframe 1: Bảng giá CW đầy đủ**

```
+-------------------------------------------------------------------------------------------+
|  BẢNG GIÁ CHỨNG QUYỀN                                            [Export Excel]           |
+-------------------------------------------------------------------------------------------+
| Search: [___________]  Filter by Issuer: [All ▼]  Filter by Underlying: [All ▼]          |
+-------------------------------------------------------------------------------------------+
| Mã CW ↕ | Giá TT↕ | Δ% ↕ | KL↕  | Giá LT↕ | Chênh lệch↕ | Hòa vốn↕ | Đòn bẩy↕ | IV(%)↕ |
|---------|---------|------|------|---------|-------------|----------|---------|--------|
| CACB2505| 1.350🔴 |+0.7% | 65.3K| 1.320   | +0.030 🔴   | 25.37    | 8.50    | 25.5%  |
| CACB2502| 2.060🟢 |-1.9% | 38.3K| 2.100   | -0.040 🟢   | 26.81    | 7.20    | 28.2%  |
| CVIC2506| 0.920🔴 |+1.1% | 95.0K| 0.900   | +0.020 🔴   | 22.84    | 12.30   | 30.1%  |
| ...     | ...     | ...  | ...  | ...     | ...         | ...      | ...     | ...    |
+-------------------------------------------------------------------------------------------+
| Delta↕ | Theta↕      | Vega↕  | Strike↕ | TLCĐ↕ | TTM↕        | Issuer↕ | Thao tác      |
|--------|-------------|--------|---------|-------|-------------|---------|---------------|
| 0.65   | -50 VNĐ/ngày| 120    | 23.40   | 2     | 45 ngày ⚪  | BSC     | [MUA] [BÁN]   |
| 0.58   | -42 VNĐ/ngày| 135    | 22.56   | 2     | 120 ngày ⚪ | SSI     | [MUA] [BÁN]   |
| 0.72   | -65 VNĐ/ngày| 98     | 21.00   | 1     | 15 ngày 🟡 | VND     | [MUA] [BÁN]   |
| ...    | ...         | ...    | ...     | ...   | ...         | ...     | ...           |
+-------------------------------------------------------------------------------------------+
| Trang 1 / 5                                                          [< Trước] [Tiếp >]  |
+-------------------------------------------------------------------------------------------+
```

**Wireframe 2: Tab Chứng quyền trên Sức khỏe CP**

```
+-------------------------------------------------------------------------------------------+
|  STB - Ngân hàng TMCP Sài Gòn Thương Tín                          Giá: 24.30 (+1.2%)     |
+-------------------------------------------------------------------------------------------+
|  [Tổng quan] [Phân tích] [Tin tức] [Tài chính] [Chứng quyền ⭐NEW]                       |
+-------------------------------------------------------------------------------------------+
|  CHỨNG QUYỀN LIÊN QUAN ĐẾN STB                                    [Xem đầy đủ bảng giá →]|
+-------------------------------------------------------------------------------------------+
| Mã CW    | Giá TT | Thay đổi   | KL   | Strike | Gap    | Hòa vốn | GTNT | Issuer | TTM  |
|----------|--------|------------|------|--------|--------|---------|------|--------|------|
| CSTB2505 | 0.850  | +0.02(2.4%)| 120K | 22.50  | +8.0%🟢| 24.20   | 0.30 | VND    | 45🟡 |
| CSTB2508 | 1.200  | -0.01(-0.8%)| 80K | 24.00  | +1.3%🟢| 26.40   | 0.15 | BSC    | 120⚪|
| CSTB2502 | 0.600  | +0.03(5.3%)| 200K | 26.00  | -6.5%🔴| 27.20   | 0.00 | SSI    | 30🟡 |
+-------------------------------------------------------------------------------------------+
|                                                              [< 1 2 3 >] (3 mã CW)        |
+-------------------------------------------------------------------------------------------+

Chú thích:
🟢 ITM (In-the-money) - CW có giá trị nội tại
🔴 OTM (Out-of-the-money) - CW chưa có giá trị nội tại
⚪ TTM > 30 ngày (an toàn)
🟡 TTM < 30 ngày (cảnh báo time decay)
```

**Wireframe 3: Tooltip mẫu**

```
+-------------------------------------------------------------------------------------------+
|  Implied Volatility (IV) ⓘ ← Hover vào đây                                               |
+-------------------------------------------------------------------------------------------+
|  📊 Biến động hàm ý (Implied Volatility)                                                  |
|                                                                                           |
|  Ý nghĩa:                                                                                 |
|  Mức độ biến động kỳ vọng của thị trường đối với cổ phiếu cơ sở. IV cao = thị trường     |
|  kỳ vọng giá cổ phiếu sẽ biến động mạnh trong thời gian tới.                             |
|                                                                                           |
|  Cách sử dụng:                                                                            |
|  • IV cao (>40%): CW đắt hơn, phù hợp nếu dự đoán biến động lớn                           |
|  • IV thấp (<20%): CW rẻ hơn, cơ hội mua nếu dự đoán thị trường sẽ biến động              |
|  • So sánh IV với biến động lịch sử để đánh giá đắt/rẻ                                    |
|                                                                                           |
|  Ví dụ: IV = 25.5% nghĩa là thị trường kỳ vọng STB biến động khoảng ±25.5%/năm           |
+-------------------------------------------------------------------------------------------+
```

### 8.3 Test Scenarios

**Test Case 1: Tính toán Giá lý thuyết chính xác**

```
Scenario: Verify Black-Scholes calculation accuracy
Given:
  S = 24.30, K = 23.40, T = 45/365 = 0.123, r = 0.025, C_market = 1.350
When:
  System calculates IV and Theoretical Price
Then:
  IV should be approximately 25-30%
  Theoretical Price should be within ±2% of C_market (1.350)
  Chênh lệch should be calculated correctly
```

**Test Case 2: Xử lý CW đã đáo hạn**

```
Scenario: Handle expired warrants
Given:
  CW CACB2401 with Expiry_Date = 2025-01-15
  Current_Date = 2025-01-16
When:
  System loads bảng giá CW
Then:
  CW CACB2401 should NOT appear in the table (hidden)
  TTM = 0, status = "Expired"
```

**Test Case 3: IV không converge**

```
Scenario: IV calculation fails to converge
Given:
  S = 24.30, K = 23.40, T = 0.123, r = 0.025, C_market = 0.01 (bất thường thấp)
When:
  System calculates IV using Bisection (100 iterations)
Then:
  IV = "N/A"
  Theoretical Price = "N/A"
  Delta, Theta, Vega = "N/A"
  Error logged: "IV không converge cho CW CACB2505"
```

### 8.4 Assumptions & Dependencies

**⚠️ Assumptions:**

1. **Lãi suất phi rủi ro cố định**: r = 2.5% cho tất cả CW. Thực tế có thể thay đổi theo kỳ hạn, nhưng đơn giản hóa trong phase 1.

2. **Không tính cổ tức (dividend)**: Công thức Black-Scholes chuẩn không tính cổ tức. Nếu CKCS trả cổ tức, cần điều chỉnh công thức → defer sang phase 2.

3. **European Call Option**: CW tại VN thường là European style (chỉ exercise vào ngày đáo hạn). Nếu có American style CW, cần mô hình khác.

4. **Thị trường hiệu quả**: Giả định không có chi phí giao dịch, không có arbitrage, thị trường liquid. Thực tế CW VN có thể kém liquid.

5. **Bisection method đủ nhanh**: Giả định 100 iterations đủ để IV converge trong 99% trường hợp. Nếu performance issue, cân nhắc Newton-Raphson.

**Dependencies:**

| Dependency | Mô tả | Owner | Status |
|------------|-------|-------|--------|
| Real-time price feed | Giá CKCS và giá CW real-time | Data Team | Available |
| CW Master Data | Thông tin K, TLCĐ, Expiry, Underlying | Data Team | Available |
| Black-Scholes library | Thư viện tính toán (VD: scipy, quantlib) | Dev Team | To be confirmed |
| Cache infrastructure | Redis hoặc in-memory cache | DevOps | Available |
| Monitoring & Alerting | Grafana, Prometheus cho performance monitoring | DevOps | Available |

### 8.5 Risks & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| IV không converge cho nhiều CW (do giá bất thường) | Medium | Medium | Validate input data quality, log warnings, có thể dùng Historical Volatility làm fallback |
| Performance issue khi tính toán cho >100 CW real-time | Medium | High | Implement caching (5-10s), optimize calculation, consider async processing |
| Công thức Black-Scholes không chính xác do thiếu tính cổ tức | Low | Medium | Document assumption rõ ràng, defer dividend adjustment sang phase 2 |
| Data quality issue (giá CKCS, giá CW missing/incorrect) | Medium | High | Implement robust validation, fallback to "N/A", alert Data team |
| Nhà đầu tư hiểu sai tooltip, ra quyết định sai | Medium | Medium | Review tooltip với Compliance, có disclaimer rõ ràng |

### 8.6 Glossary (Bổ sung)

| Thuật ngữ | Giải thích đầy đủ |
|-----------|-------------------|
| N(x) | Cumulative Distribution Function (CDF) của phân phối chuẩn. Xác suất biến ngẫu nhiên chuẩn ≤ x. |
| N'(x) | Probability Density Function (PDF) của phân phối chuẩn. N'(x) = (1/√(2π)) × e^(-x²/2). |
| Bisection Method | Phương pháp tìm nghiệm bằng chia đôi khoảng. Đơn giản, ổn định nhưng hội tụ chậm hơn Newton-Raphson. |
| Newton-Raphson | Phương pháp tìm nghiệm dùng đạo hàm. Hội tụ nhanh nhưng phức tạp, cần tính Vega. |
| Time Decay | Hiện tượng giảm giá của quyền chọn theo thời gian, do phần giá trị thời gian giảm dần về 0 khi đến đáo hạn. |
| Intrinsic Value | Giá trị nội tại - giá trị nếu exercise ngay. GTNT = max(0, (S-K)/TLCĐ) cho Call. |
| Time Value | Giá trị thời gian = Giá CW - Giá trị nội tại. Phần giá trị do kỳ vọng giá CKCS còn có thể tăng thêm. |
| Deep ITM | CW rất sâu trong tiền (S >> K). Delta → 1, Theta nhỏ. |
| Deep OTM | CW rất sâu ngoài tiền (S << K). Delta → 0, giá CW rất thấp. |

---

## KẾT LUẬN

Tài liệu BRD này cung cấp đầy đủ thông tin cho việc phát triển tính năng **Bảng Phân Tích Giá Chứng Quyền** tại VNDIRECT. Các nhóm phát triển có thể bắt đầu thiết kế kỹ thuật, implement mô hình Black-Scholes, và xây dựng UI dựa trên yêu cầu chi tiết trong tài liệu.

**Next Steps:**
1. Tech Lead review technical feasibility (đặc biệt phần IV calculation)
2. Quant Team confirm công thức và assumptions
3. Data Team confirm data availability và quality
4. Dev Team estimate effort và tạo implementation plan
5. QA Team xây dựng test plan chi tiết
6. Product Owner approve và prioritize vào sprint

**Contact:**
- Thắc mắc về nghiệp vụ: Business Analyst
- Thắc mắc về công thức: Quant Team Lead
- Thắc mắc về dữ liệu: Data Team Lead

---

**END OF DOCUMENT**
