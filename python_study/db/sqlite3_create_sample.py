import sqlite3

# SQLite DB 연결
conn = sqlite3.connect("test.db")

cursor = conn.cursor()
cursor.execute('''CREATE TABLE stocks (
                    date TEXT, trans TEXT, symbol TEXT, qty REAL, price REAL)''')

cursor.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 150, 35.2)")
cursor.execute("INSERT INTO stocks VALUES ('2006-01-06', 'BUY', 'RHAT', 170, 17)")

conn.commit()

# 데이터 Fetch
rows = cursor.execute("SELECT * FROM stocks ORDER BY price")
for row in rows:
    print(row)

# Connection 닫기
conn.close()
