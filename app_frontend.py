import streamlit as st
import requests
import plotly.graph_objects as go

FLASK_URL = "http://localhost:5000/analyze_sentiment" 
AUDIO_URL = "http://localhost:5000/get_audio" 

# Streamlit UI
st.title("Feedback Analysis Tool")
user_input = st.text_area("Enter feedback:", "")

# Button Customizations
st.markdown("""
    <style>
        .stButton > button {
            background-color: #28a745 !important;  /* Green background */
            color: white !important;               /* White text */
            border: none !important;
        }   
        .stButton > button:hover {
            background-color: #218838 !important;  /* Darker green on hover */
            color: white !important;
        }
        .stButton > button:focus {
            background-color: #228B22 !important;  /* Keep darker green when focused */
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)


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

                if sentiment and confidence_scores:
                    # Store response in session_state
                    st.session_state.sentiment = sentiment
                    st.session_state.confidence_scores = confidence_scores
                    st.session_state.ai_response = ai_response
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

# Display results
if 'sentiment' in st.session_state:
    st.markdown(f"## **Sentiment:** {st.session_state.sentiment.capitalize()}")

    labels = ['Positive', 'Neutral', 'Negative']
    sizes = [st.session_state.confidence_scores['positive'], st.session_state.confidence_scores['neutral'], st.session_state.confidence_scores['negative']]
    colors = ['#66b3ff','#99ff99','#ff6666']
    
     # Interactive Pie Chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=0.3, marker=dict(colors=colors), textinfo='percent+label', pull=[0.1, 0, 0])])
    fig.update_layout(title="Sentiment Distribution",showlegend=True)
    st.plotly_chart(fig)
    
    st.markdown(f"### **Response:** {st.session_state.ai_response}")

# Audio button
if 'ai_response' in st.session_state:
    if st.button("Play Response"):
        audio_response = requests.get(AUDIO_URL)
        if audio_response.status_code == 200:
            st.audio(audio_response.content, format="audio/wav")
        else:
            st.write("Error fetching audio file.")