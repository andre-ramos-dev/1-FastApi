from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.models.user import UserSchema, UserModel
from apps.utils import get_db

# APIRouter creates path operations for user module

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=UserSchema)
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    _user = UserModel(
        first_name=user.first_name, last_name=user.last_name, age=user.age
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


@router.get("/{first_name}/", response_model=UserSchema)
async def get_user(first_name: str, db: Session = Depends(get_db)):
    _user = db.query(UserModel).filter_by(first_name=first_name).first()
    return _user


@router.get("/", response_model=List[UserSchema])
async def get_user(db: Session = Depends(get_db)):
    _users = db.query(UserModel).all()
    return _users
