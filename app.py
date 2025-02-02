from flask import Flask, request, jsonify, send_file
from azure_sentiment import analyze_sentiment
from openai_response import get_ai_response
from azure_tts import text_to_speech
import logging

# Initialize Flask app
app = Flask(__name__)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze():
    """Handle sentiment analysis request, generate AI response, and speak it."""
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

        # Convert response to speech with emotion
        audio_file =  text_to_speech(ai_response, sentiment)

        if not audio_file:
            return jsonify({
                "sentiment": sentiment,
                "confidence_scores": confidence_scores,
                "ai_response": ai_response,
                "tts": "Speech synthesis failed."
            }), 500

        return jsonify({
            "sentiment": sentiment,
            "confidence_scores": confidence_scores,
            "ai_response": ai_response,
            "audio_url": f"http://localhost:5000/get_audio"
        })

    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/get_audio', methods=['GET'])
def get_audio():
    """Send the generated speech audio file to the frontend."""
    audio_path = "response.wav"  # Ensure this matches the filename in `text_to_speech()`
    if os.path.exists(audio_path):
        return send_file(audio_path, mimetype="audio/wav")
    else:
        return jsonify({"error": "Audio file not found."}), 404      

if __name__ == '__main__':
    app.run(debug=True, port=5000)
