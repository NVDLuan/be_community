import uuid

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.recomment import Recomment
from app.schemas.recomment import RecommentCreate, RecommentUpdate


class CRUDRecomment(CRUDBase[Recomment, RecommentCreate, RecommentUpdate]):
    def get_count_recomment_by_commet(self, db: Session, id_comment:str):
        query = db.query(self.model).filter(self.model.id == id_comment).all()
        return query.count()

    def get_recomment_by_comment(self, db: Session, id_comment: str, skip: int, limit: int):
        query = db.query(self.model).filter(self.model.id == id_comment)
        if skip is not None and limit is not None:
            query.offset(skip).limit(limit)
        return query.all()


recomment = CRUDRecomment(Recomment)


