# coding:utf-8
import pymysql

# MySQL Connection 연결 (pymysql.cursors.DictCursor는 딕셔너리 형태로 출력되고 이 부분을 생략하면 결과가 튜플 형태로 출력)
conn = pymysql.connect(host='localhost', user='kevin', password='XXXX', db='korea', charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# SQL문 실행
curs.execute("select * from day24")

# 데이터 Fetch
rows = curs.fetchall()
for row in rows:
    print(row)

# Connection 닫기
conn.close()
