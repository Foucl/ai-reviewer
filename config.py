```python
import os

# Configurations for the application
class Config:
    def __init__(self):
        self.CHATGPT_API_KEY = os.getenv('CHATGPT_API_KEY')
        self.LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
        self.REPO_PATH = os.getenv('REPO_PATH')
        self.TARGET_BRANCH = os.getenv('TARGET_BRANCH')
        self.NEW_BRANCH = os.getenv('NEW_BRANCH')

config = Config()
```