___
- Mục tiêu chung: làm cho gười đọc thấy resampling thực sự đáng dùng
- Cần có 2 yếu tố:
	- **Có baseline “không resampling” rõ ràng để so sánh**
	- **Mỗi phương pháp thắng trong một bối cảnh cụ thể**
- Tổng quan: chia thành 3 nhóm bài toán chính

| Nhóm                   | Mục tiêu                      | Phương pháp nổi bật  |
| ---------------------- | ----------------------------- | -------------------- |
| Ước lượng (Estimation) | Ước lượng bias/variance       | Jackknife, Bootstrap |
| Kiểm định giả thuyết   | Test sự khác biệt             | Permutation test     |
| Đánh giá mô hình       | Estimate generalization error | Cross-validation     |
- Mỗi nhóm sẽ có:
	- Dataset riêng (cố tình chọn để lộ điểm mạnh)
	- So sánh giữa việc có và không Resampling method
- Folder source code: 
	- Cấu trúc source code (các hàm utils, các hàm vẽ biểu đồ, các file logic bên trong resampling là file .py chạy riêng + mô tả hàm trong comment)
	- Cả pipeline cho mỗi thí nghiệm là 1 file .ipynb (người dùng muốn làm thí nghiệm thì chạy file tương ứng)
# 1. Ước lượng hiệu quả thuốc (Jackknife vs Bootstrap vs Naive)
___
## 1.1 Mục tiêu + mô tả dataset

Bối cảnh thực tế:
- Một công ty dược thử nghiệm thuốc giảm đau mới.
	- Lấy 30 bệnh nhân
	- Đo mức giảm đau (thang điểm 0–10)

👉 Câu hỏi: “Thuốc có hiệu quả trung bình bao nhiêu? Có đáng tin không?”
Mục tiêu là chứng minh:
- Naive estimate → sai lệch / không có CI
- Jackknife → tốt với estimator đơn giản
- Bootstrap → mạnh hơn với estimator phức tạp

Dataset: [Medical Cost Personal dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance) (chi phí điều trị → proxy cho hiệu quả điều trị)
- Mô tả dataset (kích thước, ý nghĩa mỗi cột)
- Dựa vào đặc điểm nào mà chọn dataset này?
- CODE: đoạn code vẽ biểu đồ bằng matplotlib để thể hiện đặc điểm đó
## 1.2 Tiến hành thí nghiệm

### Case A: Estimate mean
- Mean là đại lượng như thế nào?
- Ta kỳ vọng gì ở kết quả?
- Naive: dùng sample mean
	- Giải thích các bước làm
	- CODE và kết quả tương ứng
- Jackknife: leave-one-out mean
	- Giải thích các bước làm
	- CODE và kết quả tương ứng
- Bootstrap: resample 1000 lần
	- Giải thích các bước làm
	- CODE và kết quả tương ứng

- So sánh: Bias, Variance, Confidence Interval 
=> Rút ra nhận xét (về tính chất tập dữ liệu, về đời sống), vẽ biểu đồ nếu cần

### Case B - Estimate median
- Median là đại lượng như thế nào?
- Ta kỳ vọng gì ở kết quả?
- Naive: dùng sample mean
	- Giải thích các bước làm
	- CODE và kết quả tương ứng
- Jackknife: leave-one-out mean
	- Giải thích các bước làm
	- CODE và kết quả tương ứng
- Bootstrap: resample 1000 lần
	- Giải thích các bước làm
	- CODE và kết quả tương ứng
- Rút ra nhận xét: Jackknife hoạt động kém (median không smooth), Bootstrap hoạt động tốt + CODE vẽ biểu đồ để chứng minh (vd như distribution estimator bằng histrogram)
- Rút ra nhận xét trong đời sống

# 2. Kiểm định thuốc mới (Permutation test)
___
## 2.1 Mục tiêu + mô tả dataset

- Bối cảnh thực tế: so sánh:
	- Nhóm A: thuốc cũ
	- Nhóm B: thuốc mới
👉 Câu hỏi: “Thuốc mới có thực sự tốt hơn không?”

- Nhắc lại về toàn bộ quy trình kiếm định giả thuyết thường gặp
- Mục tiêu là Chứng minh: t-test thất bại khi giả định sai, trong khi đó Permutation test vẫn đúng
- Dataset: [Covid-19 Clinical Trial dataset](https://www.kaggle.com/datasets/parulpandey/covid19-clinical-trials-dataset)
	-  Mô tả dataset (kích thước, ý nghĩa mỗi cột, mỗi nhãn)
	- Dựa vào đặc điểm nào mà chọn dataset này?
	- CODE: đoạn code vẽ biểu đồ bằng matplotlib để thể hiện đặc điểm đó
- Metric: p-value, false positive rate (giải thích ngắn gọn tại sao lại dùng 2 metrics này)
- Ta kỳ vọng gì ở kết quả? (Khi data “đẹp” → giống nhau; Khi data “bẩn” → permutation đáng tin hơn....)
## 2.2 Tiến hành thí nghiệm

- So sánh:

|Method|Giả định|
|---|---|
|t-test|normal + equal variance|
|permutation|không cần giả định|
- Đặt giả thuyết H_0
- Mô tả quá trình permutation-test từng bước (chia nhãn, xáo lại...)
- Đi kèm CODE và kết quả tính toán
- Vẽ đồ thị mình họa
- Rút ra nhận xét => chấp nhận hay bác bỏ giả thuyết H_0

# 3. Đánh giá mô hình (Cross-Validation)
___
## 3.1 Mục tiêu & mô tả dataset
- Bạn muốn dự đoán: Khách hàng có mua sản phẩm hay không. So sánh:
	- Model A: Logistic Regression
	- Model B: Decision Tree
👉 Câu hỏi: “Model nào tốt hơn?”
- Chứng minh: 
	- Train/test split → không ổn định
	- CV → ổn định hơn
- Dataset: [Bank Marketing dataset](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset)
	- Mô tả dataset (kích thước, ý nghĩa mỗi cột, mỗi nhãn)
	- Dựa vào đặc điểm nào mà chọn dataset này?
	- CODE: đoạn code vẽ biểu đồ bằng matplotlib để thể hiện đặc điểm đó
- Metric: Accuracy variance, Bias estimate (giải thích sơ nó là gì, tại sao dùng)
-  Ta kỳ vọng gì ở kết quả? 
	- (Single split:kết quả “random”; K-fold: ổn định hơn rõ rệt, LOOCV:  đôi khi overfit) 
	- (Một lần split: Model A > Model B, Nhưng CV dô cái thì Model B ổn định hơn => Model “thắng” ban đầu thực ra chỉ ăn may)
## 3.2 Tiến hành thí nghiệm

| Method           | Đặc điểm                    |
| ---------------- | --------------------------- |
| Single split     | variance cao                |
| K-fold CV        | ổn định                     |
| Leave one out CV | bía thấp nhưng variance cao |
- tiến hành thí nghiệm giữa 3 kiểu này => tính các tham số => vẽ biểu đồ nếu cần
- Rút ra nhận xét (trong phạm vi dữ liệu, trong đời sống nếu đc)

## 4. Kết luận
___

|Phương pháp|Khi nào dùng|Insight chính|
|---|---|---|
|Jackknife|estimator đơn giản|Ước lượng bias|
|Bootstrap|mọi trường hợp|Ước lượng phân phối|
|Permutation|test giả thuyết|Không cần giả định|
|Cross-validation|ML|Đánh giá ổn định|
