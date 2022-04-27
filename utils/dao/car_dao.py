from models.models import CarModel
from sqlalchemy.orm.session import Session


class CarDao:
  def __init__(self, session: Session):
    self.__session = session;

  def get_all_cars(self):
    return self.__session.query(CarModel).all()

  def get_cars_by_brand(self, brand: str):
    return self.__session.query(CarModel).filter(CarModel.brand == brand).all()

  def get_car_by_user_id(self, user_id: int):
    return self.__session.query(CarModel).filter(CarModel.user_id == user_id).all()

  def get_cars_by_sort_price(self):
    car_list = self.get_all_cars()
    return sorted(car_list, key=lambda car: car.price)

  def create_new_rental_car(self, car_rental: CarModel):
    self.__session.add(car_rental)
    self.__session.commit()
    print("Insert car rental data to the database successfully!")
    print(car_rental)
