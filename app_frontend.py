import streamlit as st
import requests

# Flask URL
FLASK_URL = "http://localhost:5000/analyze_sentiment" 
AUDIO_URL = "http://localhost:5000/get_audio" 

# Streamlit UI
st.title("Sentiment Analysis Tool")
user_input = st.text_area("Enter feedback:", "")

# Submit button
if st.button("Submit Feedback"):
    if user_input:
        try:
            # Send the user input to Flask via a POST request
            response = requests.post(FLASK_URL, json={"feedback": user_input})

            if response.status_code == 200:
                # Extract sentiment results from Flask response
                data = response.json()
                sentiment = data.get('sentiment')
                confidence_scores = data.get('confidence_scores')
                ai_response = data.get('ai_response')
                audio_url = data.get('audio_url')

                if sentiment and confidence_scores:
                    # Display results
                    st.write(f"Sentiment: {sentiment}")
                    st.write(f"Confidence Scores: {confidence_scores}")
                    st.write(f"Response: {ai_response}")
                    
                    # Play audio button
                    if st.button("Play Response"):
                        audio_response = requests.get(AUDIO_URL)
                        if audio_response.status_code == 200:
                            st.audio(audio_response.content, format="audio/wav")
                        else:
                            st.write("Error fetching audio file.")
    
                else:
                    st.write("Error: Invalid response from the server.")
            else:
                st.write(f"Error: {response.json().get('error', 'Unknown error occurred')}")
        except requests.exceptions.RequestException as e:
            st.write(f"Error: Unable to connect to the server. Please check if the Flask backend is running. Details: {e}")
        except ValueError as e:
            st.write(f"Error: Invalid JSON response from the server. Details: {e}")
    else:
        st.write("Please enter some feedback.")