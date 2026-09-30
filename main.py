import customtkinter as ctk
from doctors import create_doctors_screen


main = ctk.CTk()


ctk.set_appearance_mode("dark")

main.title("main")
main.geometry("1400x800")


doctors_page = ctk.CTkFrame(main)
doctors_page.pack(padx=10, pady=10)

create_doctors_screen(doctors_page)

main.mainloop()
