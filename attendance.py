import re
import sqlite3
from datetime import datetime

# 텍스트 파일에서 내용을 읽어오는 함수
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# SQLite DB에 연결하고 테이블 생성
def initialize_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # `id`는 PRIMARY KEY이며, 자동 증가(autoincrement)하도록 설정
    print("테이블생성")
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS kakaoEntries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        status TEXT NOT NULL,
        date TEXT NOT NULL
    )
    ''')
    conn.commit()
    return conn

# "들어왔습니다" 및 "나갔습니다" 줄을 처리하여 DB에 저장
def process_line(conn, line, status):
    cursor = conn.cursor()

    # 이름 추출: "님이" 앞의 이름 부분 추출, "@"가 있을 경우 "@" 앞 부분 추출
    name_match = re.search(r'([^\s@]+) (?:@[^\s]*)?님이', line)
    
    # 날짜 추출: 줄의 시작 부분에서 날짜 추출 (포함된 날짜 포맷 사용)
    date_match = re.search(r'\d{4}\. \d{1,2}\. \d{1,2}\.', line)
    
    if name_match and date_match:
        name = name_match.group(1)
        date_str = date_match.group(0)
        date_obj = datetime.strptime(date_str, '%Y. %m. %d.').strftime('%Y-%m-%d')
        
        # 데이터 삽입
        cursor.execute('''
        INSERT INTO kakaoEntries (name, status, regdate) 
        VALUES (?, ?, ?)
        ''', (name, status, date_obj))
        
        conn.commit()

# 텍스트 파일 경로
file_path = 'attendancefile.txt'  # 여기에 입력 텍스트 파일 경로를 넣으세요

# 데이터베이스 파일 경로
db_path = 'attendance.db'  # 여기에 DB 파일의 경로를 넣으세요

# 텍스트 파일에서 내용 읽기
text = read_text_from_file(file_path)

# SQLite DB 초기화 및 연결
conn = initialize_db(db_path)

# 텍스트 줄별로 처리
lines = text.strip().split('\n')
for line in lines:
    if "들어왔습니다" in line:
        process_line(conn, line, "IN")
    elif "나갔습니다" in line:
        process_line(conn, line, "OUT")

# 연결 닫기
conn.close()

print(f"데이터가 '{db_path}'에 성공적으로 저장되었습니다.")
