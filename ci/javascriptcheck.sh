#!/usr/bin/env bash
echo
echo "======================"
echo "Javascript code check"
echo "======================"

set -e

readonly ESLINT_VERSION="8.24.0"

mapfile -t FILES < <(grep '\.js$' "${HOME}/changed_files.txt" || true)
if [[ ${#FILES[@]} -eq 0 ]]; then
    echo "Skipping checking, no Javascript files modified."
    exit 0
fi

echo "✔️  Checking the Javascript files..."

if [[ -x "./node_modules/.bin/eslint" ]]; then
    ./node_modules/.bin/eslint -c ci/eslintrc.json "${FILES[@]}"
else
    npx "eslint@${ESLINT_VERSION}" -c ci/eslintrc.json "${FILES[@]}"
fi
