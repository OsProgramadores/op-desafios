#!/usr/bin/env bash
echo
echo "======================"
echo "Java code check"
echo "======================"

set -e
readonly FORMATTER_VERSION="1.10.0"
readonly JAVA_FORMATTER_FILE="/tmp/google-java-format-${FORMATTER_VERSION}-all-deps.jar"
readonly JAVA_FORMATTER_URL="https://github.com/google/google-java-format/releases/download/v${FORMATTER_VERSION}/${JAVA_FORMATTER_FILE##*/}"

FILES="$(grep "\.*java$" < "${HOME}/changed_files.txt" || [[ $? == 1 ]])"
if [[ -z "${FILES}" ]]; then
    echo "Skiping checking, no Java files modified."
    exit 0
fi

# Download the repository to check the Java code style
echo "✔️  Downloading the Google Java Formatter jar..."
if [[ ! -f "${JAVA_FORMATTER_FILE}" ]]; then
    curl -LJO --show-error "${JAVA_FORMATTER_URL}" -o "${JAVA_FORMATTER_FILE}"
    chmod 755 "${JAVA_FORMATTER_FILE}"
fi

echo "✔️  Checking the Java code format..."


# Check all java files.
exitcode=0
for fname in "${FILES[@]}"; do
  echo "✔️  Checking file: ${fname}"

  output="/tmp/${fname##*/}_corrected.java"
  # The --add-exports options are to avoid some warnings raised by the JVM.
  java \
  --add-exports jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED \
  --add-exports jdk.compiler/com.sun.tools.javac.file=ALL-UNNAMED \
  --add-exports jdk.compiler/com.sun.tools.javac.parser=ALL-UNNAMED \
  --add-exports jdk.compiler/com.sun.tools.javac.tree=ALL-UNNAMED \
  --add-exports jdk.compiler/com.sun.tools.javac.util=ALL-UNNAMED \
    -jar "${JAVA_FORMATTER_FILE}" "${fname}" > "${output}"

    # For some reason, --set-exit-if-changed seems to do always return 1
    # even  when there's no difference. In this case, we check the diffs
    # manually.
    if ! diff --unified "${fname}" "${output}"; then
      echo "❌ Error: Differences found for ${fname}. Please check the output and correct."
      echo "--------------------------------------------------------------------------------"
      exitcode=1
    fi
    rm -f "${output}"
done

exit "${exitcode}"
