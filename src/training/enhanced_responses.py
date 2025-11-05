"""Enhanced response patterns for more natural and context-aware responses."""

from typing import Dict, List, Optional

class ResponsePattern:
    """Pattern for generating responses."""

    def __init__(self, template: str, variables: List[str], context_required: bool = False):
        """Initialize response pattern."""
        self.template = template
        self.variables = variables
        self.context_required = context_required

    def requires_context(self) -> bool:
        """Check if pattern requires conversation context."""
        return self.context_required

class ResponsePatterns:
    """Collection of response patterns for different scenarios."""

    @staticmethod
    def get_greeting_patterns() -> List[ResponsePattern]:
        """Get greeting response patterns."""
        return [
            ResponsePattern(
                "Hi! 👋 I'm your AI assistant. I can help you with:\n\n"
                "1. Project Features & Architecture 🏗️\n"
                "2. Development & Implementation 💻\n"
                "3. Testing & Deployment 🚀\n"
                "4. System Operations 🔧\n\n"
                "What would you like to know more about?",
                [],
                False
            ),
            ResponsePattern(
                "Hello! 👋 I'm here to assist you with the Dinesh Assistant project.\n\n"
                "I can help with:\n"
                "• Understanding the architecture\n"
                "• Development questions\n"
                "• Implementation details\n"
                "• And much more!\n\n"
                "How can I help you today?",
                [],
                False
            )
        ]

    @staticmethod
    def get_project_info_patterns() -> List[ResponsePattern]:
        """Get project information response patterns."""
        return [
            ResponsePattern(
                "Let me tell you about {topic}:\n\n"
                "{description}\n\n"
                "Would you like to know more about any specific aspect?",
                ["topic", "description"],
                False
            ),
            ResponsePattern(
                "Here's an overview of {topic}:\n\n"
                "{description}\n\n"
                "I can provide more details about any of these points. What interests you?",
                ["topic", "description"],
                False
            )
        ]

    @staticmethod
    def get_code_example_patterns() -> List[ResponsePattern]:
        """Get code example response patterns."""
        return [
            ResponsePattern(
                "Here's how to {action}:\n\n"
                "```{language}\n{code}\n```\n\n"
                "Explanation:\n{explanation}\n\n"
                "Would you like me to clarify any part of this?",
                ["action", "language", "code", "explanation"],
                False
            ),
            ResponsePattern(
                "You can {action} like this:\n\n"
                "```{language}\n{code}\n```\n\n"
                "Here's what's happening:\n{explanation}\n\n"
                "Let me know if you need any clarification!",
                ["action", "language", "code", "explanation"],
                False
            )
        ]

    @staticmethod
    def get_error_handling_patterns() -> List[ResponsePattern]:
        """Get error handling response patterns."""
        return [
            ResponsePattern(
                "I see you're having an issue with {issue}. Let's fix that:\n\n"
                "1. First, check {check}\n"
                "2. Then try this solution: {solution}\n"
                "3. If that doesn't work: {alternative}\n\n"
                "Additional context:\n{explanation}\n\n"
                "Would you like me to explain any of these steps in more detail?",
                ["issue", "check", "solution", "alternative", "explanation"],
                False
            ),
            ResponsePattern(
                "To resolve the {issue}, follow these steps:\n\n"
                "1. {check}\n"
                "2. {solution}\n"
                "3. {alternative}\n\n"
                "Explanation:\n{explanation}\n\n"
                "Let me know if you need help with any of these steps!",
                ["issue", "check", "solution", "alternative", "explanation"],
                False
            )
        ]

    @staticmethod
    def get_tutorial_patterns() -> List[ResponsePattern]:
        """Get tutorial response patterns."""
        return [
            ResponsePattern(
                "Let me guide you through {topic}:\n\n"
                "1. {step1}\n"
                "2. {step2}\n"
                "3. {step3}\n\n"
                "Additional Information:\n{additional_info}\n\n"
                "Would you like me to explain any of these steps in more detail?",
                ["topic", "step1", "step2", "step3", "additional_info"],
                False
            ),
            ResponsePattern(
                "Here's a step-by-step guide for {topic}:\n\n"
                "Step 1: {step1}\n"
                "Step 2: {step2}\n"
                "Step 3: {step3}\n\n"
                "Note:\n{additional_info}\n\n"
                "Which step would you like me to elaborate on?",
                ["topic", "step1", "step2", "step3", "additional_info"],
                False
            )
        ]

    @staticmethod
    def get_context_aware_patterns() -> List[ResponsePattern]:
        """Get context-aware response patterns."""
        return [
            ResponsePattern(
                "Building on our discussion about {previous_topic}, here's information about {new_topic}:\n\n"
                "{content}\n\n"
                "Would you like me to explain how this relates to {previous_topic}?",
                ["previous_topic", "new_topic", "content"],
                True
            ),
            ResponsePattern(
                "Since we were talking about {previous_topic}, let me show you how {new_topic} connects:\n\n"
                "{content}\n\n"
                "I can explain more about either topic. What interests you?",
                ["previous_topic", "new_topic", "content"],
                True
            )
        ]

class ResponseLibrary:
    """Library of response patterns."""

    def __init__(self):
        """Initialize response library."""
        self._patterns: Dict[str, List[ResponsePattern]] = {
            "greeting": ResponsePatterns.get_greeting_patterns(),
            "project_info": ResponsePatterns.get_project_info_patterns(),
            "code_example": ResponsePatterns.get_code_example_patterns(),
            "error_handling": ResponsePatterns.get_error_handling_patterns(),
            "tutorial": ResponsePatterns.get_tutorial_patterns(),
            "context_aware": ResponsePatterns.get_context_aware_patterns()
        }

    def get_patterns(self, category: str) -> Optional[List[ResponsePattern]]:
        """Get response patterns for a category."""
        return self._patterns.get(category)

    def add_patterns(self, category: str, patterns: List[ResponsePattern]) -> None:
        """Add new patterns to a category."""
        if category in self._patterns:
            self._patterns[category].extend(patterns)
        else:
            self._patterns[category] = patterns