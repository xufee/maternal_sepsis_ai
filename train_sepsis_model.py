import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# Load dataset
data = pd.read_csv("maternal_sepsis_dataset.csv")
print("📊 Columns in dataset:", data.columns.tolist())

# Save the target column before encoding
y = data["Sepsis_detected"]

# Drop columns not needed for training
X = data.drop(columns=["Sepsis_detected", "Patient_ID", "Outcome"], errors="ignore")

# Encode categorical features
X = pd.get_dummies(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("📈 Evaluation Results:\n", classification_report(y_test, y_pred))

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/sepsis_model.pkl")
print("✅ Model has been saved to models/sepsis_model.pkl")












