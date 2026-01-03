import numpy as np
from src.linalg.vectors import dot, norm, unit, cosine_similarity

a = np.array([3, 4])
b = np.array([2, 1])

print("dot(a,b) =", dot(a, b))  # 3*2 + 4*1 = 10
print("norm(a)  =", norm(a))  # sqrt(3^2 + 4^2) = 5
print("unit(a) =", unit(a))
print("cosine similarity(a,b)", cosine_similarity(a, b))
