#!/bin/bash

# Set the working directory
cd "/Users/dineshsrivastava/python-test/Github Projectr"

# Activate virtual environment
source .venv/bin/activate

# Set environment variables
export PYTHONPATH="/Users/dineshsrivastava/python-test/Github Projectr"

# Start the server with error logging
exec uvicorn src.web.app:app --host 127.0.0.1 --port 8000 --log-level info >> ~/Library/Logs/dinesh-assistant.log 2>> ~/Library/Logs/dinesh-assistant.error.log