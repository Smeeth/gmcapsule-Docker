# syntax=docker/dockerfile:1.4

# =============================================================================
# GmCapsule - Gemini/Titan Protocol Server
# Multi-stage build for minimal and secure Docker image
# =============================================================================

# Build arguments
ARG PYTHON_VERSION=3.13
ARG ALPINE_VERSION=3.20
ARG GMCAPSULE_VERSION=0.3.2

# =============================================================================
# Builder Stage - Install dependencies
# =============================================================================
FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION} AS builder

# Build metadata
LABEL stage=builder

# Install build dependencies
RUN --mount=type=cache,target=/var/cache/apk \
    apk add --no-cache \
        build-base \
        openssl-dev

# Install GmCapsule with pinned version
ARG GMCAPSULE_VERSION
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir --user \
    gmcapsule==${GMCAPSULE_VERSION}

# =============================================================================
# Runtime Stage - Minimal production image
# =============================================================================
FROM python:${PYTHON_VERSION}-alpine${ALPINE_VERSION}

# Build arguments for labels
ARG GMCAPSULE_VERSION
ARG BUILD_DATE
ARG VCS_REF

# OCI Image Labels (https://github.com/opencontainers/image-spec)
LABEL org.opencontainers.image.title="GmCapsule Docker" \
      org.opencontainers.image.description="Extensible Gemini and Titan protocol server" \
      org.opencontainers.image.authors="Eibo Richter <eibo.richter@gmail.com>" \
      org.opencontainers.image.vendor="Smeeth" \
      org.opencontainers.image.licenses="BSD-2-Clause" \
      org.opencontainers.image.url="https://github.com/Smeeth/gmcapsule-Docker" \
      org.opencontainers.image.source="https://github.com/Smeeth/gmcapsule-Docker" \
      org.opencontainers.image.documentation="https://github.com/Smeeth/gmcapsule-Docker/blob/main/README.md" \
      org.opencontainers.image.version="${GMCAPSULE_VERSION}" \
      org.opencontainers.image.created="${BUILD_DATE}" \
      org.opencontainers.image.revision="${VCS_REF}"

# Custom labels
LABEL maintainer="Eibo Richter <eibo.richter@gmail.com>" \
      com.gmcapsule.version="${GMCAPSULE_VERSION}" \
      com.gmcapsule.protocol="gemini,titan" \
      com.gmcapsule.port="1965"

# Install runtime dependencies only
RUN --mount=type=cache,target=/var/cache/apk \
    apk add --no-cache \
        ca-certificates \
        openssl \
        tzdata && \
    # Create non-root user with explicit UID/GID
    addgroup -g 1000 gemini && \
    adduser -D -u 1000 -G gemini -h /home/gemini -s /bin/sh gemini

# Copy Python packages from builder
COPY --from=builder --chown=gemini:gemini /root/.local /home/gemini/.local

# Set working directory
WORKDIR /srv/gemini

# Create directory structure with proper permissions
RUN mkdir -p \
        /srv/gemini/content \
        /srv/gemini/cgi-bin \
        /srv/gemini/modules \
        /srv/gemini/certs \
        /etc/gmcapsule && \
    chown -R gemini:gemini \
        /srv/gemini \
        /etc/gmcapsule && \
    chmod 755 /srv/gemini/cgi-bin

# Environment variables
ENV PATH=/home/gemini/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    TZ=Europe/Berlin \
    LANG=C.UTF-8

# Define volumes
VOLUME ["/srv/gemini/content", "/srv/gemini/cgi-bin", "/srv/gemini/modules", "/srv/gemini/certs", "/etc/gmcapsule"]

# Expose Gemini port
EXPOSE 1965/tcp

# Switch to non-root user
USER gemini

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python3 -c "import socket; s=socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(2); s.connect(('127.0.0.1', 1965)); s.close()" || exit 1

# Entrypoint and command
ENTRYPOINT ["gmcapsuled"]
CMD ["--config", "/etc/gmcapsule/config.ini"]
