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
