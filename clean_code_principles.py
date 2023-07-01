```python
class CleanCodePrinciples:
    def __init__(self):
        self.principles = {
            "MeaningfulNames": "Use meaningful and pronounceable variable names",
            "Functions": "Functions should do one thing",
            "Comments": "Only comment things that have business logic complexity",
            "Formatting": "Use consistent indentation",
            "ErrorHandling": "Don't return error codes, throw exceptions",
            "Boundaries": "Draw boundaries",
            "UnitTests": "Unit tests should be thorough and pass 100%",
            "Classes": "Organize classes around functionality, not data",
            "Concurrency": "Concurrency should be out of sight and out of mind",
            "Simplicity": "Keep it simple, stupid",
        }

    def get_principles(self):
        return self.principles
```