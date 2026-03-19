# Inferring Happiness in Long and Short IMDb Reviews with labMT
For Mini Project 1, see [mini_project_1.md](mini_project_1.md).

## Overview

This project uses the IMDb Large Movie Review Dataset to study whether review length is associated with differences in lexicon based happiness. We extracted review text and metadata from the raw IMDb files, scored each review with the labMT lexicon, and then compared the 1,000 shortest reviews with the 1,000 longest reviews. Our goal is not to treat the lexicon as emotional truth, but to test how well it works as a measurement instrument on a new corpus.

## Research Question

Do short and long IMDb reviews differ in lexicon based happiness?

## Methods

### Review length groups

To study whether review length is associated with differences in lexical happiness, we used the existing `word_count` variable in the processed IMDb dataset.

We operationalized review length as follows:

- **short reviews**: the 1,000 reviews with the lowest word counts
- **long reviews**: the 1,000 reviews with the highest word counts

To make this selection reproducible, we sorted reviews first by `word_count` and then by `review_id`, and then took the first 1,000 rows as the short group and the last 1,000 rows as the long group.

### Population and sample

The full IMDb review corpus in our processed dataset is the broader corpus we work from. For inference, we selected two samples from that corpus: the 1,000 shortest reviews and the 1,000 longest reviews. We then used bootstrap resampling within these two groups to estimate the stability of the difference in mean happiness.

### Happiness scoring

We used the cleaned labMT lexicon to assign happiness scores to words appearing in each IMDb review. For every review, we tokenized the text, matched tokens against the lexicon, counted the number of matched words, and calculated the mean happiness score across all matched tokens. Tokens not present in the lexicon were treated as out of vocabulary and were excluded from the score.

## AI Use Disclosure

This project used ChatGPT for limited support with workflow planning, debugging, and drafting. All code, results, and interpretive claims were checked by the group. We remain responsible for the contents of this repository.

## Credits

| Member | Role |
|--------|------|
| Ricarda/Jack | Repo & workflow lead |
| Ricarda | Data acquisition lead |
| Jack/Andy | Measurement lead |
| Junyi/Alessia | Stats & sampling lead |
| Natasha | Visualisation lead |

## Corpus and Provenance

### Dataset Pipeline

We use the IMDb Large Movie Review Dataset, a publicly available English-language corpus of movie reviews. The dataset includes review text and metadata such as sentiment split, rating, and review length. For this project, we use the processed review file generated from the raw dataset and focus on the `word_count` metadata variable to define short and long review groups.

<img width="964" height="2114" alt="mermaid-diagram" src="https://github.com/user-attachments/assets/1a4eab5d-4301-45b4-8fd7-e1028a4ff5df" />

### Data Provenance

The dataset created by Andrew L. Maas et al. was published in 2011 and is publicly available from the Stanford AI Lab.

Within the raw dataset, each review is stored as a text file in a folder structure indicating its sentiment (`pos` or `neg`) and dataset split (`train` or `test`). Each filename contains the review ID and rating.

To process the raw data, an extraction script (`src/fetch_data.py`) was used to create the following variables:

- `review_id`
- `rating`
- `sentiment`
- `split`
- `word_count`
- `text`

The scored dataset extends this with:

- `matched_token_count`
- `mean_happiness`

### Ethics

The dataset is publicly available and commonly used for research on sentiment analysis. It contains review text but no direct personal identifying information about reviewers. Our analysis focuses only on the textual content and metadata distributed with the public dataset, and it is used here solely for academic research purposes.

## Results

We compared the 1,000 shortest and the 1,000 longest IMDb reviews using `word_count` as the metadata variable that defines review length. The observed mean happiness score for the short review group was [INSERT], while the observed mean happiness score for the long review group was [INSERT]. The observed difference in means (long minus short) was [INSERT]. The 95% bootstrap confidence interval for this difference was [INSERT, INSERT].

### Interpretation of the bootstrap distribution

![Bootstrap Difference]

The bootstrap histogram shows the distribution of the difference in mean happiness between the long and short review groups across repeated resamples. If the distribution is centered above 0, this indicates that long reviews tend to have higher mean happiness scores than short reviews. If it is centered below 0, the opposite is true. The width of the distribution shows how stable that estimated difference is under repeated sampling.

### Interpretation of the boxplot

![Boxplot]

The boxplot compares the distribution of review-level happiness scores in the short and long review groups. It shows whether one group tends to be systematically higher than the other, while also revealing how much overlap remains between them. This helps us evaluate whether any observed difference is broad and consistent or driven only by a small part of the sample.

## Critical Reflection

This project uses a lexicon based method to measure review-level happiness in IMDb movie reviews. The method is useful for broad aggregate comparison because it provides a reproducible way to score large volumes of text using a fixed word list. At the same time, it has clear limitations. labMT scores words in isolation and therefore cannot fully capture context, negation, sarcasm, or narrative structure.

A second limitation concerns the operationalization of review length. By selecting the 1,000 shortest and 1,000 longest reviews, we create a strong contrast that is useful for comparison, but this also simplifies the full range of review lengths in the corpus. The resulting comparison should therefore be interpreted as a contrast between extreme groups rather than a complete model of how review length relates to lexical happiness across all IMDb reviews.

Finally, bootstrap resampling is only meaningful here because we explicitly treat the short and long groups as samples drawn from the broader IMDb review corpus in our processed dataset. The bootstrap distribution therefore helps us evaluate the stability of the observed mean difference under repeated resampling of these selected groups.


## How to Run
```bash
pip install -r requirements.txt

python src/load_clean.py
python src/fetch_data.py
python src/02_score_reviews.py
python src/stats_analysis.py
