import sqlite3

connection = sqlite3.connect("hospital.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS icu_beds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level INTEGER,
        bed_type TEXT,
        total INTEGER,
        occupied INTEGER
    )
""")

cursor.execute("""
    INSERT INTO icu_beds (level, bed_type, total, occupied)
    VALUES (?, ?, ?, ?)
""", (1, "ventilator", 3, 0))

cursor.execute("""
    INSERT INTO icu_beds (level, bed_type, total, occupied)
    VALUES (?, ?, ?, ?)
""",(1, "non_ventilator", 4, 1))

cursor.execute("""
    INSERT INTO icu_beds (level, bed_type, total, occupied)
    VALUES (?, ?, ?, ?)
""",(2, "ventilator", 0, 0))

cursor.execute("""
    INSERT INTO icu_beds (level, bed_type, total, occupied)
    VALUES (?, ?, ?, ?)
""",(2, "non_ventilator", 0, 0))


connection.commit()
connection.close()