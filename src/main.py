from typing import Union
# import lớp FastAPI từ thư viện fastapi
from fastapi import FastAPI

# tạo 1 app FastAPI
app = FastAPI()

# định nghĩa một route GET tại đường dẫn "/"
# khi truy cập "/" thì FastAPI sẽ gọi hàm bên dưới
@app.get("/")
def home():   # đặt tên tùy ý
    # trả về 1 dict Python, FastAPI sẽ tự động chuyển thành JSON
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}