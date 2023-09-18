# first of all let's build js
FROM node:18.17.1 as frontend_build

WORKDIR /src

COPY package*.json /src/

RUN npm i

COPY . /src/

RUN npm run build

FROM python:3.9-alpine as prod

WORKDIR /src
COPY req.txt /src/

RUN apk update --no-cache \
    && apk add build-base postgresql-dev libpq --no-cache --virtual .build-deps \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r req.txt \
    && apk del .build-deps

COPY . /src
COPY --from=frontend_build /src/backend/src/dist /src/backend/src/dist

COPY <<EOF alembic.ini
# A generic, single database configuration.

[alembic]
script_location = migrations
prepend_sys_path = .
version_path_separator = os  # Use os.pathsep. Default configuration used for new projects.

sqlalchemy.url = sqlite:///./db/dev.sqlite

[loggers]
keys = root,sqlalchemy,alembic
[handlers]
keys = console
[formatters]
keys = generic
[logger_root]
level = WARN
handlers = console
qualname =
[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine
[logger_alembic]
level = INFO
handlers =
qualname = alembic
[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic
[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
EOF

RUN mkdir db \
    && alembic upgrade head

# # application start
CMD [ "uvicorn", "--factory", "backend.src.main:app_factory", \
     "--host", "0.0.0.0", "--port", "3000", "--log-level", "info" ]