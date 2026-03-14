# Exploring Bias, Disagreement, and Corpus Difference in the labMT 1.0 Lexicon

## Overview

This project studies the labMT 1.0 dataset, the sentiment lexicon used in the hedonometer introduced by Dodds et al. Rather than treating the dataset as a neutral measurement tool, we examine it as both a statistical instrument and a cultural artifact. Our goal is to understand how the lexicon is structured, how its happiness scores are distributed, which words are most contested, and what its design choices reveal about the assumptions built into the dataset. 

## AI Use Disclosure

This project used ChatGPT for limited support with early code drafting, project structuring, and revision of written sections. All cleaning logic, calculations, and interpretive claims were checked by the group. We remain responsible for the code and the arguments presented in this repository, in line with the course requirement that substantial AI use must be disclosed and that students must be able to explain all code and claims in the repo. 

## Credits

| Member | Role |
|--------|------|
| Jack Niu | Repo & workflow lead |
| Alessia Jia | Data wrangler |
| Natasa Ignjatović | Quantitative analyst |
| Ricarda Karallus | Qualitative / close-reading lead |
| Junyi Guo | Provenance & critique lead |
| Yizhi Liu | Editor & figure curator |

### Tools used
Python, pandas, and matplotlib were used for cleaning, analysis, and visualization. ChatGPT was used for limited drafting and revision support. All final code decisions and interpretive claims were reviewed by the group.

### Source
labMT 1.0 dataset provided in course materials.  
Dodds et al. (2011), hedonometer related study.

## Dataset

Our dataset is **labMT 1.0**, a lexicon of **10,222 English words**. Each word has:

- a happiness rank
- an average happiness score on a 1 to 9 scale
- a standard deviation showing disagreement among raters
- frequency ranks across four corpora:
  - Twitter
  - Google Books
  - The New York Times
  - Song Lyrics 

The labMT lexicon is useful because it allows researchers to estimate the emotional tone of large collections of text by matching words in those texts to predefined happiness scores. At the same time, this project treats the lexicon critically. These scores are not universal truths. They reflect judgments produced by a particular annotation process, in a particular historical moment, by a particular rating population. This becomes especially visible when we examine disagreement, culturally loaded words, and corpus-specific vocabulary. 

## Methods

### Loading and cleaning the dataset

The following workflow summarizes how we transformed the raw labMT source file into the cleaned dataset used in all subsequent analyses.

![Data cleaning workflow](figures/data_cleaning_workflow.png)

**Figure 1.** Data cleaning workflow used to transform the raw tab-delimited labMT file into the cleaned dataset used in later analyses.

We loaded the raw tab-delimited file into pandas and cleaned it using Python. Following the assignment brief, we skipped the metadata lines at the top of the file, replaced `--` with `NaN`, converted the numeric columns to numeric types, and verified the final dataset structure. The cleaned dataset contains **10,222 rows and 8 columns**. A cleaned version was saved for reproducibility and reused across the analysis scripts.

In this dataset, a missing corpus rank does not indicate an error; it means that the word is not present in that corpus’s top 5000 list.

### Data dictionary

| Variable | Meaning | Type | Missing values | Note |
|---|---|---|---:|---|
| `word` | The English word evaluated in the lexicon | text | 0 | Primary lexical unit |
| `happiness_rank` | Rank of the word by average happiness | integer | 0 | Lower rank means more positive |
| `happiness_average` | Mean happiness score on a 1 to 9 scale | float | 0 | Main sentiment measure |
| `happiness_standard_deviation` | Standard deviation of ratings | float | 0 | Higher values indicate more disagreement |
| `twitter_rank` | Frequency rank in the Twitter corpus | float | 5222 | `NaN` means absent from Twitter top 5000 |
| `google_rank` | Frequency rank in Google Books | float | 5222 | `NaN` means absent from Google Books top 5000 |
| `nyt_rank` | Frequency rank in The New York Times | float | 5222 | `NaN` means absent from NYT top 5000 |
| `lyrics_rank` | Frequency rank in Song Lyrics | float | 5222 | `NaN` means absent from Lyrics top 5000 |

This table follows the brief’s requirement to document what each column represents, its type, and its missingness. The rank columns contain structural missingness because a word can be absent from one corpus while present in another.

## Sanity Checks

