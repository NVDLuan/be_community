
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.depends.user import login_required, get_current_user_active
from app.database.database import get_db
from app.models.user import User
from app.schemas.post import CreatePost, UpdatePost
from app.schemas.base_respons import DataResponse
from app.services.postSevice import PostService
from app.api.response.response import make_response_json, make_response_json_4_param

route = APIRouter()


@route.post("/post/create")
async def create_post(post: CreatePost, token: dict = Depends(login_required), db: Session = Depends(get_db)):

    uid = token['uid']
    post_srv = PostService(db)
    result = post_srv.create_post(post, uid)
    return {"data": result}


@route.get("/post/friend")
def get_post_friend(skip: int = 0, limit: int = 10, token: dict = Depends(login_required), db: Session = Depends(get_db)):
    # try:
    uid = token['uid']
    post_srv = PostService(db=db)
    result, count = post_srv.get_post_of_friend(id_user=uid)
    return make_response_json_4_param(data=result, count=count, status=200, message="")
    # except Exception as err:
    #     HTTPException(status_code=400, detail="Create not success")


@route.get("/post/getall")
def get_post_all(db: Session = Depends(get_db)):
    service = PostService(db=db)
    resutl = service.get_all()
    return {"status": 200,
            "data": resutl
            }


@route.get("/post/me")
def get_post_of_me(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user:User = Depends(get_current_user_active)):
    service = PostService(db=db)
    response, count = service.get_post_of_me(id_user=user.id, skip=skip, limit=limit)
    return make_response_json_4_param(data=response, count=count, status=200, message="thanh cong")

@route.get("/post/{pk}")
def get_post_by_id(pk:str, db:Session = Depends(get_db), user: User=Depends(get_current_user_active)):
    service = PostService(db=db)
    response = service.get_post_by_id(id=pk, id_user=user.id)
    return make_response_json(data=response, status=200, message="get success")

@route.get("/post/user")
def get_post_of_user(user_id: str = None, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user:User = Depends(get_current_user_active)):
    service = PostService(db=db)
    response, count = service.get_post_of_me(id_user=user_id, skip=skip, limit=limit)
    return make_response_json_4_param(data=response, count=count, status=200, message="thanh cong")

@route.put("/post/update")
def update_post(post_update: UpdatePost, db:Session = Depends(get_db), user: User = Depends(get_current_user_active)):
    service = PostService(db=db)
    response = service.update_post(user.id,post_update.id, post_update)
    return make_response_json(data=response, status=200, message="update thanh cong")


@route.delete("/post/delete")
def delete_post(id_post:str, db:Session = Depends(get_db), user: User = Depends(get_current_user_active)):
    service = PostService(db=db)
    response = service.remove_post(user=user, post_id=id_post)
    return make_response_json(data ="", status = 200, message="delete success")

