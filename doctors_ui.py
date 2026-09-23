import sqlite3
import customtkinter as ctk
from datetime import datetime

import sqlite3
connection = sqlite3.connect("doctors.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

ctk.set_appearance_mode("dark")

doctors_ui = ctk.CTk()


doctors_ui.title("Doctor's UI")
doctors_ui.geometry("1400x800")


lower_font = ctk.CTkFont(size=15)
name_font = ctk.CTkFont(size=18, weight="bold")
available_font = ctk.CTkFont(size=54, weight="bold")


doctors_ui.grid_rowconfigure(0, weight=1)
doctors_ui.grid_rowconfigure(1, weight=1)
doctors_ui.grid_rowconfigure(2, weight=1)
doctors_ui.grid_rowconfigure(3, weight=1)
doctors_ui.grid_rowconfigure(4, weight=1)
doctors_ui.grid_rowconfigure(5, weight=1)
doctors_ui.grid_rowconfigure(6, weight=1)


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




def create_doctor_card(parent, doctor):

    if(doctor["credential_suffix"] is not None):
        name = "● "+ doctor["title"] + " " + doctor["name"] + " " + f"({doctor["credential_suffix"]})"
    else:
        name = "● "+ doctor["title"] + " " + doctor["name"] 

    if (doctor["status"] is None):
        status="NOT SCHEDULED"
        time=""
                
    elif(doctor["status"] == "NOT_SCHEDULED"):
        status="NOT SCHEDULED TODAY"
        time=""
            
    elif(doctor["status"]== "NOT_AVAILABLE"):
        time= doctor["start_time"]+ "-" + doctor["end_time"]
        status = "NOT AVAILABLE"

    elif(doctor["status"]== "APPOINTMENTS_CLOSED"):
        time= doctor["start_time"] + "-" + doctor["end_time"]
        status = "APPOINTMENTS CLOSED"

    else:
        time= doctor["start_time"] + "-" + doctor["end_time"]
        status = "AVAILABLE"

    
    card = ctk.CTkFrame(parent, corner_radius=15)

    name_label = ctk.CTkLabel(
        card,
        text=name,
        font=name_font
    )

    qualification_label = ctk.CTkLabel(
        card,
        text=doctor["qualification"],
        font=lower_font
    )

    specialty_label = ctk.CTkLabel(
        card,
        text=doctor["specialty"],
        font=name_font
    )

    time_label = ctk.CTkLabel(
        card,
        text= time,
        font=name_font
    )

    status_label = ctk.CTkLabel(
        card,
        text=status,
        font=lower_font
    )

    card.pack(padx=5, pady=5) 
    name_label.grid(
        row=0,
        column=0,
        padx=5,
        pady=5,
        sticky="w"
    )
    qualification_label.grid(
        row=1,
        column=0,
        padx=5,
        pady=5,
        sticky="w"
    )    
    specialty_label.grid(
        row=2,
        column=0,
        padx=5,
        pady=5,
        sticky="w"
    )
    time_label.grid(
        row=3,
        column=0,
        padx=5,
        pady=5,
        sticky="w"
    )
    status_label.grid(
        row=3,
        column=1,
        padx=5,
        pady=5,
        sticky="e"
    )



doctors=get_todays_doctors("2026-09-22")

for doctor in doctors:
    if (doctor["name"]=="Plaban Mazumdar" or  doctor["name"]=="Ankit Rawniyar"):
        create_doctor_card(doctors_ui, doctor)
    

connection.close()

doctors_ui.mainloop()