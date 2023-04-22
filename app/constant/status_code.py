from enum import Enum
from starlette import status

class AppStatus(Enum):
    SUCCESS = status.HTTP_200_OK, 200, "SUCCESS"
    ERROR_404_NOT_FOUND = status.HTTP_404_NOT_FOUND, 404, "HTTP_404_NOT_FOUND"
    ERROR_UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED, 401, 'UNAUTHORIZED'
    ERROR_TOKEN_INVALID = status.HTTP_401_UNAUTHORIZED, 401, 'ERROR_TOKEN_INVALID'
    ERROR_LOGIN = status.HTTP_400_BAD_REQUEST, 400, 'ERROR LOGIN FAILED'

    LOGIN_SUCCESS = status.HTTP_200_OK, 200, 'LOGIN_SUCCESS'