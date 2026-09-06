import customtkinter as ctk

ctk.set_appearance_mode("dark")

grid_exercise = ctk.CTk()

grid_exercise.title("grid exercise")
grid_exercise.geometry("1400x800")


header = ctk.CTkFrame(grid_exercise)
header.pack(pady=20)

title = ctk.CTkLabel(
    header,
    text="ICU INFORMATION"
)
title.pack()

top_frame= ctk.CTkFrame(grid_exercise)
top_frame.pack(fill="x")
top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)
top_frame.grid_columnconfigure(2, weight=1)


total_label = ctk.CTkLabel(
    top_frame,
    text="TOTAL BEDS",
    anchor="w"
)
total_label.grid(
    row=0,
    column=0,
    padx=20,
    pady=10,
    sticky="ew"
)

available_label = ctk.CTkLabel(
    top_frame,
    text="AVAILABLE",
    anchor="w"
)
available_label.grid(
    row=0,
    column=1,
    padx=20,
    pady=10,
    sticky="ew"
)
inuse_label = ctk.CTkLabel(
    top_frame,
    text="IN USE",
    anchor="w"
)
inuse_label.grid(
    row=0,
    column=2,
    padx=20,
    pady=10,
    sticky="ew"
)

totalnum_label = ctk.CTkLabel(
    top_frame,
    text="50",
    anchor="w"
)
totalnum_label.grid(
    row=1,
    column=0,
    padx=20,
    pady=10,
    sticky="ew"
)

inusenum_label = ctk.CTkLabel(
    top_frame,
    text="30",
    anchor="w"
)
inusenum_label.grid(
    row=1,
    column=1,
    padx=20,
    pady=10,
    sticky="ew"
)

availnum_label = ctk.CTkLabel(
    top_frame,
    text="20",
    anchor="w"
)
availnum_label.grid(
    row=1,
    column=2,
    padx=20,
    pady=10,
    sticky="ew"
)



grid_exercise.mainloop()
