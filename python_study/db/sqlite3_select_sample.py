import sqlite3

# SQLite DB 연결
conn = sqlite3.connect("test.db")

# Connection 으로 부터 Cursor 생성
cursor = conn.cursor()

# SQL 쿼리 실행
cursor.execute("SELECT * FROM stocks ORDER BY price")

# 데이터 Fetch
rows = cursor.fetchall()
for row in rows:
    print(row)

# Connection 닫기
conn.close()