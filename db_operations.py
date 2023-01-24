from datetime import datetime
import pymysql
from config import *


def get_phones():
    """ Возращает список всех id и phones"""
    try:
        con = pymysql.connect(
            host='localhost',
            port=3306,
            user=user1,
            password=password1,
            database=db_name,
            # charset='utf-8',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with con.cursor() as cursor:
                select = "SELECT id, number FROM phone;"
                cursor.execute(select)
                rows = cursor.fetchall()
        finally:
            con.close()
            list_id = []
            list_phone = []
            for i in rows:
                list_id.append(i['id'])
                list_phone.append(i['number'])
            return list_id, list_phone

    except Exception as e:
        print('ERROR')
        print(e)


def get_all_phones():
    """ Возращает список всех app_id и app_hash"""
    try:
        con = pymysql.connect(
            host='localhost',
            port=3306,
            user=user1,
            password=password1,
            database=db_name,
            # charset='utf-8',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with con.cursor() as cursor:
                select = "SELECT app_id, app_hash, number FROM phone;"
                cursor.execute(select)
                rows = cursor.fetchall()
        finally:
            con.close()
            list_app_id = []
            list_app_hash = []
            list_number = []
            for i in rows:
                list_app_id.append(i['app_id'])
                list_app_hash.append(i['app_hash'])
                list_number.append(i['number'])
            return list_app_id, list_app_hash, list_number

    except Exception as e:
        print('ERROR')
        print(e)


def post_sell(id, name):
    """ Заносит в базу информацию о том, что сообщение отправлено """
    try:
        con = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with con.cursor() as cursor:
                insert_sell = f'INSERT INTO sell (phone_id, name) VALUES ({id}, "{name}");'
                cursor.execute(insert_sell)
                con.commit()
        finally:
            con.close()

    except Exception as e:
        print('ERROR')
        print(e)


def post_last_sell(list_id):
    """ Заносит в базу информацию о том, когда было отправлено последнее сообщение """
    try:
        con = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with con.cursor() as cursor:
                now = datetime.now()
                for id in list_id:
                    indic = cursor.execute(f'SELECT id FROM last_sell WHERE phone_id={id};')
                    if indic == 0:
                        insert_sell = f'INSERT INTO last_sell (phone_id, last_send) VALUES ({id}, "{now}");'
                    else:
                        insert_sell = f'UPDATE last_sell SET last_send = "{now}" WHERE phone_id = {id};'
                    cursor.execute(insert_sell)
                    con.commit()
        finally:
            con.close()

    except Exception as e:
        print('ERROR')
        print(e)
