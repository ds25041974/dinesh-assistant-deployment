"""Dinesh Assistant - Personal Project Chatbot.

This module implements a chatbot assistant that can answer questions about
the ConfigMaster project, provide help with features, and assist with usage.
"""

import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Response:
    """Chatbot response with metadata."""

    text: str
    confidence: float
    context: Dict[str, Any]
    references: List[str]


class DineshAssistant:
    """Personal chatbot assistant for ConfigMaster project."""

    def __init__(self):
        """Initialize the chatbot with knowledge base."""
        self.name = "Dinesh Assistant"
        self._knowledge_base = self._init_knowledge()
        self._context: Dict[str, Any] = {}

    def greet(self) -> str:
        """Get a warm and friendly greeting."""
        import random

        greetings = [
            f"Hey there! 👋 I'm {self.name}, and I'm super excited to help you with the "
            "ConfigMaster project! Here's what I can assist you with:\n\n"
            "🚀 Project features and capabilities\n"
            "⚙️ Configuration management\n"
            "🌍 Internationalization (i18n)\n"
            "📝 Template system\n"
            "✅ Validation framework\n"
            "🧪 Testing and development\n\n"
            "What would you like to explore today? I'm all ears! 😊",
            f"Hi! I'm {self.name}, your friendly guide to all things ConfigMaster! 🤗\n\n"
            "I love helping with:\n"
            "💫 Project features and cool capabilities\n"
            "🔧 Configuration setup and management\n"
            "🗣️ Internationalization (i18n)\n"
            "🎨 Template system\n"
            "🎯 Validation framework\n"
            "🔬 Testing and development\n\n"
            "What can I help you discover today?",
            f"Welcome! 🌟 {self.name} here, ready to make your ConfigMaster journey awesome!\n\n"
            "I'm your go-to expert for:\n"
            "✨ Project features and capabilities\n"
            "🛠️ Configuration management\n"
            "🌐 Internationalization (i18n)\n"
            "📋 Template system\n"
            "✅ Validation framework\n"
            "🧪 Testing and development\n\n"
            "Got questions? I've got answers! Let's make something amazing together! 💪",
        ]

        return random.choice(greetings)

    async def respond(self, query: str) -> Response:
        """Generate response for user query."""
        # Clean and normalize query
        query = self._normalize_query(query)

        # Find most relevant knowledge
        topic = self._identify_topic(query)
        context = self._get_context(topic)

        # Generate response
        response = self._generate_response(query, context)

        # Update conversation context
        self._update_context(query, response)

        return response

    def _normalize_query(self, query: str) -> str:
        """Clean and normalize user query."""
        return query.lower().strip()

    def _identify_topic(self, query: str) -> str:
        """Identify main topic of the query."""
        topics = {
            "config": r"config|setting|property",
            "i18n": r"i18n|language|translation|international",
            "template": r"template|pattern|format",
            "validation": r"valid|check|verify|rule",
            "test": r"test|assert|coverage|quality",
            "general": r"project|overview|feature|help",
        }

        for topic, pattern in topics.items():
            if re.search(pattern, query, re.I):
                return topic
        return "general"

    def _get_context(self, topic: str) -> Dict[str, Any]:
        """Get relevant context for topic."""
        return self._knowledge_base.get(topic, {})

    def _generate_response(self, query: str, context: Dict[str, Any]) -> Response:
        """Generate response based on query and context."""
        # Check for personality-based responses first
        personality_response = self._get_personality_response(query)
        if personality_response:
            return personality_response

        # Handle technical queries with context
        for pattern, response in context.get("patterns", {}).items():
            if re.search(pattern, query, re.I):
                # Add some personality to technical responses
                response = self._add_personality_to_response(response)
                return Response(
                    text=response,
                    confidence=0.8,
                    context=context,
                    references=context.get("references", []),
                )

        # Friendly fallback response
        return Response(
            text=self._get_fallback_response(),
            confidence=0.2,
            context=context,
            references=[],
        )

    def _add_personality_to_response(self, response: str) -> str:
        """Add personality markers to technical responses."""
        import random

        # Random friendly intros
        intros = [
            "Great question! ",
            "I'd be happy to help with that! ",
            "Ah, let me explain! ",
            "I love questions like this! ",
            "Let me break this down for you! ",
        ]

        # Random encouraging closures
        closures = [
            "\n\nHope this helps! Let me know if you need any clarification! 😊",
            "\n\nFeel free to ask if anything isn't clear! 👍",
            "\n\nDoes this answer your question? I'm here if you need more details!",
            "\n\nLet me know if you'd like to explore this topic further! 🚀",
        ]

        return f"{random.choice(intros)}{response}{random.choice(closures)}"

    def _update_context(self, query: str, response: Response) -> None:
        """Update conversation context."""
        self._context["last_query"] = query
        self._context["last_response"] = response

    def _get_fallback_response(self) -> str:
        """Get friendly fallback response when uncertain."""
        import random

        responses = [
            "Hmm, I'm not entirely sure I caught that right. 🤔 Mind rephrasing? "
            "I'd love to help - you can ask me about project features, configuration, "
            "i18n, templates, validation, or testing!",
            "I want to make sure I give you the best answer, but I'm a bit unsure about "
            "that one. 😅 Could you try asking in a different way? I'm great with topics "
            "like project features, configuration, i18n, templates, and more!",
            "Oops! I'm drawing a blank on that one! 🎯 Let's try a different approach - "
            "I'm really good at helping with project features, configuration, i18n, "
            "templates, validation, and testing. What would you like to know?",
            "I feel like we're almost there, but I want to understand your question better! "
            "💭 Can you rephrase that? I'm here to help with all sorts of things like "
            "project features, configuration, and more!",
        ]

        return random.choice(responses)

    def _get_personality_response(self, query: str) -> Optional[Response]:
        """Generate personality-based responses for casual conversation."""
        personality_patterns = {
            r"(hi|hello|hey).*": [
                "Hey there! 👋 Always great to chat with you!",
                "Hi! Hope you're having a fantastic day!",
                "Hello! I'm all ears - what's on your mind?",
            ],
            r"how are you.*": [
                "I'm doing great, thanks for asking! Ready to help you out!",
                "I'm feeling energized and ready to tackle any questions you have!",
                "Pretty good! Even AI assistants have their good days 😊",
            ],
            r"thank.*": [
                "You're welcome! Always happy to help! 😊",
                "Anytime! That's what I'm here for!",
                "No problem at all! Let me know if you need anything else!",
            ],
            r"bye|goodbye": [
                "Take care! Come back anytime!",
                "Bye for now! Looking forward to our next chat!",
                "See you later! Don't be a stranger! 👋",
            ],
            r"(who|what).*you": [
                "I'm Dinesh Assistant, your friendly AI companion! I specialize in helping with the ConfigMaster project, but I also enjoy casual chats!",
                "Think of me as your tech-savvy friend who's always excited to help with ConfigMaster and chat about anything!",
                "I'm an AI assistant with a passion for helping people and a knack for ConfigMaster details!",
            ],
        }

        for pattern, responses in personality_patterns.items():
            if re.search(pattern, query, re.I):
                import random

                return Response(
                    text=random.choice(responses),
                    confidence=0.9,
                    context={"type": "personality"},
                    references=[],
                )
        return None

    def _init_knowledge(self) -> Dict[str, Any]:
        """Initialize knowledge base."""
        return {
            "config": {
                "patterns": {
                    r"how.*(configure|setup|set up)": (
                        "Let me help you get started with the configuration! 😊\n\n"
                        "Here's what you need to do:\n"
                        "1. First, create a virtual environment (keeping things clean!)\n"
                        '2. Run: pip install -e ".[dev]" (this gets all the good stuff)\n'
                        "3. Set up your config.json (I can help with this!)\n"
                        "4. Validate everything with: python -m src.main config validate"
                    ),
                    r"what.*(settings|config|properties)": (
                        "ConfigMaster supports:\n"
                        "- Debug mode\n"
                        "- Language settings\n"
                        "- Template styles\n"
                        "- Custom messages\n"
                        "- Async mode\n"
                        "See src/config/settings.py for details."
                    ),
                },
                "references": ["src/config/settings.py", "README.md#configuration"],
            },
            "i18n": {
                "patterns": {
                    r"language.*support": (
                        "ConfigMaster supports these languages:\n"
                        "- English (en)\n"
                        "- Spanish (es)\n"
                        "- French (fr)\n"
                        "- Japanese (ja)\n"
                        "New languages can be added via translation bundles."
                    ),
                    r"how.*translate": (
                        "To add translations:\n"
                        "1. Create a translation bundle\n"
                        "2. Register with I18nManager\n"
                        "3. Use get_translation() to fetch strings\n"
                        "See src/config/i18n.py for examples."
                    ),
                },
                "references": ["src/config/i18n.py", "README.md#internationalization"],
            },
            "template": {
                "patterns": {
                    r"template.*(type|kind)": (
                        "Available template categories:\n"
                        "- Formal\n"
                        "- Casual\n"
                        "- Business\n"
                        "- Custom\n"
                        "Each supports variable interpolation and inheritance."
                    ),
                    r"how.*template": (
                        "To use templates:\n"
                        "1. Choose a template category\n"
                        "2. Create a TemplateContext\n"
                        "3. Call render() with variables\n"
                        "See src/config/templates.py for examples."
                    ),
                },
                "references": ["src/config/templates.py", "README.md#template-system"],
            },
            "validation": {
                "patterns": {
                    r"validate|validation": (
                        "Validation features:\n"
                        "- Type checking\n"
                        "- Range validation\n"
                        "- Pattern matching\n"
                        "- Custom rules\n"
                        "See src/config/validation.py for details."
                    ),
                    r"how.*valid": (
                        "To validate configurations:\n"
                        "1. Create validators (type, range, etc.)\n"
                        "2. Combine with CompositeValidator\n"
                        "3. Call validate() on config\n"
                        "Check README for complete examples."
                    ),
                },
                "references": [
                    "src/config/validation.py",
                    "README.md#validation-framework",
                ],
            },
            "test": {
                "patterns": {
                    r"run.*test": (
                        "To run tests:\n"
                        "1. pytest tests/ (all tests)\n"
                        "2. pytest tests/ --cov=src (with coverage)\n"
                        '3. pytest tests/test_main.py -k "pattern" (specific tests)'
                    ),
                    r"test.*coverage": (
                        "Test coverage features:\n"
                        "- Unit tests with pytest\n"
                        "- Property-based testing\n"
                        "- Integration tests\n"
                        "- Performance benchmarks\n"
                        "Current goal: 95% coverage"
                    ),
                },
                "references": ["tests/", "README.md#testing-framework"],
            },
            "general": {
                "patterns": {
                    r"what.*project": (
                        "ConfigMaster is an enterprise-grade configuration "
                        "management system with:\n"
                        "- Strong type validation\n"
                        "- Multi-language support\n"
                        "- Template system\n"
                        "- Async operations\n"
                        "- Comprehensive testing"
                    ),
                    r"help|feature": self.greet(),
                },
                "references": ["README.md", "src/main.py"],
            },
        }
