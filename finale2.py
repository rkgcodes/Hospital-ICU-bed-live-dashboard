import sqlite3


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


print(get_icu_status(1, "ventilator"))
print(get_icu_status(1, "non_ventilator"))
print(get_icu_status(2, "ventilator"))


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


output = update_occupied(1, "ventilator", "abc")
print (output["success"], ",", output["message"])