from fastapi import APIRouter

route = APIRouter()

@route.get("/")
async def root():
    return {"message": "Hello World"}

@route.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
