import sqlite3

connection = sqlite3.connect("hospital.db")

cursor = connection.cursor()



# values before update
cursor.execute(" SELECT * FROM icu_beds")
rows = cursor.fetchall()

for row in rows:
    print(row)
print()


def update_occupied(level, bed_type, occupied):

    cursor.execute("""
             SELECT total FROM icu_beds
             WHERE level = ? AND bed_type = ?
        """, (level, bed_type))
        
    rows = cursor.fetchone()
    

    try:
        total = row[0]
        if (total<occupied):
            raise ValueError()

    except ValueError:
        print("Cannot be greater than total beds")


    else:
        if occupied < 0:
             print("Occupied beds cannot be negative")
             return
        
        if occupied > total:
             print("Occupied beds cannot exceed total beds")
             return
        
        cursor.execute("""
                UPDATE icu_beds
                SET  occupied = ? WHERE level = ? AND bed_type = ?
        """, (occupied, level, bed_type))
        connection.commit()
        

update_occupied(1, "ventilator", 4)

#values after update

cursor.execute(" SELECT * FROM icu_beds")
rows = cursor.fetchall()

for row in rows:
    print(row)



connection.close()
