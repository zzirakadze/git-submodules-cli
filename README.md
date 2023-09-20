# git-submodules-cli

This tool assists with git branches switching with proper submodule versions by CLI command.
This tool switch main git branch project with submodule branches together.

```markdown
# Pre-history
SVN has the "externals" feature, which saves submodule projects with a specific branch under the main project branch. 
When the user switches from the "main" branch to the "example" branch, then submodules automatically switch submodules 
branches to "example-sub-1", "example-sub-2," etc.
GIT doesn't have an implemented feature to switch the main project branch with submodule branches together. The team 
should maintain it manually.
```

## TBD

## Getting started  

To run scripts:
1. Check that `test_framework_versions.py` contains you project configuration (it contains base 2023_M23 by default)
2. activate virtual environment for python 11
3. Exec `python git_switch.py Base 2023_M23` to switch all branches to proper version

