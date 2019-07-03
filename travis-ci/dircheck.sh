#!/bin/bash
# NAME
#   dircheck.sh
#
# SYNOPSIS
#   Enforce the directory rule for github.com/osprogramadores/op-desafios.
#
# DESCRIPTION
#   This script enforces the following directory structure:
#
#   desafio-*/<username>/<language>/user_files...
#
#   Where:
#     desafio-*: top level directory we check.
#     username: Github username. No files at this level.
#     language: Language. Has to be lowercase. No files other than .gitignore at this level.
#     user_files: Free form.
#
#   Also:
#     - No spaces in filenames.
#     - Only ascii chars in filenames.

# Fail on use of undefined variable.
set -o nounset

TLD="./desafio-*"
res=""

echo
echo "========================="
echo "Directory structure check"
echo "========================="

# Any files containing spaces or non-ascii (including utf8) characters.
invalid_chars=$(find . -name .git -prune -o -print | grep -P '[^[:ascii:]]|[[:space:]]')
if [[ -n "$invalid_chars" ]]; then
  res="${res}*** Files with invalid characters (spaces or non-ascii):\n$invalid_chars\n\n"
fi

# Any files found on 2nd level. We expect only directories here (username).
invalid_level2=$(find . -mindepth 2 -maxdepth 2 -type f -path "$TLD")
if [[ -n "$invalid_level2" ]]; then
  res="${res}*** Invalid username (must be a directory, not a file):\n$invalid_level2\n\n"
fi

# Any files not called .gitignore on the 3rd level. We expect only directories here (language).
invalid_level3=$(find . -mindepth 3 -maxdepth 3 -type f -path "$TLD" | grep -v \.gitignore)
if [[ -n "$invalid_level3" ]]; then
  res="${res}*** Invalid language (must be a directory, not a file):\n$invalid_level3\n\n"
fi

# Any directories on the 3rd level having uppercase characters (language should be all lowercase).
invalid_level3_case=$(find . -mindepth 3 -maxdepth 3 -type d -path "$TLD" -name '*[A-Z]*')
if [[ -n "$invalid_level3_case" ]]; then
  res="${res}*** Language directories must be all lowercase:\n$invalid_level3_case\n\n"
fi

if [[ -n "$res" ]]; then
  echo "ERROR: Problems detected in the directory structure:"
  echo
  echo -ne "$res"
  echo "See https://github.com/osprogramadores/op-desafios#estrutura-de-diret%C3%B3rios for more details"
  exit 1
fi

echo "No errors in the directory structure."
exit 0
