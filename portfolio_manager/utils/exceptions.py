from fastapi import HTTPException, status

CredentialsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

NotFoundUserException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Not found user",
    headers={"WWW-Authenticate": "Bearer"},
)

AdminPermissionException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Not valid permissions",
    headers={"WWW-Authenticate": "Bearer"},
)
