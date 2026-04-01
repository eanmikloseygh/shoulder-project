import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\leosp\PyCharmMiscProject\cleaned_performance_data.csv")

plt.figure()
plt.scatter(df["Day"], df["Sleep_hours"])
plt.title("Sleep Hours Over Time")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.ylim(0, 12)
plt.xticks(rotation=45)
plt.show()

plt.figure()
plt.plot(df["Day"], df["Shoulder_score"])
plt.title("Shoulder Score Over Time")
plt.xlabel("Day")
plt.ylabel("Shoulder Score")
plt.xticks(rotation=45)
plt.show()

plt.figure()
plt.plot(df["Day"], df["Resting_HR"])
plt.title("Resting HR Over Time")
plt.xlabel("Day")
plt.ylabel("Resting HR")
plt.xticks(rotation=45)
plt.show()

# just basic time vs variable plots above, trying correlation plots below

corr = df.corr(numeric_only=True)

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True)

plt.title("Correlation Matrix")

plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)

plt.tight_layout()
plt.show()

# some relationship plots based on observations from the correlation matrix

sns.regplot(x="Shoulder_score", y="Volume", data=df)
plt.title("Shoulder score vs volume")
plt.xlabel("Shoulder score")
plt.ylabel("Volume")
plt.show()

sns.regplot(x="Shoulder_score", y="Stress_level", data=df)
plt.title("Shoulder score vs stress level")
plt.xlabel("Shoulder score")
plt.ylabel("Stress level")
plt.show()

# using previously engineered variable for new insights

sns.boxplot(x="sleep_cat", y="Shoulder_score", data=df)
plt.title("Performance by Sleep Category")
plt.show()
