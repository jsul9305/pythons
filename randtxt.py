import tkinter as tk
from tkinter import filedialog
import random
import shutil
import os
import time

# 줄을 저장할 배열
lines = []
file_path =""

# 파일에서 텍스트를 읽어오는 함수
def load_file():
    global lines, file_path
    file_path = filedialog.askopenfilename(title="텍스트 파일을 선택하세요")
    if file_path:
        backup_path = create_backup(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        result_label.config(text="파일이 로드되었습니다! 이제 '랜덤 돌리기' 버튼을 눌러주세요.")

# 백업 파일 생성 함수
def create_backup(orign_path):
    backup_path = orign_path + time.strftime('%Y%m%d%H%M%S') + ".backup"
    shutil.copy2(orign_path, backup_path)
    return backup_path

# 파일에 변경사항을 저장하는 함수
def save_file():
    global file_path, lines
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


# 랜덤으로 한 줄을 선택하는 함수
def choose_random_line():
    global lines
    if lines:
        random_index = random.randint(0, len(lines)-1) # 랜덤 인덱스 선택
        random_line = lines.pop(random_index).strip()  # 줄에서 선택 후 배열에서 제거
        save_file() # 변경된 배일을 파일에 저장
        result_label.config(text=random_line)
    else:
        result_label.config(text="파일을 먼저 로드해주세요!")

# GUI 설정
root = tk.Tk()
root.title("Random Line Picker")

# 레이블 생성
label = tk.Label(root, text="텍스트 파일에서 랜덤으로 한 줄을 선택합니다:")
label.pack(pady=10)

# 파일 선택 버튼 생성
load_button = tk.Button(root, text="파일 열기", command=load_file)
load_button.pack(pady=10)

# 랜덤 돌리기 버튼 생성
random_button = tk.Button(root, text="랜덤 돌리기", command=choose_random_line)
random_button.pack(pady=10)

# 결과를 표시할 레이블
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# GUI 시작
root.mainloop()