#!/bin/bash

ret=0
for presub in "$@"; do
  ./travis-ci/$presub.sh || ret=1
  echo
done
exit $ret
