from app.models.post import Post
from app.models.recomment import Recomment
from app.models.user import User
from app.crud.base import Base
from sqlalchemy import Column, String, text, ForeignKey, TIMESTAMP, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Comment(Base):
    __tablename__ = "comment"

    id = Column(String(255), primary_key=True, index=True)
    id_user = Column(String(255), ForeignKey("user.id", ondelete="CASCADE", onupdate='CASCADE', deferrable=True))
    id_post = Column(String(255), ForeignKey("post.id", ondelete="CASCADE", onupdate='CASCADE', deferrable=True))
    content = Column(String(1000))
    image = Column(String(255))
    time_create = Column(DateTime)

    # Relationship
    user = relationship(User, back_populates="comment")
    post = relationship(Post, back_populates="comment")
    recomment = relationship(Recomment, back_populates="comment")
