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
#     language: Language. Has to be lowercase. No files other than .gitignore
#               and .valid at this level.
#     user_files: Free form.
#
#   Also:
#     - No spaces in filenames.
#     - Only ascii chars in filenames.
#     - No files or directories starting with ".", except for files named
#       .gitignore and .valid.

# Fail on use of undefined variable.
set -o nounset

CHANGES="${HOME}/changed_files.txt"

# Returns the name of any files containing spaces or non-ascii (including
# UTF-8) characters.
function check_filenames() {
  invalid_files=$(grep -P '[^[:ascii:]]|[[:space:]]' $CHANGES)
  if [[ -n "$invalid_files" ]]; then
    echo "*** Files contain invalid characters (spaces or non-ascii):\n$invalid_files\n\n"
  fi
}

# Returns the directories of any duplicated challenges. We don't want to see any dupes
# for a "desafios-XX/username/language" tuple.
function check_multiple() {
  level3=$(grep -o '^desafio-[0-9]*/[^/]*/[^/]*/' $CHANGES | sort -u)
  num=$(echo -e "$level3" | wc -l)
  if (( num > 1 )); then
    echo "*** Found ${num} desafios in this PR. Please submit one PR for each):\n$level3\n\n"
  fi
}

# If we have anything under desafios-XX, make sure it follows the following pattern:
# desafios-XX/username/language/files... We will not accept incomplete paths or paths
# with no files or just directories.
function check_dir_structure() {
  local ret=""

  # See the "Directory structure check" help message below for detailed rules.
  # Note the use of grep to remove any directory called .gitignore or .valid
  # and then a negative lookahead to remove any dot files that are not named
  # .gitignore or .valid.
  valid=$(mktemp)
  desafios=$(mktemp)

  grep '^desafio-[0-9]*' $CHANGES | sort -u >"${desafios}"

  grep '^desafio-[0-9]*/[^/]*/[a-z0-9_+-]*/.\+$' "${desafios}" |
    grep -v '/\.\(gitignore\|valid\)/' |
    grep -Pv '/\.(?!(gitignore|valid)$).*' > "${valid}"

  invalid=$(diff --unchanged-line-format='' --old-line-format='%L' "${desafios}" "${valid}")
  rm -f "${valid}" "${desafios}"

  if [[ -n "$invalid" ]]; then
    echo "*** Invalid directory structure. Incorrect files/directories:\n$invalid\n\n"
  fi
}

echo '
=========================
Directory structure check
========================='

invalid_filenames=$(check_filenames)
invalid_multiple=$(check_multiple)
invalid_dir_structure=$(check_dir_structure)

res="${invalid_filenames}${invalid_multiple}${invalid_dir_structure}"

if [[ -n "$res" ]]; then
echo '
=== ATTENTION ===

We detected problems in your file structure.

We expect every submission to follow the following directory structure:

desafio-NN/git-username/language/your_files_and_directories...

Note that:

1) We don not allow spaces or non-ascii characters in filenames.
2) We only accept ONE desafio per PR.
3) We reject incomplete paths (missing username, language, files).
4) Language only accepts lowercase characters, numbers, "-", "_", and "+".
5) We can have any structure under files, but we do not accept files or
   directories starting with a "." *unless* it is a file called .gitignore

Errors:
'

  echo -ne "$res"
  echo "See https://github.com/osprogramadores/op-desafios#estrutura-de-diret%C3%B3rios for more details"
  exit 1
fi

echo "No errors in the directory structure."
exit 0
