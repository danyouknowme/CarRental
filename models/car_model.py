from sqlalchemy import Column, Integer, Text
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CarModel(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, nullable=False)
    brand = Column(Text, nullable=False)
    model = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Car(id={self.id!r}, brand={self.brand!r}, model={self.model!r}, price={self.price!r}, user_id={self.user_id!r})"
