import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# 1. Load data
df = pd.read_csv("data/processed/imdb_reviews.csv")
labmt = pd.read_csv("data/clean/labMT_clean.csv")

print("IMDb columns:", df.columns.tolist())
print("labMT columns:", labmt.columns.tolist())


# 2. Find the correct labMT columns automatically
# adjust if needed after checking printed column names

possible_word_cols = ["word", "term", "token"]
possible_score_cols = ["happiness_average", "happs_avg", "score", "happiness"]

word_col = None
score_col = None

for col in possible_word_cols:
    if col in labmt.columns:
        word_col = col
        break

for col in possible_score_cols:
    if col in labmt.columns:
        score_col = col
        break

print("Using word column:", word_col)
print("Using score column:", score_col)

if word_col is None or score_col is None:
    raise ValueError("Could not find the word or score column in labMT_clean.csv")


# 3. Build lexicon dictionary
labmt_dict = dict(zip(labmt[word_col].astype(str).str.lower(), labmt[score_col]))


# 4. Tokenize and score each review
def tokenize(text):
    if pd.isna(text):
        return []
    return re.findall(r"[a-zA-Z']+", str(text).lower())


def compute_happiness(text):
    tokens = tokenize(text)
    scores = [labmt_dict[word] for word in tokens if word in labmt_dict]

    if len(scores) == 0:
        return np.nan
    return np.mean(scores)


df["happiness_score"] = df["text"].apply(compute_happiness)

print(df[["rating", "happiness_score"]].head())
print("Missing happiness scores:", df["happiness_score"].isna().sum())


# 5. Drop rows with no matched labMT words
df = df.dropna(subset=["happiness_score"])


# 6. Split into rating bands
low = df[(df["rating"] >= 1) & (df["rating"] <= 4)]
high = df[(df["rating"] >= 7) & (df["rating"] <= 10)]

print("Low rating reviews:", len(low))
print("High rating reviews:", len(high))


# 7. Extract scores
low_scores = low["happiness_score"].values
high_scores = high["happiness_score"].values

low_mean = np.mean(low_scores)
high_mean = np.mean(high_scores)
observed_diff = high_mean - low_mean

print("Low mean happiness:", low_mean)
print("High mean happiness:", high_mean)
print("Observed difference (high - low):", observed_diff)


# 8. Bootstrap CI
def bootstrap_difference(low_scores, high_scores, n_boot=5000):
    diffs = []

    for _ in range(n_boot):
        low_sample = np.random.choice(low_scores, size=len(low_scores), replace=True)
        high_sample = np.random.choice(high_scores, size=len(high_scores), replace=True)
        diff = np.mean(high_sample) - np.mean(low_sample)
        diffs.append(diff)

    return np.array(diffs)


boot_diffs = bootstrap_difference(low_scores, high_scores)

ci_lower = np.percentile(boot_diffs, 2.5)
ci_upper = np.percentile(boot_diffs, 97.5)

print("95% bootstrap CI:", ci_lower, ci_upper)


# 9. Save scored data for team use
df.to_csv("data/processed/imdb_reviews_scored.csv", index=False)


# 10. Plot bootstrap distribution
plt.hist(boot_diffs, bins=40)
plt.axvline(ci_lower, linestyle="dashed")
plt.axvline(ci_upper, linestyle="dashed")
plt.axvline(observed_diff)

plt.title("Bootstrap Distribution of Happiness Difference")
plt.xlabel("High rating - Low rating")
plt.ylabel("Frequency")

plt.savefig("figures/bootstrap_difference.png")
plt.show()

