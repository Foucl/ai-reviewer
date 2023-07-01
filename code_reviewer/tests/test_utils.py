```python
import pytest
from code_reviewer.utils import get_file_diff, get_branch_files

def test_get_file_diff():
    old_file = "old_file.py"
    new_file = "new_file.py"
    diff = get_file_diff(old_file, new_file)
    assert isinstance(diff, str), "Expected string output"

def test_get_branch_files():
    repo_path = "/path/to/repo"
    branch_name = "branch_name"
    files = get_branch_files(repo_path, branch_name)
    assert isinstance(files, list), "Expected list output"
    for file in files:
        assert isinstance(file, str), "Expected each file to be a string"
```