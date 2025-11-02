"""
Training manager for Dinesh Assistant.
Coordinates knowledge base and response pattern integration.
"""

from typing import Dict, List, Optional, Union

from .knowledge_base import Domain, KnowledgeBase, KnowledgeItem
from .response_patterns import (
    ResponsePattern,
    ResponsePatternLibrary,
    ResponseType,
    TrainingConfig,
)


class TrainingManager:
    """Manages the training and response generation for the assistant."""

    def __init__(self, config: TrainingConfig):
        self.config = config
        self.knowledge_base = KnowledgeBase()
        self.pattern_library = ResponsePatternLibrary()

    def process_query(self, query: str) -> Dict[str, Union[str, List[str]]]:
        """Process a user query and generate appropriate response."""
        # Search knowledge base
        relevant_items = self.knowledge_base.search_knowledge(query)

        # Determine best response type
        response_type = self._determine_response_type(query, relevant_items)

        # Generate response
        response = self._generate_response(query, relevant_items, response_type)

        return {
            "response": response,
            "references": self._get_references(relevant_items),
            "related_topics": self._get_related_topics(relevant_items),
        }

    def _determine_response_type(
        self, query: str, items: List[KnowledgeItem]
    ) -> ResponseType:
        """Determine the most appropriate response type based on query and context."""
        query = query.lower()

        # Check for troubleshooting queries
        if any(word in query for word in ["error", "issue", "problem", "fix", "help"]):
            return ResponseType.TROUBLESHOOT

        # Check for example requests
        if any(word in query for word in ["example", "sample", "show", "code"]):
            return ResponseType.EXAMPLE

        # Check for tutorial requests
        if any(word in query for word in ["how", "learn", "teach", "explain", "guide"]):
            return ResponseType.TUTORIAL

        # Default to direct response
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

        if response_type == ResponseType.EXAMPLE:
            return pattern.template.format(
                topic=primary_item.topic,
                language=self._determine_language(primary_item),
                code=primary_item.examples[0]
                if primary_item.examples
                else "# No example available",
                explanation=primary_item.description,
            )

        elif response_type == ResponseType.TROUBLESHOOT:
            return pattern.template.format(
                issue=query,
                check=primary_item.common_issues[0]
                if primary_item.common_issues
                else "the documentation",
                solution=primary_item.solutions[0]
                if primary_item.solutions
                else "review the logs",
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

    def _generate_fallback_response(self, query: str) -> str:
        """Generate a fallback response when no knowledge items are found."""
        return (
            f"I apologize, but I don't have specific information about '{query}'. "
            "However, I can help you with Python, GitHub, MCP Server, CI/CD, and web development topics. "
            "Could you please rephrase your question or specify which aspect you're interested in?"
        )

    def _determine_language(self, item: KnowledgeItem) -> str:
        """Determine the programming language for code examples."""
        if item.domain == Domain.PYTHON:
            return "python"
        elif item.domain == Domain.WEB:
            return "javascript"
        return "bash"  # Default for CLI examples

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
