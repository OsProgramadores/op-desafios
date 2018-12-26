#!/bin/bash
# Test if code is validated by the op-validator.

VERIFY_TOKEN_URL="https://osprogramadores.com/v/verify-token/"

# TRAVIS sets TRAVIS_COMMIT_RANGE to the range of commits for the current commit.
if [[ -z "$TRAVIS_COMMIT_RANGE" ]]; then
  echo >&2 "Note: TRAVIS_COMMIT_RANGE environment variable not set. Defaulting to HEAD^ HEAD"
  export TRAVIS_COMMIT_RANGE="HEAD^ HEAD"
fi

# For now, we only allow the submittal of one non-legacy challenge at a time.
# For unique challenge verification, we consider the distinct count of the
# tuple desafio-XX/username/language-feature for all added and modified files.
challenges=($(git diff --diff-filter=AM --name-only $TRAVIS_COMMIT_RANGE | cut -d/ -f1-3 | grep -v '^desafio-0[1-7]' | grep '^desafio-[0-9]\+' | sort -u))
num_challenges=${#challenges[@]}

# If no challenges, we exit without prejudice.
if (( num_challenges == 0 )); then
  echo "NOTE: No challenges found. Assuming other changes. Skipping."
  exit 0
fi

# No duplicate challenges (usually submitting more than one language or possibly, user).
if (( num_challenges > 1 )); then
  echo "ERROR: Please submit at most one challenge at a time. You have attempted ${num_challenges}."
  exit 1
fi

# Locate all .valid files with our expected pattern: desafio-XX/username/language-pattern/.valid
# Note that git diff --name-only only gives us the filenames. We need to extract the challenge
# directories and check if .valid exists in those locations.
cfiles=($(git diff --diff-filter=AM --name-only $TRAVIS_COMMIT_RANGE | grep -v '^desafio-0[1-7]' | grep '^desafio-[0-9]\+/[^/]*/[^/]*' ))
valid=()
for cfile in $cfiles; do
  cdir=${cfile%/*}
  if [[ -s "$cdir/.valid" ]]; then
    valid+=("$cdir/.valid")
  fi
done

# We should only have ONE valid file.
num_valid=${#valid[@]}
if (( num_valid != 1 )); then
  echo "ERROR: Must have ONE validation file (no more, no less). You have $num_valid."
  exit 1
fi

vfile="${valid[0]}"
challenge=$(echo "$vfile" | cut -d/ -f1)
username=$(echo "$vfile" | cut -d/ -f2)
token=$(head -1 "$vfile")

echo "Validation file: $vfile, username: $username, token: $token"

# Validate
if curl -Lsd "challenge_id=${challenge}&username=${username}&token=${token}" $VERIFY_TOKEN_URL | tail -1 | grep "OK"; then
  echo "Validation successful"
  exit 0
fi

echo "Validation failed"
exit 1
