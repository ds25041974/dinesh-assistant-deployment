# Deployment Guide for Dinesh Assistant

## Overview
This document explains how to deploy and run the Dinesh Assistant chatbot as a permanent service on macOS using LaunchAgent.

## Prerequisites
- Python 3.8 or higher
- macOS operating system
- Git (for version control)

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

### 4. LaunchAgent Configuration
The LaunchAgent is configured to run the chatbot as a permanent service. The configuration file is located at:
`~/Library/LaunchAgents/com.dinesh.assistant.plist`

Key configuration details:
- Service Name: com.dinesh.assistant
- Working Directory: /Users/dineshsrivastava/python-test/Github Projectr
- Python Path: .venv/bin/python
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
   - Check log files for errors
   - Ensure virtual environment is properly set up
   - Verify permissions on the project directory

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