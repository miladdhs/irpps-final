FROM mysql:8.3.0

WORKDIR /opt/db-backup

COPY backup-loop.sh /opt/db-backup/backup-loop.sh

RUN chmod +x /opt/db-backup/backup-loop.sh

ENTRYPOINT ["/opt/db-backup/backup-loop.sh"]