We used several sanity checks to ensure that the cleaned dataset was structurally reliable.

First, after cleaning, the dataset still contained **10,222 rows and 8 columns**, which confirms that parsing the raw file did not distort the expected structure. Second, we checked for duplicate words and found **no duplicated entries**, which supports the internal consistency of the lexicon. Third, we also inspected a random sample of **15 rows** to confirm that the cleaning process correctly preserved word entries, happiness values, and corpus rank columns after skipping the metadata rows and converting `--` into `NaN`. Finally, we examined the most positive and most negative words by `happiness_average` to test whether the ranking looked plausible after import. 

These checks do not prove that the dataset is unbiased or universally valid. They simply show that the file was imported and structured correctly enough for analysis. Even the idea that the top positive and negative words “make sense” depends on shared cultural and historical assumptions, which is one of the central issues this project investigates.

### Top 10 positive words

| word | happiness_average | happiness_standard_deviation |
|---|---:|---:|
| laughter | 8.50 | 0.9313 |
| happiness | 8.44 | 0.9723 |
| love | 8.42 | 1.1082 |
| happy | 8.30 | 0.9949 |
| laughed | 8.26 | 1.1572 |
| laugh | 8.22 | 1.3746 |
| laughing | 8.20 | 1.1066 |
| excellent | 8.18 | 1.1008 |
| laughs | 8.18 | 1.1551 |
| joy | 8.16 | 1.0568 |

### Top 10 negative words

| word | happiness_average | happiness_standard_deviation |
|---|---:|---:|
| terrorist | 1.30 | 0.9091 |
| suicide | 1.30 | 0.8391 |
| rape | 1.44 | 0.7866 |
| terrorism | 1.48 | 0.9089 |
| murder | 1.48 | 1.0150 |
| death | 1.54 | 1.2811 |
| cancer | 1.54 | 1.0730 |
| killed | 1.56 | 1.2316 |
| kill | 1.56 | 1.0529 |
| died | 1.56 | 1.1980 |

The top positive words are laughter, love, and happiness etc. These are words that 
are semantically and culturally unambiguous in mainstream English. 
This makes them "make sense" in the sense that they align with what most 
raters would agree is positive. However, "making sense" here is not neutral: 
it relies on shared cultural norms. A word like **joy** might carry religious 
connotations for some raters that the average score erases. Similarly, the 
most negative words including terrorist, rape, suicide, are socially taboo and 
legally marked. where agreement is partly enforced rather than naturally shared. 
The stability of these scores might reflect social desirability 
more than genuine emotional uniformity.

## Quantitative Results

### 1. Distribution of happiness scores

The first part of our quantitative analysis examined the distribution of `happiness_average` across the entire lexicon. The assignment specifically requires a histogram and summary statistics because the shape of the distribution is part of the interpretive argument, not just background description. 

![Distribution of happiness scores](figures/happiness_histogram.png)

**Figure 2.** Histogram of `happiness_average` across all 10,222 words in labMT 1.0.

#### Summary statistics

| Statistic | Value |
|---|---:|
| Mean | 5.3752 |
| Median | 5.44 |
| Standard deviation | 1.0849 |
| 5th percentile | 3.18 |
| 95th percentile | 7.08 |

The distribution is centered slightly above the neutral midpoint of 5, which suggests that the lexicon leans mildly positive overall. Most words cluster around the middle range rather than the extremes. One interesting pattern is that the dataset is not symmetrically balanced around neutrality. Instead, it seems somewhat tilted toward moderately positive language. This matters because any later use of labMT as a measurement tool inherits this lexical distribution. The instrument does not begin from a neutral emotional baseline. 

### 2. Disagreement and contested words

The dataset also includes `happiness_standard_deviation`, which allows us to ask not only how positive or negative a word is on average, but also how much raters disagreed about it. The brief explicitly requires a scatterplot and a discussion of why some words are contested. 

![Average happiness versus disagreement](figures/happiness_vs_sd_scatter.png)

**Figure 3.** Scatterplot of `happiness_average` against `happiness_standard_deviation`.

The scatterplot suggests that the highest disagreement tends to appear in the middle range rather than at the most positive or most negative extremes. This makes intuitive sense. Strongly positive or negative words are often easier to rate consistently, while ambiguous, taboo, ideological, or culturally loaded words invite more varied judgments. High standard deviation therefore should not be dismissed as noise. In many cases, it is analytically interesting because it reveals unstable or socially contested meanings. 

