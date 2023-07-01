```python
from git import Repo
import os

class RepoHandler:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = self._load_repo()

    def _load_repo(self):
        if not os.path.exists(self.repo_path):
            raise Exception(f"Repo path {self.repo_path} does not exist")
        return Repo(self.repo_path)

    def get_branch(self, branch_name):
        if branch_name not in self.repo.branches:
            raise Exception(f"Branch {branch_name} does not exist in the repo")
        return self.repo.branches[branch_name]

    def checkout_branch(self, branch_name):
        branch = self.get_branch(branch_name)
        self.repo.git.checkout(branch)

    def get_diff(self, target_branch, new_branch):
        self.checkout_branch(target_branch)
        return self.repo.git.diff(new_branch)
```