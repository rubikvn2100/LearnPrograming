# LearnPrograming

A share repo for programing learning.

# Commit message convention

Add new problem: "Add \\"`problemFile.py`\\" problem statement."

Solve problem: "Add solution for \\"`problemFile.py`\\" problem."

Add Unit Test: "Add unit test \\"`test_problemFile.py`\\" file."

Fix a file: "... `<reason>` for \\"`<fileName>`\\" ..."

# Git command convention sequence for submission

Make sure there is nothing new in remote repo, if there is then use `git pull` before any push.

1\_/ `git status` to see list of file that ready to stage.

2a/ `git diff` to see every change line by line.

2b/ `git diff <file name>` to see the change line by line in a file.

3\_/ `git add <file name>` to stage a file.

4\_/ `git status` to see if the file is staged.

5a/ `git diff --staged` to see the change in staged.

5b/ `git diff --staged <file name>` to see the change of a file in staged.

6\_/ `git commit -m "<commit message>"` with the commit message convention.

7\_/ `git status` to see if the staged file is commited

8\_/ `git log` to see if the correct commited message is displayed.

\_\_/ `git commit --amend` to change the commit message of the newest commit.

\_\_/ `git log -<N>` to see the top N commits. Ex: `git log -3` to see the top 3 commits.

\_\_/ `git log --all --decorate --oneline --graph` to see the commit tree.

# Unit test

Make sure you create test that cover edged cases. Good unit test show that you understand the problems.

You can use the follow command for testing.

`python3 -m unittest` to test all files in a directory.

`python3 -m unittest <test_file.py>` to test a file.

You can use option `--verbose` or `-v` to show the test details.

# In case you want to fix a Pull Request

Sometime, you want to change a pull request instead of making new fix commit because the change is too small or too silly. Here is how you do it.

1\_/ `git reset --soft HEAD~<N>` to remove N commits in the top of the commit tree.

2a/ `git restore --staged <file>` to restore a single file from staged.

2b/ `git restore --staged .` to restore all files in the current directory.

3\_/ What ever you need to do according to the convention sequence for submission.

4\_/ `git push --force` to force the new change into the Remote Git.

Note: if your push remove all the commits in the current Pull Request, you will also close the Pull Request. So, if you want the Pull Request to be open, you need to push at least one commit.

# In case that you make to many changes.

If you make too many commits for a problem, it is recommend to have a new clone and a new pull request.

1/ `cd` to the directory that store our git repo `LearnPrograming`

2/ `rm -rf LearnPrograming` (Note: make sure that you don't remove something that you are working on)

3/ `git clone <git-path>` to make a new clone.

4/ `cd LearnPrograming`

5/ `git log --all --decorate --oneline --graph` to see the commit tree.

6/ `git reset --hard HEAD~<N>` to remove N commit that you want to remove. Make sure you only remove your commit, don't remove my commit. Ex: `git reset --hard HEAD~5` will remove 5 commit.

7/ `git push -f` to force push the new commit tree into GitHub.

Note: step 6 and step 7 are dangerous. It is recommend to be execute carefully. Please consult me if you are in doubt.
