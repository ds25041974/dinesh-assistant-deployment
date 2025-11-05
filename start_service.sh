#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Function to check if a process is running
check_process() {
    pgrep -f "$1" > /dev/null
    return $?
}

# Ensure we're in the correct directory
cd "$SCRIPT_DIR"

# Check if Python virtual environment exists, create if it doesn't
if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
else
    source .venv/bin/activate
fi

# Kill any existing instances
pkill -f "uvicorn" || true
pkill -f "monitor_service.py" || true

# Start the monitoring service
echo "Starting service monitor..."
nohup python3 monitor_service.py > monitor.log 2>&1 &

# Wait for the service to start
echo "Waiting for service to start..."
sleep 5

# Check if service is running
if check_process "uvicorn"; then
    echo "✅ Dinesh Assistant is running!"
    echo "Access the web interface at: http://localhost:8000"
else
    echo "❌ Failed to start service. Check monitor.log for details."
    exit 1
fi