# 1. Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#to suppress warnings generated 
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

# 2. Load data
data = pd.read_csv("diamonds.csv")
print(data.head())
print(data.info())

# 3. Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

# 4. Scatter and Line plots
data.plot.scatter(x="carat", y="clarity")
plt.show()

sns.lineplot(x="carat", y="price", data=data, estimator='mean', ci=None)
plt.title("Average Price Over Carat")
plt.show()

# 5. Define features and target
features = data[["carat", "depth"]]
target = data["price"]


# 6. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# 7. Train the model
lr = LinearRegression()
lr.fit(X_train, y_train)

# 8. Predict on training and testing sets
y_train_pred = lr.predict(X_train)
y_test_pred = lr.predict(X_test)

# 9. Calculate metrics
# Training
train_r2 = r2_score(y_train, y_train_pred)
train_mae = mean_absolute_error(y_train, y_train_pred)
train_mse = mean_squared_error(y_train, y_train_pred)
train_rmse = np.sqrt(train_mse)

# Testing
test_r2 = r2_score(y_test, y_test_pred)
test_mae = mean_absolute_error(y_test, y_test_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
test_rmse = np.sqrt(test_mse)

# 10. Print results
print("\nTraining Set Performance:")
print(f"R² Score: {train_r2:.4f}")
print(f"MAE: {train_mae:.2f}")
print(f"MSE: {train_mse:.2f}")
print(f"RMSE: {train_rmse:.2f}")

print("\nTesting Set Performance:")
print(f"R² Score: {test_r2:.4f}")
print(f"MAE: {test_mae:.2f}")
print(f"MSE: {test_mse:.2f}")
print(f"RMSE: {test_rmse:.2f}")

# 11. Single new prediction example
new_prediction = lr.predict([[0.3, 60]])[0]
print("\nPrediction Example:")
print("The price of the Diamond would be:", round(new_prediction, 2))

# 12. Actual vs Predicted Plot
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_test_pred, color='blue', alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted Prices')
plt.grid(True)
plt.show()
