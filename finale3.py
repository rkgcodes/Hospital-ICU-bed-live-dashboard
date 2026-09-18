import sqlite3
import customtkinter as ctk
from datetime import datetime

ctk.set_appearance_mode("dark")

finale3 = ctk.CTk()


finale3.title("Finale 3")
finale3.geometry("1400x800")


heading_font = ctk.CTkFont(size=18, weight="bold")
update_font = ctk.CTkFont(size=14)
number_font = ctk.CTkFont(size=48, weight="bold")

finale3.grid_columnconfigure(0, weight=1)
finale3.grid_columnconfigure(1, weight=1)
finale3.grid_rowconfigure(0, weight=1)
finale3.grid_rowconfigure(1, weight=1)
finale3.grid_rowconfigure(2, weight=1)
finale3.grid_rowconfigure(3, weight=1)
header = ctk.CTkFrame(finale3, corner_radius=15)
header.grid(
    row=0,
    column=0,    
    columnspan=2,
    padx=15,
    pady=15,
    sticky="nsew"
)
now = datetime.now()
string_date = now.strftime("%d-%m-%Y %H:%M:%S")
now = "Last updated on: "+string_date



# get_status function
def get_icu_status(level, bed_type):
    with sqlite3.connect("hospital.db") as connection:
        connection.row_factory=sqlite3.Row
        cursor = connection.cursor()
    
        cursor.execute(
        "SELECT total, occupied FROM icu_beds WHERE level = ? AND bed_type = ?",
        (level, bed_type)
    )   
        row = cursor.fetchone()

    if row is None:
        print("⚠️ Wrong level and bed type")
        return


    available = row["total"]-row["occupied"]
    status= {
        "total": row["total"],
        "occupied": row["occupied"],
        "available": available
    }    
    return status


# update_occupuied status
def update_occupied(level, bed_type, occupied):
    with sqlite3.connect("hospital.db") as connection:
        connection.row_factory=sqlite3.Row
        cursor = connection.cursor()

        cursor.execute("""
             SELECT total FROM icu_beds
             WHERE level = ? AND bed_type = ?
        """, (level, bed_type))
        
        row = cursor.fetchone()

    if row is None:
        #result_label.configure(text="⚠️ ICU category not found")
        update= {
            "success": False,
            "message": "⚠️ ICU category not found"
        }
        return update

    total = row[0]    

    try:
       occupied = int(occupied)         
                   
       if (occupied < 0):
            #result_label.configure(text="⚠️ Occupied beds cannot be negative")
            update= {
                "success": False,
                "message": "⚠️ Occupied beds cannot be negative"
            }
            return update
               
       elif(occupied > total):
            #result_label.configure(text="⚠️ Occupied beds cannot exceed total beds")
            update= {
                "success": False,
                "message": "⚠️ Occupied beds cannot exceed total beds"
            }            
            return update
       
       cursor.execute("""
                       UPDATE icu_beds
                       SET  occupied = ? WHERE level = ? AND bed_type = ?
               """, (occupied, level, bed_type))
       connection.commit()

       #result_label.configure(text="✓ ICU status updated ")
       update= {
            "success": True,
            "message": "✓ ICU status updated "
        }       
    except ValueError:        
        #result_label.configure(text="⚠️ Enter occupied beds number only")
        update= {
            "success": False,
            "message": "⚠️ Enter occupied beds number only"
        }
        return update            



# UI code begins here

title = ctk.CTkLabel(
    header,
    text="ICU BED LIVE DASHBOARD",
    font=heading_font
)
title.grid(
    row=0,
    column=0,    
    padx=10,
    pady=10,
    sticky="nsew"    
)
title1 = ctk.CTkLabel(
    header,
    text="● LIVE",
    font=heading_font
)
title1.grid(
    row=0,
    column=1,    
    padx=10,
    pady=10,
    sticky="e"    
)
title2 = ctk.CTkLabel(
    header,
    font=update_font,
    text=now
)
title2.grid(
    row=1,
    column=0,    
    padx=10,
    pady=10,
    sticky="nsew"    
)
title3 = ctk.CTkLabel(
    header,
    text="LEVEL 1",
    font=heading_font,
    
)
title3.grid(
    row=2,
    column=0,    
    padx=10,
    pady=10,
    sticky="nsew" 
        
)



first_frame = ctk.CTkFrame(finale3, corner_radius=15)
first_frame.grid(
    row=1,
    column=0,
    padx=15,
    pady=15,
    sticky="nsew"
)


venti_label = ctk.CTkLabel(
    first_frame,
    text="WITH VENTILATOR",
    anchor="w",    
    font=heading_font
)
venti_label.pack(pady=10)



venti_card = ctk.CTkFrame(first_frame, fg_color="#2563eb", corner_radius=15)
venti_card.pack(fill="x", padx=10, pady=10)

avail= get_icu_status(1, "ventilator")
venti_info_label = ctk.CTkLabel(
    venti_card,
    text="AVAILABLE",
    anchor="w",    
    font=heading_font
)
venti_info_label.pack(pady=10)

venti_info1_label = ctk.CTkLabel(
    venti_card,
    text= avail["available"],
    anchor="w",    
    font=number_font
)
venti_info1_label.pack(pady=10)

connection = sqlite3.connect("hospital.db")
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("""
             SELECT * FROM icu_beds
             WHERE level = ? AND bed_type = ?
        """, (1, "ventilator")
)
        
row = cursor.fetchone()
t=row["total"]
o=row["occupied"]

venti_info2_label = ctk.CTkLabel(
    venti_card,
    text=f"Total : {t}",
    anchor="w",    
    font=heading_font
)
venti_info2_label.pack(pady=10)


