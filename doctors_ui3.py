import sqlite3
import customtkinter as ctk
from datetime import datetime

import sqlite3
connection = sqlite3.connect("doctors.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

ctk.set_appearance_mode("dark")

doctors_ui3 = ctk.CTk()


doctors_ui3.title("Doctor's UI")
doctors_ui3.geometry("1400x800")

today = datetime.now().strftime("%Y-%m-%d")
lower_font = ctk.CTkFont(size=15)
boldlower_font = ctk.CTkFont(size=15, weight="bold")
name_font = ctk.CTkFont(size=18, weight="bold")
available_font = ctk.CTkFont(size=54, weight="bold")


doctors_ui3.grid_columnconfigure(0, weight=1)
doctors_ui3.grid_columnconfigure(1, weight=1)
doctors_ui3.grid_columnconfigure(2, weight=1)

doctors_ui3.grid_rowconfigure(0, weight=1)
doctors_ui3.grid_rowconfigure(1, weight=1)
doctors_ui3.grid_rowconfigure(2, weight=1)

doctors_frame= ctk.CTkFrame(doctors_ui3, corner_radius=15)
doctors_frame.pack()

def get_todays_doctors(date):
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

        LEFT JOIN doc_schedule
        ON doc_info.id = doc_schedule.doctor_id
        AND doc_schedule.schedule_date = ?

        ORDER BY
            CASE
                WHEN doc_schedule.status = 'AVAILABLE' THEN 1
                WHEN doc_schedule.status = 'APPOINTMENTS_CLOSED' THEN 2
                WHEN doc_schedule.status = 'NOT_AVAILABLE' THEN 3
                ELSE 4
            END,
            doc_info.seniority_rank ASC

    """, (date,))

    rows = cursor.fetchall()
    connection.close()
    return rows


def format_doctor_status(doctor):
    if doctor["start_time"] and doctor["end_time"]:
        time = f'{doctor["start_time"]} - {doctor["end_time"]}'
    else:
        time = ""


    if (doctor["status"] is None) or (doctor["status"] == "NOT_SCHEDULED"):
        stat =  {
            "text": "NOT SCHEDULED TODAY",
            "color": "#9CA3AF",
            "time": ""
        }
                               
                         
    elif(doctor["status"]== "NOT_AVAILABLE"):        
        stat =  {
                "text": "NOT AVAILABLE",
                "color": "#DD2D21" ,
                "time": ""
            }
    
    elif(doctor["status"]== "APPOINTMENTS_CLOSED"):        
        stat =  {
                    "text": "APPOINTMENTS CLOSED",
                    "color": "#C67D16", 
                    "time": time
                }
    else:        
        stat =  {
            "text": "AVAILABLE",
            "color": "#16A34A",
            "time": time
        }

    return stat

 



def create_doctor_card(parent, doctor, row, column):

    if(doctor["credential_suffix"] is not None):
        name = "● "+ doctor["title"] + " " + doctor["name"] + " " + f"({doctor["credential_suffix"]})"
    else:
        name = "● "+ doctor["title"] + " " + doctor["name"] 

    status= format_doctor_status(doctor)
    
    
    card = ctk.CTkFrame(
        parent,
        width=450,
        height=160,
        corner_radius=15
    )
    card.pack_propagate(False) 



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
        font=boldlower_font
    )

    time_label = ctk.CTkLabel(
        card,
        text= status["time"],
        font=name_font
    )

    status_label = ctk.CTkLabel(
        card,
        text=status["text"],
        font=boldlower_font,
        fg_color= status["color"],
        corner_radius=15
    )

    card.grid_columnconfigure(0, weight=1)
    card.grid_columnconfigure(1, weight=0)

    card.grid(
        row=row,
        column=column,
        padx=20,
        pady=20,
        sticky="nsew"
    )

    name_label.grid(
        row=0,
        column=0,
        columnspan=2,
        padx=10,
        pady=10,
        sticky="w"
    )
    qualification_label.grid(
        row=1,
        column=0,
        columnspan=2,
        padx=10,
        
        sticky="w"
    )    
    specialty_label.grid(
        row=2,
        column=0,
        columnspan=2,
        padx=10,
        
        sticky="w"
    )
    time_label.grid(
        row=3,
        column=0,
        padx=10,
        pady=20,
        sticky="w"
    )
    status_label.grid(
        row=3,
        column=1,
        padx=10,
        pady=20,
        sticky="e"
    )

    
        
doctors=get_todays_doctors(today)

for index, doctor in enumerate(doctors):
    row = index // 2
    column = index % 2
    
    create_doctor_card(doctors_frame, doctor, row, column)

    
def refresh_doctors(doctors_frame):

    for widget in doctors_frame.winfo_children():
        widget.destroy()

    doctors = get_todays_doctors(today)

    for index, doctor in enumerate(doctors):
        row = index // 2
        column = index % 2

        create_doctor_card(doctors_frame, doctor, row, column)
        

def update_doctor_schedule(doctor_id, date, status, start_time, end_time):
    connection = sqlite3.connect("doctors.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT doc_schedule.id    
        FROM doc_schedule 
        WHERE doc_schedule.doctor_id = ?
        AND doc_schedule.schedule_date = ?   
    
        """, (doctor_id, date))
    
    existing = cursor.fetchone()
    if status in ["NOT_AVAILABLE", "NOT_SCHEDULED"]:
        start_time = None
        end_time = None

    if existing is not None:
        cursor.execute("""
            UPDATE doc_schedule
            SET status = ?, 
                start_time = ?, 
                end_time = ?
            WHERE doctor_id = ?
            AND schedule_date = ?
        """, (status, start_time, end_time, doctor_id, date))
        
    else:
    # INSERT
        cursor.execute("""
            INSERT INTO doc_schedule
            (doctor_id, schedule_date, start_time, end_time, status)
            VALUES (?, ?, ?, ?, ?)
        """, (doctor_id, date, start_time, end_time, status))

    connection.commit()
    connection.close()   
     





