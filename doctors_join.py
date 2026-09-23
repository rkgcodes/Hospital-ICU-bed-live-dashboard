import sqlite3
connection = sqlite3.connect("doctors.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()



cursor.execute("""
    SELECT 
        doc_info.title, 
        doc_info.name, 
        doc_info.qualification,
        doc_info.credential_suffix, 
        doc_info.department, 
        doc_info.specialty, 
        doc_schedule.schedule_date, 
        doc_schedule.start_time, 
        doc_schedule.end_time, 
        doc_schedule.status 
    FROM doc_info
    JOIN doc_schedule
    ON doc_info.id = doc_schedule.doctor_id      
    WHERE doc_schedule.schedule_date = ?
    """, ("2026-09-22",))

rows = cursor.fetchall()
for row in rows:
    if(row["credential_suffix"] is not None):
        print(row["title"], row["name"], "(",row["credential_suffix"],")")
    else:
        print(row["title"], row["name"])
    print(row["qualification"])
    print(row["department"])
    if (row["status"] == "NOT_SCHEDULED"):
        print(row["status"])
    else:
        print(row["start_time"], "-" ,row["end_time"])
        print(row["status"])    
    print()
    print(dict(row))
    print()




connection.close()