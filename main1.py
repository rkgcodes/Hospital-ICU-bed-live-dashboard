
import customtkinter as ctk
from doctors import get_todays_doctors, create_doctor_card, open_admin
from icu import create_level, create_icu_card, get_icu_status, update_occupied, open_admin, refresh_level

from datetime import datetime


main = ctk.CTk()


ctk.set_appearance_mode("dark")

main.title("main")
main.geometry("1400x800")

today = datetime.now().strftime("%Y-%m-%d")
heading_font = ctk.CTkFont(size=24, weight="bold")
inside_font = ctk.CTkFont(size=15, weight="bold")




title_label = ctk.CTkLabel(
    main,
    text="AROGYA DIGITAL",
    font=heading_font
                        
    )
hospital_label = ctk.CTkLabel(
    main,
    text="AROGYA HOSPITAL AND RESEARCH CENTRE",
    font=inside_font
                        
    )

title_label.pack(padx=10)
hospital_label.pack(padx=10)

page_container = ctk.CTkFrame(main)
page_container.pack(fill="both", expand=True)

icu_page = ctk.CTkFrame(page_container)
doctors_page = ctk.CTkFrame(page_container)

icu_page.grid(row=0, column=0, sticky="nsew")
doctors_page.grid(row=0, column=0, sticky="nsew")

page_container.grid_rowconfigure(0, weight=1)
page_container.grid_columnconfigure(0, weight=1)

icu_button = ctk.CTkButton(
    icu_page,
    text="ICU AVAILABILITY",
    command=icu_page.tkraise
)

doctors_button = ctk.CTkButton(
    doctors_page,
    text="TODAY'S DOCTORS",
    command=doctors_page.tkraise
)
icu_button.grid(row=1, column=0, sticky="nsew")
doctors_button.grid(row=1, column=1, sticky="nsew")


doctors_page.grid_columnconfigure(0, weight=1)
doctors_page.grid_columnconfigure(1, weight=1)
doctors_page.grid_columnconfigure(2, weight=1)

doctors_page.grid_rowconfigure(0, weight=1)
doctors_page.grid_rowconfigure(1, weight=1)
doctors_page.grid_rowconfigure(2, weight=1)



icu_page.grid_rowconfigure(0, weight=1)
icu_page.grid_rowconfigure(1, weight=1)
icu_page.grid_rowconfigure(2, weight=1)
icu_page.grid_rowconfigure(3, weight=1)

doctors_frame= ctk.CTkFrame(doctors_page, corner_radius=15)
doctors_frame.grid(row=2, column=0, sticky="nsew")


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
admin_button.grid(pady=10)



#icu ui code begins here

level1 = create_level(icu_page, 1)  
level2 = create_level(icu_page, 2)
level3 = create_level(icu_page, 3)



refresh_level(level1,1)
refresh_level(level2,2)
refresh_level(level2,3)






main.mainloop()