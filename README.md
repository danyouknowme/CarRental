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

- [Domain Diagram](../../wiki/Domain-Diagram)
- [Package Diagram](../../wiki/Package-Diagram)
- [Class Diagram](../../wiki/Class-Diagram)

