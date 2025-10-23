# Multi-Stage Build für kleineres Image
FROM python:3.14-alpine AS builder

# Build-Dependencies
RUN apk add --no-cache \
    build-base \
    openssl

# GmCapsule installieren
RUN pip install --no-cache-dir --user gmcapsule

# Runtime Stage
FROM python:3.14-alpine

# Runtime-User (non-root für Sicherheit)
RUN addgroup -g 1000 gemini && \
    adduser -D -u 1000 -G gemini gemini

# Python-Module von Builder kopieren
COPY --from=builder /root/.local /home/gemini/.local

# Arbeitsverzeichnis
WORKDIR /srv/gemini

# Verzeichnisstruktur
RUN mkdir -p \
    /srv/gemini/content \
    /srv/gemini/cgi-bin \
    /srv/gemini/modules \
    /srv/gemini/certs \
    /etc/gmcapsule && \
    chown -R gemini:gemini /srv/gemini /etc/gmcapsule

# PATH für pip-installierte Packages
ENV PATH=/home/gemini/.local/bin:$PATH

# Volumes für persistente Daten
VOLUME ["/srv/gemini/content", "/srv/gemini/cgi-bin", "/srv/gemini/modules", "/srv/gemini/certs", "/etc/gmcapsule"]

# Gemini-Port exponieren
EXPOSE 1965

# Als non-root User wechseln
USER gemini

# Health Check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import socket; s=socket.socket(); s.settimeout(2); s.connect(('localhost', 1965)); s.close()" || exit 1

# Entrypoint
ENTRYPOINT ["gmcapsuled"]
CMD ["--config", "/etc/gmcapsule/config.ini"]
