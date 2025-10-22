# GmCapsule Docker

[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.13-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-BSD--2--Clause-orange.svg)](LICENSE)
[![Gemini](https://img.shields.io/badge/Protocol-Gemini%20%26%20Titan-purple.svg)](https://geminiprotocol.net/)

A Docker container for [GmCapsule](https://git.skyjake.fi/gemini/gmcapsule/), an extensible Gemini and Titan protocol server written in Python by skyjake (developer of the Lagrange browser).

## Features

- ✨ **Gemini Protocol** - Full support for the Gemini protocol (TLS 1.2/1.3)
- 📤 **Titan Protocol** - File upload support via Titan
- 🐍 **Python Extensions** - Extensible via Python modules
- 🔒 **Secure** - Runs as non-root user with read-only filesystem
- 🚀 **Lightweight** - Based on Alpine Linux (~52MB base image)
- 🔧 **CGI Support** - Dynamic content generation via CGI scripts
- 📁 **Static Files** - Simple static file serving
- 🔐 **Auto TLS** - Automatic self-signed certificate generation

## Quick Start

### Prerequisites

- Docker
- Docker Compose (optional)

### Using Docker Compose (Recommended)

```
# Clone the repository
git clone https://github.com/Smeeth/gmcapsule-Docker.git
cd gmcapsule-Docker

# Start the container
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the container
docker-compose down
```

### Using Docker CLI

```
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

## Accessing Your Capsule

Use a Gemini browser to access your capsule:

- [Lagrange](https://gmi.skyjake.fi/lagrange/) (Desktop)
- [Amfora](https://github.com/makeworld-the-better-one/amfora) (Terminal)
- [Kristall](https://github.com/MasterQ32/kristall) (Desktop)

Navigate to:
```
gemini://localhost/
```

Or test with OpenSSL:
```
echo "gemini://localhost/" | openssl s_client -connect localhost:1965 -quiet 2>/dev/null
```

## Directory Structure

```
gmcapsule-Docker/
├── Dockerfile              # Container definition
├── docker-compose.yml      # Compose configuration
├── README.md               # This file
├── LICENSE                 # BSD-2-Clause License
├── .gitignore             # Git ignore rules
├── .dockerignore          # Docker ignore rules
├── config/
│   └── config.ini         # Server configuration
├── content/               # Static content (*.gmi files)
│   ├── index.gmi         # Homepage
│   └── about.gmi         # About page
├── cgi-bin/              # CGI scripts (optional)
│   └── localhost/
│       └── hello.py      # Example CGI script
└── modules/              # Python extensions (optional)
    └── 50_custom.py      # Example module
```

## Configuration

Edit `config/config.ini` to customize your server:

```
[server]
hostname = localhost        # Your domain name
port = 1965                # Gemini port
certs = /srv/gemini/certs  # Certificate path

[static]
root = /srv/gemini/content # Content directory
index = index.gmi          # Index file

[cgi]
bin_root = /srv/gemini/cgi-bin  # CGI directory (optional)
```

## Writing Gemini Content

Create `.gmi` (gemtext) files in the `content/` directory:

```
# Welcome to My Capsule

This is a paragraph of text.

## Links

=> about.gmi About Me
=> https://example.com External Link

## Lists

* First item
* Second item
* Third item

> This is a quote
```

## CGI Scripts

Create executable Python scripts in `cgi-bin/localhost/`:

```
#!/usr/bin/env python3
import os

# Gemini response header
print("20 text/gemini\r")

# Content
print("# Hello from CGI")
print()
print("Client cert:", os.getenv('REMOTE_IDENT', 'none'))
```

Make it executable:
```
chmod +x cgi-bin/localhost/script.py
```

## Python Extensions

Create custom modules in `modules/`:

```
def init(capsule):
    """Extension module initialization"""
    capsule.add('/custom', custom_handler)

def custom_handler(req):
    return "20 text/gemini\r\n# Custom Response\n\nHello!"
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PYTHONUNBUFFERED` | `1` | Unbuffered Python output |
| `TZ` | `Europe/Berlin` | Timezone |

## Volumes

| Path | Purpose | Mode |
|------|---------|------|
| `/etc/gmcapsule/config.ini` | Configuration file | ro |
| `/srv/gemini/content` | Static content | ro |
| `/srv/gemini/cgi-bin` | CGI scripts | ro |
| `/srv/gemini/modules` | Python extensions | ro |
| `/srv/gemini/certs` | TLS certificates | rw |

## Security

- Runs as non-root user (`gemini:gemini`, UID/GID 1000)
- Read-only root filesystem
- No new privileges
- Resource limits enforced
- Automatic health checks

## Health Checks

The container includes automatic health monitoring:

```
# Check health status
docker inspect gmcapsule | grep -A5 Health
```

## Troubleshooting

### Container won't start

```
# Check logs
docker-compose logs gmcapsule

# Verify port availability
netstat -tuln | grep 1965
```

### Permission issues

Ensure CGI scripts are executable:
```
chmod +x cgi-bin/localhost/*.py
```

### Certificate errors

Certificates are auto-generated on first start. To regenerate:
```
docker-compose down -v  # Remove volumes
docker-compose up -d    # Start fresh
```

## Performance

- **Memory**: ~128MB typical, 256MB limit
- **CPU**: 0.25 cores reserved, 1.0 core limit
- **Startup**: ~2-3 seconds
- **Connections**: Limited by Python asyncio

## Building from Source

```
# Clone repository
git clone https://github.com/Smeeth/gmcapsule-Docker.git
cd gmcapsule-Docker

# Build image
docker build -t gmcapsule:custom .

# Tag for registry
docker tag gmcapsule:custom your-registry/gmcapsule:latest
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Related Projects

- [GmCapsule](https://git.skyjake.fi/gemini/gmcapsule/) - The original server
- [Lagrange](https://gmi.skyjake.fi/lagrange/) - Gemini browser by the same author
- [Awesome Gemini](https://github.com/kr1sp1n/awesome-gemini) - Curated Gemini resources

## License

- **GmCapsule**: BSD-2-Clause License (see [upstream](https://git.skyjake.fi/gemini/gmcapsule/))
- **Docker Setup**: BSD-2-Clause License (see [LICENSE](LICENSE))

## Links

- 📖 [GmCapsule Documentation](https://geminispace.org/gmcapsule/)
- 🌐 [Gemini Protocol](https://geminiprotocol.net/)
- 🐋 [Docker Hub](https://hub.docker.com/) (if published)
- 💬 [Issues](https://github.com/Smeeth/gmcapsule-Docker/issues)

## Acknowledgments

- **skyjake** - For creating GmCapsule and Lagrange
- **Gemini community** - For the excellent protocol and ecosystem

---

Made with ❤️ for the small internet
```
