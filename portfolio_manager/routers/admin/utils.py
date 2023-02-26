from fastapi import Depends
from typing import Union
from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError
from settings.constants import JWTSettings

from utils.exceptions import CredentialsException, AdminPermissionException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def admin_routers(token: str = Depends(oauth2_scheme)) -> None:
    try:
        payload = jwt.decode(token, JWTSettings.SECRET_KEY, algorithms=[JWTSettings.ALGORITHM])
    except JWTError:
        raise CredentialsException

    username: Union[str, None] = payload.get("name")

    if not username == "admin":
        raise AdminPermissionException
