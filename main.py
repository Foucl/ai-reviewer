```python
import os
from config import CHATGPT_API_KEY, LANGCHAIN_API_KEY
from repo_handler import RepoHandler
from branch_handler import BranchHandler
from diff_analyzer import DiffAnalyzer
from code_reviewer import CodeReviewer

def main():
    repo_path = os.getenv('REPO_PATH')
    target_branch = os.getenv('TARGET_BRANCH')
    new_branch = os.getenv('NEW_BRANCH')

    repo_handler = RepoHandler(repo_path)
    branch_handler = BranchHandler(repo_handler.repo)

    target_branch_code = branch_handler.get_branch_code(target_branch)
    new_branch_code = branch_handler.get_branch_code(new_branch)

    diff_analyzer = DiffAnalyzer(target_branch_code, new_branch_code)
    code_diff = diff_analyzer.get_diff()

    code_reviewer = CodeReviewer(CHATGPT_API_KEY, LANGCHAIN_API_KEY)
    review_result = code_reviewer.review_code(code_diff)

    print(review_result)

if __name__ == "__main__":
    main()
```