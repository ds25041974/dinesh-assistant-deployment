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
        """Get chatbot greeting."""
        return (
            f"Hello! I'm {self.name}, your personal assistant for the ConfigMaster "
            "project. I can help you with:\n"
            "1. Project features and capabilities\n"
            "2. Configuration management\n"
            "3. Internationalization (i18n)\n"
            "4. Template system\n"
            "5. Validation framework\n"
            "6. Testing and development\n"
            "\nHow can I assist you today?"
        )

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
        # Simple pattern matching for now
        for pattern, response in context.get("patterns", {}).items():
            if re.search(pattern, query, re.I):
                return Response(
                    text=response,
                    confidence=0.8,
                    context=context,
                    references=context.get("references", []),
                )

        # Fallback response
        return Response(
            text=self._get_fallback_response(),
            confidence=0.2,
            context=context,
            references=[],
        )

    def _update_context(self, query: str, response: Response) -> None:
        """Update conversation context."""
        self._context["last_query"] = query
        self._context["last_response"] = response

    def _get_fallback_response(self) -> str:
        """Get fallback response when uncertain."""
        return (
            "I'm not quite sure about that. Could you rephrase your question? "
            "You can ask me about project features, configuration, i18n, "
            "templates, validation, or testing."
        )

    def _init_knowledge(self) -> Dict[str, Any]:
        """Initialize knowledge base."""
        return {
            "config": {
                "patterns": {
                    r"how.*(configure|setup|set up)": (
                        "To configure the project:\n"
                        "1. Create a virtual environment\n"
                        '2. Install with: pip install -e ".[dev]"\n'
                        "3. Configure settings in config.json\n"
                        "4. Run validation with: python -m src.main config validate"
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
