import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def set_aesthetic_style():
    """Thiết lập style chuyên nghiệp cho biểu đồ."""
    sns.set_theme(style="whitegrid")
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['figure.figsize'] = (10, 6)

def plot_resampling_dist(data, original_stat, resampling_stats, title="Resampling Distribution"):
    """Vẽ biểu đồ phân phối với dải tin cậy và giá trị gốc."""
    set_aesthetic_style()
    plt.figure()
    
    # Vẽ phân phối
    sns.histplot(resampling_stats, kde=True, color="skyblue", alpha=0.6, label="Resampled Distribution")
    
    # Vẽ giá trị gốc
    plt.axvline(original_stat, color="red", linestyle="--", linewidth=2, label=f"Original Stat: {original_stat:.4f}")
    
    # Tính Confidence Interval (95%)
    ci_lower = np.percentile(resampling_stats, 2.5)
    ci_upper = np.percentile(resampling_stats, 97.5)
    plt.axvline(ci_lower, color="green", linestyle=":", label=f"95% CI Lower: {ci_lower:.4f}")
    plt.axvline(ci_upper, color="green", linestyle=":", label=f"95% CI Upper: {ci_upper:.4f}")
    
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_bias_comparison(methods, bias_values, var_values, title="Bias and Variance Comparison"):
    """Vẽ sơ đồ cột so sánh sai lệch và phương sai giữa các phương pháp."""
    set_aesthetic_style()
    fig, ax1 = plt.subplots()

    color_bias = 'tab:blue'
    ax1.set_xlabel('Methods')
    ax1.set_ylabel('Absolute Bias', color=color_bias)
    ax1.bar(methods, [abs(b) for b in bias_values], color=color_bias, alpha=0.6, label='Bias')
    ax1.tick_params(axis='y', labelcolor=color_bias)

    ax2 = ax1.twinx()
    color_var = 'tab:red'
    ax2.set_ylabel('Variance', color=color_var)
    ax2.plot(methods, var_values, color=color_var, marker='o', linewidth=2, label='Variance')
    ax2.tick_params(axis='y', labelcolor=color_var)

    plt.title(title)
    fig.tight_layout()
    plt.show()
