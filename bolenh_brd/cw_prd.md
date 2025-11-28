Trading Platform / 8. BRD bổ sung bảng thông tin phân tích giá Chứng quyền [Updated Sept 12](/wiki/spaces/TP/history/127008879)
- ![Bach Nguyen Tung (IPAS_DBA)](/wiki/aa-avatar/712020:a3a3ddbf-153c-4f50-b358-11bb693204fe)

[Edit](/wiki/spaces/TP/pages/edit-v2/127008879)Share Copy link More actions 

# 8. BRD bổ sung bảng thông tin phân tích giá Chứng quyền

![image](/wiki/aa-avatar/712020:a3a3ddbf-153c-4f50-b358-11bb693204fe)By Bach Nguyen Tung (IPAS_DBA) 11 min 4 Add a reaction **I, INSIGHT**

1. **Nhận định về Bảng giá Chứng quyền của VNDIRECT hiện tại**: 
Bảng giá Chứng quyền hiện tại của VNDIRECT chỉ dừng ở mức hiển thị giao dịch cơ bản (mã, giá khớp, khối lượng, % thay đổi) tương tự cổ phiếu, thiếu lớp dữ liệu định giá và rủi ro đặc thù. Điều này làm giảm khả năng nhà đầu tư đánh giá đắt/rẻ, so sánh lựa chọn và quản trị time decay. 

- **Thiếu thông tin tham số kỹ thuật**: 

- Bảng giá hiện tại chỉ hiển thị các thông tin giao dịch cơ bản: mã CW, giá khớp lệnh, khối lượng, thay đổi giá 

- Hoàn toàn thiếu các chỉ số phân tích quan trọng như: Giá lý thuyết, Biến động hàm ý (IV), các chỉ số Greeks (Delta, Gamma, Theta, Vega) 

- Không có thông tin về giá hòa vốn, đòn bẩy, hay độ lệch giữa giá thị trường và giá lý thuyết 

- **Trải nghiệm người dùng kém**: 

- Nhà đầu tư không thể đánh giá để lựa chọn Chứng quyền phù hợp với khẩu vị rủi ro và trường phái đầu tư của mình. 

- Thiếu công cụ so sánh và sàng lọc các mã CW theo tiêu chí cụ thể 

- Không có tích hợp với trang phân tích cổ phiếu cơ sở 

=> Các vấn đề hiện tại ảnh hưởng tới **Khách hàng**như sau: 

- Khách hàng buộc phải sử dụng các công cụ bên ngoài (Excel, website khác) để phân tích. 

- Tạo ra rào cản cho việc ra quyết định giao dịch nhanh chóng. 

=> Ảnh hưởng đến **công ty**: 

- Bảng giá Chứng quyền VNDIRECT thiếu thông tin so với đối thủ cạnh tranh, không được đánh giá cao từ phía các nhà đầu tư giao dịch chứng quyền trên thị trường. 

2. **Nhu cầu từ phía Khách hàng giao dịch CW**mong muốn nắm thông tin chuyên sâu về giao dịch chứng quyền như phân tích dưới đây: 

- Khách hàng giao dịch chứng quyền được chia thành 2 tệp khách hàng: 

| Nhóm | Đặc điểm chính | Mục tiêu | Vấn đề gặp phải | Cách họ dùng chỉ số |
| --- | --- | --- | --- | --- |

| Nhóm | Đặc điểm chính | Mục tiêu | Vấn đề gặp phải | Cách họ dùng chỉ số |
| --- | --- | --- | --- | --- |
| KH giao dịch thông thường (Retail / F0–Bán chuyên) | Vốn nhỏ, tần suất vừa, chưa hiểu sâu Greeks | Mua CW ăn biên độ ngắn hoặc cầm đến đáo hạn “nếu đúng xu hướng” | Không biết đắt/rẻ, không rõ cần giá cơ sở tăng tới đâu mới hòa vốn | Cần bộ chỉ số rút gọn, dễ hiểu, có tooltip giáo dục |
| KH giao dịch chuyên nghiệp (Active / Semi-pro) | Theo dõi nhiều mã, so sánh nhanh, xoay vòng vốn | Tối ưu hiệu suất vốn, chọn cấu trúc rủi ro hợp lý, khai thác chênh lệch | Phải xuất Excel / dùng nền tảng khác để lọc & định giá | Dùng full bộ: định giá, Greeks, cấu trúc đòn bẩy, biến động, liquidity micro-structure |

