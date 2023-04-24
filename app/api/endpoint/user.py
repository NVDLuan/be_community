from app.api.response.response import make_response_json, make_response_json_4_param
from app.services.userService import UserService
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user import UserCreate, UserLogin, UpdateMe, ChangePassword
from app.api.depends.user import user_admin, login_required, get_current_user, get_current_user_active
from app.models.user import User
route = APIRouter()

@route.get("/user/suggest_follow")
def suggest_follow(skip: int = 0, limit: int = 10, user: User = Depends(get_current_user_active), db: Session = Depends(get_db)) -> dict:
    service = UserService(db=db)
    response, count , mess= service.suggest_follow(user.id, skip, limit)
    return make_response_json_4_param(data=response, count=count, status=200, message=mess)


@route.get("/user/following/{pk}")
def get_user_following_by_id(pk:str, skip:int=0, limit:int=10, db:Session = Depends(get_db), user:User = Depends(get_current_user_active)):
    service = UserService(db=db)
    response, count = service.get_user_following_to_user(user, pk, limit, skip)
    return make_response_json_4_param(data=response, count = count, status=200, message="get success")


@route.get("/user/following_me")
def get_user_following_by_me(skip:int=0, limit:int=10, db:Session = Depends(get_db), user:User = Depends(get_current_user_active)):
    service = UserService(db=db)
    response, count = service.get_user_following_to_user(user, user.id, limit, skip)
    return make_response_json_4_param(data=response, count = count, status=200, message="get success")

@route.get("/user/follower/{pk}")
def get_user_follower_by_user(pk:str, skip:int = 0, limit:int =10, db:Session = Depends(get_db), user:User= Depends(get_current_user_active)):
    service = UserService(db=db)
    response, count = service.get_user_follower_to_user(user, pk, limit,skip)
    return make_response_json_4_param(data=response, count=count, status=200, message="get success")


@route.get("/user/follower_me")
def get_user_follower_by_user(skip:int = 0, limit:int =10, db:Session = Depends(get_db), user:User= Depends(get_current_user_active)):
    service = UserService(db=db)
    response, count = service.get_user_follower_to_user(user, user.id, limit,skip)
    return make_response_json_4_param(data=response, count=count, status=200, message="get success")


@route.post("/user/sign_up")
async def sign_up(user_data: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    user = user_service.create_user(user_data)
    return {"message": "create success"}


@route.post("/user/login")
def sign_up(form_data: UserLogin, db: Session = Depends(get_db)):
    userService = UserService(db)
    return {
        "status": 200,
        "token": userService.login(form_data)
    }


@route.get("/user/get_all", dependencies=[Depends(user_admin)])
def get_all_user(db: Session = Depends(get_db)):
    try:
        userService = UserService(db)
        return {
            "data": userService.get_all_user(),
            "meta": {
                "status": 200,
                "detail": "success"
            }
        }
    except Exception as e:
        HTTPException(status_code=401, detail="permision")


@route.get("/user/get_me")
def get_me(user: User = Depends(get_current_user_active), db:Session = Depends(get_db)):
    service = UserService(db=db)
    response = service.get_user_by_id(user_id=user.id)
    return {"data": response,
            "meta": {
                "status": 200,
                "detail": "get me success"
            }
        }


@route.get("/user/{pk}")
def get_user(pk:str, user:User = Depends(get_current_user_active), db:Session = Depends(get_db)):
    service = UserService(db=db)
    response = service.get_user_by_id(user_id=pk, user_fr=user.id)
    return {
        "data": response,
        "meta": {
            "status": 200,
            "detail": "get success"
        }
    }

@route.patch("/user/update/me")
def update_me(user_update: UpdateMe, user: User = Depends(get_current_user_active), db: Session = Depends(get_db)):
    service = UserService(db=db)
    status = service.update_user(user, user_update)
    return {
        "data": status,
        "meta": {
            "status": 202,
            "detail": "update thanh cong"
        }
    }


@route.patch("/user/update/avatar")
def update_avatar(avatar:str, user:User= Depends(get_current_user_active), db: Session=Depends(get_db)):
    service = UserService(db=db)
    response = service.update_avatar_to_user(user_obj=user, avatar=avatar)
    return make_response_json(data = response, status=200, message="update avatar success")

@route.patch("/user/change_password")
def update_avatar(request: ChangePassword, user:User= Depends(get_current_user_active), db: Session=Depends(get_db)):
    service = UserService(db=db)
    response = service.change_password_to_user(user_obj=user, request=request)
    return make_response_json(data = response, status=200, message="update avatar success")


@route.get("/user/search")
def search_user_by_name_or_email(search: str, skip: int = 0 , limit:int = 10,
                                 user: User = Depends(get_current_user_active),
                                 db:Session = Depends(get_db)):
    service = UserService(db=db)
    response, count = service.search_user_by_mail_or_name(search=search, skip=skip, limit=limit)
    return make_response_json_4_param(data=response, count=count, status=200, message="result search")
