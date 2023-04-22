

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depends.user import get_current_user_active
from app.api.response.response import make_response_json
from app.database.database import get_db
from app.models.user import User
from app.schemas.comment import CommentCreate, CommentUpdate
from app.services.comment import CommentService

route = APIRouter()


@route.get("/comment/{pk}")
def get_comment_by_post(pk: str, skip: int, limit: int,
                        db: Session = Depends(get_db),
                        user: User = Depends(get_current_user_active)):
    service = CommentService(db=db)
    response = service.get_comment_by_post(id_post=pk, skip= skip, limit=limit)
    return make_response_json(data=response, status=200, message="get success")


@route.post("/comment/create")
def create_comment(comment_in: CommentCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user_active)):
    service = CommentService(db=db)
    response = service.create_comnent_to_post(user_id=user.id, comment_in=comment_in)
    return make_response_json(data=response, status=200, message="create comment success")


@route.put("/comment/update")
def update_comment(comment_update: CommentUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user_active)):
    service = CommentService(db=db)
    response = service.update_comment_of_user(user_id=user.id, comment_in=comment_update)
    return make_response_json(data=response, status=200, message="update comment success")


@route.delete("/comment/{pk}")
def remove_commnet(pk: str, user: User = Depends(get_current_user_active), db:Session = Depends(get_db)):
    service = CommentService(db=db)
    response = service.remove_comment_by_id(user=user, comment_id=pk )
    return make_response_json( data=response,status=200, message="deleted success")
