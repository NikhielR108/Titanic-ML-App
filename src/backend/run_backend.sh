#!/bin/bash

# this script starts the backend

echo " Starting backend"
echo "--------------------"

uvicorn api:app --reload 

