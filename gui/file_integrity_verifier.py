import os
import sys
import hashlib
import subprocess

import customtkinter as ctk

from PIL import Image
from datetime import datetime

from tkinter import filedialog
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

app.title("CryptVault - File Integrity Verifier")

app.geometry("510x615")

app.resizable(False, False)

app.configure(fg_color="#02060A")

# =====================================================
# BACKGROUND IMAGE
# =====================================================

background_path = os.path.join(project_root, "assets", "enc.jpg")

background_image = ctk.CTkImage(
    light_image=Image.open(background_path),
    dark_image=Image.open(background_path),
    size=(510, 615),
)

background_label = ctk.CTkLabel(app, image=background_image, text="")

background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# =====================================================
# MAIN GLASS PANEL
# =====================================================

main_frame = ctk.CTkFrame(
    app,
    width=480,
    height=595,
    corner_radius=28,
    fg_color="#0b1118",
    border_width=2,
    border_color="#3ea6ff",
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

main_frame.pack_propagate(False)

# =====================================================
# VAULT LOGO
# =====================================================

vault_logo = ctk.CTkImage(
    light_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    dark_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    size=(62, 62),
)

logo_label = ctk.CTkLabel(main_frame, image=vault_logo, text="")

logo_label.pack(pady=(8, 4))

# =====================================================
# TITLE
# =====================================================

title_label = ctk.CTkLabel(
    main_frame,
    text="File Integrity Verifier",
    font=("Segoe UI", 24, "bold"),
    text_color="white",
)

title_label.pack()

# =====================================================
# SUBTITLE
# =====================================================

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Generate and Verify SHA-256 Hashes",
    font=("Segoe UI", 12, "bold"),
    text_color="#93b7d7",
)

subtitle_label.pack(pady=(2, 6))

# =====================================================
# TOP SEPARATOR
# =====================================================

top_separator = ctk.CTkFrame(main_frame, height=3, fg_color="#1f6aa5")

top_separator.pack(fill="x", padx=20, pady=(0, 12))

# =====================================================
# GLOBAL VARIABLES
# =====================================================

selected_file = None

selected_hash_file = None

generated_hash = ""
# =====================================================
# FILE CARD
# =====================================================

file_card = ctk.CTkFrame(
    main_frame,
    width=450,
    height=105,
    corner_radius=20,
    fg_color="#111827",
    border_width=2,
    border_color="#244b74",
)

file_card.pack(pady=(0, 10))

file_card.pack_propagate(False)

# ---------------- TOP ROW ----------------

file_top = ctk.CTkFrame(file_card, fg_color="transparent")

file_top.pack(fill="x", padx=18, pady=(14, 8))

file_title = ctk.CTkLabel(
    file_top, text="📄 Selected File", font=("Segoe UI", 15, "bold"), text_color="white"
)

file_title.pack(side="left")

browse_file_btn = ctk.CTkButton(
    file_top,
    text="Browse",
    width=100,
    height=34,
    corner_radius=12,
    font=("Segoe UI", 13, "bold"),
    fg_color="#1f6aa5",
    hover_color="#2d7fd3",
    border_width=2,
    border_color="#58b5ff",
)

browse_file_btn.pack(side="right")

# ---------------- FILE NAME ----------------

selected_file_label = ctk.CTkLabel(
    file_card,
    text="No file selected",
    font=("Segoe UI", 13),
    text_color="#9fbad6",
    anchor="w",
    justify="left",
)

selected_file_label.pack(fill="x", padx=18)

# =====================================================
# SHA CARD
# =====================================================

sha_card = ctk.CTkFrame(
    main_frame,
    width=450,
    height=105,
    corner_radius=20,
    fg_color="#111827",
    border_width=2,
    border_color="#244b74",
)

sha_card.pack(pady=(0, 12))

sha_card.pack_propagate(False)

# ---------------- TOP ROW ----------------

sha_top = ctk.CTkFrame(sha_card, fg_color="transparent")

sha_top.pack(fill="x", padx=18, pady=(14, 8))

sha_title = ctk.CTkLabel(
    sha_top, text="🔑 SHA File", font=("Segoe UI", 15, "bold"), text_color="white"
)

sha_title.pack(side="left")

