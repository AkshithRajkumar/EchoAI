import azure.cognitiveservices.speech as speechsdk
import os
import logging
from config import SPEECH_KEY, SPEECH_REGION

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
        
        # Create speech synthesizer and generate speech
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        ssml = generate_ssml(text, sentiment)

        # Save the response
        result = synthesizer.speak_ssml_async(ssml).get()

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
        return "en-US-AmandaMultilingualNeural"  
    elif sentiment == "negative":
        return "en-US-RyanMultilingualNeural"  
    else:
        return "en-US-EmmaMultilingualNeural"  

def generate_ssml(text, sentiment):
    """Generate SSML with emotion for Azure Speech Service."""
    
    if sentiment == "positive":
        emotion = "affectionate"
        ssml = f"""
        <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='http://www.w3.org/2001/mstts' xml:lang='en-US'>
            <voice name='{select_voice(sentiment)}'>
                <prosody rate="+8.00%">
                    <mstts:express-as style='{emotion}' styledegree="1.8">
                        {text}
                    </mstts:express-as>
                </prosody>    
            </voice>
        </speak>
        """
        return ssml

    elif sentiment == "negative":
        emotion = "empathetic"
        ssml = f"""
        <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='http://www.w3.org/2001/mstts' xml:lang='en-US'>
            <voice name='{select_voice(sentiment)}'>
                <mstts:express-as role="OlderAdultMale" style='{emotion}' styledegree="1.8">
                    {text}
                </mstts:express-as>
            </voice>
        </speak>
        """
        return ssml

    else:
        emotion = "gentle"
        ssml = f"""
        <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='http://www.w3.org/2001/mstts' xml:lang='en-US'>
            <voice name='{select_voice(sentiment)}'>
                <prosody rate="+10.00%">
                    <mstts:express-as style='{emotion}' styledegree="1.8">
                        {text}
                    </mstts:express-as>
                </prosody>
            </voice>
        </speak>
        """
        return ssml
    
