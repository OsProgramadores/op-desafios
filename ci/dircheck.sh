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

# Regular expression catching obsolete directories (first path element only).
readonly OBSOLETE_REGEXP="^(desafio-04|desafio-05)$"

# Users matches by this regular expression can submit to deprecated directories.
readonly OVERRIDE_USERS='^(marcopaganini|mpinheir|qrwteyrutiyoup|BernardinoCampos|dependabot\[bot\])$'

# Regular expression catching valid languages.
readonly VALID_LANG_REGEXP="^(c|cpp|csharp|java|javascript|go|php|python)$"

# Changes points to the file containing the list of changes files for this PR.
# This file contains output equivalent to running  find . -type f | sed 's#^\./##'
# at the root of the repo.
readonly CHANGES="${HOME}/changed_files.txt"

# Returns an indented file list from a list of files in string format separated
# with '\n's.
function filelist() {
  # shellcheck disable=SC2001 # Need sed since it's a multi-line string.
  sed "s/^/  - /" <<< "$1"
}

# Returns the name of any files containing spaces or non-ascii (including
# UTF-8) characters.
function check_filenames() {
  invalid_files=$(grep -P '[^[:ascii:]]|[[:space:]]' "$CHANGES")
  if [[ -n "$invalid_files" ]]; then
    # shellcheck disable=SC2028 # Control chars expanded outside function.
    echo "❌ Files contain invalid characters (spaces or non-ascii):\n$(filelist "$invalid_files")"
  fi
}

# Returns the directories of any duplicated challenges. We don't want to see any dupes
# for a "desafios-XX/username/language" tuple.
function check_multiple() {
  level3=$(grep -o '^desafio-[0-9]*/[^/]*/[^/]*/' "$CHANGES" | sort -u)
  num=$(echo -e "$level3" | wc -l)
  if (( num > 1 )); then
    # shellcheck disable=SC2028 # Control chars expanded outside function.
    echo "❌ Found ${num} desafios in this PR. Please submit one PR for each:\n$(filelist "$level3")"
  fi
}

# If we have anything under desafios-XX, make sure it follows the following pattern:
# desafios-XX/username/language/files... We will not accept incomplete paths or paths
# with no files or just directories.
function check_dir_structure() {
  # See the "Directory structure check" help message below for detailed rules.
  # Note the use of grep to remove any directory called .gitignore or .valid
  # and then a negative lookahead to remove any dot files that are not named
  # .gitignore or .valid.
  valid=$(mktemp)
  desafios=$(mktemp)

  grep '^desafio-[0-9]*' "$CHANGES" | sort -u >"${desafios}"

  grep '^desafio-[0-9]*/[^/]*/[a-z0-9_+-]*/.\+$' "${desafios}" |
    grep -v '/\.\(gitignore\|valid\)/' |
    grep -Pv '/\.(?!(gitignore|valid)$).*' > "${valid}"

  invalid=$(diff --unchanged-line-format='' --old-line-format='%L' "${desafios}" "${valid}")
  rm -f "${valid}" "${desafios}"

  if [[ -n "$invalid" ]]; then
    # shellcheck disable=SC2028 # Control chars expanded outside function.
    echo "❌ Invalid directory structure. Incorrect files/directories:\n$(filelist "$invalid")"
  fi
}

# Flag obsolete/deprecated challenges.
function check_deprecated() {
  # Fetch the first path in the directory (desafio-XX)
  while read -r des; do
    if grep -q --perl-regexp "${OBSOLETE_REGEXP}" <<< "$des"; then
      echo "❌ Desafio ${des} is deprecated/obsolete"
    fi
  done < <(grep '^desafio-[0-9]*' "$CHANGES" | cut -d/ -f1 | uniq)
}

# Flag any invalid (non-acceptable) languages.
function check_languages() {
  while read -r lang; do
    if [[ -n "$lang" ]] && ! grep -q --perl-regexp "${VALID_LANG_REGEXP}" <<< "$lang"; then
      echo "❌ Unsupported computer language: \"${lang}\""
    fi
  done < <(grep '^desafio-[0-9]*' "$CHANGES" | cut -d/ -f3 | uniq)
}

echo '
=========================
Directory structure check
========================='

declare -a results
results=(
  "$(check_filenames)"
  "$(check_multiple)"
  "$(check_dir_structure)"
)

# Check deprecated directories and supported languages if not coming from
# one of the users authorized to override this test.
if grep -q --perl-regexp "${OVERRIDE_USERS}" <<< "${GITHUB_ACTOR:-nobody}"; then
  results+=( "$(check_deprecated)" "$(check_languages)" )
fi

# Assemble the printed output based on the contents of the results array
# with newlines separating each result.
output=""
for res in "${results[@]}"; do
  if [[ -n "$res" ]]; then
    sep=""
    [[ -n "$output" ]] && sep="\n\n"
    output="${output}${sep}${res}"
  fi
done

if [[ -n "$output" ]]; then
  echo -e "
IMPORTANT

Your directory structure has issues that need your attention.
We expect every submission to follow the following directory structure:

desafio-NN/git-username/language/your_files_and_directories...

Also note that:

1) We do not allow spaces or non-ascii characters in filenames.
2) We only accept ONE desafio per PR.
3) We reject incomplete paths (missing username, language, files).
4) There's a limited set of acceptable languages. Check the repo README.md for details.
5) We can have any structure under files, but we do not accept files or
   directories starting with a '.' *unless* it is a file called .gitignore

Errors:

$output

See https://github.com/osprogramadores/op-desafios/#readme for more details.
"
  exit 1
fi

echo "✅ No errors found in the directory structure."
exit 0
