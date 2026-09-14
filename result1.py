import sqlite3

connection = sqlite3.connect("hospital.db")

cursor = connection.cursor()

cursor.execute("""
    UPDATE icu_beds
    SET  occupied = ? WHERE level = ? AND bed_type = ?
""", (2, 1, "ventilator"))

connection.commit()

cursor.execute("SELECT * FROM icu_beds")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()




#UPDATE icu_beds
#SET occupied = 2
#WHERE level = 1 AND bed_type = 'ventilator'