import sqlite3 as bd

create_table = """
        CREATE TABLE IF NOT EXISTS users(
        user_id int primary key ,
        surname text not null,
        user_name text not null,
        patronymic text not null,
        dates text not null
        );"""

with bd.connect("db.sqlite3") as connection:
    cursor = connection.cursor()
    cursor.execute(create_table)
