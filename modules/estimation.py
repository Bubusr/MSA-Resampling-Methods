import numpy as np

def bootstrap(data, stat_func, n_resamples=1000):
    """Thực hiện Bootstrap để tính toán phân phối của một đại lượng thống kê."""
    resampled_stats = []
    n = len(data)
    for _ in range(n_resamples):
        resample = np.random.choice(data, size=n, replace=True)
        resampled_stats.append(stat_func(resample))
    
    resampled_stats = np.array(resampled_stats)
    mean_resampled = np.mean(resampled_stats)
    
    return {
        'distribution': resampled_stats,
        'mean': mean_resampled,
        'standard_error': np.std(resampled_stats),
        'ci': (np.percentile(resampled_stats, 2.5), np.percentile(resampled_stats, 97.5))
    }

def jackknife(data, stat_func):
    """Thực hiện Jackknife (Leave-one-out) để ước lượng bias và variance."""
    n = len(data)
    jack_stats = []
    for i in range(n):
        # Loại bỏ phần tử thứ i
        resample = np.delete(data, i)
        jack_stats.append(stat_func(resample))
    
    jack_stats = np.array(jack_stats)
    original_stat = stat_func(data)
    
    # Tính bias
    mean_jack = np.mean(jack_stats)
    bias = (n - 1) * (mean_jack - original_stat)
    
    # Tính variance
    variance = ((n - 1) / n) * np.sum((jack_stats - mean_jack)**2)
    
    return {
        'estimates': jack_stats,
        'bias': bias,
        'variance': variance,
        'standard_error': np.sqrt(variance)
    }

def naive_estimate(data, stat_func):
    """Ước lượng cơ bản (không resampling)."""
    return {
        'estimate': stat_func(data),
        'standard_error': np.std(data) / np.sqrt(len(data)) if stat_func == np.mean else None
    }
