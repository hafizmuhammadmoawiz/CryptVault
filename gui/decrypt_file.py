# =====================================
# IMPORTS
# =====================================

import customtkinter as ctk

from PIL import Image
import os
import sys
from tkinter import filedialog
import subprocess

from tkinter import messagebox
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

# =====================================
# FIX IMPORT PATH
# =====================================

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(project_root)


# =====================================
# APP SETTINGS
# =====================================

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

# =====================================
# MAIN WINDOW
# =====================================

app = ctk.CTk()

app.title("CryptVault - Decrypt File")

app.geometry("570x670")

app.resizable(False, False)

app.configure(fg_color="#02060a")

# =====================================
# BACKGROUND IMAGE
# =====================================

bg_path = os.path.join(project_root, "assets", "enc.jpg")

bg_image = ctk.CTkImage(
    light_image=Image.open(bg_path), dark_image=Image.open(bg_path), size=(570, 670)
)

bg_label = ctk.CTkLabel(app, image=bg_image, text="")

bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# =====================================
# MAIN GLASS PANEL
# =====================================

main_frame = ctk.CTkFrame(
    app,
    width=530,
    height=640,
    corner_radius=28,
    fg_color="#0b1118",
    border_width=2,
    border_color="#3ea6ff",
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

main_frame.pack_propagate(False)

# =====================================
# VAULT LOGO
# =====================================

vault_logo = ctk.CTkImage(
    light_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    dark_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    size=(60, 60),
)

logo_label = ctk.CTkLabel(main_frame, image=vault_logo, text="")

logo_label.pack(pady=(7, 7))

# =====================================
# TITLE
# =====================================

title_label = ctk.CTkLabel(
    main_frame, text="Decrypt Your File", font=("Segoe UI", 25, "bold")
)

title_label.pack()

# =====================================
# SUBTITLE
# =====================================

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Restore your files using the correct encryption key",
    font=("Segoe UI", 15),
    text_color="#9fbad6",
)

subtitle_label.pack(pady=(5, 5))

# =====================================
# SEPARATOR
# =====================================

separator = ctk.CTkFrame(main_frame, height=2, fg_color="#1f6aa5")

separator.pack(fill="x", padx=35, pady=(2, 2))


# =====================================
# FILE VARIABLE
# =====================================

selected_file = None
selected_key_file = None
# =====================================
# BROWSE FILE
# =====================================


def browse_file():

    global selected_file

    file_path = filedialog.askopenfilename(title="Select File To Decncrypt")
    if not file_path:
        return

    if not file_path.lower().endswith(".enc"):

        messagebox.showerror("Invalid File", "Please select a valid .enc file.")

        return

    selected_file = file_path

    file_name = os.path.basename(file_path)

    if len(file_name) > 30:
        file_name = file_name[:27] + "..."

    file_name_label.configure(text=file_name)

    file_status_label.configure(text="File Ready For Encryption", text_color="#00ff88")


def browse_key_file():

    global selected_key_file

    key_path = filedialog.askopenfilename(
        title="Select Encryption Key", filetypes=[("Key Files", "*.key")]
    )

    if not key_path:
        return

    selected_key_file = key_path

    key_name = os.path.basename(key_path)

    if len(key_name) > 30:
        key_name = key_name[:27] + "..."

    key_name_label.configure(text=key_name)

    key_status_label.configure(text="Key File Ready", text_color="#00ff88")


# =====================================

# FILE ROW

# =====================================

file_row = ctk.CTkFrame(main_frame, fg_color="transparent")

file_row.pack(pady=(8, 8))

# =====================================

# FILE CARD

# =====================================

file_card = ctk.CTkFrame(
    file_row,
    width=340,
    height=70,
    corner_radius=22,
    fg_color="#111827",
    border_width=2,
    border_color="#3ea6ff",
)

file_card.grid(row=0, column=0, padx=(0, 12))

file_card.pack_propagate(False)

# =====================================

# FILE NAME

# =====================================

file_name_label = ctk.CTkLabel(
    file_card,
    text="No File Selected",
    font=("Segoe UI", 16, "bold"),
    text_color="white",
    wraplength=280,
    justify="center",
)

