from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.schemas.user import UserInfo

class BasePost(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    id_user: Optional[str] = None
    image: Optional[str] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True


class PostResponse(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    user_oner: Optional[UserInfo] =None
    image: Optional[str] = None
    status: Optional[str] = None
    time_create: Optional[datetime] = None
    like_count: Optional[int] = None
    comment_count: Optional[int] = None
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class CreatePost(BasePost):
    pass

class UpdatePost(BasePost):
    pass