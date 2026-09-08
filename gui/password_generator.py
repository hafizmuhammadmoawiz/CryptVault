import os
import sys
import math
import string
import secrets
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

app.title("CryptVault - Password Generator")

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
    size=(72, 72),
)

logo_label = ctk.CTkLabel(main_frame, image=vault_logo, text="")

logo_label.pack(pady=(15, 10))

# =====================================================
# TITLE
# =====================================================

title_label = ctk.CTkLabel(
    main_frame,
    text="Password Generator",
    font=("Segoe UI", 25, "bold"),
    text_color="white",
)

title_label.pack()

# =====================================================
# SUBTITLE
# =====================================================

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Generate strong and secure passwords",
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
# CONTROL CARD
# =====================================================

control_card = ctk.CTkFrame(
    main_frame,
    width=515,
    height=165,
    corner_radius=20,
    fg_color="#111827",
    border_width=2,
    border_color="#244b74",
)

control_card.pack(pady=(0, 8))

control_card.pack_propagate(False)

# =====================================================
# TOP ROW
# =====================================================

top_row = ctk.CTkFrame(control_card, fg_color="transparent")

top_row.pack(fill="x", padx=18, pady=(12, 6))

length_label = ctk.CTkLabel(
    top_row,
    text="Password Length",
    font=("Segoe UI", 14, "bold"),
    text_color="white",
)

length_label.pack(side="left")

generate_btn = ctk.CTkButton(
    top_row,
    text="Generate",
    width=120,
    height=34,
    corner_radius=12,
    font=("Segoe UI", 13, "bold"),
    fg_color="#1f6aa5",
    hover_color="#2d7fd3",
    border_width=2,
    border_color="#58b5ff",
)

generate_btn.pack(side="right")

# =====================================================
# LENGTH SLIDER
# =====================================================

length_slider = ctk.CTkSlider(
    control_card,
    from_=8,
    to=20,
    number_of_steps=56,
    progress_color="#3ea6ff",
    button_color="#ffffff",
    button_hover_color="#d8ecff",
)

length_slider.set(12)

length_slider.pack(fill="x", padx=18, pady=(0, 10))

# =====================================================
# CHECKBOX AREA
# =====================================================

checkbox_frame = ctk.CTkFrame(control_card, fg_color="transparent")

checkbox_frame.pack(fill="x", padx=18)

uppercase_var = ctk.BooleanVar(value=True)
lowercase_var = ctk.BooleanVar(value=True)
numbers_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=True)
exclude_var = ctk.BooleanVar(value=True)
start_letter_var = ctk.BooleanVar(value=False)

uppercase_cb = ctk.CTkCheckBox(
    checkbox_frame,
    text="Uppercase",
    variable=uppercase_var,
    font=("Segoe UI", 13),
)

lowercase_cb = ctk.CTkCheckBox(
    checkbox_frame,
    text="Lowercase",
    variable=lowercase_var,
    font=("Segoe UI", 13),
)

numbers_cb = ctk.CTkCheckBox(
    checkbox_frame,
    text="Numbers",
    variable=numbers_var,
    font=("Segoe UI", 13),
)

symbols_cb = ctk.CTkCheckBox(
    checkbox_frame,
    text="Symbols",
    variable=symbols_var,
    font=("Segoe UI", 13),
)

exclude_cb = ctk.CTkCheckBox(
    checkbox_frame,
    text="Exclude Similar Characters",
    variable=exclude_var,
    font=("Segoe UI", 13),
)

start_letter_cb = ctk.CTkCheckBox(
    checkbox_frame,
    text="Start with Letter",
    variable=start_letter_var,
    font=("Segoe UI", 13),
)

uppercase_cb.grid(row=0, column=0, sticky="w", padx=(0, 30), pady=2)

lowercase_cb.grid(row=0, column=1, sticky="w", padx=(0, 30), pady=2)

numbers_cb.grid(row=0, column=2, sticky="w", pady=2)

symbols_cb.grid(row=1, column=0, sticky="w", padx=(0, 30), pady=2)

exclude_cb.grid(row=1, column=1, sticky="w", padx=(0, 30), pady=2)

start_letter_cb.grid(row=1, column=2, sticky="w", pady=2)


# =====================================================
# RESULT CARD
# =====================================================

result_card = ctk.CTkFrame(
    main_frame,
    width=515,
    height=165,
    corner_radius=20,
    fg_color="#111827",
    border_width=2,
    border_color="#244b74",
)

result_card.pack(pady=(0, 8))

result_card.pack_propagate(False)

# =====================================================
# PASSWORD FIELD
# =====================================================

password_entry = ctk.CTkEntry(
    result_card,
    height=48,
    corner_radius=12,
    font=("Consolas", 14),
    justify="center",
    border_width=2,
    border_color="#3ea6ff",
    fg_color="#1b1b1b",
    text_color="#ffffff",
)

password_entry.pack(fill="x", padx=18, pady=(15, 12))

password_entry.insert(0, "Generated password will appear here...")

password_entry.configure(state="readonly")

# =====================================================
# METRICS
# =====================================================

metric_frame = ctk.CTkFrame(result_card, fg_color="transparent")

metric_frame.pack(fill="x", padx=18)

# LEFT

left_metric = ctk.CTkFrame(metric_frame, fg_color="transparent")

left_metric.pack(side="left", expand=True, anchor="w")

ctk.CTkLabel(
    left_metric,
    text="Strength",
    font=("Segoe UI", 13, "bold"),
    text_color="white",
).pack(anchor="w")

