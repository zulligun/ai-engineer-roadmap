"""
End to end implementation of logistic regression from scratch.
The dataset is in day17_dataset.py file.

Problem:

Predict whether a student will pass (1) or fail (0)
Based on:
hours studied
number of practice tests taken

After training:
predict probabilities
apply threshold (0.5)

compute:
accuracy
precision
recall
"""

from scripts.day17_dataset import X, y
import numpy as np

THRESHOLD = 0.5


def sigmoid(z: float) -> float:
    return 1 / (1 + np.exp(-z))


def dot(a: np.ndarray, b: np.ndarray) -> float:
    a = np.asarray(a).reshape(-1)
    b = np.asarray(b).reshape(-1)
    if a.shape != b.shape:
        raise ValueError(
            f"Input shapes a:{a.shape}, b: {b.shape} do not match for a dot product."
        )
    return np.sum(a * b)


class LogisticRegression:
    def __init__(self, n_features: int):
        self.w = np.zeros(n_features)
        self.b = 0.0

    def predict(self, x: np.ndarray) -> float:
        x = np.asarray(x).reshape(-1)
        z = dot(self.w, x) + self.b
        p = sigmoid(z)
        # if p < THRESHOLD:
        #     return 0
        return p

    def train_step(self, x: np.ndarray, y: int, lr: float = 0.001):
        x = np.asarray(x).reshape(-1)
        p = self.predict(x)
        error = p - y
        self.w -= lr * error * x
        self.b -= lr * error


# runner script here:
X_train = X[:6]
y_train = y[:6]
X_validation = X[6:]
y_validation = y[6:]

lr = 0.1
model = LogisticRegression(n_features=X.shape[1])
epochs = 1000
for epoch in range(epochs):
    for x_i, y_i in zip(X_train, y_train):
        model.train_step(x_i, y_i, lr)
    if epoch % 200 == 0:
        train_probs = [model.predict(x) for x in X_train]
        val_probs = [model.predict(x) for x in X_validation]
        print(
            f"Epoch: {epoch}, train prob: {[float(round(p,3)) for p in train_probs]}, val_probs: {[float(round(p,3)) for p in val_probs]}"
        )

# predictions (validation)
val_probs = np.array([model.predict(x) for x in X_validation])
labels = (val_probs >= THRESHOLD).astype(int)

print("Validation probabilities:", [float(round(p, 3)) for p in val_probs])
print("Validation labels:", [int(v) for v in labels])

# Evaluation metrics
TP = np.sum((labels == 1) & (y_validation == 1))
TN = np.sum((labels == 0) & (y_validation == 0))
FP = np.sum((labels == 1) & (y_validation == 0))
FN = np.sum((labels == 0) & (y_validation == 1))

accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = (TP) / (TP + FP)
recall = TP / (TP + FN)

print(f"Accuracy = {accuracy}, precision = {precision}, recall = {recall}")
