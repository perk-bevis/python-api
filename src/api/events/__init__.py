# lấy router từ file routing.py (import tương đối, cùng thư mục)
from .routing import router  

# định nghĩa __all__ để khi dùng "from module import *" 
# thì chỉ export ra biến 'router', ẩn các biến/hàm khác
__all__ = ['router']