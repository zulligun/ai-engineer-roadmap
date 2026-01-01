import numpy as np
from src.linalg.vectors import dot


def matvec(matrix: np.ndarray, vector: np.ndarray) -> np.ndarray:
    """MMatrix-vector multiplication implemented as dot products"""

    matrix = np.asarray(matrix)
    vector = np.asarray(vector).reshape(-1)

    if matrix.shape[1] != vector.shape[0]:
        raise ValueError(
            f"Shape mismatch: {matrix.shape} cannot multiply with {vector.shape}"
        )

    result = []
    for row in matrix:
        result.append(dot(row, vector))

    return np.array(result)
