# group-5

AI-Use Disclosure: This project used [ChatGPT] to assist in drafting the pandas data-wrangling functions for load_clean.py and the descriptive statistical calculations for our Week 4 quantitative analysis. Our Data Wrangler verified the cleaning logic by manually checking the handling of null values (--), and our Quantitative Analyst cross-referenced the AI-generated means and standard deviations with manual calculations on a subset of the labMT data. We maintain full responsibility for the code and can explain every line of its implementation.

## Group Members
Natasa Ignjatović, Alessia Jia, Yizhi Liu, Jack Niu, Ricarda Karallus, Junyi Guo.

## Dataset Description

This project adopts a reparative approach  to the labMT sentiment lexicon. Rather than a 'paranoid' reading that merely seeks to expose the biases of Mechanical Turk data , we treat this tool as a composition. By assembling a reproducible Python pipeline and a structured Model Card, we enable the dataset to be 'repaired' and repurposed for humanistic inquiry into the emotional textures of cultural texts.

The dataset contains 10,222 high-frequency English words. Each word was rated for happiness by 50 participants on Amazon Mechanical Turk using a scale from 1 (least happy) to 9 (most happy). The average score represents the perceived emotional valence of each word.

In addition to happiness ratings, the dataset includes frequency ranks of words in four different corpora:

- Twitter  
- Google Books  
- The New York Times  
- Song Lyrics  

These frequency ranks indicate how often each word appears in different types of texts.

The labMT dataset allows researchers to estimate the overall happiness of large collections of text by averaging the happiness scores of the words they contain.

## Data Preparation: Formalization

"In this project, 'cleaning' is understood as formalization: the process of making our humanistic and interpretive assumptions explicit in code."

### Cleaning Process

The labMT 1.0 dataset was cleaned and prepared for analysis through the following steps:

1. **Metadata removal**  
   The first rows of the file contain descriptive metadata rather than tabular data. These rows were skipped to ensure proper parsing of the dataset.

2. **Handling missing values**  
   The dataset uses "--" to indicate that a word does not appear in a specific corpus (e.g., Twitter, Google Books, NYT, or Lyrics). These entries were replaced with `NaN` to ensure consistent handling of missing values in subsequent analysis.

3. **Type conversion**  
   All numeric columns (happiness scores and frequency ranks) were converted to appropriate numeric data types. This ensures accurate statistical calculations and prevents unintended string-based operations.

4. **Data validation**  
   The dataset structure was verified after cleaning. The final cleaned dataset contains 10,222 rows and 8 columns.

5. **Reproducibility**  
   A cleaned version of the dataset was saved to the `data/clean/` directory to ensure reproducibility and consistent use across analysis scripts.

The cleaning process ensures that the dataset is structured in one way that allows reliable quantitative analysis while preserving information about specific corpus coverage.

### Missing Values

Several frequency rank columns contain missing values. 

This happens because many words do not appear in all corpora.  
For example, some words may appear in Twitter but not in song lyrics or news articles.

Keeping these missing values allows us to see differences between corpora.

### Data Dictionary

- **word**: The English word evaluated in the survey.

- **happiness_rank**: The rank of the word based on its average happiness score.

- **happiness_average**: The mean happiness rating on a 1–9 scale.

- **happiness_standard_deviation**: The standard deviation of ratings, indicating the level of agreement among participants.

- **twitter_rank**: Frequency rank of the word in the Twitter corpus.

- **google_rank**: Frequency rank of the word in the Google Books corpus.

- **nyt_rank**: Frequency rank of the word in the New York Times corpus.

- **lyrics_rank**: Frequency rank of the word in the song lyrics corpus.

## Data provenance & critical reflection
**Provenance (how the dataset was produced in this project)**  
Our core dataset is the labMT 1.0 sentiment lexicon (10,222 English words). Each word has an average happiness score on a 1–9 scale based on ratings from 50 Amazon Mechanical Turk participants. The dataset also includes frequency ranks for the same words across four corpora (Twitter, Google Books, The New York Times, and Song Lyrics).  

For this project, we did not re-collect any ratings. We built a small, reproducible pipeline that turns the raw file into a clean CSV used by all analysis scripts. In practice, we removed non-tabular metadata rows and converted “--” to missing values (NaN) to represent “not present in that corpus”. We then converted numeric columns into numeric types and validated that the cleaned output keeps the expected structure (10,222 rows, 8 columns). The cleaned dataset is saved to `data/clean/`.