browse_sha_btn = ctk.CTkButton(
    sha_top,
    text="Browse",
    width=100,
    height=34,
    corner_radius=12,
    font=("Segoe UI", 13, "bold"),
    fg_color="#1f6aa5",
    hover_color="#2d7fd3",
    border_width=2,
    border_color="#58b5ff",
)

browse_sha_btn.pack(side="right")

# ---------------- SHA FILE NAME ----------------

selected_sha_label = ctk.CTkLabel(
    sha_card,
    text="No SHA file selected",
    font=("Segoe UI", 13),
    text_color="#9fbad6",
    anchor="w",
    justify="left",
)

selected_sha_label.pack(fill="x", padx=18)
# =====================================================
# ACTION BUTTONS
# =====================================================

action_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

action_frame.pack(pady=(0, 12))

# =====================================================
# GENERATE HASH BUTTON
# =====================================================

generate_btn = ctk.CTkButton(
    action_frame,
    text="Generate Hash",
    width=210,
    height=52,
    corner_radius=18,
    font=("Segoe UI", 15, "bold"),
    fg_color="#1f6aa5",
    hover_color="#2d7fd3",
    border_width=2,
    border_color="#58b5ff",
)

generate_btn.grid(row=0, column=0, padx=8)

# =====================================================
# VERIFY BUTTON
# =====================================================

verify_btn = ctk.CTkButton(
    action_frame,
    text="Verify Integrity",
    width=210,
    height=52,
    corner_radius=18,
    font=("Segoe UI", 15, "bold"),
    fg_color="#18324a",
    hover_color="#2d6fb3",
    border_width=2,
    border_color="#3ea6ff",
)

verify_btn.grid(row=0, column=1, padx=8)

# =====================================================
# BOTTOM SEPARATOR
# =====================================================

bottom_separator = ctk.CTkFrame(main_frame, height=2, fg_color="#1f6aa5")

bottom_separator.pack(fill="x", padx=20, pady=(14, 12))

# =====================================================
# BOTTOM BUTTONS
# =====================================================

bottom_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

bottom_frame.pack(pady=(0, 10))

# =====================================================
# CLEAR BUTTON
# =====================================================

clear_btn = ctk.CTkButton(
    bottom_frame,
    text="🗑 Clear",
    width=170,
    height=48,
    corner_radius=16,
    font=("Segoe UI", 14, "bold"),
    fg_color="#2b2b2b",
    hover_color="#3a3a3a",
    border_width=2,
    border_color="#555555",
)

clear_btn.grid(row=0, column=0, padx=10)

# =====================================================
# BACK BUTTON
# =====================================================

back_btn = ctk.CTkButton(
    bottom_frame,
    text="⬅ Back",
    width=170,
    height=48,
    corner_radius=16,
    font=("Segoe UI", 14, "bold"),
    fg_color="#202020",
    hover_color="#303030",
    border_width=2,
    border_color="#3ea6ff",
)

back_btn.grid(row=0, column=1, padx=10)

# =====================================================
# FOOTER
# =====================================================

footer_label = ctk.CTkLabel(
    main_frame,
    text="CryptVault • File Integrity Verification Engine",
    font=("Segoe UI", 11),
    text_color="gray",
)

footer_label.pack(side="bottom", pady=(0, 10))


# =====================================================
# BROWSE FILE
# =====================================================


def browse_file():

    global selected_file

    file_path = filedialog.askopenfilename(title="Select File")

    if not file_path:
        return

    selected_file = file_path

    filename = os.path.basename(file_path)

    if len(filename) > 42:
        filename = filename[:39] + "..."

    selected_file_label.configure(text=filename, text_color="white")


# =====================================================
# BROWSE SHA FILE
# =====================================================


def browse_sha_file():

    global selected_hash_file

    file_path = filedialog.askopenfilename(
        title="Select SHA File",
        filetypes=[
            ("SHA Files", "*.sha"),
            ("Text Files", "*.txt"),
            ("All Files", "*.*"),
        ],
    )

    if not file_path:
        return

    selected_hash_file = file_path

    filename = os.path.basename(file_path)

    if len(filename) > 42:
        filename = filename[:39] + "..."

    selected_sha_label.configure(text=filename, text_color="white")


# =====================================================
# CONNECT BUTTONS
# =====================================================

browse_file_btn.configure(command=browse_file)

browse_sha_btn.configure(command=browse_sha_file)


# =====================================================
# GENERATE SHA-256 HASH
# =====================================================


