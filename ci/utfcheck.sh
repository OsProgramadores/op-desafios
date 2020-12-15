#!/bin/bash
# Exit with an error code if the current commit contains binary files.

echo '
======================
UTF-8 compliance check
======================
'

tmpfile="$(mktemp)"
# shellcheck disable=SC2064
trap "rm -f ${tmpfile}" 0

set -o errexit
set -o nounset

# Only check files added or modified by this commit.
while read -r fname; do
  if [[ -s "$fname" ]]; then
    if ! iconv -f UTF-8 "$fname" -o /dev/null 2>/dev/null; then
      echo "${fname}" >>"${tmpfile}"
    fi
  else
    echo "*** NOTE: Unable to open \"$fname\". This should not happen."
  fi
done < "$HOME/changed_files.txt"

if [[ -s "${tmpfile}" ]]; then
  echo "Found files with invalid UTF-8 encoding (listed below)."
  echo "Please make sure your operating system and editor/IDE"
  echo "are properly configured to use UTF-8 as the character set."
  echo
  cat "${tmpfile}"
  exit 1
fi

echo "Test OK: All files have valid UTF-8 encoding."
exit 0
