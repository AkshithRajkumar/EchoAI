import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Azure API Credentials
LANGUAGE_ENDPOINT = os.getenv("LANGUAGE_ENDPOINT")
LANGUAGE_KEY = os.getenv("LANGUAGE_KEY")

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION")

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check for missing keys
if not LANGUAGE_ENDPOINT or not LANGUAGE_KEY:
    logging.error("Missing Azure API credentials: LANGUAGE_ENDPOINT or LANGUAGE_KEY")

if not SPEECH_KEY or not SPEECH_REGION:
    loggin.error("Missing Azure API credentials: SPEECH_KEY or SPEECH_REGION")

if not OPENAI_API_KEY:
    logging.error("Missing OpenAI API key: OPENAI_API_KEY")    