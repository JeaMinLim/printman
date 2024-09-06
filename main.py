import atexit
import tkinter as tk
from tkinter import simpledialog
import os

DRIVE_LETTER = "Z:"

def get_user_input():
    # 
    root = tk.Tk()
    root.withdraw()  # 메인 윈도우 숨기기
    path = simpledialog.askstring("Input", "경로를 입력하세요:")
    username = simpledialog.askstring("Input", "사용자 이름을 입력하세요:")
    password = simpledialog.askstring("Input", "암호를 입력하세요:", show='*')

    return path, username, password

def connect_network_drive(PATH, USERNAME, PASSWORD):
    command = f'net use {DRIVE_LETTER} {PATH} /user:{USERNAME} {PASSWORD}'
    result = os.system(command)

    if result == 0:
        print(f"성공적으로 {DRIVE_LETTER} 드라이브에 연결되었습니다.")
    else:
        print("연결에 실패했습니다. 정보를 확인하세요.")

def cleanup():
    print("프로그램이 종료됩니다.")
    disconnect_command = f"net use {DRIVE_LETTER} /delete"
    os.system(disconnect_command)

def main():
    print("프로그램이 시작되었습니다.")
    path, username, password = get_user_input()
    print(f"경로: {path}")
    print(f"사용자 이름: {username}")
    print(f"암호: {password}")

    connect_network_drive(path, username, password)

if __name__ == "__main__":
    atexit.register(cleanup)
    main()