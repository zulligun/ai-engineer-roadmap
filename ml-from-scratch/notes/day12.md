# Day 12 — Logistic Regression

**Time spent:** ~1 hour

---

## Key Points

- Logistic regression takes an input feature vector and outputs a **probability** between `0` and `1`.
- Conceptually, logistic regression is:
  **linear regression + a squashing function + a different loss function**.
- The model first computes:
z = w · x + b
- This value is passed through the **sigmoid function** before producing the final output.

---

## Sigmoid Function

- The sigmoid function maps any real number to the range `(0, 1)`:
sigmoid(z) = 1 / (1 + e^(−z))
- This allows the output to be interpreted as a **probability**.

---

## Loss Function: Binary Cross-Entropy

- Logistic regression uses **binary cross-entropy loss**:
loss = − [ y log(p) + (1 − y) log(1 − p) ]
- This loss function:
- heavily penalizes confident wrong predictions
- aligns well with probabilistic outputs
- The true labels `y` are certain (`0` or `1`), while the model’s predictions introduce uncertainty.
- Cross-entropy measures how costly the model’s predicted uncertainty is compared to the true outcome.

Example:
- If `y = 1` and `p = 0.1`, the loss is very high.
- This indicates the model was confidently wrong.
- If the model predicts correctly with high confidence, the loss is low.

---

## Logistic vs Linear Regression

- **Linear regression** outputs a numerical value.
- **Logistic regression** outputs a probability.
- A classification decision (yes/no) is made by applying a threshold to the probability.

---

## Why Not Use MSE for Classification?

- MSE produces poor gradients when combined with sigmoid.
- This leads to slow or unstable learning.
- Binary cross-entropy provides stronger, more informative gradients.
