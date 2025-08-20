from fastapi import APIRouter
# Tạo một router mới (bộ định tuyến API mới) bằng cách gọi APIRouter(
router = APIRouter()

@router.get("")
def read_events():
    return {
        "items": [1,2,3]
    }

@router.get("")
def get_event():
    return {
        "items": [1,2,3]
    }