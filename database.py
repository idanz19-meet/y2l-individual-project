from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def signup_now(name,password,email):
    new_user = User(
        name=name,
        password=password,
        email=email)
    session.add(new_user)
    session.commit()

def send_message(sender,receiver,message):
	new_message = New_message(
		sender=sender,
		receiver=receiver,
		message=message)
	session.add(new_message)
	session.commit()


def get_messages_by_id(id):
	session.query(New_message).all()
