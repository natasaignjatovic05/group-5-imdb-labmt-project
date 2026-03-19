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

scores = reviews["text"].apply(score_review)
scored = pd.concat([reviews, scores], axis=1)

scored.to_csv("data/processed/imdb_scored.csv", index=False)

print("Saved: data/processed/imdb_scored.csv")
print(scored[[
    "review_id",
    "word_count",
    "matched_token_count",
    "mean_happiness"
]].head())
