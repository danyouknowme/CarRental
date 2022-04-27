from models.user_model import UserModel
from sqlalchemy.orm.session import Session


class UserDao:
  def __init__(self, session: Session):
    self.__session = session

  def get_user_by_id(self, id):
    return self.__session.query(UserModel).filter(UserModel.id == id)[0]

  def get_all_users(self):
    return self.__session.query(UserModel).all()

  def create_new_user(self, user: UserModel):
    self.__session.add(user)
    self.__session.commit()
    print("Insert new user to the database successfully!")
    print(user)
