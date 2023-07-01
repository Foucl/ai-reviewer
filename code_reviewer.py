```python
from langchain_handler import LangchainHandler
from chatgpt_handler import ChatGPTHandler
from clean_code_principles import CleanCodePrinciples
from software_craftsmanship import SoftwareCraftsmanship

class CodeReviewer:
    def __init__(self, langchain_api_key, chatgpt_api_key):
        self.langchain_handler = LangchainHandler(langchain_api_key)
        self.chatgpt_handler = ChatGPTHandler(chatgpt_api_key)
        self.clean_code_principles = CleanCodePrinciples()
        self.software_craftsmanship = SoftwareCraftsmanship()

    def review_code(self, code_diff):
        # Build a full context of the target branch
        context = self.langchain_handler.build_context(code_diff.target_branch)

        # Ask the AI to analyze the diff to the new branch
        diff_analysis = self.langchain_handler.analyze_diff(code_diff)

        # Instruct chatgpt to focus on principles of clean code and software craftsmanship
        review_feedback = self.chatgpt_handler.generate_review(diff_analysis, context, self.clean_code_principles, self.software_craftsmanship)

        return review_feedback
```