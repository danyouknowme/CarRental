from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dao.user_dao import UserDao
from utils.dao.car_dao import CarDao


class CarRental:

  def __init__(self, connection_url="sqlite:///car_rental.db"):
    engine = create_engine(connection_url)
    session = sessionmaker(bind=engine)
    self.__db_session = session()


  def user(self):
    return UserDao(self.__db_session)

  def car(self):
    return CarDao(self.__db_session)
