from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Following(Base):
    __tablename__ = "following"
    id = Column(String(255), primary_key=True, index=True)
    id_user_to = Column(String(255), ForeignKey("user.id"))
    id_follower = Column(String(255), ForeignKey('follower.id'))
    # Relationship
    following = relationship("User", foreign_keys=[id_user_to])
    follower = relationship("Follower", foreign_keys=[id_follower])
