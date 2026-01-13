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
epochs = 1000
lr = 0.1

for epoch in range(epochs):
    for x_i, y_i in zip(X, y):
        model.train_step(x_i, y_i, lr)

    if epoch % 200 == 0 or epoch == 0:
        probs = [model.predict_proba(x) for x in X]
        print(f"Epoch {epoch}: probs = {[round(p, 2) for p in probs]}")

print("\nFinal weights:", model.w)
print("Final bias:", model.b)
