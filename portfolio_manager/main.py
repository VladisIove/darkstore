from fastapi import FastAPI

from routers.user.routers import router as user_router
from routers.admin.routers import router as admin_router

from settings.register_tortoise import orm_register
from utils.init_default_users import init_default_users

app = FastAPI()
app.include_router(user_router)
app.include_router(admin_router)

# database
orm_register(app)


# events
@app.on_event("startup")
async def startup_event():
    await init_default_users()
