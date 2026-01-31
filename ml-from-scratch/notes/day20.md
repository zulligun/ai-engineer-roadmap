# Day 20 — Naive Bayes

## Key Points

- One way to predict labels that we have seen is **logistic regression**.
- In logistic regression, we learn a weight vector `w` and bias `b` by training the model to maximize the likelihood of the observed (training) data.
- This approach is called the **discriminative** approach to machine learning, because it directly models the decision boundary via `P(y | x)`.

---

## Generative Philosophy of ML

- There is another philosophy of machine learning based on **modeling the probability distribution of the observed data**.
- This approach is called the **generative** approach.
- **Naive Bayes** is a classic example of a generative model.

---

## Bayes’ Theorem

Naive Bayes is based on Bayes’ theorem:

P(y | x) = (P(x | y) · P(y)) / P(x)

This is read as:

> *The probability of class `y` given the input features `x` is proportional to the probability of observing the features `x` when the class is `y`, multiplied by the prior probability of the class.*

---

## Prediction Using Naive Bayes

- To predict a label, we compute:

ŷ = argmax_y P(y | x)

- Since `P(x)` is the same for all classes for a fixed input, it can be ignored during comparison.
- Therefore, in practice we compute:

score(y) = P(x | y) · P(y)


- The predicted label is the class with the highest score.

---

## Computing `P(x | y)`

- To compute `P(x | y)`, Naive Bayes makes the **conditional independence assumption**:
  - All features are independent given the class.
- Under this assumption:

P(x | y) = Π P(xᵢ | y)

- The way `P(xᵢ | y)` is computed depends on the nature of the data:
  - **Gaussian Naive Bayes** for continuous features
  - **Bernoulli / Multinomial Naive Bayes** for discrete or count-based features

---

## Key Differences from Logistic Regression

- Naive Bayes does **not** use:
  - weights (`w`)
  - bias (`b`)
  - loss functions
  - gradient descent
- Instead, it relies purely on probability estimation from data.
- Training consists of estimating:
  - class priors `P(y)`
  - feature likelihood distributions `P(xᵢ | y)`

---

## Conclusion

- We now understand two major philosophies of machine learning:
  - **Discriminative models** (e.g. Logistic Regression): model `P(y | x)`
  - **Generative models** (e.g. Naive Bayes): model `P(x | y)` and `P(y)`
- Both approaches solve the same classification problem, but from fundamentally different perspectives.
