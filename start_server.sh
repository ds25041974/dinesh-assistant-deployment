#!/bin/bash

# Set the working directory
cd "/Users/dineshsrivastava/python-test/Github Projectr"

# Create log directory if it doesn't exist
mkdir -p ~/Library/Logs

# Cleanup function
cleanup() {
    echo "Stopping server..."
    pkill -f uvicorn
    exit 0
}

# Set up trap for cleanup
trap cleanup SIGINT SIGTERM

#!/bin/bash

# Set the working directory
cd "/Users/dineshsrivastava/python-test/Github Projectr"

# Create log directory if it doesn't exist
mkdir -p ~/Library/Logs

# Cleanup function
cleanup() {
    echo "$(date): Stopping server..." | tee -a ~/Library/Logs/python-chatbot.log
    pkill -f uvicorn
    exit 0
}

# Set up trap for cleanup
trap cleanup SIGINT SIGTERM

# Activate virtual environment
source .venv/bin/activate 2>/dev/null || {
    echo "$(date): Creating virtual environment..." | tee -a ~/Library/Logs/python-chatbot.log
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
}

# Set environment variables
export PYTHONPATH="/Users/dineshsrivastava/python-test/Github Projectr"

# Kill any existing uvicorn processes
pkill -f uvicorn || true
sleep 2

# Start the server with auto-restart and logging
while true; do
    echo "$(date): Starting chatbot server..." | tee -a ~/Library/Logs/python-chatbot.log
    python3 -m uvicorn src.web.app:app --host 127.0.0.1 --port 8080 --log-level info \
        >> ~/Library/Logs/python-chatbot.log 2>> ~/Library/Logs/python-chatbot.error.log || true
    
    echo "$(date): Server stopped. Restarting in 5 seconds..." | tee -a ~/Library/Logs/python-chatbot.log
    sleep 5
done

# Set environment variables
export PYTHONPATH="/Users/dineshsrivastava/python-test/Github Projectr"

# Kill any existing uvicorn processes
pkill -f uvicorn || true
sleep 2

# Start the server with auto-restart and logging
while true; do
    echo "$(date): Starting chatbot server..." | tee -a ~/Library/Logs/dinesh-assistant.log
    python3 -m uvicorn src.web.app:app --host 127.0.0.1 --port 8080 --log-level info \
        >> ~/Library/Logs/dinesh-assistant.log 2>> ~/Library/Logs/dinesh-assistant.error.log || true
    echo "$(date): Server stopped. Restarting in 5 seconds..." | tee -a ~/Library/Logs/dinesh-assistant.log
    sleep 5
done