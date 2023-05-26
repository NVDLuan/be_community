from datetime import datetime
from datetime import timedelta

import jwt
from passlib.context import CryptContext

from app.core.settings import settings
from app.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(user: User) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds=settings.EXPIRE_TOKEN
    )
    data = dict(uid=user.id, exp=expire, email=user.email, token_type="access")
    return jwt.encode(data, settings.SECRET_KEY, algorithm="HS256")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
