import sqlite3
import customtkinter as ctk
from datetime import datetime

ctk.set_appearance_mode("dark")

reuse = ctk.CTk()


reuse.title("REUSE UI FEATURES")
reuse.geometry("1200x1200")

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
       return update       
    except ValueError:        
        #result_label.configure(text="⚠️ Enter occupied beds number only")
        update= {
            "success": False,
            "message": "⚠️ Enter occupied beds number only"
        }
        return update            





# UI code begins here



def create_icu_card(parent, title, column):

    card = ctk.CTkFrame(parent)

    title_label = ctk.CTkLabel(
        card,
        text=title
    )

    available_heading = ctk.CTkLabel(
        card,
        text="AVAILABLE"
    )

    available_label = ctk.CTkLabel(
        card,
        text="0"
    )

    total_label = ctk.CTkLabel(
        card,
        text="Total : 0"
    )

    occupied_label = ctk.CTkLabel(
        card,
        text="Occupied : 0"
    )

    
    title_label.pack(pady=10)
    available_heading.pack(pady=10)    
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
        text=f"LEVEL {level}"
    )
    
    cards_frame = ctk.CTkFrame(level_frame) 
    
    vent_card = create_icu_card(cards_frame, "WITH VENTILATOR", 0)
    nonvent_card = create_icu_card(cards_frame, "WITHOUT VENTILATOR", 1)

    level_frame.pack(fill="x", pady=10)
    level_label.pack(pady=10)
    
    cards_frame.grid_columnconfigure(0, weight=1)
    cards_frame.grid_columnconfigure(1, weight=1)
    cards_frame.pack()
   
   
    return {         
        "ventilator": vent_card,
        "non_ventilator": nonvent_card
}


def refresh_card(card, level, bed_type):

    status = get_icu_status(level, bed_type)
    card["available"].configure(text=status["available"])
    card["total"].configure(text=f"Total : {status['total']}")
    card["occupied"].configure(text=f"Occupied : {status['occupied']}")    


    
level1 = create_level(reuse, 1)  
level2 = create_level(reuse, 2)
level3 = create_level(reuse, 3)

def refresh_level(level_cards, level):
    refresh_card(level_cards["ventilator"], level, "ventilator")
    refresh_card(level_cards["non_ventilator"], level, "non_ventilator")


refresh_level(level1,1)
refresh_level(level2,2)
refresh_level(level3,3)



reuse.mainloop()