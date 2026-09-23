import sqlite3
connection = sqlite3.connect("doctors.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

def get_todays_doctors(date):
    #IMPORTANT DISTINCTION USE OF AND RATHER WHERE
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
        LEFT JOIN doc_schedule
        ON doc_info.id = doc_schedule.doctor_id      
        AND doc_schedule.schedule_date = ?               
        """, (date,))
    rows = cursor.fetchall()
    return rows

def print_docinfo(date):
    doctors = get_todays_doctors(date)
    for doctor in doctors: 

        if(doctor["credential_suffix"] is not None):
            print(doctor["title"], doctor["name"], f"({doctor["credential_suffix"]})")
        else:
            print(doctor["title"], doctor["name"])
        print(doctor["qualification"])
        print(doctor["department"])
        if (doctor["status"] is None):
            print("NOT_SCHEDULED")
            
        elif(doctor["status"] == "NOT_SCHEDULED"):
            print(doctor["status"])
        
        else:
            print(doctor["start_time"], "-" ,doctor["end_time"])
            print(doctor["status"])

        print()
        print(dict(doctor))
        print()

print_docinfo("2026-09-22")
connection.close()
