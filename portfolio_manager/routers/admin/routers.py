from fastapi import APIRouter, Depends
from routers.user.models import User

from utils.jwt import get_current_user

from routers.admin.utils import admin_routers

router = APIRouter(
    prefix="/admin",
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(admin_routers)],
)


@router.get("/clear_all")
async def clear_all(user: User = Depends(get_current_user)):
    await User.all().delete()
    return {"detail": "All data deleted"}
