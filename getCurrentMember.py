import sqlite3

# SQLite DB 경로 설정
db_path = 'attendance.db'  # 실제 사용 중인 DB 파일의 경로로 변경

def get_current_members(db_path):
    # DB 연결
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 현재 참여하고 있는 멤버 목록을 추출하는 SQL 쿼리
    # 이름이 같고, 마지막 상태가 'IN'인 멤버만 조회
    query = """
    SELECT name 
    FROM kakaoEntries 
    WHERE id IN (
        SELECT MAX(id)
        FROM kakaoEntries
        GROUP BY name
        HAVING status = 'IN'
    )
    """

    cursor.execute(query)
    members = cursor.fetchall()

    # DB 연결 종료
    conn.close()

    # 추출된 멤버 목록 출력
    if members:
        print("현재 참여하고 있는 멤버 목록:")
        for member in members:
            print(member[0])
    else:
        print("현재 참여하고 있는 멤버가 없습니다.")
    print(len(members))

# 함수 실행
get_current_members(db_path)
