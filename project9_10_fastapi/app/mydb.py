import sqlite3
from app.config import DB_URL

def db_connection():
    conn = sqlite3.connect(DB_URL)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

