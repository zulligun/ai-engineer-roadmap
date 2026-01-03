# Day 6 — Cosine Similarity

**Time:** 11:00 AM

---

## Key Points

- Normalization removes the **magnitude** of a vector and preserves its **direction**.
- The dot product measures how similar two vectors are by combining:
  - direction
  - magnitude
- When vectors are normalized, magnitude is removed.
- The dot product of **unit vectors** therefore measures similarity based on **direction only**.
- This directional similarity is called **cosine similarity**.

---

## Cosine Similarity

- Cosine similarity between two vectors `a` and `b` is defined as:
cosine_similarity(a, b) = dot(unit(a), unit(b))
- The result ranges between:
- `1` → same direction
- `0` → no alignment (orthogonal)
- `-1` → opposite direction

---

## Why Cosine Similarity Is Useful

- In many machine learning problems, we care more about **how similar two things are** than how large they are.
- Cosine similarity allows us to compare vectors while ignoring differences in scale.
- It is useful whenever vectors represent **features**, and magnitude may be misleading.

---

## Reflection

Cosine similarity is not a new concept; it is simply the dot product applied after normalization.  
Understanding it as “dot product of unit vectors” makes its purpose and behavior clear.
