# Tusa budget

## Requirements

* python == 3.9
* req.txt

## Run

1. Run locally (`uvicorn`):

    `make run`

2. Run with db (`Postgres`)

    `docker compose --env-file ./dev.env up` or `make compose-up`

    Note:
        Don't forget to fill in corresponding values found in `example.env` (I suggest creating new file and naming it `dev.env`)

## Docs

### Ideas

1. Notifications to send money

### User Flow

![User Flow diagram](./docs/userflow.jpg "User Flow diagram")