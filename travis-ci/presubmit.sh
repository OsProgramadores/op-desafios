#!/bin/bash

PROGNAME="${0##*/}"

unset bad

if (( $# < 1 )); then
  echo >&2 "Use $PROGNAME checks..."
  exit 2
fi

for check in "$@"; do
  if [[ ! -x "./travis-ci/$check.sh" ]]; then
    echo "*** Invalid check: $check.sh"
    bad=1
    continue
  fi

  ./travis-ci/$check.sh || bad=1
done

# Return error if any of the previous tests failed.
[[ -n "$bad" ]] && exit 1
exit 0
