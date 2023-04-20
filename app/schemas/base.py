from datetime import datetime

from pydantic import BaseModel

class ResponseBase(BaseModel):
    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: int(v.timestamp()) * 1000
        }