# Day 14 — Classification Metrics and Their Importance

**Time spent:** ~30 minutes

---

## Key Metrics

The usefulness of a classification model is evaluated using the following metrics:

1. Accuracy  
2. Precision  
3. Recall  
4. F1 Score  

All of these metrics are derived from the **confusion matrix**.

---

## Confusion Matrix Terms

- **True Positive (TP):** actual value is `1` and predicted value is `1`
- **False Positive (FP):** actual value is `0` but predicted value is `1`
- **False Negative (FN):** actual value is `1` but predicted value is `0`
- **True Negative (TN):** actual value is `0` and predicted value is `0`

---

## Metric Definitions

- **Accuracy**
(TP + TN) / (TP + TN + FP + FN)
Measures overall correctness, but can be misleading when classes are imbalanced.

- **Precision**
TP / (TP + FP)
Out of all predictions made as positive, how many were actually correct?

- **Recall**
TP / (TP + FN)
Out of all actual positive cases, how many did the model correctly identify?

- **F1 Score**
2 * (Precision * Recall) / (Precision + Recall)
Balances precision and recall into a single metric.

---

## Threshold and Tradeoffs

Logistic regression outputs **probabilities**, not direct class labels.

A classification decision is made using a threshold:
if p > threshold → predict 1
else → predict 0

Adjusting the threshold controls the tradeoff between:
- **Precision** (reducing false positives)
- **Recall** (reducing false negatives)

Choosing the right metric and threshold depends on the problem’s real-world costs.
