import os
import pandas as pd
import matplotlib.pyplot as plt

# Ensure output folder exists
os.makedirs("figures", exist_ok=True)

# Read cleaned file
df = pd.read_csv("data/clean/labMT_clean.csv")

# Missing values should be excluded in the analysis
vals = df["happiness_average"].dropna()

# Draw histogram and save it
plt.figure(figsize=(8, 5))
plt.hist(vals, bins=30, edgecolor="black")
plt.title("Distribution of happiness scores")
plt.xlabel("happiness_average")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("figures/happiness_histogram.png", dpi=300, bbox_inches="tight")
plt.close()

# Summary statistics
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

print("\nSaved figure to figures/happiness_histogram.png")
