# Day 18 — Feature Scaling

## Key Points

### The Problem of Feature Scale

- Consider an input feature set with two features.
- Example 1:  
  Features = **[hours studied, practice tests taken]**  
  Sample values:  
  - [3, 1]  
  - [5, 2]  
  These features are on a **similar scale and range**.

- Example 2:  
  Features = **[salary, years of experience]**  
  Sample values:  
  - [50000, 7]  
  - [30000, 2]  
  These features are **not on the same scale**.

- When features are on very different scales:
  - one weight becomes very large
  - another weight becomes very small
  - gradients become unbalanced
  - training becomes unstable
  - loss curves can zig-zag
  - convergence becomes slow

- The model may become overly sensitive to one feature and ignore others.

---

### Solution — Feature Scaling

- **Feature scaling** brings features onto a similar scale or common coordinate system.
- This helps gradient descent behave more smoothly and efficiently.
- Scaling does **not** change relationships in the data.
- It improves **optimization behavior**, not model capacity.

---

## Feature Scaling Techniques

### 1️⃣ Min–Max Scaling

X_scaled = (X_train − min) / (max − min)

- Scales features to a fixed range, usually `[0, 1]`
- Less suitable for gradient descent–based models
- Commonly used for:
  - image inputs
  - bounded features

---

### 2️⃣ Standardization (Z-score Scaling)

X_scaled = (X_train − mean) / std

- Centers features around zero
- Scales them to unit variance
- Most commonly used for gradient descent models
- Helps the model:
  - converge faster
  - train more stably

---

## Important Concepts

### Loss Curve
- A **loss curve** is a plot of:
  - loss value vs number of epochs
- A smooth downward curve indicates healthy training.
- Zig-zag patterns indicate unstable optimization.

---

### Convergence
- A model is said to **converge** when:
  - loss stops decreasing significantly
  - parameter updates become very small
  - weights (`w`) and bias (`b`) stabilize

---

### Optimization
- **Optimization** is the process of adjusting model parameters (`w` and `b`)
- The goal is to minimize a loss function using gradient descent.

---

## IMPORTANT — Scaling and Data Leakage

- Scaling parameters (mean, std, min, max) must be computed **only on training data**.
- These parameters must then be:
  - stored
  - reused for validation data
  - reused for real-world inference

- Validation data must **never** be used to compute scaling parameters.
- Doing so leaks distribution information and gives the model unfair knowledge.

---

## Correct ML Pipeline with Scaling

Split data → Feature scaling → Training → Validation