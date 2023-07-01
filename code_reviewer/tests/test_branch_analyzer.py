```python
import pytest
from git import Repo
from code_reviewer.branch_analyzer import BranchAnalyzer
from code_reviewer.repo_handler import RepoHandler

def test_branch_analyzer_initialization():
    repo_handler = RepoHandler('path_to_repo')
    branch_analyzer = BranchAnalyzer(repo_handler, 'target_branch', 'new_branch')
    assert isinstance(branch_analyzer, BranchAnalyzer)

def test_get_target_branch():
    repo_handler = RepoHandler('path_to_repo')
    branch_analyzer = BranchAnalyzer(repo_handler, 'target_branch', 'new_branch')
    assert branch_analyzer.get_target_branch() == 'target_branch'

def test_get_new_branch():
    repo_handler = RepoHandler('path_to_repo')
    branch_analyzer = BranchAnalyzer(repo_handler, 'target_branch', 'new_branch')
    assert branch_analyzer.get_new_branch() == 'new_branch'

def test_analyze_diff():
    repo_handler = RepoHandler('path_to_repo')
    branch_analyzer = BranchAnalyzer(repo_handler, 'target_branch', 'new_branch')
    diff = branch_analyzer.analyze_diff()
    assert isinstance(diff, dict)
    assert 'added' in diff
    assert 'deleted' in diff
    assert 'modified' in diff

def test_get_full_context():
    repo_handler = RepoHandler('path_to_repo')
    branch_analyzer = BranchAnalyzer(repo_handler, 'target_branch', 'new_branch')
    context = branch_analyzer.get_full_context()
    assert isinstance(context, dict)
    assert 'target_branch' in context
    assert 'new_branch' in context
```