import numpy as np
from src.models.logisitic_regression import LogisticRegression

# Features: [hours_studied, sleep_hours]
X = np.array(
    [
        [2, 5],
        [4, 6],
        [6, 6],
        [8, 7],
    ]
)

# Passed exam? (0 = no, 1 = yes)
y = np.array([0, 0, 1, 1])

model = LogisticRegression(n_features=2)

for x in X:
    print("Probability:", model.predict_proba(x))
