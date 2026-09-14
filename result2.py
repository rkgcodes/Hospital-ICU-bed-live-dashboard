import sqlite3

connection = sqlite3.connect("hospital.db")

cursor = connection.cursor()



def update_occupied(level, bed_type, occupied):
   
    cursor.execute("""
         UPDATE icu_beds
         SET  occupied = ? WHERE level = ? AND bed_type = ?
    """, (occupied, level, bed_type))
    connection.commit()


update_occupied(1, "ventilator", 2)

cursor.execute("""
    SELECT * FROM icu_beds
    WHERE level = ? AND bed_type = ?
""", (1, "ventilator"))

rows = cursor.fetchall()

for row in rows:
    print(row)


connection.close()


    
