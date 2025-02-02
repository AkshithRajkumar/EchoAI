# EchoAI
 A project that recieves feedback, analyses the sentiment and responds back with speech using LLM.

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

**Installation Steps**

**Create a new Virtual Environment**

`conda create --name myenv python=3.9`

**Activate the virtual Enviornment**

`conda activate myenv`

**Clone the github repo**

`git clone https://github.com/AkshithRajkumar/EchoAI.git`

**Install Required Packages**

`pip install -r requirements.txt`

**Setup API Keys**

The project requires setting up a Language service and a Speech service under the Azure AI services. Look at the following [link](https://www.youtube.com/watch?v=anu8kPVt5PA) for setup reference. 

Additionally, a OpenAI API key is required which can be generated as a project API key.

Create a `.env` file in the project root and add:

```
OPENAI_API_KEY= your-openai-api-key  
LANGUAGE_ENDPOINT=your-azure-text-analytics-endpoint  
LANGUAGE_KEY=your-azure-text-analytics-key  
SPEECH_KEY=your-azure-speech-key  
SPEECH_REGION=your-azure-region  
```

# Implementation

**Run the Flask backend**

`python app.py`

**Run the Streamlit frontend**

`streamlit run app_frontend.py`

# Visuals

**First Look**

![Feedback Analysis UI - Streamlit](screenshots\echoai_form.jpeg)

**Submit Feedback**

![Sentiment Analysis](screenshots\echoai_response.jpeg)

**Play response**

![Reponse Audio](screenshots\echoai_response_audio.jpeg)





