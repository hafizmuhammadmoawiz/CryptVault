import sys
import os
import sqlite3

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


def manage_users():
    messagebox.showinfo("Coming Soon", "User Management Module Coming Soon.")


def view_logs():
    messagebox.showinfo("Coming Soon", "Activity Logs Module Coming Soon.")


def security_events():
    messagebox.showinfo("Coming Soon", "Security Events Monitor Coming Soon.")


def statistics():
    messagebox.showinfo("Coming Soon", "Statistics Dashboard Coming Soon.")


def manage_files():
    messagebox.showinfo("Coming Soon", "Vault File Management Coming Soon.")


def logout():
    app.destroy()


# =====================================
# MAIN WINDOW
# =====================================

app = ctk.CTk()

app.title("CryptVault - Admin Dashboard")

app.geometry("970x670")

app.resizable(False, False)

app.configure(fg_color="#02060a")

# =====================================
# BACKGROUND IMAGE
# =====================================

bg_path = os.path.join(project_root, "assets", "admin.jpg")

bg_image = ctk.CTkImage(
    light_image=Image.open(bg_path), dark_image=Image.open(bg_path), size=(1000, 700)
)

bg_label = ctk.CTkLabel(app, image=bg_image, text="")

bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# =====================================
# MAIN GLASS PANEL
# =====================================

main_frame = ctk.CTkFrame(
    app,
    width=920,
    height=660,
    corner_radius=25,
    fg_color="#111111",
    border_width=1,
    border_color="#1f6aa5",
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

main_frame.pack_propagate(False)

# =====================================
# HEADER
# =====================================

title_label = ctk.CTkLabel(
    main_frame, text="🛡 CryptVault", font=("Segoe UI", 34, "bold")
)

title_label.pack(pady=(15, 5))

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Administrator Control Center",
    font=("Segoe UI", 15),
    text_color="lightgray",
)

subtitle_label.pack()

# =====================================
# WELCOME BANNER
# =====================================

welcome_frame = ctk.CTkFrame(
    main_frame, width=850, height=80, corner_radius=20, fg_color="#16324f"
)

welcome_frame.pack(pady=(15, 10), padx=25, fill="x")

welcome_label = ctk.CTkLabel(
    welcome_frame,
    text="👋 Welcome Admin | Monitor Users, Files & Security Events",
    font=("Segoe UI", 18, "bold"),
)

welcome_label.place(relx=0.5, rely=0.5, anchor="center")

# =====================================
# DATABASE COUNTS
# =====================================


def get_total_users():

    conn = sqlite3.connect("database/database.db")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")

    total_users = cursor.fetchone()[0]

    conn.close()

    return total_users


total_users = get_total_users()

# =====================================
# STATS FRAME
# =====================================

stats_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

stats_frame.pack(pady=(7, 15))

# =====================================
# USERS CARD
# =====================================

users_card = ctk.CTkFrame(stats_frame, width=160, height=100, corner_radius=20)

users_card.grid(row=0, column=0, padx=12, pady=10)

users_card.pack_propagate(False)

users_label = ctk.CTkLabel(users_card, text="👥 USERS", font=("Segoe UI", 18, "bold"))

users_label.pack(pady=(15, 3))

users_count = ctk.CTkLabel(
    users_card, text=str(total_users), font=("Segoe UI", 30, "bold")
)

users_count.pack()

# =====================================
# FILES CARD
# =====================================

files_card = ctk.CTkFrame(stats_frame, width=160, height=100, corner_radius=20)

files_card.grid(row=0, column=1, padx=12, pady=10)

files_card.pack_propagate(False)

files_label = ctk.CTkLabel(files_card, text="📁 FILES", font=("Segoe UI", 18, "bold"))

files_label.pack(pady=(15, 3))

files_count = ctk.CTkLabel(files_card, text="0", font=("Segoe UI", 30, "bold"))

files_count.pack()

# =====================================
# LOGS CARD
# =====================================

logs_card = ctk.CTkFrame(stats_frame, width=160, height=100, corner_radius=20)

logs_card.grid(row=0, column=2, padx=12, pady=10)

