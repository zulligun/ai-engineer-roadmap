import numpy as np
from src.linalg.vectors import dot


class LinearRegression:
    def __init__(self, n_features: int):
        self.w = np.zeros(n_features)
        self.b = 0.0

    def predict(self, x: np.ndarray) -> float:
        x = np.asarray(x).reshape(-1)
        return dot(self.w, x) + self.b
