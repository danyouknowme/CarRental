# Car Rental

The car rental database contains the initials data of the users and rent cars.

## Getting Started
### Install required packages
Go to the directory and install the required packages
  ```python
  pip install -r requirements.txt
  ```
### Create the database and table schema and add initial data
Go to the directory and create "sample.db" using schema commands in a file
  ```python
  sqlite3 car_rental.db < db.schema
  ```
Open the database file with the sqlite command line utility
  ```python
  sqlite3 car_rental.db
  ```
Import the data from csv to the database file
  ```python
  sqlite> .mode csv
  sqlite> .import data/users.csv users
  sqlite> .import data/cars.csv cars
  ```
### Configure and run the application
Run the application
  ```python
  python main.py
  ```
## Project Description

- Domian Diagram

![Domian_Diagram](https://user-images.githubusercontent.com/78087668/165595733-52501c36-bdd7-4485-8ce2-8822fc162060.png)

- Package Diagram

![Package Diagram](https://user-images.githubusercontent.com/78087668/165595347-4b9e4fee-e214-4408-94e9-27675fb922f2.png)

- Class Diagram

![Class Diagram](https://user-images.githubusercontent.com/78087668/165597649-643d7d89-b592-4837-80a3-2c8d4a18cedf.png)

