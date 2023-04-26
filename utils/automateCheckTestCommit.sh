#!/bin/bash

clear

problemFileName="$1"
testFileName="test_$1"

# Test is the problem file exist.
if ! test -f "$problemFileName"; then
	echo "\"$problemFileName\" does not exist."
	exit 1
fi

# Test if the correspond test file exist.
if ! test -f "$testFileName"; then
    echo "\"$testFileName\" does not exist."
        exit 1
fi

# Test if the unit test pass
python3 -m unittest $testFileName --verbose
if [ $? -ne 0 ]; then
	exit 1
fi

echo

# Check if there are changes staged for commit.
if [ -n "$(git diff --name-only --cached)" ]; then
	echo -e "Staged are not empty. The following file is in staged:\n"
	git diff --name-only --cached

	echo

	exit 1
fi

# Test if there are new solution yet.
if git diff --quiet "$problemFileName"; then
	echo -e "\"$problemFileName\" has nothing to commit.\n"
	exit 1
fi

# Show and check if there is any trailing white space in the problem file.
git diff "$problemFileName"

echo

grep -q " \+$" $problemFileName
if [ $? -eq 0 ]; then
	echo -e "There are trailing white space in \"$problemFileName\", please remove.\n"
	exit 1
fi

# Show and check if there is any trailling white space on the test file.
git diff "$testFileName"

echo

grep -q " \+$" $testFileName
if [ $? -eq 0 ]; then
	echo -e "There are trailing white space in \"$testFileName\", please remove.\n"
	exit 1
fi

# Commit the problem file.
git add $problemFileName
git commit -m "Add \"$problemFileName\" problem statement."

echo

# Commit the test file.
git add $testFileName
git commit -m "Add unit test \"$testFileName\" file."

echo

# Display the commit tree.
git log --all --decorate --oneline --graph -30
echo
