#!/bin/bash


# activate virtual environment
source .venv/bin/activate



cd src/backend
bash ./run_backend.sh &
BACKEND_PID=$!


# start the frontend 

cd ../frontend
bash ./run_frontend.sh


# When frontend exits, kill backend automatically
kill $BACKEND_PID