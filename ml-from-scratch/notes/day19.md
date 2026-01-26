# Day 19 — Understanding Maximum Likelihood Estimation (MLE)

## Key Points

- Interestingly, we have been using **Maximum Likelihood Estimation (MLE)** all along without explicitly naming it.
- MLE means **adjusting the parameters of a model so that the observed data becomes most likely**.
- In short, **training a model is performing MLE**.

---

## Likelihood in Logistic Regression

- In logistic regression, the model outputs:

P(y = 1 | x)

- This means the **probability of the label being 1 given the input features `x`**.
- For each data point `(xᵢ, yᵢ)` in the dataset, calling `model.predict(xᵢ)` gives us `P(y = 1 | xᵢ)`.

- If `yᵢ = 1`, the probability of observing that data point is `pᵢ`.
- If `yᵢ = 0`, the probability of observing that data point is `1 − pᵢ`.

---

## Dataset Likelihood

- **Likelihood** answers the question:
  > *How likely is it to observe the entire dataset given parameters `w` and `b`?*

- The total likelihood of the dataset is computed by multiplying the probabilities of all individual data points:

Likelihood = Π P(yᵢ | xᵢ)


- The capital **Π (pi)** symbol means *product over all data points*.

---

## Log-Likelihood

- Since probabilities lie between 0 and 1, multiplying many of them results in extremely small numbers.
- To make this numerically stable and easier to optimize, we take the logarithm:

log-likelihood = Σ log P(yᵢ | xᵢ)

- Maximizing log-likelihood is equivalent to maximizing likelihood.

---

## Why We Minimize Loss

- Optimization algorithms like gradient descent are designed to **minimize** a function.
- Therefore, instead of maximizing log-likelihood, we **minimize negative log-likelihood**.

- This leads to the binary cross-entropy loss used in logistic regression:

Loss = -[ y log(p) + (1 - y) log(1 - p) ]


- The minus sign indicates that we are minimizing the negative likelihood.
- As the loss decreases, the likelihood of the observed data increases.

---

## Conclusion

- Logistic regression training is fundamentally based on **Maximum Likelihood Estimation**.
- Minimizing the loss function is equivalent to maximizing the likelihood of the observed dataset.
- What appears as a “loss function” is actually grounded in probability theory, not an arbitrary choice.
