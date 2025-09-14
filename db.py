import sqlite3

DB = "reflection.db"

def init_db():
    conn = sqlite3.connect(DB)
    cursor =conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        journal TEXT,
        intention TEXT,
        dream TEXT,
        priorities TEXT,
        reflection TEXT)
    """)
    conn.commit()
    conn.close()
    print("✅ Database initialized.")

def insert_entry(date, journal, intention, dream, priorities, reflection):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO entries (date, journal, intention, dream, priorities, reflection)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (date, journal, intention, dream, priorities, reflection))
    conn.commit()
    conn.close()
    print("✅ Entry saved.")

def fetch_entry(date):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries WHERE date = ?", (date,))
    entry = cursor.fetchone()
    conn.close()
    return entry