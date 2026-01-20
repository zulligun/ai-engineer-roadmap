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

## Understanding Noise, Weights, and Training

- **Noise** refers to variation in the training data that cannot be explained by the chosen features.
- For example, when predicting house prices using features like *size* and *number of bedrooms*, factors such as:
  - emotional sellers,
  - neighborhood quality,
  - number of balconies,
  - interior design,
  are not captured by the model and introduce noise.

- During training, the model may mistakenly treat noise as signal and adjust its weights to fit these irregularities.
- However, real-world (unseen) data may not contain the same noise patterns, causing such models to perform poorly during validation.

- **Large weights amplify the influence of specific features.**
  - Example:
    ```
    price = w1 * size + w2 * num_bedrooms
    ```
  - If `w1` is very large, even a small error or noise in the `size` feature can lead to a large change in the predicted price.

- This makes the model **overly sensitive** to certain features and amplifies noise present in the training data.

- **Regularization** penalizes large weights, keeping them in check and reducing the model’s sensitivity to noise.
- By limiting weight magnitude, regularization helps the model focus on stable patterns and improves **generalization**.
