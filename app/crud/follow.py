import uuid

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.follower import Follower
from app.models.following import Following
from app.schemas.follow import FollowingCreate
from app.schemas.follower import FollowerCreate
from app.schemas.follower import FollowerUpdate


class CRUDFollower(CRUDBase[Follower, FollowerCreate, FollowerUpdate]):

    def create_only_one(self, db: Session, user_id: str):
        data_db = db.query(Follower).filter(self.model.id_user_fr == user_id).all()
        if len(data_db) == 0 or data_db is None:
            follow = FollowerCreate()
            follow.id = uuid.uuid4()
            follow.id_user_fr = user_id
            self.create(db=db, obj_in=follow, auto_commit=True)

    def get_id_by_user_id(self, db: Session, user_id: str):
        self.create_only_one(db, user_id)
        data_db = db.query(self.model).filter(self.model.id_user_fr == user_id).first()
        return data_db


follower = CRUDFollower(Follower)


class CRUDFollowing(CRUDBase[Following, FollowingCreate, FollowingCreate]):

    def get_id_by_user_id(self, db: Session, user_id: str):
        query = db.query(self.model.id_follower).filter(self.model.id_user_to == user_id).all()

    def get_count_follow(self, db: Session, follower_id: str):
        query = db.query(self.model).filter(self.model.id_follower == follower_id).all()
        return query, len(query)

    def get_following_by_userto_fr(self, db: Session, follower_id: str, user_to: str):
        return db.query(self.model).filter(
            and_(self.model.id_follower == follower_id, self.model.id_user_to == user_to)).first()

    def get_count_following(self, db: Session, user_id: str):
        query = db.query(self.model).join(Follower, self.model.id_follower == Follower.id).filter(
            Follower.id_user_fr == user_id)
        return query.count()

    def get_count_follower(self, db: Session, user_id: str):
        query = db.query(self.model).filter(self.model.id_user_to == user_id)
        return query.count()


following = CRUDFollowing(Following)
