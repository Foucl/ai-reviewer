```python
import os
import subprocess

def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def is_repo(path):
    return '.git' in os.listdir(path)

def get_branches(path):
    command = f'cd {path} && git branch'
    output, error = execute_command(command)
    if error:
        raise Exception(f'Error while getting branches: {error}')
    branches = output.decode('utf-8').split('\n')
    return [branch.strip() for branch in branches if branch]

def get_diff(target_branch, new_branch, path):
    command = f'cd {path} && git diff {target_branch}..{new_branch}'
    output, error = execute_command(command)
    if error:
        raise Exception(f'Error while getting diff: {error}')
    return output.decode('utf-8')

def get_files_in_branch(branch, path):
    command = f'cd {path} && git ls-tree -r {branch} --name-only'
    output, error = execute_command(command)
    if error:
        raise Exception(f'Error while getting files in branch: {error}')
    return output.decode('utf-8').split('\n')
```