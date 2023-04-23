from datetime import date, datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    id: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    address: Optional[str] = None
    avatar: Optional[str] = None
    is_activate: Optional[bool] = True
    sex: Optional[str] = None
    fullname: Optional[str] = None
    birthday: Optional[date] = None
    description: Optional[str] = None
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None


class UserCreate(UserBase):
    email: EmailStr
    is_super: bool = False


class UpdateMe(BaseModel):
    address: Optional[str] = None
    sex: Optional[str] = None
    fullname: Optional[str] = None
    birthday: Optional[date] = None
    description: Optional[str] = None


class UserUpdate(BaseModel):
    id: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    avatar: Optional[str] = None
    is_activate: Optional[bool] = True
    sex: Optional[str] = None
    fullname: Optional[str] = None
    birthday: Optional[date] = None
    description: Optional[str] = None
    image_cover: Optional[str] = None
    time_create: Optional[datetime] = None

class UserInfo(BaseModel):
     id: str = Field(alias="id_user")
     avatar:str
     fullname: str

     class Config:
         allow_population_by_field_name = True
         orm_mode = True

class ChangePassword(BaseModel):
    password: Optional[str] = None
    password_new: Optional[str] = None
    confirm_password: Optional[str] = None

class ResponseUser(BaseModel):
    id: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    avatar: Optional[str] = None
    is_activate: Optional[bool] = True
    sex: Optional[str] = None
    fullname: Optional[str] = None
    birthday: Optional[date] = None
    description: Optional[str] = None
    image_cover: Optional[str] = None
    time_create: Optional[datetime] = None
    follower_count: Optional[int] = None
    following_count: Optional[int] = None
    check_follow: Optional[bool] = None
    class Config:
        orm_mode = True


class ChangePassword(BaseModel):
    password: Optional[str] = None
    new_password: Optional[str] = None
    confirm_password: Optional[str] = None

