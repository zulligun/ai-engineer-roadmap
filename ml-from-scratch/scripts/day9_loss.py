import numpy as np
from src.models.linear_regression import LinearRegression
from src.losses.mse import mean_squared_error

# Dataset
X = np.array(
    [
        [50, 2],
        [60, 2],
        [80, 3],
        [100, 3],
    ]
)

y = np.array([150, 180, 240, 300])

model = LinearRegression(n_features=2)

# Predictions
y_pred = np.array([model.predict(x) for x in X])

loss = mean_squared_error(y, y_pred)

print("Predictions:", y_pred)
print("True values:", y)
print("Loss:", loss)
