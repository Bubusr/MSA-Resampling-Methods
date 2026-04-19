import numpy as np
from utils.metrics import calc_se, calc_ci

def bootstrap(data, stat_func, n_resamples=1000):
    """Thực hiện Bootstrap để tính toán phân phối của một đại lượng thống kê."""
    resampled_stats = []
    n = len(data)
    for _ in range(n_resamples):
        resample = np.random.choice(data, size=n, replace=True)
        resampled_stats.append(stat_func(resample))
    
    resampled_stats = np.array(resampled_stats)
    return {
        'distribution': resampled_stats,
        'mean': np.mean(resampled_stats)
    }

def jackknife(data, stat_func):
    """Thực hiện Jackknife (Leave-one-out) để ước lượng bias và variance."""
    n = len(data)
    jack_stats = []
    for i in range(n):
        resample = np.delete(data, i)
        jack_stats.append(stat_func(resample))
    
    jack_stats = np.array(jack_stats)
    return {
        'estimates': jack_stats,
        'mean': np.mean(jack_stats)
    }

def naive_estimate(data, stat_func):
    """Ước lượng cơ bản không resampling."""
    return stat_func(data)

def run_full_estimation(data, stat_func, n_boot=2000, confidence=0.95):
    """
    Chạy cả Bootstrap và Jackknife để lấy phân phối của các estimator, SE và CI.
    
    Returns:
    --------
    jk_dist, boot_dist, jk_se, boot_se, jk_ci, boot_ci
    """
    # Bootstrap
    boot_res = bootstrap(data, stat_func, n_boot)
    boot_dist = boot_res['distribution']
    
    # Jackknife
    jk_res = jackknife(data, stat_func)
    jk_dist = jk_res['estimates']
    
    # Tính SE và CI
    boot_se = calc_se(boot_dist)
    boot_ci = calc_ci(boot_dist, confidence)
    
    jk_se = calc_se(jk_dist)
    jk_ci = calc_ci(jk_dist, confidence)
    
    return jk_dist, boot_dist, jk_se, boot_se, jk_ci, boot_ci
