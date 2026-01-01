# Day 3 — Matrices & Matrix–Vector Multiplication

**Time:** 9:00 AM – 3:00 PM (with breaks, New Year holiday)

---

## What We Learned

- Matrix–vector multiplication is essentially a **composition of dot products**.
- Multiplying a matrix with a vector performs a **linear transformation** on that vector.
- We implemented matrix–vector multiplication in Python by:
  - Flattening the input vector
  - Applying the dot product between each row of the matrix and the vector
- The `dot()` function from `vectors.py` (Day 1) was reused to build higher-level operations.
- Internally, matrix–vector multiplication is:
  > one dot product per matrix row

---

## Python & NumPy Learnings

- The `@` operator in Python performs matrix multiplication (`matmul`).
- NumPy arrays are **n-dimensional arrays**, not mathematical vectors by default.
- A 1D NumPy array like:
[1, 2]
has shape `(2,)` and is neither a row vector nor a column vector.
- A 2D array like:
[[1, 2],
[3, 4]]
represents two rows, each containing two elements.
- Understanding array shapes is critical, as incompatible shapes result in runtime errors.

---

## Linear Transformation Composition

- When multiple linear transformations are applied sequentially, their matrices are multiplied.
- If transformation `M1` is applied first and then `M2`, the final transformation is:
M_final = M2 @ M1
- Matrix multiplication is therefore **order-dependent** and represents composition of transformations.

---

## Shape Awareness

- The `.shape` attribute of a NumPy array returns a tuple:
- `shape[0]` → number of rows
- `shape[1]` → number of columns (for 2D arrays)
- Shape compatibility is essential for matrix–vector and matrix–matrix multiplication.

---

## Reflection

Day 3 clarified why matrices appear everywhere in machine learning:
- A matrix represents many dot products bundled together
- This explains why model equations commonly look like:
y = X @ W
- Matrix multiplication is no longer a black box; it directly builds on dot products and vector alignment.
