
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
  __abstract__ = True
  id = Column(Integer, primary_key=True, autoincrement=True)
  created_at = Column(DateTime, default=datetime.now())


class User(BaseModel):
  __tablename__ = 'users'

  nick_name = Column(String, nullable=False)
  dictionary = relationship("Dictionary", back_populates='user')


class Dictionary(BaseModel):
  __tablename__ = 'dictionary'

  ukr_word = Column(String, nullable=False)
  eng_word = Column(String, nullable=False)
  user = relationship("User", back_populates='dictionary')


class Training(BaseModel):
  __tablename__ = 'training'
  user = relationship('User', back_populates='training')
  dictionary = relationship('Dictionary', back_populates='training')


engine = create_engine("postgresql+psycopg2://nadinekononykhina:1234@localhost/bot_translator")

Base.metadata.create_all(engine)



