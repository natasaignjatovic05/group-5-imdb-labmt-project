import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load scored review data
df = pd.read_csv("data/processed/imdb_scored.csv")

# Keep only rows with required values
df = df.dropna(subset=["word_count", "mean_happiness", "review_id"]).copy()

# Ensure stable sorting
df["review_id"] = pd.to_numeric(df["review_id"], errors="coerce")
df["word_count"] = pd.to_numeric(df["word_count"], errors="coerce")
df["mean_happiness"] = pd.to_numeric(df["mean_happiness"], errors="coerce")

df = df.dropna(subset=["review_id", "word_count", "mean_happiness"]).copy()

# Sort by word_count, then review_id for deterministic selection
df_sorted = df.sort_values(by=["word_count", "review_id"], ascending=[True, True]).copy()

# Select 1000 shortest and 1000 longest reviews
short_df = df_sorted.head(1000).copy()
long_df = df_sorted.tail(1000).copy()

short_df["review_length_group"] = "short"
long_df["review_length_group"] = "long"

sample_df = pd.concat([short_df, long_df], ignore_index=True)

# Save sampled comparison dataset
sample_df.to_csv("data/processed/imdb_length_sample.csv", index=False)

# Bootstrap settings
n_boot = 5000
rng = np.random.default_rng(42)

short_scores = short_df["mean_happiness"].to_numpy()
long_scores = long_df["mean_happiness"].to_numpy()

boot_short_means = []
boot_long_means = []
boot_diffs = []

for _ in range(n_boot):
    short_resample = rng.choice(short_scores, size=len(short_scores), replace=True)
    long_resample = rng.choice(long_scores, size=len(long_scores), replace=True)

    short_mean = short_resample.mean()
    long_mean = long_resample.mean()
    diff = long_mean - short_mean

    boot_short_means.append(short_mean)
    boot_long_means.append(long_mean)
    boot_diffs.append(diff)

boot_short_means = np.array(boot_short_means)
boot_long_means = np.array(boot_long_means)
boot_diffs = np.array(boot_diffs)

# Summary table
summary = pd.DataFrame([
    {
        "review_length_group": "short",
        "n": len(short_scores),
        "mean_happiness": short_scores.mean(),
        "std_happiness": short_scores.std(ddof=1),
        "ci_lower": np.percentile(boot_short_means, 2.5),
        "ci_upper": np.percentile(boot_short_means, 97.5),
        "min_word_count": short_df["word_count"].min(),
        "max_word_count": short_df["word_count"].max()
    },
    {
        "review_length_group": "long",
        "n": len(long_scores),
        "mean_happiness": long_scores.mean(),
        "std_happiness": long_scores.std(ddof=1),
        "ci_lower": np.percentile(boot_long_means, 2.5),
        "ci_upper": np.percentile(boot_long_means, 97.5),
        "min_word_count": long_df["word_count"].min(),
        "max_word_count": long_df["word_count"].max()
    }
])

summary.to_csv("tables/length_group_summary.csv", index=False)

# Difference summary
diff_summary = pd.DataFrame([{
    "comparison": "long_minus_short",
    "observed_difference": long_scores.mean() - short_scores.mean(),
    "ci_lower": np.percentile(boot_diffs, 2.5),
    "ci_upper": np.percentile(boot_diffs, 97.5)
}])

diff_summary.to_csv("tables/length_difference_summary.csv", index=False)

# Figure 1: bootstrap difference histogram
plt.figure(figsize=(8, 5))
plt.hist(boot_diffs, bins=40)
plt.axvline(np.percentile(boot_diffs, 2.5), linestyle="--")
plt.axvline(np.percentile(boot_diffs, 97.5), linestyle="--")
plt.axvline(boot_diffs.mean(), linestyle="-")
plt.title("Bootstrap Distribution of Mean Happiness Difference")
plt.xlabel("Mean happiness difference (long - short)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("figures/bootstrap_difference.png", dpi=300)
plt.close()

# Figure 2: boxplot by review length group
plt.figure(figsize=(8, 5))
plt.boxplot(
    [short_scores, long_scores],
    labels=["short", "long"]
)
plt.title("Happiness Scores by Review Length Group")
plt.xlabel("Review length group")
plt.ylabel("Mean happiness")
plt.tight_layout()
plt.savefig("figures/happiness_boxplot.png", dpi=300)
plt.close()

print("Saved:")
print("- data/processed/imdb_length_sample.csv")
print("- tables/length_group_summary.csv")
print("- tables/length_difference_summary.csv")
print("- figures/bootstrap_difference.png")
print("- figures/happiness_boxplot.png")
print(summary)
print(diff_summary)
