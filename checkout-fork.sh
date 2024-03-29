#!/bin/bash
# Generated by ChatGPT

# Check if the parameter is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <username:branch-name>"
    exit 1
fi

# Split the input into username and branch-name
IFS=':' read -r USERNAME BRANCH_NAME <<< "$1"

# Default to master if no branch name is provided
if [ -z "$BRANCH_NAME" ]; then
    BRANCH_NAME="master"
fi

# Repository name is hardcoded as per your request
REPOSITORY_NAME="op-desafios"

# Check if the remote already exists
if git remote get-url "$USERNAME" > /dev/null 2>&1; then
    echo "Remote '$USERNAME' already exists. Fetching updates..."
else
    # Add remote for the given username
    git remote add "$USERNAME" https://github.com/"$USERNAME"/"$REPOSITORY_NAME".git
fi

# Fetch the latest changes from this remote
git fetch "$USERNAME"

# Check if the branch already exists locally
if git branch --list | grep -q "${USERNAME}-${BRANCH_NAME}$"; then
    echo "Branch '${USERNAME}-${BRANCH_NAME}' already exists. Switching to it..."
    git checkout "${USERNAME}-${BRANCH_NAME}"
else
    # Checkout a new branch based on the fork's branch
    git checkout -b "${USERNAME}-${BRANCH_NAME}" --track "$USERNAME/$BRANCH_NAME"
fi

