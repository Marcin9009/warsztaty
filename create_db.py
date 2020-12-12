from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTabl
CREATE_DB = "CREATE DATABASE confi_db"