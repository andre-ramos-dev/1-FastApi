from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from apps.utils import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=True, index=True)
    last_name = Column(String)
    age = Column(Integer, )


class UserSchema(BaseModel):
    first_name: str
    last_name: str = None
    age: int

    class Config:
        orm_mode = True
