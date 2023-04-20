import uuid

from sqlalchemy.orm import Session
from app.crud.follow import follower, following
from app.schemas.follow import FollowingCreate
class FollowService:
    def __init__(self, db:Session):
        self.db = db

    def get_user_following_by_id(self, user_id: str):
        id_follower = follower.create_only_one(self.db, user_id)
        return following.get_count_follow(self.db, id_follower)

    def create_following(self, user_id: str, follow: FollowingCreate):
        follower.create_only_one(self.db, user_id)
        id_follower = follower.get_id_by_user_id(self.db, user_id)
        follow.id_follower = id_follower.id
        follow.id = uuid.uuid4()
        return following.create(db=self.db, obj_in=follow)

    def get_follower_by_id(self, user_id: str):
        data_db = following.get_id_by_user_id(self.db, user_id)
        data=[]
        for id in data_db:
            query = follower.get(self.db, id)
            data.append(query)
        return data

    def remove_following(self, user_id: str, user_rm: str):
        follower_db = follower.get_id_by_user_id(db=self.db, user_id=user_id)
        data_db = following.get_following_by_userto_fr(db=self.db, follower_id=follower_db.id, user_to=user_rm)
        status = following.remove(db=self.db, id=data_db.id, auto_commit=True)
        self.db.commit()
        return status

    def follow_friend_suggest(self, user_id: str):
        pass
