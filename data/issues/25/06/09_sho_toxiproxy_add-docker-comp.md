issue title: Add docker compose sample
labels: none
comment count: 0
hyperlink: https://github.com/shopify/toxiproxy/issues/647
status: open
date opened: 2025-06-09
repo 30d_merge_rate: 7

====

description:
I think that a docker compose sample for simple scenarios would be useful for those who are trying to create a simple configuration for testing. My final sample for fixed toxics is like below, but possibly something even simpler could be created.

```
services:
  db:
    container_name: sample_postgres_container
    image: postgres:17.5
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-postgres}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-postgres}
      POSTGRES_DB: sample
      PGDATA: /data/postgres
    volumes:
       - sample_postgres:/data/postgres
    ports:
      - "5433:5432"
    networks:
      - sample_postgres
  toxiproxy:
    container_name: sample_toxiproxy_container
    image: ghcr.io/shopify/toxiproxy:2.12.0
    links:
      - db
    ports:
      - "8474:8474"
      - "5434:5434"
    environment:
      LOG_LEVEL: info
    networks:
      - sample_postgres
    post_start:
      - command: "/toxiproxy-cli create -l 0.0.0.0:5434 -u db:5432 postgres1ms"
      - command: "/toxiproxy-cli toxic add -t latency -a latency=1 postgres1ms"

networks:
  sample_postgres:
    driver: bridge

volumes:
    sample_postgres:
```

===
