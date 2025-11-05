"""Core response templates for common queries."""

HELP_RESPONSE = {
    "general": (
        "Let me show you exactly what I can do to help you! 🚀\n\n"
        "1. I'm Your Project Guide 🎯\n"
        "   • Help you understand the codebase\n"
        "   • Guide you through features\n"
        "   • Fix problems and errors\n"
        "   • Share best practices\n\n"
        "2. Development Support 💻\n"
        "   • Code understanding\n"
        "   • Testing and quality\n"
        "   • Best practices\n"
        "   • Problem-solving\n\n"
        "3. Documentation Help �\n"
        "   • Project structure\n"
        "   • Implementation guides\n"
        "   • Configuration info\n"
        "   • Usage examples\n\n"
        "Just ask specific questions like:\n"
        '• "What features does this project have?"\n'
        '• "How do I implement [specific feature]?"\n'
        '• "Help me understand [concept]"\n'
        '• "Can you explain [specific part]?"\n\n'
        "I'll provide focused, relevant answers without going off-topic."
    ),
    "project": (
        "Here's what I can tell you about the project:\n\n"
        "1. Core Features\n"
        "   • Smart chatbot assistant\n"
        "   • Natural language processing\n"
        "   • Context-aware responses\n\n"
        "2. Technical Stack\n"
        "   • Python backend\n"
        "   • FastAPI web framework\n"
        "   • Modular architecture\n\n"
        "What specific aspect would you like to know more about?"
    ),
    "mcp": (
        "The Model Context Protocol (MCP) is a specialized protocol for AI/ML model interaction. "
        "It provides:\n\n"
        "1. Standardized Communication\n"
        "   • Consistent API interface\n"
        "   • Structured data exchange\n"
        "   • Protocol buffers support\n\n"
        "2. Integration Features\n"
        "   • Client-server architecture\n"
        "   • Authentication handling\n"
        "   • Error management\n\n"
        "Would you like to know about:\n"
        "• Implementation details?\n"
        "• API specifications?\n"
        "• Integration steps?\n"
    ),
}

ERROR_RESPONSES = {
    "not_understood": (
        "I need more specific information to help you better. Could you:\n\n"
        "1. Specify what aspect you're interested in?\n"
        "2. Ask about a particular feature or concept?\n"
        "3. Share what you're trying to accomplish?\n\n"
        "This helps me provide more relevant answers."
    ),
    "off_topic": (
        "I'm focused on helping with this project and related development tasks. "
        "Could you ask something specific about:\n\n"
        "• Project features and implementation\n"
        "• Technical questions and problems\n"
        "• Development guidance\n"
    ),
}

GREETING_RESPONSE = (
    "Hello! 👋 I'm here to help with project-related questions and development tasks.\n\n"
    "You can ask me about:\n"
    "• Project features and capabilities\n"
    "• Implementation details\n"
    "• Technical problems\n\n"
    "What would you like to know?"
)
