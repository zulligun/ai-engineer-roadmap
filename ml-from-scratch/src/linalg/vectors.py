import numpy as np


def dot(a: np.ndarray, b: np.ndarray) -> float:
    """Dot product of two vectors"""
    a = np.asarray(a).reshape(-1)
    b = np.asarray(b).reshape(-1)
    if a.shape != b.shape:
        raise ValueError(f"Shape mismatch: {a.shape} vs {b.shape}")
    return float(np.sum(a * b))


def norm(a: np.ndarray) -> float:
    """Euclidean norm (L2)."""
    a = np.asarray(a).reshape(-1)
    return float(np.sqrt(dot(a, a)))
