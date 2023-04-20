from fastapi import HTTPException

from app.crud.user import user
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserUpdate, ResponseUser
from app.api.depends.token import get_password_hash, verify_password, create_access_token
from app.crud.follow import following


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_create: UserCreate):
        user_create.password = get_password_hash(user_create.password)
        user_db = user.create_User(db=self.db, userCreate=user_create)
        return user_db

    def login(self, form_data: UserLogin):
        list_user = user.get_user_by_email(self.db, form_data.email)
        if len(list_user) == 0:
            raise HTTPException(
                status_code=400,
                detail="email invalid"
            )
        db_user = list_user[0]
        if not verify_password(form_data.password, db_user.password):
            raise HTTPException(
                status_code=400,
                detail="email invalid"
            )
        return create_access_token(db_user)

    def get_all_user(self):
        return user.get_all_user(self.db)

    def update_user(self, user_db: User, user_update: UserUpdate):
        status_update = user.update(db=self.db, db_obj=user_db, obj_in=user_update)
        return status_update

    def get_user_by_id(self, user_id: str):
        data = user.get(db=self.db, id=user_id)
        response = ResponseUser.from_orm(data)
        response.following_count = following.get_count_following(db=self.db, user_id=user_id)
        response.follower_count = following.get_count_follower(db=self.db, user_id=user_id)
        return response

    def suggest_follow(self, user_id, skip: int = None, limit: int = None):
        data = user.suggest_follow_by_user(db = self.db, user_id=user_id, limit=limit, skip=skip)
        # response = []
        # if len(data) == 0:
        #     return None, 0
        # for item in data:
        #     response.append(ResponseUser.from_orm(item))
        # return response, count
        return data
