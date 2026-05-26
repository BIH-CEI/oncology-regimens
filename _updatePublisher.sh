#!/bin/bash
# Download the latest HL7 IG-Publisher jar into ./input-cache/publisher.jar
set -euo pipefail

INPUT_CACHE_PATH="$PWD/input-cache"
PUBLISHER_JAR="$INPUT_CACHE_PATH/publisher.jar"
DL_URL="https://github.com/HL7/fhir-ig-publisher/releases/latest/download/publisher.jar"

mkdir -p "$INPUT_CACHE_PATH"

echo "Downloading IG Publisher from $DL_URL ..."
curl -fSL --progress-bar "$DL_URL" -o "$PUBLISHER_JAR"

echo "Done. Publisher at: $PUBLISHER_JAR"
java -jar "$PUBLISHER_JAR" -v 2>/dev/null | head -1 || true
