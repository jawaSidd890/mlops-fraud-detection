import pandas as pd

new = pd.read_csv("new_data.csv")
old = pd.read_csv("../data/raw.csv")

if abs(new.mean().sum() - old.mean().sum()) > 5:
    print("Data drift detected – retraining required")