## Phân loại theo chiến lược thời gian nắm giữ

| Chiến lược | Khung thời gian | Trọng tâm quyết định | Chỉ số cốt lõi |
| --- | --- | --- | --- |

| Chiến lược | Khung thời gian | Trọng tâm quyết định | Chỉ số cốt lõi |
| --- | --- | --- | --- |
| Ngắn – Trung hạn (Trading CW | lướt biến động) | Trong ngày → vài tuần | Giá CW hiện tại có đắt/rẻ? Biên độ kỳ vọng vs phí thời gian? Tính thanh khoản ra/vào? |
| Dài hạn (Giữ tới đáo hạn có điều kiện) | 1–3 tháng hoặc đến Expiry | Khả năng đạt Break-even / vượt Strike; rủi ro Time Decay tăng cuối kỳ | Break-even, TTM (Days to Expiry), Intrinsic vs Time Value, Delta (ổn định?), IV (định giá cao quá không?), Premium % |

## Bộ chỉ số tối ưu dành cho KH đề xuất & đối tượng ưu tiên

| STT | Chỉ số | Ý nghĩa | Đối tượng KH sử dụng |
| --- | --- | --- | --- |

| STT | Chỉ số | Ý nghĩa | Đối tượng KH sử dụng |
| --- | --- | --- | --- |
| 1 | Giá lý thuyết | Mốc tham chiếu định giá công bằng theo mô hình toán học, giúp đánh giá CW đắt/rẻ | KH giao dịch thông thường và chuyên nghiệp |
| 2 | Chênh lệch giá lý thuyết | Đo mức độ đắt/rẻ của CW. Dương = đắt, âm = rẻ so với fair value | KH giao dịch thông thường và chuyên nghiệp |
| 3 | Điểm hòa vốn | Giá CKCS cần đạt để CW có lãi khi exercise, quan trọng cho hold-to-expiry | KH giao dịch thông thường |
| 4 | Đòn bẩy hiệu dụng | Đo độ nhạy thực tế của CW với biến động CKCS, có tính xác suất thành công | KH giao dịch thông thường |
| 5 | Implied Volatility | Kỳ vọng biến động của thị trường đối với CKCS, cao = kỳ vọng biến động mạnh | KH giao dịch thông thường |
| 6 | TTM (Time to Maturity) | Thời gian còn lại tính theo năm, ảnh hưởng đến Time Value và Theta decay | KH giao dịch thông thường và chuyên nghiệp |
| 7 | Delta | Tỷ lệ thay đổi giá CW khi CKCS tăng 1đ. Nền tảng cho hedging và đòn bẩy hiệu dụng | KH giao dịch thông thường và chuyên nghiệp |

1. **Thiếu kết nối giữa CKCS và CW**

- Khi Khách hàng quan tâm đến 1 cổ phiếu nhưng khách hàng cũng không biết hoặc không được tổng hợp thông tin của các chứng quyền có liên quan đến cổ phiếu đó. 
Ví dụ Khách hàng quan tâm đến cổ phiếu STB nhưng không biết có CW liên quan 

- Phải tìm kiếm riêng biệt thay vì xem tổng quan tại một nơi 

- CW trên Bảng giá có ít đường dẫn, khó tiếp cận 

1. **Cơ hội từ Kế hoạch Phát hành CW**của VNDIRECT 

- Tháng 09/2025: VNDIRECT sẽ có đợt phát hành CW đầu tiên sau 1 năm tạm dừng 

