# LearnPrograming

A share repo for programing learning.

# Commit message convention

Add new problem: "Add `problemFile.py` problem statement."

Solve problem: "Add solution for `problemFile.py` problem."

Add Unit Test: "Add unit test `test_problemFile.py` file."

Fix a file: "`<reason>` for `<fileName>.<extension>`"

# Git command convention sequence for submission

Make sure there is nothing new in remote repo, if there is then use `git pull`.

1/ `git status` to see list of file that ready to stage.

2/ `git diff` to see the change line by line.

3/ `git diff <file name>` to see the change line by line in a file before staged

4/ `git add <file name>` to stage the file.

5/ `git diff --staged <file name>` to see the change of a staged file.

6/ `git commit -m "<commit message>"`

7/ `git status` and `git log` to double check the change.

\_/ `git commit --amend` to change the commit message of the newest commit.

\_/ `git log -<N>` to see the top N commits. Ex: `git log -3` to see the top 3 commits.

\_/ `git log --all --decorate --oneline --graph` to see the commit tree.

# Unit test

Make sure you create test that cover edged cases. Good unit test show that you understand the problems.

You can use the follow command for testing.

`python3 -m unittest` to test all files in a directory.

`python3 -m unittest <test_file.py>` to test a file.

You can use option `--verbose` or `-v` to show the test details.

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
