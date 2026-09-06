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
    text="ICU BED LIVE DASHBOARD"
)
title.pack()

top_frame= ctk.CTkFrame(second)
top_frame.pack(fill="x")

top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)
top_frame.grid_columnconfigure(2, weight=1)


total_card = ctk.CTkFrame(top_frame)
total_card.pack()


total_label= ctk.CTkFont(size=18, weight="bold")
total_label = ctk.CTkLabel(
    total_card,
    text="TOTAL BEDS",
    anchor="w"
)
total_label.grid(
    row=0,
    column=0,
    padx=15,
    pady=15,
    sticky="nsew"
)

totalnum_label = ctk.CTkFont(size=40, weight="bold")
totalnum_label = ctk.CTkLabel(
    total_card,
    text="50",
    anchor="w"
    
)
totalnum_label.grid(
    row=1,
    column=0,
    padx=15,
    pady=15,
    sticky="nsew"
)


available_card = ctk.CTkFrame(top_frame)
available_card.pack()

available_label= ctk.CTkFont(size=18, weight="bold")
available_label = ctk.CTkLabel(
    available_card,
    text="AVAILABLE",
    anchor="w"
)
available_label.grid(
    row=0,
    column=1,
    padx=15,
    pady=15,
    sticky="nsew"
)

availnum_label=ctk.CTkFont(size=40, weight="bold")
availnum_label = ctk.CTkLabel(
    available_card,
    text="30",
    anchor="w"
)
availnum_label.grid(
    row=1,
    column=1,
    padx=15,
    pady=15,
    sticky="nsew"
)

inuse_card = ctk.CTkFrame(top_frame)
inuse_card.pack()

inuse_label= ctk.CTkFont(size=18, weight="bold")
inuse_label = ctk.CTkLabel(
    inuse_card,
    text="IN USE",
    anchor="w"
)
inuse_label.grid(
    row=0,
    column=2,
    padx=15,
    pady=15,
    sticky="nsew"
)
inusenum_label=ctk.CTkFont(size=40, weight="bold")
inusenum_label = ctk.CTkLabel(
    inuse_card,
    text="20",
    anchor="w"
    
)
inusenum_label.grid(
    row=1,
    column=2,
    padx=15,
    pady=15,
    sticky="nsew"
)

second.mainloop()
