from sqlalchemy import and_

from app.crud.base import CRUDBase
from app.models.like import Like
from app.schemas.like import LikeCreate, LikeUpdate

from sqlalchemy.orm import Session


class CRUDLke(CRUDBase[Like, LikeCreate, LikeUpdate]):

    def get_user_like_to_post(self, db: Session, post_id: str):
        query = db.query(self.model).filter(self.model.id_post == post_id).all()
        return query

    def get_count_like_to_post(self, db: Session, post_id: str) -> int:
        query = db.query(self.model).filter(self.model.id_post == post_id)
        return query.count()

    def get_like_by_user_and_post(self, db: Session, user_id:str, post_id: str):
        query = db.query(self.model).filter(and_(self.model.id_user == user_id, self.model.id_post == post_id)).first()
        return query

    def check_user_like(self, db: Session, user_id:str, post_id: str):
        data = self.get_like_by_user_and_post(db, user_id, post_id)
        if data is not None:
            return True
        return False


like = CRUDLke(Like)
