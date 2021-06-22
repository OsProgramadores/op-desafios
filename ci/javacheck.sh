#!/usr/bin/env bash
echo
echo "======================"
echo "Java code check"
echo "======================"

set -e

FORMATTER_VERSION=1.10.0

# Download the repository to check the Java code style
echo
echo "Downloading the Google Java Formatter jar..."

CACHE_DIR=$HOME/.cache
mkdir -p "${CACHE_DIR}"
pushd "${CACHE_DIR}"
if [ ! -f google-java-format-"${FORMATTER_VERSION}"-all-deps.jar ]
then
    curl -LJO "https://github.com/google/google-java-format/releases/download/v${FORMATTER_VERSION}/google-java-format-${FORMATTER_VERSION}-all-deps.jar"
    chmod 755 google-java-format-"${FORMATTER_VERSION}"-all-deps.jar
fi
popd

echo
echo "Checking the Java code format..."

# Only Added and modified files are checked.
cat $HOME/changed_files.txt | while read fname; do
  ext="${fname##*.}"
  if [[ "$ext" == "java" ]]; then
    echo "* Checking ${fname}"
    # The --set-exit-if-changed will throw an error if the code is not following the patterns
    java -jar ${CACHE_DIR}/google-java-format-"${FORMATTER_VERSION}"-all-deps.jar --set-exit-if-changed "${fname}"
  fi
done