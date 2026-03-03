# group-5
## Dataset Description

This project uses the labMT 1.0 dataset (Language Assessment by Mechanical Turk), developed by Dodds et al. (2011) to construct a large-scale “hedonometer” for measuring happiness in text.

The dataset contains 10,222 high-frequency English words. Each word was rated for happiness by 50 participants on Amazon Mechanical Turk using a scale from 1 (least happy) to 9 (most happy). The average score represents the perceived emotional valence of each word.

In addition to happiness ratings, the dataset includes frequency ranks of words in four different corpora:

- Twitter  
- Google Books  
- The New York Times  
- Song Lyrics  

These frequency ranks indicate how often each word appears in different types of texts.

The labMT dataset allows researchers to estimate the overall happiness of large collections of text by averaging the happiness scores of the words they contain.
## Data Preparation

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

### Transition to Quantitative Analysis

With the dataset cleaned and properly structured, we can now proceed to quantitative exploration. 

The preparation steps ensure that the happiness scores and frequency ranks are stored in consistent numeric formats, allowing reliable statistical analysis. 

In the following section, we examine the distribution of happiness scores and identify key patterns within the dataset.