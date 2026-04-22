import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Simple synthetic data: y = 3x + noise
rng = np.random.default_rng(42)
X = np.arange(1, 21).reshape(-1, 1)
y = 3 * X.ravel() + rng.normal(0, 2, size=X.shape[0])

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

print(f"Intercept: {model.intercept_:.3f}")
print(f"Coefficient: {model.coef_[0]:.3f}")
print(f"MSE: {mean_squared_error(y, predictions):.3f}")
print(f"R2 Score: {r2_score(y, predictions):.3f}")
