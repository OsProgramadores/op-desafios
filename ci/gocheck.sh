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

# Generate a clean GOPATH in the specified directory.
function clean_gopath() {
  export gp="${1?}"
  rm -rf "${gp}"
  mkdir -p "${gp}"/{src,pkg,bin}
}

# Main

echo
echo "============="
echo "Go Code check"
echo "============="

set -o nounset

# List of all distinct directories having at least one modified with a ".go" extension
go_dirs=$(grep '\.go$' "$HOME/changed_files.txt" | xargs -l dirname 2>/dev/null | sort -u)

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

  # Copy current directory to a clean directory inside GOPATH.
  export GOPATH="/tmp/go"
  export TESTDIR="${GOPATH}/src/test"
  clean_gopath "${GOPATH}"

  pushd "${dir}" >/dev/null
  cp -ar . "${TESTDIR}"
  popd >/dev/null

  # Fetch dependencies.
  pushd "${TESTDIR}" >/dev/null
  go get -t ./...

  for test in go_lint go_vet go_fmt; do
    echo -e "\n*** Running test $test"
    $test && echo "No problems found" || err=1
  done
  popd >/dev/null
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
