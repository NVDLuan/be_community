from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.schemas.user import UserInfo


class RecommentBase(BaseModel):
    id: Optional[str] = None
    id_user: Optional[str] = None
    id_cmt: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None
    time_create: Optional[datetime] = None

    class Config:
        orm_mode = True


class RecommentCreate(RecommentBase):
    pass


class RecommentUpdate(RecommentBase):
    pass


class RecommentResponse(BaseModel):
    id: Optional[str] = None
    user: Optional[UserInfo]= None
    id_cmt: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None
    time_create: Optional[datetime] = None

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True