import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Step 1: Load the dataset
data = pd.read_csv("data/simulated_health_data.csv")

# Step 2: Define features (X) and target (y)
X = data.drop(columns=["kidney_stress_risk"])
y = data["kidney_stress_risk"]

# Step 3: Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 6: Save the trained model
joblib.dump(model, "model/kidney_risk_model.pkl")
print(" Model saved to model/kidney_risk_model.pkl")
