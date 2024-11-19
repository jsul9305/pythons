import requests
from bs4 import BeautifulSoup
import sqlite3

# 1. 페이지 요청
url = "http://marathon.pe.kr/index_calendar.html"
response = requests.get(url)

# 2. BeautifulSoup으로 페이지 파싱
soup = BeautifulSoup(response.content, 'html.parser')

# 3. 원하는 데이터 추출 (예: 대회 일정)
# 예시: 일정이 table 태그에 들어가 있다고 가정
events = []
table = soup.find('table')  # 대회 정보가 들어간 테이블 선택
rows = table.find_all('tr')  # 각 대회 행을 선택

# 크롤링 예시
for row in rows:
    cols = row.find_all('td')
    if len(cols) > 1:
        date = cols[0].text.strip()  # 첫 번째 열: 날짜
        event = cols[1].text.strip()  # 두 번째 열: 대회명
        location = cols[2].text.strip()  # 세 번째 열: 장소
        url = cols[3].find('a')['href'] if cols[3].find('a') else ''  # 네 번째 열: 대회 사이트 링크 (있는 경우)
        events.append({
            'date': date,
            'event': event,
            'location': location,
            'url': url  # URL 추가
        })


print(events)
