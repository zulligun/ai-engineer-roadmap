# Day 4 — Understanding the Length of a Vector (Norm)

**Time:** 9:00–10:00 AM

**Video watched:**  
[Vector dot product and vector length | Khan Academy](https://www.youtube.com/watch?v=WNuIhXo39_k)

---

## Learned Points

- The length of a vector in 2D space can be visualized as the hypotenuse of a right-angled triangle formed by projecting the vector onto the x and y axes.
- In this triangle, the vector itself represents the hypotenuse.
- By the Pythagorean theorem, if a vector is represented as `[x, y]`, its length is:
sqrt(x² + y²)

- The expression `x² + y²` is exactly the **dot product of the vector with itself**.
- Therefore, the **norm (length)** of a vector `a` is defined as:
norm(a) = sqrt(dot(a, a))
- Squaring both sides removes the square root:
norm(a)² = dot(a, a)
- This means the dot product of a vector **with itself** gives the square of its length.

---

## Reflection

The norm represents the magnitude (length) of a vector, independent of its direction.  
This explains why dot products combine both direction and magnitude, and why separating these two concepts will be important later in machine learning.
