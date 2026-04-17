from sklearn.model_selection import cross_val_score, KFold, LeaveOneOut, train_test_split
import numpy as np

def evaluate_model_stability(model, X, y, cv_folds=5):
    """So sánh độ ổn định giữa Single Split, K-Fold và LOOCV."""
    
    # 1. Single Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model.fit(X_train, y_train)
    single_score = model.score(X_test, y_test)
    
    # 2. K-Fold
    kf = KFold(n_splits=cv_folds, shuffle=True)
    kfold_scores = cross_val_score(model, X, y, cv=kf)
    
    # 3. LOOCV (Cảnh báo: Tốn tài nguyên nếu dữ liệu lớn)
    loo = LeaveOneOut()
    # Chỉ lấy sample nếu dữ liệu quá lớn để tránh treo máy
    if len(X) > 500:
        indices = np.random.choice(len(X), 500, replace=False)
        loo_scores = cross_val_score(model, X[indices], y[indices], cv=loo)
    else:
        loo_scores = cross_val_score(model, X, y, cv=loo)
        
    return {
        'single_split': single_score,
        'kfold': {
            'scores': kfold_scores,
            'mean': np.mean(kfold_scores),
            'std': np.std(kfold_scores)
        },
        'loocv': {
            'scores': loo_scores,
            'mean': np.mean(loo_scores),
            'std': np.std(loo_scores)
        }
    }
