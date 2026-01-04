import numpy as np
from src.models.linear_regression import LinearRegression

# we see here how we can "predict a number from input features" using Linear Regression

# Each house: [size, rooms]
X = np.array(
    [
        [50, 2],
        [60, 2],
        [80, 3],
        [100, 3],
    ]
)
# Prices (in arbitrary units)
y = np.array([150, 180, 240, 300])

model = LinearRegression(n_features=2)

print("Initial weights:", model.w, "bias:", model.b)

for x_i in X:
    print("Prediction:", model.predict(x_i))
