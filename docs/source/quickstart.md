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
