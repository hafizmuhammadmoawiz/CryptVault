import os
import sys
import subprocess

import customtkinter as ctk

from PIL import Image

from tkinter import messagebox

# =====================================================
# PROJECT ROOT
# =====================================================

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(project_root)

# =====================================================
# APP SETTINGS
# =====================================================

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

# =====================================================
# MAIN WINDOW
# =====================================================

app = ctk.CTk()

app.title("CryptVault - My Files")

app.geometry("570x675")

app.resizable(False, False)

app.configure(fg_color="#02060A")

# =====================================================
# BACKGROUND
# =====================================================

background_path = os.path.join(project_root, "assets", "enc.jpg")

background_image = ctk.CTkImage(
    light_image=Image.open(background_path),
    dark_image=Image.open(background_path),
    size=(570, 675),
)

background_label = ctk.CTkLabel(app, image=background_image, text="")

background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# =====================================================
# MAIN PANEL
# =====================================================

main_frame = ctk.CTkFrame(
    app,
    width=540,
    height=655,
    corner_radius=28,
    fg_color="#0b1118",
    border_width=2,
    border_color="#3ea6ff",
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

main_frame.pack_propagate(False)

# =====================================================
# LOGO
# =====================================================

vault_logo = ctk.CTkImage(
    light_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    dark_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    size=(58, 58),
)

logo_label = ctk.CTkLabel(main_frame, image=vault_logo, text="")

logo_label.pack(pady=(8, 4))

# =====================================================
# TITLE
# =====================================================

title_label = ctk.CTkLabel(
    main_frame, text="My Files", font=("Segoe UI", 24, "bold"), text_color="white"
)

title_label.pack()

# =====================================================
# SUBTITLE
# =====================================================

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Manage your encrypted file history",
    font=("Segoe UI", 12),
    text_color="#93b7d7",
)

subtitle_label.pack(pady=(2, 4))

# =====================================================
# TOP SEPARATOR
# =====================================================

top_separator = ctk.CTkFrame(main_frame, height=2, fg_color="#1f6aa5")

top_separator.pack(fill="x", padx=18, pady=(0, 8))

# =====================================================
# SCROLLABLE AREA
# =====================================================

scroll_frame = ctk.CTkScrollableFrame(
    main_frame, width=500, height=320, corner_radius=20, fg_color="transparent"
)

scroll_frame.pack(fill="both", expand=True, padx=18, pady=(0, 3))

# =====================================================
# FILE CARD (DUMMY)
# =====================================================

file_card = ctk.CTkFrame(
    scroll_frame,
    corner_radius=18,
    fg_color="#111827",
    border_width=2,
    border_color="#244b74",
)

file_card.pack(fill="x", pady=(0, 7))

# =====================================================
# ROW BUILDER
# =====================================================


def create_row(
    parent,
    left_title,
    left_value,
    center_title,
    center_value,
    button_text,
    button_color,
):

    row = ctk.CTkFrame(parent, fg_color="transparent")

    row.pack(fill="x", padx=14, pady=4)

    # LEFT

    left = ctk.CTkFrame(row, fg_color="transparent")

    left.pack(side="left", expand=True, anchor="w")

    ctk.CTkLabel(
        left, text=left_title, font=("Segoe UI", 12, "bold"), text_color="white"
    ).pack(anchor="w")

    ctk.CTkLabel(
        left, text=left_value, font=("Segoe UI", 12), text_color="#6bc5ff"
    ).pack(anchor="w")

    # CENTER

    center = ctk.CTkFrame(row, fg_color="transparent")

    center.pack(side="left", expand=True, anchor="w")

    ctk.CTkLabel(
        center, text=center_title, font=("Segoe UI", 12, "bold"), text_color="white"
    ).pack(anchor="w")

    ctk.CTkLabel(
        center, text=center_value, font=("Segoe UI", 12), text_color="#6bc5ff"
    ).pack(anchor="w")

    # BUTTON

    btn = ctk.CTkButton(
        row,
        text=button_text,
        width=95,
        height=34,
        corner_radius=10,
        fg_color=button_color,
        hover_color=button_color,
        font=("Segoe UI", 12, "bold"),
    )

    btn.pack(side="right", padx=(10, 0))


# =====================================================
# DUMMY DATA
# =====================================================

create_row(
    file_card,
    "Original File",
    "report.pdf",
    "Original Path",
    r"D:\...\report.pdf",
    "📂 Open",
    "#1f6aa5",
)

create_row(
    file_card,
    "Encrypted File",
    "report.pdf.enc",
    "Encrypted Path",
    r"D:\...\report.pdf.enc",
    "📂 Open",
    "#1f6aa5",
)

create_row(
    file_card,
    "Key File",
    "report.key",
    "Key Path",
    r"D:\...\report.key",
    "❌ Missing",
    "#b3261e",
)

create_row(file_card, "Size", "2.35 MB", "Status", "Encrypted", "Delete", "#5b1f1f")

create_row(
    file_card,
    "Encrypted At",
    "07-Jul-2026",
    "Decrypted At",
    "Not Yet",
    "Details",
    "#3a3a3a",
)


# =====================================================
# BOTTOM SEPARATOR
# =====================================================

bottom_separator = ctk.CTkFrame(main_frame, height=2, fg_color="#1f6aa5")

bottom_separator.pack(fill="x", padx=18, pady=(2, 8))

# =====================================================
# BUTTONS
# =====================================================

button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

button_frame.pack(pady=(0, 8))

refresh_btn = ctk.CTkButton(
    button_frame,
    text="🔄 Refresh",
    width=180,
    height=42,
    corner_radius=14,
    fg_color="#1f6aa5",
    hover_color="#2d7fd3",
    border_width=2,
    border_color="#58b5ff",
    font=("Segoe UI", 13, "bold"),
)

refresh_btn.pack(side="left", padx=10)

back_btn = ctk.CTkButton(
    button_frame,
    text="↩ Back",
    width=180,
    height=42,
    corner_radius=14,
    fg_color="#2d2d2d",
    hover_color="#3b3b3b",
    border_width=2,
    border_color="#58b5ff",
    font=("Segoe UI", 13, "bold"),
)

back_btn.pack(side="left", padx=10)

# =====================================================
# FOOTER
# =====================================================

footer_title = ctk.CTkLabel(
    main_frame,
    text="CryptVault File History",
    font=("Segoe UI", 12),
    text_color="#8d8d8d",
)

footer_title.pack(pady=(2, 0))

footer_subtitle = ctk.CTkLabel(
    main_frame,
    text="Track • Manage • Protect",
    font=("Segoe UI", 11),
    text_color="#6c6c6c",
)

footer_subtitle.pack(pady=(2, 4))

# =====================================================
# DUMMY BUTTON ACTIONS
# =====================================================

refresh_btn.configure(
    command=lambda: messagebox.showinfo(
        "Refresh", "Database integration coming in Part 2."
    )
)

back_btn.configure(command=lambda: app.destroy())

# =====================================================
# RUN
# =====================================================

app.mainloop()
