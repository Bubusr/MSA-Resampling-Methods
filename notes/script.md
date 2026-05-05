# Kịch bản Trình bày: Thực nghiệm các phương pháp Resampling (Resampling Methods)

**Mục tiêu chung:** Giúp người nghe/người xem thấy được sức mạnh thực sự và lý do tại sao các phương pháp Resampling lại rất đáng dùng trong phân tích dữ liệu thực tế.

---

## 1. Phần Mở Đầu (Intro)

* **Hình ảnh (Visual):** Slide tiêu đề "Sức mạnh của Resampling Methods" hoặc hiển thị cấu trúc tổng thể của dự án (`README.md`).
* **Lời thoại (Audio):** 
  "Xin chào các bạn. Hôm nay, chúng ta sẽ cùng đi sâu vào các phương pháp Resampling (lấy mẫu lại) thông qua các thực nghiệm cụ thể. Trong thực tế phân tích dữ liệu, các giả định của thống kê truyền thống thường bị vi phạm. Mục tiêu của buổi trình bày hôm nay là chứng minh bằng thực tế: tại sao Resampling lại thực sự đáng dùng và giúp chúng ta đưa ra những quyết định thống kê chính xác hơn.
  
  Chúng ta sẽ cùng nhau thực hiện 3 thí nghiệm, mỗi thí nghiệm có một mục đích cụ thể và sử dụng phương pháp riêng, đi kèm với những dataset được cố tình lựa chọn để bộc lộ rõ nhất điểm mạnh của việc sử dụng Resampling so với các phương pháp thông thường."

* **Hình ảnh (Visual):** Slide hiển thị bảng tổng quan 3 thí nghiệm:
  1. Ước lượng (Mean/Median) - Jackknife, Bootstrap.
  2. Kiểm định giả thuyết (Khác biệt 2 nhóm) - Permutation-test.
  3. Đánh giá mô hình (Chọn Model A/B) - Cross-validation.

---

## 2. Thí nghiệm 1: Ước lượng (Estimation Lab)

* **Hình ảnh (Visual):** Mở notebook `experiments/1_Estimation_Lab.ipynb`. Hiển thị phần mô tả phân phối dữ liệu mẫu ban đầu.
* **Lời thoại (Audio) - Đặt vấn đề:** 
  "Thí nghiệm đầu tiên của chúng ta là bài toán Ước lượng. Hãy bắt đầu bằng một câu hỏi thực tế: Nhìn vào bộ dữ liệu thu thập được này, liệu phân phối của nó có đang bị lệch (skewed) hay chứa các giá trị ngoại lai (outliers) hay không? Nếu chỉ tính giá trị trung bình (mean) hoặc trung vị (median) một cách trực tiếp (Naive) trên mẫu hiện có, liệu con số đơn lẻ đó có đủ độ tin cậy để đại diện cho toàn bộ quần thể?"
  
* **Hình ảnh (Visual):** Trình chiếu kết quả của Bootstrap (biểu đồ phân phối của Mean và Median, cùng với giá trị Standard Error - SE). Nhấn mạnh vào sự khác biệt lớn về độ rộng (SE) giữa Mean và Median.
* **Lời thoại (Audio) - Kết quả Bootstrap & Suy luận phát hiện Outlier:**
  "Nhưng hãy nhìn xem điều kỳ diệu gì xảy ra khi chúng ta áp dụng Bootstrap. Bằng cách 'rút ngẫu nhiên có hoàn lại' hàng ngàn lần, chúng ta đã giả lập lại được toàn bộ quần thể. Thay vì một con số vô hồn, Bootstrap cung cấp cho ta một **phân phối** đầy đủ. 
  
  Đặc biệt, thông qua phân phối này, chúng ta có thể **phát hiện và đánh giá tác động của Outlier (dữ liệu ngoại lai)** một cách cực kỳ trực quan! Các bạn hãy nhìn vào sự khác biệt giữa Mean và Median trên màn hình. Do tập dữ liệu chi phí y tế thường chứa những ca bệnh có viện phí khổng lồ (Outlier/độ lệch phải), phân phối Bootstrap của **Mean** dao động rất mạnh, dẫn đến **Sai số chuẩn (SE)** lớn và dải phân phối rộng. 
  Trong khi đó, **Median** (trung vị) miễn nhiễm với outlier, nên phân phối Bootstrap của nó co cụm và ổn định hơn rất nhiều (SE thấp). 
  Như vậy, Resampling không chỉ giúp ta tính được Khoảng tin cậy mà không cần công thức toán học, mà nó còn là 'chiếc kính lúp' soi ra sự bất thường của dữ liệu. Từ đó ta đi đến quyết định thực tế: Trong trường hợp này, dùng Median làm đại diện trung tâm sẽ an toàn và chính xác hơn Mean rất nhiều!"

