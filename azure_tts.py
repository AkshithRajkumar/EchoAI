import azure.cognitiveservices.speech as speechsdk
import os
import logging
from config import SPEECH_KEY, SPEECH_REGION

# Ensure API keys are set
if not SPEECH_KEY or not SPEECH_REGION:
    logging.error("Azure Speech API credentials are missing!")

# Function to generate and play speech with emotion
def text_to_speech(text, sentiment, filename = "response.wav"):
    """Convert text to speech with emotion using Azure Speech Service."""
    
    try:
        # Initialize speech config
        speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
        speech_config.speech_synthesis_voice_name = select_voice(sentiment)  # Select voice based on sentiment
        
        # Set output to a file instead of just playing it
        audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
        # Create speech synthesizer
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

        # Generate SSML (Speech Synthesis Markup Language) for emotional speech
        ssml = generate_ssml(text, sentiment)

        # Speak the response
        result = synthesizer.speak_ssml(ssml)

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"Speech synthesis completed successfully! Audio saved as {filename}")
            return filename
        
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
            return None        

    except Exception as e:
        logging.error(f"Azure TTS error: {str(e)}")
        return None

def select_voice(sentiment):
    """Select Azure Neural Voice with the appropriate emotional tone."""
    if sentiment == "positive":
        return "en-US-JennyNeural"  # Friendly, warm voice
    elif sentiment == "negative":
        return "en-US-GuyNeural"  # Calm, serious male voice
    else:
        return "en-US-AriaNeural"  # Neutral, balanced voice

def generate_ssml(text, sentiment):
    """Generate SSML with emotion for Azure Speech Service."""
    
    if sentiment == "positive":
        emotion = "cheerful"
    elif sentiment == "negative":
        emotion = "hopeful"
    else:
        emotion = "neutral"
    
    ssml = f"""
    <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='http://www.w3.org/2001/mstts' xml:lang='en-US'>
        <voice name='{select_voice(sentiment)}'>
            <mstts:express-as style='{emotion}'>
                {text}
            </mstts:express-as>
        </voice>
    </speak>
    """
    return ssml
