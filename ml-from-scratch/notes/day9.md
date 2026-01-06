# Day 9 — Loss Function: Mean Squared Error (MSE)

**Time spent:** ~30 minutes

---

## Key Points

- The difference between a predicted value and the true value is called the **error**:
error = y_pred − y_true

- A **loss function** maps this error to a single number that measures how bad the prediction is.
- In Mean Squared Error (MSE), the loss for a single prediction is:
loss = (y_pred − y_true)²

yaml
Copy code

---

## Why Square the Error?

Squaring the error:
- ensures the loss is always positive
- penalizes larger errors more than smaller ones
- results in a smooth function that is easier to optimize

---

## Mean Squared Error (MSE)

- For a dataset with multiple predictions:
- compute the squared error for each prediction
- take the mean of all squared errors
- In code, this looks like:
mean((y_pred − y_true)²)

- MSE produces a **single scalar value** that summarizes model performance.

---

## Key Insight

Training a model means **adjusting parameters (weights and bias)** so that the loss function is minimized.  
Reducing loss means predictions are getting closer to the true values.