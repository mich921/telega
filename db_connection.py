import pymysql
from config import user, password, db_name


try:
    con = pymysql.connect(
        host='109.161.51.224',
        port=3306,
        user=user,
        password=password,
        database=db_name,
        # charset='utf-8',
        cursorclass=pymysql.cursors.DictCursor
    )
    print('Connected successfully ...')
    print('#' * 20)

    try:
        with con.cursor() as cursor:
            select = "SELECT id, number FROM phone;"
            cursor.execute(select)
            rows = cursor.fetchall()
            print(rows)
    finally:
        con.close()

except Exception as e:
    print('ERROR')
    print(e)
