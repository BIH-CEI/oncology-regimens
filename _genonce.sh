#!/bin/bash
# Build the IG once: run SUSHI to compile FSH, then the IG Publisher to render
# the HTML site and validate.
set -euo pipefail

INPUT_CACHE_PATH="./input-cache"
PUBLISHER_JAR="$INPUT_CACHE_PATH/publisher.jar"

if ! command -v sushi >/dev/null 2>&1; then
  echo "SUSHI not installed.  Install with: npm install -g fsh-sushi" >&2
  exit 1
fi

if [ ! -f "$PUBLISHER_JAR" ]; then
  echo "IG Publisher jar not found at $PUBLISHER_JAR" >&2
  echo "Run ./_updatePublisher.sh first." >&2
  exit 1
fi

# Local TX server preference (we run one on :3000 via the ceir-os stack)
TXOPT=""
if curl -fsS http://localhost:3000/metadata >/dev/null 2>&1; then
  echo "Using local terminology server at http://localhost:3000"
  TXOPT="-tx http://localhost:3000"
elif curl -fsS https://tx.fhir.org/r4/metadata >/dev/null 2>&1; then
  echo "Using public tx.fhir.org/r4"
  TXOPT=""
else
  echo "No terminology server reachable; running with -tx n/a"
  TXOPT="-tx n/a"
fi

echo "── SUSHI ──"
sushi build .

echo "── IG Publisher ──"
export JAVA_TOOL_OPTIONS="${JAVA_TOOL_OPTIONS:-} -Dfile.encoding=UTF-8"
java -jar "$PUBLISHER_JAR" -ig . $TXOPT "$@"

echo
echo "Output: file://$PWD/output/index.html"