file_name_label.place(relx=0.5, rely=0.31, anchor="center")

# =====================================
# FILE STATUS
# =====================================

file_status_label = ctk.CTkLabel(
    file_card,
    text="Choose a file to continue",
    font=("Segoe UI", 11),
    text_color="gray",
)

file_status_label.place(relx=0.5, rely=0.68, anchor="center")

# =====================================
# BROWSE BUTTON
# =====================================

browse_btn = ctk.CTkButton(
    file_row,
    text="📂 Browse",
    width=140,
    height=70,
    corner_radius=22,
    font=("Segoe UI", 19, "bold"),
    fg_color="#18324a",
    hover_color="#2d6fb3",
    border_width=2,
    border_color="#3ea6ff",
    command=browse_file,
)

browse_btn.grid(row=0, column=1)

# =====================================
# KEY FILE ROW
# =====================================

key_row = ctk.CTkFrame(main_frame, fg_color="transparent")

key_row.pack(pady=(0, 8))

# =====================================
# KEY FILE CARD
# =====================================

key_card = ctk.CTkFrame(
    key_row,
    width=340,
    height=70,
    corner_radius=22,
    fg_color="#111827",
    border_width=2,
    border_color="#3ea6ff",
)

key_card.grid(row=0, column=0, padx=(0, 12))

key_card.pack_propagate(False)

# =====================================
# KEY FILE NAME
# =====================================

key_name_label = ctk.CTkLabel(
    key_card,
    text="No Key Selected",
    font=("Segoe UI", 16, "bold"),
    text_color="white",
    wraplength=280,
    justify="center",
)

key_name_label.place(relx=0.5, rely=0.31, anchor="center")

# =====================================
# KEY FILE STATUS
# =====================================

key_status_label = ctk.CTkLabel(
    key_card,
    text="Choose a .key file",
    font=("Segoe UI", 11),
    text_color="gray",
)

key_status_label.place(relx=0.5, rely=0.68, anchor="center")

# =====================================
# KEY BROWSE BUTTON
# =====================================

key_browse_btn = ctk.CTkButton(
    key_row,
    text="🔑 Browse",
    width=140,
    height=70,
    corner_radius=22,
    font=("Segoe UI", 19, "bold"),
    fg_color="#18324a",
    hover_color="#2d6fb3",
    border_width=2,
    border_color="#3ea6ff",
    command=browse_key_file,
)

key_browse_btn.grid(row=0, column=1)

# =====================================
# ENCRYPTION INFO TITLE
# =====================================

info_title = ctk.CTkLabel(
    main_frame,
    text="Decryption Information",
    font=("Segoe UI", 16, "bold"),
    text_color="#3ea6ff",
)

info_title.pack(pady=(3, 3))

# =====================================
# INFO CARD
# =====================================

info_card = ctk.CTkFrame(
    main_frame,
    width=390,
    height=75,
    corner_radius=24,
    fg_color="#111827",
    border_width=2,
    border_color="#3ea6ff",
)

info_card.pack()

info_card.pack_propagate(False)

# =====================================

# BACK TO DASHBOARD

# =====================================


def back_to_dashboard():
    app.destroy()

    subprocess.Popen(["python", "gui/dashboard.py"])


# =====================================

# ACTION BUTTONS

# =====================================

button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

button_frame.pack(pady=(15, 10))


