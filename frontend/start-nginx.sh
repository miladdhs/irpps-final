#!/bin/sh
set -eu

CERT_DIR=/etc/nginx/certs
CRT_FILE="$CERT_DIR/fullchain.pem"
KEY_FILE="$CERT_DIR/privkey.pem"

mkdir -p "$CERT_DIR"

if [ ! -s "$CRT_FILE" ] || [ ! -s "$KEY_FILE" ]; then
  openssl req -x509 -nodes -newkey rsa:2048 \
    -keyout "$KEY_FILE" \
    -out "$CRT_FILE" \
    -days 365 \
    -subj "/CN=irpps.org"
fi

exec nginx -g "daemon off;"
