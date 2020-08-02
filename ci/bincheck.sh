#!/bin/bash
# Exit with an error code if the current commit contains binary files.

echo
echo "=================="
echo "Binary Files check"
echo "=================="

tempfile="$(mktemp --tmpdir=/tmp binfoo.XXXX)"
trap "rm -f $tempfile" 0

set -o errexit

# Only check files added or modified by this commit.
cat "$HOME/changed_files.txt" | while read fname; do
  file --mime "${fname}" | grep "charset=binary$" >>$tempfile
done

if [[ -s "$tempfile" ]]; then
  echo "Binary files are not allowed in this repository."
  echo "The following files appear to contain binary data:"
  echo
  sed -e 's/^/* /' "$tempfile"
  exit 1
fi

exit 0
