
from sqlalchemy.orm import Session
from main import User, engine



def generate_user(count: int = 1):
  user = [
    User(
    nick_name = 'Nadine'
    )
  ]

  with Session(engine) as session:
    session.add_all(user)
    session.commit()
