from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.response.response import make_response_json
from app.database.database import get_db
from app.models.user import User
from app.services.follow import FollowService
from app.schemas.follow import FollowingCreate
from app.api.depends.user import get_current_user_active

route = APIRouter()


@route.post("/follow/")
async def create_folow(fl: FollowingCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user_active)):
    # try:
    service = FollowService(db=db)
    result = service.create_following(user_id=user.id, follow=fl)
    return {
        "data": result,
        "meta": {
            "status": 200,
            "detail": "create follow success"
        }
    }


@route.delete("/follow")
async def remove_follow(user_id_remove:str, user: User = Depends(get_current_user_active), db:Session = Depends(get_db)):
    service = FollowService(db=db)
    response = service.remove_following(user.id, user_id_remove)
    return make_response_json(data=response, status=200, message="deleted success")
    # except Exception as error:
    #     HTTPException(status_code=400, detail="create follow not success")