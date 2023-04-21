from datetime import date, datetime
from typing import Optional, List

from pydantic import BaseModel

from app.schemas.user import UserInfo


class CommentBase(BaseModel):
    id: Optional[str] = None
    id_post: Optional[str] = None
    content: Optional[str] = None
    image: Optional[str] = None

    class Config:
        orm_mode = True


class CommentCreate(CommentBase):
    id_user: Optional[str] = None


class CommentUpdate(CommentBase):
    pass


class CommentResponse(BaseModel):
    id: Optional[str] = None
    id_post: Optional[str] = None
    user: Optional[UserInfo] = None
    content: Optional[str] = None
    image: Optional[str] = None
    time_create: Optional[datetime] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