### 15 most contested words

| word | happiness_average | happiness_standard_deviation |
|---|---:|---:|
| fucking | 4.64 | 2.9260 |
| fuckin | 3.86 | 2.7405 |
| fucked | 3.56 | 2.7117 |
| pussy | 4.80 | 2.6650 |
| whiskey | 5.72 | 2.6422 |
| slut | 3.57 | 2.6300 |
| cigarettes | 3.31 | 2.5997 |
| fuck | 4.14 | 2.5794 |
| mortality | 4.38 | 2.5546 |
| cigarette | 3.09 | 2.5163 |
| motherfuckers | 2.51 | 2.4675 |
| churches | 5.70 | 2.4599 |
| motherfucking | 2.64 | 2.4558 |
| capitalism | 5.16 | 2.4524 |
| porn | 4.18 | 2.4302 |

Five especially revealing contested words are **whiskey**, **churches**, **capitalism**, **porn**, and **fucked**. These words are contested for different reasons. **Whiskey** can be associated with pleasure, sociability, addiction, or self-destruction. **Churches** and **capitalism** point more directly to ideological disagreement. **Porn** combines taboo, desire, shame, and moral judgment. **Fucked** can function as insult, exaggeration, expression of frustration, or even intensifier. These examples show that disagreement often emerges not from poor annotation, but from the fact that words can carry multiple meanings across contexts and communities. 

### 3. Corpus comparison

The corpus rank columns allow us to compare what counts as common language across different communication environments. The assignment asks for at least one plot or table showing corpus differences and overlap. 

![Corpus comparison](figures/corpus_comparison.png)

**Figure 4.** Comparison of labMT word presence and overlap across Twitter, Google Books, The New York Times, and Song Lyrics.

Pairwise overlap between the top 5000 words in each corpus:

| Pair | Shared words |
|---|---:|
| Twitter and Google Books | 2696 |
| Twitter and NYT | 2881 |
| Twitter and Lyrics | 3127 |
| Google Books and NYT | 3414 |
| Google Books and Lyrics | 2368 |
| NYT and Lyrics | 2241 |

Additional overlap findings:

- words present in all four corpora: **1816**
- words present in at least one corpus: **9895**

Unique to each corpus:

- Twitter: **952**
- Google Books: **1115**
- NYT: **1043**
- Lyrics: **1486**

Google Books and NYT share the largest overlap, which suggests a closer relationship between edited print language and institutional news discourse. Lyrics appears to be the most distinct corpus, likely because it reflects more expressive and genre-specific language than edited print or news text. Twitter overlaps relatively strongly with Lyrics, which fits their more informal and conversational style. A concrete example is **lol**, which appears prominently in Twitter language but is not common in Google Books. This illustrates the broader point that “common language” depends heavily on where language is sampled from. 

## Qualitative Exhibit: The Lexicon as a Cultural Artifact

Following the brief, we created a small exhibit of 20 words across four categories: very positive, very negative, highly contested, and weird or culturally loaded. 

| word | category | happiness_average | happiness_standard_deviation |
|---|---|---:|---:|
| love | positive | 8.42 | 1.1082 |
| successful | positive | 8.16 | 1.0759 |
| laughing | positive | 8.20 | 1.1066 |
| joy | positive | 8.16 | 1.0568 |
| happiness | positive | 8.44 | 0.9723 |
| suffer | negative | 2.08 | 1.3827 |
| killed | negative | 1.56 | 1.2316 |
| rape | negative | 1.44 | 0.7866 |
| terrorist | negative | 1.30 | 0.9091 |
| virus | negative | 2.08 | 1.3377 |
| fucked | contested | 3.56 | 2.7117 |
| shots | contested | 3.32 | 2.0146 |
| omfg | contested | 4.52 | 2.0726 |
| oprah | contested | 5.42 | 2.0513 |
| christ | contested | 6.16 | 2.3067 |
| ipod | culturally_loaded | 6.56 | 1.7515 |
| taxes | culturally_loaded | 2.70 | 1.5286 |
| usa | culturally_loaded | 6.58 | 1.8416 |
| saddam | culturally_loaded | 2.48 | 1.5680 |
| rainbow | culturally_loaded | 8.10 | 0.9949 |

