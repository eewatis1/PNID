import sqlite3
import os

DB_PATH = 'pnid.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)')

def add_item(name):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('INSERT INTO items (name) VALUES (?)', (name,))

def get_items():
    if not os.path.exists(DB_PATH):
        return []
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute('SELECT name FROM items').fetchall()