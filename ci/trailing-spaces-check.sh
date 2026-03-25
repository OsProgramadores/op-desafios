#!/bin/bash
# Exit with an error code if the current commit contains files with
# lines having spaces or tabs at EOL.

echo '
======================
Trailing spaces check
======================
'

tmpfile="$(mktemp)"
# shellcheck disable=SC2064
trap "rm -f ${tmpfile}" 0

set -o errexit
set -o nounset

# Only check files added or modified by this commit.
# TODO: Make this more efficient for large sets of files.
while read -r fname; do
  if [[ -s "$fname" ]]; then
    grep -HPn '[ \t]+$' "$fname" >>"$tmpfile" || true
  else
    echo "*** NOTE: Unable to open \"$fname\". This should not happen."
  fi
done < "$HOME/changed_files.txt"

if [[ -s "${tmpfile}" ]]; then
  echo "Found files containing lines with spaces or tabs at end-of-line."
  echo "Please remove all lines containing only spaces and any extra"
  echo "spaces or tabs after the last non-blank character in the files"
  echo "and lines indicated below:"
  echo
  cat "${tmpfile}"
  exit 1
fi

echo "Test OK: No files with lines containing trailing spaces."
exit 0
