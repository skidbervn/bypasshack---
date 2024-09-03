import requests
import time
import os
from datetime import datetime

# Mã màu ANSI
RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

def fetch_data(fluxus_link):
    # Xây dựng URL API với liên kết Fluxus
    api_url = f"https://duckcute-zeta.vercel.app/adlink?link={fluxus_link}"

    try:
        # Gửi yêu cầu GET đến API
        response = requests.get(api_url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP

        # Phân tích JSON từ phản hồi
        data = response.json()

        # Lấy giá trị của 'key'
        key_value = data.get('key', 'No key found')
        return key_value
    except requests.RequestException as e:
        print(f"Đã xảy ra lỗi: {e}")
        return None

def print_slowly(text, delay=0.05):
    """In văn bản một cách từ từ với khoảng thời gian trễ giữa các ký tự."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Để xuống dòng sau khi in xong

def print_centered_ascii(ascii_text, width, color_code):
    """In văn bản ASCII căn giữa với chiều rộng cụ thể và màu sắc."""
    lines = ascii_text.split('\n')
    colored_text = f"{color_code}{ascii_text}{RESET}"
    for line in colored_text.split('\n'):
        centered_line = line.center(width)
        print(centered_line)

def get_current_time():
    """Trả về thời gian hiện tại theo định dạng giờ:phút:giây"""
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def get_current_date():
    """Trả về ngày hiện tại theo định dạng ngày-tháng-năm"""
    now = datetime.now()
    return now.strftime("%d-%m-%Y")

def get_location():
    """Trả về vị trí giả lập, có thể thay đổi tùy ý"""
    return "Hà Nội, Việt Nam"

if __name__ == "__main__":
    # Văn bản ASCII cần căn giữa và màu sắc
    ascii_art = """
____  _   _ ____  _   _ _   _ __  __ _____ ___   
/ ___|| | | |  _ \| | | | | | |  \/  | ____/ _ \  
\___ \| | | | |_) | |_| | | | | |\/| |  _|| | | | 
 ___) | |_| |  __/|  _  | |_| | |  | | |__| |_| | 
|____/ \___/|_|   |_| |_|\___/|_|  |_|_____\___/  
    """
    color_code = BLUE  # Mã màu ANSI cho màu xanh dương

    # Tính toán chiều rộng của màn hình
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80  # Chiều rộng mặc định nếu không thể lấy kích thước màn hình

    # In văn bản ASCII căn giữa với màu sắc
    print_centered_ascii(ascii_art, width, color_code)

    # In thông tin ngày giờ và vị trí
    print(f"{BLUE}Ngày: {RESET}{get_current_date()}")
    print(f"{BLUE}Giờ: {RESET}{get_current_time()}")
    print(f"{BLUE}Vị trí: {RESET}{get_location()}")
    
    # Nhập liên kết Fluxus từ người dùng
    fluxus_link = input("Nhập liên kết Fluxus: ").strip()

    # Lấy dữ liệu từ API
    key_value = fetch_data(fluxus_link)

    if key_value is not None:
        print("\nGiá trị key nhận được:")
        print_slowly(key_value)
    else:
        print("Không thể lấy dữ liệu.")
