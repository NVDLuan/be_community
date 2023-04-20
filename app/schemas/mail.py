
from typing import Optional, List

from pydantic import BaseModel, EmailStr


class MailTo(BaseModel):
    email: Optional[EmailStr] = None