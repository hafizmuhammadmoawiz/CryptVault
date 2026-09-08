import sys
import os
import subprocess

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

from core.authentication import login_user

# =====================================
# SETTINGS
# =====================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =====================================
# FUNCTIONS
# =====================================


def open_register_page():
    app.destroy()
    subprocess.Popen(["python", "gui/register_page.py"])


def open_forgot_password():

    app.destroy()

    import subprocess

    subprocess.Popen(["python", "gui/forgot_password.py"])


def open_dashboard(role, username):

    with open("current_user.txt", "w") as file:

        file.write(username)

    app.destroy()

    if role == "admin":

        subprocess.Popen(["python", "gui/admin_dashboard.py"])

    else:

        subprocess.Popen(["python", "gui/dashboard.py"])


def handle_login():

    username = username_entry.get().strip()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning("Missing Data", "Please enter username and password.")
        return

    result = login_user(username, password)

    if result["success"]:

        messagebox.showinfo("Success", f"Welcome {username}")

        open_dashboard(result["role"], username)

    else:

        messagebox.showerror("Login Failed", result["message"])


def toggle_password():

    if password_entry.cget("show") == "*":

        password_entry.configure(show="")
        eye_btn.configure(text="🙈")

    else:

        password_entry.configure(show="*")
        eye_btn.configure(text="👁")


# =====================================
# WINDOW
# =====================================

app = ctk.CTk()

app.title("CryptVault - Login")
app.geometry("550x650")
app.resizable(False, False)
app.configure(fg_color="#02060a")

# =====================================
# BACKGROUND IMAGE
# =====================================

bg_path = os.path.join(project_root, "assets", "login.jpg")

bg_image = ctk.CTkImage(
    light_image=Image.open(bg_path), dark_image=Image.open(bg_path), size=(550, 650)
)

bg_label = ctk.CTkLabel(app, image=bg_image, text="")

bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# =====================================
# GLASS CARD
# =====================================

main_frame = ctk.CTkFrame(
    app, width=430, height=625, corner_radius=15, fg_color="#111111", border_width=0
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

main_frame.pack_propagate(False)

# =====================================
# VAULT IMAGE
# =====================================

vault_icon = ctk.CTkImage(
    light_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    dark_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    size=(75, 75),
)

# =====================================
# VAULT ICON
# =====================================

icon_label = ctk.CTkLabel(main_frame, image=vault_icon, text="")

icon_label.pack(pady=(9, 9))

# =====================================
# TITLE
# =====================================

title_label = ctk.CTkLabel(
    main_frame, text="Login to Your CryptVault Account", font=("Segoe UI", 18, "bold")
)

title_label.pack(pady=(0, 10))

# =====================================
# USERNAME
# =====================================

username_label = ctk.CTkLabel(main_frame, text="Username", font=("Segoe UI", 16))

username_label.pack()

username_entry = ctk.CTkEntry(
    main_frame,
    width=350,
    height=50,
    corner_radius=15,
    placeholder_text="Enter username",
)

username_entry.pack(pady=(10, 20))

# =====================================
# PASSWORD
# =====================================

password_label = ctk.CTkLabel(main_frame, text="Password", font=("Segoe UI", 16))

password_label.pack()

password_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

password_frame.pack(pady=(10, 25))

password_entry = ctk.CTkEntry(
    password_frame,
    width=290,
    height=50,
    corner_radius=15,
    show="*",
    placeholder_text="Enter password",
)

password_entry.pack(side="left")

# =====================================
# PASSWORD SECURITY
# =====================================

password_entry.bind("<Control-c>", lambda e: "break")
password_entry.bind("<Control-v>", lambda e: "break")
password_entry.bind("<Control-x>", lambda e: "break")
password_entry.bind("<Control-a>", lambda e: "break")

eye_btn = ctk.CTkButton(
    password_frame,
    text="👁",
    width=50,
    height=50,
    corner_radius=15,
    command=toggle_password,
    fg_color="#1f6aa5",
    hover_color="#144870",
)

eye_btn.pack(side="left", padx=(5, 0))

# =====================================
# LOGIN BUTTON
# =====================================

login_button = ctk.CTkButton(
    main_frame,
    text="Login",
    width=350,
    height=52,
    corner_radius=15,
    font=("Segoe UI", 16, "bold"),
    command=handle_login,
    fg_color="#1f6aa5",
    hover_color="#144870",
)

login_button.pack(pady=(10, 20))

# =====================================
# FORGOT PASSWORD
# =====================================

forgot_button = ctk.CTkButton(
    main_frame,
    text="Forgot Password?",
    fg_color="transparent",
    hover=False,
    text_color="#4da6ff",
    width=150,
    command=open_forgot_password,
)

forgot_button.pack(pady=(0, 5))

# =====================================
# REGISTER SECTION
# =====================================

register_label = ctk.CTkLabel(
    main_frame,
    text="Don't have an account?",
    text_color="lightgray",
    font=("Segoe UI", 14),
)

register_label.pack(pady=(10, 8))

register_button = ctk.CTkButton(
    main_frame,
    text="Register",
    width=350,
    height=52,
    corner_radius=15,
    fg_color="transparent",
    border_width=2,
    border_color="#1f6aa5",
    hover_color="#10253a",
    command=open_register_page,
)

register_button.pack()

# =====================================
# FOOTER
# =====================================

footer_label = ctk.CTkLabel(main_frame, text="CryptVault v1.0", text_color="gray")

footer_label.pack(side="bottom", pady=10)

# =====================================
# ENTER KEY SUPPORT
# =====================================

app.bind("<Return>", lambda event: handle_login())

# =====================================
# RUN APP
# =====================================

app.mainloop()
