import pandas as pd
import matplotlib.pyplot as plt


# Read cleaned file
df = pd.read_csv("data/clean/labMT_clean.csv")

# Missing values should be excluded in the analysis
vals = df["happiness_average"].dropna()

# drawing histogram
plt.figure(figsize=(8, 5))
plt.hist(vals, bins=30, edgecolor="black")
plt.title("Histogram of happiness_average")
plt.xlabel("happiness_average")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#statistics
mean_val = vals.mean()
median_val = vals.median()
std_val = vals.std()
p5 = vals.quantile(0.05)
p95 = vals.quantile(0.95)

print("Summary statistics for happiness_average:")
print(f"Count:  {vals.count()}")
print(f"Mean:   {mean_val:.4f}")
print(f"Median: {median_val:.4f}")
print(f"Std:    {std_val:.4f}")
print(f"5th percentile:  {p5:.4f}")
print(f"95th percentile: {p95:.4f}")