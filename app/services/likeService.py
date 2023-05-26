import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud.like import like
from app.schemas.like import LikeCreate
from app.schemas.like import LikeResponse


class LikeService:
    def __init__(self, db: Session):
        self.db = db

    def create_like(self, user_id: str, like_in: LikeCreate):
        like_db = like.get_like_by_user_and_post(db=self.db, user_id=user_id, post_id=like_in.id_post)
        if like_db is not None:
            raise HTTPException(status_code=401, detail="Liked")
        like_in.id_user = user_id
        like_in.id = uuid.uuid4()
        status = like.create(db=self.db, obj_in=like_in, auto_commit=True)
        return status

    def delete_like(self, user_id: str, like_in: LikeCreate):
        like_db = like.get_like_by_user_and_post(db=self.db, user_id=user_id, post_id=like_in.id_post)

        if like_db is None:
            raise HTTPException(status_code=401, detail="ko tim thaay bai post")
        status = like.remove(db=self.db, id=like_db.id)
        self.db.commit()
        return status

    def get_user_like_on_post(self, post_id: str):
        list_user = like.get_user_like_to_post(db=self.db, post_id=post_id)
        response = []
        for item in list_user:
            response.append(LikeResponse.from_orm(item))
        return response
        # return LikeResponse.from_orm(list_user)
