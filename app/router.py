from fastapi import APIRouter
from app.api.endpoint import index, user, post,upload, sendMail, follow, like, comment, reply_comment

route = APIRouter()

route.include_router(index.route, tags=["index"])
route.include_router(user.route, tags=["user"])
route.include_router(post.route, tags=["post"])
route.include_router(upload.route, tags=["upload"])
route.include_router(sendMail.route, tags=["send mail"])
route.include_router(follow.route, tags=["follow"])
route.include_router(like.route, tags=['like'])
route.include_router(comment.route, tags=['comment'])
route.include_router(reply_comment.route, tags=['reply comment'])
