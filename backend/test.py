from preprocess import preprocess_text

text = "This movie was AMAZING!!! https://google.com"

print(preprocess_text(text))


# test.py
from predict import predict_sentiment

print(predict_sentiment("This movie was absolutely fantastic, I loved it!"))
print(predict_sentiment("Terrible film, complete waste of time."))
