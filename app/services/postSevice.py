import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud.comment import comment
from app.crud.post import post
from app.schemas.post import CreatePost, UpdatePost, PostResponse
from app.crud.like import like

class PostService:
    def __init__(self, db: Session):
        self.db = db

    def create_post(self, post_cr: CreatePost, id_user: str):
        post_cr.id_user = id_user
        post_cr.id = uuid.uuid4()
        result = post.create(db=self.db, obj_in=post_cr, auto_commit=True)
        self.db.commit()
        return result

    def update_post(self, id_user: str, post_id: str, post_cr: UpdatePost):
        post_in = post.get(self.db, post_id)
        if post_in.id_user is not id_user:
            raise HTTPException(status_code=403, detail="PERMISSION DENIED")
        result = post.update(self.db, post_in, post_cr)
        self.db.commit()
        return result

    def remove_post(self, id_user:str, post_id:str):
        post_in = post.get(self.db, post_id)
        if post_in.id_user is not id_user:
            raise HTTPException(status_code=403, detail="PERMISSION DENIED")
        result = post.remove(db=self.db, id=post_id, auto_commit=True)
        return result

    def get_post_of_friend(self, id_user: str, skip: int = None, limit: int = None):
        result, count = post.get_post_friend(self.db, id_user, skip, limit)
        # data=[]
        # for item in result:
        #     data.append(self.make_response(item))
        # return data
        response=[]
        for item in result:
            p = PostResponse.from_orm(item)
            p.like_count= like.get_count_like_to_post(db=self.db, post_id=item.id)
            p.comment_count = comment.get_count_comment_by_post(self.db, item.id)
            response.append(p)
        return response, count

    def make_response(self, user):
        return dict(id=post.id, status=post.status, title=post.title, content=post.content, image=post.image, user_oner=dict(id_user=post.user_oner.id, name=post.user_oner.fullname, avatar=post.user_oner.avatar))
    def get_post(self, post_id: str):
        p = post.get(self.db, post_id)
        response = PostResponse.from_orm(p)
        response.like_count = like.get_count_like_to_post(self.db, p.id)
        response.comment_count = comment.get_count_comment_by_post(self.db, p.id)
        return response

    def get_all(self):
        return post.get_multi(db=self.db)

    def get_post_of_me(self, id_user: str, skip: int, limit: int):
        result, count = post.get_post_me(self.db, id_user, skip, limit)
        response = []
        for item in result:
            p = PostResponse.from_orm(item)
            p.like_count = like.get_count_like_to_post(db=self.db, post_id=item.id)
            p.comment_count = comment.get_count_comment_by_post(self.db, item.id)
            response.append(p)
        return response, count
