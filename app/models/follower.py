from app.models.base import Base

from sqlalchemy import Column, String, text, ForeignKey, TIMESTAMP, Boolean, Table
from sqlalchemy.orm import relationship


class Follower(Base):
    __tablename__ = "follower"
    id = Column(String(255), primary_key=True, index=True)
    id_user_fr = Column(String(255), ForeignKey("user.id"))

    # Relationship
    follower = relationship("User", foreign_keys=[id_user_fr], uselist=False)
