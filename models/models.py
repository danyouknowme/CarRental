from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(Text, nullable=False)
    lastname = Column(Text, nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(Text, nullable=False)

    car = relationship("CarModel", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, firstname={self.firstname!r}, lastname={self.lastname!r}, age={self.age!r}, phone={self.phone!r})"


class CarModel(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, nullable=False)
    brand = Column(Text, nullable=False)
    model = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("UserModel", back_populates="car")

    def __repr__(self):
        return f"Car(id={self.id!r}, brand={self.brand!r}, model={self.model!r}, price={self.price!r}, user_id={self.user_id!r})"
