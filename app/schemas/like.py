from typing import Optional
from pydantic import BaseModel, Field

from app.schemas.user import UserInfo


class LikeBsase(BaseModel):
    id: Optional[str] = None
    id_user: Optional[str] = None
    id_post: Optional[str] = None

    class Config:
        orm_mode = True


class LikeCreate(LikeBsase):
    pass


class LikeUpdate(LikeBsase):
    pass


class LikeRequest(BaseModel):
    id_post: Optional[str] = None



class LikeResponse(LikeBsase):
    user: Optional[UserInfo]= None

    class Config:
        arbitrary_types_allowed = True
