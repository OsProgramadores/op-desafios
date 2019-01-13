#!/bin/bash

for presub in "$@"; do
  ./travis-ci/$presub.sh
  echo
done
