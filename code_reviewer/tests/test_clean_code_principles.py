```python
import pytest
from code_reviewer.clean_code_principles import CleanCodePrinciples

def test_init():
    ccp = CleanCodePrinciples()
    assert isinstance(ccp, CleanCodePrinciples)

def test_analyze_code():
    ccp = CleanCodePrinciples()
    code = """
    def hello_world():
        print("Hello, World!")
    """
    result = ccp.analyze_code(code)
    assert isinstance(result, dict)
    assert 'variables' in result
    assert 'functions' in result
    assert 'classes' in result

def test_check_naming_convention():
    ccp = CleanCodePrinciples()
    code = """
    def HelloWorld():
        print("Hello, World!")
    """
    result = ccp.check_naming_convention(code)
    assert isinstance(result, dict)
    assert 'variables' in result
    assert 'functions' in result
    assert 'classes' in result

def test_check_code_complexity():
    ccp = CleanCodePrinciples()
    code = """
    def hello_world():
        if True:
            print("Hello, World!")
    """
    result = ccp.check_code_complexity(code)
    assert isinstance(result, dict)
    assert 'cyclomatic_complexity' in result

def test_check_code_length():
    ccp = CleanCodePrinciples()
    code = """
    def hello_world():
        print("Hello, World!")
    """
    result = ccp.check_code_length(code)
    assert isinstance(result, dict)
    assert 'line_count' in result
    assert 'function_count' in result
    assert 'class_count' in result
```