#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB"<<-EOSQL
	CREATE USER appuser;
	CREATE DATABASE application;
	GRANT ALL PRIVILEGES ON DATABASE application TO appuser;
EOSQL