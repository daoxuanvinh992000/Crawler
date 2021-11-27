import requests
from bs4 import BeautifulSoup

def call_request(url):
    return requests.get(url)

def get_bs_object(job_url):
    response = call_request(job_url)
    if response.status_code == 200: #.status_code kiểm tra trạng thái 200 là thành công, 3**: không có quyền, 4**: not found, ̀**: server lỗi
        html_text = response.text
        bs = BeautifulSoup(html_text, 'html.parser')
        return bs

