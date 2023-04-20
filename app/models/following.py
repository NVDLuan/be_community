from app.models.base import Base

from sqlalchemy import Column, String, text, ForeignKey, TIMESTAMP, Boolean, Table
from sqlalchemy.orm import relationship


class Following(Base):
    __tablename__ = "following"
    id = Column(String(255), primary_key=True, index=True)
    id_user_to = Column(String(255), ForeignKey("user.id"))
    id_follower = Column(String(255), ForeignKey('follower.id'))
    # Relationship
    following = relationship("User", foreign_keys=[id_user_to])
    follower = relationship("Follower", foreign_keys=[id_follower])