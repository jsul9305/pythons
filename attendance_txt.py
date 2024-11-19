import re
from datetime import datetime

# 텍스트 파일에서 내용을 읽어오는 함수
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# 결과를 텍스트 파일에 저장하는 함수
def save_to_text_file(output_path, entries):
    with open(output_path, 'w', encoding='utf-8') as file:
        for entry in entries:
            # file.write(f"{entry['name']} - {entry['status']} - {entry['date']}\n")
            file.write(f"{entry}\n")

# "들어왔습니다" 및 "나갔습니다" 줄 추출 및 리스트에 저장
def process_line(line, status):
    # 이름 추출: "님이" 앞의 이름 부분 추출, "@"가 있을 경우 "@" 앞 부분 추출
    # name_match = re.search(r'([^\s@]+) (?:@[^\s]*)?님이', line)
    # name_match = re.search(r'([^\s@]+) (?:@[^\s]*)?님이', line)
    name_match = re.search(r'([^\s@]+)(?:\s+@[^\s]*)?님이', line)
    
    # 날짜 추출: 줄의 시작 부분에서 날짜 추출 (포함된 날짜 포맷 사용)
    # date_match = re.search(r'(\d{4}\. \d{1,2}\. \d{1,2}\.)', line)
    date_match = re.search(r'(\d{4}\.\s*\d{1,2}\.\s*\d{1,2}\.)', line)
    
    if name_match and date_match:
        name = name_match.group(1)
        date_str = date_match.group(0)
        date_obj = datetime.strptime(date_str, '%Y. %m. %d.').strftime('%Y-%m-%d')
        
        # return {'name': name, 'status': status, 'date': date_obj}
        return name
    else:
        name = name_match.group(1) if name_match else None
        date_obj = date_match.group(1) if date_match else None
        # return {'name': name, 'status': status, 'date': date_obj}        
        return name
    return None

# 텍스트 파일 경로
file_path = input("추출대상 ? (txt 파일명 제외)")  # 여기에 입력 텍스트 파일 경로를 넣으세요

# 출력 파일 경로
output_path = file_path+'_output.txt'  # 여기에 출력 텍스트 파일 경로를 넣으세요
file_path = file_path + '.txt'

# 텍스트 파일에서 내용 읽기
text = read_text_from_file(file_path)

# 결과를 저장할 리스트
entries = []

# 텍스트 줄별로 처리
lines = text.strip().split('\n')
for line in lines:
    if "들어왔습니다" in line:
        entry = process_line(line, "IN")
        if entry:
            entries.append(entry)
    elif "나갔습니다" in line:
        entry = process_line(line, "OUT")
        if entry:
            entries.append(entry)

# 결과를 텍스트 파일에 저장
save_to_text_file(output_path, entries)

print(f"데이터가 '{output_path}'에 성공적으로 저장되었습니다.")
