import sqlite3
connection = sqlite3.connect("doctors.db")

connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS doc_schedule (
        id INTEGER PRIMARY KEY AUTOINCREMENT,       
        doctor_id INTEGER NOT NULL,
        schedule_date TEXT,
        start_time TEXT,
        end_time TEXT,
        status TEXT,

        FOREIGN KEY (doctor_id) REFERENCES doc_info(id)
    )
""")

cursor.execute("""
    INSERT INTO doc_schedule (doc_id, schedule_date, start_time, end_time, status)
    VALUES (?, ?, ?, ?, ?)
""", (1, "2026-09-22", "10:00", "13:00", "AVAILABLE"))

cursor.execute("""
    INSERT INTO doc_schedule (doc_id, schedule_date, start_time, end_time, status)
    VALUES (?, ?, ?, ?, ?)
""", (2, "2026-09-22", "11:00", "14:00", "APPOINTMENTS_CLOSED"))

cursor.execute("""
    INSERT INTO doc_schedule (doc_id, schedule_date, start_time, end_time, status)
    VALUES (?, ?, ?, ?, ?)
""", (3, "2026-09-22", "17:00", "21:00", "NOT_AVAILABLE"))


cursor.execute("""
    INSERT INTO doc_schedule (doc_id, schedule_date, start_time, end_time, status)
    VALUES (?, ?, ?, ?, ?)
""", (4, "2026-09-22", None, None, "NOT_SCHEDULED"))


cursor.execute("SELECT * FROM doc_schedule")
rows = cursor.fetchall()
for row in rows:    
    print(row)


connection.commit()
connection.close()
