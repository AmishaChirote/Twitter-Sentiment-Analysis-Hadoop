# Twitter Sentiment Analysis using Hadoop MapReduce

The project uses the Sentiment140 Twitter dataset containing approximately 1.6 million tweets. Hadoop MapReduce and Hadoop Streaming were used to process the dataset and generate sentiment analysis results.

## Project Workflow

Twitter Dataset
→ Preprocessing
→ Mapper
→ Reducer
→ Sentiment Analysis Results

## Project Files

### preprocess_dataset.py
Preprocesses the original dataset by:
- Converting text to lowercase
- Removing URLs
- Removing user mentions
- Processing hashtags
- Removing invalid or malformed records

### twitter_mapper_vader.py
Mapper implementation using the VADER sentiment analyzer.

### mapper_lexical.py
Mapper implementation using a lexicon-based sentiment analysis approach with predefined positive and negative word lists.

### twitter_reducer.py
Reducer implementation used to generate:
- Sentiment Distribution
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

### Activity_3_Report.pdf
Final project report containing methodology, results, comparisons and analysis.

### Screenshots
Contains screenshots of:
- Mapper and reducer implementations
- Hadoop execution
- HDFS output verification
- Sentiment analysis results
- Visualization Graphs

## Dataset

Dataset Used: Sentiment140 Twitter Dataset

Approximate Size: 1.6 Million Tweets

Label Encoding:
- 0 = Negative
- 4 = Positive

## Experiments Performed

### Experiment 1 - VADER Sentiment Analysis

Accuracy: 52.42%

### Experiment 2 - Lexicon-Based Sentiment Analysis

Accuracy: 15.71%

### Experiment 3 - Lexicon-Based Sentiment Analysis (Preprocessed Dataset)

Accuracy: 15.75%

## Technologies Used

- Python
- Hadoop MapReduce
- Hadoop Streaming
- HDFS
- VADER Sentiment Analyzer

## Notes

Two sentiment analysis approaches were evaluated:

1. VADER Sentiment Analyzer
2. Lexicon-Based Sentiment Analysis

The lexicon-based model was also tested on both the original and preprocessed datasets to study the effect of preprocessing on model performance.

## Visualizations

The following visualizations were generated from the sentiment analysis results:

- Accuracy Comparison of Models
- Sentiment Distribution Bar Chart
- Sentiment Distribution Pie Chart
