from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Follower(Base):
    __tablename__ = "follower"
    id = Column(String(255), primary_key=True, index=True)
    id_user_fr = Column(String(255), ForeignKey("user.id"))

    # Relationship
    follower = relationship("User", foreign_keys=[id_user_fr], uselist=False)
