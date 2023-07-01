```python
import os
from git import Repo
from typing import Tuple

def get_repo(repo_path: str) -> Repo:
    """
    Returns a Repo object for the given path.
    """
    if not os.path.exists(repo_path):
        raise Exception(f"Repo not found at {repo_path}")
    return Repo(repo_path)

def get_branches(repo: Repo, target_branch: str, new_branch: str) -> Tuple[str, str]:
    """
    Returns the target and new branches if they exist in the repo.
    """
    branches = [str(branch) for branch in repo.branches]
    if target_branch not in branches:
        raise Exception(f"Target branch {target_branch} not found in repo")
    if new_branch not in branches:
        raise Exception(f"New branch {new_branch} not found in repo")
    return target_branch, new_branch

def get_diff(repo: Repo, target_branch: str, new_branch: str) -> str:
    """
    Returns the diff between the target branch and the new branch.
    """
    target = repo.commit(target_branch)
    new = repo.commit(new_branch)
    return repo.git.diff(target, new)
```