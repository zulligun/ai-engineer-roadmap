import numpy as np

X = np.array(
    [
        [1500, 0],
        [5015, 1],
        [3200, 1],
        [4500, 2],
        [5400, 3],
    ]
)

mean = X.mean(axis=0)
std = X.std(axis=0)

# feature scaling using standardization (z-score)
X_scaled = (X - mean) / std

print("Original:\n", X)
print("Scaled:\n", np.round(X_scaled, 3))
