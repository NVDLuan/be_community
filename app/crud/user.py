import logging
import uuid
from typing import Any

from sqlalchemy import and_
from sqlalchemy import not_
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app import models
from app.models.follower import Follower
from app.models.following import Following
from app.models.user import User
from app.schemas.user import UserCreate
from app.schemas.user import UserUpdate
from .base import CRUDBase

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def create_User(self, db: Session, userCreate: UserCreate):
        userCreate.id = str(uuid.uuid4())
        user_db = self.create(db=db, obj_in=userCreate, auto_commit=False)
        db.commit()
        return user_db

    def get_user_by_email(self, db: Session, email: str):
        user = db.query(User).filter(User.email == email).first()
        return user

    def get_user_by_id(self, db: Session, user_id: Any) -> User:
        logger.info("CRUDUser: get_user_by_id called.")
        logger.debug("With: User ID - %s", user_id)

        user = db.query(models.User).filter(models.User.id == user_id).first()

        logger.info("CRUD: get_user_by_id success")
        return user

    def is_active(self, user: User) -> bool:
        return user.is_activate

    def is_super_user(self, user: User) -> bool:
        return user.is_super

    def get_all_user(self, db: Session):
        return db.query(User).all()

    def get_user_following_to_user(self, db: Session, user_id: str, skip: int, limit: int):
        query = db.query(self.model).join(Following, self.model.id == Following.id_user_to). \
            join(Follower, Following.id_follower == Follower.id). \
            filter(Follower.id_user_fr == user_id)
        count = query.count()
        if skip is not None and limit is not None:
            query.offset(skip).limit(limit)
        return query.all(), count

    def get_user_follower_of_user(self, db: Session, user_id: str, skip: int, limit: int):
        query = db.query(self.model).join(Follower, self.model.id == Follower.id_user_fr). \
            join(Following, Follower.id == Following.id_follower). \
            filter(Following.id_user_to == user_id)
        count = query.count()
        if skip is not None and limit is not None:
            query.offset(skip).limit(limit)
        return query.all(), count

    def suggest_follow_by_user(self, db: Session, user_id: str, follower_id: str, skip: int, limit: int):
        logger.debug(f"skip={skip}, limit ={limit}")
        iquery = db.query(Following).filter(Following.id_follower == follower_id).all()
        condition = []
        for item in iquery:
            condition.append(item.id_user_to)
        query = db.query(self.model).filter(and_(not_(self.model.id.in_(condition)), self.model.id != user_id))
        count = query.count()
        return query.limit(3), count

    def search_user_by_mail_and_name(self, db: Session, search: str, skip: int, limit: int):
        query = db.query(self.model).filter(
            or_(self.model.email.like(f"%{search}%"), self.model.fullname.like(f"%{search}%")))
        count = query.count()
        if skip is not None and limit is not None:
            query.offset(skip).limit(limit)
        return query.all(), count


user = CRUDUser(User)