* **Góc Kinh Nghiệm (Slide phụ trợ): 4 Trường Hợp Chẩn Đoán Nhanh Dữ Liệu Bằng Bootstrap**
  Thông qua việc so sánh phân phối Bootstrap giữa Mean và Median, chúng ta có thể chẩn đoán bộ dữ liệu theo logic "Nếu - Thì" sau:
  
  1. **Trường hợp 1: Dữ liệu phân phối chuẩn, đối xứng (Không có Outlier)**
     - **NẾU:** Phân phối Mean và Median gần như trùng khớp, và SE(Mean) ≈ SE(Median).
     - **THÌ:** Dữ liệu đối xứng, không nhiễu bởi cực trị. 👉 Dùng Mean là tối ưu.

  2. **Trường hợp 2: Dữ liệu lệch phải (Có High-value Outliers)** *(Như dữ liệu Medical Charges)*
     - **NẾU:** Phân phối Mean dịch sang phải so với Median, và SE(Mean) >> SE(Median).
     - **THÌ:** Tập dữ liệu bị lệch phải, chứa Outlier giá trị rất cao. 👉 Bắt buộc dùng Median.

  3. **Trường hợp 3: Dữ liệu lệch trái (Có Low-value Outliers)**
     - **NẾU:** Phân phối Mean dịch sang trái so với Median, và SE(Mean) >> SE(Median).
     - **THÌ:** Tập dữ liệu bị lệch trái, chứa Outlier giá trị cực kỳ thấp. 👉 Bắt buộc dùng Median.

  4. **Trường hợp 4: Dữ liệu phân phối phân cụm / Đa đỉnh (Bimodal)**
     - **NẾU:** Phân phối Median nứt thành 2 đỉnh hoặc rải rác, và SE(Median) > SE(Mean).
     - **THÌ:** Dữ liệu có thể bị phân cụm (ví dụ thiếu khúc giữa). 👉 Cần vẽ Histogram để kiểm tra và phân tích tách rời.

---

## 3. Thí nghiệm 2: Kiểm định giả thuyết (Hypothesis Testing)

* **Hình ảnh (Visual):** Chuyển sang notebook `experiments/2_Hypothesis_Testing.ipynb`. Hiển thị biểu đồ phân phối p-value, so sánh với T-test.
* **Lời thoại (Audio):**
  "Tiếp theo là Thí nghiệm số 2: Kiểm định giả thuyết. Bài toán đặt ra là kiểm tra sự khác biệt giữa hai nhóm dữ liệu. Thông thường, mọi người sẽ nghĩ ngay đến T-test. Tuy nhiên, T-test dựa trên những giả định chặt chẽ về phân phối chuẩn của dữ liệu.
  
  Để khắc phục điều này, chúng ta sử dụng **Permutation test** (được triển khai trong `modules/testing.py`). Thay vì dựa vào các phân phối lý thuyết, phương pháp này liên tục hoán vị ngẫu nhiên nhãn của hai nhóm dữ liệu để xây dựng lên một phân phối thực tế của kiểm định. Cách tiếp cận 'không tham số' (non-parametric) này giúp kết quả tính toán p-value đáng tin cậy hơn rất nhiều, ngay cả khi dữ liệu bất thường và không thỏa mãn điều kiện của T-test."

---

## 4. Thí nghiệm 3: Đánh giá mô hình (Model Selection)

* **Hình ảnh (Visual):** Chuyển đến notebook `experiments/3_Model_Selection.ipynb`. Hiển thị kết quả khi chạy train-test split thông thường với các random seed khác nhau (ví dụ: seed 1 thì Model A tốt hơn, seed 2 thì Model B lại tốt hơn).
* **Lời thoại (Audio) - Đặt vấn đề:**
  "Thí nghiệm cuối cùng đưa chúng ta đến bài toán Lựa chọn mô hình (Model Selection). Giả sử chúng ta có hai mô hình A và B. Nếu chỉ chia tập train-test một lần duy nhất theo cách thông thường, kết quả sẽ rất rủi ro. Như trên màn hình, sự biến động là quá lớn: với cách chia dữ liệu này, Model A trông có vẻ tốt hơn; nhưng chỉ cần đổi random seed, Model B lại lật ngược tình thế. Chúng ta hoàn toàn bế tắc trong việc quyết định xem mô hình nào mới thực sự tốt!"

