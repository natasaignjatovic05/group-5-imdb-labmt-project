import re
import pandas as pd

# Load IMDb reviews
reviews = pd.read_csv("data/processed/imdb_reviews.csv")

# Load cleaned labMT lexicon
labmt = pd.read_csv("data/clean/labMT_clean.csv")

# Build dictionary: word -> happiness score
score_dict = dict(
    zip(
        labmt["word"].astype(str).str.lower(),
        labmt["happiness_average"]
    )
)

def assign_rating_band(rating):
    if 1 <= rating <= 4:
        return "low"
    elif 5 <= rating <= 6:
        return "medium"
    elif 7 <= rating <= 10:
        return "high"
    return None

def tokenize(text):
    if pd.isna(text):
        return []
    return re.findall(r"[a-zA-Z']+", str(text).lower())

def score_review(text):
    tokens = tokenize(text)
    matched_scores = [score_dict[token] for token in tokens if token in score_dict]

    matched_token_count = len(matched_scores)
    mean_happiness = (
        sum(matched_scores) / matched_token_count
        if matched_token_count > 0
        else None
    )

    return pd.Series({
        "matched_token_count": matched_token_count,
        "mean_happiness": mean_happiness
    })

# Add rating band
reviews["rating_band"] = reviews["rating"].apply(assign_rating_band)

# Score each review
scores = reviews["text"].apply(score_review)

# Combine
scored = pd.concat([reviews, scores], axis=1)

# Save output
scored.to_csv("data/processed/imdb_scored.csv", index=False)

print("Saved: data/processed/imdb_scored.csv")
print(scored[[
    "review_id",
    "rating",
    "rating_band",
    "matched_token_count",
    "mean_happiness"
]].head())
