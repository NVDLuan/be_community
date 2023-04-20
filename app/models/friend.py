from app.models.user import User
from base import Base
from sqlalchemy import Column, String, text, ForeignKey,TIMESTAMP,Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Friend(Base):
    __tablename__ = "friend"

    id = Column(String(255), primary_key=True, index=True)
    id_user_fr = Column(String(255), ForeignKey("user.id"))
    id_user_to = Column(String(255), ForeignKey("user.id"))
    time_add = Column(DateTime)

    # Relationship
    user_fr = relationship(User, foreign_keys=[id_user_fr])
    user_to = relationship(User, foreign_keys=[id_user_to])

