# 2.2 Code tasks
# Plot happiness_average (x-axis) vs happiness_standard_deviation (y-axis) as a scatterplot.
# Identify the 15 words with the highest standard deviation.

import pandas as pd
import matplotlib.pyplot as plt

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

plt.title("Disagreement")
plt.xlabel("happiness_average")
plt.ylabel("happiness_standard_deviation")
plt.tight_layout()
plt.show()

# Most "disagreed-about" words have highest std dev
top15 = df.sort_values("happiness_standard_deviation", ascending=False).head(15)

print("15 words with highest happiness_standard_deviation:")
print(top15[["word", "happiness_average", "happiness_standard_deviation"]].to_string(index=False))