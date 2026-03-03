import pandas as pd

def create_features(df):
    df["Month"] = pd.to_datetime(df["Date"]).dt.month
    df = pd.get_dummies(df, drop_first=True)
    return df