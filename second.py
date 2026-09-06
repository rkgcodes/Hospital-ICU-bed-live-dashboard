import customtkinter as ctk

ctk.set_appearance_mode("dark")

second = ctk.CTk()

second.title("second exercise")
second.geometry("1400x800")

heading_font = ctk.CTkFont(size=18, weight="bold")
number_font = ctk.CTkFont(size=40, weight="bold")
header = ctk.CTkFrame(second)
header.pack(pady=20)


title = ctk.CTkLabel(
    header,
    text="ICU BED LIVE DASHBOARD",
    font=heading_font
)
title.pack()

top_frame= ctk.CTkFrame(second)
top_frame.pack(fill="x")

top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)
top_frame.grid_columnconfigure(2, weight=1)


total_card = ctk.CTkFrame(top_frame)
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
    


available_card = ctk.CTkFrame(top_frame)
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

inuse_card = ctk.CTkFrame(top_frame)
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


ventilator_frame= ctk.CTkFrame(second)
ventilator_frame.pack(fill="x")
ventilator_frame.grid_columnconfigure(0, weight=1)
ventilator_frame.grid_columnconfigure(1, weight=1)
ventilator_frame.grid_columnconfigure(2, weight=1)


venti_total_card = ctk.CTkFrame(ventilator_frame)
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
venti_total_label.pack()


ventitotalnum_label = ctk.CTkLabel(
    venti_total_card,
    text="10",
    anchor="w",
    font=number_font    
)
ventitotalnum_label.pack()
    


venti_inuse_card = ctk.CTkFrame(ventilator_frame)
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
venti_inuse_label.pack()

ventiinusenum_label = ctk.CTkLabel(
    venti_inuse_card,
    text="5",
    anchor="w",
    font=number_font
    
)
ventiinusenum_label.pack()


withoutventi_card = ctk.CTkFrame(ventilator_frame)
withoutventi_card.grid(
    row=0,
    column=2,
    padx=15,
    pady=15,
    sticky="nsew"
)

withoutventi_label = ctk.CTkLabel(
    withoutventi_card,
    text="WITHOUT VENTILATOR",
    anchor="w",
    font=heading_font
)
withoutventi_label.pack()

withoutventinum_label = ctk.CTkLabel(
    withoutventi_card,
    text="40",
    anchor="w",
    font=number_font
    
)
withoutventinum_label.pack()

second.mainloop()
