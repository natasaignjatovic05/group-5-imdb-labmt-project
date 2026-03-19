# Inferring Happiness in long and short IMDb Reviews with labMT

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
 
### Dataset

We use the IMDb Large Movie Review Dataset, a publicly available English-language corpus of movie reviews. The dataset includes review text and metadata such as sentiment split, rating, and review length. For this project, we use the processed review file generated from the raw dataset and focus on the `word_count` metadata variable to define short and long review groups.

### Dataset Pipeline

```mermaid
flowchart TD
    A[Raw IMDb review files] --> B[Extract review text and metadata]
    B --> C[Create processed review dataset]
    C --> D[Tokenize review text]
    D --> E[Match tokens to labMT lexicon]
    E --> F[Compute matched token count and mean happiness]
    F --> G[Sort by word_count and review_id]
    G --> H[Select 1,000 shortest reviews]
    G --> I[Select 1,000 longest reviews]
    H --> J[Bootstrap comparison]
    I --> J
    J --> K[Figures and interpretation]

## Results



### Interpretation of the bootstrap distribution



The bootstrap histogram is centered around a positive mean difference of about 0.114, which shows that high-rated reviews consistently score higher than low-rated reviews across repeated resamples. The distribution is relatively narrow, and almost all of its mass lies well above 0. This means the estimated difference is stable rather than being driven by a few unusual samples.

The dashed vertical lines marking the 95% confidence interval lie roughly between 0.112 and 0.116. Since the full interval is positive, we have strong evidence that the average labMT happiness score is higher for high-rated reviews than for low-rated reviews. In other words, the lexicon captures a small but reliable difference in evaluative language between the two rating bands.

### Interpretation of the boxplot

The boxplot shows that the distribution of labMT happiness scores for high-rated reviews is shifted upward relative to low-rated reviews. The median for the high-rated group is clearly above the median for the low-rated group, which matches the numerical result that high-rated reviews have a higher average happiness score.

At the same time, the two groups still overlap. This is important because it shows that not every high-rated review is strongly positive in wording, and not every low-rated review is strongly negative. Reviews often mix praise, criticism, plot summary, irony, and genre-specific vocabulary. The boxplot therefore supports a real group-level difference, while also showing that lexical happiness is only one dimension of review language.

## Critical Reflection



## How to Run
```bash
pip install -r requirements.txt

python src/load_clean.py 
python src/fetch_data.py 
python src/stats_analysis.py
```