def open_admin(doctors_frame):
    admin_window = ctk.CTkToplevel(doctors_ui3)

    admin_window.title("Doctor Admin")
    admin_window.geometry("700x600")

    ctk.CTkLabel(
        admin_window,
        text="DOCTOR ADMIN PANEL",
        font=name_font
    ).pack(pady=30)

    admin_frame= ctk.CTkFrame(admin_window, corner_radius=15)
    admin_frame.pack()

       

    status_options = [
        "AVAILABLE",
        "APPOINTMENTS_CLOSED",
        "NOT_AVAILABLE",
        "NOT_SCHEDULED"
    ]

    time=["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00"]
    connection = sqlite3.connect("doctors.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            doc_info.id,
            doc_info.title,
            doc_info.name,                
            doc_info.credential_suffix          
                    
        FROM doc_info
               
        ORDER BY
            doc_info.seniority_rank ASC
            
        """,)
            
    rows = cursor.fetchall()
    doctors={}
    for row in rows:
        if(row["credential_suffix"] is not None):
            name = row["title"] + " " + row["name"] + " " + f"({row["credential_suffix"]})"
        else:
            name = row["title"] + " " + row["name"]            
        doctors[name]= row["id"]


   
        
    def doctor_selected(choice):
        selected_name = doctor_combo.get()
        doctor_id = doctors[selected_name]
        cursor.execute("""
            SELECT doc_schedule.start_time, doc_schedule.end_time, doc_schedule.status                      
                            
            FROM doc_schedule
                       
            WHERE doc_schedule.doctor_id = ? AND doc_schedule.schedule_date = ?
                    
            """,(doctor_id, today))
        selected_info = cursor.fetchone()        
        
        if(selected_info["start_time"] and selected_info["end_time"] ) is None:
            status_combo.set(selected_info["status"])
            start_combo.set("")
            end_combo.set("")

        else:
            status_combo.set(selected_info["status"])
            start_combo.set(selected_info["start_time"])
            end_combo.set(selected_info["end_time"])



    doctor_label = ctk.CTkLabel(
        admin_frame,
        text="DOCTOR",
        font=boldlower_font
        
    )
    doctor_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew") 


    doctor_combo = ctk.CTkComboBox(
        admin_frame,
        values=list(doctors.keys()),
        command=doctor_selected
    )
    doctor_combo.grid(row=0, column=1, padx=20, pady=20, sticky="nsew" )

    status_label = ctk.CTkLabel(
        admin_frame,
        text="STATUS",
        font=boldlower_font
    )
    status_label.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")                   
    


    status_combo = ctk.CTkComboBox(
        admin_frame,
        values=status_options
    )
    status_combo.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
          


   
    start_label = ctk.CTkLabel(
        admin_frame,
        text="START TIME",
        font=boldlower_font
    )
    start_label.grid(row=2, column=0, padx=20, pady=20, sticky="nsew") 
    
    
    start_combo = ctk.CTkComboBox(
        admin_frame,
        values=time
    )
    start_combo.grid(row=2, column=1, padx=20, pady=20, sticky="nsew" )


    end_label = ctk.CTkLabel(
            admin_frame,
            text="END TIME",
            font=name_font
        )
    end_label.grid(row=3, column=0, padx=20, pady=20, sticky="nsew") 
        
        
    end_combo = ctk.CTkComboBox(
            admin_frame,
            values=time
        )
    end_combo.grid(row=3, column=1, padx=20, pady=20, sticky="nsew" )

    
    
    def test_selection():
        selected_name = doctor_combo.get()

        doctor_id = doctors[selected_name]

        status = status_combo.get()
        start_time = start_combo.get()
        end_time = end_combo.get()

        print("Doctor :", selected_name)
        print("ID :", doctor_id)
        print("Status :", status)
        print("Start :", start_time)
        print("End :", end_time)
        update_doctor_schedule(doctor_id, today, status, start_time, end_time)
        refresh_doctors(doctors_frame)
      


    update_button = ctk.CTkButton(
            admin_frame,
            text="UPDATE",
            command=test_selection
        )
    update_button.grid(row=4, column=1, padx=20, pady=20, sticky="nsew" )
    


admin_button = ctk.CTkButton(
        doctors_ui3,
        text="ADMIN",
        command=lambda: open_admin(doctors_frame)
    )
admin_button.pack(pady=20)

       
      
    

    
        
connection.close()

doctors_ui3.mainloop()