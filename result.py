import sqlite3

connection = sqlite3.connect("hospital.db")

cursor = connection.cursor()


#pythonlogic to check & print one condition
cursor.execute("SELECT * FROM icu_beds")
rows = cursor.fetchall()
for row in rows:
    for bedtype in row:
        if(bedtype =='ventilator'):
            print(row)
print()

#sqlite logic to fetch all rows that satisfies the condition
cursor.execute("""
    SELECT * FROM icu_beds
    WHERE level = ? AND bed_type = ?
""", (1, "ventilator"))

rows = cursor.fetchall()

for row in rows:
    print(row)

print()


#single condition
cursor.execute(
    "SELECT * FROM icu_beds WHERE level = ?",
    (1,)
)
rows = cursor.fetchall()

for row in rows:
    print(row)

print()

# Only selected columns
cursor.execute(
    "SELECT total, occupied FROM icu_beds WHERE level = ? AND bed_type = ?",
    (1, "ventilator")
)

row = cursor.fetchone()

total = row[0]
occupied = row[1]

available = total - occupied

print(available)
print()



# python logic to check two condtion, however vague
cursor.execute("SELECT * FROM icu_beds")
rows = cursor.fetchall()
for row in rows:
    if 1 in row and "ventilator" in row:
        print(row)
print()




# rowfactory concept
connection = sqlite3.connect("hospital.db")
connection.row_factory = sqlite3.Row

cursor = connection.cursor()
cursor.execute("SELECT * FROM icu_beds")
rows = cursor.fetchall()
for row in rows:
    if row["level"] == 1 and row["bed_type"] == "ventilator":
        print(tuple(row))
print()


print(type(row))
print(row.keys())
print(tuple(row))

print(dict(row))


connection.close()
