



def create_doctors_screen(parent, ctk):
    heading_font = ctk.CTkFont(size=24)
    inside_font = ctk.CTkFont(size=18)
        
    title_label = ctk.CTkLabel(
            parent,
            text="AROGYA DIGITAL",
            font=heading_font
                        
        )

    card = ctk.CTkFrame(parent)
        

    inside_label= ctk.CTkLabel(
            card,
            text="TODAY'S  DOCTORS",
            font=inside_font
            
        )
    
    
    title_label.pack(padx=40, pady=40)
    card.pack(padx=40, pady=40)
    inside_label.pack(padx=40, pady=40)






