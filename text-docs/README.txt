# Dinesh Assistant - Simple Guide

WHAT IS THIS?
-------------
Dinesh Assistant is your personal AI helper that stays running on your computer all the time. It helps you understand and work with your project code and documentation.

MAIN FEATURES
------------
1. Always Available
   - Works 24/7
   - Runs as a permanent service on your computer
   - Starts automatically when your computer starts

2. Easy to Use
   - Use through your web browser at http://localhost:8000
   - Type commands in your terminal
   - Gets automatic updates

3. Helpful Features
   - Answers questions about your project
   - Helps with coding problems
   - Keeps track of changes
   - Connects with GitHub
   - Handles errors automatically

HOW TO START
-----------
1. First Time Setup:
   - Open Terminal
   - Go to project folder
   - Run: source .venv/bin/activate
   - Run: pip install -e .

2. Using the Web Interface:
   - Open your web browser
   - Go to: http://localhost:8000
   - Start asking questions!

3. Using in Terminal:
   - Open Terminal
   - Run: python -m src.main chat

NEED HELP?
---------
- Check error logs: ~/Library/Logs/dinesh-assistant.error.log
- View regular logs: ~/Library/Logs/dinesh-assistant.log
- Visit: http://localhost:8000/docs for more help

Remember: The assistant is always running in the background, ready to help!