#!/bin/bash
# Exit with an error code if the current commit contains binary files.

echo
echo "=================="
echo "Binary Files check"
echo "=================="

if [[ -z "$TRAVIS_COMMIT_RANGE" ]]; then
  echo >&2 "Note: TRAVIS_COMMIT_RANGE environment variable not set. Defaulting to HEAD HEAD^"
  export TRAVIS_COMMIT_RANGE="HEAD HEAD^"
fi

tempfile="$(mktemp --tmpdir=/tmp binfoo.XXXX)"
trap "rm -f $tempfile" 0

set -o errexit

# Only check files added or modified by this commit.
git diff --diff-filter=AM --name-only $TRAVIS_COMMIT_RANGE | while read fname; do
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