**Critical reflection (bias, limitations, and consequences)**  
These happiness scores are not “ground truth”; they are a snapshot of how a specific rater group judged words at a specific time. Different populations, time periods, or communities may rate the same word differently, so our numbers should be treated as estimates rather than universal facts.  

The dataset is word-level and removes context, so some words are naturally ambiguous or contested (irony, slang, taboo, political terms). For example, “shot” can refer to alcohol, vaccination, or gun violence, and “iPod” is time-specific, so the same token can carry different affect depending on context and historical moment. High standard deviation can reflect real disagreement, not just noise. Also, the rank columns contain structural missingness: a NaN means the word does not appear in that corpus, not that the dataset is broken. This makes it easy to compare vocabulary coverage across corpora, but results can shift if missing values are dropped without care. Overall, it works well for broad distribution patterns, but for contested words we still need short qualitative examples to avoid over-interpreting the numbers. In our write-up, we flag high-SD words and treat them as prompts for close reading rather than treating the mean score as a final answer.

## Transition to Quantitative Analysis: Distributions & Ontology
Following the **Theory of Data**, we recognize that our cleaned CSV is not a perfect mirror of human language, but a **sample**. We move from treating these scores as "matters of fact" to a **distribution**, acknowledging that "the word is not the thing".

### The Four Moments of the labMT Lexicon
We audited the `happiness_average` distribution to define the "shape" of our dataset:

| Moment | Metric | Value | Humanistic Interpretation |
| :--- | :--- | :--- | :--- |
| **1st** | **Mean** | [Insert #] | The central "vibe" or baseline happiness of the sample. |
| **2nd** | **Variance** | [Insert #] | The level of "uncertainty" or spread in the word ratings. |
| **3rd** | **Skewness** | [Insert #] | Identifies if the lexicon is lopsided (e.g., biased toward happy words). |
| **4th** | **Kurtosis** | [Insert #] | Indicates the presence of "outlier" words with extreme scores. |

In the following section, we examine the distribution of happiness scores and identify key patterns within the dataset.

### Interpret the histogram in words
### Is the distribution centered? skewed? clustered?
### Identify 1 pattern you did not expect.

The scatterplot shows a large cluster of words around happiness_average ≈ 5–7 with moderate disagreement (SD ≈ 1.1–1.7), meaning most words are rated somewhat positive and people mostly agree. Disagreement is highest for mid-range/neutral-ish words (~3–6) and generally lower at the extremes, where words have clearer emotional meanings. A surprising pattern is the dense “valley” of very low SD near happiness_average ≈ 5, suggesting many neutral everyday words are rated quite consistently.

### Pick 5 of the “most disagreed-about” words and discuss why they might be contested:
### – ambiguity / multiple meanings
### – cultural references
### – slang and time period
### – irony, profanity, or taboo

1) fucking / fuck / fuckin / fucked / motherfucking / motherfuckers (profanity + context + intensity)

These words are context-dependent:
	•	Some people rate them very negative because they’re rude/aggressive/offensive.
	•	Others rate them less negative (or even positive-ish) because they’re used as emphasis (“that’s fucking amazing”), joking, or in friendly slang.
That split creates huge disagreement → high standard deviation.

2) pussy (multiple meanings + taboo)

This word has very different meanings:
	•	As an insult (“coward”), it’s negative.
	•	As a sexual term, people might react with anything from positive to negative depending on comfort, gender norms, and values.
Because it’s taboo and ambiguous, ratings spread out a lot.

3) slut (taboo + cultural norms)

Strong moral/cultural judgement is involved:
	•	Some see it as a harsh insult (very negative).
	•	Others may see it as reclaimed language in some contexts, or interpret it differently based on culture/generation.
That leads to big disagreement.

4) porn (taboo + personal values)

People’s reactions differ a lot:
	•	Some associate it with shame/exploitation/addiction → negative.
	•	Others associate it with pleasure/freedom/neutral media → less negative or even positive.
So responses vary widely → high SD.

5) capitalism (cultural/political associations)

This one is interesting because it’s not “emotional” in a simple way:
	•	Some connect it to opportunity/freedom/success → positive.
	•	Others connect it to inequality/exploitation → negative.
It’s contested because it’s tied to ideology and lived experience, not a single emotion.

### Connect the qualitative interpretation to the quantitative pattern

A strong pattern in the list is that the highest-disagreement words are mostly:
	•	taboo/profanity/sex words, or
	•	culture/ideology-loaded words

Those categories usually create polarized reactions, meaning some raters give very low scores and others give higher scores. That "split” produces a large standard deviation, which is exactly this measure captures: disagreement among raters.


