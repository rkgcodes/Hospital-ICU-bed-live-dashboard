

import customtkinter as ctk

BG_MAIN = "#101C2B"
BG_CARD = "#203247"
ACCENT = "#3B82F6"
ACCENT_HOVER = "#2563EB"
TEXT_PRIMARY = "#F0F6FC"
TEXT_SECONDARY = "#B8CCDE"
TEXT_SPECIALTY = "#79C7ED"
CARD_BORDER = "#365775"

# Available
AVAILABLE_BG = "#22C55E"
AVAILABLE_HOVER = "#16A34A"
AVAILABLE_TEXT = "#052E16"

# Appointments Closed
CLOSED_BG = "#FFB454"
CLOSED_HOVER = "#F59E0B"
CLOSED_TEXT = "#5A3000"

# Not Available
UNAVAILABLE_BG = "#FF6262"
UNAVAILABLE_HOVER = "#EF4444"
UNAVAILABLE_TEXT = "#5F0909"

# Not Scheduled
UNSCHEDULED_BG = "#B8C7D9"
UNSCHEDULED_HOVER = "#94A3B8"
UNSCHEDULED_TEXT = "#334155"


# ICU
ICU_TYPE = "#67C7F5"       # cyan — WITH/WITHOUT VENTILATOR

AVAILABLE_TEXT = "#4ADE80" # green
TOTAL_TEXT = "#FACC15"     # yellow
OCCUPIED_TEXT = "#FB7185"  # soft red/coral

ICU_CARD = "#20364D"
ICU_BORDER = "#365F7D"
TEXT_PRIMARY = "#F8FAFC"

def create_fonts():
    return {
        "doctor": ctk.CTkFont(
            family="Arial",
            size=28,
            weight="bold"
        ),
        "specialty": ctk.CTkFont(
            family="Arial",
            size=20,
            weight="bold"
        ),
        "body": ctk.CTkFont(
            family="Arial",
            size=15
        ),
        "available": ctk.CTkFont(
            family="Arial",
            size=54
        ),
        "venti": ctk.CTkFont(
            family="Arial",
            size=24
        ),
        "icuinfo": ctk.CTkFont(
            family="Arial",
            size=18,
            weight="bold"
        ),
        "statusfont": ctk.CTkFont(
            family="Arial",
            size=15,
            weight="bold"
        ) 

    


    }
  

