import os
import pandas as pd
import matplotlib.pyplot as plt

# Ensure output folder exists
os.makedirs("figures", exist_ok=True)

# Load data
df = pd.read_csv("data/clean/labMT_clean.csv")

# Scatterplot
plt.figure(figsize=(7, 5))
plt.scatter(
    df["happiness_average"],
    df["happiness_standard_deviation"],
    alpha=0.4,
    s=20
)

plt.title("Average happiness versus disagreement")
plt.xlabel("happiness_average")
plt.ylabel("happiness_standard_deviation")
plt.tight_layout()
plt.savefig("figures/happiness_vs_sd_scatter.png", dpi=300, bbox_inches="tight")
plt.close()

# Most disagreed-about words have highest std dev
top15 = df.sort_values("happiness_standard_deviation", ascending=False).head(15)

print("15 words with highest happiness_standard_deviation:")
print(top15[["word", "happiness_average", "happiness_standard_deviation"]].to_string(index=False))

print("\nSaved figure to figures/happiness_vs_sd_scatter.png")
