"""Enhanced domain handling for better response management."""

from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple
from .domains import Domain


@dataclass
class DomainInfo:
    """Information about a specific domain."""
    domain: Domain
    keywords: Set[str]
    context_words: Set[str]
    priority: int
    description: str


@dataclass
class DomainResponse:
    """Structured response for a domain."""
    text: str
    references: List[str]
    followup_questions: List[str]
    code_examples: Optional[List[str]] = None


class DomainHandler:
    """Handler for domain-specific responses and interactions."""

    def __init__(self):
        """Initialize domain handler with predefined domain information."""
        self.domain_info: Dict[Domain, DomainInfo] = {
            Domain.PYTHON: DomainInfo(
                domain=Domain.PYTHON,
                keywords={"python", "pip", "pytest", "async", "type hints"},
                context_words={"code", "programming", "development", "script"},
                priority=1,
                description="Python development and best practices"
            ),
            Domain.MCP: DomainInfo(
                domain=Domain.MCP,
                keywords={"mcp", "model context protocol", "context management"},
                context_words={"server", "protocol", "integration"},
                priority=1,
                description="MCP server capabilities and integration"
            ),
            Domain.PROJECT: DomainInfo(
                domain=Domain.PROJECT,
                keywords={"help", "about", "how", "what"},
                context_words={"explain", "tell", "show", "describe"},
                priority=0,
                description="General project information"
            ),
            # Add other domains as needed
        }

    def detect_domains(self, query: str) -> List[Tuple[Domain, float]]:
        """
        Detect relevant domains for a query with confidence scores.
        
        Args:
            query: User's input query
            
        Returns:
            List of (domain, confidence) tuples, sorted by confidence
        """
        query_words = set(query.lower().split())
        scores: List[Tuple[Domain, float]] = []
        
        for domain, info in self.domain_info.items():
            score = 0.0
            
            # Check direct keyword matches (high weight)
            keyword_matches = len(query_words.intersection(info.keywords))
            score += keyword_matches * 2.0
            
            # Check context word matches (lower weight)
            context_matches = len(query_words.intersection(info.context_words))
            score += context_matches * 0.5
            
            # Add priority bonus
            score += info.priority * 0.25
            
            if score > 0:
                scores.append((domain, score))
        
        return sorted(scores, key=lambda x: x[1], reverse=True)

    def get_domain_response(
        self, domain: Domain, context: Optional[str] = None
    ) -> DomainResponse:
        """
        Get a response for a specific domain.
        
        Args:
            domain: Domain enum value
            context: Optional context to customize response
            
        Returns:
            DomainResponse with text and metadata
        """
        if domain == Domain.PYTHON:
            return DomainResponse(
                text=(
                    "This project uses Python with modern best practices:\n\n"
                    "1. Language Features 🐍\n"
                    "   • Type hints for code safety\n"
                    "   • Async/await for performance\n"
                    "   • Modern Python 3.8+ features\n\n"
                    "2. Development Tools ⚙️\n"
                    "   • pytest for testing\n"
                    "   • mypy for type checking\n"
                    "   • black & isort for formatting\n\n"
                    "3. Project Structure 📁\n"
                    "   • Modular package organization\n"
                    "   • Clean code practices\n"
                    "   • Documentation standards\n\n"
                    "What specific Python feature would you like to explore?"
                ),
                references=[
                    "src/main.py",
                    "src/chatbot.py",
                    "src/training/"
                ],
                followup_questions=[
                    "How do you use type hints?",
                    "Can you show me async examples?",
                    "How is testing implemented?"
                ],
                code_examples=[
                    "# Type hints example\ndef process_data(items: List[str]) -> Dict[str, int]:\n    return {item: len(item) for item in items}",
                    "# Async example\nasync def fetch_data(url: str) -> str:\n    async with aiohttp.ClientSession() as session:\n        async with session.get(url) as response:\n            return await response.text()"
                ]
            )
        elif domain == Domain.MCP:
            return DomainResponse(
                text=(
                    "The MCP (Model Context Protocol) server in this project:\n\n"
                    "1. Key Features 🎯\n"
                    "   • Context-aware response handling\n"
                    "   • Efficient state management\n"
                    "   • Domain-specific integrations\n\n"
                    "2. Implementation ⚙️\n"
                    "   • FastAPI-based architecture\n"
                    "   • Async request processing\n"
                    "   • Structured response format\n\n"
                    "3. Capabilities 💡\n"
                    "   • Multi-domain knowledge\n"
                    "   • Enhanced context tracking\n"
                    "   • Natural language processing\n\n"
                    "What aspect of MCP would you like to learn more about?"
                ),
                references=[
                    "src/chatbot.py",
                    "src/training/llm_knowledge_base.py",
                    "docs/HYBRID_ARCHITECTURE.md"
                ],
                followup_questions=[
                    "How does context tracking work?",
                    "Can you explain the response format?",
                    "How is state managed?"
                ]
            )
        else:
            return DomainResponse(
                text=(
                    "I can help you with:\n\n"
                    "1. Project Features 🚀\n"
                    "   • Python development\n"
                    "   • MCP server integration\n"
                    "   • Project architecture\n\n"
                    "2. Development Support ⚙️\n"
                    "   • Code examples\n"
                    "   • Best practices\n"
                    "   • Troubleshooting\n\n"
                    "What would you like to explore?"
                ),
                references=["README.md", "docs/"],
                followup_questions=[
                    "Tell me about Python features",
                    "How does MCP work?",
                    "Show me the project structure"
                ]
            )

    def get_combined_response(
        self, domains: List[Tuple[Domain, float]]
    ) -> DomainResponse:
        """
        Generate a combined response for multiple relevant domains.
        
        Args:
            domains: List of (domain, confidence) tuples
            
        Returns:
            DomainResponse combining information from all relevant domains
        """
        if not domains:
            return self.get_domain_response(Domain.PROJECT)
            
        if len(domains) == 1:
            return self.get_domain_response(domains[0][0])
            
        # For multiple domains, combine responses intelligently
        main_responses = []
        all_references = []
        all_followups = []
        
        for domain, confidence in domains[:2]:  # Take top 2 domains
            response = self.get_domain_response(domain)
            main_responses.append(response.text.split("\n\n", 1)[1])  # Skip intro
            all_references.extend(response.references)
            all_followups.extend(response.followup_questions[:2])
                
        combined_text = (
            "Let me explain how these aspects work together:\n\n"
            f"{main_responses[0]}\n\n"
            "This integrates with:\n\n"
            f"{main_responses[1]}\n\n"
            "Would you like to explore any specific aspect in more detail?"
        )
        
        return DomainResponse(
            text=combined_text,
            references=list(set(all_references)),
            followup_questions=all_followups,
            code_examples=[]
        )