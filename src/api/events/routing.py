from fastapi import APIRouter
# import lớp APIRouter để tạo "router" con, gom nhóm các endpoint lại với nhau
from .schemas import EventSchema
# Tạo một router mới (bộ định tuyến API mới)
router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class BlogModal():
    title: str
    content: str
    published: str

@router.post("/create/{id}")
def create_new_blog(blog: BlogModal, id: int, version: 1):
    return blog

# Định nghĩa 1 endpoint GET tại đường dẫn "" (chuỗi rỗng = root path của router này)
# Nếu include_router(router, prefix="/events") thì endpoint thực tế sẽ là /events
@router.get("/{blog_home}")
def read_events():
    """
    💡 Hàm này miêu tả... 
    """
    return {
        "items": [1,2,3]
    }

# Lại định nghĩa thêm 1 endpoint GET cũng tại đường dẫn "" (trùng với cái trên)
# => route trên (read_events) sẽ bị override, chỉ còn route này hoạt động
@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {
        "id": event_id
    }
