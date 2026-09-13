import customtkinter as ctk
from datetime import datetime

ctk.set_appearance_mode("dark")

polish2 = ctk.CTk()

polish2.title("Polish exercise 2")
polish2.geometry("1400x800")

heading_font = ctk.CTkFont(size=18, weight="bold")
update_font = ctk.CTkFont(size=14)
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
    font=update_font,
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


total_card = ctk.CTkFrame(top_frame, fg_color="#2563eb", corner_radius=15)
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
total_label.pack(pady=10)


totalnum_label = ctk.CTkLabel(
    total_card,
    text="50",
    anchor="w",
    font=number_font    
)
totalnum_label.pack(pady=10)
    


available_card = ctk.CTkFrame(top_frame,fg_color="#15803d", corner_radius=15)
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
available_label.pack(pady=10)



availnum_label = ctk.CTkLabel(
    available_card,
    text="30",
    anchor="w",
    font=number_font
)
availnum_label.pack(pady=10)

inuse_card = ctk.CTkFrame(top_frame, fg_color="#dc2626", corner_radius=15)
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
inuse_label.pack(pady=10)


inusenum_label = ctk.CTkLabel(
    inuse_card,
    text="20",
    anchor="w",
    font=number_font
    
)
inusenum_label.pack(pady=10)

ventilator_frame= ctk.CTkFrame(polish2, corner_radius=15)
ventilator_frame.pack(fill="x")
ventilator_frame.grid_columnconfigure(0, weight=1)
ventilator_frame.grid_columnconfigure(1, weight=1)
ventilator_frame.grid_columnconfigure(2, weight=1)


venti_total_card = ctk.CTkFrame(ventilator_frame, fg_color="#7C3AED", corner_radius=15)
venti_total_card.grid(
    row=0,
    column=0,
    padx=15,
    pady=15,
    sticky="nsew"
)
venti_total_label = ctk.CTkLabel(
    venti_total_card,
    text="WITH VENTILATOR",
    anchor="w",    
    font=heading_font
)
venti_total_label.pack(pady=10)


ventitotalnum_label = ctk.CTkLabel(
    venti_total_card,
    text="10",
    anchor="w",
    font=number_font    
)
ventitotalnum_label.pack(pady=10)
    


venti_inuse_card = ctk.CTkFrame(ventilator_frame,fg_color="#D97706", corner_radius=15)
venti_inuse_card.grid(
    row=0,
    column=1,
    padx=15,
    pady=15,
    sticky="nsew"
)

venti_inuse_label = ctk.CTkLabel(
    venti_inuse_card,
    text="IN USE",
    anchor="w",
    font=heading_font
)
venti_inuse_label.pack(pady=10)

ventiinusenum_label = ctk.CTkLabel(
    venti_inuse_card,
    text="5",
    anchor="w",
    font=number_font
    
)
ventiinusenum_label.pack(pady=10)


withoutventi_card = ctk.CTkFrame(ventilator_frame, fg_color="#0F766E", corner_radius=15)
withoutventi_card.grid(
    row=0,
    column=2,
    padx=15,
    pady=15,
    sticky="nsew"
)

withoutventi_label = ctk.CTkLabel(
    withoutventi_card,
    text="W/O VENTILATOR",
    anchor="w",
    font=heading_font
)
withoutventi_label.pack(pady=10)

withoutventinum_label = ctk.CTkLabel(
    withoutventi_card,
    text="40",
    anchor="w",
    font=number_font
    
)
withoutventinum_label.pack(pady=10)




second_frame= ctk.CTkFrame(polish2, corner_radius=15)
second_frame.pack(fill="x")
second_frame.grid_columnconfigure(0, weight=1)




def print_num():    

    try:
        num = int(numstr.get())
    

        if (0<=num<=50):

            available = 50 - num
            inusenum_label.configure(text=str(num))
            availnum_label.configure(text=str(available))
            title2.configure(text="Last updated on: "+ datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
            result_label.configure(text="✓ Dashboard Updated")
        
        else:
            result_label.configure(admin_card, text="⚠️ Enter a valid number")

    except ValueError:
                result_label.configure(admin_card, text="⚠️ Enter a valid number")

    
    


admin_card = ctk.CTkFrame(second_frame, fg_color="#2b2b2b", corner_radius=15)
admin_card.grid(
    row=0,
    column=0,
    padx=20,
    pady=20,
    sticky="w"
    
)

belowlabel = ctk.CTkLabel(
    admin_card,
    text="ADMIN UPDATE ",
    anchor="w",
    font=heading_font
    )
belowlabel.pack(pady=10)

adminlabel = ctk.CTkLabel(
    admin_card,
    text="ICU Beds Currently in use: ",
    anchor="w",
    font=heading_font
    )
adminlabel.pack(pady=10)
    

numstr = ctk.CTkEntry(admin_card)      
numstr.pack()

button = ctk.CTkButton(
    admin_card,
    text="UPDATE",
    font=heading_font,
    command=print_num
    
)
button.pack(pady=10)

result_label = ctk.CTkLabel(admin_card, text="")
result_label.pack(pady=10)




def vprint_num():    

    try:
        vnum = int(vnumstr.get())
    

        if (0<=vnum<=10):

            ventiinusenum_label.configure(text=str(vnum))            
            title2.configure(text="Last updated on: "+ datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
            vresult_label.configure(text="✓ Dashboard Updated")
        
        else:
            vresult_label.configure(vadmin_card, text="⚠️ Enter a valid number")

    except ValueError:            
            vresult_label.configure(vadmin_card, text="⚠️ Enter a valid number")

    
    


vadmin_card = ctk.CTkFrame(second_frame, fg_color="#2b2b2b", corner_radius=15)
vadmin_card.grid(
    row=0,
    column=0,
    padx=20,
    pady=20,
    sticky="e"
    
)

vbelowlabel = ctk.CTkLabel(
    vadmin_card,
    text="ADMIN UPDATE ",
    anchor="w",
    font=heading_font
    )
vbelowlabel.pack(pady=10)

vadminlabel = ctk.CTkLabel(
    vadmin_card,
    text="ICU beds Currently in use with ventilator: ",
    anchor="w",
    font=heading_font
    )
vadminlabel.pack(pady=10)
    

vnumstr = ctk.CTkEntry(vadmin_card)      
vnumstr.pack()

vbutton = ctk.CTkButton(
    vadmin_card,
    text="UPDATE",
    font=heading_font,
    command=vprint_num
    
)
vbutton.pack(pady=10)

vresult_label = ctk.CTkLabel(vadmin_card, text="")
vresult_label.pack(pady=10)


polish2.mainloop()