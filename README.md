[![PyPi Package Version](https://img.shields.io/pypi/v/pyTelegramBotAPI.svg)](https://pypi.python.org/pypi/pyTelegramBotAPI)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pyTelegramBotAPI.svg)](https://pypi.python.org/pypi/pyTelegramBotAPI)
[![Documentation Status](https://readthedocs.org/projects/pytba/badge/?version=latest)](https://pytba.readthedocs.io/en/latest/?badge=latest)
[![PyPi downloads](https://img.shields.io/pypi/dm/pyTelegramBotAPI.svg)](https://pypi.org/project/pyTelegramBotAPI/)
[![PyPi status](https://img.shields.io/pypi/status/pytelegrambotapi.svg?style=flat-square)](https://pypi.python.org/pypi/pytelegrambotapi)

# <p align="center">huynhminhkhoi
Module Giúp Bạn Né Bug Nhẹ
Hãy Cùng Khám Phá Thư Viện Để Sử Dụng Nhé!
## Nội Dung

* [Cài Đặt Thư Viện](#c%C3%A0i-%C4%91%E1%BA%B7t-th%C6%B0-vi%E1%BB%87n)
* [Các Hàm Cơ Bản](#)
* [Check Key Ngày Hoặc Key Vip](#check-key-ngay-hoac-key-vip)
## Cài Đặt Thư Viện
Thư viện này đã được thử nghiệm với Python 3.11. Cách cài đặt thư viện:
```
$ pip install huynhminhkhoi
```
## Các Hàm Cơ Bản
Lớp huynhminhkhoi (được định nghĩa trong \__init__.py) gói gọn 2 lệnh gọi API. Nó cung cấp các chức năng như `get_key` và `check_key` 

Tạo 1 Tệp Có Tên Bất Kì Ví Dụ `khoidz.py`. Sau đó, mở tệp và tham khảo đoạn code dưới đây:
```python
import huynhminhkhoi
import requests
ip_get = requests.get('http://ip-api.com/json/').json()['query']
client = huynhminhkhoi.Api.client("name_key", list_obj = list_token_link)
get_key = client.get_key(ip = ip_get)
print(get_key)
```
*Note: `name_key` sẽ là tên key của bạn, 
`list_token_link` sẽ là danh sách lần lượt chứa token link1s và web chứa key của bạn.*

Bạn có thể nhìn ví dụ dưới đây về danh sách chứa token và web chứa key tôi gợi ý ở trên:
```python
import huynhminhkhoi
import requests
ip_get = requests.get("http://ip-api.com/json/").json()['query']
list_token_link = ["your_token", "https://huynhminhkhoidev.x10.mx/key.html?keyhomnay="]
client = huynhminhkhoi.Api.client("name_key", list_obj = list_token_link)
get_key = client.get_key(ip = ip_get)
print(get_key)
```
## Check Key Ngày Hoặc Key Vip

