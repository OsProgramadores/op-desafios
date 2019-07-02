#!/bin/bash
# Test code formatting compliance (Go)

# Run golint on all files in the current directory.
function go_lint() {
  golint -set_exit_status 2>&1
}

# Run govet on all files in the current directory.
function go_vet() {
  go vet 2>&1
}

# Run go_fmt in all go files in current dir. Report diffs.
function go_fmt() {
  # Create a temp file just for this check.
  local tmp=`mktemp`
  trap "rm -f $tmp" EXIT

  find . -type f -name '*.go' -exec gofmt -s -l "{}" \; >"$tmp"
  if grep -q . "$tmp"; then
    echo "ERROR: The following files need formatting with gofmt -s:"
    cat "$tmp"
    rm -f "$tmp"
    return 1
  fi
}

# Main

echo
echo "============="
echo "Go Code check"
echo "============="

# TRAVIS sets TRAVIS_COMMIT_RANGE to the range of commits for the current commit.
if [[ -z "$TRAVIS_COMMIT_RANGE" ]]; then
  export TRAVIS_COMMIT_RANGE="HEAD^"
  echo >&2 "Note: TRAVIS_COMMIT_RANGE environment variable not set. Defaulting to $TRAVIS_COMMIT_RANGE"
fi

set -o nounset

# List of all distinct directories having at least one modified with a ".go" extension
go_dirs=$(git diff --diff-filter=AM --name-only $TRAVIS_COMMIT_RANGE | grep '\.go$' | xargs -l dirname 2>/dev/null | sort -u)

tmpfile=`mktemp`
trap "rm -f $tmpfile" EXIT


# Save stdout/err in FD 6/7, redirect stdout and stderr to $tmpfile.
exec 6>&1 >$tmpfile
exec 7>&2 2>&1

err=0

for dir in $go_dirs; do
  echo
  echo "============================================================"
  echo "Testing directory: $dir"
  echo "============================================================"

  # Fetch dependencies.
  go get -t ./...

  for test in go_lint go_vet go_fmt; do
    echo -e "\n*** Running test $test"
    pushd "$dir" >/dev/null
    $test && echo "No problems found" || err=1
    popd >/dev/null
  done
done

# Restore FDs and close FDs 6/7.
exec 1>&6 6>&-
exec 2>&7 7>&-

# Display results of all tests.
cat $tmpfile

if (( err == 1 )); then
  exit 1
fi

echo "No Go code errors detected."
exit 0