strength_value = ctk.CTkLabel(
    left_metric,
    text="----------",
    font=("Segoe UI", 13),
    text_color="#6bc5ff",
)

strength_value.pack(anchor="w")

# RIGHT

right_metric = ctk.CTkFrame(metric_frame, fg_color="transparent")

right_metric.pack(side="right", expand=True, anchor="e")

ctk.CTkLabel(
    right_metric,
    text="Entropy",
    font=("Segoe UI", 13, "bold"),
    text_color="white",
).pack(anchor="w")

entropy_value = ctk.CTkLabel(
    right_metric,
    text="----------",
    font=("Segoe UI", 13),
    text_color="#6bc5ff",
)

entropy_value.pack(anchor="w")

# =====================================================
# BOTTOM SEPARATOR
# =====================================================

bottom_separator = ctk.CTkFrame(main_frame, height=2, fg_color="#1f6aa5")

bottom_separator.pack(fill="x", padx=18, pady=(0, 8))

# =====================================================
# BUTTONS
# =====================================================

button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

button_frame.pack()

copy_btn = ctk.CTkButton(
    button_frame,
    text="📋 Copy",
    width=170,
    height=44,
    corner_radius=16,
    fg_color="#2f7bbb",
    hover_color="#3e93dc",
    border_width=2,
    border_color="#58b5ff",
    font=("Segoe UI", 14, "bold"),
)

copy_btn.pack(side="left", padx=10)

back_btn = ctk.CTkButton(
    button_frame,
    text="↩ Back",
    width=170,
    height=44,
    corner_radius=16,
    fg_color="#2d2d2d",
    hover_color="#3b3b3b",
    border_width=2,
    border_color="#58b5ff",
    font=("Segoe UI", 14, "bold"),
)

back_btn.pack(side="left", padx=10)

# =====================================================
# FOOTER
# =====================================================

footer_title = ctk.CTkLabel(
    main_frame,
    text="CryptVault Password Generator",
    font=("Segoe UI", 12),
    text_color="#8d8d8d",
)

footer_title.pack(pady=(10, 0))

footer_subtitle = ctk.CTkLabel(
    main_frame,
    text="Generate • Protect • Secure",
    font=("Segoe UI", 11),
    text_color="#6c6c6c",
)

footer_subtitle.pack(pady=(2, 0))
# =====================================================
# GENERATE PASSWORD
# =====================================================


def generate_password():

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = "!@#$%^&*()_-+=<>?/[]{}"

    # ==========================================
    # EXCLUDE SIMILAR CHARACTERS
    # ==========================================

    if exclude_var.get():

        for ch in "O0Il1":

            uppercase = uppercase.replace(ch, "")
            lowercase = lowercase.replace(ch, "")
            numbers = numbers.replace(ch, "")

    # ==========================================
    # BUILD CHARACTER POOL
    # ==========================================

    pool = ""

    if uppercase_var.get():
        pool += uppercase

    if lowercase_var.get():
        pool += lowercase

    if numbers_var.get():
        pool += numbers

    if symbols_var.get():
        pool += symbols

    # ==========================================
    # VALIDATION
    # ==========================================

    if pool == "":

        messagebox.showwarning(
            "Selection Required", "Please select at least one character type."
        )

        return

    length = int(length_slider.get())

    # ==========================================
    # GENERATE PASSWORD
    # ==========================================

    password = ""

    for _ in range(length):

        password += secrets.choice(pool)

    # ==========================================
    # UPDATE PASSWORD FIELD
    # ==========================================

    password_entry.configure(state="normal")

    password_entry.delete(0, "end")

    password_entry.insert(0, password)

    password_entry.configure(state="readonly")

    # ==========================================
    # PASSWORD STRENGTH
    # ==========================================

    pool_size = len(pool)

    entropy = length * math.log2(pool_size)

    if entropy < 40:

        strength = "Weak"
        color = "#ff4d4d"

    elif entropy < 60:

        strength = "Medium"
        color = "#ffb84d"

    elif entropy < 80:

        strength = "Strong"
        color = "#00d27a"

    else:

        strength = "Very Strong"
        color = "#00ff88"

    # ==========================================
    # UPDATE METRICS
    # ==========================================

    strength_value.configure(text=strength, text_color=color)

    entropy_value.configure(text=f"{entropy:.1f} Bits", text_color="#6bc5ff")


# =====================================================
# CONNECT GENERATE BUTTON
# =====================================================

generate_btn.configure(command=generate_password)
# =====================================================
# COPY PASSWORD
# =====================================================


def copy_password():

    password = password_entry.get()

    if password == "" or password == "Generated password will appear here...":

        messagebox.showwarning("No Password", "Please generate a password first.")

        return

    app.clipboard_clear()

    app.clipboard_append(password)

    app.update()

    messagebox.showinfo("Copied", "Password copied to clipboard successfully.")


# =====================================================
# BACK TO DASHBOARD
# =====================================================


def back_to_dashboard():

    app.destroy()

    subprocess.Popen(
        [
            "python",
            os.path.join("gui", "dashboard.py"),
        ]
    )


# =====================================================
# UPDATE SLIDER TITLE
# =====================================================


def update_length(value):

    length_label.configure(text=f"Password Length ({int(float(value))})")


length_slider.configure(command=update_length)

update_length(length_slider.get())


# =====================================================
# CONNECT BUTTONS
# =====================================================

generate_btn.configure(command=generate_password)

copy_btn.configure(command=copy_password)

back_btn.configure(command=back_to_dashboard)


# =====================================================
# RUN APPLICATION
# =====================================================

app.mainloop()
