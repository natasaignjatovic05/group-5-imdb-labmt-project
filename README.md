# group-5

AI-Use Disclosure: This project used [ChatGPT] to assist in drafting the pandas data-wrangling functions for load_clean.py and the descriptive statistical calculations for our Week 4 quantitative analysis. Our Data Wrangler verified the cleaning logic by manually checking the handling of null values (--), and our Quantitative Analyst cross-referenced the AI-generated means and standard deviations with manual calculations on a subset of the labMT data. We maintain full responsibility for the code and can explain every line of its implementation.

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

### Preliminary Findings: Regularities & Sampling
Our audit shows that the "Regularities" we find (mathematical patterns) are a snapshot of the 2011 Mechanical Turk socio-technical moment. By **formalizing** our assumptions—such as converting `--` to `pd.NA`—we have "repaired" this **Convenience Sample** so it can be safely repurposed for inquiry into our own text corpora.
