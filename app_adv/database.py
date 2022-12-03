import atexit
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, func, ForeignKey
from config import PG_DSN

engine = create_engine(PG_DSN)
Base = declarative_base()
Session = sessionmaker(bind=engine)

atexit.register(lambda: engine.dispose())

class OwnerModel(Base):

    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    ads = relationship('AdvertisementModel', backref='owner')


class AdvertisementModel(Base):

    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    owner_id = Column(Integer, ForeignKey('owners.id'))


Base.metadata.create_all(engine)
