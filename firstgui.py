import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()

app.title("My First GUI")
app.geometry("600x400")


def hello():
    print("Button clicked!")


header = ctk.CTkFrame(app)
header.pack(pady=20)

title = ctk.CTkLabel(
    header,
    text="My First Application"
)
title.pack()


name = ctk.CTkEntry(
    app,
    placeholder_text="Enter your name"
)
name.pack(pady=10)


button = ctk.CTkButton(
    app,
    text="CLICK ME",
    command=hello
)
button.pack(pady=10)


app.mainloop()