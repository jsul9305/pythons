import re
import sqlite3
from datetime import datetime

# DB 경로 설정
db_path = 'attendance.db'
# 텍스트 파일 경로 설정
file_path = 'juslist.txt'



# 데이터 파싱 및 DB 입력 함수
def insert_data_to_db(line, db_path):
    # DB 연결
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 테이블 생성 (이미 존재하면 무시)
    cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      state TEXT NOT NULL,
                      date_time TEXT NOT NULL
                      )''')

    # 정규표현식을 사용하여 데이터 파싱
    # pattern = r'([\w\s]+)(?: @[\w\d_]+)?, (\d{4}\. \d{1,2}\. \d{1,2}\. (오전|오후) \d{3,4}), \(\d{5}(?:, [^()]+)?\)'    match = re.match(pattern, line)

    if match:
        name = match[1].strip()
        date_time_str = match[2].strip()

        # 시간 변환 (오전/오후 처리)
        time_pattern = r'(\d{4})\. (\d{1,2})\. (\d{1,2})\. (오전|오후) (\d{3,4})'
        date_match = re.match(time_pattern, date_time_str)

        if date_match:
            year, month, day, period, time_str = date_match.groups()


            # 시간과 분을 추출
            if len(time_str) == 4:
                hour = int(time_str[:2])  # 앞의 두 자리가 시간
                minute = int(time_str[2:])  # 뒤의 두 자리가 분
            elif len(time_str) == 3:
                hour = int(time_str[0])  # 첫 번째 자리가 시간
                minute = int(time_str[1:])  # 나머지 두 자리가 분
            else:
                hour = int(time_str)  # 시간만 있는 경우 (예: "9")
                minute = 0  # 분은 0으로 설정

            # 오후인 경우 시간 변환 (24시간 형식으로)
            if period == '오후' and hour != 12:
                hour += 12
            elif period == '오전' and hour == 12:
                hour = 0  # 오전 12시는 0시로 변환

            formatted_date_time = f"{year}-{int(month):02d}-{int(day):02d} {hour:02d}:{minute:02d}:00"

            
            print("INSERT INTO members (name, state, date_time) VALUES (?, ?, ?)",
                           (name, 'IN', formatted_date_time))

            # DB에 데이터 삽입
            #cursor.execute("INSERT INTO members (name, state, date_time) VALUES (?, ?, ?)",
            #               (name, 'IN', formatted_date_time))
    
    # 변경 사항 저장 및 DB 연결 종료
    # conn.commit()
    conn.close()

# 텍스트 파일에서 데이터를 한 줄씩 읽어와서 처리하는 함수
def process_file_by_line(file_path, db_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            insert_data_to_db(line.strip(), db_path)
    print("모든 데이터가 DB에 성공적으로 저장되었습니다.")

# 텍스트 파일의 데이터를 한 줄씩 처리
process_file_by_line(file_path, db_path)