### Interpret what your plot suggests about the four corpora.
The overlap heatmap shows that Google Books and the NYT share the most vocabulary in their top-5000 lists (3414 shared words), suggesting a more similar “edited/formal” register. Lyrics is the most distinct corpus, with the smallest overlaps—especially with NYT (2241)—indicating more genre-specific, emotional, and stylistic language. Twitter sits between them and overlaps relatively strongly with Lyrics (3127), consistent with both being more informal and conversational.

### Give one concrete example of a word that is “common” in one corpus but missing in another, and interpret why that might be.
Example word: lol — It’s very common on Twitter (rank 42) because it’s internet slang used for quick reactions and humor in casual conversation. It’s missing from Google Books’ top words because published books are more formal/edited and rarely use abbreviations like “lol,” so it doesn’t appear frequently enough to rank in that corpus.
### Preliminary Findings: Regularities & Sampling
Our audit shows that the "Regularities" we find (mathematical patterns) are a snapshot of the 2011 Mechanical Turk socio-technical moment. By **formalizing** our assumptions—such as converting `--` to `pd.NA`—we have "repaired" this **Convenience Sample** so it can be safely repurposed for inquiry into our own text corpora.


## Qualitative exploration: close reading the lexicon as a cultural artifact
### Build a small "exhibit" of words

### code task: create a small table of 20 words 
| **word** | **category** | **happiness_average** | **happiness_standard_deviation** |
| :--- | :--- | :--- | :--- |
| **love** | positive  |8.42 | 1.1082 |
| **successfull** | positive | 8.16 | 1.08597 |
| **laughing** | positive | 8.27 | 1.066 |
| **joy** | positive | 8.16 | 1.0568 |
| **happiness** | positive | 8.44 | 0.9723 |
| **suffer** | negative | 2.08 | 1.3827 |
| **killed** | negative | 1.56 | 1.2316 |
| **rape** | negative | 1.44 | 0.7866 |
| **terrorist** | negative | 1.30 | 0.9091 |
| **virus** | negative | 2.08 | 1.3377 |
| **fucked** | contested | 3.56 | 2.7117 |
| **shots** | contested | 3.32 | 2.0146 |
| **omfg** | contested | 4.52 | 2.0726 |
| **oprah** | contested | 5.42 | 2.0513 |
| **christ** | contested | 6.16 | 2.3067 |
| **ipod** | culturally_loaded | 6.56 | 1.7515 |
| **taxes** | culturally_loaded | 2.70 | 1.5286 |
| **usa** | culturally_loaded | 6.58 | 1.8416 |
| **saddam** | culturally_loaded | 2.48 | 1.568 |
| **rainbow** | culturally_loaded | 8.10 | 0.9949 |

### Intepretation 

The positive words are often associated with emotions like “love” and “joy”. These are universal emotions which are not dependent on cultural backgrounds and can represent a wide range of individual experiences. The negative words are often associated with violence and suffering. These words are likely unambiguous, and the negative association is universal among individuals. 

Words with high standard deviation imply that individuals associate them with different meanings and that the words themselves can be overly simplified without context. This can have various reasons; for instance, the word “Christ” can exhibit significant variations across cultural and religious backgrounds. Whereas the word “shot” can have different meanings depending on the interpretation of the word itself. The word can be associated with alcoholic shots, but also with gun violence or vaccinations. Lastly, the words “fucked” and “omfg” can be used both as a negative impression as well as an exaggeration, which depends not only on the context but also on the age of the person. 

Some words also carry historical and cultural meanings. These can also depend on their time period; for example, “iPod” might have a different happiness score nowadays as it is not commonly used anymore. The same goes for country rankings(“USA”), as international relations and reputations can change notably over time. Some words in the list were quite surprising, such as “Saddam”, which likely refers to the political figure Saddam Hussein and was clearly ranked negatively. 

These different categories underscore, and examples demonstrate how the words themselves are shaped by emotional, historical, political and also cultural meaning. Furthermore, a high standard deviation suggests that a word is likely to have very different interpretations and associations among individuals.

# Inference - Happiness Dynamics in Movie Reviews 

## Research Question ( ? )

## Dataset ( role 2 )

## Data Provenance ( role 2 )

## Methods ( role 3 & 4 ) 

### Hendonometer Implimentations ( role 3) 

### Statistical Analysis ( role 4 ) 

## Results

### Figures (role 5 )

### Statistical Findings ( Role 4 ) 

## Limitations ( ? ) 

## Reproducibility (Role 1 )

### References


