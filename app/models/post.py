from app.models.user import User
from app.models.base import Base
from sqlalchemy import Column, String, text, ForeignKey,TIMESTAMP,Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
class Post(Base):
    __tablename__ = "post"

    id = Column(String(255), primary_key=True)
    title = Column(String(255))
    content = Column(String(1000))
    id_user = Column(String(255), ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE", deferrable=True),  nullable=False,)
    time_create = Column(DateTime, default=datetime.now)
    image = Column(String(255))
    status = Column(String(20))

    # Relationship
    user_oner = relationship(User, foreign_keys=[id_user],  overlaps="posts")
    comment = relationship("Comment", back_populates="post")