This exhibit makes clear that the lexicon is not just a neutral list of words with stable emotional values. Some entries, such as **love** or **terrorist**, are relatively unambiguous in mainstream English and therefore show more stable emotional ratings. Others are more revealing. **Saddam**, **USA**, **taxes**, and **rainbow** are not emotionally self-evident in the same way. Their ratings likely reflect political framing, national identity, media exposure, and cultural associations carried by the Mechanical Turk raters. This is exactly the type of inference our supervisor said needed to be developed more deeply: the scores do not simply describe the words, they also reveal something about the people who rated them and the historical environment in which they did so. **iPod** is especially useful because it exposes the temporal specificity of the lexicon. It reflects a particular technological moment rather than a timeless lexical property. 

## Critical Reflection

### Reconstructing the pipeline

In our own words, the dataset pipeline can be reconstructed as follows:

1. A lexicon of common English words was assembled.
2. The words were rated for happiness by Amazon Mechanical Turk participants on a 1 to 9 scale.
3. The ratings were aggregated into average happiness scores and standard deviations.
4. The words were linked to corpus-specific rank columns from Twitter, Google Books, The New York Times, and Song Lyrics.
5. In our own workflow, we loaded the raw file, skipped metadata rows, replaced `--` with missing values, converted numeric fields, and saved a cleaned version for reproducible analysis. 

### Five consequences of the dataset’s design choices

**1. Words are rated in isolation rather than in context.**  
This makes large scale sentiment scoring possible, but it also strips away syntax, irony, speaker position, and neighboring words. 
concrete example: **shots** can refer to medicine, alcohol, sports, or gun violence, but the dataset compresses those meanings into one average score. 

**2. The ratings come from a specific annotator population at a specific historical moment.**  
This makes the dataset historically interesting, but it also means that some scores capture rater norms rather than stable lexical meaning. 
concrete example: The scores for **Saddam**, **USA**, and **rainbow** are especially suggestive here. 

**3. Disagreement is stored numerically as standard deviation.**  
This is useful because it reveals contested words, but the number alone cannot explain why a word is contested. concrete example: Words like **capitalism** and **churches** require qualitative interpretation alongside the plot. 

**4. Corpus coverage is structurally uneven.**  
A missing corpus rank is not an error. It shows that different communication environments privilege different vocabularies. 
concrete example: That is why a term like **lol** can feel central in Twitter but absent from Google Books. 

**5. The lexicon leans mildly positive overall.**  
This means the tool is not emotionally neutral at baseline. Since the distribution is centered above 5, later hedonometer analyses inherit a slightly positive lexical environment from the start. 

## Instrument Note

If we were to use labMT 1.0 as an instrument today, we would trust it most for broad aggregate comparisons across large English text collections. It is useful for detecting general shifts in emotional vocabulary, for comparing corpora at a high level, and for identifying words that are relatively stable versus highly contested. It is especially useful when paired with qualitative interpretation rather than treated as self-sufficient.

At the same time, we would refuse to treat its scores as universal emotional truth. The lexicon is based on isolated words rather than contextualized language, so it cannot reliably capture irony, sentence meaning, speaker intention, or political nuance. It also reflects a particular rating population and moment in time, which means that culturally loaded words may say as much about the raters as about the words themselves.

If rebuilt today, we would improve the instrument in three ways. First, we would document the rater population more transparently. Second, we would include phrase-level or sentence-level ratings for ambiguous terms. Third, we would account more explicitly for temporal change and community-specific language use. In this sense, labMT remains useful, but only when its limits are made visible rather than ignored. 

## How to Run

Install dependencies from `requirements.txt`, then run the scripts in the following order:

```bash
pip install -r requirements.txt
python src/load_clean.py
python src/2_1_distrib_happ_score.py
python src/2_2_contested.py
python src/2_3_corpus_comparison.py
python src/3_1_word_exhibit.py

Repository structure:

- `data/` contains the raw dataset and cleaned output
- `src/` contains the Python scripts
- `figures/` contains the plots and workflow figure used in this README
- `tables/` stores exported tables referenced in the analysis

To ensure reproducibility, all plots should be saved into `figures/` and all outputs should be generated from the scripts above in a clean environment using only `requirements.txt`.
