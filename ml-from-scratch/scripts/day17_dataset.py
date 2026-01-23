import numpy as np

# Features: [hours studied, practice tests]
X = np.array(
    [
        [1, 0],
        [2, 1],
        [3, 1],
        [4, 2],
        [5, 3],
        [1, 3],
        [2, 4],
        [3, 5],
    ]
)

# Labels: pass (1) or fail (0)
y = np.array([0, 0, 0, 1, 1, 0, 1, 1])
