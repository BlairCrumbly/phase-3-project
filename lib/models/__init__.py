import sqlite3

CONN = sqlite3.connect('lib/company.db')
CURSOR = CONN.cursor()

print("Connected to the database:", CONN)