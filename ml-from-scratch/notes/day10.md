# Day 10 — Training the Model Using Stochastic Gradient Descent

**Time spent:** ~2 hours

---

## Key Points

- The main aim of training a model is to **minimize its loss function**.
- In linear regression, this is done using **gradient descent**.
- The loss function can be visualized as a surface with:
  - high-loss regions
  - low-loss regions
- The **gradient** of the loss points in the direction of the steepest increase.
- To reduce loss, we move in the **opposite direction** of the gradient — this is gradient descent.

---

## Gradients in Linear Regression

For a single data point:

- Gradient with respect to weights:
dL/dw = 2 (ŷ − y) x
This means the input vector scaled by twice the prediction error.

- Gradient with respect to bias:
dL/db = 2 (ŷ − y)

---

## Update Rules

To reduce loss, parameters are updated as:

w = w − α (dL/dw)
b = b − α (dL/db)

Where:
- `α` is the **learning rate**
- It controls how large a step we take during each update

A learning rate that is too large can overshoot the minimum,  
while a very small learning rate leads to slow convergence.

---

## Training Process (Stochastic Gradient Descent)

- A training step:
  - takes one feature vector `x`
  - computes the prediction `ŷ`
  - calculates the error `(ŷ − y)`
  - updates weights and bias using the gradients
- In one **epoch**, this process is repeated for all data points.
- Example:
  - 5 data points
  - 100 epochs
  - Total updates = 5 × 100 = 500 steps

---

## Key Insight

The goal of training is **learning shared patterns**, not memorizing individual data points.

Linear regression assumes that input features and output values are related by a **single linear relationship with noise**.  
If this assumption does not hold, more complex models are needed.
