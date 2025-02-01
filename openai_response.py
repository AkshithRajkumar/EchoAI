import openai
import logging
from config import OPENAI_API_KEY

# Set OpenAI API key
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY
else:
    logging.error("OpenAI API Key is missing.")

def get_ai_response(sentiment, feedback):
    """Generate a response using OpenAI GPT model."""

    # Construct the prompt
    prompt = f"""
    The following is a customer feedback message along with its sentiment analysis result.
    - Sentiment: {sentiment}
    - Feedback: "{feedback}"

    Based on this, provide a professional, empathetic, and helpful response.
    If the sentiment is negative, acknowledge the issue and offer assistance.
    If the sentiment is positive, express gratitude and encourage further engagement.
    Keep the response concise and friendly.
    """

    try:
        # Make the API request
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100  # Limit the response length
        )
        # Extract and return the generated response
        return response.choices[0].message.content

    except Exception as e:
        # Handle other unexpected errors
        logging.error(f"Unexpected error: {str(e)}")
        return "An unexpected error occurred. Please check the logs for details."
