#!/bin/bash
# Test code formatting compliance.
# So far only python3 supported.

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

# TRAVIS sets TRAVIS_COMMIT_RANGE to the range of commits for the current commit.
if [[ -z "$TRAVIS_COMMIT_RANGE" ]]; then
  echo >&2 "Note: TRAVIS_COMMIT_RANGE environment variable not set. Defaulting to HEAD HEAD^"
  export TRAVIS_COMMIT_RANGE="HEAD HEAD^"
fi

# From this point on, we exit immediately with any failure.
# TODO: Improve this to only exit after all files have been
# checked, but note that travis-ci makes special use of $?
# (https://docs.travis-ci.com/user/customizing-the-build/#note-on-)
set -e

# Only Added and modified files are checked.
git diff --diff-filter=AM --name-only $TRAVIS_COMMIT_RANGE | while read fname; do
  # May be possible to use TRAVIS_CI_BUILD instead of .. below.
  ext="${fname##*.}"
  if [[ "$ext" == "py" ]]; then
    pylint --rcfile=pylint3.rc ../"$fname"
  fi
done

# Error out if any files need formatting.
if grep -q . "$TMPFILE"; then
  echo "ERROR: The following files need formatting with gofmt -s:"
  cat $TMPFILE
  exit 1
fi
