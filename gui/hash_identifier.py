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

app.title("CryptVault - Hash Identifier")

app.geometry("550x685")

app.resizable(False, False)

app.configure(fg_color="#02060A")

# =====================================================
# BACKGROUND
# =====================================================

background_path = os.path.join(project_root, "assets", "enc.jpg")

background_image = ctk.CTkImage(
    light_image=Image.open(background_path),
    dark_image=Image.open(background_path),
    size=(550, 685),
)

background_label = ctk.CTkLabel(app, image=background_image, text="")

background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# =====================================================
# MAIN PANEL
# =====================================================

main_frame = ctk.CTkFrame(
    app,
    width=520,
    height=675,
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
    size=(55, 55),
)

logo_label = ctk.CTkLabel(main_frame, image=vault_logo, text="")

logo_label.pack(pady=(4, 4))

# =====================================================
# TITLE
# =====================================================

title_label = ctk.CTkLabel(
    main_frame,
    text="Hash Identifier",
    font=("Segoe UI", 23, "bold"),
    text_color="white",
)

title_label.pack()

# =====================================================
# SUBTITLE
# =====================================================

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Identify cryptographic hash algorithms",
    font=("Segoe UI", 12),
    text_color="#93b7d7",
)

subtitle_label.pack(pady=(2, 4))

# =====================================================
# SEPARATOR
# =====================================================

top_separator = ctk.CTkFrame(main_frame, height=3, fg_color="#1f6aa5")

top_separator.pack(fill="x", padx=20, pady=(0, 7))

# =====================================================
# HASH INPUT CARD
# =====================================================

input_card = ctk.CTkFrame(
    main_frame,
    width=500,
    height=110,
    corner_radius=20,
    fg_color="#111827",
    border_width=2,
    border_color="#244b74",
)

input_card.pack(pady=(0, 9))

input_card.pack_propagate(False)

# =====================================================
# INPUT TITLE
# =====================================================

input_title = ctk.CTkLabel(
    input_card, text="Hash Input", font=("Segoe UI", 15, "bold"), text_color="white"
)

input_title.pack(anchor="w", padx=18, pady=(12, 6))

# =====================================================
# HASH TEXTBOX
# =====================================================

hash_textbox = ctk.CTkTextbox(
    input_card,
    width=455,
    height=70,
    corner_radius=12,
    border_width=2,
    border_color="#3ea6ff",
    fg_color="#1a1a1a",
    text_color="white",
    font=("Consolas", 13),
)

hash_textbox.pack(padx=18, pady=(0, 8))

hash_textbox.insert("1.0", "Paste hash here...")

# =====================================================
# PLACEHOLDER HANDLING
# =====================================================

placeholder_active = True


def clear_placeholder(event):

    global placeholder_active

    if placeholder_active:

        hash_textbox.delete("1.0", "end")

        placeholder_active = False


def restore_placeholder(event):

    global placeholder_active

    content = hash_textbox.get("1.0", "end").strip()

    if content == "":

        hash_textbox.insert("1.0", "Paste hash here...")

        placeholder_active = True


hash_textbox.bind("<FocusIn>", clear_placeholder)

hash_textbox.bind("<FocusOut>", restore_placeholder)

# =====================================================
# RESULT CARD
# =====================================================

result_card = ctk.CTkFrame(
    main_frame,
    width=500,
    height=285,
    corner_radius=20,
    fg_color="#111827",
    border_width=2,
    border_color="#244b74",
)

result_card.pack(pady=(0, 5))

result_card.pack_propagate(False)

# =====================================================
# RESULT TITLE
# =====================================================

result_title = ctk.CTkLabel(
    result_card,
    text="Hash Analysis Report",
    font=("Segoe UI", 16, "bold"),
    text_color="white",
)

result_title.pack(pady=(5, 4))
# =====================================================
# METRICS AREA
# =====================================================

metrics_frame = ctk.CTkFrame(result_card, fg_color="transparent")

metrics_frame.pack(fill="both", expand=True, padx=18, pady=(3, 3))

# =====================================================
# METRICS LAYOUT
# =====================================================

content_frame = ctk.CTkFrame(metrics_frame, fg_color="transparent")

content_frame.pack(fill="both", expand=True, padx=10, pady=5)

# ================= LEFT COLUMN =================

left_column = ctk.CTkFrame(content_frame, fg_color="transparent")

left_column.pack(side="left", fill="both", expand=True)

# ================= CENTER LINE =================

center_line = ctk.CTkFrame(content_frame, width=2, height=200, fg_color="#3ea6ff")

center_line.pack(side="left", padx=18, pady=2)

# ================= RIGHT COLUMN =================

right_column = ctk.CTkFrame(content_frame, fg_color="transparent")

right_column.pack(side="left", fill="both", expand=True)


# =====================================================
# HELPER
# =====================================================


def create_item(parent, title):

    ctk.CTkLabel(
        parent,
        text=title,
        font=("Segoe UI", 13, "bold"),
        text_color="white",
    ).pack(anchor="w")

    value = ctk.CTkLabel(
        parent,
        text="----------",
        font=("Segoe UI", 13),
        text_color="#6bc5ff",
    )

    value.pack(anchor="w", pady=(4, 14))

    return value


# ================= LEFT =================

algorithm_value = create_item(left_column, "Algorithm")

security_value = create_item(left_column, "Security")

primary_use_value = create_item(left_column, "Primary Use")

# ================= RIGHT =================

length_value = create_item(right_column, "Hash Length")

