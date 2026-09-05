import customtkinter as ctk

ctk.set_appearance_mode("dark")

exe = ctk.CTk()
exe.title("Excercise")
exe.geometry("600x400")

def print_name():
    entered_name = name.get()
    result_label.configure(text="Hello " + entered_name)

header = ctk.CTkFrame(exe)
header.pack()

title = ctk.CTkLabel(
    header,
    text="MY ICU APPLICATION"
)


title.pack(pady=20)


label = ctk.CTkLabel(exe, text="Enter your name:")
label.pack()

name = ctk.CTkEntry(exe)       

name.pack(pady=10)


button = ctk.CTkButton(
    exe,
    text="CLICK ME",
    command=print_name
    
)
button.pack(pady=10)

result_label = ctk.CTkLabel(exe, text="")
result_label.pack()

exe.mainloop()
