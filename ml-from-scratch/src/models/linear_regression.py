import numpy as np
from src.linalg.vectors import dot


class LinearRegression:
    def __init__(self, n_features: int):
        self.w = np.zeros(n_features)
        self.b = 0.0

    def predict(self, x: np.ndarray) -> float:
        x = np.asarray(x).reshape(-1)
        return dot(self.w, x) + self.b

    def train_step(self, x: np.ndarray, y: float, lr: float = 0.001):
        x = np.asarray(x).reshape(-1)

        y_pred = self.predict(x)

        error = y_pred - y

        # gradients
        grad_w = 2 * error * x
        grad_b = 2 * error

        # update weights and bias
        self.w -= lr * grad_w
        self.b -= lr * grad_b

    def train_batch(self, X: np.ndarray, y: np.ndarray, lr: float = 0.001):
        X = np.asarray(X)
        y = np.asarray(y)

        y_pred = np.array([self.predict(x) for x in X])
        errors = y_pred - y

        grad_w = 2 * np.mean(errors[:, None] * X, axis=0)
        grad_b = 2 * np.mean(errors)

        self.w -= lr * grad_w
        self.b -= lr * grad_b
