import sqlite3
import time

now =  time
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
conn = sqlite3.connect('C:/SQLite/pydb.db', isolation_level=None)

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")  # 접속 해제conn.close()
# 출처: https://programexplorer.tistory.com/64 [프로그램 탐험가의 개발 세계 탐험기:티스토리]