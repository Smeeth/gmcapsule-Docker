# GmCapsule Docker Documentation

Welcome to the GmCapsule Docker documentation. This guide will help you deploy and manage a [GmCapsule](https://git.skyjake.fi/gemini/gmcapsule/) server using Docker containers.

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-BSD--2--Clause-green)](https://github.com/Smeeth/gmcapsule-Docker/blob/main/LICENSE)

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
