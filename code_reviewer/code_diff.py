```python
import difflib
from .repo_handler import RepoHandler
from .branch_analyzer import BranchAnalyzer

class CodeDiff:
    def __init__(self, repo_handler: RepoHandler, branch_analyzer: BranchAnalyzer):
        self.repo_handler = repo_handler
        self.branch_analyzer = branch_analyzer

    def get_diff(self, branch1: str, branch2: str):
        branch1_content = self.branch_analyzer.get_branch_content(branch1)
        branch2_content = self.branch_analyzer.get_branch_content(branch2)

        diff = difflib.unified_diff(
            branch1_content, branch2_content, lineterm=""
        )

        return "\n".join(list(diff))

    def print_diff(self, branch1: str, branch2: str):
        diff = self.get_diff(branch1, branch2)
        print(diff)
```