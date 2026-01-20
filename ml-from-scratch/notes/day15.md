# Day 15 — Underfitting, Overfitting, and Generalization

---

## Underfitting

- Underfitting occurs when a model is **too simple** to capture patterns in the data.
- Underfitted models perform poorly on:
  - training data
  - validation data
- They exhibit:
  - high training error
  - high validation error
- Example:
  - Using linear regression on highly non-linear data

---

## Overfitting

- Overfitting occurs when a model is **too complex** and memorizes the training data.
- Overfitted models:
  - perform very well on training data
  - perform poorly on unseen (validation) data
- Such models fail to **generalize**.

---

## Why Training Accuracy Is Misleading

- A model can achieve very high training accuracy by memorizing the data.
- This does not guarantee good performance on unseen data.
- Generalization performance must be evaluated using a validation set.

---

## Regularization (Conceptual)

- Regularization penalizes model complexity by adding a constraint to the loss function.
- It discourages the model from relying too heavily on any single feature.
- This helps prevent overfitting.

---

## Why Penalizing Large Weights Helps Generalization

- Large weights make the model overly sensitive to specific features.
- This amplifies noise in the training data.
- Regularization keeps weights small, encouraging simpler and more stable models.
- Simpler models tend to generalize better to unseen data.

---

## Note

- L2 regularization is a common regularization technique.
- We focus on intuition first; mathematical details will be introduced later when needed.
