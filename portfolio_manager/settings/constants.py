import os

FINHUB_API_KEY = os.getenv("FINHUB_API_KEY")


class JWTSettings:
    SECRET_KEY: str = os.getenv("JWT_TOKEN", "your-256-bit-secret")
    ALGORITHM: str = os.getenv("JWT_ALGORITM", "HS256")


POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

db_connection = f"asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}"

DATABASE_CONFIG = {
    "connections": {"default": db_connection},
    "apps": {
        "user": {
            "models": ["routers.user.models", "aerich.models"],
        },
    },
}