* **Hình ảnh (Visual):** Trình chiếu kết quả chạy **10-Fold Cross-validation** (từ `modules/evaluation.py`), đặc biệt nhấn mạnh vào biểu đồ hộp (boxplot) và các con số cụ thể về Độ chính xác trung bình (Accuracy) và độ lệch chuẩn (Std/Variance).
* **Lời thoại (Audio) - Phương pháp & Quyết định cuối cùng:**
  "Để phá vỡ thế bế tắc đó, chúng ta áp dụng Resampling thông qua **Cross-validation**. Bằng cách lặp lại quá trình huấn luyện và kiểm thử 10 lần trên các tập dữ liệu con khác nhau (10-Fold), yếu tố may rủi được loại bỏ hoàn toàn.
  
  Và đây là phần kết luận trực tiếp dựa trên những con số cụ thể: 
  Thứ nhất, về độ chính xác trung bình, mô hình **Logistic Regression** đạt **77.58%**, cao hơn so với **Decision Tree** (chỉ đạt **75.28%**). 
  Thứ hai, và cũng là quan trọng nhất, khi nhìn vào độ lệch chuẩn (thể hiện độ biến động), Logistic Regression chỉ dao động quanh mức **$\pm$ 4.11%**, trong khi Decision Tree dao động lên tới **$\pm$ 6.89%**. Biểu đồ hộp (boxplot) cũng trực quan hóa rõ ràng dải kết quả của Logistic Regression hẹp và tập trung hơn rất nhiều.
  
  Điều này chứng minh bằng số liệu thực tế rằng: Logistic Regression không chỉ dự đoán chính xác hơn mà còn cực kỳ ổn định, ít rủi ro bị 'overfit' trên dữ liệu mới. Dựa trên bằng chứng vững chắc này, chúng ta hoàn toàn tự tin chốt **Logistic Regression** làm mô hình cuối cùng để triển khai."

* **Hình ảnh (Visual):** Slide đặt câu hỏi Q&A "Tại sao Decision Tree lại thua?" và cách khắc phục.
* **Lời thoại (Audio) - Mở rộng:**
  "Sẽ có một câu hỏi vô cùng thực tế được đặt ra ở đây: Tại sao với dữ liệu dạng bảng chứa nhiều biến phân loại (categorical) như Bank Marketing, Decision Tree lại lép vế?
  Lý do thứ nhất là do bộ dữ liệu này có chứa đặc trưng mang tính tuyến tính quyết định rất mạnh (như thời lượng cuộc gọi). Lý do thứ hai, bản chất Logistic Regression là một mô hình toàn cục, đơn giản và ít nhạy cảm với nhiễu dữ liệu hơn. Nên khi chịu phép thử Cross-Validation, tính ổn định của nó đã phát huy sức mạnh.
  
  Vậy nếu muốn Decision Tree làm tốt hơn, ta phải tiền xử lý dữ liệu thế nào? Khác với Logistic Regression, cây quyết định sẽ bị 'nhầm lẫn' nếu ta ép các biến phân loại thành số thứ tự (Label Encoding). Thay vào đó, chúng ta phải sử dụng **One-Hot Encoding** để cây phân nhánh chính xác. Hơn nữa, ta cần sử dụng GridSearch để tìm độ sâu (`max_depth`) tối ưu, hoặc tốt nhất là nâng cấp hẳn lên mô hình tập hợp như **Random Forest** để triệt tiêu phương sai cao vốn có của một cây quyết định đơn lẻ."


## 5. Tổng kết (Outro)

* **Hình ảnh (Visual):** Quay lại Slide tổng kết hoặc hiển thị cây thư mục dự án (`modules`, `utils`, `experiments`).
* **Lời thoại (Audio):**
  "Như vậy, qua 3 thí nghiệm thực tiễn: từ Ước lượng, Kiểm định giả thuyết, cho đến Lựa chọn mô hình, chúng ta đã thấy rõ được giá trị to lớn của các phương pháp Resampling. Chúng giúp phân tích trở nên mạnh mẽ, linh hoạt và ít phụ thuộc vào các giả định toán học cứng nhắc.
  
  Toàn bộ mã nguồn, cấu trúc thư mục rõ ràng từ các logic tính toán trong thư mục `modules/` (estimation, testing, evaluation) đến các hàm hỗ trợ trực quan trong `utils/` đều được chia sẻ trong dự án này. Các bạn hoàn toàn có thể chạy lại các notebook để tự mình kiểm chứng.
  
  Cảm ơn các bạn đã theo dõi!"
