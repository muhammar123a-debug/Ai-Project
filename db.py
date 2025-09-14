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

def fetch_entries():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows