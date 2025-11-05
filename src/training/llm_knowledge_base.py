"""
LLM Knowledge Base Integration for enhanced responses and natural language understanding.
Uses OpenAI's capabilities to provide more natural and contextual responses.
"""

import os
import openai
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Any, Union
from enum import Enum

# Initialize OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY", "your-api-key-here")

# System prompt for consistent behavior
SYSTEM_PROMPT = """You are an AI assistant specifically trained for this project. Your responses should:
1. Be focused and relevant to the specific query
2. Avoid repeating information across different topics
3. Maintain context awareness
4. Provide clear, structured answers
5. Use appropriate technical detail level

When handling combined topics (e.g., MCP + Python), organize the response to clearly separate and relate the topics.
Avoid generic responses and focus on project-specific details."""

class IntentCategory(Enum):
    """Categories for user intents to better understand queries."""
    TECHNICAL = "technical"
    TUTORIAL = "tutorial"
    TROUBLESHOOTING = "troubleshooting"
    PROJECT = "project"
    GENERAL = "general"
    DEVELOPMENT = "development"
    PYTHON = "python"
    GITHUB = "github"
    CICD = "cicd"
    MCP = "mcp"
    ARCHITECTURE = "architecture"
    AI_MODEL = "ai_model"
    LOCAL_DEV = "local_development"

@dataclass
class EnhancedPrompt:
    """Structure for enhanced prompts with variations and context."""
    base_prompt: str
    variations: List[str]  # Different ways to phrase the same query
    keywords: List[str]    # Technical keywords
    layman_terms: List[str]  # Non-technical equivalent terms
    context: Dict[str, Union[str, bool]]  # Additional context for understanding
    category: IntentCategory

@dataclass
class LLMResponse:
    """Structured response from LLM with enhanced context."""
    text: str
    confidence: float
    context: Dict[str, Any]
    follow_ups: List[str]  # Suggested follow-up questions
    code_examples: Optional[List[str]] = None
    references: Optional[List[str]] = None

