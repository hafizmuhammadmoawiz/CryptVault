import os
import sys
import math
import string
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

app.title("CryptVault - Password Attack Simulator")

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
# MAIN GLASS PANEL
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
    main_frame,
    text="Password Attack Simulator",
    font=("Segoe UI", 24, "bold"),
    text_color="white",
)

title_label.pack()


# =====================================================
# SUBTITLE
# =====================================================

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Analyze Password Security Against Common Attack Techniques",
    font=("Segoe UI", 12, "bold"),
    text_color="#93b7d7",
)

subtitle_label.pack(pady=(2, 6))


# =====================================================
# TOP SEPARATOR
# =====================================================

top_separator = ctk.CTkFrame(main_frame, height=2, fg_color="#1f6aa5")

top_separator.pack(fill="x", padx=20, pady=(0, 10))

# =====================================================
# INPUT CARD
# =====================================================

input_card = ctk.CTkFrame(
    main_frame,
    width=500,
    height=150,
    corner_radius=20,
    fg_color="#111827",
    border_width=2,
    border_color="#244b74",
)

input_card.pack(pady=(0, 10))

input_card.pack_propagate(False)

# =====================================================
# PASSWORD LABEL
# =====================================================

password_label = ctk.CTkLabel(
    input_card,
    text="Password",
    font=("Segoe UI", 15, "bold"),
    text_color="white",
)

password_label.pack(anchor="w", padx=20, pady=(10, 4))

# =====================================================
# PASSWORD ROW
# =====================================================

password_row = ctk.CTkFrame(input_card, fg_color="transparent")

password_row.pack()

# =====================================================
# PASSWORD ENTRY
# =====================================================

password_entry = ctk.CTkEntry(
    password_row,
    width=350,
    height=40,
    corner_radius=14,
    border_width=2,
    border_color="#3ea6ff",
    placeholder_text="Enter password to analyze...",
    font=("Segoe UI", 14),
    show="•",
)

password_entry.grid(row=0, column=0, padx=(0, 8))

# =====================================================
# SHOW / HIDE PASSWORD
# =====================================================

password_visible = False


def toggle_password():

    global password_visible

    password_visible = not password_visible

    if password_visible:

        password_entry.configure(show="")

        eye_btn.configure(text="🙈")

    else:

        password_entry.configure(show="•")

        eye_btn.configure(text="👁")


eye_btn = ctk.CTkButton(
    password_row,
    text="👁",
    width=48,
    height=40,
    corner_radius=14,
    fg_color="#18324a",
    hover_color="#2d6fb3",
    command=toggle_password,
)

eye_btn.grid(row=0, column=1)

# =====================================================
# ANALYZE BUTTON
# =====================================================

analyze_btn = ctk.CTkButton(
    input_card,
    text="▶ Analyze Password",
    width=400,
    height=50,
    corner_radius=15,
    font=("Segoe UI", 15, "bold"),
    fg_color="#1f6aa5",
    hover_color="#2d7fd3",
    border_width=2,
    border_color="#58b5ff",
)

analyze_btn.pack(pady=(10, 0))

# =====================================================
# RESULT CARD
# =====================================================

result_card = ctk.CTkFrame(
    main_frame,
    width=500,
    height=240,
    corner_radius=20,
    fg_color="#111827",
    border_width=2,
    border_color="#244b74",
)

result_card.pack(pady=(0, 8))

result_card.pack_propagate(False)

# =====================================================
# RESULT TITLE
# =====================================================

result_title = ctk.CTkLabel(
    result_card,
    text="Security Analysis Report",
    font=("Segoe UI", 16, "bold"),
    text_color="white",
)

result_title.pack(pady=(10, 8))

# =====================================================
# METRICS AREA
# =====================================================

metrics_frame = ctk.CTkFrame(result_card, fg_color="transparent")

metrics_frame.pack(fill="both", expand=True, padx=15)

# =====================================================
# LEFT PANEL
# =====================================================

left_panel = ctk.CTkFrame(metrics_frame, width=220, fg_color="transparent")

left_panel.pack(side="left", fill="both", expand=True)

