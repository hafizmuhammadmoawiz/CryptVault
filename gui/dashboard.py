import sys
import os
import subprocess

# =====================================
# CURRENT USER
# =====================================

try:

    with open("current_user.txt", "r") as file:

        current_user = file.read().strip()

except:

    current_user = "User"
# =====================================
# FIX IMPORT PATH
# =====================================

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(project_root)

# =====================================
# IMPORTS
# =====================================

import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

# =====================================
# APP SETTINGS
# =====================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =====================================
# BUTTON FUNCTIONS
# =====================================


from tkinter import filedialog


def encrypt_file():

    app.destroy()

    subprocess.Popen(["python", "gui/encrypt_file.py"])


def decrypt_file():

    app.destroy()

    subprocess.Popen(["python", "gui/decrypt_file.py"])


def my_files():
    messagebox.showinfo("Coming Soon", "Vault File Manager Coming Soon.")


def password_generator():

    app.destroy()

    subprocess.Popen(["python", "gui/password_generator.py"])


def security_tools():

    app.destroy()

    subprocess.Popen(["python", "gui/security_tools.py"])


def logout():

    try:

        os.remove("current_user.txt")

    except:

        pass

    app.destroy()

    subprocess.Popen(["python", "gui/login.py"])


# =====================================
# MAIN WINDOW
# =====================================

app = ctk.CTk()

app.title("CryptVault - Dashboard")

app.geometry("970x670")

app.resizable(False, False)

app.configure(fg_color="#02060a")

# =====================================
# BACKGROUND IMAGE
# =====================================

bg_path = os.path.join(project_root, "assets", "user.jpg")

bg_image = ctk.CTkImage(
    light_image=Image.open(bg_path), dark_image=Image.open(bg_path), size=(970, 670)
)

bg_label = ctk.CTkLabel(app, image=bg_image, text="")

bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# =====================================
# MAIN GLASS PANEL
# =====================================

