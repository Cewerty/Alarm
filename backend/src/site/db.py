from sqlalchemy import Column, Integer, String, BigInteger, Text, TIMESTAMP
from sqlalchemy import MetaData, Table, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import sqlite3
import aiosqlite

url = 'sqlite+aiosqlite:///./test.db'
sync_engine = create_engine(url, connect_args= {'check_same_thread': False}, future=True)
engine = create_async_engine(url,)
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class PostInDB(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)

async def get_db():
    async with Session() as session:
        yield session
