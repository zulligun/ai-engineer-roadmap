# Day 8 — Introduction to Linear Regression

**Time spent:** ~30 minutes

---

## Key Questions and Answers

### What is linear regression trying to do?
Linear regression tries to predict a **numerical value** from a set of input features.

In our example, the goal is to predict a house price given features such as:
[size, number_of_rooms]

---

### How does the model make a prediction?
The prediction is computed using the formula:
ŷ = w · x + b

Where:
- `ŷ` → predicted value
- `w` → weight vector
- `x` → input feature vector
- `b` → bias term

Conceptually, linear regression computes a **weighted sum of input features**, plus a bias.

---

### Why is the dot product central here?
The dot product is used to compute the **weighted contribution** of each feature.

Each weight represents how strongly a feature influences the prediction.
The dot product combines all feature contributions into a single number.

---

### Why do initial predictions start at zero?
At initialization:
- all weights are set to zero
- bias is set to zero

Therefore:
- `w · x = 0`
- `ŷ = 0`

This represents an **untrained model**, before learning begins.
