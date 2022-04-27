from utils.car_rental import CarRental
from models.car_model import CarModel
from models.user_model import UserModel

car_rental = CarRental()


print(car_rental.user().get_user_by_id(4))
print(car_rental.user().get_all_users())

print(car_rental.car().get_all_cars())
print(car_rental.car().get_cars_by_brand("HONDA"))
print(car_rental.car().get_car_by_user_id(1))
print(car_rental.car().get_cars_by_sort_price())

# Create new user and insert to database
new_user = UserModel(firstname="Thanathip", lastname="Suwannakhot", age=20, phone="0951683442")
car_rental.user().create_new_user(new_user)
# Create a new rental car and rented by the new user
new_rental = CarModel(brand="MAZDA", model="Mazda 4", price=1300, user_id=new_user.id)
car_rental.car().create_new_rental_car(new_rental)
