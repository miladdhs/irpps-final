#!/bin/sh
set -eu

BACKUP_DIR="${BACKUP_DIR:-/backups/mysql}"
INTERVAL_HOURS="${BACKUP_INTERVAL_HOURS:-168}"
RETENTION_COUNT="${BACKUP_RETENTION_COUNT:-12}"
DB_HOST="${DB_HOST:-mysql}"
DB_PORT="${DB_PORT:-3306}"
DB_NAME="${DB_NAME:?DB_NAME is required}"
DB_USER="${DB_USER:?DB_USER is required}"
DB_PASSWORD="${DB_PASSWORD:?DB_PASSWORD is required}"

mkdir -p "${BACKUP_DIR}"

wait_for_mysql() {
  until mysqladmin ping \
    -h"${DB_HOST}" \
    -P"${DB_PORT}" \
    -u"${DB_USER}" \
    -p"${DB_PASSWORD}" \
    --silent; do
    echo "Waiting for MySQL at ${DB_HOST}:${DB_PORT}..."
    sleep 5
  done
}

create_backup() {
  timestamp="$(date +"%Y-%m-%d_%H-%M-%S")"
  filename="${BACKUP_DIR}/${DB_NAME}_${timestamp}.sql.gz"

  echo "Creating backup: ${filename}"
  mysqldump \
    -h"${DB_HOST}" \
    -P"${DB_PORT}" \
    -u"${DB_USER}" \
    -p"${DB_PASSWORD}" \
    --single-transaction \
    --quick \
    --routines \
    --events \
    --triggers \
    --default-character-set=utf8mb4 \
    "${DB_NAME}" | gzip -c > "${filename}"

  old_files="$(ls -1t "${BACKUP_DIR}/${DB_NAME}_"*.sql.gz 2>/dev/null | tail -n +"$((RETENTION_COUNT + 1))" || true)"
  if [ -n "${old_files}" ]; then
    echo "${old_files}" | while IFS= read -r old_file; do
      rm -f "${old_file}"
    done
  fi
  echo "Backup completed."
}

sleep_seconds=$((INTERVAL_HOURS * 3600))

wait_for_mysql

while true; do
  create_backup
  sleep "${sleep_seconds}"
done
