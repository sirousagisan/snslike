from datetime import datetime, timedelta, timezone
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database import Base 

JST = timezone(timedelta(hours=9), "JST")

class User(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String(512), unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=JST))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=JST), onupdate=datetime.now(tz=JST))
    
    articles = relationship("Arttcle", backref="user")
    like = relationship("Like", backref="user")
    followers = relationship("Follow", foreign_keys="Follow.follower_id", backref="follower")
    followees = relationship("Follow", foreign_keys="Follow.followee_id", backref="followee")

class Article(Base):
    __tablename__ = "article"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String)
    body: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=JST))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=JST), onupdate=datetime.now(tz=JST))
    likes = relationship("Like", backref="article")
    tags = relationship("ArticleTag", backref="article")

class Like(Base):
    __tablename__ = "like"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=JST))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=JST), onupdate=datetime.now(tz=JST))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    article_id: Mapped[int] = mapped_column(Integer, ForeignKey("article.id"))

class Follow(Base):
    __tablename__ = "follow"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    follower_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    followee_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=JST))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=JST), onupdate=datetime.now(tz=JST))
    
class Tag(Base):
    __tablename__ = "tag"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=JST))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=JST), onupdate=datetime.now(tz=JST))
    article_tags = relationship("ArticleTag", backref="tag")

class ArticleTag(Base):
    __tablename__ = "article_tag"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    article_id = mapped_column(Integer, ForeignKey("article.id"))
    tag_id = mapped_column(Integer, ForeignKey("tag.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=JST))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(tz=JST), onupdate=datetime.now(tz=JST))

