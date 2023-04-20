from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


from app.models.user import User


from app.models.base import Base


class Recomment(Base):
    __tablename__ = "recomment"

    id = Column(String(255), primary_key=True, index=True)
    id_user = Column(String(255), ForeignKey("user.id", ondelete="CASCADE", onupdate='CASCADE', deferrable=True))
    id_cmt = Column(String(255), ForeignKey("comment.id", ondelete="CASCADE", onupdate='CASCADE', deferrable=True))
    content = Column(String(1000))
    image = Column(String(255))
    time_create = Column(DateTime)

    # Relationship
    user = relationship(User, back_populates="recomment")
    comment = relationship("Comment", back_populates="recomment")
