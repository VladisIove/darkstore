from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise

from settings.constants import DATABASE_CONFIG


def orm_register(app: FastAPI) -> None:
    register_tortoise(app, DATABASE_CONFIG)