class LLMKnowledgeBase:
    """Enhanced knowledge base using LLM capabilities."""
    
    def __init__(self) -> None:
        self.context: Dict[str, Any] = {}
        self.openai_available = bool(openai.api_key and openai.api_key != "your-api-key-here")
        self.prompts: Dict[str, EnhancedPrompt] = {}
        self.response_templates: Dict[IntentCategory, List[str]] = {}
        self._initialize_knowledge()

    def _initialize_knowledge(self):
        """Initialize enhanced prompts and responses with comprehensive domain knowledge."""
        # Python Development Knowledge
        self.prompts["python_dev"] = EnhancedPrompt(
            base_prompt="How can I implement or use Python features in this project?",
            variations=[
                "How do I use Python in this project?",
                "Show me Python examples",
                "Help with Python coding",
                "Python best practices",
                "How to structure Python code",
                "Python design patterns",
                "Advanced Python features"
            ],
            keywords=[
                "async/await", "decorators", "type hints", "dataclasses",
                "context managers", "generators", "iterators", "metaclasses",
                "descriptors", "protocols", "abstract base classes",
                "dependency injection", "factories", "singletons"
            ],
            layman_terms=[
                "write better code", "improve code quality",
                "make code faster", "organize code",
                "handle errors better", "write cleaner code",
                "make code reusable", "fix code problems"
            ],
            context={
                "skill_level": "mixed",
                "focus": "python_mastery",
                "needs": "practical_implementation",
                "best_practices": True,
                "performance_oriented": True
            },
            category=IntentCategory.PYTHON
        )
        
        # FastAPI Integration Knowledge
        self.prompts["fastapi_dev"] = EnhancedPrompt(
            base_prompt="How can I work with FastAPI in this project?",
            variations=[
                "FastAPI implementation help",
                "API development guide",
                "FastAPI best practices",
                "How to create endpoints",
                "FastAPI authentication",
                "API documentation"
            ],
            keywords=[
                "FastAPI", "Pydantic", "endpoints", "async",
                "OpenAPI", "Swagger", "middleware", "dependency injection",
                "path operations", "request validation", "response models",
                "background tasks", "WebSocket", "CORS", "security"
            ],
            layman_terms=[
                "create web service", "build API",
                "handle web requests", "process data",
                "validate input", "secure API",
                "document API", "manage users"
            ],
            context={
                "skill_level": "intermediate",
                "focus": "web_development",
                "needs": "api_design",
                "security_focused": True
            },
            category=IntentCategory.TECHNICAL
        )

        # Project Understanding Prompts
        self.prompts["project_overview"] = EnhancedPrompt(
            base_prompt="What does this project do and how can I use it?",
            variations=[
                "Explain this project to me",
                "How does this work?",
                "What's this all about?",
                "Give me an overview"
            ],
            keywords=[
                "architecture", "structure", "components",
                "features", "implementation", "design"
            ],
            layman_terms=[
                "big picture", "overview", "summary",
                "explanation", "guide", "walkthrough"
            ],
            context={
                "skill_level": "any",
                "focus": "understanding",
                "needs": "clear_explanation"
            },
            category=IntentCategory.PROJECT
        )

        # Troubleshooting Prompts
        self.prompts["error_help"] = EnhancedPrompt(
            base_prompt="Help me fix an error or problem in the code",
            variations=[
                "Why isn't this working?",
                "How do I fix this error?",
                "Debug help needed",
                "Code not working"
            ],
            keywords=[
                "exception", "error", "bug", "issue",
                "debug", "fix", "problem", "traceback"
            ],
            layman_terms=[
                "not working", "broken", "stuck",
                "help", "issues", "problems"
            ],
            context={
                "skill_level": "any",
                "focus": "problem_solving",
                "needs": "specific_solution"
            },
            category=IntentCategory.TROUBLESHOOTING
        )

        # GitHub Knowledge
        self.prompts["github_integration"] = EnhancedPrompt(
            base_prompt="How to use GitHub features and integration?",
            variations=[
                "GitHub workflow help",
                "Repository management",
                "Git commands guide",
                "GitHub Actions setup",
                "Pull request workflow",
                "GitHub CI/CD"
            ],
            keywords=[
                "git", "github", "actions", "workflows", "pull requests",
                "branches", "commits", "merge", "rebase", "CI/CD",
                "repository", "issues", "projects", "releases"
            ],
            layman_terms=[
                "save code changes", "collaborate",
                "track changes", "review code",
                "manage project", "automate tasks",
                "share code", "backup code"
            ],
            context={
                "skill_level": "mixed",
                "focus": "version_control",
                "needs": "collaboration",
                "automation": True
            },
            category=IntentCategory.GITHUB
        )

        # CI/CD Knowledge
        self.prompts["cicd_implementation"] = EnhancedPrompt(
            base_prompt="How to implement CI/CD pipelines?",
            variations=[
                "Setup continuous integration",
                "Deployment automation",
                "Pipeline configuration",
                "GitHub Actions workflow",
                "Testing automation",
                "Release process"
            ],
            keywords=[
                "pipeline", "workflows", "automation", "testing",
                "deployment", "integration", "docker", "kubernetes",
                "infrastructure", "monitoring", "secrets"
            ],
            layman_terms=[
                "automatic testing", "code checks",
                "automatic deployment", "build process",
                "quality checks", "release process",
                "deployment steps"
            ],
            context={
                "skill_level": "advanced",
                "focus": "automation",
                "needs": "reliability",
                "security_focused": True
            },
            category=IntentCategory.CICD
        )

        # MCP Server Knowledge
        self.prompts["mcp_server"] = EnhancedPrompt(
            base_prompt="How to work with MCP server?",
            variations=[
                "MCP integration guide",
                "Model Context Protocol",
                "MCP server setup",
                "MCP features usage",
                "Context management"
            ],
            keywords=[
                "MCP", "context protocol", "model integration",
                "server setup", "API", "context management",
                "state handling", "request processing"
            ],
            layman_terms=[
                "handle AI requests", "manage AI context",
                "process AI responses", "connect AI models",
                "smart responses", "AI integration"
            ],
            context={
                "skill_level": "advanced",
                "focus": "ai_integration",
                "needs": "implementation",
                "performance": True
            },
            category=IntentCategory.MCP
        )

        # Hybrid Architecture Knowledge
        self.prompts["hybrid_architecture"] = EnhancedPrompt(
            base_prompt="Understanding hybrid architecture implementation",
            variations=[
                "Hybrid system design",
                "Local and cloud integration",
                "Distributed architecture",
                "System components",
                "Architecture patterns"
            ],
            keywords=[
                "hybrid", "architecture", "microservices",
                "distributed systems", "scalability", "resilience",
                "cloud integration", "local processing"
            ],
            layman_terms=[
                "system design", "how it works",
                "system parts", "working together",
                "reliability", "performance",
                "flexibility"
            ],
            context={
                "skill_level": "advanced",
                "focus": "architecture",
                "needs": "understanding",
                "scalability": True
            },
            category=IntentCategory.ARCHITECTURE
        )

        # AI Model Integration
        self.prompts["ai_model"] = EnhancedPrompt(
            base_prompt="How to work with AI models in the system?",
            variations=[
                "AI integration guide",
                "Model implementation",
                "Neural network setup",
                "AI configuration",
                "Model training"
            ],
            keywords=[
                "AI", "machine learning", "neural networks",
                "model training", "inference", "optimization",
                "parameters", "hyperparameters"
            ],
            layman_terms=[
                "smart features", "learning system",
                "intelligent responses", "automated learning",
                "smart decisions", "pattern recognition"
            ],
            context={
                "skill_level": "advanced",
                "focus": "ai_implementation",
                "needs": "optimization",
                "performance": True
            },
            category=IntentCategory.AI_MODEL
        )

        # Initialize response templates with more natural, context-aware responses
        self.response_templates = {
            IntentCategory.TECHNICAL: [
                "📝 Here's a detailed technical explanation:\n\n{explanation}\n\n"
                "💡 Example Implementation:\n```python\n{code}\n```\n\n"
                "🔑 Key Points:\n{points}\n\n"
                "📚 Additional Resources:\n{resources}",
                
                "🛠️ Let me show you the technical approach:\n\n"
                "1️⃣ {concept_explanation}\n"
                "2️⃣ Here's how to implement it:\n```python\n{code}\n```\n"
                "3️⃣ Important considerations:\n{considerations}\n"
                "💡 Pro tip: {tip}"
            ],
            
            IntentCategory.PROJECT: [
                "🌟 Project Overview:\n\n{overview}\n\n"
                "✨ Key Features:\n{features}\n\n"
                "🚀 Getting Started:\n{steps}\n\n"
                "💡 Best Practices:\n{practices}",
                
                "📋 Project Guide:\n\n"
                "📌 Purpose: {purpose}\n"
                "🎯 Main Components:\n{components}\n"
                "⚡ Key Functionality:\n{functionality}\n"
                "🔧 Setup Guide:\n{setup}"
            ],
            
            IntentCategory.TROUBLESHOOTING: [
                "🔍 Issue Analysis:\n\n"
                "❗ Problem: {diagnosis}\n\n"
                "✅ Solution:\n{solution}\n\n"
                "🛡️ Prevention Tips:\n{prevention}\n\n"
                "💡 Additional Context: {context}",
                
                "🛠️ Let's fix this step by step:\n\n"
                "1️⃣ Issue Identified: {issue}\n"
                "2️⃣ Root Cause: {cause}\n"
                "3️⃣ Solution Steps:\n{solution}\n"
                "📝 Note: {note}"
            ],
            
            IntentCategory.GITHUB: [
                "🌟 GitHub Guide:\n\n"
                "1️⃣ Process Overview:\n{overview}\n"
                "2️⃣ Step-by-Step:\n{steps}\n"
                "3️⃣ Best Practices:\n{practices}\n"
                "💡 Pro Tips:\n{tips}",
                
                "🔄 GitHub Workflow:\n\n"
                "📋 Setup: {setup}\n"
                "⚡ Commands:\n```bash\n{commands}\n```\n"
                "✨ Features: {features}\n"
                "🎯 Next Steps: {next_steps}"
            ],
            
            IntentCategory.CICD: [
                "🚀 CI/CD Pipeline Guide:\n\n"
                "1️⃣ Pipeline Overview:\n{overview}\n"
                "2️⃣ Configuration:\n```yaml\n{config}\n```\n"
                "3️⃣ Implementation Steps:\n{steps}\n"
                "📝 Important Notes:\n{notes}",
                
                "⚡ Automation Setup:\n\n"
                "🎯 Goals: {goals}\n"
                "🛠️ Tools: {tools}\n"
                "📋 Process: {process}\n"
                "✅ Validation: {validation}"
            ],

            IntentCategory.MCP: [
                "🔄 MCP Integration Guide:\n\n"
                "📌 Setup: {setup}\n"
                "🔗 Integration:\n```python\n{code}\n```\n"
                "⚙️ Configuration: {config}\n"
                "💡 Tips: {tips}",
                
                "🛠️ MCP Implementation:\n\n"
                "1️⃣ Architecture: {architecture}\n"
                "2️⃣ Components: {components}\n"
                "3️⃣ Usage:\n```python\n{usage}\n```\n"
                "📝 Notes: {notes}"
            ],
            
            IntentCategory.ARCHITECTURE: [
                "🏗️ Architecture Overview:\n\n"
                "📌 Design: {design}\n"
                "🔄 Flow: {flow}\n"
                "⚙️ Components: {components}\n"
                "📊 Scalability: {scalability}",
                
                "🌟 System Design:\n\n"
                "1️⃣ Overview: {overview}\n"
                "2️⃣ Components:\n{components}\n"
                "3️⃣ Integration: {integration}\n"
                "4️⃣ Best Practices: {practices}"
            ],
            
            IntentCategory.AI_MODEL: [
                "🤖 AI Model Guide:\n\n"
                "📌 Model: {model}\n"
                "⚙️ Configuration:\n```python\n{config}\n```\n"
                "🔄 Training: {training}\n"
                "📊 Performance: {performance}",
                
                "🎯 AI Implementation:\n\n"
                "1️⃣ Setup: {setup}\n"
                "2️⃣ Integration:\n```python\n{code}\n```\n"
                "3️⃣ Optimization: {optimization}\n"
                "💡 Tips: {tips}"
            ]
        }

    def enhance_response(self, query: str, base_response: str) -> LLMResponse:
        """Enhance a base response with LLM capabilities."""
        # Analyze query intent and context
        intent = self._analyze_intent(query)
        context = self._analyze_query_context(query)
        
        # Generate enhanced response components
        enhanced_text = self._add_context_to_response(base_response, context)
        examples = self._generate_relevant_examples(query)
        references = self._find_relevant_references(query)
        followups = self._generate_followups(query, context)
        
        # Add domain-specific enhancements
        if intent.get("domain") == "technical":
            enhanced_text = self._add_technical_context(enhanced_text, query)
        
        # Add human-like elements
        enhanced_text = self._add_personality(enhanced_text)
        enhanced_text = self._add_engagement_elements(enhanced_text)
        
        return LLMResponse(
            text=enhanced_text,
            confidence=self._calculate_confidence(query, enhanced_text),
            context={**context, "intent": intent},
            follow_ups=followups,
            code_examples=examples,
            references=references
        )

    def _add_context_to_response(self, text: str, context: Dict[str, Any]) -> str:
        """Add contextual information to the response."""
        # Add relevant context markers
        if context.get("intent") == "technical_question":
            text = f"📝 Technical Details: {text}"
        elif context.get("intent") == "concept_explanation":
            text = f"💡 Concept Overview: {text}"
        
        # Add domain-specific context
        domain = context.get("domain", "general")
        if domain != "general":
            text = f"[{domain.upper()}] {text}"
        
        return text

    def _analyze_intent(self, query: str) -> Dict[str, Any]:
        """Analyze query intent with domain awareness."""
        intent = {
            "domain": self._determine_domain(query),
            "complexity": "medium",
            "user_expertise": "intermediate"
        }
        return intent

    def _determine_domain(self, query: str) -> str:
        """Determine the technical domain of the query."""
        domain_keywords = {
            "technical": ["implement", "code", "function", "class", "method"],
            "conceptual": ["explain", "understand", "concept", "theory"],
            "troubleshooting": ["error", "bug", "fix", "issue", "problem"],
            "best_practices": ["best", "practice", "pattern", "recommend"]
        }
        # Implement domain detection logic
        return "technical"  # Placeholder

    def _add_technical_context(self, text: str, query: str) -> str:
        """Add relevant technical context to the response."""
        # Add technical details based on context
        return text  # Placeholder

    def _add_personality(self, text: str) -> str:
        """Add human-like personality elements to the response."""
        # Add conversational elements
        return text  # Placeholder

    def _add_engagement_elements(self, text: str) -> str:
        """Add elements to increase user engagement."""
        # Add encouraging and interactive elements
        return text  # Placeholder

    def _calculate_confidence(self, query: str, response: str) -> float:
        """Calculate confidence score for the response."""
        # Implement confidence calculation logic
        return 0.95  # Placeholder

    def _add_natural_language(self, response: str) -> str:
        """Add natural language elements to make response more conversational."""
        # This would use LLM to make the response more natural
        # For now, return the original response
        return response

    def _analyze_query_context(self, query: str) -> Dict[str, str]:
        """Analyze the query to understand context and intent."""
        # This would use LLM to analyze query context
        return {
            "intent": "technical_question",
            "complexity": "intermediate",
            "domain": "python_development"
        }

    def _generate_followups(self, query: str, context: Dict[str, str]) -> List[str]:
        """Generate relevant follow-up questions."""
        # This would use LLM to generate contextual follow-ups
        return [
            "Would you like to see more examples?",
            "Should I explain any part in more detail?",
            "Do you want to learn about related features?"
        ]

    def _generate_relevant_examples(self, query: str) -> List[str]:
        """Generate contextually relevant code examples."""
        # This would use LLM to generate specific examples
        return [
            "# Example implementation\ndef example():\n    pass",
            "# Alternative approach\nclass Alternative:\n    pass"
        ]

    def _find_relevant_references(self, query: str) -> List[str]:
        """Find relevant documentation and references."""
        # This would use LLM to find relevant documentation
        return [
            "Project Documentation",
            "Python Best Practices Guide",
            "Related Examples"
        ]

    async def analyze_error(self, query: str) -> LLMResponse:
        """Analyze and provide solutions for error-related queries."""
        # Identify error type and context
        error_type = self._identify_error_type(query)
        error_context = self._analyze_error_context(query)
        
        # Generate solution
        solution = self._generate_error_solution(error_type, error_context)
        
        # Find similar issues and prevention tips
        similar_issues = self._find_similar_issues(error_type)
        prevention_tips = self._generate_prevention_tips(error_type)
        
        # Format response using troubleshooting template
        template = self.response_templates[IntentCategory.TROUBLESHOOTING][0]
        response_text = template.format(
            diagnosis=error_context["description"],
            solution=solution,
            prevention="\n".join(f"• {tip}" for tip in prevention_tips),
            context="\n".join(similar_issues)
        )
        
        return LLMResponse(
            text=response_text,
            confidence=0.85,
            context={"type": "error", **error_context},
            follow_ups=self._generate_error_followups(error_type),
            code_examples=self._generate_error_examples(error_type),
            references=self._find_error_references(error_type)
        )

    async def get_domain_response(self, query: str, domain: str) -> LLMResponse:
        """Generate domain-specific responses."""
        # Get domain context and keywords
        domain_prompt = self.prompts.get(f"{domain}_dev") or self.prompts["project_overview"]
        
        # Generate domain-specific content
        content = self._generate_domain_content(query, domain_prompt)
        examples = self._generate_domain_examples(query, domain)
        references = self._find_domain_references(domain)
        
        # Format response using appropriate template
        category = IntentCategory[domain.upper()] if domain.upper() in IntentCategory.__members__ else IntentCategory.TECHNICAL
        template = self.response_templates[category][0]
        
        if domain == "python":
            response_text = template.format(
                explanation=content["explanation"],
                code=content["code"],
                points="\n".join(f"• {point}" for point in content["key_points"]),
                resources="\n".join(f"• {ref}" for ref in references)
            )
        else:
            response_text = content["text"]
        
        return LLMResponse(
            text=response_text,
            confidence=0.9,
            context={"type": "domain", "domain": domain, **content["context"]},
            follow_ups=self._generate_domain_followups(query, domain),
            code_examples=examples,
            references=references
        )

    async def get_general_response(self, query: str) -> LLMResponse:
        """Generate general responses for non-specific queries."""
        # Analyze general context
        context = self._analyze_query_context(query)
        intent = self._analyze_intent(query)
        
        # Generate content based on general understanding
        content = self._generate_general_content(query, context)
        examples = self._generate_general_examples(query)
        references = self._find_general_references(query)
        
        # Format response using appropriate template
        template = self.response_templates[IntentCategory.TECHNICAL][1]
        response_text = template.format(
            concept_explanation=content["explanation"],
            code=content.get("code", "# No code example available"),
            considerations=content["considerations"],
            tip=content["tip"]
        )
        
        return LLMResponse(
            text=response_text,
            confidence=0.75,
            context={"type": "general", **context},
            follow_ups=self._generate_followups(query, context),
            code_examples=examples,
            references=references
        )

    def _identify_error_type(self, query: str) -> str:
        """Identify the type of error from the query."""
        error_types = {
            "syntax": ["syntax", "invalid syntax", "parsing"],
            "runtime": ["runtime", "exception", "error occurred"],
            "logic": ["incorrect output", "wrong result", "not working"],
            "import": ["import", "module not found", "no module"],
            "attribute": ["attribute", "has no attribute", "undefined"]
        }
        
        for error_type, keywords in error_types.items():
            if any(keyword in query.lower() for keyword in keywords):
                return error_type
        return "unknown"

    def _analyze_error_context(self, query: str) -> Dict[str, str]:
        """Analyze the context of an error query."""
        return {
            "description": "Detailed error analysis",
            "severity": "medium",
            "scope": "local",
            "impact": "minimal"
        }

    def _generate_error_solution(self, error_type: str, context: Dict[str, str]) -> str:
        """Generate solution for the identified error."""
        solutions = {
            "syntax": "Review and correct the syntax according to Python's rules",
            "runtime": "Add appropriate error handling and input validation",
            "logic": "Review the logic and add debugging statements",
            "import": "Verify package installation and import statements",
            "attribute": "Check object type and available attributes"
        }
        return solutions.get(error_type, "Investigate the issue further")

    def _find_similar_issues(self, error_type: str) -> List[str]:
        """Find similar issues for the error type."""
        return [
            "Similar issue in related code",
            "Common pitfalls with this error",
            "Recent fixes for similar problems"
        ]

    def _generate_prevention_tips(self, error_type: str) -> List[str]:
        """Generate tips to prevent similar errors."""
        return [
            "Use type hints to catch errors early",
            "Add input validation",
            "Implement proper error handling",
            "Write comprehensive tests"
        ]

    def _generate_error_followups(self, error_type: str) -> List[str]:
        """Generate follow-up questions for error resolution."""
        return [
            "Would you like to see a working example?",
            "Should I explain the solution in more detail?",
            "Would you like to learn about prevention?"
        ]

    def _generate_error_examples(self, error_type: str) -> List[str]:
        """Generate example code showing error fixes."""
        return [
            "# Correct implementation\ntry:\n    result = process_data()\nexcept ValueError:\n    handle_error()",
            "# Alternative solution\ndef safe_process():\n    validate_input()"
        ]

    def _find_error_references(self, error_type: str) -> List[str]:
        """Find references related to the error type."""
        return [
            "Python Error Handling Guide",
            "Common Python Pitfalls",
            "Best Practices for Error Prevention"
        ]

    def _generate_domain_content(self, query: str, prompt: EnhancedPrompt) -> Dict[str, Any]:
        """Generate domain-specific content."""
        return {
            "explanation": "Detailed technical explanation",
            "code": "# Example implementation\ndef example():\n    pass",
            "key_points": ["Key point 1", "Key point 2", "Key point 3"],
            "context": {"expertise_level": "intermediate"},
            "text": "Comprehensive response text"
        }

    def _generate_domain_examples(self, query: str, domain: str) -> List[str]:
        """Generate domain-specific code examples."""
        return [
            "# Domain-specific example\ndef domain_example():\n    pass",
            "# Alternative approach\nclass DomainSolution:\n    pass"
        ]

    def _find_domain_references(self, domain: str) -> List[str]:
        """Find domain-specific references."""
        return [
            f"{domain.title()} Documentation",
            f"{domain.title()} Best Practices",
            f"{domain.title()} Examples"
        ]

    def _generate_domain_followups(self, query: str, domain: str) -> List[str]:
        """Generate domain-specific follow-up questions."""
        return [
            f"Would you like to explore more {domain} features?",
            "Should we dive deeper into any specific aspect?",
            "Would you like to see more examples?"
        ]

    def _generate_general_content(self, query: str, context: Dict[str, str]) -> Dict[str, Any]:
        """Generate content for general queries."""
        return {
            "explanation": "Clear explanation of the concept",
            "code": "# General example\ndef example():\n    pass",
            "considerations": "Important points to consider",
            "tip": "Helpful tip for implementation"
        }

    def _generate_general_examples(self, query: str) -> List[str]:
        """Generate general code examples."""
        return [
            "# Basic example\ndef basic_example():\n    pass",
            "# Advanced usage\nclass AdvancedExample:\n    pass"
        ]

    def _find_general_references(self, query: str) -> List[str]:
        """Find general references for the query."""
        return [
            "General Documentation",
            "Best Practices Guide",
            "Related Examples"
        ]