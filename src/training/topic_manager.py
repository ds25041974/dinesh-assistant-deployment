"""Topic Manager for controlling chatbot responses."""

from dataclasses import dataclass
from typing import Dict, List, Optional, Set

from .domain_handler import DomainHandler, DomainResponse


@dataclass
class TopicResponse:
    """Response from a specific topic with metadata."""

    text: str
    confidence: float
    category: str
    references: List[str]
    followup_questions: Optional[List[str]] = None
    code_examples: Optional[List[str]] = None


class TopicManager:
    """Manages topic detection and responses to ensure focused, relevant answers."""

    def __init__(self):
        """Initialize topic manager with domain handler and core topics."""
        self.domain_handler = DomainHandler()
        self._initialize_topics()

    def _initialize_topics(self) -> None:
        """Initialize core topics and their patterns."""
        self.topics = {
            "general_help": {
                "patterns": {
                    "how can you help",
                    "what can you help with",
                    "how can you help me",
                    "what can you do",
                    "what do you do",
                    "what can you do for me",
                    "help me",
                    "help",
                    "assist",
                    "tell me what you can do",
                    "explain what you can do",
                    "what are your capabilities",
                    "what assistance can you provide",
                    "show me what you can do",
                    "what are your features",
                },
                "response": (
                    "Hi! Let me tell you exactly how I can help make your work easier and more efficient! 😊\n\n"
                    "1. I'm Your Personal Development Assistant 🤝\n"
                    "   • I'll answer all your questions instantly\n"
                    "   • Guide you through complex tasks step by step\n"
                    "   • Help you find and fix problems quickly\n"
                    "   • Explain things in a clear, friendly way\n\n"
                    "2. Here's How I Make Your Life Easier �\n"
                    "   • Save time: Get immediate answers instead of searching\n"
                    "   • Learn faster: Get clear explanations with examples\n"
                    "   • Work better: Follow best practices and avoid common mistakes\n"
                    "   • Solve problems: Get help when you're stuck\n\n"
                    "3. I Can Help You With 🎯\n"
                    "   • Understanding any part of the project\n"
                    "   • Writing and improving code\n"
                    "   • Fixing errors and debugging\n"
                    "   • Learning new concepts and techniques\n\n"
                    "4. Getting Started is Easy 🚀\n"
                    "   Just ask me things like:\n"
                    '   • "Can you explain how [something] works?"\n'
                    '   • "Help me fix this error: [error message]"\n'
                    '   • "How do I do [something]?"\n\n'
                    "What would you like help with? I'm here to assist you! 💡"
                )
            },
            "project_info": {
                "patterns": {
                    "tell me about this project",
                    "what is this project",
                    "project features",
                    "project capabilities",
                    "what does this project do",
                    "technical details",
                    "how does it work",
                    "technical about this project"
                },
                "response": (
                    "Let me tell you what this project can do for you! 🚀\n\n"
                    "1. Smart Chatbot Features\n"
                    "   • Natural conversation handling\n"
                    "   • Context-aware responses\n"
                    "   • Customizable response patterns\n"
                    "   • Easy integration with your apps\n\n"
                    "2. Modern Tech Stack Benefits\n"
                    "   • FastAPI for quick, reliable responses\n"
                    "   • Async support for better performance\n"
                    "   • Type safety to prevent errors\n"
                    "   • Easy to extend and customize\n\n"
                    "3. Development Tools\n"
                    "   • pytest for testing\n"
                    "   • GitHub Actions for CI/CD\n"
                    "   • OpenAPI/Swagger documentation\n\n"
                    "Which technical aspect would you like me to explain in detail?"
                ),
            },
            "python": {
                "patterns": {
                    "python",
                    "tell me about python",
                    "how does python",
                    "python features",
                    "python development"
                },
                "response": (
                    "This project uses Python with modern best practices:\n\n"
                    "1. Language Features\n"
                    "   • Type hints for code safety\n"
                    "   • Async/await for performance\n"
                    "   • Modern Python 3.8+ features\n\n"
                    "2. Development Tools\n"
                    "   • pytest for testing\n"
                    "   • mypy for type checking\n"
                    "   • black & isort for formatting\n\n"
                    "3. Project Structure\n"
                    "   • Modular package organization\n"
                    "   • Clean code practices\n"
                    "   • Documentation standards\n\n"
                    "What Python-related aspect interests you?"
                ),
            },
            "github": {
                "patterns": {
                    "github",
                    "tell me github",
                    "how does github",
                    "git features",
                    "version control"
                },
                "response": (
                    "This project uses GitHub for version control and collaboration:\n\n"
                    "1. Version Control\n"
                    "   • Git repository management\n"
                    "   • Branch protection rules\n"
                    "   • Code review workflows\n\n"
                    "2. CI/CD Pipeline\n"
                    "   • GitHub Actions automation\n"
                    "   • Automated testing\n"
                    "   • Code quality checks\n\n"
                    "3. Project Management\n"
                    "   • Issue tracking\n"
                    "   • Project boards\n"
                    "   • Release management\n\n"
                    "Which GitHub feature would you like to know more about?"
                ),
            },
            "cicd": {
                "patterns": {
                    "ci",
                    "cd",
                    "ci cd",
                    "ci/cd",
                    "continuous integration",
                    "continuous deployment",
                    "deployment pipeline",
                    "tell me about ci cd"
                },
                "response": (
                    "Our CI/CD pipeline ensures code quality and automated deployment:\n\n"
                    "1. Continuous Integration\n"
                    "   • Automated testing\n"
                    "   • Code quality checks\n"
                    "   • Type verification\n\n"
                    "2. Continuous Deployment\n"
                    "   • Automated builds\n"
                    "   • Staging deployments\n"
                    "   • Production releases\n\n"
                    "3. Quality Gates\n"
                    "   • Test coverage requirements\n"
                    "   • Code style enforcement\n"
                    "   • Security scanning\n\n"
                    "Would you like details about any specific CI/CD aspect?"
                ),
            }
        }

        # Initialize reference mappings
        self.references: Dict[str, List[str]] = {
            "general_help": ["docs/CHATBOT.md", "docs/HYBRID_ARCHITECTURE.md"],
            "project_info": ["docs/DEPLOYMENT.md", "README.md"],
            "python": ["src/main.py", "src/chatbot.py", "src/training/"],
            "github": [".github/", "README.md"],
            "cicd": ["docs/DEPLOYMENT.md", ".github/workflows/"]
        }

    def get_help_response(self) -> str:
        """Get a general help response about capabilities."""
        return (
            "Let me explain exactly how I can help you succeed with this project! 💡\n\n"
            "1. I'm Your Project Expert & Guide 🎯\n"
            "   • I know everything about this project's features and code\n"
            "   • I can help you understand any part you're interested in\n"
            "   • I'll guide you step-by-step through implementation\n"
            "   • I can show you the best practices specific to this project\n\n"
            "2. Real Benefits for You 💫\n"
            "   • Save time with instant, accurate answers\n"
            "   • Learn faster with clear explanations\n"
            "   • Avoid common mistakes with best practices\n"
            "   • Get unstuck quickly when you have problems\n\n"
            "3. Just Ask Me About 🎯\n"
            "   • How to implement any feature\n"
            "   • Understanding code or concepts\n"
            "   • Fixing errors or improving code\n"
            "   • Best practices and techniques\n\n"
            "What would you like help with? I'm here to assist you every step of the way! �"
        )

    def get_response(self, query: str) -> TopicResponse:
        """Get response for a query based on its topic and domains.

        Args:
            query: The user's input query

        Returns:
            TopicResponse: Response for the matched topic/domains, or a default response
        """
        query = query.lower().strip()

        # First, check for domain-specific matches
        domains = self.domain_handler.detect_domains(query)
        if domains:
            if len(domains) > 1:
                response = self.domain_handler.get_combined_response(domains)
            else:
                response = self.domain_handler.get_domain_response(domains[0][0])

            confidence = domains[0][1] if domains else 0.5
            return TopicResponse(
                text=response.text,
                confidence=confidence,
                category=domains[0][0].name.lower(),
                references=response.references,
                followup_questions=response.followup_questions,
                code_examples=response.code_examples
            )

        # If no domain matches, check traditional topics
        for topic, info in self.topics.items():
            if any(pattern in query for pattern in info["patterns"]):
                return TopicResponse(
                    text=info["response"],
                    confidence=1.0,
                    category=topic,
                    references=self.references.get(topic, []),
                )

        # No matches found, return general help message
        return TopicResponse(
            text=self.get_help_response(),
            confidence=0.5,
            category="general",
            references=["Project Guide"],
            followup_questions=[
                "Tell me about Python features",
                "How does MCP work?",
                "Show me the project structure"
            ]
        )
