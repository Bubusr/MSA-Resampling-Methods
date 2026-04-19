import numpy as np

def calc_se(distribution):
    """
    Tính Standard Error (SE) từ phân phối của estimator.
    """
    # Đối với Jackknife, công thức SE khác một chút, 
    # nhưng nếu đây là phân phối từ Bootstrap, ta dùng np.std.
    # Để tổng quát cho "phân phối", ta dùng độ lệch chuẩn của mảng.
    return np.std(distribution, ddof=1)

def calc_ci(distribution, confidence=0.95):
    """
    Tính Khoảng tin cậy (CI) từ phân phối của estimator bằng phương pháp Percentile.
    """
    alpha = 1 - confidence
    lower_bound = np.percentile(distribution, (alpha / 2) * 100)
    upper_bound = np.percentile(distribution, (1 - alpha / 2) * 100)
    return lower_bound, upper_bound
