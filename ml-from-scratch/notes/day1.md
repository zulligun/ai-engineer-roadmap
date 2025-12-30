# Day 1 — Vectors (Foundations)

**Time spent:** 2 hours (8:00–10:00 AM)

---

## Environment Setup

Today was focused on setting up a clean and professional development environment.

Completed setup:
1. Windows Subsystem for Linux (WSL) — Ubuntu
2. Python and VS Code extensions
3. Code formatters and linters (Black, Ruff)
4. Python virtual environment (`venv`)

---

## Python Project Structure & Execution

### `__init__.py`
- Learned the importance of `__init__.py` files.
- Adding this file makes a folder a **Python package**, which allows it to be imported and reused by other modules.

### Running Python Modules
- Correct way to run project code:
  ```bash
  python -m package.module

- The .py extension should not be used with -m.
Why?
Using .py causes Python to interpret it as a module name, leading to ModuleNotFoundError.
-m expects a module path, not a filename.

## Linear Algebra — Vectors (Conceptual Understanding)

Watched:

[Vectors | Chapter 1, Essence of Linear Algebra — 3Blue1Brown](https://www.youtube.com/watch?v=fNk_zzaMoSs)

### Key Takeaways

    - Vectors can be understood from multiple perspectives:

    Mathematics:
        An abstract object that has magnitude and direction.
    Physics:
        A quantity with both value and direction, usually represented as an arrow in space (often starting at the origin).
    Computer Science / Machine Learning:
        A list of numbers representing features or attributes.
        Example: a house represented as a vector of [price, area].

    The coordinates are just a representation — the vector itself is the underlying concept.

--- 
## Code Work

- Created vector-related utilities inside src/linalg/.

Implemented:

dot() — dot product

norm() — vector magnitude

These operations are used in the code but not fully understood yet.
The geometric intuition behind them will be covered next.

--- 

## Reflection

Today focused on:

Environment setup
Python packaging fundamentals
Understanding what vectors are conceptually
Operations on vectors (dot product, norm, orthogonality) will be explored next.

--- 
