import numpy as np
from src.linalg.matrices import matvec

A = np.array([[1, 2], [3, 4]])
x = np.array([5, 6])
y = matvec(A, x)

print("Matrix A:\n", A)
print("Vector x:", x)
print("Result y:", y)