def generate_hash():

    global generated_hash

    if selected_file is None:

        messagebox.showwarning("No File", "Please select a file first.")

        return

    sha256 = hashlib.sha256()

    try:

        with open(selected_file, "rb") as file:

            while True:

                chunk = file.read(4096)

                if not chunk:
                    break

                sha256.update(chunk)

        generated_hash = sha256.hexdigest().upper()

    except Exception as e:

        messagebox.showerror("Error", f"Failed to generate hash.\n\n{e}")

        return

    # =====================================================
    # DEFAULT SHA FILE NAME
    # =====================================================

    default_name = os.path.splitext(os.path.basename(selected_file))[0] + ".sha"

    # =====================================================
    # SAVE LOCATION
    # =====================================================

    save_path = filedialog.asksaveasfilename(
        title="Save SHA File",
        initialfile=default_name,
        defaultextension=".sha",
        filetypes=[("SHA Files", "*.sha")],
    )

    if not save_path:
        return

    # =====================================================
    # FILE INFORMATION
    # =====================================================

    file_name = os.path.basename(selected_file)

    generated_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    # =====================================================
    # SAVE SHA FILE
    # =====================================================

    try:

        with open(save_path, "w", encoding="utf-8") as file:

            file.write(f"""========================================
        CryptVault Integrity File
========================================

File Name :
{file_name}

Algorithm :
SHA-256

Generated :
{generated_time}

Purpose :
File Integrity Verification

SHA-256 Hash :

{generated_hash}

========================================
Generated By :
CryptVault v1.0
========================================
""")

    except Exception as e:

        messagebox.showerror("Error", f"Unable to save SHA file.\n\n{e}")

        return

    # =====================================================
    # SUCCESS
    # =====================================================

    messagebox.showinfo("Success", "SHA-256 hash generated and saved successfully.")


# =====================================================
# CONNECT BUTTON
# =====================================================

generate_btn.configure(command=generate_hash)
# =====================================================
# VERIFY INTEGRITY
# =====================================================


def verify_integrity():

    if selected_file is None:

        messagebox.showwarning("No File", "Please select a file first.")

        return

    if selected_hash_file is None:

        messagebox.showwarning("No SHA File", "Please select a SHA file first.")

        return

    # ==========================================
    # GENERATE CURRENT HASH
    # ==========================================

    sha256 = hashlib.sha256()

    try:

        with open(selected_file, "rb") as file:

            while True:

                chunk = file.read(4096)

                if not chunk:
                    break

                sha256.update(chunk)

        current_hash = sha256.hexdigest()

    except Exception as e:

        messagebox.showerror("Error", str(e))

        return

    # ==========================================
    # READ STORED HASH
    # ==========================================

    try:

        with open(selected_hash_file, "r") as file:

            lines = file.readlines()

    except Exception as e:

        messagebox.showerror("Error", str(e))

        return

    stored_hash = None

    for line in lines:

        line = line.strip()

        if len(line) == 64:

            stored_hash = line.lower()

            break

    if stored_hash is None:

        messagebox.showerror("Invalid SHA File", "Hash could not be found.")

        return

    # ==========================================
    # COMPARE HASHES
    # ==========================================

    if current_hash.lower() == stored_hash:

        messagebox.showinfo(
            "Integrity Verified",
            "✔ File integrity verified.\n\n" "The file has not been modified.",
        )

    else:

        messagebox.showerror(
            "Integrity Failed",
            "✖ Hash mismatch.\n\n" "The file has been modified or corrupted.",
        )


# =====================================================
# CLEAR
# =====================================================


def clear_fields():

    global selected_file
    global selected_hash_file
    global generated_hash

    selected_file = None
    selected_hash_file = None
    generated_hash = ""

    selected_file_label.configure(text="No file selected", text_color="#9fbad6")

    selected_sha_label.configure(text="No SHA file selected", text_color="#9fbad6")


# =====================================================
# BACK
# =====================================================


def back_to_security_tools():

    app.destroy()

    subprocess.Popen(["python", os.path.join("gui", "security_tools.py")])


# =====================================================
# CONNECT BUTTONS
# =====================================================

verify_btn.configure(command=verify_integrity)

clear_btn.configure(command=clear_fields)

back_btn.configure(command=back_to_security_tools)

# =====================================================
# RUN APPLICATION
# =====================================================

app.mainloop()
