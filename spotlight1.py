import customtkinter as ctk
from PIL import Image


def create_spotlight_screen1(parent):

    image = Image.open("D:\VS\Project\mnsaikia_spotlight.png")

    spotlight_image = ctk.CTkImage(
        light_image=image,
        dark_image=image,
        size=(1400, 720)
    )

    image_label = ctk.CTkLabel(
        parent,
        image=spotlight_image,
        text=""
    )

    image_label.pack(expand=True)

    def resize_image(event):
        ratio = 16 / 9

        width = event.width
        height = int(width / ratio)

        if height > event.height:
            height = event.height
            width = int(height * ratio)

        spotlight_image.configure(size=(width, height))

    parent.bind("<Configure>", resize_image)