import sqlite3
import customtkinter as ctk
from datetime import datetime

ctk.set_appearance_mode("dark")

finale6 = ctk.CTk()


finale6.title("Finale 6")
finale6.geometry("1400x800")


heading_font = ctk.CTkFont(size=21, weight="bold")
update_font = ctk.CTkFont(size=18)
available_font = ctk.CTkFont(size=54, weight="bold")


finale6.grid_rowconfigure(0, weight=1)
finale6.grid_rowconfigure(1, weight=1)
finale6.grid_rowconfigure(2, weight=1)
finale6.grid_rowconfigure(3, weight=1)

header = ctk.CTkFrame(finale6, corner_radius=15)
header.pack(pady=10)
now = datetime.now()
string_date = now.strftime("%d-%m-%Y %H:%M:%S")
now = "Updated : "+string_date



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

       
       update= {
            "success": True,
            "message": "✓ ICU status updated "
        }
       return update       
    except ValueError:        
        
        update= {
            "success": False,
            "message": "⚠️ Enter occupied beds number only"
        }
        return update            




title = ctk.CTkLabel(
    header,
    text="AROGYA HOSPITAL & RESEARCH CENTRE",
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
    text="ICU BED AVAILABILITY",
    font=heading_font,
    
)
title2.grid(
    row=1,
    column=0,    
    padx=10,
    pady=10,
    sticky="w" 
        
)
title3 = ctk.CTkLabel(
    header,
    font=update_font,
    text=now
)
title3.grid(
    row=1,
    column=1,    
    padx=10,
    pady=10,
    sticky="e"    
)



# UI code begins here


def create_icu_card(parent, title, column):

    card = ctk.CTkFrame(parent)

    title_label = ctk.CTkLabel(
        card,
        text=title,
        font=update_font
    )

    available_heading = ctk.CTkLabel(
        card,
        text="AVAILABLE",
        font=heading_font
    )

    available_label = ctk.CTkLabel(
        card,
        text="0",
        font=available_font
    )

    total_label = ctk.CTkLabel(
        card,
        text="Total : 0",
        font=update_font
    )

    occupied_label = ctk.CTkLabel(
        card,
        text="Occupied : 0",
        font=update_font
    )

    
    title_label.pack(padx=10, pady=10)
    available_heading.pack(padx=10, pady=10)    
    card.grid(
    row=0,
    column=column,
    padx=20,
    pady=20,
    sticky="nsew"
)
    available_label.pack(pady=10)
    total_label.pack(pady=10)
    occupied_label.pack(pady=10)
    return {
    "available": available_label,
    "total": total_label,
    "occupied": occupied_label
}


def create_level(parent, level):

    level_frame = ctk.CTkFrame(parent)   

    level_label = ctk.CTkLabel(
        level_frame,
        text=f"LEVEL {level}",
        font=heading_font
    )
    
    cards_frame = ctk.CTkFrame(level_frame) 
    level_frame.pack(fill="x", pady=10)
    level_label.pack(pady=10)

    x = get_icu_status(level, "ventilator")
    y = get_icu_status(level, "non_ventilator")

    if(x["total"]==0 and y["total"]==0):        
        
        message_label = ctk.CTkLabel(
            level_frame,
            text="ICU FACILITY NOT AVAILABLE",
            font=update_font
        )
        message_label.pack(pady=10)
        output = None

    else:
    
        vent_card = create_icu_card(cards_frame, "WITH VENTILATOR", 0)
        nonvent_card = create_icu_card(cards_frame, "WITHOUT VENTILATOR", 1)

        cards_frame.grid_columnconfigure(0, weight=1)
        cards_frame.grid_columnconfigure(1, weight=1)
        cards_frame.pack()
        output = {         
            "ventilator": vent_card,
            "non_ventilator": nonvent_card
        }   
    
   
   
    return output


def refresh_card(card, level, bed_type):

    status = get_icu_status(level, bed_type)
    card["available"].configure(text=status["available"])
    card["total"].configure(text=f"Total : {status['total']}")
    card["occupied"].configure(text=f"Occupied : {status['occupied']}")    


    
level1 = create_level(finale6, 1)  
level2 = create_level(finale6, 2)
level3 = create_level(finale6, 3)


def refresh_level(level_cards, level):
    if(level_cards is not None):
        refresh_card(level_cards["ventilator"], level, "ventilator")
        refresh_card(level_cards["non_ventilator"], level, "non_ventilator")


refresh_level(level1,1)
refresh_level(level2,2)
refresh_level(level2,3)







def open_admin():
    admin_window = ctk.CTkToplevel(finale6)

    admin_window.title("ICU Admin")
    admin_window.geometry("700x300")

    ctk.CTkLabel(
        admin_window,
        text="ADMIN PANEL"
    ).pack(pady=30)

    admin_frame= ctk.CTkFrame(admin_window, corner_radius=15)
    admin_frame.pack()

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
        




admin_button = ctk.CTkButton(
    finale6,
    text="ADMIN",
    command=open_admin
)
admin_button.pack()







# change is required
def refresh_dashboard():
    refresh_level(level1, 1)
    refresh_level(level2, 2)
    refresh_level(level3, 3)
    

    title2.configure(text="Last updated on: "+ datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    





finale6.mainloop()