"""Domain definitions for the chatbot knowledge base."""

from enum import Enum, auto


class Domain(Enum):
    """Knowledge domains for the chatbot."""

    ARCHITECTURE = auto()  # Project architecture and design
    PYTHON = auto()  # Python-specific features and implementations
    DEPLOYMENT = auto()  # Deployment and service management
    GITHUB = auto()  # GitHub integration and services
    WEB = auto()  # Web interface and APIs
    MCP = auto()  # Model Context Protocol servers
    OPERATION = auto()  # Operational aspects and maintenance
    TESTING = auto()  # Testing frameworks and procedures
    PROJECT = auto()  # General project information
    TRAINING = auto()  # Training and knowledge management