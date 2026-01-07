import numpy as np
from src.losses.mse import mean_squared_error
from src.models.linear_regression import LinearRegression

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

lr = 0.0001
epochs = 1000

for epoch in range(epochs):
    for x_i, y_i in zip(X, y):
        model.train_step(x_i, y_i, lr)

    if epoch % 200 == 0:
        preds = np.array([model.predict(x) for x in X])
        loss = mean_squared_error(y, preds)
        print(f"Epoch {epoch}, Loss {loss:.2f}")


print("\nFinal weights:", model.w)
print("Final bias:", model.b)
