import numpy as np

def permutation_test(group_a, group_b, stat_func=np.mean, n_permutations=1000):
    """Thực hiện Permutation Test để so sánh sự khác biệt giữa hai nhóm."""
    combined = np.concatenate([group_a, group_b])
    n_a = len(group_a)
    
    observed_diff = stat_func(group_a) - stat_func(group_b)
    
    perm_diffs = []
    for _ in range(n_permutations):
        # Trộn ngẫu nhiên nhãn
        shuffled = np.random.permutation(combined)
        new_a = shuffled[:n_a]
        new_b = shuffled[n_a:]
        perm_diffs.append(stat_func(new_a) - stat_func(new_b))
    
    perm_diffs = np.array(perm_diffs)
    
    # Tính p-value (hai phía)
    p_value = np.mean(np.abs(perm_diffs) >= np.abs(observed_diff))
    
    return {
        'observed_diff': observed_diff,
        'permutation_diffs': perm_diffs,
        'p_value': p_value
    }
