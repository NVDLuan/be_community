import logging
import uuid
from typing import Any, Dict, Optional, Union
from uuid import uuid4

from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload

from app.models.post import Post
from app.models.follower import Follower
from app.models.following import Following
from app.models.user import User
from app.schemas.post import CreatePost, UpdatePost
from .base import CRUDBase
from .. import models, crud

logger = logging.getLogger(__name__)


class CRUDPost(CRUDBase[Post, CreatePost, UpdatePost]):

    def get_post_friend(self, db: Session, user_id: str, skip: int, limit: int):
        query = db.query(self.model).options(joinedload(self.model.user_oner)).join(Following, self.model.id_user == Following.id_user_to) \
            .join(Follower, Follower.id == Following.id_follower).filter(Follower.id_user_fr == user_id).order_by(
            self.model.time_create.desc())
        if skip is not None and limit is not None:
            query = query.offset(skip).limit(limit)
        return query.all(), query.count()

    def get_post_me(self, db: Session, user_id: str, skip: int, limit: int):
        query_set = db.query(self.model).filter(self.model.id_user == user_id).order_by(self.model.time_create.desc())
        if skip is not None and limit is not None:
            query_set = query_set.offset(skip).limit(limit)
        return query_set.all(),  query_set.count()


post = CRUDPost(Post)