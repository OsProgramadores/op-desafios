#!/usr/bin/env bash
echo
echo "======================"
echo "Javascript code check"
echo "======================"

set -e

readonly ESLINT_VERSION="8.24.0"

FILES="$(grep "\.*js$" < "${HOME}/changed_files.txt" || [[ $? == 1 ]])"
if [[ -z "${FILES}" ]]; then
    echo "Skiping checking, no Javascript files modified."
    exit 0
fi

echo "✔️  Checking the Javascript files..."

npx eslint@$ESLINT_VERSION -c ci/.eslintrc.yml ${FILES[@]}