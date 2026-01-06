import numpy as np


def squared_error(y_true: float, y_pred: float) -> float:
    """Element wise squared error"""
    return (y_pred - y_true) ** 2


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    y_true - np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    return float(np.mean((y_pred - y_true) ** 2))
