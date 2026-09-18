import sqlite3
connection = sqlite3.connect("hospital.db")
connection.row_factory=sqlite3.Row
cursor = connection.cursor()

def get_icu_status(level, bed_type):
    
    cursor.execute(
    "SELECT total, occupied FROM icu_beds WHERE level = ? AND bed_type = ?",
    (level, bed_type)
)   
    row = cursor.fetchone()

    if row is None:
        print("⚠️ Wrong level and bed type")
        return


    available = row["total"]-row["occupied"]
    return {
    "total": row["total"],
    "occupied": row["occupied"],
    "available": available
}




#status= get_icu_status(1, "ventilator")
#print (status)


print(get_icu_status(1, "ventilator"))
print(get_icu_status(1, "non_ventilator"))
print(get_icu_status(2, "ventilator"))

