from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class User(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    email = Column(String)    

class New_message(Base):
	__tablename__ = "messages_table"
	id = Column(Integer, primary_key=True)
	from_who = Column(String)
	to_whom = Column(String)
	message = Column(String)
