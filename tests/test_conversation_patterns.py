"""Test suite for conversation patterns."""

from src.training.conversation_patterns import (
    ConversationContext,
    ConversationEnhancer,
    ConversationPatternLibrary,
    Emotion,
)


def test_conversation_context_initialization():
    """Test initialization of ConversationContext."""
    context = ConversationContext()
    assert context.user_name is None
    assert context.conversation_history == []
    assert context.current_topic is None
    assert context.emotion_state == Emotion.NEUTRAL
    assert context.interaction_count == 0


def test_pattern_library_initialization():
    """Test initialization of ConversationPatternLibrary."""
    library = ConversationPatternLibrary()

    # Test all pattern categories exist
    assert hasattr(library, "greetings")
    assert hasattr(library, "acknowledgments")
    assert hasattr(library, "empathy_patterns")
    assert hasattr(library, "encouragement")
    assert hasattr(library, "clarification")
    assert hasattr(library, "transitions")

    # Test pattern categories have content
    assert len(library.greetings["first_time"]) > 0
    assert len(library.acknowledgments["understanding"]) > 0
    assert len(library.empathy_patterns["error_encountered"]) > 0


def test_conversation_enhancer_basic_response():
    """Test basic response enhancement."""
    enhancer = ConversationEnhancer()
    response = "Here's how to use Python lists."
    query = "How do I use lists in Python?"
    topic = "Python Lists"

    enhanced = enhancer.enhance_response(response, query, topic)

    # Check if enhanced response contains key components
    assert response in enhanced
    assert topic in enhanced
    assert enhancer.context.interaction_count == 1
    assert enhancer.context.current_topic == topic


def test_conversation_enhancer_error_empathy():
    """Test empathetic response for error-related queries."""
    enhancer = ConversationEnhancer()
    response = "Check your syntax and make sure all brackets are closed."
    query = "I'm getting an error in my Python code"

    enhanced = enhancer.enhance_response(response, query)

    # Check if response includes empathy for errors
    assert any(
        pattern in enhanced
        for pattern in enhancer.patterns.empathy_patterns["error_encountered"]
    )


def test_conversation_enhancer_learning_support():
    """Test supportive response for learning-related queries."""
    enhancer = ConversationEnhancer()
    response = "Python is a high-level programming language."
    query = "I want to learn Python"

    enhanced = enhancer.enhance_response(response, query)

    # Check if response includes learning support
    assert any(
        pattern in enhanced
        for pattern in enhancer.patterns.empathy_patterns["learning_new"]
    )


def test_conversation_enhancer_context_reset():
    """Test conversation context reset."""
    enhancer = ConversationEnhancer()

    # Generate some conversation history
    enhancer.enhance_response("Response 1", "Query 1", "Topic 1")
    enhancer.enhance_response("Response 2", "Query 2", "Topic 2")

    assert enhancer.context.interaction_count == 2
    assert len(enhancer.context.conversation_history) == 2

    # Reset context
    enhancer.reset_context()

    assert enhancer.context.interaction_count == 0
    assert len(enhancer.context.conversation_history) == 0


def test_conversation_enhancer_farewell():
    """Test farewell message generation."""
    enhancer = ConversationEnhancer()

    # Generate some conversation history
    enhancer.enhance_response("Response 1", "Query 1")
    enhancer.enhance_response("Response 2", "Query 2")

    farewell = enhancer.generate_farewell()

    assert isinstance(farewell, str)
    assert len(farewell) > 0
    assert str(enhancer.context.interaction_count) in farewell
