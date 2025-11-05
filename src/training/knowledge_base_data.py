"""Knowledge base data for Dinesh Assistant."""

from typing import Dict, List

from .domains import Domain

# Knowledge base structured by domain
KNOWLEDGE_BASE: Dict[Domain, List[Dict[str, str]]] = {
    Domain.ARCHITECTURE: [
        {
            "topic": "Hybrid Architecture",
            "description": (
                "Dinesh Assistant uses a hybrid architecture combining local processing with cloud-based intelligence:\n\n"
                "1. Local Service Layer:\n"
                "   • FastAPI web server\n"
                "   • Process management\n"
                "   • File system operations\n"
                "   • Cache management\n\n"
                "2. Cloud Integration Layer:\n"
                "   • GitHub services integration\n"
                "   • Azure OpenAI services\n"
                "   • MCP server connections\n"
                "   • Remote API management\n\n"
                "3. Intelligence Layer:\n"
                "   • Natural language processing\n"
                "   • Context management\n"
                "   • Pattern matching\n"
                "   • Response generation"
            ),
            "keywords": ["architecture", "structure", "design", "system", "hybrid"],
            "examples": [
                "User Request -> Local Service -> Cloud Services -> Response",
                "File Operation -> Local Processing -> Cache -> Response"
            ]
        }
    ],
    
    Domain.PYTHON: [
        {
            "topic": "Python Implementation",
            "description": (
                "The project uses Python 3.8+ with modern features and best practices:\n\n"
                "1. Key Python Features Used:\n"
                "   • Type hints for better code clarity\n"
                "   • Async/await for non-blocking operations\n"
                "   • Dataclasses for structured data\n"
                "   • Context managers for resource handling\n\n"
                "2. Project Structure:\n"
                "   • Modular package organization\n"
                "   • Clean separation of concerns\n"
                "   • Object-oriented design\n"
                "   • Comprehensive testing"
            ),
            "keywords": ["python", "implementation", "features", "code", "development"],
            "examples": [
                "from dataclasses import dataclass\n@dataclass\nclass Response:\n    text: str\n    confidence: float"
            ]
        }
    ],

    Domain.DEPLOYMENT: [
        {
            "topic": "Service Deployment",
            "description": (
                "The project uses LaunchAgent for permanent service deployment:\n\n"
                "1. Service Components:\n"
                "   • LaunchAgent configuration\n"
                "   • Startup script management\n"
                "   • Process monitoring\n"
                "   • Error recovery\n\n"
                "2. Key Features:\n"
                "   • Automatic startup\n"
                "   • Process persistence\n"
                "   • Error logging\n"
                "   • Health monitoring"
            ),
            "keywords": ["deployment", "service", "launchagent", "startup", "monitoring"],
            "examples": [
                "launchctl load -w ~/Library/LaunchAgents/com.dinesh.assistant.plist"
            ]
        }
    ],

    Domain.GITHUB: [
        {
            "topic": "GitHub Integration",
            "description": (
                "The project integrates with GitHub for version control and collaboration:\n\n"
                "1. GitHub Features:\n"
                "   • Repository management\n"
                "   • Code version control\n"
                "   • Issue tracking\n"
                "   • Pull request handling\n\n"
                "2. CI/CD Pipeline:\n"
                "   • Automated testing\n"
                "   • Code quality checks\n"
                "   • Documentation updates\n"
                "   • Deployment automation"
            ),
            "keywords": ["github", "version control", "git", "collaboration", "ci/cd"],
            "examples": [
                "git push origin main",
                "gh pr create --title 'Update feature'"
            ]
        }
    ],

    Domain.WEB: [
        {
            "topic": "Web Interface",
            "description": (
                "The project provides a web interface using FastAPI:\n\n"
                "1. Web Components:\n"
                "   • FastAPI backend\n"
                "   • HTML templates\n"
                "   • Static assets\n"
                "   • WebSocket support\n\n"
                "2. Features:\n"
                "   • Real-time chat\n"
                "   • Response formatting\n"
                "   • Error handling\n"
                "   • API documentation"
            ),
            "keywords": ["web", "interface", "fastapi", "api", "frontend"],
            "examples": [
                "from fastapi import FastAPI\napp = FastAPI()\n@app.get('/')\ndef root():\n    return {'status': 'ok'}"
            ]
        }
    ],

    Domain.MCP: [
        {
            "topic": "MCP Servers",
            "description": (
                "The project uses Model Context Protocol servers for integration:\n\n"
                "1. MCP Features:\n"
                "   • Standardized communication\n"
                "   • Request routing\n"
                "   • Response aggregation\n"
                "   • Error handling\n\n"
                "2. Integration Points:\n"
                "   • GitHub services\n"
                "   • Azure services\n"
                "   • Local processing\n"
                "   • API management"
            ),
            "keywords": ["mcp", "protocol", "server", "integration", "model"],
            "examples": [
                "mcp_client.send_request(endpoint='github', action='create_issue')"
            ]
        }
    ],

    Domain.OPERATION: [
        {
            "topic": "System Operation",
            "description": (
                "The project operates as a permanent system service:\n\n"
                "1. Operational Features:\n"
                "   • 24/7 availability\n"
                "   • Auto-restart capability\n"
                "   • Error recovery\n"
                "   • Resource management\n\n"
                "2. Monitoring:\n"
                "   • Health checks\n"
                "   • Error logging\n"
                "   • Performance tracking\n"
                "   • Resource usage"
            ),
            "keywords": ["operation", "monitoring", "service", "maintenance", "health"],
            "examples": [
                "curl http://localhost:8000/health",
                "tail -f ~/Library/Logs/dinesh-assistant.log"
            ]
        }
    ],

    Domain.TESTING: [
        {
            "topic": "Testing Framework",
            "description": (
                "The project uses comprehensive testing with pytest:\n\n"
                "1. Test Components:\n"
                "   • Unit tests\n"
                "   • Integration tests\n"
                "   • Coverage reporting\n"
                "   • CI/CD integration\n\n"
                "2. Testing Features:\n"
                "   • Automated testing\n"
                "   • Mock objects\n"
                "   • Fixtures\n"
                "   • Parameterization"
            ),
            "keywords": ["testing", "tests", "pytest", "coverage", "quality"],
            "examples": [
                "pytest tests/",
                "pytest --cov=src tests/"
            ]
        }
    ],

    Domain.PROJECT: [
        {
            "topic": "Project Overview",
            "description": (
                "Dinesh Assistant is an AI-powered development assistant:\n\n"
                "1. Key Features:\n"
                "   • Natural language interaction\n"
                "   • Project-specific knowledge\n"
                "   • Development assistance\n"
                "   • System automation\n\n"
                "2. Use Cases:\n"
                "   • Code help\n"
                "   • Documentation\n"
                "   • Project management\n"
                "   • System maintenance"
            ),
            "keywords": ["project", "overview", "features", "about", "introduction"],
            "examples": [
                "python -m src.main --help",
                "python -m src.main chat --web"
            ]
        }
    ],

    Domain.TRAINING: [
        {
            "topic": "Training System",
            "description": (
                "The project uses a sophisticated training system:\n\n"
                "1. Training Components:\n"
                "   • Knowledge base management\n"
                "   • Response patterns\n"
                "   • Context tracking\n"
                "   • Learning pipeline\n\n"
                "2. Features:\n"
                "   • Pattern matching\n"
                "   • Response generation\n"
                "   • Context awareness\n"
                "   • Continuous learning"
            ),
            "keywords": ["training", "learning", "knowledge", "patterns", "responses"],
            "examples": [
                "from training import TrainingManager\nmanager = TrainingManager(config)"
            ]
        }
    ]
}

