"""Dinesh Assistant - Personal Project Chatbot.

This module implements an advanced chatbot assistant to provide natural,
contextual responses about the project, features, and development assistance.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union

from .training.core_responses import GREETING_RESPONSE
from .training.topic_manager import TopicManager


@dataclass
class Response:
    """Chatbot response with metadata."""

    text: str
    confidence: float
    context: Dict[str, Any]
    references: List[str]
    followup_questions: Optional[List[str]] = None
    code_examples: Optional[List[str]] = None


class DineshAssistant:
    """Personal chatbot assistant for development and project help."""

    def __init__(self):
        """Initialize the chatbot with advanced capabilities."""
        self.name = "Dinesh Assistant"
        self.topic_manager = TopicManager()
        self._context: Dict[str, Any] = {
            "conversation_history": [],
            "error_context": {},
            "domain_context": {},
            "user_preferences": {},
        }
        self._initialize_greetings()
        self._initialize_error_handlers()

    def _initialize_greetings(self) -> None:
        """Initialize enhanced greeting responses."""
        self.greeting_text = (
            "Hello! 👋 I'm your AI assistant. Let me help you with:\n\n"
            "1. 🚀 Technical Implementation\n"
            "   • Python development and best practices\n"
            "   • FastAPI and web services\n"
            "   • Testing and quality assurance\n\n"
            "2. � Project Features\n"
            "   • GitHub integration and CI/CD\n"
            "   • MCP server deployment\n"
            "   • Hybrid architecture\n\n"
            "3. 🤖 AI Integration\n"
            "   • Context management\n"
            "   • Enhanced responses\n"
            "   • Intelligent assistance\n\n"
            "4. �️ Development Support\n"
            "   • Error troubleshooting\n"
            "   • Performance optimization\n"
            "   • Security best practices\n\n"
            "How can I assist you today? Feel free to ask in your own words! 😊"
        )

    def _initialize_error_handlers(self) -> None:
        """Initialize error handling patterns and responses."""
        self.error_patterns = {
            "runtime": {
                "patterns": ["RuntimeError", "Exception", "Error occurred"],
                "handler": self._handle_runtime_error,
            },
            "import": {
                "patterns": ["ImportError", "ModuleNotFoundError", "No module named"],
                "handler": self._handle_import_error,
            },
            "syntax": {
                "patterns": ["SyntaxError", "IndentationError", "Invalid syntax"],
                "handler": self._handle_syntax_error,
            },
            "type": {
                "patterns": ["TypeError", "AttributeError", "Cannot access"],
                "handler": self._handle_type_error,
            },
            "value": {
                "patterns": ["ValueError", "KeyError", "IndexError"],
                "handler": self._handle_value_error,
            },
        }

    def greet(self) -> str:
        """Generate a greeting message."""
        return self.greeting_text

    def _extract_topics(self, query: str) -> List[str]:
        """Extract and prioritize topics from the query."""
        topics = set()

        topic_patterns = {
            "python": {
                "primary": ["python", "code", "programming", "script"],
                "secondary": ["development", "type hints", "async", "test"],
                "layman": [
                    "write a program",
                    "create something",
                    "build",
                    "make",
                    "fix code",
                ],
            },
            "mcp": {
                "primary": ["mcp", "model context protocol", "smart server"],
                "secondary": ["server", "integration", "context", "connect"],
                "layman": ["ai connection", "smart system", "brain", "intelligence"],
            },
            "identity": {
                "primary": ["powered by", "who are you", "what are you", "your name"],
                "secondary": ["capabilities", "features", "can you", "help me"],
                "layman": [
                    "what can you do",
                    "how do you work",
                    "tell me about yourself",
                ],
            },
            "architecture": {
                "primary": ["architecture", "structure", "design", "system"],
                "secondary": ["organization", "pattern", "flow", "layout"],
                "layman": ["how does it work", "explain the system", "show me around"],
            },
            "web": {
                "primary": ["web", "api", "endpoint", "http", "fastapi"],
                "secondary": ["server", "route", "request", "response"],
                "layman": ["website", "webpage", "online", "internet", "web service"],
            },
            "deployment": {
                "primary": ["deploy", "install", "setup", "configuration"],
                "secondary": ["launch", "start", "run", "execute"],
                "layman": ["get it running", "make it work", "start the system"],
            },
            "error": {
                "primary": ["error", "bug", "issue", "problem", "crash"],
                "secondary": ["not working", "fails", "wrong", "incorrect"],
                "layman": [
                    "broken",
                    "doesn't work",
                    "help me fix",
                    "something's wrong",
                ],
            },
            "documentation": {
                "primary": ["docs", "documentation", "guide", "tutorial"],
                "secondary": ["example", "explanation", "reference"],
                "layman": ["show me how", "teach me", "learn about", "understand"],
            },
        }

        query_lower = query.lower()

        for topic, patterns in topic_patterns.items():
            if any(kw in query_lower for kw in patterns["primary"]):
                topics.add(topic)
            elif any(kw in query_lower for kw in patterns["secondary"]):
                topics.add(topic)

        return list(topics)

    async def _handle_error_query(self, query: str) -> Response:
        """Handle queries related to errors and issues."""
        for pattern_type, info in self.error_patterns.items():
            if any(p in query.lower() for p in info["patterns"]):
                response_text = info["handler"](query)
                return Response(
                    text=response_text,
                    confidence=0.9,
                    context={"type": "error", "error_type": pattern_type},
                    references=["Error Handling Guide"],
                )

        # Generic error handling response
        return Response(
            text=(
                "I'll help you troubleshoot this issue. Could you please:\n"
                "1. Share the exact error message\n"
                "2. Describe what you were trying to do\n"
                "3. Show me the relevant code section"
            ),
            confidence=0.7,
            context={"type": "error", "stage": "gathering_info"},
            references=["Troubleshooting Guide"],
        )

    async def _handle_domain_query(self, query: str, domain: str) -> Response:
        """Handle domain-specific queries."""
        topic_response = self.topic_manager.get_response(query)
        return Response(
            text=topic_response.text,
            confidence=topic_response.confidence,
            context={"type": "domain", "domain": domain},
            references=topic_response.references,
            followup_questions=getattr(topic_response, "followup_questions", None),
            code_examples=getattr(topic_response, "code_examples", None),
        )

    def _is_capability_query(self, query: str) -> bool:
        """Check if the query is about the assistant's capabilities."""
        capability_keywords = [
            "can you",
            "what can",
            "help me",
            "your capabilities",
            "what do you do",
            "how do you",
            "abilities",
        ]
        return any(keyword in query.lower() for keyword in capability_keywords)

    async def _handle_capability_query(self, query: str) -> Response:
        """Handle queries about the assistant's capabilities."""
        return Response(
            text=(
                "I can help you with:\n"
                "1. Python programming questions and issues\n"
                "2. GitHub-related tasks and queries\n"
                "3. CI/CD pipeline setup and troubleshooting\n"
                "4. Model Context Protocol (MCP) implementation\n"
                "5. General programming assistance and error analysis\n\n"
                "What would you like to know more about?"
            ),
            confidence=1.0,
            context={"type": "capabilities"},
            references=[],
            followup_questions=[
                "Tell me about Python features",
                "How does MCP work?",
                "Explain the project structure",
            ],
        )

    async def respond(self, query: str) -> Response:
        """Generate a context-aware response to the user's query."""
        try:
            # Initial query analysis
            query = query.strip()
            topics = self._extract_topics(query)
            domain = self._detect_technical_domain(query)
            needs_ai = self._requires_openai(query)
            network_ok = self._check_network()

            # Response selection strategy:
            # 1. If network is good and query needs AI, use OpenAI first
            # 2. If network is poor or query is simple, use local knowledge
            # 3. For mixed cases, combine both with confidence scoring

            if needs_ai:
                if network_ok:
                    # Try OpenAI first for best response quality
                    try:
                        openai_response = await self._get_openai_response(
                            query, topics, domain
                        )
                        if openai_response.confidence > 0.8:
                            return openai_response
                    except Exception as e:
                        # Log error but continue with local knowledge
                        print(f"OpenAI error: {e}")
                else:
                    return Response(
                        text=(
                            "I notice your question might benefit from AI-powered analysis, but I'm currently in offline mode. "
                            "I'll help you with my local knowledge base instead.\n\n"
                            "For best results with complex queries, please try again when network connectivity is better."
                        ),
                        confidence=0.8,
                        context={"type": "network_error", "fallback": "local"},
                        references=[],
                    )

            query = query.strip()
            topics = self._extract_topics(query)

            # Handle identity questions first
            if "identity" in topics:
                response = Response(
                    text=(
                        "I'm your project-specific AI assistant, focused on helping you understand "
                        "and work with this codebase effectively. I can help with:\n\n"
                        "1. Python development best practices\n"
                        "2. Project architecture and components\n"
                        "3. Error analysis and troubleshooting\n"
                        "4. Documentation and knowledge sharing\n\n"
                        "How can I assist you with the project today?"
                    ),
                    confidence=1.0,
                    context={"type": "identity"},
                    references=["Project Documentation"],
                    followup_questions=[
                        "Show me Python best practices",
                        "Explain the project structure",
                        "Help with error handling",
                    ],
                )
                self._update_context(query, response)
                return response

            # Handle MCP + Python combination
            if set(["mcp", "python"]).issubset(set(topics)):
                return await self._handle_mcp_python_query(query)

            # Check for error-related queries
            if any(
                error in query.lower()
                for error in ["error", "bug", "issue", "problem", "fix"]
            ):
                return await self._handle_error_query(query)

            # Enhanced greeting detection
            greetings = {
                "hi",
                "hello",
                "hey",
                "greetings",
                "good morning",
                "good afternoon",
                "good evening",
                "hi there",
                "hello there",
                "howdy",
            }

            if any(greeting in query.lower() for greeting in greetings):
                response = Response(
                    text=self.greeting_text,
                    confidence=1.0,
                    context={"type": "greeting"},
                    references=[],
                    followup_questions=[
                        "Tell me about Python features",
                        "How does MCP work?",
                        "Show me the project structure",
                    ],
                )
                self._update_context(query, response)
                return response

            # Process domain-specific queries
            domain = self._detect_technical_domain(query)
            if domain != "general":
                return await self._handle_domain_query(query, domain)

            # Process capability queries
            if self._is_capability_query(query):
                return await self._handle_capability_query(query)

            # Default to topic manager response
            topic_response = self.topic_manager.get_response(query)
            response = Response(
                text=topic_response.text,
                confidence=topic_response.confidence,
                context={"type": "general", "category": topic_response.category},
                references=topic_response.references,
                followup_questions=getattr(topic_response, "followup_questions", None),
                code_examples=getattr(topic_response, "code_examples", None),
            )
            self._update_context(query, response)
            return response

        except Exception as e:
            return Response(
                text=(
                    f"I apologize, but I encountered an error: {str(e)}. "
                    "Please try rephrasing your query."
                ),
                confidence=0.5,
                context={"type": "error", "error": str(e)},
                references=[],
            )

    def _update_context(self, query: str, response: Response) -> None:
        """Update conversation context with enhanced tracking."""
        # Update basic context
        self._context["last_query"] = query
        self._context["last_response"] = response
        self._context["interaction_count"] = (
            self._context.get("interaction_count", 0) + 1
        )

        # Track conversation history with enhanced metadata
        self._context["conversation_history"].append(
            {
                "query": query,
                "response": {
                    "text": response.text,
                    "confidence": response.confidence,
                    "category": response.context.get("type", "general"),
                    "references": response.references,
                    "followup_questions": getattr(response, "followup_questions", []),
                    "code_examples": getattr(response, "code_examples", []),
                },
                "timestamp": self._get_timestamp(),
            }
        )

        # Clean up old history (keep last 10 interactions)
        if len(self._context["conversation_history"]) > 10:
            self._context["conversation_history"] = self._context[
                "conversation_history"
            ][-10:]

    def _handle_runtime_error(self, error: str) -> str:
        """Handle runtime errors with detailed explanation."""
        return (
            "🔍 I noticed a runtime error. Let me help you fix that:\n\n"
            f"Error: {error}\n\n"
            "Common causes:\n"
            "1. Invalid operations\n"
            "2. Resource unavailability\n"
            "3. State inconsistencies\n\n"
            "Suggested solutions:\n"
            "1. Check input validation\n"
            "2. Verify resource availability\n"
            "3. Add proper error handling\n\n"
            "Would you like me to show you an example of proper error handling?"
        )

    def _handle_import_error(self, error: str) -> str:
        """Handle import errors with installation guidance."""
        return (
            "📦 Looks like we have an import issue. Let's resolve it:\n\n"
            f"Error: {error}\n\n"
            "This usually means:\n"
            "1. A package is not installed\n"
            "2. Python path is incorrect\n"
            "3. Virtual environment is not activated\n\n"
            "Quick fix steps:\n"
            "1. Check requirements.txt\n"
            "2. Verify virtual environment\n"
            "3. Install missing packages\n\n"
            "Would you like me to help you install the required packages?"
        )

    def _handle_syntax_error(self, error: str) -> str:
        """Handle syntax errors with code correction."""
        return (
            "🔧 I found a syntax error. Let me help you fix it:\n\n"
            f"Error: {error}\n\n"
            "Common issues:\n"
            "1. Missing parentheses/brackets\n"
            "2. Incorrect indentation\n"
            "3. Invalid Python syntax\n\n"
            "Best practices:\n"
            "1. Use a code formatter (black)\n"
            "2. Enable syntax highlighting\n"
            "3. Check indentation carefully\n\n"
            "Would you like me to show you the correct syntax?"
        )

    def _handle_type_error(self, error: str) -> str:
        """Handle type errors with type hints guidance."""
        return (
            "📝 I noticed a type error. Let's fix it properly:\n\n"
            f"Error: {error}\n\n"
            "This typically means:\n"
            "1. Incompatible types used\n"
            "2. Missing type conversions\n"
            "3. Incorrect method usage\n\n"
            "Modern Python solutions:\n"
            "1. Use type hints\n"
            "2. Add runtime type checking\n"
            "3. Implement proper validation\n\n"
            "Would you like to see how to use type hints correctly?"
        )

    def _handle_value_error(self, error: str) -> str:
        """Handle value errors with validation guidance."""
        return (
            "⚠️ I found a value error. Let's handle it properly:\n\n"
            f"Error: {error}\n\n"
            "Common causes:\n"
            "1. Invalid input values\n"
            "2. Incorrect data format\n"
            "3. Missing validation\n\n"
            "Best practices:\n"
            "1. Add input validation\n"
            "2. Use data validation libraries\n"
            "3. Implement error boundaries\n\n"
            "Would you like to see examples of proper validation?"
        )

    async def _handle_mcp_python_query(self, query: str) -> Response:
        """Handle combined MCP and Python-related queries."""
        return Response(
            text=(
                "Let me explain how this project leverages both Python and MCP server capabilities:\n\n"
                "1. Modern Python Development 🐍\n"
                "   • Type hints for enhanced code safety\n"
                "   • Async/await for efficient async operations\n"
                "   • Latest Python 3.8+ features for better performance\n"
                "   • Comprehensive testing with pytest\n\n"
                "2. MCP Server Integration 🔄\n"
                "   • FastAPI-based implementation for high performance\n"
                "   • Context-aware response handling\n"
                "   • Efficient state management\n"
                "   • Domain-specific knowledge integration\n\n"
                "3. Development Workflow ⚙️\n"
                "   • Code quality tools: mypy, black, isort\n"
                "   • Automated testing and CI/CD\n"
                "   • Clear documentation standards\n"
                "   • Modular project structure\n\n"
                "4. Key Features 🎯\n"
                "   • Intelligent response generation\n"
                "   • Enhanced context management\n"
                "   • Multi-domain knowledge support\n"
                "   • Error handling and recovery\n\n"
                "Would you like to explore any specific aspect in more detail?"
            ),
            confidence=0.95,
            context={
                "type": "technical",
                "domains": ["python", "mcp"],
                "focus": "implementation",
            },
            references=[
                "src/main.py",
                "src/chatbot.py",
                "src/training/",
                "Project Documentation",
            ],
            followup_questions=[
                "How do type hints work?",
                "Explain the MCP server architecture",
                "Show me testing examples",
            ],
        )

    def _detect_technical_domain(self, query: str) -> str:
        """Detect the technical domain of the query with enhanced understanding."""
        domain_patterns = {
            "python": {
                "keywords": ["python", "code", "function", "class", "method"],
                "phrases": ["write a program", "create a script", "python code"],
                "concepts": ["object oriented", "inheritance", "variables"],
                "layman": ["make it work", "write something", "program logic"],
            },
            "web": {
                "keywords": ["api", "endpoint", "http", "fastapi", "route"],
                "phrases": ["web service", "api endpoint", "http request"],
                "concepts": ["rest", "http methods", "api design"],
                "layman": ["website", "web page", "internet", "online"],
            },
            "github": {
                "keywords": ["git", "github", "commit", "push", "pull"],
                "phrases": ["version control", "source code", "repository"],
                "concepts": ["branching", "merging", "collaboration"],
                "layman": ["save changes", "track code", "backup code"],
            },
            "ai": {
                "keywords": ["model", "ml", "train", "predict", "ai"],
                "phrases": ["machine learning", "artificial intelligence"],
                "concepts": ["neural network", "deep learning", "training"],
                "layman": ["smart system", "intelligence", "learning"],
            },
            "architecture": {
                "keywords": ["design", "structure", "pattern", "component"],
                "phrases": ["system design", "project structure"],
                "concepts": ["modularity", "scalability", "patterns"],
                "layman": ["how it works", "system layout", "organization"],
            },
            "testing": {
                "keywords": ["test", "pytest", "coverage", "assert"],
                "phrases": ["unit test", "integration test"],
                "concepts": ["test cases", "mocking", "fixtures"],
                "layman": ["check if it works", "verify", "validate"],
            },
            "deployment": {
                "keywords": ["deploy", "server", "cloud", "container"],
                "phrases": ["production environment", "deployment process"],
                "concepts": ["continuous integration", "automation"],
                "layman": ["put online", "make live", "launch"],
            },
        }

        def calculate_domain_score(query_lower: str, patterns: dict) -> float:
            score = 0
            # Direct keyword matches have highest weight
            if any(kw in query_lower for kw in patterns["keywords"]):
                score += 3
            # Phrase matches have medium weight
            if any(phrase in query_lower for phrase in patterns["phrases"]):
                score += 2
            # Concept and layman term matches have lower weight
            if any(concept in query_lower for concept in patterns["concepts"]):
                score += 1
            if any(term in query_lower for term in patterns["layman"]):
                score += 0.5
            return score

        query_lower = query.lower()
        scores = {
            domain: calculate_domain_score(query_lower, patterns)
            for domain, patterns in domain_patterns.items()
        }

        # Get domain with highest score
        max_score = max(scores.values())
        if max_score > 0:
            return max(scores.items(), key=lambda x: x[1])[0]

        return "general"

    def _get_timestamp(self) -> str:
        """Get current timestamp for context tracking."""
        from datetime import datetime

        return datetime.now().isoformat()

    def _requires_openai(self, query: str) -> bool:
        """Check if the query requires OpenAI capabilities and if it should be prioritized."""
        # Direct AI keywords that strongly suggest OpenAI usage
        ai_keywords = [
            "generate",
            "create",
            "write",
            "analyze",
            "summarize",
            "explain in detail",
            "compare",
            "improve",
            "suggest",
            "how would you",
            "what do you think",
            "complex",
            "advanced",
            "ai",
            "intelligence",
        ]

        # Contextual keywords that might benefit from AI
        contextual_keywords = [
            "why",
            "how come",
            "what if",
            "explain",
            "understand",
            "help me with",
            "show me how",
            "can you help",
            "best way to",
            "alternative",
            "better way",
            "optimize",
            "improve",
        ]

        # Complex question indicators
        complex_patterns = [
            "difference between",
            "compare and contrast",
            "pros and cons",
            "advantages and disadvantages",
            "step by step",
            "in depth",
            "detailed explanation",
        ]

        # Check network conditions and query complexity
        query_lower = query.lower()

        # Direct AI keywords take highest priority
        if any(keyword in query_lower for keyword in ai_keywords):
            return True

        # If network is good, use AI for complex or contextual queries
        if self._check_network():
            # Complex patterns take second priority
            if any(pattern in query_lower for pattern in complex_patterns):
                return True

            # Contextual keywords take third priority
            if any(keyword in query_lower for keyword in contextual_keywords):
                # Only use OpenAI for longer, more complex queries with these keywords
                words = query_lower.split()
                return (
                    len(words) > 3
                )  # Only use OpenAI for more complex contextual queries

        return False

    def _check_network(self) -> bool:
        """Check if network connectivity is available and fast enough for AI operations."""
        import socket
        import statistics
        import time

        def measure_latency() -> float:
            try:
                start = time.time()
                socket.create_connection(("api.openai.com", 443), timeout=1)
                return time.time() - start
            except (OSError, socket.timeout):
                return float("inf")

        # Test multiple times to get a stable measurement
        latencies = [measure_latency() for _ in range(3)]

        # Remove infinite values from failed attempts
        valid_latencies = [lat for lat in latencies if lat != float("inf")]

        # If all attempts failed, network is down
        if not valid_latencies:
            return False

        # Calculate median latency
        median_latency = statistics.median(valid_latencies)

        # Consider network good if median latency is under 300ms
        return median_latency < 0.3  # 300ms threshold

    async def _get_openai_response(
        self, query: str, topics: List[str], domain: str
    ) -> Response:
        """Get an enhanced response using OpenAI capabilities."""
        try:
            # Prepare context-aware prompt
            prompt = self._build_openai_prompt(query, topics, domain)

            # Get response from OpenAI
            response_text = await self._call_openai_api(prompt)

            # Post-process the response
            processed_response = self._process_openai_response(response_text, query)

            # Generate relevant code examples if needed
            code_examples = (
                self._generate_code_examples(query, domain)
                if "code" in topics
                else None
            )

            # Find relevant documentation references
            references = self._find_relevant_docs(query, domain)

            # Generate follow-up questions
            followups = self._generate_followup_questions(query, response_text)

            return Response(
                text=processed_response,
                confidence=0.95,  # OpenAI responses get high confidence
                context={
                    "type": "ai_enhanced",
                    "domain": domain,
                    "topics": topics,
                    "source": "openai",
                },
                references=references,
                followup_questions=followups,
                code_examples=code_examples,
            )
        except Exception as e:
            # Log error and return None to fallback to local knowledge
            print(f"OpenAI response generation error: {e}")
            raise

    def _build_openai_prompt(self, query: str, topics: List[str], domain: str) -> str:
        """Build a context-aware prompt for OpenAI."""
        # Start with the base context
        prompt = (
            "You are a technical assistant helping with a Python project. "
            "Your responses should be clear, accurate, and helpful.\n\n"
        )

        # Add domain-specific context
        domain_contexts = {
            "python": "Focus on Python best practices, modern features, and clean code.",
            "web": "Consider FastAPI, API design, and web service architecture.",
            "github": "Include Git workflow, collaboration, and version control aspects.",
            "ai": "Focus on AI/ML implementation and integration details.",
            "architecture": "Consider system design, patterns, and architectural principles.",
            "testing": "Emphasize testing practices, coverage, and quality assurance.",
            "deployment": "Focus on deployment, CI/CD, and operational aspects.",
        }

        if domain in domain_contexts:
            prompt += f"Context: {domain_contexts[domain]}\n\n"

        # Add conversation history context if relevant
        if self._context.get("conversation_history"):
            last_interaction = self._context["conversation_history"][-1]
            prompt += f"Previous topic: {last_interaction['response']['category']}\n\n"

        # Add the actual query
        prompt += f"User question: {query}\n\n"

        # Add specific instructions
        prompt += (
            "Provide a detailed, well-structured response. "
            "Include relevant examples and best practices. "
            "If discussing code, provide clear, idiomatic examples."
        )

        return prompt

    async def _call_openai_api(self, prompt: str) -> str:
        """Call OpenAI API with proper error handling and retries."""
        import asyncio

        from openai import AsyncOpenAI

        # Create async OpenAI client
        client = AsyncOpenAI()

        async def try_openai_call(retries: int = 3) -> str:
            for attempt in range(retries):
                try:
                    response = await client.chat.completions.create(
                        model="gpt-4",  # Use the most capable model
                        messages=[
                            {
                                "role": "system",
                                "content": "You are a technical assistant specialized in Python development.",
                            },
                            {"role": "user", "content": prompt},
                        ],
                        temperature=0.7,  # Balance between creativity and accuracy
                        max_tokens=1000,  # Adjust based on expected response length
                        presence_penalty=0.6,  # Encourage diverse responses
                        frequency_penalty=0.2,  # Reduce repetition
                    )
                    return response.choices[0].message.content
                except Exception:
                    if attempt == retries - 1:
                        raise
                    await asyncio.sleep(1 * (attempt + 1))  # Exponential backoff
            raise RuntimeError("Failed to get OpenAI response after multiple retries")

        return await try_openai_call()

    def _process_openai_response(self, response_text: str, original_query: str) -> str:
        """Process and enhance the OpenAI response."""
        # Clean up and format the response
        lines = response_text.split("\n")
        processed_lines = []

        code_block = False
        for line in lines:
            # Handle code blocks
            if "```" in line:
                code_block = not code_block
                processed_lines.append(line)
                continue

            # Add emoji indicators for different content types
            if not code_block:
                if line.strip().endswith(":"):
                    line = "🔍 " + line  # Sections
                elif "Example" in line:
                    line = "💡 " + line  # Examples
                elif "Note:" in line:
                    line = "📝 " + line  # Notes
                elif any(
                    word in line.lower() for word in ["warning", "caution", "important"]
                ):
                    line = "⚠️ " + line  # Warnings

            processed_lines.append(line)

        return "\n".join(processed_lines)

    def _generate_code_examples(self, query: str, domain: str) -> List[str]:
        """Generate relevant code examples based on the query and domain."""
        examples = []

        domain_examples = {
            "python": [
                "# Modern Python example\nasync def process_data(items: List[Dict]):\n    results = await asyncio.gather(*[process_item(item) for item in items])\n    return [result for result in results if result]",
                "# Type hints example\nfrom typing import Optional\n\ndef get_user(user_id: int) -> Optional[Dict]:\n    user = db.query(user_id)\n    return user if user else None",
            ],
            "web": [
                "# FastAPI endpoint example\n@app.get('/api/v1/items/{item_id}')\nasync def get_item(item_id: int) -> Dict:\n    return await items_service.get_item(item_id)",
                "# Error handling example\nfrom fastapi import HTTPException\n\ndef validate_item(item: Item) -> None:\n    if not item.name:\n        raise HTTPException(status_code=400, detail='Name is required')",
            ],
        }

        if domain in domain_examples:
            examples.extend(domain_examples[domain])

        return examples

    def _find_relevant_docs(self, query: str, domain: str) -> List[str]:
        """Find relevant documentation references."""
        base_docs = ["Project Documentation", "README.md"]

        domain_docs = {
            "python": ["Python Best Practices Guide", "Type Hints Documentation"],
            "web": ["FastAPI Documentation", "API Design Guide"],
            "github": ["Git Workflow Guide", "GitHub Actions Setup"],
            "architecture": ["System Architecture Doc", "Design Patterns Guide"],
        }

        refs = base_docs.copy()
        if domain in domain_docs:
            refs.extend(domain_docs[domain])

        return refs

    def _generate_followup_questions(self, query: str, response: str) -> List[str]:
        """Generate contextual follow-up questions."""
        followups = [
            "Would you like to see more detailed examples?",
            "Should I explain any part in more detail?",
            "Would you like to learn about best practices for this?",
        ]

        # Add domain-specific follow-ups
        domain_followups = {
            "python": [
                "How do I implement this with async/await?",
                "What are the type hints for this case?",
            ],
            "web": [
                "How do I handle errors in this API?",
                "What about request validation?",
            ],
            "testing": ["How do I write tests for this?", "What about edge cases?"],
            "deployment": [
                "How do I deploy this to production?",
                "What about monitoring?",
            ],
        }

        domain = self._detect_technical_domain(query)
        if domain in domain_followups:
            followups.extend(domain_followups[domain])

        return followups[:3]  # Return top 3 most relevant
