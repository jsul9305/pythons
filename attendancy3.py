import re
import sqlite3
from datetime import datetime

# DB 경로 설정
db_path = 'attendance.db'
# 텍스트 파일 경로 설정
file_path = 'jusin.txt'

cnt = 0

def parse_and_insert_data(line, db_path):
    # 정규 표현식을 수정하여 다양한 이름과 시간을 인식하도록 설정
    pattern = re.compile(
        r'([^\s,]+(?: [^\s,]+)?(?:@[^\s,]+)?)\s*,\s*(\d{4})\.\s*(\d{1,2})\.\s*(\d{1,2})\.\s*(오전|오후)\s*(\d{1,4})\s*,\s*\(([^)]+)\)'
    )

    match = pattern.match(line.strip())
    if match:
        name_with_tag = match.group(1).strip()
        year, month, day, period, time_str, extra_info = match.groups()[1:]

        # 시간과 분을 올바르게 추출
        if len(time_str) == 4:  # 예: "1059"
            hour = int(time_str[:2])  # 앞의 두 자리가 시간
            minute = int(time_str[2:])  # 뒤의 두 자리가 분
        elif len(time_str) == 3:  # 예: "953"
            hour = int(time_str[0])  # 첫 번째 자리가 시간
            minute = int(time_str[1:])  # 나머지 두 자리가 분
        elif len(time_str) == 2:  # 예: "59"
            hour = int(time_str[0])  # 첫 번째 자리가 시간
            minute = int(time_str[1:])  # 나머지 한 자리가 분
        else:  # 예: "5"
            hour = int(time_str)  # 시간만 있는 경우
            minute = 0

        # 오후인 경우 시간 변환 (24시간 형식으로)
        if period == '오후' and hour != 12:
            hour += 12
        elif period == '오전' and hour == 12:
            hour = 0  # 오전 12시는 0시로 변환

        # 날짜와 시간의 형식을 포맷
        formatted_date_time = f"{year}-{int(month):02d}-{int(day):02d} {hour:02d}:{minute:02d}:00"

        # 이름과 인스타그램 아이디를 추출
        name, instagram_id = parse_name_and_instagram(name_with_tag)

        # 데이터베이스에 입력하는 함수 호출
        insert_data_to_db(name, instagram_id, formatted_date_time, extra_info, db_path)
    else:
        print(f"Invalid data format: {line.strip()}")

def parse_name_and_instagram(name_with_tag):
    # 이름과 인스타그램 아이디를 추출하는 함수
    parts = re.split(r'[@\s]', name_with_tag.strip())
    name = parts[0].strip()
    instagram_id = parts[1].strip() if len(parts) > 1 else None
    return name, instagram_id

def insert_data_to_db(name, instagram_id, date_time, extra_info, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    global cnt
    cnt += 1
    # SQL 쿼리를 변수로 정의
    sql_query = 'INSERT INTO members (name, instagram_id, date_time, state) VALUES (?, ?, ?, ?)'
    
    # 변수로 SQL 쿼리를 실행
    cursor.execute(sql_query, (name, instagram_id, date_time, 'IN'))
    print(sql_query, (name, instagram_id, date_time, 'IN'))
    
    #cursor.execute(sql_query, (name, instagram_id, date_time, 'OUT'))
    #print(sql_query, (name, instagram_id, date_time, 'OUT'))

    conn.commit()
    conn.close()

# 텍스트 파일에서 데이터를 한 줄씩 읽어와서 처리하는 함수
def process_file_by_line(file_path, db_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parse_and_insert_data(line.strip(), db_path)
    print("모든 데이터가 DB에 성공적으로 저장되었습니다.")

# 텍스트 파일의 데이터를 한 줄씩 처리
process_file_by_line(file_path, db_path)
print(f"Total entries processed: {cnt}")