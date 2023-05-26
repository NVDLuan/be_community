from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr


class MailTo(BaseModel):
    email: Optional[EmailStr] = None
