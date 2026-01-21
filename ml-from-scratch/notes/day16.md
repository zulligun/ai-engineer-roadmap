# Day 16 — Bias–Variance Tradeoff

**Time spent:** ~15 minutes

---

## Key Concepts

### What is Bias?
- Bias is the error introduced due to **over-simplification** of a model.
- High bias means:
  - the model is too simple
  - it fails to capture underlying patterns
  - it **underfits** the data
- Underfit models perform poorly on both:
  - training data
  - validation data

---

### What is Variance?
- Variance is the error introduced due to **over-sensitivity** of a model to the data.
- High variance means:
  - the model fits noise instead of signal
  - predictions change significantly with small changes in data
  - the model **overfits**
- Overfit models:
  - perform very well on training data
  - perform poorly on validation data

---

### Relationship to Underfitting and Overfitting

- **Underfitting** occurs when the model is not complex enough to recognize patterns.
  - This is what **high bias** represents.
  - Such models have high error on both training and validation sets.

- **Overfitting** occurs when the model is too complex and overly sensitive.
  - This is what **high variance** represents.
  - Such models memorize training data but fail to generalize to unseen data.

---

### Why Can’t Bias and Variance Both Be Minimized?

- There is an inherent **tradeoff** between bias and variance.
- Reducing bias requires increasing model complexity, which:
  - improves pattern recognition
  - but increases variance by fitting noise
- Reducing variance requires simplifying the model, which:
  - reduces sensitivity to noise
  - but increases bias by missing patterns

---

### How Regularization Affects Bias and Variance

- Regularization penalizes large weights during training.
- This prevents the model from becoming overly sensitive to specific features.
- As a result:
  - **variance decreases**
  - **bias increases slightly**
- The net effect is improved **generalization**.

---

## Bias–Variance Tradeoff Summary Table

| Model / Property      | Bias | Variance |
|----------------------|------|----------|
| Underfitting Model   | High | Low      |
| Overfitting Model    | Low  | High     |
| Simple Model         | High | Low      |
| Complex Model        | Low  | High     |
| Regularization Effect| ↑    | ↓        |

---

## Key Insight

Every machine learning model represents a balance between bias and variance.  
Good models do not eliminate error — they **manage tradeoffs** to generalize well.
