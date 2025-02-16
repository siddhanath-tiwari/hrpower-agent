# from transformers import pipeline

# # Load sentiment analysis model
# sentiment_pipeline = pipeline("sentiment-analysis")

# def analyze_sentiment(text):
#     result = sentiment_pipeline(text)
#     return result

# # Example usage
# feedback = "The candidate was very knowledgeable and had a positive attitude."
# sentiment = analyze_sentiment(feedback)
# print(sentiment)


from transformers import pipeline

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return {"label": result[0]['label'], "score": result[0]['score']}

# Example usage
feedback = "The candidate was very knowledgeable and had a positive attitude."
sentiment = analyze_sentiment(feedback)
print(sentiment)
