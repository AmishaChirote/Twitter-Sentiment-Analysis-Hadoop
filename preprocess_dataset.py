import csv
import re

INPUT_FILE = "/home/hduser/Downloads/twitter_Amisha.csv"

OUTPUT_FILE = "/home/hduser/Downloads/twitter_preprocessed.csv"

def clean_tweet(tweet):

    # Convert to lowercase
    tweet = tweet.lower()

    # Remove URLs
    tweet = re.sub(r"http\S+|www\S+", "", tweet)

    # Remove Twitter mentions
    tweet = re.sub(r"@\w+", "", tweet)

    # Remove hashtag symbol but preserve the word
    tweet = tweet.replace("#", "")

    # Remove extra spaces
    tweet = " ".join(tweet.split())

    return tweet

total_rows = 0
processed_rows = 0
missing_tweets = 0
invalid_labels = 0
malformed_rows = 0

with open(INPUT_FILE, "r", encoding="utf-8-sig",
          errors="replace", newline="") as infile:

    reader = csv.reader(infile)

    with open(OUTPUT_FILE, "w", encoding="utf-8",
              newline="") as outfile:

        writer = csv.writer(outfile)

        for row in reader:

            total_rows += 1

            # Check required columns
            if len(row) <= 5:
                malformed_rows += 1
                continue

            # Extract sentiment label
            label = row[0].strip()

            # Keep only valid labels
            if label not in ["0", "4"]:
                invalid_labels += 1
                continue

            # Extract tweet
            tweet = row[5].strip()

            # Remove missing tweets
            if not tweet or tweet.lower() in ["nan", "null", "none"]:
                missing_tweets += 1
                continue

            # Apply basic preprocessing
            cleaned_tweet = clean_tweet(tweet)

            # Remove empty tweets after cleaning
            if not cleaned_tweet:
                missing_tweets += 1
                continue

            # Replace original tweet with cleaned tweet
            row[5] = cleaned_tweet

            # Save the complete CSV row
            writer.writerow(row)

            processed_rows += 1

print("\n========== DATA PREPROCESSING REPORT ==========")

print("Original Dataset Rows:", total_rows)

print("Successfully Processed Rows:", processed_rows)

print("Missing Tweets Removed:", missing_tweets)

print("Invalid Labels Removed:", invalid_labels)

print("Malformed Rows Removed:", malformed_rows)
