from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy.orm import relationship

from app.models.base import Base


class Like(Base):
    __tablename__ = "like"

    id = Column(String(255), primary_key=True, unique=True, server_default=text("uuid_generate_v4()"), )
    id_user = Column(String(255), ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE", deferrable=True))
    id_post = Column(String(255), ForeignKey("post.id", ondelete="CASCADE", onupdate="CASCADE", deferrable=True))

    post = relationship("Post")
    user = relationship("User")
