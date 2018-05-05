# Updating Repos and Squashing Commits

### Updating Branches, Repos, and Forks:
- `git fetch upstream master` -> download latest changes from upstream
- `git rebase upstream/master` -> apply those changes to local repo
- `git push origin/master` -> push changes to our fork

### Squashing Commits:
- `git rebase -i HEAD~<number_of_commits_to_merge_into_one>` -> replace `pick` with `squash` or `s` for all commits except the one on the top.
- `git push origin <branch_name>` -> push the squashed commit. Sometimes, `--force` option with the command will be needed. **USE WITH CAUTION**
