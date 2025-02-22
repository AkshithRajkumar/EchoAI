#!/bin/bash
# Start Flask backend
gunicorn -w 4 -b 0.0.0.0:5000 app:app &

# Start Streamlit frontend
streamlit run app_frontend.py --server.port 8501 --server.address 0.0.0.0
