from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, relationship

PG_CONN_URI = "postgresql+asyncpg://postgres:password@localhost/postgres"

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    
    user = relationship("User", back_populates="posts")


engine = create_async_engine(PG_CONN_URI, echo=False)

Session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)
