Task for this project: https://darkstoreapp.notion.site/Portfolio-Manager-API-Python-3f79ed6c559e4ef8ba6246108a76f3b0

For running localy need do several steps: 

- create env files in folder .provisions/secrets:
    1. First file is envs for database:
        > POSTGRES_USER
        > POSTGRES_PASSWORD
        > POSTGRES_DB
    2. Second file is env for fastapi application:
        > JWT_TOKEN, default is your-256-bit-secret
        > JWT_ALGORITM, default is HS256
        > FINHUB_API_KEY

- run command `make build`

- run command `make up`