# MSA: Resampling Methods Exploration

Dự án nghiên cứu và thực nghiệm các phương pháp **Resampling** (Tái lấy mẫu) trong thống kê và học máy. Tập trung vào việc ước lượng sai số, kiểm định giả thuyết và đánh giá mô hình.


## 📁 Cấu trúc dự án
```text
├── 1_Estimation_Lab.ipynb    # Ước lượng Mean/Median (Jackknife vs Bootstrap)
├── 2_Hypothesis_Testing.ipynb # Kiểm định giả thuyết (Permutation Test vs T-Test)
├── 3_Model_Selection.ipynb    # Đánh giá độ ổn định mô hình (K-Fold vs LOOCV)
├── Idea Thực nghiệm.md        # Tài liệu ý tưởng ban đầu
├── modules/                  # Logic lõi thuật toán (.py)
├── utils/                    # Công cụ vẽ biểu đồ (.py)
├── data/                     # Thư mục chứa các tệp dữ liệu thí nghiệm
└── README.md                 # Hướng dẫn sử dụng
```

## 🛠 Hướng dẫn sử dụng
### Chạy trên Google Colab
1. Upload trực tiếp các tệp `.ipynb` lên Colab.
2. Nhấn **Run All**. Ô code **"KHÔI PHỤC HỆ THỐNG"** sẽ tự động chuẩn bị folder `modules`, `utils` và dữ liệu CSV cho bạn.

### Chạy trên máy bộ (Local)
1. Clone repository:
   ```bash
   git clone https://github.com/Bubusr/MSA-Resampling-Methods.git
   cd MSA-Resampling-Methods
   ```
2. Cài đặt thư viện:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn requests gdown
   ```

## 📊 Phương pháp triển khai
- **Estimation**: Tính toán bias, variance, SE. Chứng minh sự khác biệt giữa Jackknife và Bootstrap.
- **Hypothesis Testing**: Sử dụng Permutation test để kiểm định p-value mà không phụ thuộc vào giả định phân phối.
- **Model Evaluation**: So sánh phương sai của các phương pháp đánh giá mô hình (Single Split vs K-Fold CV).
