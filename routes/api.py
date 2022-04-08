from fastapi import APIRouter
from apps.endpoints import user

router = APIRouter()
router.include_router(user.router)