# Project api

---

* [Start local project](#Start-local-project)
    * [Create `.env`](#Create-env)
    * [docker containers up](#Docker-containers-up)
    * [Migrate db](#Migrate-db)

---

## Start local project

### Create env
To run the project, you need to create an `.env' file.
For convenience, the root of the project contains a file with an example `.env_example`.
You need to create an `.env` file that inherits the contents of the `.env_example` file.

### Docker containers up
Run command in shell:

```shell
docker-compose up -d --build app
```

### Migrate db

Run command in shell:
```shell
python app/manage.py migrate
```

