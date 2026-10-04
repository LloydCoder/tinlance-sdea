#!/usr/bin/env bash
set -euo pipefail

: "${SDEA_DOMAIN:?SDEA_DOMAIN must be set}"

curl --fail --silent --show-error --max-time 10 "https://${SDEA_DOMAIN}/healthz" >/dev/null
curl --fail --silent --show-error --max-time 10 "https://${SDEA_DOMAIN}/readyz" >/dev/null

echo "SDEA production health checks passed."
