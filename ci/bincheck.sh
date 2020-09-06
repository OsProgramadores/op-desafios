#!/bin/bash
# Exit with an error code if the current commit contains binary files.

echo '
==================
Binary Files check
==================
'

tmpfile="$(mktemp)"
trap "rm -f ${tmpfile}" 0

set -o errexit
set -o nounset

# Only check files added or modified by this commit.
cat "$HOME/changed_files.txt" | while read fname; do
  if [[ -s "$fname" ]]; then
    if file --mime "${fname}" | grep -q "charset=binary$"; then
      echo "${fname}" >>"${tmpfile}"
    fi
  else
    echo "*** NOTE: Unable to open \"$fname\". This should not happen."
  fi
done

if [[ -s "${tmpfile}" ]]; then
  echo "Binary files are not allowed in this repository."
  echo "The following files appear to contain binary data:"
  echo
  cat "${tmpfile}"
  exit 1
fi

echo "Test OK: No binary files found."
exit 0
