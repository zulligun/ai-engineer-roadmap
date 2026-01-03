# Day 5 — Normalization and Unit Vectors

**Time:** 9:00 AM

**Video watched:**  
[Unit Vectors | Khan Academy](https://www.youtube.com/watch?v=jCkhbKFZgLk)

---

## Key Points

- A vector consists of **magnitude (length)** and **direction**.
- The length of a vector is its **magnitude**, also called its **norm**.
- From Day 4, the norm of a vector is:
  - the square root of its dot product with itself
  - geometrically, the length of the vector from the origin
- The dot product measures how much two vectors **align**, combining both magnitude and direction.

---

## Unit Vectors

- A **unit vector** is a vector whose magnitude (norm) is exactly **1**.
- Any non-zero vector can be converted into a unit vector by dividing it by its norm.
- This works because dividing by the norm **scales the vector** so that its length becomes 1.
- The **direction remains unchanged**, only the magnitude is removed.

---

## Normalization

- The process of converting a vector into a unit vector is called **normalization**.
- Normalization:
  - removes magnitude
  - preserves direction
- A **zero vector** cannot be normalized because it has no direction.

---

## Reflection

Normalization allows us to compare vectors based purely on direction.  
This is important in machine learning when magnitude represents scale or frequency, but direction represents meaning or intent.
