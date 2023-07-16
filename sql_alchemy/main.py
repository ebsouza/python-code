import sqlalchemy as db
from sqlalchemy.orm import Session

from models import User, Task

engine = db.create_engine("sqlite:///database.db", echo=True, future=True)

with Session(engine) as session:
     user_1 = User(
         name="User 1",
         fullname="Simple Robot",
         tasks=[Task(description="A simple task")],
     )
     user_2 = User(
         name="User 2",
         fullname="IA Robot",
         tasks=[
             Task(description="A simple task"),
             Task(description="A not so simple task"),
         ],
     )
     user_3 = User(name="User 3", fullname="Real Human")

     session.add_all([user_1, user_2, user_3])

     session.commit()

