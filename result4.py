import customtkinter as ctk
ctk.set_appearance_mode("dark")
result4 = ctk.CTk()
result4.title("Excercise")
result4.geometry("600x400")




import sqlite3
connection = sqlite3.connect("hospital.db")
cursor = connection.cursor()





def get_occupied_beds():
    occupied=num.get()
    update_occupied(1, "ventilator", occupied)


   #result_label.configure(text="Hello " + entered_name)



header = ctk.CTkFrame(result4)
header.pack()

title = ctk.CTkLabel(
    header,
    text="UI & DB Integartion"
)


title.pack(pady=20)


label = ctk.CTkLabel(result4, text="Enter occupied beds")
label.pack()

num = ctk.CTkEntry(result4)

num.pack(pady=10)


button = ctk.CTkButton(
    result4,
    text="CLICK ME",
    command=get_occupied_beds
    
)
button.pack(pady=10)

result_label = ctk.CTkLabel(result4, text="")
result_label.pack()



def update_occupied(level, bed_type, occupied):

    cursor.execute("""
             SELECT total FROM icu_beds
             WHERE level = ? AND bed_type = ?
        """, (level, bed_type))
        
    row = cursor.fetchone()
    total = row[0]
    

    try:
       occupied = int(occupied)         
                   
       if (occupied < 0):
            print("Occupied beds cannot be negative")
            return
               
       elif(occupied > total):
            print("Occupied beds cannot exceed total beds")
            return
       cursor.execute("""
                       UPDATE icu_beds
                       SET  occupied = ? WHERE level = ? AND bed_type = ?
               """, (occupied, level, bed_type))
       connection.commit()
               
    except ValueError:
        print("Enter occupied beds number only")
         
    

connection.close()

result4.mainloop()