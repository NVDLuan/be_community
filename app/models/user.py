from sqlalchemy.orm import relationship

from app.models.base import Base
from sqlalchemy import ForeignKey, Integer, String, Column, TIMESTAMP, text, Date, Boolean, DateTime, DATE
from datetime import datetime


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    address = Column(String(255))
    password = Column(String(255))
    sex = Column(String(10))
    avatar = Column(String(255), default="https://res.cloudinary.com/dy0mhielk/image/upload/v1682395261/social/blftkogghkfuft5ipx1d.png")
    birthday = Column(DATE)
    lasted_login = Column(DateTime)
    status = Column(String(255))
    time_create = Column(DateTime, default=datetime.now)
    is_super = Column(Boolean)
    description = Column(String(255))
    image_cover = Column(String(255), default="https://res.cloudinary.com/dy0mhielk/image/upload/v1682265810/social/bgmeicum5jqhitfy32zj.jpg")
    is_activate = Column(Boolean)

    #Relationship
    posts = relationship("Post", cascade="delete")
    follower = relationship('Follower',  uselist=False, back_populates="follower" )
    following = relationship('Following', cascade='delete', back_populates="following")
    comment = relationship("Comment",cascade='delete', back_populates="user")
    recomment = relationship("Recomment", cascade='delete', back_populates="user")


