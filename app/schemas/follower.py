from typing import Optional
from pydantic import BaseModel


class FollowerCreate(BaseModel):
    id: Optional[str] = None
    id_user_fr: Optional[str] = None


class FollowerUpdate(FollowerCreate):
    pass