# Common response patterns for different query types
RESPONSE_PATTERNS = {
    "greeting": [
        "Hi! 👋 I'm Dinesh Assistant. How can I help you today?",
        "Hello! I'm here to help with your development needs. What can I do for you?",
        "Greetings! I'm your AI assistant. What would you like to know about the project?"
    ],
    "project": [
        "Let me tell you about {topic}:\n\n{description}",
        "Here's what you need to know about {topic}:\n\n{description}",
        "I can help you understand {topic}:\n\n{description}"
    ],
    "code": [
        "Here's how to {action}:\n\n```{language}\n{code}\n```\n\n{explanation}",
        "You can {action} like this:\n\n```{language}\n{code}\n```\n\n{explanation}",
        "Here's a code example for {action}:\n\n```{language}\n{code}\n```\n\n{explanation}"
    ],
    "error": [
        "I see you're having an issue with {problem}. Let's fix that:\n\n{solution}",
        "To resolve the {problem}, try this:\n\n{solution}",
        "Here's how to fix the {problem}:\n\n{solution}"
    ],
    "help": [
        "I can help you with:\n\n{capabilities}\n\nWhat would you like to know more about?",
        "Here are my capabilities:\n\n{capabilities}\n\nHow can I assist you?",
        "I'm skilled in:\n\n{capabilities}\n\nWhat interests you?"
    ]
}

# Keywords for different types of queries
QUERY_KEYWORDS = {
    "project": ["what", "tell", "explain", "describe", "show"],
    "code": ["how", "example", "implement", "code", "function"],
    "error": ["error", "issue", "problem", "fix", "wrong"],
    "help": ["help", "assist", "guide", "support", "aid"]
}