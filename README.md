# ConfigMaster Project with Dinesh Assistant

## Overview

ConfigMaster is an enterprise-grade configuration management system featuring Dinesh Assistant, an advanced AI-powered chatbot that provides interactive help and documentation. This document provides a comprehensive guide to the project, its chatbot capabilities, and technical implementation.

## Table of Contents

- [Quick Links](#quick-links)
- [New Documentation](#new-documentation)
  - [Chatbot Documentation](docs/CHATBOT.md) - Detailed guide for Dinesh Assistant
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Development](#development)

## System Architecture

```
┌─────────────────────────────────────────┐
│            Dinesh Assistant             │
├─────────────────┬───────────────────────┤
│   Core Engine   │    Interface Layer    │
├─────────────────┼───────────────────────┤
│  NLP Pipeline   │     CLI Interface     │
│  Knowledge Base │     Web Interface     │
│  Response Gen   │     REST API          │
├─────────────────┴───────────────────────┤
│         FastAPI Backend Server          │
└─────────────────────────────────────────┘
```

## Features

### Core Functionality
- **Natural Language Processing**: Advanced text understanding and response generation
- **Knowledge Base**: Extensible information storage and retrieval
- **Context Management**: Maintains conversation context and history
- **Asynchronous Processing**: Non-blocking operations for better performance

### User Interfaces
1. **Command Line Interface (CLI)**
   - Interactive chat mode
   - One-shot query mode
   - Rich text output
   - Command history

2. **Web Interface**
   - Modern responsive design
   - Real-time chat updates
   - Message history display
   - Reference links support

### Backend System
- **FastAPI Server**
  - RESTful API endpoints
  - WebSocket support
  - Async request handling
  - API documentation
- **Data Management**
  - In-memory cache
  - Session handling
  - State persistence

## Project Structure

```
.
├── src/
│   ├── main.py              # CLI and core functionality
│   └── config/
│       ├── i18n.py          # Internationalization
│       ├── settings.py      # Configuration handling
│       ├── templates.py     # Template management
│       └── validation.py    # Config validation
├── tests/                   # Test files
├── .github/                 # GitHub workflows
├── pyproject.toml          # Project configuration
└── # ConfigMaster: Advanced Python Configuration Management System

## Project Overview & System Architecture

ConfigMaster is an enterprise-grade configuration management system built with a microservices-oriented architecture. The system is designed to handle complex configuration scenarios while maintaining high reliability and scalability.

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     ConfigMaster Core                       │
├───────────────┬───────────────┬────────────┬───────────────┤
│ Configuration │    Template   │    i18n    │  Validation   │
│   Manager     │    Engine     │   System   │    Engine     │
├───────────────┴───────────────┴────────────┴───────────────┤
│                    Integration Layer                        │
├───────────────┬───────────────┬────────────┬───────────────┤
│  MCP Server   │     Azure     │   GitHub   │    Cloud      │
│  Protocol     │   Services    │     API    │   Storage     │
└───────────────┴───────────────┴────────────┴───────────────┘
         ▲              ▲             ▲            ▲
         │              │             │            │
    ┌────┴──────┬──────┴─────┬──────┴─────┬──────┴─────┐
    │   Web     │   Mobile   │  Desktop   │   CLI      │
    │   Apps    │   Apps     │   Apps     │  Tools     │
    └───────────┴───────────┴────────────┴────────────┘
```

### Core Objectives

ConfigMaster addresses critical enterprise needs through:

1. **Configuration Reliability**
   - Prevent configuration errors through strong type validation
   - Ensure configuration consistency across environments
   - Protect against invalid or malformed settings

2. **Global Application Support**
   - Enable seamless internationalization
   - Support multiple languages and locales
   - Maintain consistent user experience across regions

3. **Enterprise Scalability**
   - Handle complex configuration hierarchies
   - Support multiple environments (dev, staging, prod)
   - Enable configuration versioning and rollbacks

4. **Developer Productivity**
   - Reduce configuration-related bugs
   - Streamline development workflow
   - Provide clear error messages and validation

5. **System Integration**
   - Connect with MCP servers for enhanced capabilities
   - Enable cloud service integration
   - Support modern deployment patterns

ConfigMaster is a robust, enterprise-grade configuration management system built in Python that provides advanced features for handling application settings, internationalization, templating, and validation. This project demonstrates modern Python development practices and integrates with Model Context Protocol (MCP) servers for enhanced functionality.

## Technical Specifications & Feature Analysis

### 1. Configuration Management System
**Architecture Pattern**: Repository Pattern with Event Sourcing
**Data Flow**: Config Request → Validation → Processing → Storage → Response
**Performance Metrics**: <100ms response time, 99.99% availability

#### Core Components
```python
@dataclass
class ConfigSpec:
    """Configuration specification."""
    name: str
    version: str
    environment: str
    timestamp: datetime
    checksum: str
    data: Dict[str, Any]
    metadata: Dict[str, Any]

class ConfigurationManager:
    def __init__(self):
        self._cache = LRUCache(maxsize=1000)
        self._event_bus = EventBus()
        self._storage = ConfigStorage()
    
    async def get_config(self, name: str) -> ConfigSpec:
        # Implementation with caching and validation
        pass

    async def update_config(self, config: ConfigSpec) -> None:
        # Implementation with event sourcing
        pass
```

#### Advanced Features
1. **Version Control**
   ```python
   async def rollback_config(self, name: str, version: str) -> None:
       previous = await self._storage.get_version(name, version)
       await self.update_config(previous)
   ```

2. **Change Tracking**
   ```python
   def track_changes(self) -> AsyncIterator[ConfigChange]:
       async for event in self._event_bus.subscribe("config.*"):
           yield ConfigChange.from_event(event)
   ```
**Objective**: Provide a robust, type-safe configuration system that prevents runtime errors
- **Features**:
  - Strong type validation with runtime checking
  - Default value management
  - Configuration inheritance
  - Environment-specific overrides
  - JSON serialization and deserialization
  - Validation hooks and custom validators
  - Protected attributes for sensitive data

### 2. Internationalization (i18n) Framework
**Architecture Pattern**: Strategy Pattern with Resource Bundle
**Performance**: On-demand loading with LRU caching
**Storage**: Hierarchical JSON with fallback chains

#### Implementation Details
```python
from enum import Enum
from typing import Dict, Optional
from dataclasses import dataclass

class Language(Enum):
    EN = "en"
    ES = "es"
    FR = "fr"
    JA = "ja"

@dataclass
class TranslationBundle:
    """Translation resource bundle."""
    language: Language
    translations: Dict[str, str]
    fallback: Optional[Language]
    metadata: Dict[str, Any]

class I18nManager:
    def __init__(self):
        self._bundles: Dict[Language, TranslationBundle] = {}
        self._cache = TranslationCache()
        
    async def get_translation(
        self, 
        key: str, 
        language: Language,
        **params: Dict[str, Any]
    ) -> str:
        bundle = self._bundles.get(language)
        if not bundle:
            return await self._fallback_translation(key, language)
            
        template = bundle.translations.get(key)
        return template.format(**params) if template else key
        
    async def add_language(
        self,
        language: Language,
        translations: Dict[str, str],
        fallback: Optional[Language] = None
    ) -> None:
        bundle = TranslationBundle(
            language=language,
            translations=translations,
            fallback=fallback,
            metadata={"timestamp": datetime.now()}
        )
        self._bundles[language] = bundle
```

#### Features & Capabilities:
  - Support for multiple languages (EN, ES, FR, JA)
  - Language-specific message templates
  - Character encoding handling
  - Locale-aware formatting
  - Translation management
  - Fallback language support
  - Runtime language switching

### 3. Template Engine
**Objective**: Provide flexible message and content templating with proper categorization
- **Features**:
  - Template categorization (Formal, Casual, Business)
  - Tag-based template search
  - Template validation
  - Variable interpolation
  - Template inheritance
  - Category-based filtering
  - Custom template registration

### 4. Validation Framework
**Architecture Pattern**: Chain of Responsibility with Composite
**Performance**: Parallel validation for independent rules
**Extension**: Plugin-based validator registration

#### Validation System
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Any, Dict

@dataclass
class ValidationContext:
    """Validation context with metadata."""
    value: Any
    path: str
    metadata: Dict[str, Any]
    parent: Optional['ValidationContext']

class Validator(ABC):
    """Abstract base class for validators."""
    
    @abstractmethod
    async def validate(
        self,
        context: ValidationContext
    ) -> List[ValidationError]:
        """Validate the given context."""
        pass

class CompositeValidator(Validator):
    """Composite validator that runs multiple validators."""
    
    def __init__(self, validators: List[Validator]):
        self.validators = validators
        
    async def validate(
        self,
        context: ValidationContext
    ) -> List[ValidationError]:
        errors = []
        for validator in self.validators:
            errors.extend(await validator.validate(context))
        return errors

class TypeValidator(Validator):
    """Validates type constraints."""
    
    def __init__(self, expected_type: Type):
        self.expected_type = expected_type
        
    async def validate(
        self,
        context: ValidationContext
    ) -> List[ValidationError]:
        if not isinstance(context.value, self.expected_type):
            return [
                ValidationError(
                    path=context.path,
                    message=f"Expected {self.expected_type.__name__}"
                )
            ]
        return []

class RangeValidator(Validator):
    """Validates numeric ranges."""
    
    def __init__(self, min_value: float, max_value: float):
        self.min_value = min_value
        self.max_value = max_value
        
    async def validate(
        self,
        context: ValidationContext
    ) -> List[ValidationError]:
        if not self.min_value <= context.value <= self.max_value:
            return [
                ValidationError(
                    path=context.path,
                    message=f"Value must be between {self.min_value} and {self.max_value}"
                )
            ]
        return []
```

#### Validation Rules & Extensions:

```python
@dataclass
class RegexValidator(Validator):
    """Validates string patterns."""
    pattern: str
    flags: re.RegexFlag = re.UNICODE
    
    async def validate(
        self,
        context: ValidationContext
    ) -> List[ValidationError]:
        if not re.match(self.pattern, context.value, self.flags):
            return [
                ValidationError(
                    path=context.path,
                    message=f"Value must match pattern {self.pattern}"
                )
            ]
        return []

class CustomValidator(Validator):
    """Custom validation logic."""
    
    def __init__(self, func: Callable[[Any], bool], message: str):
        self.func = func
        self.message = message
        
    async def validate(
        self,
        context: ValidationContext
    ) -> List[ValidationError]:
        if not self.func(context.value):
            return [ValidationError(path=context.path, message=self.message)]
        return []

# Example Usage:
config = {
    'server': {
        'port': 8080,
        'host': 'localhost',
        'timeout': 30
    },
    'database': {
        'url': 'postgresql://localhost/db',
        'pool_size': 10
    }
}

# Create validators
port_validator = CompositeValidator([
    TypeValidator(int),
    RangeValidator(1024, 65535)
])

url_validator = CompositeValidator([
    TypeValidator(str),
    RegexValidator(r'^[a-z]+://[^/\s:]+(?::\d+)?(?:/\S*)?$')
])

# Validate configuration
async def validate_config(config: dict):
    validators = {
        'server.port': port_validator,
        'database.url': url_validator,
        'server.timeout': RangeValidator(0, 300),
        'database.pool_size': RangeValidator(1, 100)
    }
    
    errors = []
    for path, validator in validators.items():
        value = get_path(config, path)
        context = ValidationContext(value=value, path=path)
        errors.extend(await validator.validate(context))
    return errors
```

This validation framework provides:
1. **Type Safety**: Strict type checking for configuration values
2. **Range Validation**: Numeric bounds for ports, timeouts, etc.
3. **Pattern Matching**: Regex validation for URLs, paths, etc.
4. **Custom Rules**: Extensible validation through custom functions
5. **Composability**: Chain multiple validators for complex rules
6. **Async Support**: Parallel validation for better performance
7. **Plugin System**: Dynamic validator registration and loading
8. **Path-based**: Dot notation for nested configuration access
  - Type checking
  - Value range validation
  - Required field validation
  - Custom validation rules
  - Validation error reporting
  - Nested object validation
  - Cross-field validation

### 5. Template System
**Architecture Pattern**: Prototype + Builder
**Performance**: Cached template compilation
**Extension**: Custom template functions

#### Template System
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Any, Optional
import jinja2

@dataclass
class TemplateContext:
    """Template rendering context."""
    variables: Dict[str, Any]
    parent: Optional['TemplateContext'] = None
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get variable from context chain."""
        if key in self.variables:
            return self.variables[key]
        if self.parent:
            return self.parent.get(key, default)
        return default

class TemplateEngine(ABC):
    """Abstract template engine interface."""
    
    @abstractmethod
    def render(
        self, 
        template: str,
        context: TemplateContext
    ) -> str:
        """Render template with context."""
        pass

class JinjaEngine(TemplateEngine):
    """Jinja2-based template engine."""
    
    def __init__(self):
        self.env = jinja2.Environment(
            loader=jinja2.BaseLoader(),
            autoescape=True,
            trim_blocks=True,
            lstrip_blocks=True
        )
        self._cache = {}
        
    def render(
        self,
        template: str,
        context: TemplateContext
    ) -> str:
        """Render template with cached compilation."""
        if template not in self._cache:
            self._cache[template] = self.env.from_string(template)
        return self._cache[template].render(**context.variables)

class ConfigTemplate:
    """Configuration template with inheritance."""
    
    def __init__(
        self,
        content: str,
        engine: TemplateEngine,
        parent: Optional['ConfigTemplate'] = None
    ):
        self.content = content
        self.engine = engine
        self.parent = parent
        
    def render(
        self,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Render template with parent chain."""
        if self.parent:
            base = self.parent.render(context)
            context = {**base, **context}
            
        rendered = self.engine.render(
            self.content,
            TemplateContext(context)
        )
        return yaml.safe_load(rendered)
```

#### Features & Capabilities:
1. **Template Inheritance**: Chain multiple templates
2. **Context Chaining**: Nested variable resolution
3. **Caching**: Pre-compiled templates for performance
4. **Custom Functions**: Extensible template operations
5. **Safe Rendering**: Automatic escaping and validation
6. **YAML Support**: Configuration file generation
7. **Flexible Engine**: Pluggable template engines
8. **Variable Resolution**: Hierarchical lookup system

### 6. Asynchronous Operations
**Architecture Pattern**: Event-driven with Task Pool
**Performance**: Non-blocking I/O with minimal overhead
**Extension**: Custom task schedulers and executors

#### Async Framework
```python
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List
from dataclasses import dataclass
import asyncio

T = TypeVar('T')

@dataclass
class AsyncResult(Generic[T]):
    """Result of an async operation."""
    value: Optional[T]
    error: Optional[Exception]
    duration: float
    metadata: Dict[str, Any]

class AsyncOperation(ABC, Generic[T]):
    """Base class for async operations."""
    
    def __init__(self, timeout: Optional[float] = None):
        self.timeout = timeout
        self._start_time: Optional[float] = None
        
    @abstractmethod
    async def execute(self) -> T:
        """Execute the async operation."""
        pass
        
    async def run(self) -> AsyncResult[T]:
        """Run operation with timeout and metrics."""
        self._start_time = asyncio.get_event_loop().time()
        try:
            async with asyncio.timeout(self.timeout):
                value = await self.execute()
                return AsyncResult(
                    value=value,
                    error=None,
                    duration=self._get_duration(),
                    metadata=self._get_metadata()
                )
        except Exception as e:
            return AsyncResult(
                value=None,
                error=e,
                duration=self._get_duration(),
                metadata=self._get_metadata()
            )
            
    def _get_duration(self) -> float:
        """Calculate operation duration."""
        if self._start_time is None:
            return 0.0
        return asyncio.get_event_loop().time() - self._start_time
        
    def _get_metadata(self) -> Dict[str, Any]:
        """Get operation metadata."""
        return {
            "timeout": self.timeout,
            "start_time": self._start_time
        }

class AsyncOperationPool:
    """Pool for managing concurrent operations."""
    
    def __init__(
        self, 
        max_concurrency: int = 10,
        default_timeout: Optional[float] = None
    ):
        self._semaphore = asyncio.Semaphore(max_concurrency)
        self.default_timeout = default_timeout
        self._active: List[AsyncOperation] = []
        
    async def submit(
        self,
        operation: AsyncOperation[T]
    ) -> AsyncResult[T]:
        """Submit operation to pool."""
        async with self._semaphore:
            self._active.append(operation)
            try:
                return await operation.run()
            finally:
                self._active.remove(operation)
                
    async def map(
        self,
        operations: List[AsyncOperation[T]]
    ) -> List[AsyncResult[T]]:
        """Run multiple operations concurrently."""
        tasks = [
            self.submit(op)
            for op in operations
        ]
        return await asyncio.gather(*tasks)
```

#### Features & Capabilities:
1. **Operation Management**
   - Timeout handling
   - Error recovery
   - Performance metrics
   - Operation cancellation

2. **Concurrency Control**
   - Resource limits
   - Task scheduling
   - Load balancing
   - Priority queues

3. **Error Handling**
   - Graceful timeout
   - Operation retry
   - Error aggregation
   - Recovery strategies

4. **Performance**
   - Non-blocking I/O
   - Resource pooling
   - Task batching 
   - Load optimization

### 7. Testing Framework
  - Async configuration loading
  - Concurrent template processing
  - Non-blocking I/O operations
  - Timeout handling
  - Error recovery
  - Performance optimization
  - Resource cleanup

### 6. Testing Framework
**Objective**: Maintain code quality and prevent regressions
- **Features**:
  - Comprehensive test suite
  - Integration tests
  - Performance tests
  - Memory usage monitoring
  - Coverage reporting
  - Edge case testing
  - Concurrent operation testing

### 7. Testing Framework
**Architecture Pattern**: Fixture Factory with Test Suites
**Coverage Goal**: 95% code coverage with mutation testing
**Extension**: Custom test runners and reporting

#### Test Framework
```python
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Type
import pytest
import hypothesis
from hypothesis import strategies as st

@dataclass
class TestCase:
    """Test case specification."""
    name: str
    inputs: Dict[str, Any]
    expected: Any
    raises: Optional[Type[Exception]] = None
    timeout: Optional[float] = None
    tags: List[str] = field(default_factory=list)

class TestSuite:
    """Collection of related test cases."""
    
    def __init__(
        self,
        name: str,
        description: str,
        fixtures: List[str]
    ):
        self.name = name
        self.description = description
        self.fixtures = fixtures
        self._cases: List[TestCase] = []
        
    def add_case(self, case: TestCase) -> None:
        """Add test case to suite."""
        self._cases.append(case)
        
    def parametrize(self) -> List[pytest.Mark]:
        """Generate pytest parametrize markers."""
        return [
            pytest.mark.parametrize(
                "test_case",
                self._cases,
                ids=[c.name for c in self._cases]
            )
        ]
        
class AsyncTestCase(TestCase):
    """Async-specific test case."""
    
    async def run(self, **fixtures) -> None:
        """Execute async test case."""
        if self.timeout:
            async with asyncio.timeout(self.timeout):
                await self._run_test(**fixtures)
        else:
            await self._run_test(**fixtures)
            
    async def _run_test(self, **fixtures) -> None:
        """Run test with error checking."""
        if self.raises:
            with pytest.raises(self.raises):
                await self._execute(**fixtures)
        else:
            result = await self._execute(**fixtures)
            assert result == self.expected

class PropertyBasedTest:
    """Property-based test generation."""
    
    def __init__(self, module: Any):
        self.module = module
        
    @hypothesis.given(
        st.from_type(str),
        st.from_type(dict)
    )
    def test_config_stability(
        self,
        name: str,
        data: Dict[str, Any]
    ) -> None:
        """Test configuration serialization."""
        config = self.module.Config(name=name, data=data)
        serialized = config.to_dict()
        loaded = self.module.Config.from_dict(serialized)
        assert config == loaded
```

#### Testing Capabilities:
1. **Unit Testing**
   - Fixture management
   - Parameterized tests
   - Async test support
   - Exception testing

2. **Property Testing**
   - Data generation
   - Property validation
   - Edge case testing
   - Shrinking support

3. **Integration Tests**
   - Component interaction
   - System boundaries
   - Service mocking
   - Database testing

4. **Performance Tests**
   - Load testing
   - Stress testing
   - Memory profiling
   - Timing analysis

### 8. MCP Server Integration
**Objective**: Extend functionality through Model Context Protocol servers
- **Features**:
  - GitHub integration
    * Repository management
    * Code synchronization
    * Automated workflows
  - Azure services
    * Cloud configuration
    * Resource management
    * Monitoring
  - Development tools
    * Code analysis
    * Quality checks
    * Documentation

## MCP Server Integration

### What is MCP (Model Context Protocol)?

The Model Context Protocol (MCP) is a sophisticated communication protocol that enables seamless integration between development tools, AI assistants, and various services. In this project, we utilize MCP servers for:

1. **GitHub Integration**
   - Repository management
   - Code synchronization
   - Automated workflows
   - Collaboration features

2. **Azure Services** (Optional Extension)
   - Cloud configuration management
   - Service deployment
   - Resource monitoring
   - Security compliance

3. **Development Tools**
   - Code analysis
   - Documentation generation
   - Quality assurance
   - Performance monitoring

### Benefits of MCP Server Integration

1. **Enhanced Development Workflow**
   - Automated code reviews
   - Intelligent code suggestions
   - Context-aware assistance
   - Integrated version control

2. **Improved Code Quality**
   - Real-time validation
   - Best practice enforcement
   - Automated testing
   - Security scanning

3. **Streamlined Deployment**
   - Automated builds
   - Environment consistency
   - Configuration validation
   - Rollback capabilities

4. **Team Collaboration**
   - Code sharing
   - Knowledge management
   - Project synchronization
   - Change tracking

## Installation

```bash
# Clone the repository
git clone https://github.com/ds25041974/python-config-manager.git

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"
```

## Technical Implementation

### Core Components

1. **Chatbot Engine (`src/chatbot.py`)**
```python
class DineshAssistant:
    """Core chatbot implementation with NLP capabilities."""
    
    async def respond(self, query: str) -> Response:
        """Generate response for user query."""
        # Process query and generate response
        
    def greet(self) -> str:
        """Generate welcome message."""
        # Return personalized greeting
```

2. **Web Backend (`src/web/app.py`)**
```python
app = FastAPI(title="Dinesh Assistant")

@app.post("/api/chat")
async def chat(request: ChatRequest) -> Dict:
    """Handle chat messages."""
    response = await assistant.respond(request.query)
    return {
        "text": response.text,
        "confidence": response.confidence,
        "references": response.references
    }
```

3. **CLI Interface (`src/main.py`)**
```python
def main():
    """CLI entry point with multiple modes."""
    parser = argparse.ArgumentParser()
    # ... command setup ...
    
    if args.web:
        # Start web interface
        uvicorn.run(app, host="0.0.0.0", port=8000)
    elif args.query:
        # One-shot query mode
        response = asyncio.run(assistant.respond(args.query))
        print(response.text)
    else:
        # Interactive mode
        # ... chat loop ...
```

### Web Interface

1. **Frontend (`src/web/templates/index.html`)**
   - Responsive chat interface
   - Message history display
   - Real-time updates
   - Reference link handling

2. **Styling (`src/web/static/style.css`)**
   - Modern design
   - Mobile-friendly layout
   - Smooth animations
   - Theme customization

### System Integration

1. **MCP Server Connection**
   ```
   Client <-> MCP Protocol <-> Server
   |-- Authentication
   |-- Request Routing
   |-- Response Handling
   |-- Error Management
   ```

2. **Cloud Service Integration**
   ```
   ConfigMaster <-> Azure Services
   |-- Configuration Sync
   |-- Resource Management
   |-- Monitoring Integration
   |-- Security Controls
   ```

3. **Development Pipeline**
   ```
   Local Dev <-> GitHub <-> CI/CD
   |-- Code Validation
   |-- Automated Testing
   |-- Documentation Generation
   |-- Deployment Management
   ```

## Project Structure

```
src/
├── chatbot.py          # Core chatbot implementation
├── main.py            # CLI interface
├── config/            # Configuration files
│   ├── i18n.py       # Internationalization
│   ├── settings.py   # App settings
│   ├── templates.py  # Response templates
│   └── validation.py # Input validation
└── web/              # Web interface
    ├── app.py       # FastAPI backend
    ├── static/      # Static assets
    │   └── style.css
    └── templates/   # HTML templates
        └── index.html
tests/               # Test suite
├── test_chatbot.py
└── test_main.py
```

## Installation

1. Create virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Usage

### CLI Mode

1. Interactive chat:
   ```bash
   python -m src.main chat
   ```

2. One-shot query:
   ```bash
   python -m src.main chat --query "What is Python?"
   ```

3. Web interface:
   ```bash
   python -m src.main chat --web
   ```
   Then open http://localhost:8000 in your browser.

### API Endpoints

1. **GET /** - Web interface
2. **GET /api/greet** - Initial greeting
3. **POST /api/chat** - Chat endpoint
   ```json
   {
     "query": "What is Python?"
   }
   ```

## Project Structure

```
src/
├── config/
│   ├── i18n.py        # Internationalization support
│   ├── settings.py    # Configuration management
│   ├── templates.py   # Template system
│   └── validation.py  # Validation logic
├── main.py           # Main application entry
tests/
└── test_main.py     # Comprehensive tests
```

## Advanced Features and Best Practices

### 1. Error Handling Strategy
- Hierarchical error classification
- Detailed error messages
- Error recovery mechanisms
- Graceful degradation
- Debug mode support

### 2. Performance Optimization
- Caching mechanisms
- Lazy loading
- Resource pooling
- Memory management
- Concurrent operations

### 3. Security Considerations
- Protected attributes
- Input validation
- Safe serialization
- Secure defaults
- Access control

### 4. Extensibility
- Plugin architecture
- Custom validators
- Template extensions
- Language additions
- Integration points

### 5. Monitoring and Debugging
- Logging system
- Performance metrics
- Memory tracking
- Operation timing
- Error reporting

## Development

### Running Tests

```bash
# All tests
pytest tests/

# With coverage
pytest --cov=src tests/
```

### Code Quality

```bash
# Format code
black .
isort .

# Type checking
mypy src tests
```

## Technologies Used

- **Python 3.8+**: Core implementation
- **FastAPI**: Web backend
- **Uvicorn**: ASGI server
- **Jinja2**: HTML templating
- **Pytest**: Testing framework
- **Black/isort/mypy**: Code quality tools

## Future Enhancements

1. **Enhanced NLP**
   - Sentiment analysis
   - Entity recognition
   - Intent classification

2. **Extended Features**
   - User authentication
   - Conversation persistence
   - Multi-language support
   - Voice interface

3. **System Improvements**
   - Distributed processing
   - Caching optimization
   - Load balancing
   - Monitoring/analytics

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Run tests
5. Submit pull request

## License

MIT License - see LICENSE file for details.               # This file
```

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Usage

### Basic Greeting

```bash
# English greeting
python -m src.main greet "World"

# Spanish greeting
python -m src.main greet "World" --language es

# Formal style in French
python -m src.main greet "World" --language fr --style formal

# Custom message in Japanese
python -m src.main greet "World" --language ja --message "おはようございます"
```

### Template Management

```bash
# List all templates
python -m src.main templates

# List formal templates
python -m src.main templates --category formal

# Search by tags
python -m src.main templates --tags "business,polite"
```

### Configuration

```bash
# View current config
python -m src.main config view

# Validate config file
python -m src.main config validate --file config.json

# Save current settings
python -m src.main greet "World" --debug --style formal --save-config config.json
```

## Development

This project uses modern Python development tools for quality and consistency:

- **Type Hints**: All code is type-annotated and checked with mypy
- **Documentation**: Google-style docstrings
- **Testing**: pytest with async support and coverage reporting
- **Code Quality**: 
  - black for formatting
  - isort for import sorting
  - flake8 for linting
  - mypy for type checking
  - pre-commit hooks for consistent style

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=xml
```

### Code Quality

```bash
# Format code
black .
isort .

# Run linting
flake8 .
mypy src tests
```

## CI/CD

The project uses GitHub Actions for continuous integration with:

- Multi-Python version testing (3.8-3.11)
- Code formatting verification
- Type checking
- Linting
- Test coverage reporting
- Automatic coverage upload to Codecov

The workflow runs on:
- Push to main branch
- Pull request to main branch

## Project Conventions

1. Type hints on all functions and classes
2. Google-style docstrings for public APIs
3. Test coverage for new functionality
4. Black code formatting
5. Pre-commit hooks for code quality

## Requirements

- Python 3.8 or higher
- Dependencies listed in pyproject.toml
- Development tools in optional-dependencies.dev