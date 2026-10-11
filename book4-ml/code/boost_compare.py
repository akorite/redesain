# code/ch05/boost_compare.py -- residuals shrink stage by stage,
# then scratch tree vs HistGradientBoosting on the same split.
# Run from the repository root:  python3 code/ch05/boost_compare.py
import numpy as np, time
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor

X, y = fetch_california_housing(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=7)

# --- boosting by hand: predict the mean, then fit residuals --------------
print("boosting by hand (depth-3 trees, lr=0.3):")
lr = 0.3
F = np.full(len(Xtr), ytr.mean()); pred_te = np.full(len(Xte), ytr.mean())
trees = []
for stage in range(17):
    if stage in [0, 1, 2, 4, 8, 16]:
        rmse_tr = np.sqrt(((F - ytr) ** 2).mean())
        rmse_te = np.sqrt(((pred_te - yte) ** 2).mean())
        print(f"  stage {stage:>2}: train RMSE {rmse_tr:.4f}  "
              f"test RMSE {rmse_te:.4f}")
    t = DecisionTreeRegressor(max_depth=3, random_state=stage).fit(Xtr, ytr - F)
    trees.append(t)
    F += lr * t.predict(Xtr); pred_te += lr * t.predict(Xte)

# --- library comparison on the same split ---------------------------------
print("\nlibrary models:")
for name, m in [("single tree", DecisionTreeRegressor(random_state=7)),
                ("random forest", RandomForestRegressor(200, n_jobs=-1,
                                                        random_state=7)),
                ("HistGB", HistGradientBoostingRegressor(random_state=7))]:
    t0 = time.time(); m.fit(Xtr, ytr); dt = time.time() - t0
    print(f"  {name:>13}: test R2 {m.score(Xte, yte):.3f}   "
          f"fit {dt*1000:.0f} ms")
