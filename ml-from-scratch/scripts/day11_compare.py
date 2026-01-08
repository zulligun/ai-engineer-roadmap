import numpy as np
from src.models.linear_regression import LinearRegression
from src.losses.mse import mean_squared_error

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

epochs = 500
lr = 0.0001

for epoch in range(epochs):
    model.train_batch(X, y, lr)

preds = np.array([model.predict(x) for x in X])
loss = mean_squared_error(y, preds)

print("Final weights:", model.w)
print("Final bias:", model.b)
print("Final loss:", loss)
print("True y:", y)
print("Predicated y:", preds)