left_panel.pack_propagate(False)

# =====================================================
# CENTER SEPARATOR
# =====================================================

center_line = ctk.CTkFrame(metrics_frame, width=3, fg_color="#3ea6ff")

center_line.pack(side="left", fill="y", padx=12)


# =====================================================
# RIGHT PANEL
# =====================================================

right_panel = ctk.CTkFrame(metrics_frame, width=220, fg_color="transparent")

right_panel.pack(side="left", fill="both", expand=True)

right_panel.pack_propagate(False)

# =====================================================
# METRIC BUILDER
# =====================================================


def create_metric(parent, title):

    card = ctk.CTkFrame(parent, height=48, fg_color="transparent")

    card.pack(fill="x", pady=2)

    card.pack_propagate(False)

    title_label = ctk.CTkLabel(
        card, text=title, font=("Segoe UI", 13, "bold"), text_color="white"
    )

    title_label.pack(anchor="w")

    value_label = ctk.CTkLabel(
        card, text="----------", font=("Segoe UI", 13), text_color="#6bc5ff"
    )

    value_label.pack(anchor="w", pady=(1, 0))

    return value_label


# =====================================================
# LEFT SIDE
# =====================================================

strength_value = create_metric(left_panel, "Password Strength")

pool_value = create_metric(left_panel, "Character Pool")

bruteforce_value = create_metric(left_panel, "Brute Force Time")

# =====================================================
# RIGHT SIDE
# =====================================================

entropy_value = create_metric(right_panel, "Entropy")

dictionary_value = create_metric(right_panel, "Dictionary Attack")

hybrid_value = create_metric(right_panel, "Hybrid Attack")


# =====================================================
# COMMON PASSWORD DATABASE
# =====================================================

COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "123123",
    "qwerty",
    "abc123",
    "admin",
    "administrator",
    "root",
    "welcome",
    "letmein",
    "dragon",
    "football",
    "pakistan",
    "pakistan123",
    "iloveyou",
}

# =====================================================
# ANALYZE PASSWORD
# =====================================================


def analyze_password():

    password = password_entry.get().strip()

    # ==========================================
    # EMPTY PASSWORD
    # ==========================================

    if password == "":

        messagebox.showwarning("Empty Password", "Please enter a password first.")

        return

    # ==========================================
    # PASSWORD LENGTH
    # ==========================================

    length = len(password)

    # ==========================================
    # CHARACTER TYPES
    # ==========================================

    has_lower = any(c.islower() for c in password)

    has_upper = any(c.isupper() for c in password)

    has_digit = any(c.isdigit() for c in password)

    has_symbol = any(c in string.punctuation for c in password)

    # ==========================================
    # CHARACTER POOL
    # ==========================================

    pool = 0

    if has_lower:
        pool += 26

    if has_upper:
        pool += 26

    if has_digit:
        pool += 10

    if has_symbol:
        pool += len(string.punctuation)

    # ==========================================
    # UPDATE CHARACTER POOL
    # ==========================================

    pool_value.configure(text=f"{pool} Characters", text_color="#6bc5ff")

    # ==========================================
    # DICTIONARY ATTACK CHECK
    # ==========================================

    if password.lower() in COMMON_PASSWORDS:

        dictionary_value.configure(text="Vulnerable", text_color="#ff4d4d")

    else:

        dictionary_value.configure(text="Safe", text_color="#00ff88")

    # ==========================================
    # SEND TO SECURITY ENGINE
    # ==========================================

    calculate_security(
        password=password,
        length=length,
        pool=pool,
        has_lower=has_lower,
        has_upper=has_upper,
        has_digit=has_digit,
        has_symbol=has_symbol,
    )


# =====================================================
# CONNECT ANALYZE BUTTON
# =====================================================

analyze_btn.configure(command=analyze_password)


# =====================================================
# CALCULATE SECURITY
# =====================================================


