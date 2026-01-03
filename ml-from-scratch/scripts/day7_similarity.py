from src.linalg.vectors import cosine_similarity

# A movie is represented as a feature set of [action, romance, comedy]
# We will write a recommender system that will rank the movies based on the user's profile
# The user's profile is also represented as a feature set [action, romance, comedy]

# For a recommender system such as this, we need to see what movie's feature vector is as close in direction to the user's prfile feature vector.
# this can be done by measuring the cosine similarity of user's feature vector with each movie.
# As we know, cosine similarity ranges from -1 to 1. Higher number means higher similarity.

# Movies represented as feature vectors [action, romance, comedy]
movies = {
    "Action Blast": [9, 1, 1],
    "Love Story": [1, 9, 2],
    "Funny Nights": [1, 2, 9],
    "Action Comedy": [7, 2, 6],
    "Romantic Comedy": [2, 7, 6],
}

# User preference vector (likes action + comedy)
user_profile = [8, 1, 6]

print("User profile:", user_profile)
print("\nSimilarity scores:\n")

scores = []

for name, vector in movies.items():
    score = cosine_similarity(user_profile, vector)
    scores.append((name, score))

# Sort by similarity (highest first)
scores.sort(key=lambda x: x[1], reverse=True)
for movie, score in scores:
    print(f"{movie:20s} -> similarity = {score:.3f}")
