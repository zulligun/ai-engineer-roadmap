# Day 11 — Batch Gradient Descent and Concept Consolidation

**Time spent:** ~2 hours

---

## Key Concepts

- **Stochastic Gradient Descent (SGD)** updates the model parameters once per data point.
- Each training step involves:
  - computing the error for one data point
  - immediately updating weights and bias
- **Batch Gradient Descent (BGD)** computes the average error across **all data points** and updates the model parameters **once per epoch**.
- BGD results in:
  - fewer parameter updates
  - more stable convergence
  - higher computational cost per update

---

## Batch Gradient Computation

For a dataset with `N` samples:

- Gradient with respect to weights:
dL/dw = (2/N) ∑ (ŷᵢ − yᵢ) xᵢ
= 2 * mean(errors * X)

- Gradient with respect to bias:
dL/db = (2/N) ∑ (ŷᵢ − yᵢ)
= 2 * mean(errors)

Where:
- `errors = ŷ − y`
- `N` is the number of samples

---

## NumPy Broadcasting Insights

- A 1D NumPy array has shape `(N,)`.
- Using `errors[:, None]` adds a new axis, converting it to `(N, 1)`.
- This allows broadcasting with `X`, which has shape `(N, n_features)`.

### Broadcasting rules:
- Dimensions are compared from right to left
- Broadcasting is allowed if:
1. dimensions are equal, or
2. one of the dimensions is `1`

This enables each error value to scale its corresponding feature vector.

---

## Use of `axis` in `np.mean`

- `axis=0`: collapses rows → computes the mean of each column
- `axis=1`: collapses columns → computes the mean of each row

In batch gradient descent:
- we use `axis=0` to compute the gradient **per feature**
- this ensures `grad_w` has the same shape as the weight vector `w`

---

## Key Insight

Batch gradient descent makes explicit what SGD approximates:
**learning is driven by the average error signal across the dataset**, not any single data point.
