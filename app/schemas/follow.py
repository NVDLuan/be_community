
from typing import Optional
from pydantic import BaseModel


class FollowingCreate(BaseModel):
    id:Optional[str] = None
    id_user_to: Optional[str] = None
    id_follower: Optional[str] = None


class FollowingUpdate(FollowingCreate):
    pass
