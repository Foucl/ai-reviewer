```python
import os
import git
from git import Repo

class RepoHandler:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = self._load_repo()

    def _load_repo(self):
        if not os.path.exists(self.repo_path):
            raise ValueError(f"Repo path {self.repo_path} does not exist.")
        return Repo(self.repo_path)

    def get_branches(self):
        return [branch.name for branch in self.repo.branches]

    def checkout_branch(self, branch_name):
        if branch_name not in self.get_branches():
            raise ValueError(f"Branch {branch_name} does not exist in the repo.")
        self.repo.git.checkout(branch_name)

    def get_diff(self, target_branch, new_branch):
        self.checkout_branch(target_branch)
        target_commit = self.repo.commit(target_branch)

        self.checkout_branch(new_branch)
        new_commit = self.repo.commit(new_branch)

        return self.repo.git.diff(target_commit, new_commit)
```