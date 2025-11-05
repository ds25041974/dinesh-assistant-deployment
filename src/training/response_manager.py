"""
Response Manager for handling different types of queries and generating focused responses.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class QueryResponse:
    """Structured response with context."""

    text: str
    category: str
    confidence: float
    references: List[str] = field(default_factory=list)
    follow_up_questions: List[str] = field(default_factory=list)


class ResponseManager:
    """Manages chat responses with focused, contextual answers."""

    def __init__(self):
        self._initialize_responses()

    def _initialize_responses(self):
        """Initialize core response templates."""
        self.help_response = {
            "text": (
                "I specialize in helping with the following project areas:\n\n"
                "1. Technical Documentation 📚\n"
                "   • Project architecture details\n"
                "   • Code organization guides\n"
                "   • Implementation patterns\n"
                "   • Best practices docs\n\n"
                "2. Development Support 💻\n"
                "   • FastAPI implementation\n"
                "   • Testing strategies\n"
                "   • Code quality tips\n"
                "   • Problem-solving help\n\n"
                "3. Project Features 🎯\n"
                "   • Smart response system\n"
                "   • Topic-based processing\n"
                "   • Context management\n"
                "   • Pattern recognition\n\n"
                "Ask me specific questions like:\n"
                '• "How is the project structured?"\n'
                '• "What are the key features?"\n'
                '• "Show me implementation examples"\n'
            ),
            "follow_ups": [
                "Would you like to know about specific features?",
                "Need help with implementation details?",
                "Want to understand the project structure?",
            ],
        }

        self.topic_responses = {
            "project": {
                "text": (
                    "This project is a modern chatbot with these features:\n\n"
                    "1. Smart Conversations\n"
                    "   • Natural language understanding\n"
                    "   • Context-aware responses\n"
                    "   • Focused problem solving\n\n"
                    "2. Technical Capabilities\n"
                    "   • Python-based backend\n"
                    "   • FastAPI web interface\n"
                    "   • Modular architecture\n\n"
                    "What specific aspect interests you?"
                ),
                "references": ["Project Overview", "Architecture Guide"],
            },
            "mcp": {
                "text": (
                    "The Model Context Protocol (MCP) provides:\n\n"
                    "1. Structured Communication\n"
                    "   • Standard API interface\n"
                    "   • Secure data exchange\n"
                    "   • Error handling\n\n"
                    "2. Integration Features\n"
                    "   • Easy client setup\n"
                    "   • Clear protocol spec\n"
                    "   • Built-in validation\n\n"
                    "What would you like to know about MCP?"
                ),
                "references": ["MCP Documentation", "Integration Guide"],
            },
        }

    def get_help_response(self) -> QueryResponse:
        """Get the main help response."""
        return QueryResponse(
            text=self.help_response["text"],
            category="help",
            confidence=1.0,
            references=["Project Guide", "Documentation"],
            follow_up_questions=self.help_response["follow_ups"],
        )

    def get_topic_response(self, topic: str) -> Optional[QueryResponse]:
        """Get response for a specific topic."""
        if topic not in self.topic_responses:
            return None

        info = self.topic_responses[topic]
        return QueryResponse(
            text=info["text"],
            category=topic,
            confidence=1.0,
            references=info.get("references", []),
            follow_up_questions=info.get("follow_ups", []),
        )

    def is_help_query(self, query: str) -> bool:
        """Check if the query is asking for help."""
        help_patterns = {
            "how can you help",
            "what can you help with",
            "how can you help me",
            "tell me how you can help",
            "what can you do",
            "please tell me in detail",
            "tell me in detail",
            "help me",
            "what do you do",
            "explain what you can do",
        }
        query = query.lower().strip()
        return any(pattern in query for pattern in help_patterns)

    def is_topic_query(self, query: str, topic: str) -> bool:
        """Check if the query is about a specific topic."""
        query = query.lower().strip()
        topic_patterns = {
            "project": [
                "project",
                "features",
                "capabilities",
                "what can",
                "tell me about",
                "explain",
            ],
            "mcp": [
                "mcp",
                "model context protocol",
                "protocol",
                "integration",
                "model context",
            ],
        }

        if topic not in topic_patterns:
            return False

        return any(pattern in query for pattern in topic_patterns[topic])

    def get_default_response(self) -> QueryResponse:
        """Get a default response asking for clarification."""
        return QueryResponse(
            text=(
                "I'd be happy to help! Could you please:\n\n"
                "1. Specify what you'd like to know about\n"
                "2. Ask about a specific feature or topic\n"
                "3. Tell me what you're trying to accomplish\n\n"
                "This helps me provide more relevant information."
            ),
            category="clarification",
            confidence=0.5,
            follow_up_questions=[
                "Would you like to know about project features?",
                "Need help with a specific task?",
                "Want to learn about certain functionality?",
            ],
        )
