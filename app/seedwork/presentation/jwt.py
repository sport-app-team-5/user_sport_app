from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.config.env import env

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 7
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")


def create_access_token(data: dict, expires_delta: timedelta = timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)) -> str:
    _data_to_encode = data.copy()
    _expire = datetime.utcnow() + expires_delta
    _data_to_encode.update({"exp": _expire})

    return encode_token(_data_to_encode)


def encode_token(data_to_encode: dict) -> str:
    try:
        return jwt.encode(data_to_encode, env.SECRET_KEY, algorithm=ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')


def decode_token(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        return jwt.decode(token, env.SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')
