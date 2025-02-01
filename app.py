from flask import Flask, request, jsonify
from azure_sentiment import analyze_sentiment
from openai_response import get_ai_response
import logging

# Initialize Flask app
app = Flask(__name__)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze():
    """Handle sentiment analysis request and generate AI response."""
    try:
        feedback = request.json.get("feedback")
        if not feedback:
            return jsonify({"error": "No feedback provided"}), 400

        # Perform sentiment analysis
        sentiment_data = analyze_sentiment(feedback)
        if "error" in sentiment_data:
            return jsonify(sentiment_data), 500

        sentiment = sentiment_data["sentiment"]
        confidence_scores = sentiment_data["confidence_scores"]

        # Get AI-generated response
        ai_response = get_ai_response(sentiment, feedback)

        return jsonify({
            "sentiment": sentiment,
            "confidence_scores": confidence_scores,
            "ai_response": ai_response
        })

    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