logs_card.pack_propagate(False)

logs_label = ctk.CTkLabel(logs_card, text="📋 LOGS", font=("Segoe UI", 18, "bold"))

logs_label.pack(pady=(15, 3))

logs_count = ctk.CTkLabel(logs_card, text="0", font=("Segoe UI", 30, "bold"))

logs_count.pack()

# =====================================
# EVENTS CARD
# =====================================

events_card = ctk.CTkFrame(stats_frame, width=160, height=100, corner_radius=20)

events_card.grid(row=0, column=3, padx=12, pady=10)

events_card.pack_propagate(False)

events_label = ctk.CTkLabel(
    events_card, text="🚨 EVENTS", font=("Segoe UI", 18, "bold")
)

events_label.pack(pady=(15, 3))

events_count = ctk.CTkLabel(events_card, text="0", font=("Segoe UI", 30, "bold"))

events_count.pack()

# =====================================
# ADMIN ACTIONS FRAME
# =====================================

actions_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

actions_frame.pack(pady=10)

# =====================================
# ROW 1
# =====================================

users_btn = ctk.CTkButton(
    actions_frame,
    text="👥 Manage Users",
    width=300,
    height=60,
    corner_radius=18,
    font=("Segoe UI", 16, "bold"),
    fg_color="#1f6aa5",
    hover_color="#144870",
    command=manage_users,
)

users_btn.grid(row=0, column=0, padx=10, pady=9)

files_btn = ctk.CTkButton(
    actions_frame,
    text="📁 Manage Files",
    width=300,
    height=60,
    corner_radius=18,
    font=("Segoe UI", 16, "bold"),
    fg_color="#1f6aa5",
    hover_color="#144870",
    command=manage_files,
)

files_btn.grid(row=0, column=1, padx=10, pady=9)

# =====================================
# ROW 2
# =====================================

logs_btn = ctk.CTkButton(
    actions_frame,
    text="📋 View Logs",
    width=300,
    height=60,
    corner_radius=18,
    font=("Segoe UI", 16, "bold"),
    fg_color="#1f6aa5",
    hover_color="#144870",
    command=view_logs,
)

logs_btn.grid(row=1, column=0, padx=10, pady=9)

events_btn = ctk.CTkButton(
    actions_frame,
    text="🚨 Security Events",
    width=300,
    height=60,
    corner_radius=18,
    font=("Segoe UI", 16, "bold"),
    fg_color="#1f6aa5",
    hover_color="#144870",
    command=security_events,
)

events_btn.grid(row=1, column=1, padx=10, pady=9)

# =====================================
# ROW 3
# =====================================

stats_btn = ctk.CTkButton(
    actions_frame,
    text="📊 Statistics",
    width=300,
    height=60,
    corner_radius=18,
    font=("Segoe UI", 16, "bold"),
    fg_color="#1f6aa5",
    hover_color="#144870",
    command=statistics,
)

stats_btn.grid(row=2, column=0, padx=10, pady=9)

logout_btn = ctk.CTkButton(
    actions_frame,
    text="🚪 Logout",
    width=300,
    height=60,
    corner_radius=18,
    font=("Segoe UI", 16, "bold"),
    fg_color="#b22222",
    hover_color="#7a1414",
    command=logout,
)

logout_btn.grid(row=2, column=1, padx=10, pady=9)


# =====================================
# FOOTER
# =====================================

footer_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

footer_frame.pack(side="bottom", fill="x", pady=(0, 12))

footer_label = ctk.CTkLabel(
    footer_frame,
    text="CryptVault Admin Console v2.0",
    font=("Segoe UI", 13),
    text_color="gray",
)

footer_label.pack()

copyright_label = ctk.CTkLabel(
    footer_frame,
    text="🔐 Cyber Security Administration Panel",
    font=("Segoe UI", 11),
    text_color="#6c6c6c",
)

copyright_label.pack()

# =====================================
# KEY BINDINGS
# =====================================

app.bind("<Escape>", lambda event: logout())

# =====================================
# RUN APP
# =====================================

app.mainloop()
