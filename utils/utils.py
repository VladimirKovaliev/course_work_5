import psycopg2
import os
import json
#
# параметры подключения к БД
# params = {
#     "host": "localhost",
#     "user": "postgres",
#     "password": os.getenv('DB_PSW'),
#     "port": "5432",
#     "database": "cw_database"
# }
#
# def close_all_connections(db_params):
#     # установка соединения с PostgreSQL сервером
#     conn = psycopg2.connect(
#         host=db_params['host'],
#         user=db_params['user'],
#         password=db_params['password'],
#         port=db_params['port']
#     )
#
#     # создание объекта-cursor
#     cursor = conn.cursor()
#
#     # закрытие соединений к cw_database
#     cursor.execute("""
#         SELECT pg_terminate_backend(pg_stat_activity.pid)
#         FROM pg_stat_activity
#         WHERE pg_stat_activity.datname = 'cw_database'
#     """)
#
#     # закрытие соединения с PostgreSQL сервером
#     cursor.close()
#     conn.close()
# def create_database():
#     # установка соединения с PostgreSQL сервером
#     conn = psycopg2.connect(
#         host=params['host'],
#         user=params['user'],
#         password=params['password'],
#         port=params['port']
#     )
#
#     # создание объекта-cursor
#     cursor = conn.cursor()
#
#     # закрытие соединения с текущей базой данных, если оно открыто
#     cursor.execute("SELECT 1;")
#     cursor.close()
#     conn.close()
#
#     # создание базы данных cw_database
#     conn = psycopg2.connect(
#         host=params['host'],
#         user=params['user'],
#         password=params['password'],
#         port=params['port']
#     )
#     cursor = conn.cursor()
#     cursor.execute("CREATE DATABASE cw_database;")
#
#     # закрытие соединения с PostgreSQL сервером
#     cursor.close()
#     conn.close()
#     print("Database created successfully")
#
# def create_tables(params):
#     # установка соединения с БД
#     conn = psycopg2.connect(**params)
#     cursor = conn.cursor()
#
#     # создание таблицы employers
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS employers (
#             id SERIAL PRIMARY KEY,
#             name TEXT
#         )
#     """)
#
#     # создание таблицы vacancies
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS vacancies (
#             id SERIAL PRIMARY KEY,
#             name TEXT,
#             salary_min INTEGER,
#             salary_max INTEGER,
#             employer_id INTEGER REFERENCES employers(id)
#         )
#     """)
#     # сохранение изменений
#     conn.commit()
#
#     # закрытие соединения с БД
#     cursor.close()
#     conn.close()
#     print("Tables created successfully")
#
#
# def insert_data(params):
#     # установка соединения с БД
#     conn = psycopg2.connect(**params)
#     cursor = conn.cursor()
#
#     # добавление данных в таблицу employers
#     employers_data = [
#         ('Company A',),
#         ('Company B',)
#     ]
#     cursor.executemany("INSERT INTO employers (name) VALUES (%s)", employers_data)
#
#     # добавление данных в таблицу vacancies
#     vacancies_data = [
#         ('Vacancy A', 1000, 2000, 1),
#         ('Vacancy B', 1500, 2500, 1),
#         ('Vacancy C', 2000, 3000, 2),
#         ('Vacancy D', 3000, 4000, 2)
#     ]
#     cursor.executemany("INSERT INTO vacancies (name, salary_min, salary_max, employer_id) VALUES (%s, %s, %s, %s)", vacancies_data)
#
#     # сохранение изменений
#     conn.commit()
#
#     # закрытие соединения с БД
#     cursor.close()
#     conn.close()
#     print("Data inserted successfully")
#
#
# create_database()
# create_tables(params)

params = {
    "host": "localhost",
    "user": "postgres",
    "password": os.getenv('DB_PSW'),
    "port": "5432",
}

def create_database(database_name: str):
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    # проверка на существование базы данных
    cur.execute("""
        SELECT COUNT(*)
        FROM pg_catalog.pg_database
        WHERE datname = %s
    """, (database_name,))
    exists = cur.fetchone()[0]

    # удаление базы данных, если она существует
    if exists:
        cur.execute(f'DROP DATABASE {database_name}')

    # создание базы данных
    cur.execute(f'CREATE DATABASE {database_name}')

    cur.close()
    conn.close()

def save_json_to_database(json_file):
    conn = psycopg2.connect(dbname='cw_database')
    with conn.cursor() as cur:



create_database('cw_database')