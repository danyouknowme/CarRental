from utils.car_rental import CarRental
from models.car_model import CarModel

car_rental = CarRental()


print(car_rental.user().get_user_by_id(4))
print(car_rental.user().get_all_users())

print(car_rental.car().get_all_cars())
print(car_rental.car().get_cars_by_brand("HONDA"))
print(car_rental.car().get_car_by_user_id(1))
print(car_rental.car().get_cars_by_sort_price())

new_rental = CarModel(brand="MAZDA", model="Mazda 2", price=1300, user_id=1)

car_rental.car().create_new_rental_car(new_rental)