status_value = create_item(right_column, "Status")

risk_value = create_item(
    right_column, "Risk Level"
)  # =====================================================
# ACTION BUTTONS
# =====================================================

action_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

action_frame.pack(pady=(0, 6))

identify_btn = ctk.CTkButton(
    action_frame,
    text="Identify",
    width=170,
    height=40,
    corner_radius=16,
    font=("Segoe UI", 14, "bold"),
    fg_color="#1f6aa5",
    hover_color="#2d7fd3",
    border_width=2,
    border_color="#58b5ff",
)

identify_btn.grid(row=0, column=0, padx=8)

clear_btn = ctk.CTkButton(
    action_frame,
    text="Clear",
    width=170,
    height=40,
    corner_radius=16,
    font=("Segoe UI", 14, "bold"),
    fg_color="#2b2b2b",
    hover_color="#3a3a3a",
    border_width=2,
    border_color="#555555",
)

clear_btn.grid(row=0, column=1, padx=8)

# =====================================================
# BACK BUTTON
# =====================================================

back_btn = ctk.CTkButton(
    main_frame,
    text="⬅ Back",
    width=170,
    height=40,
    corner_radius=16,
    font=("Segoe UI", 14, "bold"),
    fg_color="#202020",
    hover_color="#303030",
    border_width=2,
    border_color="#3ea6ff",
)

back_btn.pack(pady=(0, 10))

# =====================================================
# FOOTER
# =====================================================

footer_label = ctk.CTkLabel(
    main_frame,
    text="CryptVault Hash Analysis Engine",
    font=("Segoe UI", 11),
    text_color="gray",
)

footer_label.pack(side="bottom", pady=(0, 14))

# =====================================================
# IDENTIFY HASH
# =====================================================


def identify_hash():

    hash_value = hash_textbox.get("1.0", "end").strip()

    # Remove Placeholder

    if hash_value == "Paste hash here...":

        hash_value = ""

    # Empty Check

    if hash_value == "":

        messagebox.showwarning("Empty Input", "Please paste a hash first.")

        return

    # Remove Spaces

    hash_value = hash_value.replace(" ", "")

    # Convert Lowercase

    hash_value = hash_value.lower()

    # Validate Hex

    try:

        int(hash_value, 16)

    except ValueError:

        messagebox.showerror(
            "Invalid Hash", "Hash contains invalid hexadecimal characters."
        )

        return

    # =====================================================
    # HASH DETECTION
    # =====================================================

    length = len(hash_value)

    if length == 32:

        algorithm = "MD5"
        security = "Weak"
        status = "Deprecated"
        primary_use = "Legacy Systems"
        risk = "High"
        color = "#ff4d4d"

    elif length == 40:

        algorithm = "SHA-1"
        security = "Weak"
        status = "Deprecated"
        primary_use = "Legacy Systems"
        risk = "High"
        color = "#ff884d"

    elif length == 56:

        algorithm = "SHA-224"
        security = "Good"
        status = "Acceptable"
        primary_use = "Data Integrity"
        risk = "Medium"
        color = "#ffd24d"

    elif length == 64:

        algorithm = "SHA-256"
        security = "Strong"
        status = "Recommended"
        primary_use = "Integrity Verification"
        risk = "Low"
        color = "#00ff88"

    elif length == 96:

        algorithm = "SHA-384"
        security = "Strong"
        status = "Recommended"
        primary_use = "Digital Signatures"
        risk = "Low"
        color = "#00ff88"

    elif length == 128:

        algorithm = "SHA-512"
        security = "Very Strong"
        status = "Recommended"
        primary_use = "High Security Systems"
        risk = "Very Low"
        color = "#00ff88"

    else:

        algorithm = "Unknown"
        security = "Unknown"
        status = "Unsupported"
        primary_use = "Unknown"
        risk = "Unknown"
        color = "#ff4d4d"

    # =====================================================
    # UPDATE UI
    # =====================================================

    algorithm_value.configure(text=algorithm, text_color=color)

    length_value.configure(text=f"{length} Characters", text_color="#6bc5ff")

    security_value.configure(text=security, text_color=color)

    status_value.configure(text=status, text_color=color)

    primary_use_value.configure(text=primary_use, text_color="#6bc5ff")

    risk_value.configure(text=risk, text_color=color)


# =====================================================
# CONNECT IDENTIFY BUTTON
# =====================================================

identify_btn.configure(command=identify_hash)

# =====================================================
# CLEAR HASH
# =====================================================


def clear_fields():

    global placeholder_active

    hash_textbox.delete("1.0", "end")

    hash_textbox.insert("1.0", "Paste hash here...")

    placeholder_active = True

    algorithm_value.configure(text="----------", text_color="#6bc5ff")

    length_value.configure(text="----------", text_color="#6bc5ff")

    security_value.configure(text="----------", text_color="#6bc5ff")

    status_value.configure(text="----------", text_color="#6bc5ff")
    primary_use_value.configure(text="----------", text_color="#6bc5ff")

    risk_value.configure(text="----------", text_color="#6bc5ff")


# =====================================================
# BACK
# =====================================================


def back_to_security_tools():

    app.destroy()

    subprocess.Popen(["python", os.path.join("gui", "security_tools.py")])


# =====================================================
# CONNECT BUTTONS
# =====================================================

identify_btn.configure(command=identify_hash)

clear_btn.configure(command=clear_fields)

back_btn.configure(command=back_to_security_tools)


# =====================================================
# RUN APPLICATION
# =====================================================

app.mainloop()
