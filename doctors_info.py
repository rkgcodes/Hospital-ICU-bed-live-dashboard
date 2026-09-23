import sqlite3
connection = sqlite3.connect("doctors.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS doc_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT DEFAULT 'Dr.',
        name TEXT,
        qualification TEXT,
        credential_suffix TEXT DEFAULT NULL,
        department TEXT,
        specialty TEXT,
        seniority_rank INTEGER
       )
""")

cursor.execute("""
    INSERT INTO doc_info (name, qualification, department, specialty, seniority_rank)
    VALUES (?, ?, ?, ?, ?)
""", ("Plaban Mazumdar", "MBBS, MD", "Medicine", "Internal Medicine", 1))

cursor.execute("""
    INSERT INTO doc_info (name, qualification, department, specialty, seniority_rank)
    VALUES (?, ?, ?, ?, ?)
""", ("M. N. Saikia", "MBBS, MS", "Surgery", "Laproscopic Surgery", 2))

cursor.execute("""
    INSERT INTO doc_info (name, qualification, department, specialty, seniority_rank)
    VALUES (?, ?, ?, ?, ?)
""", ("G. K. Das", "MBBS, DNB", "Gynecologist", "Obstetrics & Gynaecology", 3))

cursor.execute("""
    INSERT INTO doc_info (name, qualification, department, specialty, seniority_rank)
    VALUES (?, ?, ?, ?, ?)
""", ("D. Choudhury", "MBBS, DNB ENT", "ENT", "ENT Specialist", 4))

cursor.execute("""
    INSERT INTO doc_info (name, qualification, department, specialty, seniority_rank)
    VALUES (?, ?, ?, ?, ?)
""", ("A. Das", "MBBS, MD Paediatrics", "Paeditrian", "Child Specialist", 5))

cursor.execute("""
    INSERT INTO doc_info (name, qualification, credential_suffix, department, specialty, seniority_rank)
    VALUES (?, ?, ?, ?, ?, ?)
""", ("Ankit Rawniyar", "BPT, MPT", "PT", "Physiotherapy", "Musculoskelatan Physiotherapy", 6))




cursor.execute("SELECT * FROM doc_info")
rows = cursor.fetchall()
for row in rows:    
    print(row)


connection.commit()
connection.close()

