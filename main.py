import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

LANGUAGE_ENDPOINT = os.getenv("LANGUAGE_ENDPOINT")
LANGUAGE_KEY = os.getenv("LANGUAGE_KEY")

# Initialize Azure Text Analytics Client
credential = AzureKeyCredential(LANGUAGE_KEY)
client = TextAnalyticsClient(endpoint=LANGUAGE_ENDPOINT, credential=credential)

# Directory containing text files
documents_folder = "documents"

def analyze_sentiment_for_file(file_name):
    """Analyzes sentiment for a given text file inside the 'documents' folder."""
    file_path = os.path.join(documents_folder, file_name)

    if not os.path.exists(file_path):
        print(f"Error: File '{file_name}' not found in '{documents_folder}'.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        document_text = f.read()

    # Perform sentiment analysis
    result = client.analyze_sentiment([document_text])[0]

    # Print the results
    print(f"File: {file_name}")
    print(f"Sentiment: {result.sentiment}")
    print(f"Confidence Scores: {result.confidence_scores}")
    print("-" * 50)

# Example Usage
document_name = "document_11.txt"  # Change this to test different files
analyze_sentiment_for_file(document_name)
