from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTabl
CREATE_DB = "CREATE DATABASE confi_db;"
CREATE_USER_TABLE = """CREATE TABLE users(
    id serial PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    hashed_password varchar(80))"""

CERATE_MASSANGES_TABLE = """CREATE TABLE massages(
    id serial PRIMARY KEY,
    from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    creation_data timestamp default current_timestamp)"""

USER = "postgres"
PASSWORD = "coderslab"
HOST = "127.0.0.1"
try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("created datebase")
    except DuplicateDatabase as d:
        print("exist database", d)
    cnx.close()
except OperationalError as o: print("Error")


try:
    cnx = connect(database="confi_db", user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_USER_TABLE)
        print("Table user")
    except DuplicateDatabase as d:
        print("table exists", d)

    try:
        cursor.execute(CERATE_MASSANGES_TABLE)
        print("Table massage")
    except DuplicateDatabase as d:
        print("table exist", d)
    cnx.close()
except OperationalError as o:
    print("Error", o)




