from typing import Union
# import lớp FastAPI từ thư viện fastapi
from fastapi import FastAPI
from api.events import router as events_router

# tạo 1 app FastAPI
app = FastAPI()
app.include_router(events_router, prefix="/api/events")

# định nghĩa một route GET tại đường dẫn "/"
# khi truy cập "/" thì FastAPI sẽ gọi hàm bên dưới
@app.get("/")
def home():   # đặt tên tùy ý
    # trả về 1 dict Python, FastAPI sẽ tự động chuyển thành JSON
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
 
@app.get("/healthz")
def read_api_health():  
    return {"status": "ok"}