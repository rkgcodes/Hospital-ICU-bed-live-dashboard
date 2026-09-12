import customtkinter as ctk
from datetime import datetime

ctk.set_appearance_mode("dark")

polish2 = ctk.CTk()

polish2.title("Polish exercise 2")
polish2.geometry("1400x800")

heading_font = ctk.CTkFont(size=18, weight="bold")
number_font = ctk.CTkFont(size=48, weight="bold")
header = ctk.CTkFrame(polish2, corner_radius=15)
header.pack(pady=20)
now = datetime.now()
string_date = now.strftime("%d-%m-%Y %H:%M:%S")
now = "Last updated on: "+string_date


title = ctk.CTkLabel(
    header,
    text="ICU BED LIVE DASHBOARD",
    font=heading_font
)
title.grid(
    row=0,
    column=0,
    padx=20,
    pady=20,
    sticky="w"    
)
title1 = ctk.CTkLabel(
    header,
    text="● LIVE",
    font=heading_font
)
title1.grid(
    row=0,
    column=1,
    padx=20,
    pady=20,
    sticky="e"    
)
title2 = ctk.CTkLabel(
    header,
    text=now
)
title2.grid(
    row=1,
    column=0,
    padx=20,
    pady=20,
    sticky="w"    
)
top_frame= ctk.CTkFrame(polish2, corner_radius=15)
top_frame.pack(fill="x")

top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)
top_frame.grid_columnconfigure(2, weight=1)


total_card = ctk.CTkFrame(top_frame, fg_color="blue", corner_radius=15)
total_card.grid(
    row=0,
    column=0,
    padx=15,
    pady=15,
    sticky="nsew"
    
)


total_label = ctk.CTkLabel(
    total_card,
    text="TOTAL BEDS",
    anchor="w",    
    font=heading_font
)
total_label.pack()


totalnum_label = ctk.CTkLabel(
    total_card,
    text="50",
    anchor="w",
    font=number_font    
)
totalnum_label.pack()
    


available_card = ctk.CTkFrame(top_frame,fg_color="green", corner_radius=15)
available_card.grid(
    row=0,
    column=1,
    padx=15,
    pady=15,
    sticky="nsew"
)


available_label = ctk.CTkLabel(
    available_card,
    text="AVAILABLE",
    anchor="w",
    font=heading_font
)
available_label.pack()



availnum_label = ctk.CTkLabel(
    available_card,
    text="30",
    anchor="w",
    font=number_font
)
availnum_label.pack()

inuse_card = ctk.CTkFrame(top_frame, fg_color="red", corner_radius=15)
inuse_card.grid(
    row=0,
    column=2,
    padx=15,
    pady=15,
    sticky="nsew"
)


inuse_label = ctk.CTkLabel(
    inuse_card,
    text="IN USE",
    anchor="w",
    font=heading_font
)
inuse_label.pack()


inusenum_label = ctk.CTkLabel(
    inuse_card,
    text="20",
    anchor="w",
    font=number_font
    
)
inusenum_label.pack()





second_frame= ctk.CTkFrame(polish2, corner_radius=15)
second_frame.pack(fill="x")
second_frame.grid_columnconfigure(0, weight=1)


def print_num():
    num= numstr.get()
    num=int(num)
    result_label.configure(num)


admin_card = ctk.CTkFrame(second_frame, fg_color="grey", corner_radius=15)
admin_card.grid(
    row=0,
    column=0,
    padx=20,
    pady=20,
    sticky="nsew"
    
)

belowlabel = ctk.CTkLabel(
    admin_card,
    text="ADMIN UPDATE ",
    anchor="w",
    font=heading_font
    )
belowlabel.pack()

adminlabel = ctk.CTkLabel(
    admin_card,
    text="Beds Currently in use: ",
    anchor="w",
    font=heading_font
    )
adminlabel.pack()
    

numstr = ctk.CTkEntry(admin_card)      
numstr.pack()

button = ctk.CTkButton(
    admin_card,
    text="UPDATE",
    font=heading_font,
    command=print_num
    
)
button.pack()

result_label = ctk.CTkLabel(admin_card, text="")
result_label.pack()


polish2.mainloop()