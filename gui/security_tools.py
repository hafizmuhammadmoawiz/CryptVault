import os
import sys
import subprocess

import customtkinter as ctk
from datetime import datetime

from PIL import Image
from tkinter import messagebox

# ======================================================
# PROJECT PATH
# ======================================================

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(project_root)

# ======================================================
# APPLICATION SETTINGS
# ======================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ======================================================
# MAIN WINDOW
# ======================================================

app = ctk.CTk()

app.title("CryptVault - Security Tools")

app.geometry("570x675")

app.resizable(False, False)

app.configure(fg_color="#02060a")

# ======================================================
# BACKGROUND IMAGE
# ======================================================

background_path = os.path.join(project_root, "assets", "enc.jpg")

background_image = ctk.CTkImage(
    light_image=Image.open(background_path),
    dark_image=Image.open(background_path),
    size=(570, 675),
)

background_label = ctk.CTkLabel(app, image=background_image, text="")

background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# ======================================================
# MAIN GLASS PANEL
# ======================================================

main_frame = ctk.CTkFrame(
    app,
    width=540,
    height=660,
    corner_radius=30,
    fg_color="#0b1118",
    border_width=2,
    border_color="#3ea6ff",
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

main_frame.pack_propagate(False)

# ======================================================
# VAULT LOGO
# ======================================================

vault_logo = ctk.CTkImage(
    light_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    dark_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    size=(50, 50),
)

logo_label = ctk.CTkLabel(main_frame, image=vault_logo, text="")

logo_label.pack(pady=(5, 3))

# ======================================================
# TITLE
# ======================================================

title_label = ctk.CTkLabel(
    main_frame, text="Security Tools", font=("Segoe UI", 25, "bold"), text_color="white"
)

title_label.pack()

# ======================================================
# SUBTITLE
# ======================================================

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Offensive Security Analysis Suite",
    font=("Segoe UI", 13),
    text_color="#8fb6d9",
)

subtitle_label.pack(pady=(2, 3))

# ======================================================
# SEPARATOR
# ======================================================

separator = ctk.CTkFrame(main_frame, height=2, fg_color="#1f6aa5")

separator.pack(fill="x", padx=10)


# ======================================================
# TOOLKIT STATUS CARD
# ======================================================

status_card = ctk.CTkFrame(
    main_frame,
    width=470,
    height=60,
    corner_radius=20,
    fg_color="#111827",
    border_width=1,
    border_color="#244b74",
)

status_card.pack(pady=(11, 11))

status_card.pack_propagate(False)

left_status = ctk.CTkLabel(
    status_card,
    text=("Available Tools\n" "3"),
    justify="center",
    font=("Segoe UI", 15, "bold"),
    text_color="white",
)

left_status.place(relx=0.22, rely=0.5, anchor="center")

middle_line = ctk.CTkFrame(status_card, width=2, height=40, fg_color="#1f6aa5")

middle_line.place(relx=0.5, rely=0.5, anchor="center")

right_status = ctk.CTkLabel(
    status_card,
    text=("Toolkit Status\n" "🟢 READY"),
    justify="center",
    font=("Segoe UI", 15, "bold"),
    text_color="#00ff88",
)

right_status.place(relx=0.77, rely=0.5, anchor="center")


# ======================================================
# SELECTED TOOL
# ======================================================

selected_tool = None

selected_card = None

tool_cards = []

# ======================================================
# TOOL SELECTION
# ======================================================


def select_tool(tool_name, card):

    global selected_tool
    global selected_card

    selected_tool = tool_name

    selected_card = card

    # Reset All Cards

    for tool in tool_cards:

        tool.configure(fg_color="#111827", border_color="#3ea6ff")

    # Highlight Selected Card

    card.configure(fg_color="#162536", border_color="#00ff88")


# ======================================================
# HOVER EFFECT
# ======================================================


def card_enter(card):

    if card != selected_card:

        card.configure(fg_color="#172331")


def card_leave(card):

    if card != selected_card:

        card.configure(fg_color="#111827")


# ======================================================
# CREATE TOOL CARD
# ======================================================


