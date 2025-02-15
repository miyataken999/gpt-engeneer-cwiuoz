#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --host 0.0.0.0 --port 8000
