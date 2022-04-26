from models.car_model import CarModel
from sqlalchemy.orm.session import Session


class CarDao:
  def __init__(self, session: Session):
    self.__session = session;

  def get_all_cars(self):
    return self.__session.query(CarModel).all()
