from textblob import TextBlob
from textblob.en import sentiment


def sentiment_analysis(text):
    # create a TextBlob object
    blob = TextBlob(text)
    # perform sentiment analysis
    sentiment = blob.sentiment
    # Interpretation of results
    if sentiment.polarity > 0:
        return "positive"
    elif sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"


