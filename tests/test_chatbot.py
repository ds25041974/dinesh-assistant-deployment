"""Tests for Dinesh Assistant chatbot."""

import pytest

from src.chatbot import DineshAssistant, Response


@pytest.fixture
def assistant():
    """Create chatbot instance for testing."""
    return DineshAssistant()


def test_greeting(assistant):
    """Test chatbot greeting."""
    greeting = assistant.greet()
    assert isinstance(greeting, str)
    assert "project assistant" in greeting.lower()
    assert "help you with" in greeting.lower()


@pytest.mark.asyncio
async def test_config_response(assistant):
    """Test configuration-related responses."""
    response = await assistant.respond("how do I configure the project?")
    assert isinstance(response, Response)
    assert "project" in response.text.lower()
    assert "development" in response.text.lower()
    assert response.confidence > 0.7
    assert any(ref in response.references for ref in ["Project Guide", "README.md"])


@pytest.mark.asyncio
async def test_i18n_response(assistant):
    """Test i18n-related responses."""
    response = await assistant.respond("what languages are supported?")
    assert isinstance(response, Response)
    assert "english" in response.text.lower()
    assert "spanish" in response.text.lower()
    assert response.confidence > 0.7
    assert any("i18n.py" in ref for ref in response.references)


@pytest.mark.asyncio
async def test_template_response(assistant):
    """Test template-related responses."""
    response = await assistant.respond("what template types are available?")
    assert isinstance(response, Response)
    assert "formal" in response.text.lower()
    assert "business" in response.text.lower()
    assert response.confidence > 0.7
    assert any("template" in ref.lower() for ref in response.references)


@pytest.mark.asyncio
async def test_validation_response(assistant):
    """Test validation-related responses."""
    response = await assistant.respond("how do I validate configurations?")
    assert isinstance(response, Response)
    assert "validator" in response.text.lower()
    assert response.confidence > 0.7
    assert any("validation" in ref.lower() for ref in response.references)


@pytest.mark.asyncio
async def test_test_response(assistant):
    """Test testing-related responses."""
    response = await assistant.respond("how do I run tests?")
    assert isinstance(response, Response)
    assert "pytest" in response.text.lower()
    assert response.confidence > 0.7
    assert any("test" in ref.lower() for ref in response.references)


@pytest.mark.asyncio
async def test_unknown_query(assistant):
    """Test fallback for unknown queries."""
    response = await assistant.respond("what is the meaning of life?")
    assert isinstance(response, Response)
    assert "not quite sure" in response.text.lower()
    assert response.confidence < 0.5


@pytest.mark.asyncio
async def test_context_tracking(assistant):
    """Test conversation context tracking."""
    response1 = await assistant.respond("what is this project?")
    response2 = await assistant.respond("how do I use it?")

    assert isinstance(response1, Response)
    assert isinstance(response2, Response)
    assert "project" in response1.text.lower()
    assert "features" in response1.text.lower()
    assert response1.confidence > 0.7
    assert response2.confidence > 0.7
