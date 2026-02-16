import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("training_data.csv")

# Separate features and target
X = df.drop("performance_score", axis=1)
y = df["performance_score"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

import matplotlib.pyplot as plt

importances = model.feature_importances_
feature_names = X.columns

for name, importance in zip(feature_names, importances):
    print(f"{name}: {importance:.4f}")


# Evaluate
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"MAE: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

# Save model
joblib.dump(model, "trained_model.pkl")

print("Model saved as trained_model.pkl")
