import re

# 파일 이름 설정
input_file_name = 'juslist.txt'  # 원본 텍스트 파일
output_file_name = 'formatted_juslist.txt'  # 변환된 내용을 저장할 파일

# 정규 표현식을 정의하여 각 줄의 정보를 추출
line_pattern = re.compile(r'(\S+)\s*(@\S+)?\s*,\s*(\d{4}\.\s*\d{1,2}\.\s*\d{1,2}\.\s*[오후|오전]+\s*\d{4}),\s+\((\d{5}),\s*(\d{4}-\d{2}-\d{2})\s*[오후|오전]+\s*\d{2}:\d{2}\)')

def format_line(line):
    # 정규 표현식을 사용하여 필요한 정보를 추출
    match = line_pattern.match(line)
    if match:
        name, handle, date, number, last_date = match.groups()
        # 정규식에 따른 변환 규칙 적용
        formatted_handle = handle if handle else ""
        formatted_line = f"{name} {formatted_handle}, {date}, ({number}, {last_date})"
        return formatted_line
    return None

# 입력 파일을 열고 한 줄씩 읽어서 변환 후 출력 파일에 저장
with open(input_file_name, 'r', encoding='utf-8') as infile, open(output_file_name, 'w', encoding='utf-8') as outfile:
    for line in infile:
        formatted_line = format_line(line.strip())
        if formatted_line:
            outfile.write(formatted_line + '\n')

print(f"파일 '{output_file_name}'로 저장되었습니다.")