def decrypt_selected_file():

    global selected_file
    global selected_key_file

    if not selected_file:

        messagebox.showwarning("No Encrypted File", "Please select a .enc file first.")

        return

    if not selected_key_file:

        messagebox.showwarning("No Key File", "Please select a .key file first.")

        return

    try:

        # =====================================
        # LOAD KEY FILE
        # =====================================

        with open(selected_key_file, "rb") as key_file:

            key = key_file.read()

        # =====================================
        # CREATE FERNET CIPHER
        # =====================================

        cipher = Fernet(key)

        # =====================================
        # READ ENCRYPTED FILE
        # =====================================

        with open(selected_file, "rb") as encrypted_file:

            encrypted_data = encrypted_file.read()

        # =====================================
        # DECRYPT DATA
        # =====================================

        decrypted_data = cipher.decrypt(encrypted_data)

        # =====================================
        # EXTRACT ORIGINAL FILE NAME
        # =====================================

        filename_bytes, file_data = decrypted_data.split(b"||CRYPTVAULT||", 1)

        original_name = filename_bytes.decode()

        # =====================================
        # ASK SAVE LOCATION
        # =====================================

        output_file_path = filedialog.asksaveasfilename(
            title="Save Decrypted File",
            initialfile=original_name,
            defaultextension=os.path.splitext(original_name)[1],
            filetypes=[("All Files", "*.*")],
        )

        if not output_file_path:

            return

        # =====================================
        # SAVE DECRYPTED FILE
        # =====================================

        with open(output_file_path, "wb") as output_file:

            output_file.write(file_data)

        # =====================================
        # SUCCESS MESSAGE
        # =====================================

        success_label.configure(
            text=(
                f"✅ {original_name} decrypted successfully\n"
                f"📁 Location: {os.path.basename(os.path.dirname(output_file_path))}"
            ),
            justify="center",
        )

        app.after(5000, lambda: success_label.configure(text=""))

        # =====================================
        # RESET ENC CARD
        # =====================================

        file_name_label.configure(text="No Encrypted File")

        file_status_label.configure(text="Choose a .enc file", text_color="gray")

        # =====================================
        # RESET KEY CARD
        # =====================================

        key_name_label.configure(text="No Key Selected")

        key_status_label.configure(text="Choose a .key file", text_color="gray")

        selected_file = None
        selected_key_file = None

    except InvalidToken:

        messagebox.showerror(
            "Invalid Key", "The selected key does not match this encrypted file."
        )

    except ValueError:

        messagebox.showerror(
            "Invalid File",
            "This file was not encrypted using the latest CryptVault format.",
        )

    except Exception as error:

        messagebox.showerror("Decryption Error", str(error))


# =====================================
# DECRYPT BUTTON
# =====================================

decrypt_btn = ctk.CTkButton(
    button_frame,
    text="🔓 Decrypt File",
    width=220,
    height=58,
    corner_radius=22,
    font=("Segoe UI", 17, "bold"),
    fg_color="#1f6aa5",
    hover_color="#2d7fd3",
    border_width=2,
    border_color="#58b5ff",
    command=decrypt_selected_file,
)

decrypt_btn.grid(row=0, column=0, padx=10)

# =====================================

# BACK BUTTON

# =====================================

back_btn = ctk.CTkButton(
    button_frame,
    text="⬅ Back",
    width=150,
    height=58,
    corner_radius=22,
    font=("Segoe UI", 16, "bold"),
    fg_color="#202020",
    hover_color="#303030",
    border_width=2,
    border_color="#3ea6ff",
    command=back_to_dashboard,
)

back_btn.grid(row=0, column=1, padx=10)


# =====================================
# INFO TEXT
# =====================================

info_label = ctk.CTkLabel(
    info_card,
    text=(
        "• AES-256 Decryption                 • Key Verification\n\n"
        "• Restore Original File                • Invalid Keys Rejected"
    ),
    justify="left",
    font=("Segoe UI", 15),
    text_color="white",
)

info_label.place(relx=0.05, rely=0.5, anchor="w")

# =====================================
# SECURITY NOTICE
# =====================================

notice_label = ctk.CTkLabel(
    main_frame,
    text="⚠ CryptVault does not store your encryption keys.",
    font=("Segoe UI", 15),
    text_color="#ffcc00",
)

notice_label.pack(pady=(7, 7))

# =====================================
# SUCCESS LABEL
# =====================================

success_label = ctk.CTkLabel(
    main_frame,
    text="",
    font=("Segoe UI", 13, "bold"),
    text_color="#00ff88",
)

success_label.pack(pady=(5, 5))


# =====================================

# FOOTER

# =====================================

footer_label = ctk.CTkLabel(
    main_frame,
    text="CryptVault Secure Encryption Engine",
    font=("Segoe UI", 12),
    text_color="gray",
)

footer_label.pack(side="bottom", pady=15)


# =====================================
# RUN APP
# =====================================

app.mainloop()
