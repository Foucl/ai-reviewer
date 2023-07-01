```python
import sys
from code_reviewer.repo_handler import RepoHandler
from code_reviewer.branch_analyzer import BranchAnalyzer
from code_reviewer.code_diff import CodeDiff
from code_reviewer.clean_code_principles import CleanCodePrinciples
from code_reviewer.software_craftsmanship import SoftwareCraftsmanship

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <target_branch> <new_branch>")
        sys.exit(1)

    target_branch = sys.argv[1]
    new_branch = sys.argv[2]

    repo_handler = RepoHandler()
    repo_handler.clone_repo()

    branch_analyzer = BranchAnalyzer(repo_handler)
    branch_analyzer.build_context(target_branch)

    code_diff = CodeDiff(branch_analyzer)
    diff_result = code_diff.analyze_diff(new_branch)

    clean_code_principles = CleanCodePrinciples()
    clean_code_result = clean_code_principles.check(diff_result)

    software_craftsmanship = SoftwareCraftsmanship()
    craftsmanship_result = software_craftsmanship.check(diff_result)

    print("Clean Code Principles Check Result: ", clean_code_result)
    print("Software Craftsmanship Check Result: ", craftsmanship_result)

if __name__ == "__main__":
    main()
```