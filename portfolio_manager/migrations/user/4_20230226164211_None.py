from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "created" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE "users" IS 'User model';
CREATE TABLE IF NOT EXISTS "positions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "currency" VARCHAR(20) NOT NULL,
    "amount" DOUBLE PRECISION NOT NULL,
    "created_dt" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "created" DATE NOT NULL,
    "updated" DATE NOT NULL,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "positions" IS 'User portfolio of cryptocurrency';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
