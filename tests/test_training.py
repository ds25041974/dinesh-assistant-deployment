"""
Integration tests for the training system.
"""

import pytest

from ..training.knowledge_base import Domain, KnowledgeBase
from ..training.response_patterns import ResponseType, TrainingConfig
from ..training.training_manager import TrainingManager


def test_knowledge_base_initialization():
    """Test knowledge base initialization."""
    kb = KnowledgeBase()

    # Check Python knowledge
    python_venv = kb.get_knowledge(Domain.PYTHON, "virtual_environments")
    assert python_venv is not None
    assert python_venv.topic == "Virtual Environments"
    assert len(python_venv.examples) > 0

    # Check GitHub knowledge
    github_actions = kb.get_knowledge(Domain.GITHUB, "actions")
    assert github_actions is not None
    assert github_actions.topic == "GitHub Actions"
    assert len(github_actions.examples) > 0


def test_response_generation():
    """Test response generation for different queries."""
    config = TrainingConfig()
    manager = TrainingManager(config)

    # Test Python-related query
    python_response = manager.process_query("How do I create a virtual environment?")
    assert "virtual environment" in python_response["response"].lower()
    assert len(python_response["references"]) > 0

    # Test GitHub-related query
    github_response = manager.process_query("Help with GitHub Actions workflow")
    assert "github actions" in github_response["response"].lower()
    assert "workflow" in github_response["response"].lower()

    # Test troubleshooting query
    error_response = manager.process_query("Fix GitHub Actions error")
    assert any(
        word in error_response["response"].lower()
        for word in ["check", "solution", "fix"]
    )


def test_response_types():
    """Test different response types."""
    config = TrainingConfig()
    manager = TrainingManager(config)

    # Test example response
    example_response = manager.process_query("Show me an example of FastAPI")
    assert "```" in example_response["response"]  # Should contain code block

    # Test tutorial response
    tutorial_response = manager.process_query("How to use MCP server?")
    assert any(
        str(i) in tutorial_response["response"] for i in range(1, 4)
    )  # Should have numbered steps

    # Test direct response
    direct_response = manager.process_query("What is CI/CD?")
    assert "Example:" in direct_response["response"]


def test_fallback_responses():
    """Test fallback responses for unknown queries."""
    config = TrainingConfig()
    manager = TrainingManager(config)

    response = manager.process_query("Tell me about quantum computing")
    assert "apologize" in response["response"].lower()
    assert "python" in response["response"].lower()  # Should mention supported topics


def test_knowledge_search():
    """Test knowledge base search functionality."""
    kb = KnowledgeBase()

    # Test exact match
    results = kb.search_knowledge("virtual environment")
    assert len(results) > 0
    assert any(r.topic == "Virtual Environments" for r in results)

    # Test partial match
    results = kb.search_knowledge("github")
    assert len(results) > 0
    assert any(r.domain == Domain.GITHUB for r in results)

    # Test case insensitivity
    results = kb.search_knowledge("FASTAPI")
    assert len(results) > 0
    assert any("FastAPI" in r.topic for r in results)
