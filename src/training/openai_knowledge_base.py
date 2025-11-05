"""OpenAI-enhanced knowledge base for advanced technical topics."""

from typing import Dict, List

from .domains import Domain

# Enhanced knowledge base with OpenAI-driven technical content
OPENAI_KNOWLEDGE_BASE: Dict[Domain, List[Dict[str, str]]] = {
    Domain.PYTHON: [
        {
            "topic": "Python Best Practices",
            "description": (
                "Modern Python development best practices:\n\n"
                "1. Code Organization:\n"
                "   • Use type hints for better code clarity\n"
                "   • Implement docstrings (Google style)\n"
                "   • Follow PEP 8 style guidelines\n"
                "   • Use dataclasses for data structures\n\n"
                "2. Error Handling:\n"
                "   • Use specific exception types\n"
                "   • Implement context managers\n"
                "   • Handle cleanup in finally blocks\n"
                "   • Log errors appropriately\n\n"
                "3. Performance Optimization:\n"
                "   • Use generators for large datasets\n"
                "   • Implement caching strategies\n"
                "   • Profile code for bottlenecks\n"
                "   • Optimize database queries"
            ),
            "examples": [
                """# Type hints example
def process_data(items: List[Dict[str, Any]]) -> Generator[str, None, None]:
    \"\"\"Process items and yield results.
    
    Args:
        items: List of data items to process
        
    Yields:
        Processed item strings
    \"\"\"
    for item in items:
        yield transform_item(item)""",
                """# Context manager example
class DatabaseConnection:
    def __enter__(self):
        self.conn = create_connection()
        return self.conn
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()"""
            ]
        },
        {
            "topic": "Python Testing",
            "description": (
                "Comprehensive testing strategies:\n\n"
                "1. Unit Testing:\n"
                "   • pytest for test framework\n"
                "   • pytest-cov for coverage\n"
                "   • Mock objects for isolation\n"
                "   • Parametrized tests\n\n"
                "2. Integration Testing:\n"
                "   • Test database interactions\n"
                "   • API endpoint testing\n"
                "   • Service integration tests\n"
                "   • Environment management\n\n"
                "3. Performance Testing:\n"
                "   • Load testing with locust\n"
                "   • Profiling with cProfile\n"
                "   • Memory usage analysis\n"
                "   • Response time monitoring"
            ),
            "examples": [
                """# Pytest test example
def test_process_data():
    \"\"\"Test data processing functionality.\"\"\"
    input_data = [{"id": 1, "value": "test"}]
    result = list(process_data(input_data))
    assert len(result) == 1
    assert isinstance(result[0], str)""",
                """# Mock example
@patch('module.external_service')
def test_service_integration(mock_service):
    mock_service.return_value = {'status': 'success'}
    result = process_with_service()
    assert result['status'] == 'success'"""
            ]
        }
    ],

    Domain.ARCHITECTURE: [
        {
            "topic": "Hybrid vs Cloud Architecture",
            "description": (
                "Advantages of hybrid architecture over pure cloud:\n\n"
                "1. Cost Benefits:\n"
                "   • Reduced cloud compute costs\n"
                "   • Optimized data transfer\n"
                "   • Local processing savings\n"
                "   • Flexible resource allocation\n\n"
                "2. Scalability:\n"
                "   • Dynamic resource management\n"
                "   • Local-first processing\n"
                "   • Cloud burst capability\n"
                "   • Load-based scaling\n\n"
                "3. Performance:\n"
                "   • Reduced latency\n"
                "   • Local data processing\n"
                "   • Optimized response times\n"
                "   • Better user experience\n\n"
                "4. Security:\n"
                "   • Data locality control\n"
                "   • Reduced exposure\n"
                "   • Custom security policies\n"
                "   • Compliance management"
            ),
            "examples": [
                """# Hybrid processing example
def process_request(data):
    if requires_local_processing(data):
        return process_locally(data)
    return process_in_cloud(data)""",
                """# Cost optimization
def optimize_resource_usage():
    current_load = get_system_load()
    if current_load > CLOUD_THRESHOLD:
        scale_cloud_resources()
    else:
        process_locally()"""
            ]
        }
    ],

    Domain.GITHUB: [
        {
            "topic": "GitHub CI/CD Integration",
            "description": (
                "Advanced GitHub CI/CD practices:\n\n"
                "1. Workflow Automation:\n"
                "   • GitHub Actions integration\n"
                "   • Automated testing\n"
                "   • Deployment pipelines\n"
                "   • Environment management\n\n"
                "2. Quality Assurance:\n"
                "   • Code quality checks\n"
                "   • Security scanning\n"
                "   • Performance testing\n"
                "   • Documentation updates\n\n"
                "3. Deployment Strategies:\n"
                "   • Blue-green deployment\n"
                "   • Canary releases\n"
                "   • Rolling updates\n"
                "   • Automated rollback"
            ),
            "examples": [
                """# GitHub Actions workflow
name: CI/CD Pipeline
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Tests
        run: |
          python -m pytest
          python -m coverage report""",
                """# Deployment script
def deploy_service():
    verify_tests()
    update_environment()
    deploy_new_version()
    health_check()
    switch_traffic()"""
            ]
        }
    ],

    Domain.OPERATION: [
        {
            "topic": "Service Optimization",
            "description": (
                "Service optimization strategies:\n\n"
                "1. Resource Management:\n"
                "   • Memory optimization\n"
                "   • CPU usage control\n"
                "   • Network efficiency\n"
                "   • Storage optimization\n\n"
                "2. Performance Tuning:\n"
                "   • Response time optimization\n"
                "   • Query optimization\n"
                "   • Cache management\n"
                "   • Load balancing\n\n"
                "3. Monitoring:\n"
                "   • Health checks\n"
                "   • Performance metrics\n"
                "   • Error tracking\n"
                "   • Usage analytics"
            ),
            "examples": [
                """# Resource monitoring
def monitor_resources():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    if cpu_usage > THRESHOLD or memory_usage > THRESHOLD:
        optimize_resources()""",
                """# Performance optimization
@cache_result(timeout=3600)
def expensive_operation(data):
    result = process_complex_data(data)
    return optimize_output(result)"""
            ]
        },
        {
            "topic": "Cyber Security",
            "description": (
                "Security implementation strategies:\n\n"
                "1. Authentication:\n"
                "   • Multi-factor authentication\n"
                "   • Token-based security\n"
                "   • Session management\n"
                "   • Access control\n\n"
                "2. Data Protection:\n"
                "   • Encryption at rest\n"
                "   • Secure transmission\n"
                "   • Data sanitization\n"
                "   • Backup strategies\n\n"
                "3. Security Monitoring:\n"
                "   • Intrusion detection\n"
                "   • Audit logging\n"
                "   • Vulnerability scanning\n"
                "   • Security updates"
            ),
            "examples": [
                """# Security middleware
def security_middleware(request):
    validate_token(request.headers.get('Authorization'))
    sanitize_input(request.data)
    log_access(request)
    return process_request(request)""",
                """# Data encryption
def protect_sensitive_data(data):
    encrypted = encrypt_data(data)
    store_securely(encrypted)
    audit_log.info('Data protected successfully')"""
            ]
        }
    ]
}