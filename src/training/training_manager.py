"""
Training manager for Dinesh Assistant.
Coordinates knowledge base and response pattern integration.
"""

from typing import Dict, List, Union

from .conversation_patterns import ConversationEnhancer
from .knowledge_base import Domain, KnowledgeBase, KnowledgeItem
from .response_patterns import ResponsePatternLibrary, ResponseType, TrainingConfig
from .openai_knowledge_base import OPENAI_KNOWLEDGE_BASE


class TrainingManager:
    """Manages the training and response generation for the assistant."""

    def __init__(self, config: TrainingConfig):
        self.config = config
        self.knowledge_base = KnowledgeBase()
        self.pattern_library = ResponsePatternLibrary()
        self.conversation_enhancer = ConversationEnhancer()
        self._integrate_openai_knowledge()

    def _integrate_openai_knowledge(self) -> None:
        """Integrate OpenAI-enhanced knowledge base."""
        print("Integrating OpenAI knowledge...")
        for domain, items in OPENAI_KNOWLEDGE_BASE.items():
            for item in items:
                self.knowledge_base.add_knowledge_item(
                    KnowledgeItem(
                        topic=item["topic"],
                        description=item["description"],
                        domain=domain,
                        examples=item.get("examples", []),
                        related_topics=[],
                        common_issues=[],
                        solutions=[]
                    )
                )
        print("OpenAI knowledge integration complete")

    def process_query(self, query: str) -> Dict[str, Union[str, List[str]]]:
        """Process a user query and generate appropriate response."""
        print(f"\nProcessing query: {query}")  # Debug log

        # First check for exact query matches
        query_lower = query.lower().strip()

        # Python feature patterns
        python_patterns = {
            "python features": {
                "response": self._get_python_features_response(),
                "references": ["Python", "Programming", "Language Features"],
            },
            "tell me about python": {
                "response": self._get_python_features_response(),
                "references": ["Python", "Programming", "Language Features"],
            },
        }

        # Project feature patterns
        project_patterns = {
            "project features": {
                "response": self._get_project_features_response(),
                "references": ["Project", "Features", "Capabilities"],
            },
            "tell me about this project": {
                "response": self._get_project_features_response(),
                "references": ["Project", "Features", "Capabilities"],
            },
        }

        # Common virtual environment queries
        venv_patterns = [
            "virtual environment",
            "venv",
            "virtualenv",
            "python env",
            "create environment",
            "how to create virtual environment",
            "how do i create a virtual environment",
        ]

        # First check exact matches for Python/project features
        if query_lower in python_patterns:
            return python_patterns[query_lower]
        elif query_lower in project_patterns:
            return project_patterns[query_lower]
        # Then check virtual environment patterns
        elif any(query_lower == pattern for pattern in venv_patterns):
            print("[DEBUG] Found exact virtual environment query match")
            return {
                "response": (
                    "Here's how to create and use a Python virtual environment:\n\n"
                    "1. Create a new virtual environment:\n"
                    "```bash\n"
                    "python -m venv .venv\n"
                    "```\n\n"
                    "2. Activate the environment:\n"
                    "- On Unix/MacOS:\n"
                    "```bash\n"
                    "source .venv/bin/activate\n"
                    "```\n"
                    "- On Windows:\n"
                    "```bash\n"
                    ".venv\\Scripts\\activate\n"
                    "```\n\n"
                    "3. Install packages:\n"
                    "```bash\n"
                    "pip install -r requirements.txt\n"
                    "```\n\n"
                    "To deactivate when you're done:\n"
                    "```bash\n"
                    "deactivate\n"
                    "```"
                ),
                "references": [
                    "Python Virtual Environments",
                    "pip",
                    "package management",
                ],
                "related_topics": ["dependencies", "requirements.txt", "Python setup"],
            }

        # Skip training manager for help queries
        help_patterns = {
            "help",
            "how can you help",
            "what can you help with",
            "how can you help me",
            "tell me how you can help",
            "what can you do",
            "what do you do",
            "what can you do for me",
            "what assistance can you provide",
            "show me what you can do"
        }
        if any(pattern in query_lower for pattern in help_patterns):
            return {
                "response": (
                    "I'm your dedicated assistant for this project! Here's what I can do for you:\n\n"
                    "1. Smart Development Help �\n"
                    "   • Guide you through the codebase\n"
                    "   • Explain complex concepts clearly\n"
                    "   • Help fix errors and issues\n"
                    "   • Suggest best practices\n\n"
                    "2. Project Features 🎯\n"
                    "   • Smart response system\n"
                    "   • Context management\n"
                    "   • Pattern matching\n"
                    "   • API integration\n\n"
                    "3. Development Support 💻\n"
                    "   • FastAPI implementation\n"
                    "   • Testing strategies\n"
                    "   • Code organization\n"
                    "   • Problem-solving\n\n"
                    "Ask me specific questions like:\n"
                    '• "How is the project structured?"\n'
                    '• "What are the key features?"\n'
                    '• "Help me understand testing"\n'
                ),
                "references": ["Project Guide", "Documentation"],
                "related_topics": ["project", "features", "documentation"],
            }

        # For other queries, continue with regular knowledge base search
        relevant_items = self.knowledge_base.search_knowledge(query)
        print(f"Found {len(relevant_items)} relevant items")  # Debug log

        # Determine best response type
        response_type = self._determine_response_type(query, relevant_items)
        print(f"Selected response type: {response_type}")  # Debug log

        # Generate response
        response = self._generate_response(query, relevant_items, response_type)
        print(f"Generated initial response: {response[:100]}...")  # Debug log

        # If response is None, generate fallback
        if response is None or not response.strip():
            print("Initial response was empty, using fallback")  # Debug log
            response = self._generate_fallback_response(query)

        # Get references and related topics
        references = self._get_references(relevant_items)
        topics = self._get_related_topics(relevant_items)
        print(f"Found {len(topics)} related topics")  # Debug log

        # For non-help queries, enhance the response
        enhanced_response = response
        if not any(pattern in query_lower for pattern in help_patterns):
            enhanced_response = self.conversation_enhancer.enhance_response(
                response, query, topics[0] if topics else None
            )
            print(f"Enhanced response: {enhanced_response[:100]}...")  # Debug log

        return {
            "response": enhanced_response,
            "references": references,
            "related_topics": topics,
        }

    def _determine_response_type(
        self, query: str, items: List[KnowledgeItem]
    ) -> ResponseType:
        """Determine the most appropriate response type based on query and context."""
        query = query.lower()
        words = set(query.split())

        # Print the detected query type for debugging
        print(f"\nAnalyzing query type for: {query}")

        # Project feature query
        project_terms = {
            "feature",
            "project",
            "tell me about",
            "what can",
            "capability",
        }
        if any(term in query for term in project_terms):
            print("Detected: Project features query")
            return ResponseType.DIRECT

        # Python features query
        python_terms = {
            "python",
            "feature",
            "features",
            "what is",
            "tell me about python",
        }
        python_features = {
            "class",
            "function",
            "method",
            "decorator",
            "generator",
            "async",
            "context manager",
            "exception",
            "inheritance",
            "polymorphism",
        }
        if any(term in query for term in python_terms) or any(
            feature in query for feature in python_features
        ):
            print("Detected: Python features query")
            return ResponseType.DIRECT

        # First check for specific query types based on content and relevant items
        if items:
            if items[0].domain == Domain.GITHUB:
                print("Detected: GitHub query")
                return ResponseType.DIRECT
            elif items[0].topic == "Python Features":
                print("Detected: Python features query")
                return ResponseType.DIRECT

        # Check for troubleshooting queries
        troubleshoot_words = {
            "error",
            "issue",
            "problem",
            "fix",
            "help",
            "wrong",
            "not working",
            "failed",
        }
        if any(word in words or word in query for word in troubleshoot_words):
            print("Detected: Troubleshooting query")
            return ResponseType.TROUBLESHOOT

        # Check for how-to and creation requests
        howto_words = {
            "how",
            "create",
            "setup",
            "set up",
            "configure",
            "install",
            "make",
        }
        if any(word in query for word in howto_words):
            print("Detected: Tutorial/how-to query")
            return ResponseType.TUTORIAL

        # Check for example requests
        example_words = {"example", "sample", "show", "code", "demonstrate"}
        if any(word in words or word in query for word in example_words):
            print("Detected: Example query")
            return ResponseType.EXAMPLE

        print("Detected: Direct response query")
        return ResponseType.DIRECT

    def _generate_response(
        self, query: str, items: List[KnowledgeItem], response_type: ResponseType
    ) -> str:
        """Generate a response using knowledge items and response patterns."""
        if not items:
            return self._generate_fallback_response(query)

        # Get appropriate response pattern
        pattern = self.pattern_library.get_random_pattern(response_type)
        if not pattern:
            return self._generate_fallback_response(query)

        # Fill pattern with knowledge
        primary_item = items[0]  # Use most relevant item
        try:
            if response_type == ResponseType.EXAMPLE:
                return pattern.template.format(
                    topic=primary_item.topic,
                    language=self._determine_language(primary_item),
                    code=(
                        primary_item.examples[0]
                        if primary_item.examples
                        else "# No example available"
                    ),
                    explanation=primary_item.description,
                )

            elif response_type == ResponseType.TROUBLESHOOT:
                return pattern.template.format(
                    issue=query,
                    check=(
                        primary_item.common_issues[0]
                        if primary_item.common_issues
                        else "the documentation"
                    ),
                    solution=(
                        primary_item.solutions[0]
                        if primary_item.solutions
                        else "review the logs"
                    ),
                    alternative="contact support",
                    explanation=primary_item.description,
                )

            elif response_type == ResponseType.TUTORIAL:
                steps = (
                    primary_item.solutions[:3]
                    if primary_item.solutions
                    else ["Read documentation"]
                )
                while len(steps) < 3:
                    steps.append("Practice and experiment")

                return pattern.template.format(
                    topic=primary_item.topic,
                    step1=steps[0],
                    step2=steps[1],
                    step3=steps[2],
                    additional_info=primary_item.description,
                )

            else:  # DIRECT response
                return f"{primary_item.description}\n\nExample:\n{primary_item.examples[0] if primary_item.examples else 'No example available'}"

        except (KeyError, IndexError, ValueError) as e:
            print(f"Error generating response: {e}")  # For debugging
            return self._generate_fallback_response(query)

    def _generate_fallback_response(self, query: str) -> str:
        """Generate a fallback response when no knowledge items are found."""
        return (
            "I can help you better if you ask about:\n\n"
            "1. Project Features\n"
            "   • Architecture and design\n"
            "   • Implementation details\n"
            "   • Available functionality\n\n"
            "2. Development Tasks\n"
            "   • Code organization\n"
            "   • Testing strategies\n"
            "   • Best practices\n\n"
            "What specific aspect would you like to know about?"
        )

    def _determine_language(self, item: KnowledgeItem) -> str:
        """Determine the programming language for code examples."""
        if item.domain == Domain.PYTHON:
            return "python"
        elif item.domain == Domain.WEB:
            return "javascript"
        return "bash"  # Default for CLI examples

    def _get_python_features_response(self) -> str:
        """Get a comprehensive response about Python features."""
        return (
            "Python is a versatile programming language with many powerful features:\n\n"
            "1. Core Features\n"
            "   - Easy to read syntax and dynamic typing\n"
            "   - Rich built-in data structures (lists, dictionaries, sets)\n"
            "   - List/Dict comprehensions for concise data processing\n"
            "   - Iterators and generators for efficient memory use\n\n"
            "2. Object-Oriented Programming\n"
            "   - Classes and inheritance\n"
            "   - Encapsulation and polymorphism\n"
            "   - Properties and descriptors\n"
            "   - Method overriding and super()\n\n"
            "3. Advanced Features\n"
            "   - Decorators for function/class modification\n"
            "   - Context managers (with statement)\n"
            "   - Async/await for asynchronous code\n"
            "   - Type hints for better code clarity\n\n"
            "4. Error Handling\n"
            "   - Try/except for exception handling\n"
            "   - Custom exception classes\n"
            "   - Finally blocks for cleanup\n\n"
            "Would you like to learn more about any specific feature?"
        )

    def _get_project_features_response(self) -> str:
        """Get information about the project's features."""
        return (
            "This project is a smart chatbot assistant with the following features:\n\n"
            "1. Natural Language Processing\n"
            "   - Understanding user queries\n"
            "   - Context-aware responses\n"
            "   - Multiple domain support\n\n"
            "2. Knowledge Domains\n"
            "   - Python development and features\n"
            "   - GitHub and version control\n"
            "   - Web development and APIs\n"
            "   - CI/CD and deployment\n\n"
            "3. Core Features\n"
            "   - Virtual environment management\n"
            "   - Package dependency handling\n"
            "   - Project configuration\n"
            "   - Testing framework\n\n"
            "4. Web Interface\n"
            "   - FastAPI backend\n"
            "   - Interactive chat UI\n"
            "   - Real-time responses\n\n"
            "Would you like to know more about any specific feature?"
        )

    def _get_references(self, items: List[KnowledgeItem]) -> List[str]:
        """Get relevant reference topics from knowledge items."""
        references = []
        for item in items:
            references.extend(item.related_topics)
        return list(set(references))  # Remove duplicates

    def _get_related_topics(self, items: List[KnowledgeItem]) -> List[str]:
        """Get related topics from knowledge items."""
        topics = []
        for item in items:
            topics.append(item.topic)
        return list(set(topics))  # Remove duplicates

    def reset_conversation(self) -> None:
        """Reset the conversation context."""
        self.conversation_enhancer.reset_context()

    def get_farewell(self) -> str:
        """Get a contextual farewell message."""
        return self.conversation_enhancer.generate_farewell()
