from fastapi import APIRouter, UploadFile, File
import cloudinary
import cloudinary.uploader

from app.core.settings import settings

cloudinary.config(
    cloud_name=settings.CLOUD_NAME,
    api_key=settings.API_KEY,
    api_secret=settings.API_SECRET,
)

route = APIRouter()


@route.post('/upload')
async def upload(file: UploadFile = File(...)):

    result = cloudinary.uploader.upload(file.file, folder="social")
    url = result.get("secure_url")
    return {
        "data": url,
        "meta": {
            "status": 200,
            "detail": "upload file to cloud success"
        }
    }
