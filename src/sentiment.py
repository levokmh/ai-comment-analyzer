import streamlit as st
from transformers import pipeline


@st.cache_resource
def load_classifier():
    """
    Load and cache the sentiment analysis model.
    """
    return pipeline(
        "sentiment-analysis",
        model="nlptown/bert-base-multilingual-uncased-sentiment"
    )


classifier = load_classifier()


def analyze_sentiments(texts):
    """
    Analyze a list of comments and return sentiment labels.
    """

    results = classifier(texts)

    sentiments = []

    for result in results:
        label = result["label"]

        if "4" in label or "5" in label:
            sentiments.append("positive")

        elif "3" in label:
            sentiments.append("neutral")

        else:
            sentiments.append("negative")

    return sentiments