def create_tool_card(title, description, category, tool_name):

    card = ctk.CTkFrame(
        main_frame,
        width=470,
        height=90,
        corner_radius=24,
        fg_color="#111827",
        border_width=2,
        border_color="#3ea6ff",
        cursor="hand2",
    )

    card.pack(pady=(0, 15))

    card.pack_propagate(False)

    # ==========================================
    # TITLE
    # ==========================================

    title_label = ctk.CTkLabel(
        card, text=title, font=("Segoe UI", 18, "bold"), text_color="white"
    )

    title_label.pack(anchor="w", padx=13, pady=(9, 2))

    # ==========================================
    # DESCRIPTION
    # ==========================================

    description_label = ctk.CTkLabel(
        card,
        text=description,
        justify="left",
        wraplength=400,
        font=("Segoe UI", 12),
        text_color="#9fbad6",
    )

    description_label.pack(anchor="w", padx=20)

    # ==========================================
    # READY BADGE
    # ==========================================

    ready_label = ctk.CTkLabel(
        card, text="● READY", font=("Segoe UI", 11, "bold"), text_color="#00ff88"
    )

    ready_label.place(relx=0.93, rely=0.18, anchor="e")

    # ==========================================
    # EVENTS
    # ==========================================

    widgets = [card, title_label, description_label, ready_label]

    for widget in widgets:

        widget.bind(
            "<Button-1>", lambda e, name=tool_name, frame=card: select_tool(name, frame)
        )

        widget.bind("<Enter>", lambda e, frame=card: card_enter(frame))

        widget.bind("<Leave>", lambda e, frame=card: card_leave(frame))

    tool_cards.append(card)

    return card


# ======================================================
# PASSWORD ATTACK SIMULATOR
# ======================================================

attack_card = create_tool_card(
    title="⚔ Password Attack Simulator",
    description=(
        "Analyze password complexity, estimate brute-force "
        "resistance and evaluate attack feasibility."
    ),
    category="Offensive Security",
    tool_name="attack",
)

# ======================================================
# SHA-256 INTEGRITY CHECKER
# ======================================================

hash_card = create_tool_card(
    title="🛡 File Integrity Verifier",
    description=(
        "Generate and compare SHA-256 hashes to verify "
        "whether a file has been modified."
    ),
    category="Digital Forensics",
    tool_name="hash",
)

# ======================================================
# HASH IDENTIFIER
# ======================================================

identifier_card = create_tool_card(
    title="🔍 Hash Identifier",
    description=(
        "Automatically identify hash algorithms such as "
        "MD5, SHA-1, SHA-256 and SHA-512."
    ),
    category="Hash Analysis",
    tool_name="identifier",
)
# ======================================================
# OPEN SELECTED TOOL
# ======================================================


def launch_tool():

    if selected_tool is None:

        messagebox.showwarning(
            "No Tool Selected", "Please select a security tool first."
        )

        return

    app.destroy()

    tool_pages = {
        "attack": "password_attack.py",
        "hash": "file_integrity_verifier.py",
        "identifier": "hash_identifier.py",
    }

    subprocess.Popen(["python", os.path.join("gui", tool_pages[selected_tool])])


# ======================================================
# BACK TO DASHBOARD
# ======================================================


def back_to_dashboard():

    app.destroy()

    subprocess.Popen(["python", os.path.join("gui", "dashboard.py")])


# ======================================================
# ACTION BUTTONS
# ======================================================

button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

button_frame.pack(side="bottom", pady=(20, 20))

# ======================================================
# LAUNCH BUTTON
# ======================================================

launch_btn = ctk.CTkButton(
    button_frame,
    text="▶ Launch Selected Tool",
    width=240,
    height=60,
    corner_radius=24,
    font=("Segoe UI", 17, "bold"),
    fg_color="#1f6aa5",
    hover_color="#2d7fd3",
    border_width=2,
    border_color="#58b5ff",
    command=launch_tool,
)

launch_btn.grid(row=0, column=0, padx=(0, 12))

# ======================================================
# BACK BUTTON
# ======================================================

back_btn = ctk.CTkButton(
    button_frame,
    text="← Dashboard",
    width=170,
    height=60,
    corner_radius=24,
    font=("Segoe UI", 16, "bold"),
    fg_color="#161616",
    hover_color="#262626",
    border_width=2,
    border_color="#3ea6ff",
    command=back_to_dashboard,
)

back_btn.grid(row=0, column=1)

# ======================================================
# FOOTER SEPARATOR
# ======================================================

footer_line = ctk.CTkFrame(main_frame, height=1, fg_color="#20364f")

footer_line.pack(side="bottom", fill="x", padx=30, pady=(8, 8))

# ======================================================
# FOOTER
# ======================================================

footer_label = ctk.CTkLabel(
    main_frame,
    text="CryptVault • Offensive Security Analysis Suite",
    font=("Segoe UI", 11),
    text_color="#70879d",
)

footer_label.pack(side="bottom", pady=(0, 2))

# ======================================================
# RUN APPLICATION
# ======================================================

app.mainloop()
