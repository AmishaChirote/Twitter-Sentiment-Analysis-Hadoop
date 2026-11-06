# Twitter Sentiment Analysis using Hadoop MapReduce

This project was created as part of Activity 3: Sentiment Analysis Pipeline with Social Media Data.

The project uses the Sentiment140 Twitter dataset containing approximately 1.6 million tweets. Hadoop MapReduce and Hadoop Streaming were used to process the dataset and generate sentiment analysis results.

## Project Workflow

Twitter Dataset
→ Preprocessing
→ Mapper
→ Reducer
→ Sentiment Analysis Results

## Files

### preprocess_dataset.py
Used to clean the original dataset by:
- Converting text to lowercase
- Removing URLs
- Removing user mentions
- Processing hashtags
- Removing malformed records
- Removing invalid labels

### twitter_mapper_vader.py
Mapper implementation using the VADER sentiment analyzer.

### twitter_mapper_lexicon.py
Mapper implementation using a lexicon-based sentiment analysis approach.

### twitter_reducer.py
Reducer implementation used to generate:
- Sentiment Distribution
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## Technologies Used

- Python
- Hadoop MapReduce
- Hadoop Streaming
- HDFS
- VADER Sentiment Analyzer

## Dataset

Sentiment140 Twitter Dataset
Approximate size: 1.6 million tweets

## Results

### Model Comparison

| Model | Accuracy |
|---------|---------|
| VADER | 52.42% |
| Lexicon-Based | 15.71% |

### Preprocessing Comparison

| Dataset | Accuracy |
|----------|---------|
| Original Dataset | 15.71% |
| Preprocessed Dataset | 15.75% |
