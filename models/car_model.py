from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base

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
