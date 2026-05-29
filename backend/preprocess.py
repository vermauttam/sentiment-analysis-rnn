import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# Create stemmer object once
ps = PorterStemmer()

# Create stopwords set once
stop_words = set(stopwords.words("english"))


# Remove HTML tags
def remove_html(text):

    text = re.sub(r"<.*?>", "", text)

    return text


# Remove URLs
def remove_urls(text):

    text = re.sub(r"http\S+", "", text)

    return text


# Remove punctuations
def remove_punctuations(text):

    text = re.sub(r"[^A-Za-z0-9\s]", "", text)

    return text


# Remove stopwords and perform stemming in one pass
def remove_stopwords_and_stem(text):

    tokens = word_tokenize(text)

    processed_words = [
        ps.stem(word)
        for word in tokens
        if word not in stop_words
    ]

    return " ".join(processed_words)


# Complete preprocessing pipeline
def preprocess_text(text):

    # lowercase
    text = text.lower()

    # remove html tags
    text = remove_html(text)

    # remove urls
    text = remove_urls(text)

    # remove punctuations
    text = remove_punctuations(text)

    # remove stopwords and stem
    text = remove_stopwords_and_stem(text)

    return text