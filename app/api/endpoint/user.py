from app.api.response.response import make_response_json
from app.services.userService import UserService
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user import UserCreate, UserLogin, UserUpdate
from app.api.depends.user import user_admin, login_required, get_current_user, get_current_user_active
from app.models.user import User
route = APIRouter()


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
def get_me(user:User = Depends(get_current_user_active), db:Session = Depends(get_db)):
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
    response = service.get_user_by_id(user_id=pk)
    return {"data": response,
            "meta": {
                "status": 200,
                "detail": "get me success"
            }
            }

@route.patch("/user/update/me")
def update_me(user_update: UserUpdate, user: User = Depends(get_current_user_active), db: Session = Depends(get_db)):
    service = UserService(db=db)
    status = service.update_user(user, user_update)
    return {
        "data": status,
        "meta": {
            "status": 202,
            "detail": "update thanh cong"
        }
    }

@route.get("/user/suggest_follow")
def suggest_follow(skip:int = 0, limit: int = 10, user: User = Depends(get_current_user_active), db: Session = Depends(get_db)):
    service = UserService(db=db)
    response = service.suggest_follow(user.id, skip,limit)
    return {
        "data": response,
        "count": 1000,
        "meta": {
            "status": 202,
            "detail": "update thanh cong"
        }
    }
