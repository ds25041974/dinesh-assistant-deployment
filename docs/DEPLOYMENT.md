# Deployment Guide for Dinesh Assistant

## Overview
This document explains how to deploy and run the Dinesh Assistant chatbot as a permanent service on macOS using LaunchAgent with a robust startup script.

## Prerequisites
- Python 3.8 or higher
- macOS operating system
- Git (for version control)
- Bash shell

## System Architecture

```
┌─────────────────────────────────┐
│        LaunchAgent Service      │
│    (com.dinesh.assistant)      │
├─────────────────────────────────┤
│        start_server.sh          │
│   (Environment & Server Setup)   │
├─────────────────────────────────┤
│         Uvicorn Server          │
│    (FastAPI Web Application)    │
└─────────────────────────────────┘
```

## Installation Steps

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Github\ Projectr
```

### 2. Set Up Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
pip install -e .
```

### 4. Server Startup Script
Create the startup script `start_server.sh`:

```bash
#!/bin/bash

# Set the working directory
cd "/Users/dineshsrivastava/python-test/Github Projectr"

# Activate virtual environment
source .venv/bin/activate

# Set environment variables
export PYTHONPATH="/Users/dineshsrivastava/python-test/Github Projectr"

# Start the server with error logging
exec uvicorn src.web.app:app --host 127.0.0.1 --port 8000 --log-level info >> ~/Library/Logs/dinesh-assistant.log 2>> ~/Library/Logs/dinesh-assistant.error.log
```

Make the script executable:
```bash
chmod +x start_server.sh
```

### 5. LaunchAgent Configuration
The LaunchAgent is configured to run the startup script as a permanent service. The configuration file is located at:
`~/Library/LaunchAgents/com.dinesh.assistant.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.dinesh.assistant</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/Users/dineshsrivastava/python-test/Github Projectr/start_server.sh</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <dict>
        <key>SuccessfulExit</key>
        <false/>
    </dict>
    <key>StandardOutPath</key>
    <string>/Users/dineshsrivastava/Library/Logs/dinesh-assistant.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/dineshsrivastava/Library/Logs/dinesh-assistant.error.log</string>
    <key>WorkingDirectory</key>
    <string>/Users/dineshsrivastava/python-test/Github Projectr</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
        <key>PYTHONPATH</key>
        <string>/Users/dineshsrivastava/python-test/Github Projectr</string>
    </dict>
</dict>
</plist>
```

Key configuration details:
- Service Name: com.dinesh.assistant
- Startup Script: start_server.sh
- Working Directory: /Users/dineshsrivastava/python-test/Github Projectr
- Environment Variables: PATH and PYTHONPATH configured
- Auto-restart: Enabled through KeepAlive configuration
- Log Files:
  - Main Log: ~/Library/Logs/dinesh-assistant.log
  - Error Log: ~/Library/Logs/dinesh-assistant.error.log

### 5. Service Management

#### Start the Service
```bash
launchctl load -w ~/Library/LaunchAgents/com.dinesh.assistant.plist
```

#### Stop the Service
```bash
launchctl unload ~/Library/LaunchAgents/com.dinesh.assistant.plist
```

#### Restart the Service
```bash
launchctl unload ~/Library/LaunchAgents/com.dinesh.assistant.plist
launchctl load -w ~/Library/LaunchAgents/com.dinesh.assistant.plist
```

## Monitoring and Maintenance

### Log Files
- Main application logs: `~/Library/Logs/dinesh-assistant.log`
- Error logs: `~/Library/Logs/dinesh-assistant.error.log`

### Health Check
- Access http://localhost:8000/health to verify the service is running
- API Documentation: http://localhost:8000/docs

## Troubleshooting

### Common Issues and Solutions

1. **Service Won't Start**
   - Check log files for errors: `tail -f ~/Library/Logs/dinesh-assistant.error.log`
   - Ensure virtual environment is properly set up
   - Verify permissions: `ls -l start_server.sh`
   - Check if port 8000 is available: `lsof -i :8000`
   - Verify the service status: `launchctl list | grep com.dinesh.assistant`

2. **Web Interface Not Accessible**
   - Confirm the service is running: `launchctl list | grep com.dinesh.assistant`
   - Check if port 8000 is already in use: `lsof -i :8000`
   - Review error logs for connection issues

3. **Dependencies Issues**
   - Reactivate virtual environment: `source .venv/bin/activate`
   - Reinstall dependencies: `pip install -r requirements.txt`

## Security Considerations
- The service runs on localhost (127.0.0.1) for security
- Access is limited to the local machine
- Environment variables and sensitive data are managed through the LaunchAgent plist

## Updating the Service
1. Pull latest code changes
2. Update dependencies: `pip install -r requirements.txt`
3. Restart the service using the commands above

## Directory Structure
```
.
├── .venv/                  # Virtual environment
├── src/                    # Source code
│   ├── web/               # Web interface
│   │   ├── app.py         # FastAPI application
│   │   ├── static/        # Static files
│   │   └── templates/     # HTML templates
│   └── main.py            # Main entry point
├── docs/                  # Documentation
└── requirements.txt       # Project dependencies
```