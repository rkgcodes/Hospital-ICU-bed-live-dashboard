import sqlite3
import customtkinter as ctk

from theme import (
    BG_MAIN,
    BG_CARD,
    ACCENT,
    ACCENT_HOVER,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    TEXT_SPECIALTY,
    ICU_TYPE,     # cyan — WITH/WITHOUT VENTILATOR

    AVAILABLE_TEXT, # green
    TOTAL_TEXT,    # yellow
    OCCUPIED_TEXT,  # soft red/coral

    ICU_CARD,
    ICU_BORDER,
    
   
)


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




def create_icu_card(parent, title, column, fonts):
    
    card = ctk.CTkFrame(parent, corner_radius=15, fg_color=ICU_CARD, border_color=ICU_BORDER, border_width=1)

    title_label = ctk.CTkLabel(
        card,
        text=title,
        font=fonts["icuinfo"],
        text_color=TEXT_PRIMARY
    )

    available_heading = ctk.CTkLabel(
        card,
        text="AVAILABLE",
        font=fonts["specialty"],
        text_color=AVAILABLE_TEXT
    )

    available_label = ctk.CTkLabel(
        card,
        text="0",
        font=fonts["available"],
        text_color=AVAILABLE_TEXT
    )

    total_label = ctk.CTkLabel(
        card,
        text="Total : 0",
        font=fonts["icuinfo"],
        text_color=TOTAL_TEXT
    )

    occupied_label = ctk.CTkLabel(
        card,
        text="Occupied : 0",
        font=fonts["icuinfo"],
        text_color=OCCUPIED_TEXT
    )

    
    title_label.pack(padx=10,pady=(15, 8))
    available_heading.pack(padx=10, pady=(8, 0))    
    card.grid(
    row=0,
    column=column,
    padx=20,
    pady=20,
    sticky="nsew"
)
    available_label.pack(padx=10, pady=(0, 12))
    total_label.pack(padx=10, pady=(8, 6))
    occupied_label.pack(padx=10, pady=(6, 15))
    return {
    "available": available_label,
    "total": total_label,
    "occupied": occupied_label
}


def create_level(parent, level, fonts):
       
    
    level_frame = ctk.CTkFrame(parent, fg_color=BG_MAIN)   

    level_label = ctk.CTkLabel(
        level_frame,
        text=f"LEVEL {level}",
        font=fonts["specialty"],
        text_color=TEXT_SPECIALTY
    )
    
    cards_frame = ctk.CTkFrame(level_frame, fg_color=BG_MAIN) 
    level_frame.pack(fill="x", pady=10)
    level_label.pack(pady=10)

    x = get_icu_status(level, "ventilator")
    y = get_icu_status(level, "non_ventilator")

    if(x["total"]==0 and y["total"]==0):        
        
        message_label = ctk.CTkLabel(
            level_frame,
            text="ICU FACILITY NOT AVAILABLE",
            font=fonts["icuinfo"]
        )
        message_label.pack(pady=10)
        output = None

    else:
    
        vent_card = create_icu_card(cards_frame, "WITH VENTILATOR", 0, fonts)
        nonvent_card = create_icu_card(cards_frame, "WITHOUT VENTILATOR", 1, fonts)

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


def open_admin(parent, refresh):
    heading_font1 = ctk.CTkFont(size=15)
    
    admin_window = ctk.CTkToplevel(parent)

    admin_window.title("ICU Admin")
    admin_window.geometry("900x450")

    ctk.CTkLabel(
        admin_window,
        text="ADMIN PANEL"
    ).pack(pady=30)

    admin_frame= ctk.CTkFrame(admin_window, corner_radius=15)
    admin_frame.pack()

    admin_card = ctk.CTkFrame(admin_frame, fg_color=BG_MAIN, corner_radius=15)
    admin_card.pack()


    belowlabel = ctk.CTkLabel(
            admin_card,
            text="ADMIN UPDATE ",
            font=heading_font1
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
            font=heading_font1
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
        font=heading_font1
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
            refresh()
            #refresh_dashboard()


    def update_non_ventilator():
        occupied1 = numstr1.get()

        result1 = update_occupied(1, "non_ventilator", occupied1)

        result_label1.configure(text=result1["message"])

        if result1["success"]:
            refresh()
            #refresh_dashboard()


    button = ctk.CTkButton(
        admin_card,
        text="UPDATE",
        font=heading_font1,
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
        font=heading_font1,
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



def create_icu_screen(parent, fonts):

    content = ctk.CTkFrame(parent, fg_color=BG_MAIN)
    content.pack(fill="both", expand=True, padx=10, pady=10)

    title_label = ctk.CTkLabel(
        content,
        text="AROGYA HOSPITAL & RESEARCH CENTRE",
        font=fonts["doctor"]
                            
    )
      
    inside_label= ctk.CTkLabel(
        content,
        text="ICU BED DASHBOARD",
        font=fonts["specialty"]
                
    )
        
        
    title_label.pack(padx=10, pady=10) 
    
    inside_label.pack(padx=10)

    level1 = create_level(content, 1, fonts)
    level2 = create_level(content, 2, fonts)
    level3 = create_level(content, 3, fonts)

    def refresh():
        refresh_dashboard(level1, level2, level3)

    refresh()
    admin_button = ctk.CTkButton(
    parent,
    text="ADMIN",
    command=lambda: open_admin(parent, refresh)
)
    admin_button.pack()
    return refresh