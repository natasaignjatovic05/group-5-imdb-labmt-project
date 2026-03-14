import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ensure output folder exists
os.makedirs("figures", exist_ok=True)

df = pd.read_csv("data/clean/labMT_clean.csv")

rank_cols = {
    "Twitter": "twitter_rank",
    "GoogleBooks": "google_rank",
    "NYT": "nyt_rank",
    "Lyrics": "lyrics_rank",
}

TOP_N = 5000

# Create mask per corpus
present = {name: df[col].notna() & (df[col] <= TOP_N) for name, col in rank_cols.items()}

# Count how many words appear in each corpus top 5000
counts = {name: int(mask.sum()) for name, mask in present.items()}
print(f"Counts of labMT words present in top {TOP_N}:")
for name, c in counts.items():
    print(f"  {name:10s}: {c}")

# Compute overlap table
corpora = list(rank_cols.keys())
overlap = pd.DataFrame(index=corpora, columns=corpora, dtype=int)
for a in corpora:
    for b in corpora:
        overlap.loc[a, b] = int((present[a] & present[b]).sum())

print("\nPairwise overlap counts (intersection size):")
print(overlap)

# All-four overlap and union
all_four = present["Twitter"] & present["GoogleBooks"] & present["NYT"] & present["Lyrics"]
any_of = present["Twitter"] | present["GoogleBooks"] | present["NYT"] | present["Lyrics"]

print(f"\nWords present in ALL FOUR corpora (top {TOP_N}): {int(all_four.sum())}")
print(f"Words present in AT LEAST ONE corpus (top {TOP_N}): {int(any_of.sum())}")

# Unique-to-corpus counts
unique_counts = {}
for a in corpora:
    others = None
    for b in corpora:
        if b == a:
            continue
        others = present[b] if others is None else (others | present[b])
    unique_counts[a] = int((present[a] & ~others).sum())

print("\nUnique-to-corpus counts:")
for k, v in unique_counts.items():
    print(f"  {k:10s}: {v}")

# Save bar chart
plt.figure(figsize=(7, 4))
plt.bar(list(counts.keys()), list(counts.values()))
plt.title(f"How many labMT words appear in each corpus (top {TOP_N})")
plt.xlabel("Corpus")
plt.ylabel("Count of labMT words present")
plt.tight_layout()
plt.savefig("figures/corpus_presence_bar.png", dpi=300, bbox_inches="tight")
plt.close()

# Save overlap heatmap
overlap_arr = overlap.to_numpy()
plt.figure(figsize=(6, 5))
plt.imshow(overlap_arr)
plt.xticks(range(len(corpora)), corpora, rotation=25, ha="right")
plt.yticks(range(len(corpora)), corpora)
plt.title(f"Overlap counts (top {TOP_N})")
plt.colorbar(label="Intersection size")
for i in range(len(corpora)):
    for j in range(len(corpora)):
        plt.text(j, i, overlap_arr[i, j], ha="center", va="center")
plt.tight_layout()
plt.savefig("figures/corpus_comparison.png", dpi=300, bbox_inches="tight")
plt.close()

print("\nSaved figures to:")
print("  figures/corpus_presence_bar.png")
print("  figures/corpus_comparison.png")
