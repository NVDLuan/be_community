from typing import Dict

from fastapi import HTTPException

from app.crud.user import user
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserUpdate, ResponseUser, UpdateMe, ChangePassword
from app.api.depends.token import get_password_hash, verify_password, create_access_token
from app.crud.follow import following, follower
from app.services.follow import FollowService

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_create: UserCreate):
        db_user = user.get_user_by_email(self.db, user_create.email)
        if db_user is not None:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )
        user_create.password = get_password_hash(user_create.password)
        user_db = user.create_User(db=self.db, userCreate=user_create)
        return user_db

    def login(self, form_data: UserLogin):
        db_user = user.get_user_by_email(self.db, form_data.email)
        if db_user is None:
            raise HTTPException(
                status_code=400,
                detail="email invalid"
            )
        if not verify_password(form_data.password, db_user.password):
            raise HTTPException(
                status_code=400,
                detail="wrong password"
            )
        return create_access_token(db_user)

    def get_all_user(self):
        return user.get_all_user(self.db)

    def update_user(self, user_db: User, user_update: UpdateMe):
        data = user_update.__dict__
        status_update = user.update(db=self.db, db_obj=user_db, obj_in=data)
        return status_update

    def get_user_by_id(self, user_id: str, user_fr:str=None):
        data = user.get(db=self.db, id=user_id)
        response = ResponseUser.from_orm(data)
        response.following_count = following.get_count_following(db=self.db, user_id=user_id)
        response.follower_count = following.get_count_follower(db=self.db, user_id=user_id)
        if user_fr is not None:
            fl_service = FollowService(db=self.db)
            response.check_follow = fl_service.check_follow_to_user(user_id=user_fr, user_to=user_id)
        return response

    def suggest_follow(self, user_id, skip: int = None, limit: int = None):
        # data = user.get_user_follower_of_user(db = self.db, user_id=user_id, limit=limit, skip=skip)
        follower_db = follower.get_id_by_user_id(db=self.db, user_id=user_id)
        data, count = user.suggest_follow_by_user(db=self.db, user_id=user_id, follower_id=follower_db.id, skip=skip, limit=limit)
        response = []
        # if len(data) == 0:
        #     return None, 0
        for item in data:
            response.append(ResponseUser.from_orm(item))
        return response, count, follower_db.id

    def get_user_following_to_user(self, user_call: User, user_id: str, limit:int, skip:int):
        data, count = user.get_user_following_to_user(db = self.db, user_id=user_id, limit=limit, skip= skip)
        response =[]
        fl_service = FollowService(db=self.db)
        for item in data:
            tmp = ResponseUser.from_orm(item)
            tmp.check_follow = fl_service.check_follow_to_user(user_id=user_call.id, user_to=item.id)
            response.append(tmp)
        return response, count

    def get_user_follower_to_user(self, user_call:User, user_id:str, limit:int, skip:int):
        data, count = user.get_user_follower_of_user(db = self.db, user_id=user_id, limit=limit, skip= skip)
        response=[]
        fl_service = FollowService(db=self.db)
        for item in data:
            tmp = ResponseUser.from_orm(item)
            tmp.check_follow = fl_service.check_follow_to_user(user_id=user_call.id, user_to=item.id)
            response.append(tmp)
        return response, count

    def update_avatar_to_user(self, user_obj: User, avatar:str):
        data_update = dict(avatar=avatar)
        data = user.update(db=self.db, db_obj=user_obj, obj_in=data_update)
        return ResponseUser.from_orm(data)

    def update_image_cover_to_user(self, user_obj: User, img:str):
        data_update = dict(image_cover=img)
        data = user.update(db=self.db, db_obj=user_obj, obj_in=data_update)
        return ResponseUser.from_orm(data)

    def change_password_to_user(self, user_obj: User, request: ChangePassword):
        data = user.get(self.db, id = user_obj.id)
        if not verify_password(request.password, data.password):
            raise HTTPException(status_code=400, detail="wrong password")
        if not request.new_password == request.confirm_password:
            raise HTTPException(status_code=400, detail="password and new password different ones")
        data_update = dict(password=get_password_hash(request.confirm_password))
        data = user.update(db=self.db, db_obj=user_obj, obj_in=data_update)
        return ResponseUser.from_orm(data)

    def search_user_by_mail_or_name(self, search: str, skip:int, limit: int):
        data, count = user.search_user_by_mail_and_name(db = self.db, search = search, skip=skip, limit=limit)
        response = []
        fl_service = FollowService(db=self.db)
        for item in data:
            tmp = ResponseUser.from_orm(item)
            tmp.check_follow = fl_service.check_follow_to_user(user_id=user_call.id, user_to=item.id)
            response.append(tmp)
        return response, count