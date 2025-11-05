"""
Training configuration and response patterns for Dinesh Assistant.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List


class ResponseType(Enum):
    DIRECT = "direct"
    EXAMPLE = "example"
    TUTORIAL = "tutorial"
    TROUBLESHOOT = "troubleshoot"


@dataclass
class TrainingConfig:
    """Configuration for assistant training."""

    # Response generation settings
    max_context_length: int = 2048
    temperature: float = 0.7
    top_p: float = 0.9
    response_types: List[ResponseType] = None

    # Domain weights for response relevance
    domain_weights: Dict[str, float] = None

    def __post_init__(self):
        if self.response_types is None:
            self.response_types = list(ResponseType)
        if self.domain_weights is None:
            self.domain_weights = {
                "python": 1.0,
                "github": 1.0,
                "mcp": 1.0,
                "cicd": 1.0,
                "web": 1.0,
            }


@dataclass
class ResponsePattern:
    """Template for generating structured responses."""

    type: ResponseType
    template: str
    variables: List[str]
    examples: List[Dict[str, str]]


class ResponsePatternLibrary:
    """Collection of response patterns for different scenarios."""

    def __init__(self):
        self.patterns: Dict[ResponseType, List[ResponsePattern]] = {
            response_type: [] for response_type in ResponseType
        }
        self._initialize_patterns()

    def _initialize_patterns(self):
        """Initialize response patterns for different types."""
        # Direct response patterns
        self.patterns[ResponseType.DIRECT].extend(
            [
                ResponsePattern(
                    type=ResponseType.DIRECT,
                    template="Here's how to {action}: {explanation}",
                    variables=["action", "explanation"],
                    examples=[
                        {
                            "action": "use the chatbot",
                            "explanation": "Ask me about project features, technical details, or implementation guidance - I'll provide focused, relevant responses",
                        },
                        {
                            "action": "get help with development",
                            "explanation": "I can assist with code examples, best practices, and problem-solving guidance",
                        }
                    ],
                )
            ]
        )

        # Example patterns
        self.patterns[ResponseType.EXAMPLE].extend(
            [
                ResponsePattern(
                    type=ResponseType.EXAMPLE,
                    template="Here's an example of {topic}:\n\n```{language}\n{code}\n```\n\n{explanation}",
                    variables=["topic", "language", "code", "explanation"],
                    examples=[
                        {
                            "topic": "FastAPI endpoint",
                            "language": "python",
                            "code": "@app.get('/items/{item_id}')\ndef read_item(item_id: int):\n    return {'item_id': item_id}",
                            "explanation": "This creates a GET endpoint that accepts an item ID",
                        }
                    ],
                )
            ]
        )

        # Tutorial patterns
        self.patterns[ResponseType.TUTORIAL].extend(
            [
                ResponsePattern(
                    type=ResponseType.TUTORIAL,
                    template="Let's learn about {topic}:\n\n1. {step1}\n2. {step2}\n3. {step3}\n\n{additional_info}",
                    variables=["topic", "step1", "step2", "step3", "additional_info"],
                    examples=[
                        {
                            "topic": "GitHub Actions",
                            "step1": "Create .github/workflows directory",
                            "step2": "Add workflow YAML file",
                            "step3": "Configure workflow triggers and steps",
                            "additional_info": "Workflows run automatically on specified events",
                        }
                    ],
                )
            ]
        )

        # Troubleshooting patterns
        self.patterns[ResponseType.TROUBLESHOOT].extend(
            [
                ResponsePattern(
                    type=ResponseType.TROUBLESHOOT,
                    template="To fix {issue}:\n\n1. First, check {check}\n2. Then, try {solution}\n3. If that doesn't work, {alternative}\n\nCommon cause: {explanation}",
                    variables=[
                        "issue",
                        "check",
                        "solution",
                        "alternative",
                        "explanation",
                    ],
                    examples=[
                        {
                            "issue": "failed GitHub Actions workflow",
                            "check": "the workflow logs",
                            "solution": "update dependencies",
                            "alternative": "rebuild the environment",
                            "explanation": "Outdated dependencies often cause workflow failures",
                        }
                    ],
                )
            ]
        )

    def get_pattern(self, response_type: ResponseType) -> List[ResponsePattern]:
        """Get all patterns for a specific response type."""
        return self.patterns[response_type]

    def get_random_pattern(self, response_type: ResponseType) -> ResponsePattern:
        """Get a random pattern for variety in responses."""
        import random

        patterns = self.patterns[response_type]
        return random.choice(patterns) if patterns else None
