# Day 7 — A Recommender System Using Cosine Similarity

**Time spent:** ~2 hours

---

## What We Did

- Designed a simple recommender system that ranks movies based on a user’s preferences.
- Each movie was represented as a feature vector:
[action, romance, comedy]
- The values in the vector represent how strongly each theme is present in the movie.
- The user’s preferences were represented using the same feature space.
- For each movie, we computed the **cosine similarity** between the movie vector and the user profile.
- Movies were ranked in descending order of similarity.

---

## Key Observations

- Cosine similarity compares vectors based on **direction**, not absolute magnitude.
- Before computing cosine similarity, vectors are normalized into **unit vectors**.
- Normalization:
- removes absolute magnitude (length becomes 1)
- preserves the **relative importance** of features
- This ensures that similarity is based on **preference patterns**, not raw intensity.
- Using unit vectors allows fair comparison across items with different scales.

---

## Additional Learnings

- Learned about Python string formatting for clean output:
- `20s` for alignment
- `.3f` for decimal precision

---

## Conclusion

Cosine similarity is useful when comparing items based on **intent or taste**, where direction matters more than magnitude.  
This approach forms the foundation of many recommendation and similarity-based systems.
