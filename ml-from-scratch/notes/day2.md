# Day 2 — Dot Product & Linear Transformations

**Time:** 9:00–10:00 AM

---

## What We Learned Today

- Watched:  
  [Dot products and duality — 3Blue1Brown](https://www.youtube.com/watch?v=LyGKycYT2v0)

- To better understand the above video, also watched:  
  [Linear transformations and matrices — 3Blue1Brown](https://www.youtube.com/watch?v=kYB8IZa5AuE)

---

## Linear Transformations

- A transformation is **linear** if:
  - The origin does not move
  - Straight lines remain straight (no bending)

- To predict where a vector lands after a linear transformation, it is sufficient to know:
  - Where **î** (unit x-vector) lands
  - Where **ĵ** (unit y-vector) lands

- Any vector can be expressed as a linear combination of **î** and **ĵ**.
  - The coefficients represent the projection of the vector onto the x and y axes.

---

## Matrices as Transformations

- A linear transformation can be represented as a **matrix**.
- The matrix encodes the coordinates of where **î** and **ĵ** land after transformation:

[ î_x ĵ_x ]
[ î_y ĵ_y ]

- Multiplying this matrix by a vector `[x, y]` gives the transformed coordinates of that vector.

---

## Duality and Dot Product

- A linear functional from ℝ² → ℝ can be represented as a **1×2 matrix**, for example:
[a b]

- This represents a transformation that projects vectors onto a 1-dimensional line.

- This leads to **duality**:
- A linear transformation can be represented as a vector
- A vector can be viewed as a transformation acting on another vector

- The **dot product** is exactly this idea:
- It measures how much one vector projects onto another
- The result is a **scalar** representing alignment

---

## Key Properties of Dot Product

- If two vectors point in the **same direction**, the dot product is large and positive
- If they point in **opposite directions**, the dot product is negative
- If they are **orthogonal (perpendicular)**, the dot product is zero

This means orthogonal vectors have **no overlap or influence** on each other.

---

## Analyzing Day 1 Code

### `dot()` Function
- `np.asarray()` ensures the input is treated as a NumPy array
- `reshape(-1)` flattens the input into a 1D vector
- The `*` operator performs **element-wise (Hadamard) multiplication**
- `np.sum()` adds the products to produce the dot product

### `norm()` Function
- Not fully understood yet conceptually
- From the code, it is computed as:
sqrt(dot(a, a))
- This suggests it measures the magnitude (length) of a vector
- The geometric meaning will be explained later
