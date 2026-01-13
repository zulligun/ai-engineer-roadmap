# Day 13 — Training Logistic Regression

**Time spent:** ~1 hour

---

## Key Points

- Logistic regression is trained using **gradient descent**, just like linear regression.
- The combination of **sigmoid activation** and **binary cross-entropy loss** leads to very simple gradients.
- The core error signal is:
# Day 13 — Training Logistic Regression

**Time spent:** ~1 hour

---

## Key Points

- Logistic regression is trained using **gradient descent**, just like linear regression.
- The combination of **sigmoid activation** and **binary cross-entropy loss** leads to very simple gradients.
- The core error signal is:
error = p − y
where:
- `p` is the predicted probability
- `y` is the true label (0 or 1)

- This error represents the **gradient of the loss with respect to the model’s linear score (`z`)**.
- Using the chain rule, the full parameter gradients become:
∂L/∂w = error * x
∂L/∂b = error

- The same weights and bias are shared across all data points.
- Training adjusts these shared parameters to minimize the **average loss over the dataset**.
- Confident wrong predictions produce large gradients and are corrected quickly.
- Uncertain predictions produce smaller gradients and are corrected more slowly.

---

## Key Insight

Logistic regression learns by propagating a probabilistic error signal backward through the model and updating parameters to reduce cross-entropy loss.
