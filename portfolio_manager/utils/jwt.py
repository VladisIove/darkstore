from typing import Union

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from routers.user.models import User
from settings.constants import JWTSettings
from utils.exceptions import CredentialsException, NotFoundUserException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, JWTSettings.SECRET_KEY, algorithms=[JWTSettings.ALGORITHM])
    except JWTError:
        raise CredentialsException

    username: Union[str, None] = payload.get("name")

    if username is None:
        raise CredentialsException

    user = await User.filter(name=username).first()
    if not user:
        return NotFoundUserException

    return user
