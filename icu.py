import sqlite3
import customtkinter as ctk


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
        
        update= {
            "success": False,
            "message": "⚠️ ICU category not found"
        }
        return update

    total = row[0]    

    try:
       occupied = int(occupied)         
                   
       if (occupied < 0):
            
            update= {
                "success": False,
                "message": "⚠️ Occupied beds cannot be negative"
            }
            return update
               
       elif(occupied > total):
            
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




def create_icu_card(parent, title, column):
    heading_font = ctk.CTkFont(size=21, weight="bold")
    update_font = ctk.CTkFont(size=18)
    available_font = ctk.CTkFont(size=54, weight="bold")

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
    heading_font = ctk.CTkFont(size=21, weight="bold")
    update_font = ctk.CTkFont(size=18)
    
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





def refresh_level(level_cards, level):
    if(level_cards is not None):
        refresh_card(level_cards["ventilator"], level, "ventilator")
        refresh_card(level_cards["non_ventilator"], level, "non_ventilator")



def refresh_dashboard(level1, level2, level3):
    refresh_level(level1, 1)
    refresh_level(level2, 2)
    refresh_level(level3, 3)



