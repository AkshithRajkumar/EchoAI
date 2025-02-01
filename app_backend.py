from flask import Flask, request, jsonify
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.exceptions import AzureError
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Azure Text Analytics credentials and client
LANGUAGE_ENDPOINT = os.getenv("LANGUAGE_ENDPOINT")
LANGUAGE_KEY = os.getenv("LANGUAGE_KEY")

if not LANGUAGE_ENDPOINT or not LANGUAGE_KEY:
    logging.error("Missing environment variables: LANGUAGE_ENDPOINT or LANGUAGE_KEY")
else:
    credential = AzureKeyCredential(LANGUAGE_KEY)
    client = TextAnalyticsClient(endpoint=LANGUAGE_ENDPOINT, credential=credential)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    """Handle sentiment analysis request."""
    try:
        # Get the feedback from the POST request
        feedback = request.json.get("feedback")

        if not feedback:
            return jsonify({"error": "No feedback provided"}), 400

        # Perform sentiment analysis
        result = client.analyze_sentiment([feedback])[0]
        sentiment = result.sentiment
        confidence_scores = {
            "positive": result.confidence_scores.positive,
            "neutral": result.confidence_scores.neutral,
            "negative": result.confidence_scores.negative
        }
        return jsonify({
            'sentiment': sentiment,
            'confidence_scores': confidence_scores
        })
    except AzureError as e:
        logging.error(f"Azure API error: {str(e)}")
        return jsonify({"error": f"Azure API error: {str(e)}"}), 500
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Run the Flask app