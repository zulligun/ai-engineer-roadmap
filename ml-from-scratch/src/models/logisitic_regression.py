import numpy as np
from src.linalg.vectors import dot


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


class LogisticRegression:
    def __init__(self, n_features: int):
        self.w = np.zeros(n_features)
        self.b = 0.0

    def predict_proba(self, x: np.ndarray) -> float:
        x = np.asarray(x)
        z = dot(self.w, x) + self.b
        return sigmoid(z)

    def train_step(self, x: np.ndarray, y: int, lr: float = 0.01):
        x = np.asarray(x).reshape(-1)

        p = self.predict_proba(x)
        error = p - y
        self.w -= lr * error * x
        self.b -= lr * error
