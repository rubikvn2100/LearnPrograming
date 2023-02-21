# LearnPrograming

A share repo for programing learning.

# Commit naming convention

Add new problem: "Add `problemFile.py` problem statement."

Solve problem: "Add solution for `problemFile.py` problem."

Add Unit Test: "Add unit test for `problemFile.test.py` problem."

Fix a file: "`<reason>` for `<fileName>.<extension>` problem."

# Git command convention sequence for submission

Make sure there is nothing new in remote repo, if yes use `git pull`

1/ `git status` to see current files change.

2a/ `git diff` to see the change line by line.

2b/ `git diff <file name>` to see the change line by line in a file.

3/ `git add <file name>` to stage the file.

3\*/ `git diff --staged <file name>` to see the change of a staged file.

4/ `git commit -m "<commit message>"`

5/ `git status` and `git log` to double check the change.

6/ `git commit --amend` to change the commit message of the newest commit.

7\*/ `git log --all --decorate --oneline --graph` to see the commit tree.

# Unit test convention

Make sure you create test that cover edged case. Good unit test show that you understand the problems.
