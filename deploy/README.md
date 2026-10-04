# SDEA VPS production deployment

This deployment is a single-VPS Docker Compose topology for the first production stage.

~~~text
Internet
  -> Caddy :80/:443
  -> SDEA API :8000
       -> PostgreSQL
       -> Valkey
  -> SDEA Worker
~~~

Only Caddy publishes host ports. PostgreSQL and Valkey remain on the private Compose network.

## Recommended VPS

- 4 vCPU
- 8 GB RAM
- 80–160 GB SSD/NVMe
- Ubuntu 24.04 LTS
- European region close to Tinlance's primary customer base

This is a starting point, not a permanent scaling limit.

## DNS and TLS

Create an A record for the SDEA hostname pointing to the VPS IPv4 address. Add an AAAA record only if IPv6 is configured correctly.

Caddy automatically obtains and renews public TLS certificates when the hostname resolves to the server and ports 80/443 are reachable.

## Host hardening

Use a non-root administrative user and SSH keys. Enable automatic security updates. Allow only SSH, HTTP and HTTPS through the host firewall.

Example UFW policy:

~~~bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
~~~

Never expose PostgreSQL 5432 or Valkey 6379 to the public internet.

## Docker

Install Docker Engine and the Compose plugin using Docker's official installation instructions.

Verify:

~~~bash
docker --version
docker compose version
~~~

## Application checkout

Use a dedicated deployment directory:

~~~bash
sudo mkdir -p /opt/tinlance-sdea
sudo chown "$USER":"$USER" /opt/tinlance-sdea
cd /opt/tinlance-sdea
git clone https://github.com/LloydCoder/tinlance-sdea.git .
~~~

The production Compose files live under deploy/.

## GHCR authentication

The production image is published to GitHub Container Registry by GitHub Actions.

On the VPS, authenticate with a GitHub credential that has the minimum package-read permission required for the private image:

~~~bash
echo "$GHCR_READ_TOKEN" | docker login ghcr.io -u LloydCoder --password-stdin
~~~

Never commit the token.

## Configure runtime secrets

~~~bash
cd /opt/tinlance-sdea/deploy
cp .env.example .env
chmod 600 .env
~~~

Set:

- SDEA_DOMAIN
- POSTGRES_PASSWORD to a long random value
- DATABASE_URL using the same password
- REDIS_URL

For higher-assurance deployments, migrate credentials from .env to Docker Compose secrets. Environment variables are intentionally used in this first deployment because they keep the single-VPS bootstrap simple.

## Start

~~~bash
docker compose -f compose.yaml pull
docker compose -f compose.yaml up -d
docker compose -f compose.yaml ps
~~~

Then verify:

~~~bash
curl -fsS https://$SDEA_DOMAIN/healthz
curl -fsS https://$SDEA_DOMAIN/readyz
~~~

The liveness endpoint is dependency-free. Readiness requires PostgreSQL and Valkey.

## Release flow

GitHub Actions builds and publishes the container on pushes to main and version tags.

The VPS deployment is intentionally pull-based:

~~~text
GitHub main
   |
   v
CI: tests + container build
   |
   v
GHCR image
   |
   v
VPS: docker compose pull
   |
   v
docker compose up -d
~~~

Deployment:

~~~bash
cd /opt/tinlance-sdea
git pull --ff-only origin main
cd deploy
docker compose pull
docker compose up -d
docker compose ps
~~~

## Rollback

Pin both the API and worker to a known previous image tag in a temporary Compose override and redeploy.

Do not roll back a database schema blindly. Schema changes must be backward-compatible before a release is promoted.

## Backups and disaster recovery

The VPS is not the only copy of production data.

Required operating policy:

- daily PostgreSQL logical backup
- encrypted off-host retention
- documented restore procedure
- periodic restore verification
- separate backup credentials
- retention aligned with SDEA governance policy

A Docker volume on the same VPS is not disaster recovery.

## Scaling path

### Stage 1

- one VPS
- one API container
- one worker
- PostgreSQL
- Valkey
- Caddy

### Stage 2

- managed PostgreSQL
- external object storage
- separate worker capacity
- external monitoring
- off-host backups

### Stage 3

- multiple API replicas
- multiple workers
- managed queue
- managed PostgreSQL
- object storage
- multi-zone deployment if justified

Do not introduce Kubernetes until actual operational requirements justify it.

## Runtime boundary

The service layer is separate from SDEA's domain contracts. API, queue, database and deployment concerns must not become a second semantic authority.

The current worker is deliberately fail-closed. It accepts only structured JSON job envelopes and rejects unsupported job types. It does not execute arbitrary Python or pretend that domain ingestion handlers exist before their persistence and execution contracts are implemented and tested.

This means this deployment branch establishes the production runtime substrate without falsely claiming that source ingestion, persistence repositories, or inference jobs are already production-complete.

## Security boundary

Agent Platform remains authoritative for identity, authorization, approvals, tool access, sandboxing, budgets and governed execution.

SDEA HTTP endpoints, queue messages, PostgreSQL and Valkey are not authorization boundaries.
