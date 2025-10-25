# GmCapsule Docker Documentation

Welcome to the GmCapsule Docker documentation. This guide will help you deploy and manage a [GmCapsule](https://git.skyjake.fi/gemini/gmcapsule/) server using Docker containers.

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-BSD--2--Clause-green)](https://github.com/Smeeth/gmcapsule-Docker/blob/main/LICENSE)

## What is GmCapsule?

GmCapsule is an extensible server for the [Gemini protocol](https://geminiprotocol.net/), written in Python by skyjake (developer of the Lagrange browser). It supports:

- **Gemini Protocol** – Lightweight, privacy-focused protocol
- **Titan Protocol** – File upload extension
- **CGI Support** – Dynamic content generation
- **Python Extensions** – Modular architecture

## What is this Docker Container?

This project provides a production-ready Docker container for GmCapsule with:

- ✅ Multi-architecture support (AMD64, ARM64)
- ✅ Security hardened (non-root user, read-only filesystem)
- ✅ Automatic TLS certificate generation
- ✅ Health checks and monitoring
- ✅ Easy configuration and deployment

## Quick Start

Get started in minutes:

1. **Pull the image**:  
   ```
   docker pull ghcr.io/smeeth/gmcapsule-docker:latest
   ```
2. **Create configuration**: See our [Quick Start Guide](quickstart.md)
3. **Run the container**:  
   ```
   docker compose up -d
   ```
4. **Access your capsule**: Connect with a Gemini browser.

```
New to Gemini? Check out our [Quick Start Guide](quickstart.md) for a step-by-step walkthrough.
```

## Documentation

```
:maxdepth: 2
:caption: Getting Started

quickstart
installation
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
:caption: Advanced Topics

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

## Quick Links

::::{grid} 2
:gutter: 3

:::{grid-item-card} 🚀 Quick Start
:link: quickstart
:link-type: doc

Get your server running in 5 minutes
:::

:::{grid-item-card} ⚙️ Configuration
:link: configuration
:link-type: doc

Complete configuration reference
:::

:::{grid-item-card} 📖 User Guide
:link: usage
:link-type: doc

Learn how to use GmCapsule
:::

:::{grid-item-card} 🐛 Troubleshooting
:link: troubleshooting
:link-type: doc

Common issues and solutions
:::

::::

## Project Links

- [📦 GitHub Repository](https://github.com/Smeeth/gmcapsule-Docker)
- [🐳 Docker Hub](https://hub.docker.com/r/smeeth/gmcapsule-docker)
- [🌐 GmCapsule Upstream](https://git.skyjake.fi/gemini/gmcapsule/)
- [💬 Report Issues](https://github.com/Smeeth/gmcapsule-Docker/issues)

## Indices and Tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`
