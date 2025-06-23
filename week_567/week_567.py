import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")
df = df.dropna()  # to remove missing values if any

# Line plot: average bill length per species
avg_bill = df.groupby("species")["bill_length_mm"].mean()
plt.figure(figsize=(6,4))
plt.plot(avg_bill.index, avg_bill.values, marker='o', linestyle='-')
plt.title("Avg Bill Length by Species")
plt.xlabel("Species")
plt.ylabel("Bill Length (mm)")
plt.grid(True)
plt.show()

# Scatter plot: bill length vs depth
plt.figure(figsize=(6, 4))
sns.scatterplot(
    data=df,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",         # color by species
    palette="Set1",       
    alpha=0.7
)
plt.title("Bill Length vs Bill Depth (by Species)")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")
plt.legend(title="Species")
plt.grid(True)
plt.tight_layout()
plt.show()

sns.set_theme() 
# Histogram of flipper length
plt.figure(figsize=(6,4))
sns.histplot(data=df, x="flipper_length_mm", kde=True, bins=20)
plt.title("Flipper Length Distribution")
plt.show()

# Box plot of flipper length by species
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="species", y="flipper_length_mm")
plt.title("Flipper Length by Species")
plt.show()