```python
import os
from git import Repo
from .repo_handler import RepoHandler

class BranchAnalyzer:
    def __init__(self, repo_handler: RepoHandler):
        self.repo_handler = repo_handler

    def get_target_branch_context(self, target_branch: str):
        self.repo_handler.checkout_branch(target_branch)
        return self.repo_handler.get_current_branch_context()

    def analyze_diff_to_new_branch(self, new_branch: str):
        target_branch_context = self.get_target_branch_context(new_branch)
        diff = self.repo_handler.get_diff_between_branches(new_branch)
        return self._analyze_diff(diff, target_branch_context)

    def _analyze_diff(self, diff, target_branch_context):
        added_lines = []
        removed_lines = []
        for file_diff in diff:
            for hunk in file_diff:
                for line in hunk:
                    if line.is_added:
                        added_lines.append(line)
                    elif line.is_removed:
                        removed_lines.append(line)
        return {
            'added_lines': added_lines,
            'removed_lines': removed_lines,
            'target_branch_context': target_branch_context
        }
```