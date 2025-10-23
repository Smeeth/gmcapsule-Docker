# GmCapsule Docker

[![GitHub Actions](https://github.com/Smeeth/gmcapsule-Docker/workflows/Build%20and%20Push%20Docker%20Image/badge.svg)](https://github.com/Smeeth/gmcapsule-Docker/actions)
[![License](https://img.shields.io/badge/License-BSD--2--Clause-orange.svg)]
[![Python](https://img.shields.io/badge/Python-3.13-green.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Protocol-Gemini%20%26%20Titan-purple.svg)](https://geminiprotocol.net/)

A production-ready Docker container for [GmCapsule](https://git.skyjake.fi/gemini/gmcapsule/), an extensible Gemini and Titan protocol server written in Python by [skyjake](https://skyjake.fi/) (developer of the Lagrange browser).

## ✨ Features

- 🌐 **Gemini Protocol** - Full support for Gemini protocol (TLS 1.2/1.3)
- 📤 **Titan Protocol** - File upload support via Titan
- 🐍 **Python Extensions** - Extensible via Python modules
- 🔒 **Secure** - Non-root user, read-only filesystem, signed images
- 🚀 **Lightweight** - Alpine Linux based (~52MB compressed)
- 🏗️ **Multi-Architecture** - Native support for AMD64 and ARM64
- 🔧 **CGI Support** - Dynamic content generation via CGI scripts
- 📁 **Static Files** - Simple static file serving
- 🔐 **Auto TLS** - Automatic self-signed certificate generation
- 📊 **Health Checks** - Built-in container health monitoring

## 🚀 Quick Start

### Using Pre-built Image (Recommended)

```
# Pull from GitHub Container Registry
docker pull ghcr.io/smeeth/gmcapsule-docker:latest

# Run the container
docker run -d \
  --name gmcapsule \
  -p 1965:1965 \
  -v $(pwd)/config:/etc/gmcapsule:ro \
  -v $(pwd)/content:/srv/gemini/content:ro \
  ghcr.io/smeeth/gmcapsule-docker:latest
```

### Using Docker Compose

Create a `docker-compose.yml`:

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
    healthcheck:
      test: ["CMD", "python3", "-c", "import socket; s=socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(('localhost', 1965)); s.close()"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  gmcapsule-certs:
```

Then run:

```
docker-compose up -d
```

### Building from Source

```
# Clone the repository
git clone https://github.com/Smeeth/gmcapsule-Docker.git
cd gmcapsule-Docker

# Build the image
docker build -t gmcapsule:latest .

# Run the container
docker run -d \
  --name gmcapsule \
  -p 1965:1965 \
  -v $(pwd)/config:/etc/gmcapsule:ro \
  -v $(pwd)/content:/srv/gemini/content:ro \
  gmcapsule:latest
```

## 🌐 Accessing Your Capsule

### Gemini Browsers

Use a Gemini browser to access your capsule:

- **[Lagrange](https://gmi.skyjake.fi/lagrange/)** - Beautiful GUI browser (Windows, macOS, Linux)
- **[Amfora](https://github.com/makeworld-the-better-one/amfora)** - Terminal-based browser
- **[Kristall](https://github.com/MasterQ32/kristall)** - Cross-platform GUI browser
- **[Castor](https://git.sr.ht/~julienxx/castor)** - GTK browser for Linux

Navigate to:
```
gemini://localhost/
```

### Testing with OpenSSL

```
# Test connection
echo "gemini://localhost/" | openssl s_client -connect localhost:1965 -quiet 2>/dev/null

# Test with custom port
echo "gemini://localhost/" | openssl s_client -connect localhost:1965 -ign_eof
```

## 📁 Directory Structure

```
gmcapsule-Docker/
├── .github/
│   ├── workflows/
│   │   ├── docker-build.yml      # Multi-arch build & publish
│   │   ├── security-scan.yml     # Trivy & Dockle scans
│   │   ├── dockerfile-lint.yml   # Hadolint checks
│   │   └── codeql.yml           # Python security analysis
│   └── dependabot.yml           # Automated updates
├── Dockerfile                   # Container definition
├── docker-compose.yml           # Compose configuration
├── README.md                    # This file
├── LICENSE                      # BSD-2-Clause License
├── SECURITY.md                  # Security policy
├── CONTRIBUTING.md              # Contribution guidelines
├── .gitignore                  # Git ignore rules
├── .dockerignore               # Docker ignore rules
├── .hadolint.yaml              # Dockerfile linting config
├── config/
│   └── config.ini              # Server configuration
├── content/                    # Static content (*.gmi files)
│   ├── index.gmi              # Homepage
│   └── about.gmi              # About page
├── cgi-bin/                   # CGI scripts (optional)
│   └── localhost/
│       └── hello.py           # Example CGI script
└── modules/                   # Python extensions (optional)
    └── 50_custom.py           # Example module
```

## ⚙️ Configuration

Edit `config/config.ini` to customize your server:

```
[server]
hostname = localhost              # Your domain name
port = 1965                      # Gemini port (default: 1965)
certs = /srv/gemini/certs        # Certificate path

[static]
root = /srv/gemini/content       # Content directory
index = index.gmi                # Index file
charset = UTF-8                  # Character encoding

[cgi]
bin_root = /srv/gemini/cgi-bin  # CGI directory (optional)
```

### Advanced Configuration

For production deployments, consider:

- Setting a custom `hostname` (your domain)
- Using Let's Encrypt certificates (mount to `/srv/gemini/certs`)
- Configuring reverse proxy (Traefik, Nginx) for external access
- Setting up logging and monitoring

## 📝 Writing Gemini Content

Create `.gmi` (gemtext) files in the `content/` directory:

```
# Welcome to My Capsule

This is a paragraph of text in gemtext format.

## Links

=> about.gmi About Me
=> gemini://example.com Another Capsule
=> https://example.com External Website

## Lists

* First item
* Second item
* Third item

## Preformatted Text

```
ASCII Art or Code
Goes Here
```

> This is a quote
```

### Gemtext Syntax Reference

- `# Heading` - Level 1 heading
- `## Heading` - Level 2 heading
- `### Heading` - Level 3 heading
- `=> URL Text` - Link
- `* Item` - List item
- `> Quote` - Quoted text
- ` ```

## 🔧 CGI Scripts

Create executable Python scripts in `cgi-bin/localhost/`:

```python
#!/usr/bin/env python3
import os
import sys
from datetime import datetime

# Gemini response header (MUST end with \r\n)
print("20 text/gemini\r")

# Content
print("# Hello from CGI")
print()
print(f"Current time: {datetime.now()}")
print(f"Client cert: {os.getenv('REMOTE_IDENT', 'none')}")
print(f"Request URL: {os.getenv('GEMINI_URL', 'unknown')}")
```

Make it executable:
```bash
chmod +x cgi-bin/localhost/script.py
```

### Available CGI Environment Variables

- `GEMINI_URL` - Full request URL
- `SCRIPT_NAME` - Script path
- `PATH_INFO` - Extra path info
- `QUERY_STRING` - Query string
- `REMOTE_IDENT` - Client certificate identifier
- `TLS_CIPHER` - TLS cipher used
- `TLS_VERSION` - TLS version

## 🐍 Python Extensions

Create custom modules in `modules/` (prefix with number for load order):

```python
# modules/50_custom.py

def init(capsule):
    """
    Extension module initialization
    Called when GmCapsule starts
    """
    capsule.add('/custom', custom_handler)
    capsule.add('/api', api_handler)
    print("[Extension] Custom module loaded")

def custom_handler(req):
    """Handle /custom requests"""
    return "20 text/gemini\r\n# Custom Response\n\nHello from extension!"

def api_handler(req):
    """Handle /api requests"""
    import json
    data = {"status": "ok", "message": "API works"}
    return f"20 application/json\r\n{json.dumps(data)}"
```

## 🌍 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PYTHONUNBUFFERED` | `1` | Unbuffered Python output |
| `TZ` | `Europe/Berlin` | Timezone for logs |
| `GMCAPSULE_PORT` | `1965` | Override default port |
| `GMCAPSULE_HOST` | `0.0.0.0` | Bind address |

## 💾 Volumes

| Path | Purpose | Mode | Notes |
|------|---------|------|-------|
| `/etc/gmcapsule/config.ini` | Configuration file | `ro` | Required |
| `/srv/gemini/content` | Static content | `ro` | Gemtext files |
| `/srv/gemini/cgi-bin` | CGI scripts | `ro` | Must be executable |
| `/srv/gemini/modules` | Python extensions | `ro` | Numbered .py files |
| `/srv/gemini/certs` | TLS certificates | `rw` | Auto-generated if missing |

## 🔒 Security Features

- ✅ **Non-root execution** - Runs as `gemini:gemini` (UID/GID 1000)
- ✅ **Read-only root filesystem** - Prevents container modification
- ✅ **No new privileges** - Security flag enabled
- ✅ **Resource limits** - Memory and CPU limits enforced
- ✅ **Health checks** - Automatic container health monitoring
- ✅ **Image signing** - Signed with Cosign
- ✅ **SBOM included** - Software Bill of Materials
- ✅ **Vulnerability scanning** - Trivy scans on every build
- ✅ **Provenance attestation** - Build provenance included

### Verifying Image Signature

```bash
# Install cosign
brew install cosign  # macOS
# or
apt install cosign   # Debian/Ubuntu

# Verify signature
cosign verify ghcr.io/smeeth/gmcapsule-docker:latest \
  --certificate-identity-regexp="https://github.com/Smeeth/gmcapsule-Docker" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```

## 🏥 Health Checks

The container includes automatic health monitoring:

```bash
# Check health status
docker inspect gmcapsule | grep -A5 Health

# View health check logs
docker inspect --format='{{json .State.Health}}' gmcapsule | jq
```

Health check runs every 30 seconds and verifies:
- Port 1965 is accepting connections
- Python process is running
- Container can respond to requests

## 🐛 Troubleshooting

### Container won't start

```bash
# Check logs
docker logs gmcapsule

# Check with docker-compose
docker-compose logs gmcapsule

# Verify port availability
netstat -tuln | grep 1965
# or
ss -tuln | grep 1965
```

### Permission issues

```bash
# Fix CGI script permissions
chmod +x cgi-bin/localhost/*.py

# Check file ownership
ls -la cgi-bin/localhost/

# Fix if needed (run as your user, not root)
chown -R 1000:1000 cgi-bin/
```

### Certificate errors

```bash
# Certificates are auto-generated on first start
# To regenerate:
docker-compose down -v  # Remove volumes
docker-compose up -d    # Start fresh

# Or manually with named volume:
docker volume rm gmcapsule-docker_gmcapsule-certs
```

### Connection refused

```bash
# Check if container is running
docker ps | grep gmcapsule

# Check port mapping
docker port gmcapsule

# Test from inside container
docker exec gmcapsule netstat -tuln | grep 1965
```

### Logs show errors

```bash
# View detailed logs
docker logs -f gmcapsule

# Check Python errors
docker exec gmcapsule python3 -c "import gmcapsule; print('OK')"
```

## 📊 Performance

### Resource Usage

- **Memory**: ~128MB typical, 256MB limit
- **CPU**: 0.25 cores reserved, 1.0 core limit  
- **Startup**: ~2-3 seconds
- **Image Size**: ~52MB compressed, ~140MB uncompressed
- **Connections**: Limited by Python asyncio (typically 1000+)

### Optimization Tips

- Use read-only volumes where possible
- Mount certificates volume for persistence
- Use Docker BuildKit cache for faster builds
- Consider using `--memory=256m --cpus=1` limits

## 🏗️ Multi-Architecture Support

Pre-built images are available for:

- **linux/amd64** - x86_64 (Intel/AMD)
- **linux/arm64** - ARM64 (Apple Silicon, Raspberry Pi 4/5, AWS Graviton)

Docker automatically pulls the correct architecture:

```bash
# On Raspberry Pi 4/5
docker pull ghcr.io/smeeth/gmcapsule-docker:latest

# On Apple Silicon Mac
docker pull ghcr.io/smeeth/gmcapsule-docker:latest

# On Intel/AMD
docker pull ghcr.io/smeeth/gmcapsule-docker:latest
```

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests: `docker build -t gmcapsule:test .`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

### Development Workflow

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/gmcapsule-Docker.git
cd gmcapsule-Docker

# Build locally
docker build -t gmcapsule:dev .

# Test
docker run -d --name gmcapsule-test -p 1965:1965 gmcapsule:dev

# Check logs
docker logs gmcapsule-test

# Clean up
docker stop gmcapsule-test && docker rm gmcapsule-test
```

## 📦 Related Projects

- [GmCapsule](https://git.skyjake.fi/gemini/gmcapsule/) - The original server
- [Lagrange](https://gmi.skyjake.fi/lagrange/) - Gemini browser by the same author
- [Awesome Gemini](https://github.com/kr1sp1n/awesome-gemini) - Curated Gemini resources
- [Gemini Protocol Specification](https://geminiprotocol.net/docs/specification.gmi)
- [Geminispace.info](https://geminispace.info/) - Gemini search engine

## 📚 Resources

### Documentation

- 📖 [GmCapsule Documentation](https://geminispace.org/gmcapsule/)
- 🌐 [Gemini Protocol](https://geminiprotocol.net/)
- 📝 [Gemtext Format](https://geminiprotocol.net/docs/gemtext.gmi)
- 🐋 [Docker Documentation](https://docs.docker.com/)

### Community

- 💬 [GitHub Issues](https://github.com/Smeeth/gmcapsule-Docker/issues)
- 🗣️ [Reddit /r/Gemini](https://reddit.com/r/geminiprotocol)

## 🔖 Version Tags

Images are tagged with multiple versions:

- `latest` - Latest stable release
- `v1.0.0` - Specific version
- `v1.0` - Minor version
- `v1` - Major version
- `main` - Latest main branch build
- `sha-abc1234` - Specific commit

```bash
# Pull specific version
docker pull ghcr.io/smeeth/gmcapsule-docker:v1.0.0

# Pull latest
docker pull ghcr.io/smeeth/gmcapsule-docker:latest
```

## 📜 License

- **GmCapsule**: BSD-2-Clause License (see [upstream](https://git.skyjake.fi/gemini/gmcapsule/))
- **Docker Setup**: BSD-2-Clause License (see [LICENSE](LICENSE))

## 🙏 Acknowledgments

- **[skyjake](https://skyjake.fi/)** - For creating GmCapsule and Lagrange
- **Gemini community** - For the excellent protocol and ecosystem
- **Contributors** - Everyone who has contributed to this project

## 📊 Project Status






***

<div align="center">

**Made with ❤️ for the small internet**

[Report Bug](https://github.com/Smeeth/gmcapsule-Docker/issues) · [Request Feature](https://github.com/Smeeth/gmcapsule-Docker/issues) · [Contribute](CONTRIBUTING.md)

</div>
