```python
from git import Repo

class BranchHandler:
    def __init__(self, repo_path):
        self.repo = Repo(repo_path)

    def get_branch(self, branch_name):
        return self.repo.branches[branch_name]

    def get_diff(self, target_branch, new_branch):
        target = self.get_branch(target_branch)
        new = self.get_branch(new_branch)
        return target.commit.diff(new.commit)

    def get_commits(self, branch_name):
        branch = self.get_branch(branch_name)
        return list(branch.iter_commits())
```