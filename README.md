# EchoAI
 A project that recieves feedback, analyses the sentiment and responds back with speech using LLM.  

**Input:** User feedback  
**Processing:** Sentiment Analysis + AI Response Generation  
**Output:** Text & Speech Response (with emotion)  

# Feedback Analysis Web App

This project is a **Flask + Streamlit** web app that performs **sentiment analysis** using the **Azure Language Service API** and generates AI-based responses via the **OpenAI GPT API**. The response is also converted to speech using the **Azure Speech Service API**. 

**Technologies Used:** Flask, Streamlit, OpenAI API, Azure AI Services  
**Purpose:** Analyze sentiment from text input and generate appropriate spoken responses with emotion.

## Features 
-Analyze sentiment of text using Azure AI Language Service  
-Generate AI-based responses with OpenAI GPT  
-Convert text responses to speech using Azure AI Speech Service 
-Interactive Streamlit UI with a pie chart visualization  
-Play and download generated speech response directly in the app  

# Getting Started

Follow these steps to set up and run EchoAI:

**Installation Steps**

***Create a new Virtual Environment***

`conda create --name myenv python=3.9`

***Activate the virtual Enviornment***

`conda activate myenv`

***Clone the github repo***


```bash
git clone https://github.com/AkshithRajkumar/EchoAI.git
cd EchoAI
```

***Install Required Packages***

`pip install -r requirements.txt`

***Setup API Keys***

The project requires Azure AI Language & Speech services and an OpenAI API key.

Follow this [Azure Setup Guide](https://www.youtube.com/watch?v=anu8kPVt5PA) for setting up Azure services.

Create a `.env` file in the project root and add:

```
OPENAI_API_KEY= your-openai-api-key  
LANGUAGE_ENDPOINT=your-azure-text-analytics-endpoint  
LANGUAGE_KEY=your-azure-text-analytics-key  
SPEECH_KEY=your-azure-speech-key  
SPEECH_REGION=your-azure-region  
```

# Implementation

***Run the Flask backend***

`python app.py`

Expected Output:

* The Flask API starts running on http://127.0.0.1:5000/.   
* Ready to analyze sentiment & generate AI responses.  

***Run the Streamlit frontend***

`streamlit run app_frontend.py`

Expected Output:

* The Streamlit UI opens in your browser.  
* Users can enter feedback & receive AI-powered spoken responses.  

# Visuals

**First Look**

![Feedback Analysis UI - Streamlit](https://github.com/AkshithRajkumar/EchoAI/blob/main/screenshots/echoai_form1.jpeg)

**Submit Feedback**

![Sentiment Analysis](https://github.com/AkshithRajkumar/EchoAI/blob/main/screenshots/echoai_response.jpeg)

**Play response**

![Reponse Audio](https://github.com/AkshithRajkumar/EchoAI/blob/main/screenshots/echoai_response_audio.jpeg)