venti_info3_label = ctk.CTkLabel(
    venti_card,
    text=f"Occupied : {o}",
    anchor="w",    
    font=heading_font
)
venti_info3_label.pack(pady=10)
connection.close()



# second frame code

second_frame = ctk.CTkFrame(finale3, corner_radius=15)
second_frame.grid(
    row=1,
    column=1,
    padx=15,
    pady=15,
    sticky="nsew"
)


non_venti_label = ctk.CTkLabel(
    second_frame,
    text="WITHOUT VENTILATOR",
    anchor="w",    
    font=heading_font
)
non_venti_label.pack(pady=10)


non_venti_card = ctk.CTkFrame(second_frame, fg_color="#7C3AED", corner_radius=15)
non_venti_card.pack(fill="x", padx=10, pady=10)

##
nonavail= get_icu_status(1, "non_ventilator")
nonventi_info_label = ctk.CTkLabel(
   non_venti_card,
    text="AVAILABLE",
    anchor="w",    
    font=heading_font
)
nonventi_info_label.pack(pady=10)

nonventi_info1_label = ctk.CTkLabel(
    non_venti_card,
    text= nonavail["available"],
    anchor="w",    
    font=number_font
)


nonventi_info1_label.pack(pady=10)

connection = sqlite3.connect("hospital.db")
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

cursor.execute("""
             SELECT * FROM icu_beds
             WHERE level = ? AND bed_type = ?
        """, (1, "non_ventilator")
)
        
row = cursor.fetchone()
t1=row["total"]
o1=row["occupied"]

nonventi_info2_label = ctk.CTkLabel(
    non_venti_card,
    text=f"Total : {t1}",
    anchor="w",    
    font=heading_font
)
nonventi_info2_label.pack(pady=10)


nonventi_info3_label = ctk.CTkLabel(
    non_venti_card,
    text=f"Occupied : {o1}",
    anchor="w",    
    font=heading_font
)
nonventi_info3_label.pack(pady=10)
connection.close()

admin_frame= ctk.CTkFrame(finale3, corner_radius=15)
admin_frame.grid(
    row=2,
    column=0,
    columnspan=2,
    padx=15,
    pady=15,
    sticky="nsew"
)


# change is required
def refresh_dashboard():
    vent = get_icu_status(1, "ventilator")
    nonvent = get_icu_status(1, "non_ventilator")

    title2.configure(text="Last updated on: "+ datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    venti_info1_label.configure(text=str(vent["available"]))
    venti_info2_label.configure(text=f"Total : {vent['total']}")
    venti_info3_label.configure(text=f"Occupied : {vent['occupied']}")

    nonventi_info1_label.configure.configure(text=str(nonvent["available"]))
    nonventi_info2_label.configure(text=f"Total : {nonvent['total']}")
    nonventi_info3_label.configure(text=f"Occupied : {nonvent['occupied']}")

def update_ventilator():
    occupied = numstr.get()

    result = update_occupied(1, "ventilator", occupied)

    result_label.configure(text=result["message"])

    if result["success"]:
        refresh_dashboard()


def update_non_ventilator():
    occupied1 = numstr1.get()

    result1 = update_occupied(1, "non_ventilator", occupied1)

    result_label1.configure(text=result1["message"])

    if result1["success"]:
        refresh_dashboard()             
        


admin_card = ctk.CTkFrame(admin_frame, fg_color="#2b2b2b", corner_radius=15)
admin_card.pack()

belowlabel = ctk.CTkLabel(
    admin_card,
    text="ADMIN UPDATE ",
    font=heading_font
    )
belowlabel.grid(
    row=0,
    column=0,
    columnspan=3,
    padx=20,
    pady=20,
    sticky="nsew"
    
)

adminlabel = ctk.CTkLabel(
    admin_card,
    text="ICU Beds with ventilator in use: ",
    anchor="w",
    font=heading_font
    )
adminlabel.grid(
    row=1,
    column=0,
    padx=20,
    pady=20,
    sticky="w"
    
)

numstr = ctk.CTkEntry(admin_card)      
numstr.grid(
    row=1,
    column=1,
    padx=20,
    pady=20,
    sticky="w"
    
)

button = ctk.CTkButton(
    admin_card,
    text="UPDATE",
    font=heading_font,
    command=update_ventilator
    
)
button.grid(
    row=1,
    column=2,
    padx=20,
    pady=20,
    sticky="w"
    
)

result_label = ctk.CTkLabel(admin_card, text="")
result_label.grid(
    row=1,
    column=3,
    padx=20,
    pady=20,
    sticky="w"
    
)

# update 

adminlabel1 = ctk.CTkLabel(
    admin_card,
    text="ICU Beds without ventilator in use: ",
    anchor="w",
    font=heading_font
    )
adminlabel1.grid(
    row=2,
    column=0,
    padx=20,
    pady=20,
    sticky="w"
    
)

numstr1 = ctk.CTkEntry(admin_card)      
numstr1.grid(
    row=2,
    column=1,
    padx=20,
    pady=20,
    sticky="w"
    
)

button1 = ctk.CTkButton(
    admin_card,
    text="UPDATE",
    font=heading_font,
    command=update_non_ventilator
    
)
button1.grid(
    row=2,
    column=2,
    padx=20,
    pady=20,
    sticky="w"
    
)

result_label1 = ctk.CTkLabel(admin_card, text="")
result_label1.grid(
    row=2,
    column=3,
    padx=20,
    pady=20,
    sticky="w"
    
)


finale3.mainloop()