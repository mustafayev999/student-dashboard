import sqlite3

def get_connection():
    # Məlumatlar yerli student_data.db faylında saxlanılacaq
    conn = sqlite3.connect("student_data.db", check_same_thread=False)
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Tətbiq başladqda cədvəlin mövcudluğunu təmin edirik
create_table()

def add_student(name, score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, score) VALUES (?, ?)", (name, score))
    conn.commit()  # Məlumatı bazada yadda saxlayır
    conn.close()

def get_students(search_query=""):
    conn = get_connection()
    cursor = conn.cursor()
    if search_query:
        cursor.execute("SELECT name, score FROM students WHERE name LIKE ?", (f"%{search_query}%",))
    else:
        cursor.execute("SELECT name, score FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows