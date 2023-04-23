
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depends.user import get_current_user_active
from app.api.response.response import make_response_json
from app.database.database import get_db
from app.models.user import User
from app.services.likeService import LikeService
from app.schemas.like import LikeCreate, LikeResponse, LikeRequest

route = APIRouter()


@route.get("/like/get_post")
def get_like_on_post(id_post: str, db: Session=Depends(get_db), user: User = Depends(get_current_user_active)):
    service = LikeService(db=db)
    response = service.get_user_like_on_post(id_post)
    return make_response_json(data=response, status=200, message="get like success")
    # return {
    #     "data": response,
    #     "meta":{
    #         "status": 200,
    #         "detail": ""
    #     }
    # }


@route.post("/like_to_post")
def create_like_to_post(request: LikeCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user_active)):
    service = LikeService(db=db)
    response = service.create_like(user_id=user.id, like_in=request)
    return {
        "data": response,
        "meta":{
            "status": 200,
            "detail":""
        }
    }


@route.delete("/like_to_post")
def remove_like(request: LikeCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user_active)):
    service = LikeService(db=db)
    response = service.delete_like(user_id=user.id, like_in=request)
    return make_response_json(data=response, status=202, message="Remove like success")


@route.get("/like/count/{pk}")
def get_count_like_of_post(pk:str, db: Session = Depends(get_db), user: User = Depends(get_current_user_active)):
    service = LikeService(db=db)
    response = service.get_user_like_on_post(pk)
    return make_response_json(data=response, status=200, message="get count like success")


