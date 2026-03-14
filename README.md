# Inferring Happiness in IMDb Reviews with labMT

For Mini Project 1, see [mini_project_1.md](mini_project_1.md).

## Overview

This project uses the IMDb Large Movie Review Dataset to study how lexicon based happiness varies across review rating bands. We score each review using the labMT lexicon, compare low, medium, and high rated reviews, and estimate uncertainty around these differences. Our goal is not to treat the lexicon as emotional truth, but to test how well it works as a measurement instrument on a new corpus.

## Research Question

How does labMT based happiness vary across IMDb rating bands, and how certain are these differences?

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
# Dataset 

This project includes the usage of the "IMDb Large Movie review Dataset v1.0", by Maas et al. "2011). The Dataset was interested as a benchmark for sentiment classification. It consists of 50,000 movie overviews divided into: 
***-*** 25,000 training reviews
***-*** 25,000 test reviews
These reviews are categorized into positive and negative reviews.
***-*** 25,000 positive reviews (corresponds to a raring of ≥ 7)
***-*** 25,000 negative reviews (corresponds to a rating of ≤ 4)
Reviews a re stored as single files and follow the fromat: [id]_[rating].txt, where the "id" represents a unique review identifier and the "rating" represents the IMDb rating on a scale from 1-10.
For this project, the labeled reviews following dictionaries are being used:
***-*** "train/pos"
***-*** "train/neg"
***-*** "test/pos"
***-*** "test/neg"
We extracted the review metadata and review texts needed from these files.  

# Data Provenance 


## Methods

### Rating bands

We grouped IMDb reviews into three rating bands using the original numeric `rating` field:

- **low**: ratings 1 to 4
- **medium**: ratings 5 to 6
- **high**: ratings 7 to 10

This grouping gives us a meaningful metadata variable for comparison and supports sampling and inference across review groups.

## Results

We compared labMT-based happiness scores between low-rated IMDb reviews (ratings 1–4) and high-rated IMDb reviews (ratings 7–10). The average happiness score for low-rated reviews was approximately 5.360, while the average for high-rated reviews was approximately 5.474. The observed mean difference (high minus low) was about 0.114.

To assess the stability of this difference, we used bootstrap resampling with 5,000 iterations. The 95% bootstrap confidence interval for the mean difference was approximately [0.1119, 0.1158]. Because this interval does not include 0, the difference is unlikely to be due to random sampling variation alone.

Taken together, these results suggest that high-rated IMDb reviews tend to use slightly more positively weighted vocabulary than low-rated reviews when measured with the labMT lexicon. The difference is small, but it is consistent across resamples.

### Interpretation of the bootstrap distribution

The bootstrap histogram is centered around a positive mean difference of about 0.114, which shows that high-rated reviews consistently score higher than low-rated reviews across repeated resamples. The distribution is relatively narrow, and almost all of its mass lies well above 0. This means the estimated difference is stable rather than being driven by a few unusual samples.

The dashed vertical lines marking the 95% confidence interval lie roughly between 0.112 and 0.116. Since the full interval is positive, we have strong evidence that the average labMT happiness score is higher for high-rated reviews than for low-rated reviews. In other words, the lexicon captures a small but reliable difference in evaluative language between the two rating bands.

### Interpretation of the boxplot

The boxplot shows that the distribution of labMT happiness scores for high-rated reviews is shifted upward relative to low-rated reviews. The median for the high-rated group is clearly above the median for the low-rated group, which matches the numerical result that high-rated reviews have a higher average happiness score.

At the same time, the two groups still overlap. This is important because it shows that not every high-rated review is strongly positive in wording, and not every low-rated review is strongly negative. Reviews often mix praise, criticism, plot summary, irony, and genre-specific vocabulary. The boxplot therefore supports a real group-level difference, while also showing that lexical happiness is only one dimension of review language.

## Critical Reflection

## How to Run
