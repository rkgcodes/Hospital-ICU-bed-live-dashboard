import customtkinter as ctk

from theme import create_fonts
from doctors import create_doctors_screen
from icu import create_icu_screen
from spotlight import create_spotlight_screen
from spotlight1 import create_spotlight_screen1

from theme import (
    BG_MAIN    
   
)
main = ctk.CTk()

fonts = create_fonts()


ctk.set_appearance_mode("dark")

main.title("main")
main.geometry("1400x800")


# Navigation stays visible above both pages.
navigation = ctk.CTkFrame(main)
navigation.pack(fill="x", padx=10, pady=(10, 0))

# Both pages share this display area.
page_container = ctk.CTkFrame(main)
page_container.pack(fill="both", expand=True, padx=10, pady=10)

page_container.grid_rowconfigure(0, weight=1)
page_container.grid_columnconfigure(0, weight=1)

doctors_page = ctk.CTkFrame(page_container, fg_color=BG_MAIN)
icu_page = ctk.CTkFrame(page_container)
spotlight_page = ctk.CTkFrame(page_container)
spotlight_page1 = ctk.CTkFrame(page_container)

# Same grid position: the pages overlap.
doctors_page.grid(row=0, column=0, sticky="nsew")
icu_page.grid(row=0, column=0, sticky="nsew")
spotlight_page.grid(row=0, column=0, sticky="nsew")
spotlight_page1.grid(row=0, column=0, sticky="nsew")


# Build each screen once.
create_doctors_screen(doctors_page, fonts)
refresh_icu = create_icu_screen(icu_page, fonts)
create_spotlight_screen(spotlight_page)
create_spotlight_screen1(spotlight_page1)


def show_doctors():
    doctors_page.tkraise()


def show_icu():
    refresh_icu()
    icu_page.tkraise()

def show_spotlight():
    spotlight_page.tkraise()

def show_spotlight1():
    spotlight_page1.tkraise()




current_page = 0
def auto_rotate():
    global current_page

    if current_page == 0:
        show_doctors()

    elif current_page == 1:
        show_icu()

    elif current_page == 2:
        show_spotlight()

    else:
        show_spotlight1()
   
    current_page = (current_page + 1) % 4

    main.after(5000, auto_rotate)



auto_rotate()




doctors_button = ctk.CTkButton(
    navigation,
    text="TODAY'S DOCTORS",
    command=show_doctors
)
doctors_button.pack(side="left", padx=10, pady=10)

icu_button = ctk.CTkButton(
    navigation,
    text="ICU AVAILABILITY",
    command=show_icu
)
icu_button.pack(side="left", padx=10, pady=10)

spotlight_button = ctk.CTkButton(
    navigation,
    text="DOCTOR'S SPOTLIGHT 1",
    command=show_spotlight
)
spotlight_button.pack(side="left", padx=10, pady=10)

spotlight_button1 = ctk.CTkButton(
    navigation,
    text="DOCTOR'S SPOTLIGHT 2",
    command=show_spotlight
)
spotlight_button1.pack(side="left", padx=10, pady=10)


# Default page when the application starts.



main.mainloop()