- Đây là cơ hội tốt để tạo ra một "bộ sản phẩm truyền thông": Phát hành CW + Công cụ phân tích CW. 

- Việc có công cụ phân tích chuyên sâu sẽ hỗ trợ trực tiếp cho việc marketing và bán các sản phẩm CW do VNDIRECT phát hành. 

### II PASSION

Trong các công ty chứng khoán thường xuyên phát hành chứng quyền tại Việt Nam có TCBS và VPBankS cung cấp Bảng giá CW mang nhiều thông tin từ giao dịch cơ bản đến các chỉ số phân tích chuyên sâu cho Khách hàng giao dịch chứng quyền. 

- Hiển thị các chỉ số tính toán sẵn để nhà đầu tư ra quyết định nhanh. 

1. **Bảng giá Chứng quyền TCBS**( [Techcom Securities (TCBS) - Công ty Cổ phần Chứng khoán Kỹ Thương](https://www.tcbs.com.vn/bang-gia-chung-quyen)) 

Open image-20250814-232152.png ![image-20250814-232152.png](blob:https://ipas-tech.atlassian.net/3b02bc3d-51af-4603-8b12-3aae7fd11c53#media-blob-url=true&id=18987fa4-dec8-40d7-a5af-08b81f0eeed5&collection=contentId-127008879&contextId=127008879&mimeType=image%2Fpng&name=image-20250814-232152.png&size=370086&width=2560&height=1068&alt=image-20250814-232152.png)Bảng giá TCBS có các trường thông tin mà VNDIRECT không có như bảng dưới đây: 

| STT | Tên trường | Cách tính | Ý nghĩa |
| --- | --- | --- | --- |

| STT | Tên trường | Cách tính | Ý nghĩa |
| --- | --- | --- | --- |
| 1 | Giá lý thuyết | Tính theo mô hình Black-Scholes: C = S×N(d1) - K×e^(-r×T)×N(d2) | Giá trị hợp lý của chứng quyền theo lý thuyết tài chính |
| 2 | Giá thực hiện | Strike Price từ hợp đồng phát hành | Giá thực hiện quyền của chứng quyền (VD: 23.40, 22.56, 21.98) |
| 3 | TLCĐ | Tỷ lệ chuyển đổi từ hợp đồng | Số lượng cổ phiếu cơ sở tương ứng với 1 chứng quyền |
| 4 | Điểm HV | Giá thực hiện + (Giá CW hiện tại × Tỷ lệ chuyển đổi) | Mức giá của cổ phiếu cơ sở mà tại đó nhà đầu tư sẽ hòa vốn. Đây là một trong những chỉ tiêu quan trọng nhất của chứng quyền |
| 5 | GT nội tại | max(0, (Giá CKCS - Giá thực hiện) / TLCĐ) | Giá trị nội tại (GTNT), hay Giá trị bán chặt, dùng để đo lường mức độ chênh lệch giữa Giá hiện tại của CKCS và Giá thực hiện (Strike Price) của chứng quyền |
| 6 | GTNT/ TLCĐ | Giá trị nội tại / Tỷ lệ chuyển đổi | Giá trị nội tại trên mỗi đơn vị tỷ lệ chuyển đổi |
| 7 | GT thanh toán | (Giá CKCS - Strike Price) / TLCĐ nếu ITM | Giá trị thanh toán khi thực hiện quyền (nếu có lợi). Nếu chênh lệch dương, chứng quyền đang ở trạng thái "trong tiền" (ITM); Nếu chênh lệch bằng 0, chứng quyền ở trạng thái "hòa vốn" (ATM); Nếu chênh lệch âm, chứng quyền ở trạng thái "ngoài tiền" (OTM) |
| 8 | Độ lệch | Giá thị trường - Giá lý thuyết | Chênh lệch giữa giá giao dịch thực tế và giá lý thuyết |
| 9 | Độ lệch* | Độ lệch chuẩn hóa theo thời gian | Độ lệch được điều chỉnh theo thời gian còn lại đến đáo hạn |
| 10 | Đòn bẩy vốn | Giá CKCS / (Giá CW × TLCĐ) | Mức độ khuếch đại của chứng quyền so với cổ phiếu cơ sở |
| 11 | Đòn bẩy HD | Delta × Đòn bẩy vốn | Đòn bẩy hiệu dụng có tính đến độ nhạy Delta |
| 12 | Biến động hàm ý | Tính ngược từ giá thị trường bằng Newton-Raphson | Mức độ biến động được thị trường kỳ vọng (Implied Volatility) |
| 13 | Biến động CKCS | Độ lệch chuẩn của lợi nhuận CKCS trong quá khứ | Biến động lịch sử của cổ phiếu cơ sở (Historical Volatility) |
| 14 | BĐ hàm ý | Biến động hàm ý - Biến động CKCS | Chênh lệch giữa biến động kỳ vọng và biến động lịch sử |
| 15 | Lãi suất hàm ý | Lãi suất được tính ngược từ giá thị trường | Lãi suất phi rủi ro được thị trường kỳ vọng |

1. **Bảng giá Chứng quyền VPBankS**( [VPBank Securities niêm yết 17 mã Chứng quyền có bảo đảm mới!](https://www.vpbanks.com.vn/post/vpbank-securities-niem-yet-chung-quyen-moi)) 

Open image-20250908-062237.png ![image-20250908-062237.png](blob:https://ipas-tech.atlassian.net/404ddc64-2783-49e3-baff-5d47baece88e#media-blob-url=true&id=2dedc261-9370-46ac-bbf1-7bbb7b07a35f&collection=contentId-127008879&contextId=127008879&mimeType=image%2Fpng&name=image-20250908-062237.png&size=293340&width=1920&height=832&alt=image-20250908-062237.png)Bảng giá VPBankS: Có các thông tin **Chỉ số định giá & rủi ro**mà VNDIRECT chưa có như sau: 

| STT | Tên trường | Cách tính | Ý nghĩa |
| --- | --- | --- | --- |

| STT | Tên trường | Cách tính | Ý nghĩa |
| --- | --- | --- | --- |
| 1 | Độ lệch | (Giá thị trường - Giá lý thuyết) / Giá lý thuyết × 100% | Đánh giá CW đang đắt hay rẻ so với giá trị hợp lý. Dương (+) = đắt, Âm (-) = rẻ, giúp nhà đầu tư tránh mua đắt và tìm cơ hội entry tốt |
| 2 | Đòn bẩy vốn | Giá CKCS / (Giá CW × TLCĐ) | Đo lường mức độ khuếch đại rủi ro/lợi nhuận. Cho biết 1 đồng đầu tư CW tương đương bao nhiêu đồng đầu tư CKCS, giúp quản lý rủi ro và position sizing |

### III ACTION

1. Ra mắt Bảng phân tích CW tích hợp trên DBoard với các chỉ số cốt lõi. 

- Tăng chiều sâu khi sử dụng bảng giá Chứng quyền 

- Tăng lượng KH chủ động giao dịch chứng quyền tại VNDIRECT → Tăng lượng phí giao dịch 

2. Bổ sung tab CW trên trang Sức khỏe Cổ phiếu và các tính năng nâng cao. 

- **Khám phá cơ hội mới**: Dễ dàng tìm thấy CW liên quan đến cổ phiếu quan tâm 

- **So sánh hiệu quả**: Xem thông tin CKCS và CW cùng lúc để đưa ra quyết định 

### IV. MINDFULNESS

1. Tính toán và tích hợp bộ thông tin tham số kỹ thuật trên Bảng giá DBoard 

- Mô tả các trường thông tin tham số 

Open image-20250908-090116.png ![image-20250908-090116.png](blob:https://ipas-tech.atlassian.net/860d2dfd-2e89-49cb-b79f-b6c445d786d5#media-blob-url=true&id=1d184bb1-6aa0-473a-8292-65f9111491cb&collection=contentId-127008879&contextId=127008879&mimeType=image%2Fpng&name=image-20250908-090116.png&size=816411&width=5184&height=1673&alt=image-20250908-090116.png)
- **(1) Giá lý thuyết**

- Đây là mức giá hợp lý của một chứng quyền được tính toán dựa trên một mô hình toán học tài chính, cụ thể lựa chọn là mô hình **Black-Scholes**. 

- Mục đích của việc tính giá lý thuyết là để trả lời câu hỏi: "Với tất cả các yếu tố hiện tại (giá cổ phiếu, thời gian, biến động...), chứng quyền này *đáng giá*bao nhiêu?" 

Nhà đầu tư sau đó sẽ so sánh **Giá lý thuyết**này với **Giá thị trường**(giá đang giao dịch) để xác định xem chứng quyền đang bị định giá thấp (rẻ) hay định giá cao (đắt). 

- Nếu `Giá thị trường < Giá lý thuyết`: Chứng quyền có thể đang bị định giá thấp, là một cơ hội mua tiềm năng. 

- Nếu `Giá thị trường > Giá lý thuyết`: Chứng quyền có thể đang bị định giá cao, nhà đầu tư nên cẩn trọng. 

- Công thức 

`-	Công thức Black-Scholes:
	C = S * N(d1) - K * e^(-rT) * N(d2)
	Trong đó:
	d1 = [ln(S/K) + (r + σ²/2) * T] / (σ * √T)
	d2 = d1 - σ * √T
	N(x) là hàm phân phối tích lũy chuẩn (Cumulative Distribution Function).`
- **Các tham số đầu vào**

- **S (Spot Price):**Giá hiện tại của tài sản cơ sở. 

- **K (Strike Price):**Giá thực hiện của chứng quyền. 

- **T (Time to Expiration):**Thời gian còn lại cho đến ngày đáo hạn, được tính bằng năm. 

- **Công thức:**T = (Số ngày còn lại) / 365 ****

- **r (Risk-Free Interest Rate):**Lãi suất phi rủi ro thường là 2.5%. 

- **C (Call Price):**Giá thị trường của chứng quyền mua (có thể là giá khớp lệnh hoặc giá Bid 1, Ask 1 tuỳ theo mục đích). ****

- **σ (Sigma):**Độ biến động hàm ý (Implied Volatility). Đây vừa là một kết quả cần tính, vừa là đầu vào để tính các chỉ số Greek 

- (2) **Chênh lệch giá lý thuyết**: Đo mức độ đặt / rẻ của CW. 

- Công thức: `Chênh lệch giá lý thuyết = Giá thị trường - Giá lý thuyết (Black-Scholes)`

- **(3) Điểm hòa vốn**: Mức giá của tài sản cơ sở để nhà đầu tư hoà vốn tại ngày đáo hạn 

- Giá hoà vốn = Giá thực hiện + Giá CW * Tỷ lệ chuyển đổi 

- **Ví dụ:**Nhà đầu tư mua 1 CW với giá thực hiện 100,000 VND, tỷ lệ chuyển đổi 2:1, giá chứng quyền là 2,000 VND. Điểm hoà vốn sẽ là 104,000 VND. 

- **(4) Đòn bẩy hiệu dụng**: 

- Đây là chỉ số đo lường mức độ khuếch đại của CW so với CKCS. 

- Công thức: 

`Đòn bẩy = Giá CKCS hiện tại / (Giá CW hiện tại * Tỷ lệ chuyển đổi)`
- Ý nghĩa: 

- So sánh hiệu quả vốn 

- Đánh giá rủi ro - lợi nhuận 

- **(5) IV (Implied Volatility):**Độ biến động hàm ý. 

- IV không được tính bằng một công thức trực tiếp. Nó là giá trị **σ (sigma)**khiến cho giá lý thuyết từ mô hình Black-Scholes bằng với giá giao dịch trên thị trường khoặc giá mục tiêu (C) 

- Hệ thống cần sử dụng một phương pháp tìm kiếm lặp (iterative search methor) như **Bisection**để tìm ra giá trị IV. Có thể sử dụng các phương pháp khác như **Newton-Raphson**, **Gradient Descent**khoặc **Bayesian Optimization.**(Có thể trao đổi thêm để chọn ra phương pháp tối ưu nhất) 

- **(7) Delta:**Độ nhạy của giá CW theo tài sản cơ sở. 

- **Mô tả:**Đo lường mức độ thay đổi giá của CW khi giá tài sản cơ sở thay đổi 1 đơn vị. 

- **Công thức:**Delta = N(d1) 

- **Ý nghĩa thực tế:**Delta = 0.6 có nghĩa là nếu giá cổ phiếu cơ sở tăng 100 VND, giá chứng quyền sẽ tăng khoảng 60 VND 

- **(8) Vega (ν)**Độ nhạy của giá CW theo IV ****

- **Mô tả:**Đo lường mức độ thay đổi giá của chứng quyền khi IV thay đổi 1%. 

- **Công thức:**ν = S * N'(d1) * √T 

- **Ý nghĩa thực tế:**Là sự thay đổi giá trên mỗi 1 điểm thay đổi của IV (ví dụ từ 20% lên 21%). Để dễ hiểu cho người dùng, nên hiển thị giá trị này dưới dạng "thay đổi trên mỗi 1% IV" 

- **(9) Theta (Θ)**Mức độ giảm giá của CW theo thời gian. 

- **Mô tả:**Đo lường mức độ giảm giá của chứng quyền khi thời gian trôi qua 1 ngày. 

- **Công thức**(kết quả tính theo năm): 

Θ_năm = - [(S * N'(d1) * σ) / (2 * √T)] - [r * K * e^(-rT) * N(d2)] 

- Chuyển đổi sang ngày (luôn hiển thị theo ngày): 

Θ_ngày = Θ_năm / 365 

- **Ý nghĩa thực tế:**Theta = -50 có nghĩa là mỗi ngày trôi qua, chứng quyền này sẽ mất đi khoản 50 VND giá trị do yếu tố thời gian, với các yếu tố khác không đổi. 

2. Bổ sung Tab chứng quyền trên Sức khỏe cổ phiếu 

- Hiển thị 1 tab chứng quyền đối với các mã Chứng khoán cơ sở làm tài sản cơ sở của các mã Chứng quyền 

- Mô tả giao diện 

Open image-20250826-032305.png ![image-20250826-032305.png](blob:https://ipas-tech.atlassian.net/f72d4a14-cddb-4cce-a8d9-3ee0d7fc1c4d#media-blob-url=true&id=4d0b69f3-d2a5-49bd-a98f-e67128617739&collection=contentId-127008879&contextId=127008879&mimeType=image%2Fpng&name=image-20250826-032305.png&size=141868&width=1083&height=479&alt=image-20250826-032305.png)

- Mô tả dữ liệu bảng 

| Tên Trường | Ý Nghĩa |
| --- | --- |

| Tên Trường | Ý Nghĩa |
| --- | --- |
| Mã CW | Mã định danh chứng quyền (CACB2505, CACB2502) - cho biết loại CW, mã cơ sở và thời hạn |
| Giá thị trường | Giá giao dịch hiện tại của chứng quyền (1.35, 2.06 VNĐ) - cập nhật real-time |
| Thay đổi | Thay đổi giá so với phiên trước (+0.01/+0.7%, -0.04/-1.9%) |
| Khối lượng | Số lượng chứng quyền được giao dịch trong phiên (65.30, 38.30 nghìn CW) |
| Giá thực hiện | Giá cố định để thực hiện quyền mua/bán cổ phiếu cơ sở (21.977, 23.397 VNĐ) |
| Gap | Chênh lệch giữa giá cổ phiếu cơ sở và giá thực hiện (2.32, 0.90) |
| Hòa vốn | Mức giá cổ phiếu cơ sở cần đạt để nhà đầu tư (25.37, 26.81 VNĐ) |
| Giá trị nội tại | "Giá trị thực của CW nếu thực hiện quyền ngay. Dương: ITM, Âm: OTM, Bằng 0: ATM" |
| Tổ chức phát hành | Công ty phát hành chứng quyền (BSC, SSI) - ảnh hưởng đến uy tín và thanh khoản |
| Thời hạn | Ngày đáo hạn và số ngày còn lại (TTM). Ảnh hưởng trực tiếp đến giá trị thời gian của CW- Công thức: (Ngày đáo hạn - Ngày hiện tại) / 365 |
| Thao tác | Các nút chức năng (MUA/BÁN) để thực hiện giao dịch trực tiếp từ bảng |

### V. Launching plan

- Truyền thông khi VND Phát hành các mã Chứng quyền mới 

- Nội dung truyền thông tới Khách hàng: 

- Truyền thông cập nhật thay đổi về tính năng hoặc chính sách sản phẩm cho đối tượng KH đang và đã sử dụng sản phẩm 

## Related content

More info Collapse [2. SRS 7 chỉ số trên Bảng giá Chứng quyền](/wiki/spaces/TP/pages/141328440/2.+SRS+7+ch+s+tr+n+B+ng+gi+Ch+ng+quy+n)2. SRS 7 chỉ số trên Bảng giá Chứng quyền [Trading Platform](/wiki/spaces/TP/overview)Read with this [1. Bổ sung bảng Chứng quyền có cùng CKCS](/wiki/spaces/TP/pages/118620650/1.+B+sung+b+ng+Ch+ng+quy+n+c+c+ng+CKCS)1. Bổ sung bảng Chứng quyền có cùng CKCS [Trading Platform](/wiki/spaces/TP/overview)Read with this [Ver 1 - Tích hợp giải pháp có sử dụng chứng thư số/chữ ký số cho hệ thống giao dịch chứng khoán trực tuyến qua Cổng ký số từ xa trên nền tảng định danh và xác thực điện tử VNeID](/wiki/spaces/VNDgmap/pages/47218856/Ver+1+-+T+ch+h+p+gi+i+ph+p+c+s+d+ng+ch+ng+th+s+ch+k+s+cho+h+th+ng+giao+d+ch+ch+ng+kho+n+tr+c+tuy+n+qua+C+ng+k+s+t+xa+tr+n+n+n+t+ng+nh+danh+v+x+c+th+c+i+n+t+VNeID)Ver 1 - Tích hợp giải pháp có sử dụng chứng thư số/chữ ký số cho hệ thống giao dịch chứng khoán trực tuyến qua Cổng ký số từ xa trên nền tảng định danh và xác thực điện tử VNeID [OPERATION BUSINESS REQUIREMENT (BRD)](/wiki/spaces/VNDgmap/overview)More like this [Quy chế, quy định](/wiki/spaces/TP/pages/18484639/Quy+ch+quy+nh)Quy chế, quy định [Trading Platform](/wiki/spaces/TP/overview)More like this [A - BRD - Xử lý các sự kiện Quyền](/wiki/spaces/KRX/pages/16749983/A+-+BRD+-+X+l+c+c+s+ki+n+Quy+n)A - BRD - Xử lý các sự kiện Quyền [KRX](/wiki/spaces/KRX/overview)More like this [Lệnh TWAP](/wiki/spaces/API/pages/90473530/L+nh+TWAP)Lệnh TWAP [API PUBLIC - OA](/wiki/spaces/API/overview)Read with this Collapse action bar Open Comments Panel Open Details Panel Listen Give feedback on our new layout Rovo Button ![image](https://secure.gravatar.com/avatar/f2fb9b0f19d863d1ddcd50b77a410180?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FB-0.png)Bach Nguyen Tung (IPAS_DBA) Comment in progress - select to continue Add a comment Add labels Add a reaction