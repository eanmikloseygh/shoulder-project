import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\leosp\Documents\work1 - Sheet1.csv')

# I want to make a categorical value for sleep based using the information from my hours and quality rating

conditions = [
    # Good
    (df["Sleep_hours"].between(7, 9)) & (df["Sleep_Quality"].between(8, 10)),

    # Poor
    (df["Sleep_hours"] <= 5) | (df["Sleep_hours"] >= 11) | (df["Sleep_Quality"] <= 5),

    # Neutral (everything else reasonable)
    (df["Sleep_hours"].between(6, 10)) & (df["Sleep_Quality"].between(6, 10))
]

choices = ["Good", "Poor", "Neutral"]
df["sleep_cat"] = np.select(conditions, choices, default="Unknown")

print(df["sleep_cat"].value_counts())
print(df[["Sleep_hours", "Sleep_Quality", "sleep_cat"]].head(30)) #did this to confirm everything is working

# Now I want to make some rolling variables to reduce daily noise and lag variables to evaluate yesterday's effect on the following day

df["Sleep_7day_avg"] = df["Sleep_hours"].rolling(window=7).mean()
df["RHR_7day_avg"] = df["Resting_HR"].rolling(window=7).mean()

df["Sleep_lag1"] = df["Sleep_hours"].shift(1)
df["RHR_lag1"] = df["Resting_HR"].shift(1)
df["SS_lag1"] = df["Shoulder_score"].shift(1)

df.to_csv("cleaned_performance_data.csv", index=False)