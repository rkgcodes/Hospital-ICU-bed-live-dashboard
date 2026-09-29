
import customtkinter as ctk
from doctors import create_doctors_screen, get_todays_doctors, refresh_doctors, create_doctor_card, open_admin
from datetime import datetime


main = ctk.CTk()


ctk.set_appearance_mode("dark")

main.title("main")
main.geometry("1400x800")

today = datetime.now().strftime("%Y-%m-%d")


doctors_page = ctk.CTkFrame(main)
doctors_page.pack(padx=10, pady=10)

create_doctors_screen(doctors_page)

doctors_page.grid_columnconfigure(0, weight=1)
doctors_page.grid_columnconfigure(1, weight=1)
doctors_page.grid_columnconfigure(2, weight=1)

doctors_page.grid_rowconfigure(0, weight=1)
doctors_page.grid_rowconfigure(1, weight=1)
doctors_page.grid_rowconfigure(2, weight=1)

doctors_frame= ctk.CTkFrame(doctors_page, corner_radius=15)
doctors_frame.pack()


doctors=get_todays_doctors(today)

for index, doctor in enumerate(doctors):
    row = index // 2
    column = index % 2
    
    create_doctor_card(doctors_frame, doctor, row, column)


admin_button = ctk.CTkButton(
        doctors_page,
        text="ADMIN",
        command=lambda: open_admin(doctors_frame)
    )
admin_button.pack(pady=10)

main.mainloop()