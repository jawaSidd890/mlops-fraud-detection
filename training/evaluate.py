import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

df = pd.read_csv("../data/raw.csv")
X = df.drop("fraud", axis=1)
y = df["fraud"]

model = joblib.load("model.pkl")
pred = model.predict(X)

print("Accuracy:", accuracy_score(y, pred))
