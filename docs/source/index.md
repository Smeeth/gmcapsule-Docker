# GmCapsule Docker Documentation

Welcome to the GmCapsule Docker documentation. This guide will help you deploy and manage a [GmCapsule](https://git.skyjake.fi/gemini/gmcapsule/) server using Docker containers.

```
:target: https://www.docker.com/
:alt: Docker
```

```
:target: https://www.python.org/
:alt: Python
```

```
:target: https://github.com/Smeeth/gmcapsule-Docker/blob/main/LICENSE
:alt: License
```

## What is GmCapsule?

GmCapsule is an extensible server for the [Gemini protocol](https://geminiprotocol.net/), written in Python by skyjake (developer of the Lagrange browser). It supports:

- **Gemini Protocol** - Lightweight, privacy-focused protocol
- **Titan Protocol** - File upload extension
- **CGI Support** - Dynamic content generation
- **Python Extensions** - Modular architecture

## What is this Docker Container?

This project provides a production-ready Docker container for GmCapsule with:

- ✅ Multi-architecture support (AMD64, ARM64)
- ✅ Security hardened (non-root user, read-only filesystem)
- ✅ Automatic TLS certificate generation
- ✅ Health checks and monitoring
- ✅ Easy configuration and deployment

## Quick Links

- [Installation Guide](installation.md)
- [Configuration Reference](configuration.md)
- [Usage Examples](usage.md)
- [Troubleshooting](troubleshooting.md)
- [GitHub Repository](https://github.com/Smeeth/gmcapsule-Docker)

## Table of Contents

```
:maxdepth: 2
:caption: Getting Started

installation
quickstart
configuration
```

```
:maxdepth: 2
:caption: User Guide

usage
gemtext
cgi-scripts
extensions
```

```
:maxdepth: 2
:caption: Advanced

security
deployment
monitoring
troubleshooting
```

```
:maxdepth: 2
:caption: Reference

environment-variables
volumes
api-reference
```

```
:maxdepth: 1
:caption: Community

contributing
changelog
license
```

## Indices and tables

* {ref}`genindex`
* {ref}`modindex`
* {ref}`search`
```

## 5. `docs/source/installation.md`

```markdown
# Installation

This guide covers different ways to install and run GmCapsule Docker.

## Prerequisites

Before you begin, ensure you have:

- Docker Engine 20.10+ or Docker Desktop
- Docker Compose 2.0+ (optional but recommended)
- 256MB RAM minimum
- 1GB disk space

## Installation Methods

### Using Pre-built Images (Recommended)

Pull the latest image from GitHub Container Registry:

```
docker pull ghcr.io/smeeth/gmcapsule-docker:latest
```

Available architectures:
- `linux/amd64` (Intel/AMD 64-bit)
- `linux/arm64` (ARM 64-bit, Raspberry Pi 4/5, Apple Silicon)

### Using Docker Compose

1. Create a `docker-compose.yml` file:

```
version: '3.8'

services:
  gmcapsule:
    image: ghcr.io/smeeth/gmcapsule-docker:latest
    container_name: gmcapsule
    ports:
      - "1965:1965"
    volumes:
      - ./config:/etc/gmcapsule:ro
      - ./content:/srv/gemini/content:ro
      - ./cgi-bin:/srv/gemini/cgi-bin:ro
      - ./modules:/srv/gemini/modules:ro
      - gmcapsule-certs:/srv/gemini/certs
    restart: unless-stopped

volumes:
  gmcapsule-certs:
```

2. Start the container:

```
docker-compose up -d
```

### Building from Source

1. Clone the repository:

```
git clone https://github.com/Smeeth/gmcapsule-Docker.git
cd gmcapsule-Docker
```

2. Build the image:

```
docker build -t gmcapsule:local .
```

3. Run the container:

```
docker run -d \
  --name gmcapsule \
  -p 1965:1965 \
  -v $(pwd)/config:/etc/gmcapsule:ro \
  -v $(pwd)/content:/srv/gemini/content:ro \
  gmcapsule:local
```

## Verifying Installation

Check if the container is running:

```
docker ps | grep gmcapsule
```

View container logs:

```
docker logs gmcapsule
```

Test the Gemini connection:

```
echo "gemini://localhost/" | openssl s_client -connect localhost:1965 -quiet 2>/dev/null
```
