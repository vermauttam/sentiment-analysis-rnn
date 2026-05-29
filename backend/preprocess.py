import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# Create stemmer object once
ps = PorterStemmer()

# Create stopwords set once
stop_words = set(stopwords.words("english"))


# Remove URLs
def remove_urls(text):

    text = re.sub(r"http\S+", "", text)

    return text


# Remove punctuations
def remove_punctuations(text):

    text = re.sub(r"[^A-Za-z0-9\s]", "", text)

    return text


# Remove HTML tags
def remove_html(text):

    text = re.sub(r"<.*?>", "", text)

    return text


# Remove stopwords
def remove_stopwords(text):

    tokens = word_tokenize(text)

    filtered_words = [
        word for word in tokens
        if word not in stop_words
    ]

    return " ".join(filtered_words)


# Perform stemming
def stemming(text):

    tokens = word_tokenize(text)

    stemmed_words = [
        ps.stem(token)
        for token in tokens
    ]

    return " ".join(stemmed_words)


# Complete preprocessing pipeline
def preprocess_text(text):

    # lowercase
    text = text.lower()

    # remove urls
    text = remove_urls(text)

    # remove punctuations
    text = remove_punctuations(text)

    # remove html
    text = remove_html(text)

    # remove stopwords
    text = remove_stopwords(text)

    # stemming
    text = stemming(text)

    return text