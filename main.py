import customtkinter as ctk
from doctors import create_doctors_screen
from icu import create_icu_screen

main = ctk.CTk()


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

doctors_page = ctk.CTkFrame(page_container)
icu_page = ctk.CTkFrame(page_container)

# Same grid position: the pages overlap.
doctors_page.grid(row=0, column=0, sticky="nsew")
icu_page.grid(row=0, column=0, sticky="nsew")

# Build each screen once.
create_doctors_screen(doctors_page)
refresh_icu = create_icu_screen(icu_page)


def show_doctors():
    doctors_page.tkraise()


def show_icu():
    refresh_icu()
    icu_page.tkraise()


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

# Default page when the application starts.
show_doctors()

main.mainloop()
