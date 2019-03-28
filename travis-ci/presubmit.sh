#!/bin/bash

echo
echo "===== Directory Structure check ====="
echo
./travis-ci/dircheck.sh

echo
echo "===== Binary files check ====="
echo
./travis-ci/bincheck.sh

echo
echo "===== Python code check (if needed) ====="
echo
./travis-ci/codecheck.sh

echo
echo "===== Validator token check ====="
echo
./travis-ci/validator.sh
