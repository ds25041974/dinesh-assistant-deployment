"""
Conversation patterns and human-like behavior for Dinesh Assistant.
"""

import random
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Union


class Emotion(Enum):
    """Emotional states for response tone."""

    NEUTRAL = "neutral"
    EMPATHETIC = "empathetic"
    ENCOURAGING = "encouraging"
    PROFESSIONAL = "professional"
    THOUGHTFUL = "thoughtful"


class PersonalityTrait(Enum):
    """Personality traits for consistent behavior."""

    HELPFUL = "helpful"
    PATIENT = "patient"
    KNOWLEDGEABLE = "knowledgeable"
    PRECISE = "precise"
    FRIENDLY = "friendly"


@dataclass
class ConversationContext:
    """Maintains context for natural conversation flow."""

    user_name: Optional[str] = None
    conversation_history: List[Dict[str, str]] = None
    current_topic: Optional[str] = None
    emotion_state: Emotion = Emotion.NEUTRAL
    interaction_count: int = 0

    def __post_init__(self):
        self.conversation_history = (
            [] if self.conversation_history is None else self.conversation_history
        )


class ConversationPatternLibrary:
    """Library of human-like conversation patterns."""

    def __init__(self):
        self._initialize_patterns()

    def _initialize_patterns(self):
        """Initialize conversation patterns."""
        self.greetings = {
            "first_time": [
                "Hello! I'm Dinesh Assistant, ready to assist with the project.",
                "Hi there! I'm here to help with project tasks.",
                "Welcome! I'm your project assistant.",
            ],
            "returning": [
                "Welcome back to the project!",
                "Good to see you again! What would you like to know?",
                "Hello again! Ready to discuss the project?",
            ],
        }

        self.acknowledgments = {
            "understanding": [
                "I see what you're trying to do.",
                "I understand your requirement.",
                "That's a good question about {topic}.",
            ],
            "thinking": [
                "Let me think about the best way to help you with that.",
                "I'll find the most relevant information for you.",
                "Give me a moment to gather the best resources.",
            ],
        }

        self.empathy_patterns = {
            "error_encountered": [
                "I understand how frustrating these errors can be.",
                "Don't worry, we'll solve this together.",
                "That's a tricky issue, but we can fix it.",
            ],
            "learning_new": [
                "Learning new technologies can be challenging, but I'm here to help.",
                "Take your time. We'll go through this step by step.",
                "That's a great topic to learn about. Let's explore it together.",
            ],
        }

        self.encouragement = {
            "progress": [
                "You're making good progress!",
                "That's exactly right!",
                "You're getting the hang of this!",
            ],
            "difficulty": [
                "Let's break this down into smaller steps.",
                "We can tackle this one piece at a time.",
                "Don't worry if it seems complex at first.",
            ],
        }

        self.clarification = {
            "request": [
                "Could you tell me more about what you're trying to achieve?",
                "Just to make sure I understand correctly, are you trying to {action}?",
                "Would you mind providing a bit more context?",
            ],
            "confirmation": [
                "Is that what you were looking for?",
                "Did that help answer your question?",
                "Would you like me to explain anything in more detail?",
            ],
        }

        self.transitions = {
            "topic_change": [
                "Now, regarding your question about {new_topic}...",
                "Let's move on to your point about {new_topic}.",
                "Speaking of {new_topic}...",
            ],
            "additional_info": [
                "I can also tell you about {related_topic} if you're interested.",
                "This relates to {related_topic}, which might be helpful to know.",
                "You might also want to know about {related_topic}.",
            ],
        }


class ConversationEnhancer:
    """Enhances responses with human-like conversation patterns."""

    def __init__(self):
        self.patterns = ConversationPatternLibrary()
        self.context = ConversationContext()

    def enhance_response(
        self, response: str, query: str, topic: Optional[str] = None
    ) -> str:
        """
        Enhance a technical response with human-like elements.

        Args:
            response: The technical response to enhance
            query: The original user query
            topic: The current topic of discussion

        Returns:
            Enhanced response with human-like elements
        """
        # For help queries, return unmodified response
        query_lower = query.lower().strip()
        help_patterns = {
            "help",
            "how can you help",
            "what can you help with",
            "how can you help me",
            "what can you do",
            "what do you do",
            "what can you do for me",
            "how can ai help me",
            "what are your features",
        }
        if any(pattern in query_lower for pattern in help_patterns):
            # Enhance help responses with a friendly introduction
            enhanced = []
            if not response.startswith("I'm your AI-powered project assistant"):
                enhanced.append("I'm here to help you succeed! Let me show you what I can do.")
            enhanced.append(response)
            return "\n".join(enhanced)

        # For greetings, return unmodified response
        greeting_patterns = {"hi", "hello", "hey", "greetings", "hi there"}
        if query_lower in greeting_patterns:
            return response

        enhanced = []

        # Apply empathy patterns for errors
        if "error" in query_lower or "problem" in query_lower or "issue" in query_lower:
            enhanced.append(random.choice(self.patterns.empathy_patterns["error_encountered"]))
        
        # Apply learning support patterns
        if "learn" in query_lower or "teach" in query_lower or "explain" in query_lower:
            enhanced.append(random.choice(self.patterns.empathy_patterns["learning_new"]))
        
        # Add contextual acknowledgment
        if len(query.split()) > 3:
            if topic:
                enhanced.append(f"Regarding {topic}:")

        # Add main response
        enhanced.append(response)

        # For technical queries, add a simple follow-up
        if topic and topic not in ["general_help", "greeting"]:
            enhanced.append("\nWould you like more specific details about this?")

        # Update context
        self.context.interaction_count += 1
        self.context.current_topic = topic
        self.context.conversation_history.append({"query": query, "response": response})

        return "\n".join(enhanced)

    def generate_farewell(self) -> str:
        """Generate a contextual farewell message."""
        base_message = (
            f"We've had {self.context.interaction_count} helpful interactions. "
            "I hope I've been able to assist you well!\n\n"
        )
        
        follow_ups = [
            "Is there anything else you'd like to know?",
            "Feel free to ask if you have more questions!",
            "Don't hesitate to reach out if you need more help.",
        ]
        
        return base_message + random.choice(follow_ups)

    def reset_context(self):
        """Reset the conversation context."""
        self.context = ConversationContext()

    def update_context(self, query: str, response: str):
        """Update conversation context with new query-response pair."""
        self.context.interaction_count += 1
        self.context.conversation_history.append({"query": query, "response": response})
