from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from models.base_model import Base

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
