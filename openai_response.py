import openai
import logging
from config import OPENAI_API_KEY

if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY
else:
    logging.error("OpenAI API Key is missing.")

def get_ai_response(sentiment, feedback):
    """Generate a response using OpenAI GPT model."""

    prompt = f"""
    The following is a customer feedback message along with its sentiment analysis result.
    - Sentiment: {sentiment}
    - Feedback: "{feedback}"

    You are an AI assistant that generates professional, empathetic, and concise responses to customer feedback.

    Instructions:
    1. Analyze the given feedback and its sentiment.
    - If the sentiment is positive, express gratitude and encourage further engagement.
    - If the sentiment is negative,  acknowledge the issue and offer assistance.
    - If the sentiment is neutral, acknowledge the feedback politely and maintain a balanced tone.

    2. Keep the response short (2-3 sentences).
    3. Maintain a warm, professional, and natural tone.
    """

    try:
        # Calling the API
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # We can use gpt-4 as well. Will cost more.
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100 
        )
        return response.choices[0].message.content

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return "An unexpected error occurred. Please check the logs for details."