main_frame = ctk.CTkFrame(
    app,
    width=910,
    height=650,
    corner_radius=25,
    fg_color="#111111",
    border_width=1,
    border_color="#1f6aa5",
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

main_frame.pack_propagate(False)

# =====================================
# HEADER FRAME
# =====================================

header_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

header_frame.pack(pady=(20, 10))

# =====================================
# LOGO
# =====================================

vault_logo = ctk.CTkImage(
    light_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    dark_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    size=(70, 70),
)

logo_label = ctk.CTkLabel(header_frame, image=vault_logo, text="")

logo_label.grid(row=0, column=0, rowspan=2, padx=(0, 15))

# =====================================
# TITLE
# =====================================

title_label = ctk.CTkLabel(
    header_frame, text="CryptVault", font=("Segoe UI", 32, "bold")
)

title_label.grid(row=0, column=1, sticky="w")

# =====================================
# SUBTITLE
# =====================================

subtitle_label = ctk.CTkLabel(
    header_frame,
    text="Your Personal Secure Vault",
    font=("Segoe UI", 14),
    text_color="lightgray",
)

subtitle_label.grid(row=1, column=1, sticky="w")

# =====================================
# WELCOME BANNER
# =====================================

welcome_frame = ctk.CTkFrame(
    main_frame,
    width=820,
    height=85,
    corner_radius=24,
    fg_color="#0b1d33",
    border_width=2,
    border_color="#3ea6ff",
)

welcome_frame.pack(pady=(15, 15), padx=30, fill="x")

welcome_frame.pack_propagate(False)

# =====================================
# WELCOME TITLE
# =====================================

welcome_label = ctk.CTkLabel(
    welcome_frame,
    text=f"Welcome to CryptVault, {current_user} • Secure Your Digital Assets",
    font=("Segoe UI", 21, "bold"),
    text_color="white",
)

welcome_label.place(relx=0.5, rely=0.38, anchor="center")

# =====================================
# TAGLINE
# =====================================

tagline_label = ctk.CTkLabel(
    welcome_frame,
    text="Protect • Encrypt • Manage • Secure",
    font=("Segoe UI", 12),
    text_color="#7db8ff",
)

tagline_label.place(relx=0.5, rely=0.72, anchor="center")
# =====================================
# CARD ICONS
# =====================================

encrypt_icon = ctk.CTkImage(
    Image.open(os.path.join(project_root, "assets", "encrypted_card.png")),
    size=(25, 25),
)

files_icon = ctk.CTkImage(
    Image.open(os.path.join(project_root, "assets", "file_card.png")),
    size=(25, 25),
)

security_icon = ctk.CTkImage(
    Image.open(os.path.join(project_root, "assets", "security_card.png")),
    size=(25, 25),
)

# =====================================
# USER STATS FRAME
# =====================================

stats_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

stats_frame.pack(pady=(5, 5))

# =====================================
# FILES CARD
# =====================================

files_card = ctk.CTkFrame(
    stats_frame,
    width=180,
    height=80,
    corner_radius=22,
    fg_color="#111827",
    border_width=2,
    border_color="#00d4ff",
)

files_card.grid(row=0, column=0, padx=15)

files_card.pack_propagate(False)

files_label = ctk.CTkLabel(
    files_card,
    text=" MY FILES",
    image=files_icon,
    compound="left",
    font=("Segoe UI", 16, "bold"),
    text_color="#00d4ff",
)

files_label.pack(pady=(10, 3))

files_count = ctk.CTkLabel(
    files_card,
    text="0",
    font=("Segoe UI", 25, "bold"),
    text_color="white",
)

files_count.pack()

# =====================================
# ENCRYPTED CARD
# =====================================

encrypted_card = ctk.CTkFrame(
    stats_frame,
    width=180,
    height=80,
    corner_radius=22,
    fg_color="#111827",
    border_width=2,
    border_color="#3ea6ff",
)

encrypted_card.grid(row=0, column=1, padx=15)

encrypted_card.pack_propagate(False)

encrypted_label = ctk.CTkLabel(
    encrypted_card,
    text=" ENCRYPTED",
    image=encrypt_icon,
    compound="left",
    font=("Segoe UI", 16, "bold"),
    text_color="#3ea6ff",
)

encrypted_label.pack(pady=(10, 3))

encrypted_count = ctk.CTkLabel(
    encrypted_card,
    text="0",
    font=("Segoe UI", 25, "bold"),
    text_color="white",
)

encrypted_count.pack()

# =====================================
# SECURITY CARD
# =====================================

security_card = ctk.CTkFrame(
    stats_frame,
    width=180,
    height=80,
    corner_radius=22,
    fg_color="#111827",
    border_width=2,
    border_color="#3ea6ff",
)

security_card.grid(row=0, column=2, padx=15)

security_card.pack_propagate(False)

security_label = ctk.CTkLabel(
    security_card,
    text=" SECURITY",
    image=security_icon,
    compound="left",
    font=("Segoe UI", 16, "bold"),
    text_color="#3ea6ff",
)

security_label.pack(pady=(10, 3))

security_count = ctk.CTkLabel(
    security_card,
    text="100%",
    font=("Segoe UI", 25, "bold"),
    text_color="white",
)

security_count.pack()

# =====================================
# BUTTON ICONS
# =====================================

encrypt_icon = ctk.CTkImage(
    Image.open(os.path.join(project_root, "assets", "encrypt.png")),
    size=(28, 28),
)

decrypt_icon = ctk.CTkImage(
    Image.open(os.path.join(project_root, "assets", "decrypt.png")),
    size=(28, 28),
)

files_icon = ctk.CTkImage(
    Image.open(os.path.join(project_root, "assets", "file.png")),
    size=(28, 28),
)

generator_icon = ctk.CTkImage(
    Image.open(os.path.join(project_root, "assets", "password.png")),
    size=(28, 28),
)

security_icon = ctk.CTkImage(
    Image.open(os.path.join(project_root, "assets", "security.png")),
    size=(28, 28),
)

logout_icon = ctk.CTkImage(
    Image.open(os.path.join(project_root, "assets", "logout2.png")),
    size=(28, 28),
)

# =====================================
# BUTTON FRAME
# =====================================

button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

button_frame.pack(pady=7)

# =====================================
# ROW 1
# =====================================

encrypt_btn = ctk.CTkButton(
    button_frame,
    text=" Encrypt File",
    image=encrypt_icon,
    compound="left",
    width=255,
    height=70,
    corner_radius=22,
    font=("Segoe UI", 17, "bold"),
    fg_color="#18324a",
    hover_color="#2d6fb3",
    border_width=2,
    border_color="#3ea6ff",
    command=encrypt_file,
)

encrypt_btn.grid(row=0, column=0, padx=20, pady=10)

decrypt_btn = ctk.CTkButton(
    button_frame,
    text=" Decrypt File",
    image=decrypt_icon,
    compound="left",
    width=255,
    height=70,
    corner_radius=22,
    font=("Segoe UI", 17, "bold"),
    fg_color="#18324a",
    hover_color="#2d6fb3",
    border_width=2,
    border_color="#3ea6ff",
    command=decrypt_file,
)

decrypt_btn.grid(row=0, column=1, padx=20, pady=10)

# =====================================
# ROW 2
# =====================================

files_btn = ctk.CTkButton(
    button_frame,
    text=" My Files",
    image=files_icon,
    compound="left",
    width=255,
    height=70,
    corner_radius=22,
    font=("Segoe UI", 17, "bold"),
    fg_color="#18324a",
    hover_color="#2d6fb3",
    border_width=2,
    border_color="#3ea6ff",
    command=my_files,
)

files_btn.grid(row=1, column=0, padx=20, pady=10)

generator_btn = ctk.CTkButton(
    button_frame,
    text=" Password Generator",
    image=generator_icon,
    compound="left",
    width=255,
    height=70,
    corner_radius=22,
    font=("Segoe UI", 17, "bold"),
    fg_color="#18324a",
    hover_color="#2d6fb3",
    border_width=2,
    border_color="#3ea6ff",
    command=password_generator,
)

generator_btn.grid(row=1, column=1, padx=20, pady=10)

# =====================================
# ROW 3
# =====================================

security_btn = ctk.CTkButton(
    button_frame,
    text=" Security Tools",
    image=security_icon,
    compound="left",
    width=255,
    height=70,
    corner_radius=22,
    font=("Segoe UI", 17, "bold"),
    fg_color="#18324a",
    hover_color="#2d6fb3",
    border_width=2,
    border_color="#3ea6ff",
    command=security_tools,
)

security_btn.grid(row=2, column=0, padx=20, pady=10)

logout_btn = ctk.CTkButton(
    button_frame,
    text=" Logout",
    image=logout_icon,
    compound="left",
    width=255,
    height=70,
    corner_radius=22,
    font=("Segoe UI", 17, "bold"),
    fg_color="#8b1e1e",
    hover_color="#c62828",
    border_width=2,
    border_color="#ff4d4d",
    command=logout,
)

logout_btn.grid(row=2, column=1, padx=20, pady=10)

# =====================================
# FOOTER
# =====================================

footer_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

footer_frame.pack(side="bottom", fill="x", pady=(0, 15))

footer_label = ctk.CTkLabel(
    footer_frame,
    text="CryptVault User Console v1.0",
    font=("Segoe UI", 13),
    text_color="gray",
)

footer_label.pack()

security_footer = ctk.CTkLabel(
    footer_frame,
    text="🔐 Encrypt • Protect • Secure",
    font=("Segoe UI", 11),
    text_color="#6c6c6c",
)

security_footer.pack()

# =====================================
# KEY BINDINGS
# =====================================

app.bind("<Escape>", lambda event: logout())

# =====================================
# RUN APP
# =====================================

app.mainloop()
