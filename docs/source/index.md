Hier ist eine vollständige ReadTheDocs-Dokumentation für dein Repository:

## 1. `.readthedocs.yaml` (Root des Repositories)

```yaml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the OS, Python version and other tools
build:
  os: ubuntu-24.04
  tools:
    python: "3.13"
  jobs:
    post_checkout:
      # Cancel building pull requests when a newer commit is pushed
      - |
        if [ "$READTHEDOCS_VERSION_TYPE" = "external" ] && git show-ref --quiet --verify "refs/remotes/origin/$READTHEDOCS_VERSION"; then
          git fetch origin --force "$READTHEDOCS_VERSION:$READTHEDOCS_VERSION"
          if [ "$READTHEDOCS_GIT_COMMIT_HASH" != "$(git rev-parse HEAD)" ]; then
            echo "Newer commit found, stopping build"
            exit 183
          fi
        fi

# Build documentation in the docs/ directory with Sphinx
sphinx:
  configuration: docs/source/conf.py
  builder: html
  fail_on_warning: false

# Optionally build your docs in additional formats
formats:
  - pdf
  - epub

# Python requirements to build docs
python:
  install:
    - requirements: docs/requirements.txt
```

## 2. `docs/requirements.txt`

```txt
sphinx>=7.0.0
sphinx-rtd-theme>=2.0.0
myst-parser>=2.0.0
sphinx-copybutton>=0.5.2
sphinx-autobuild>=2024.0.0
sphinxcontrib-mermaid>=0.9.2
sphinx-tabs>=3.4.5
```

## 3. `docs/source/conf.py`

```python
# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------
project = 'GmCapsule Docker'
copyright = f'2025, Eibo Richter'
author = 'Eibo Richter'
release = '1.0.0'
version = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',              # Markdown support
    'sphinx.ext.autodoc',       # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',      # Google/NumPy docstring style
    'sphinx.ext.viewcode',      # Add links to source code
    'sphinx.ext.intersphinx',   # Link to other project's documentation
    'sphinx.ext.todo',          # Support for todo items
    'sphinx_copybutton',        # Add copy button to code blocks
    'sphinxcontrib.mermaid',    # Mermaid diagram support
    'sphinx_tabs.tabs',         # Tabbed content
]

# MyST Parser configuration
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "substitution",
    "tasklist",
]

# Source files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document
master_doc = 'index'

# Templates
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = None
html_favicon = None

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Custom CSS
html_css_files = [
    'custom.css',
]

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
}

latex_documents = [
    (master_doc, 'gmcapsule-docker.tex', 'GmCapsule Docker Documentation',
     author, 'manual'),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    (master_doc, 'gmcapsule-docker', 'GmCapsule Docker Documentation',
     [author], 1)
]

# -- Options for Epub output -------------------------------------------------
epub_title = project
epub_exclude_files = ['search.html']

# -- Intersphinx configuration -----------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'docker': ('https://docker-py.readthedocs.io/en/stable/', None),
}

# -- Extension configuration -------------------------------------------------
todo_include_todos = True
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
```

## 4. `docs/source/index.md`

```markdown
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

## Next Steps

- [Quick Start Guide](quickstart.md)
- [Configuration](configuration.md)
- [Usage Examples](usage.md)
```

## 6. `docs/source/quickstart.md`

```markdown
# Quick Start Guide

Get your GmCapsule server up and running in 5 minutes.

## Step 1: Create Directory Structure

```
mkdir -p gmcapsule/{config,content,cgi-bin,modules}
cd gmcapsule
```

## Step 2: Create Configuration File

Create `config/config.ini`:

```
[server]
hostname = localhost
port = 1965
certs = /srv/gemini/certs

[static]
root = /srv/gemini/content
index = index.gmi
charset = UTF-8
```

## Step 3: Create Your First Gemtext Page

Create `content/index.gmi`:

```
# Welcome to My Gemini Capsule

This is my first page on the small internet!

## About Me

I'm exploring the Gemini protocol, a lightweight alternative to the web.

## Links

=> about.gmi About This Capsule
=> gemini://geminiprotocol.net/ Learn More About Gemini
```

## Step 4: Start the Server

Using Docker:

```
docker run -d \
  --name gmcapsule \
  -p 1965:1965 \
  -v $(pwd)/config:/etc/gmcapsule:ro \
  -v $(pwd)/content:/srv/gemini/content:ro \
  ghcr.io/smeeth/gmcapsule-docker:latest
```

Or using Docker Compose:

```
docker-compose up -d
```

## Step 5: Access Your Capsule

### Using a Gemini Browser

Download a Gemini browser:

- **[Lagrange](https://gmi.skyjake.fi/lagrange/)** (Recommended)
- **[Amfora](https://github.com/makeworld-the-better-one/amfora)** (Terminal)
- **[Kristall](https://github.com/MasterQ32/kristall)** (Desktop)

Navigate to:
```
gemini://localhost/
```

### Using OpenSSL (Testing)

```
echo "gemini://localhost/" | openssl s_client -connect localhost:1965 -quiet 2>/dev/null
```

## What's Next?

- Learn about [Gemtext syntax](gemtext.md)
- Add [CGI scripts](cgi-scripts.md) for dynamic content
- Explore [Python extensions](extensions.md)
- Configure for [production deployment](deployment.md)
```

## 7. `docs/source/_static/custom.css`

```css
/* Custom styles for GmCapsule Docker documentation */

:root {
    --gemini-purple: #8b4d8e;
    --docker-blue: #2496ed;
}

/* Better code block styling */
.highlight {
    border-left: 3px solid var(--docker-blue);
    padding-left: 1em;
}

/* Admonition styling */
.admonition {
    border-left: 4px solid var(--gemini-purple);
}

/* Better table styling */
table.docutils {
    border: none;
    border-collapse: collapse;
}

table.docutils th {
    background-color: var(--docker-blue);
    color: white;
}

/* Code button styling */
button.copybtn {
    background-color: var(--docker-blue);
}

