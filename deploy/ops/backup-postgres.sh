#!/usr/bin/env bash
set -euo pipefail

: "${POSTGRES_CONTAINER:=tinlance-sdea-postgres-1}"
: "${BACKUP_DIR:=/var/backups/tinlance-sdea}"
: "${POSTGRES_USER:?POSTGRES_USER must be set}"
: "${POSTGRES_DB:?POSTGRES_DB must be set}"

mkdir -p "$BACKUP_DIR"
chmod 700 "$BACKUP_DIR"

timestamp="$(date -u +%Y%m%dT%H%M%SZ)"
output="$BACKUP_DIR/sdea-$timestamp.sql.gz"

docker exec "$POSTGRES_CONTAINER" pg_dump --clean --if-exists --no-owner --no-privileges -U "$POSTGRES_USER" "$POSTGRES_DB" | gzip -9 > "$output"
chmod 600 "$output"

echo "Created $output"
