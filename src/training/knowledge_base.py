"""
Knowledge Base for Dinesh Assistant.
Defines specialized domain knowledge and response patterns.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional


class Domain(Enum):
    PYTHON = "python"
    GITHUB = "github"
    MCP = "mcp"
    CICD = "cicd"
    WEB = "web"


@dataclass
class KnowledgeItem:
    """Represents a piece of knowledge with context and examples."""

    domain: Domain
    topic: str
    description: str
    examples: List[str]
    related_topics: List[str]
    common_issues: List[str]
    solutions: List[str]


class KnowledgeBase:
    """Manages domain-specific knowledge for the assistant."""

    def __init__(self):
        self.knowledge: Dict[Domain, Dict[str, KnowledgeItem]] = {
            domain: {} for domain in Domain
        }
        self._initialize_knowledge()

    def _initialize_knowledge(self):
        """Initialize the knowledge base with domain-specific information."""
        # Python Knowledge
        self._add_python_knowledge()
        # GitHub Knowledge
        self._add_github_knowledge()
        # MCP Server Knowledge
        self._add_mcp_knowledge()
        # CI/CD Knowledge
        self._add_cicd_knowledge()
        # Web Development Knowledge
        self._add_web_knowledge()

    def _add_python_knowledge(self):
        """Add Python-specific knowledge."""
        self.knowledge[Domain.PYTHON].update(
            {
                "project_setup": KnowledgeItem(
                    domain=Domain.PYTHON,
                    topic="Project Setup",
                    description="This project uses modern Python practices with a clean architecture and comprehensive testing.",
                    examples=[
                        "# Run the tests\npytest tests/",
                        "# Format code\nblack . && isort .",
                        "# Start the chatbot\npython -m src.main",
                    ],
                    related_topics=[
                        "testing",
                        "code quality",
                        "project structure",
                        "development workflow"
                    ],
                    common_issues=[
                        "Understanding project structure",
                        "Running test suite",
                        "Code formatting",
                        "Getting started"
                    ],
                    solutions=[
                        "Review project documentation",
                        "Follow test guidelines",
                        "Use provided tools",
                        "Check example code"
                    ],
                ),
                "fastapi": KnowledgeItem(
                    domain=Domain.PYTHON,
                    topic="FastAPI Web Framework",
                    description="FastAPI is a modern, fast web framework for building APIs with Python 3.6+ based on standard Python type hints. It's designed to be easy to use, fast to code, and ready for production.",
                    examples=[
                        "# Basic FastAPI application\nfrom fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\ndef root():\n    return {'message': 'Hello World'}",
                        "# Path parameters\n@app.get('/items/{item_id}')\ndef read_item(item_id: int):\n    return {'item_id': item_id}",
                        "# Query parameters\n@app.get('/search/')\ndef search(q: str, skip: int = 0, limit: int = 10):\n    return {'q': q, 'skip': skip, 'limit': limit}",
                    ],
                    related_topics=[
                        "web development",
                        "API design",
                        "async programming",
                        "Pydantic",
                        "OpenAPI/Swagger",
                    ],
                    common_issues=[
                        "CORS configuration problems",
                        "Dependency injection confusion",
                        "Path operation ordering",
                        "Type hint errors",
                    ],
                    solutions=[
                        "Add CORSMiddleware for cross-origin requests",
                        "Use Depends for clean dependency injection",
                        "Order path operations from most specific to least",
                        "Ensure Python type hints are correct",
                    ],
                ),
                "testing": KnowledgeItem(
                    domain=Domain.PYTHON,
                    topic="Python Testing",
                    description="Python testing frameworks and best practices for writing unit tests, integration tests, and ensuring code quality through comprehensive test coverage.",
                    examples=[
                        "# Basic pytest test\ndef test_function():\n    assert add(2, 3) == 5",
                        "# Fixture example\n@pytest.fixture\ndef test_data():\n    return {'key': 'value'}",
                        "# Parametrized test\n@pytest.mark.parametrize('input,expected', [(1,2), (2,4)])\ndef test_double(input, expected):\n    assert double(input) == expected",
                    ],
                    related_topics=[
                        "pytest",
                        "unittest",
                        "test coverage",
                        "mocking",
                        "fixtures",
                    ],
                    common_issues=[
                        "Tests not discovering all files",
                        "Fixture scope problems",
                        "Mock side effects",
                        "Coverage reporting issues",
                    ],
                    solutions=[
                        "Check pytest.ini configuration",
                        "Adjust fixture scopes appropriately",
                        "Use proper mock return values",
                        "Configure coverage settings correctly",
                    ],
                ),
            }
        )

    def _add_github_knowledge(self):
        """Add GitHub-specific knowledge."""
        self.knowledge[Domain.GITHUB].update(
            {
                "overview": KnowledgeItem(
                    domain=Domain.GITHUB,
                    topic="GitHub Platform",
                    description=(
                        "GitHub is a web-based platform for version control and collaboration using Git. "
                        "It provides hosting for software development, enables team collaboration, "
                        "and offers tools for code review, project management, and automation."
                    ),
                    examples=[
                        "git clone https://github.com/username/repository.git",
                        "git push origin main",
                    ],
                    related_topics=[
                        "version control",
                        "Git",
                        "repositories",
                        "collaboration",
                    ],
                    common_issues=[
                        "Authentication issues",
                        "Repository access",
                        "Merge conflicts",
                    ],
                    solutions=[
                        "Set up SSH keys",
                        "Check repository permissions",
                        "Follow Git best practices",
                    ],
                ),
                "actions": KnowledgeItem(
                    domain=Domain.GITHUB,
                    topic="GitHub Actions",
                    description=(
                        "GitHub Actions is an automation platform that enables you to create custom "
                        "software development workflows directly in your GitHub repository. "
                        "It's commonly used for CI/CD, testing, and deployment."
                    ),
                    examples=[
                        "name: CI\non: [push]\njobs:\n  build:\n    runs-on: ubuntu-latest",
                        "steps:\n  - uses: actions/checkout@v2",
                    ],
                    related_topics=[
                        "workflows",
                        "CI/CD",
                        "automation",
                        "DevOps",
                    ],
                    common_issues=[
                        "Workflow not triggering",
                        "Action permissions",
                        "Secrets management",
                    ],
                    solutions=[
                        "Check trigger events",
                        "Verify permissions",
                        "Set repository secrets",
                    ],
                ),
                "repositories": KnowledgeItem(
                    domain=Domain.GITHUB,
                    topic="GitHub Repositories",
                    description=(
                        "Repositories are the fundamental unit of GitHub, containing all of your project's files "
                        "and revision history. They can be public or private, and include features like "
                        "issue tracking, pull requests, and project management tools."
                    ),
                    examples=[
                        "git init\ngit remote add origin https://github.com/username/repo.git",
                        "git push -u origin main",
                    ],
                    related_topics=[
                        "Git",
                        "version control",
                        "branches",
                        "collaboration",
                    ],
                    common_issues=[
                        "Repository initialization",
                        "Remote configuration",
                        "Branch management",
                    ],
                    solutions=[
                        "Follow repository setup guide",
                        "Configure Git properly",
                        "Use branch protection rules",
                    ],
                ),
            }
        )

    def _add_mcp_knowledge(self):
        """Add MCP Server-specific knowledge."""
        self.knowledge[Domain.MCP].update(
            {
                "integration": KnowledgeItem(
                    domain=Domain.MCP,
                    topic="MCP Integration",
                    description="Model Context Protocol server integration",
                    examples=[
                        "from mcp_client import MCPClient",
                        "client = MCPClient(endpoint='localhost:50051')",
                    ],
                    related_topics=["context management", "API", "protocols"],
                    common_issues=[
                        "Connection failures",
                        "Context synchronization",
                        "Protocol version mismatches",
                    ],
                    solutions=[
                        "Check server status",
                        "Update client version",
                        "Verify endpoints",
                    ],
                )
            }
        )

    def _add_cicd_knowledge(self):
        """Add CI/CD-specific knowledge."""
        self.knowledge[Domain.CICD].update(
            {
                "pipelines": KnowledgeItem(
                    domain=Domain.CICD,
                    topic="CI/CD Pipelines",
                    description="Continuous Integration and Deployment workflows",
                    examples=[
                        "pytest && black . && isort .",
                        "docker build -t myapp .",
                    ],
                    related_topics=["testing", "deployment", "automation"],
                    common_issues=["Failed tests", "Build errors", "Deployment issues"],
                    solutions=[
                        "Check test coverage",
                        "Validate dependencies",
                        "Review logs",
                    ],
                )
            }
        )

    def _add_web_knowledge(self):
        """Add Web Development-specific knowledge."""
        self.knowledge[Domain.WEB].update(
            {
                "api_design": KnowledgeItem(
                    domain=Domain.WEB,
                    topic="API Design",
                    description="RESTful API design principles and practices",
                    examples=["GET /api/v1/users", "POST /api/v1/users/{id}/update"],
                    related_topics=["REST", "endpoints", "HTTP methods"],
                    common_issues=[
                        "Endpoint naming",
                        "Status codes",
                        "Response format",
                    ],
                    solutions=[
                        "Follow REST conventions",
                        "Use proper status codes",
                        "Document API specs",
                    ],
                )
            }
        )

    def get_knowledge(self, domain: Domain, topic: str) -> Optional[KnowledgeItem]:
        """Retrieve specific knowledge item."""
        return self.knowledge[domain].get(topic)

    def search_knowledge(self, query: str) -> List[KnowledgeItem]:
        """Search knowledge base for relevant items."""
        results = []
        query = query.lower()
        query_words = set(query.split())

        print(f"\nProcessing query: {query}")
        print(f"Query words: {query_words}")

        # Common words to ignore
        stop_words = {
            "a",
            "an",
            "the",
            "in",
            "on",
            "at",
            "to",
            "for",
            "of",
            "with",
            "by",
            "do",
            "does",
            "how",
            "what",
            "where",
            "when",
            "why",
            "which",
            "i",
        }
        query_words = {word for word in query_words if word not in stop_words}

        # Add common action variations and expand query words
        action_variations = {
            "create": ["create", "make", "setup", "set up", "build", "start", "new"],
            "use": ["use", "work with", "utilize", "run"],
            "install": ["install", "download", "get"],
        }
        expanded_query_words = set(query_words)

        # Expand query words with variations
        for word in query_words:
            for action, variations in action_variations.items():
                if word in variations:
                    expanded_query_words.add(action)
                    expanded_query_words.update(variations)

        query_words = expanded_query_words

        # Project-specific terms
        project_terms = {
            "project",
            "chatbot",
            "assistant",
            "feature",
            "dinesh",
            "capabilities",
            "this project",
            "bot",
            "system",
            "functionality",
        }

        # Word pairs for better context
        word_list = query.split()
        word_pairs = [
            f"{word_list[i]} {word_list[i + 1]}" for i in range(len(word_list) - 1)
        ]

        print(f"Word pairs: {word_pairs}")

        # Convert query to lowercase for matching
        query_lower = query.lower()

        # First check if it's a project-specific query
        if any(term in query_lower for term in project_terms):
            return [
                KnowledgeItem(
                    domain=Domain.PYTHON,
                    topic="Project Features",
                    description=(
                        "This project is a smart chatbot assistant with the following features:\n\n"
                        "1. Natural Language Processing\n"
                        "   - Understands user queries\n"
                        "   - Provides context-aware responses\n"
                        "   - Handles multiple topics\n\n"
                        "2. Knowledge Domains\n"
                        "   - Python development\n"
                        "   - GitHub and version control\n"
                        "   - Web development\n"
                        "   - CI/CD and deployment\n\n"
                        "3. Core Features\n"
                        "   • Smart Response Generation\n"
                        "   • Topic-Based Processing\n"
                        "   • Context Management\n"
                        "   • Pattern Recognition"
                        "4. Web Interface\n"
                        "   - FastAPI backend\n"
                        "   - Interactive chat UI\n"
                        "   - Real-time responses"
                    ),
                    examples=[],
                    related_topics=["chatbot", "python", "web development", "testing"],
                    common_issues=["Response accuracy", "Query understanding"],
                    solutions=["Provide specific questions", "Use clear keywords"],
                )
            ]

        # First, determine which domain the query is most likely about
        domain_scores = {domain: 0 for domain in Domain}
        query_lower = query.lower()

        # Score each domain based on keyword presence
        domain_keywords = {
            Domain.GITHUB: set(["github", "git", "repo", "pull request", "issue"]),
            Domain.PYTHON: set(
                [
                    "python",
                    "pip",
                    "package",
                    "library",
                    "module",
                    "feature",
                    "class",
                    "function",
                    "method",
                    "decorator",
                    "async",
                    "generator",
                    "list",
                    "dict",
                    "tuple",
                    "set",
                    "iterator",
                    "comprehension",
                    "exception",
                    "error handling",
                    "context manager",
                    "with",
                    "import",
                    "inheritance",
                    "polymorphism",
                    "encapsulation",
                    "object oriented",
                    "oop",
                ]
            ),
            Domain.WEB: set(["api", "endpoint", "http", "rest", "request"]),
            Domain.CICD: set(["pipeline", "deploy", "build", "test", "continuous"]),
            Domain.MCP: set(["mcp", "protocol", "server", "context"]),
        }

        # Initialize Python features knowledge if not exists
        if "python_features" not in self.knowledge[Domain.PYTHON]:
            self.knowledge[Domain.PYTHON]["python_features"] = KnowledgeItem(
                domain=Domain.PYTHON,
                topic="Python Features",
                description=(
                    "Python is a versatile language with many powerful features:\n\n"
                    "1. Core Features\n"
                    "   - Easy to read, dynamic typing\n"
                    "   - Built-in data structures (lists, dictionaries, sets)\n"
                    "   - List/Dict comprehensions\n"
                    "   - Iterator and generator support\n\n"
                    "2. Object-Oriented Features\n"
                    "   - Classes and inheritance\n"
                    "   - Encapsulation and polymorphism\n"
                    "   - Method overriding\n"
                    "   - Properties and descriptors\n\n"
                    "3. Advanced Features\n"
                    "   - Decorators for function/class modification\n"
                    "   - Context managers (with statement)\n"
                    "   - Async/await for asynchronous programming\n"
                    "   - Type hints and annotations\n\n"
                    "4. Error Handling\n"
                    "   - Try/except blocks\n"
                    "   - Custom exceptions\n"
                    "   - Context managers for cleanup"
                ),
                examples=[
                    "# List comprehension\nnumbers = [x * 2 for x in range(5)]\n\n"
                    "# Generator function\ndef gen():\n    yield 1\n    yield 2\n\n"
                    "# Class with properties\nclass Person:\n    def __init__(self, name):\n"
                    "        self._name = name\n    @property\n    def name(self):\n"
                    "        return self._name"
                ],
                related_topics=[
                    "object oriented programming",
                    "functional programming",
                    "error handling",
                    "async programming",
                ],
                common_issues=[
                    "Understanding decorators",
                    "Managing imports",
                    "Proper error handling",
                ],
                solutions=[
                    "Read official Python documentation",
                    "Practice with examples",
                    "Use type hints for clarity",
                ],
            )

        for domain, keywords in domain_keywords.items():
            if any(keyword in query_lower for keyword in keywords):
                domain_scores[domain] = 2  # High priority for domain-specific queries

        # Search through items with domain awareness
        for domain, items in self.knowledge.items():
            domain_multiplier = domain_scores[domain] or 1.0
            for item in items.values():
                score = 0
                topic_lower = item.topic.lower()
                desc_lower = item.description.lower()

                # Direct matches in topic or description with domain awareness
                if query in topic_lower:
                    score += 10 * domain_multiplier
                if query in desc_lower:
                    score += 8 * domain_multiplier

                # Word matching with emphasis on action words and topics
                for word in query_words:
                    # Topic matches with higher weight for the actual query words
                    if word in topic_lower:
                        score += 5  # Base score for any topic match
                        if word in query_words:
                            score += (
                                3  # Additional score if it matches the actual query
                            )
                    # Description matches with higher score for query-specific terms
                    if word in desc_lower:
                        if word in action_variations:
                            score += 3  # Score for action words
                        elif word in query_words:
                            score += 2  # Score for query-specific terms
                        else:
                            score += 1
                    # Example matches
                    if any(word in ex.lower() for ex in item.examples):
                        score += 1
                    # Related topic matches
                    if any(word in topic.lower() for topic in item.related_topics):
                        score += 2

                # Pair matching for better context
                for pair in word_pairs:
                    if pair in topic_lower:
                        score += 5
                    if pair in desc_lower:
                        score += 4

                if score > 0:
                    print(f"Match: {item.topic} (Score: {score})")
                    item_data = {
                        "item": item,
                        "score": score,
                        "domain_relevance": self._calculate_domain_relevance(
                            query, item.domain
                        ),
                    }
                    results.append(item_data)

        # Sort by score and domain relevance
        sorted_results = sorted(
            results, key=lambda x: (x["score"], x["domain_relevance"]), reverse=True
        )

        # Return just the items in sorted order
        return [item_data["item"] for item_data in sorted_results]

    def _calculate_domain_relevance(self, query: str, domain: Domain) -> float:
        """Calculate how relevant a domain is to the query."""
        domain_keywords = {
            Domain.PYTHON: {
                "python": 2.0,  # Higher weight for primary domain terms
                "chatbot": 2.0,
                "nlp": 1.5,
                "ai": 1.5,
                "assistant": 1.5,
                "conversation": 1.0,
                "response": 1.0,
                "context": 1.0,
                "patterns": 0.8,
                "features": 0.8,
                "learning": 0.8,
            },
            Domain.GITHUB: {
                "github": 2.0,  # Higher weight for primary domain terms
                "git": 1.5,
                "repository": 1.0,
                "commit": 1.0,
                "push": 0.8,
                "pull": 0.8,
            },
            Domain.MCP: {
                "mcp": 2.0,
                "protocol": 1.0,
                "server": 0.8,
                "client": 0.8,
                "context": 0.8,
            },
            Domain.CICD: {
                "ci": 2.0,
                "cd": 2.0,
                "pipeline": 1.0,
                "build": 0.8,
                "deploy": 1.0,
                "test": 0.5,
            },
            Domain.WEB: {
                "api": 1.5,
                "rest": 1.5,
                "endpoint": 1.0,
                "http": 1.0,
                "web": 1.5,
                "request": 0.8,
            },
        }

        query_words = set(query.lower().split())
        domain_dict = domain_keywords.get(domain, {})

        # Calculate weighted score for matching words
        score = sum(domain_dict.get(word, 0) for word in query_words)
        return score / max(len(query_words), 1)  # Normalize by query length

    def get_help_response(self) -> str:
        """Get a general help response about capabilities."""
        response = (
            "I'm your AI assistant for this project. I can help you with:\n\n"
            "1. Project Development\n"
            "   • Understanding the architecture\n"
            "   • Implementing features\n"
            "   • Testing and quality assurance\n\n"
            "2. Technical Guidance\n"
            "   • Best practices\n"
            "   • Code organization\n"
            "   • Project structure\n\n"
            "What would you like to know about?"
        )
        return response
