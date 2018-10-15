# coding: utf-8

ENV = 'local'

PARAMS = dict(
    DEBUG=True,

    POSTGRES_ENGINE='django.db.backends.postgresql_psycopg2',
    POSTGRES_DB='new_database1',
    POSTGRES_HOST='127.0.0.1',
    POSTGRES_USER='postgres',
    POSTGRES_PORT=5432,
    POSTGRES_PASSWORD='drainwhis',
    OPEN_EXCHANGE_RATE_URL='https://openexchangerates.org/api',
    OPEN_EXCHANGE_RATE_API_ID='d66916da559642bcb76f4b9bdad47f21',
    REDIS_URL="redis://localhost:6379/1"
)
