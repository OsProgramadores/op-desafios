#!/bin/bash
# Test code formatting compliance.
# So far only python3 supported.

echo
echo "======================"
echo "Python (v3) code check"
echo "======================"

set -e

# Only Added and modified files are checked.
cat $HOME/changed_files.txt | while read fname; do
  ext="${fname##*.}"
  if [[ "$ext" == "py" ]]; then
    echo "* Checking ${fname}"
    pylint --rcfile="ci/pylint3.rc" "$fname"
  fi
done