def calculate_security(
    password,
    length,
    pool,
    has_lower,
    has_upper,
    has_digit,
    has_symbol,
):

    # ==========================================
    # ENTROPY
    # ==========================================

    entropy = round(length * math.log2(pool), 2)

    entropy_value.configure(
        text=f"{entropy} Bits",
        text_color="#6bc5ff",
    )

    # ==========================================
    # PASSWORD STRENGTH SCORE
    # ==========================================

    score = 0

    if length >= 8:
        score += 1

    if length >= 12:
        score += 1

    if has_lower:
        score += 1

    if has_upper:
        score += 1

    if has_digit:
        score += 1

    if has_symbol:
        score += 1

    # ==========================================
    # PASSWORD STRENGTH
    # ==========================================

    if score <= 2:

        strength_value.configure(
            text="Weak",
            text_color="#ff4d4d",
        )

    elif score <= 4:

        strength_value.configure(
            text="Medium",
            text_color="#ffb84d",
        )

    else:

        strength_value.configure(
            text="Strong",
            text_color="#00ff88",
        )

    # ==========================================
    # BRUTE FORCE ESTIMATION
    # ==========================================

    combinations = pool**length

    guesses_per_second = 100_000_000_000

    seconds = combinations / guesses_per_second

    bruteforce_value.configure(
        text=format_time(seconds),
        text_color="#6bc5ff",
    )

    # ==========================================
    # HYBRID ATTACK
    # ==========================================

    hybrid_seconds = seconds / 500

    hybrid_value.configure(
        text=format_time(hybrid_seconds),
        text_color="#6bc5ff",
    )


# =====================================================
# FORMAT TIME
# =====================================================


def format_time(seconds):

    if seconds < 1:
        return "< 1 Second"

    elif seconds < 60:
        return f"{int(seconds)} Seconds"

    elif seconds < 3600:
        return f"{int(seconds/60)} Minutes"

    elif seconds < 86400:
        return f"{int(seconds/3600)} Hours"

    elif seconds < 31536000:
        return f"{int(seconds/86400)} Days"

    elif seconds < 31536000000:
        return f"{int(seconds/31536000)} Years"

    else:
        return "Millions of Years"


# =====================================================
# CLEAR ANALYSIS
# =====================================================


def clear_analysis():

    password_entry.delete(0, "end")

    password_entry.focus()

    strength_value.configure(text="----------", text_color="#6bc5ff")

    entropy_value.configure(text="----------", text_color="#6bc5ff")

    pool_value.configure(text="----------", text_color="#6bc5ff")

    dictionary_value.configure(text="----------", text_color="#6bc5ff")

    bruteforce_value.configure(text="----------", text_color="#6bc5ff")

    hybrid_value.configure(text="----------", text_color="#6bc5ff")


# =====================================================
# BACK
# =====================================================


def back_to_security_tools():

    app.destroy()

    subprocess.Popen(["python", os.path.join("gui", "security_tools.py")])


# =====================================================
# BUTTONS
# =====================================================

button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

button_frame.pack(pady=(10, 10))

# -----------------------------

clear_btn = ctk.CTkButton(
    button_frame,
    text="🗑 Clear",
    width=155,
    height=45,
    corner_radius=15,
    font=("Segoe UI", 14, "bold"),
    fg_color="#2b2b2b",
    hover_color="#3a3a3a",
    border_width=2,
    border_color="#555555",
    command=clear_analysis,
)

clear_btn.grid(row=0, column=0, padx=8)

# -----------------------------

back_btn = ctk.CTkButton(
    button_frame,
    text="⬅ Back",
    width=155,
    height=45,
    corner_radius=15,
    font=("Segoe UI", 14, "bold"),
    fg_color="#18324a",
    hover_color="#2d6fb3",
    border_width=2,
    border_color="#3ea6ff",
    command=back_to_security_tools,
)

back_btn.grid(row=0, column=1, padx=8)

# =====================================================
# FOOTER
# =====================================================

footer = ctk.CTkLabel(
    main_frame,
    text="CryptVault • Password Security Analysis Engine",
    font=("Segoe UI", 10),
    text_color="gray",
)

footer.pack(side="bottom", pady=(0, 11))

# =====================================================
# RUN APPLICATION
# =====================================================

app.mainloop()
