from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.exceptions import AzureError
import logging
from config import LANGUAGE_ENDPOINT, LANGUAGE_KEY

# Initialize Azure Sentiment Analysis client
if LANGUAGE_ENDPOINT and LANGUAGE_KEY:
    credential = AzureKeyCredential(LANGUAGE_KEY)
    client = TextAnalyticsClient(endpoint=LANGUAGE_ENDPOINT, credential=credential)
else:
    client = None

def analyze_sentiment(feedback):
    """Analyze sentiment of a given feedback text using Azure."""
    if not client:
        return {"error": "Azure Text Analytics client is not initialized."}

    try:
        result = client.analyze_sentiment([feedback])[0]
        sentiment = result.sentiment
        confidence_scores = {
            "positive": result.confidence_scores.positive,
            "neutral": result.confidence_scores.neutral,
            "negative": result.confidence_scores.negative
        }
        return {"sentiment": sentiment, "confidence_scores": confidence_scores}

    except AzureError as e:
        logging.error(f"Azure API error: {str(e)}")
        return {"error": f"Azure API error: {str(e)}"}
