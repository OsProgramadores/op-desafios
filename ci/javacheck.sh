#!/usr/bin/env bash
echo
echo "======================"
echo "Java code check"
echo "======================"

set -e

echo
echo "Checking if some Java file was modified..."
FILES=$(cat ${HOME}/changed_files.txt | grep ".*java$" || [[ $? == 1 ]])

if [ -z ${FILES} ]; then
    echo "Skiping checking, no Java file was modified..."
    exit 0
fi

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

# The --set-exit-if-changed will throw an error if the code is not following the patterns
# The -n option will display all files that not follows the desired patterns
# The --add-exports options are to avoid some warnings raised by the JVM
java \
  --add-exports jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED \
  --add-exports jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED \
  --add-exports jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED \
  --add-exports jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED \
  --add-exports jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED \
  -jar ${CACHE_DIR}/google-java-format-"${FORMATTER_VERSION}"-all-deps.jar -n --set-exit-if-changed ${FILES[@]}
