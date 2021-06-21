#!/usr/bin/env bash

FORMATTER_VERSION=1.10.0

# Download the repository to check the Java code style
CACHE_DIR=$HOME/.cache
mkdir -p "${CACHE_DIR}"
pushd "${CACHE_DIR}"
if [ ! -f google-java-format-"${FORMATTER_VERSION}"-all-deps.jar ]
then
    curl -LJO "https://github.com/google/google-java-format/releases/download/google-java-format-${FORMATTER_VERSION}/google-java-format-${FORMATTER_VERSION}-all-deps.jar"
    chmod 755 google-java-format-"${FORMATTER_VERSION}"-all-deps.jar
fi
popd

# Get all changed files
FILES=$(cat $HOME/changed_files.txt)

# Run the java code formatter
# The --set-exit-if-changed will throw an error if the code is not following the patterns
java -jar .cache/google-java-format-"${FORMATTER_VERSION}"-all-deps.jar --set-exit-if-changed ${FILES[@]}