#!/bin/bash


# activate virtual environment
source .venv/bin/activate

echo "Starting backend"
echo "-----------------"

cd src/backend
uvicorn api:app --reload &
sleep 3

echo "Starting frontend"
echo "-----------------"

cd ../frontend
streamlit run app.py
