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
                "virtual_environments": KnowledgeItem(
                    domain=Domain.PYTHON,
                    topic="Virtual Environments",
                    description="Isolated Python environments for project dependencies",
                    examples=[
                        "python -m venv .venv",
                        "source .venv/bin/activate",
                        "pip install -r requirements.txt",
                    ],
                    related_topics=["pip", "dependencies", "packages"],
                    common_issues=[
                        "Environment not activating",
                        "Package conflicts",
                        "Path issues",
                    ],
                    solutions=[
                        "Verify Python version",
                        "Check activation script",
                        "Rebuild environment",
                    ],
                ),
                "fastapi": KnowledgeItem(
                    domain=Domain.PYTHON,
                    topic="FastAPI Framework",
                    description="Modern web framework for building APIs with Python",
                    examples=[
                        "from fastapi import FastAPI\napp = FastAPI()",
                        "@app.get('/')\ndef root(): return {'message': 'Hello'}",
                    ],
                    related_topics=["web frameworks", "async", "APIs"],
                    common_issues=[
                        "CORS configuration",
                        "Dependency injection",
                        "Path operations",
                    ],
                    solutions=[
                        "Enable CORS middleware",
                        "Use Depends for DI",
                        "Check path parameters",
                    ],
                ),
            }
        )

    def _add_github_knowledge(self):
        """Add GitHub-specific knowledge."""
        self.knowledge[Domain.GITHUB].update(
            {
                "actions": KnowledgeItem(
                    domain=Domain.GITHUB,
                    topic="GitHub Actions",
                    description="Automated workflow system for CI/CD",
                    examples=[
                        "name: CI\non: [push]\njobs:\n  build:\n    runs-on: ubuntu-latest",
                        "steps:\n  - uses: actions/checkout@v2",
                    ],
                    related_topics=["workflows", "CI/CD", "automation"],
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
                )
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
        for domain in self.knowledge.values():
            for item in domain.values():
                if (
                    query in item.topic.lower()
                    or query in item.description.lower()
                    or any(query in example.lower() for example in item.examples)
                ):
                    results.append(item)
        return results
