import sys
import os
import json
import subprocess
import re

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

from core.authentication import register_user, email_exists, username_exists
from core.otp_manager import generate_otp, send_otp_email

# =====================================
# OTP TEMP STORAGE
# =====================================

generated_otp = None

pending_user = {}

# =====================================
# SETTINGS
# =====================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =====================================
# NAVIGATION
# =====================================


def open_login_page():

    app.destroy()
    subprocess.Popen(["python", "gui/login_page.py"])


# =====================================
# LIVE PASSWORD VALIDATION
# =====================================


def check_password_strength(event=None):

    password = password_entry.get()

    upper = bool(re.search(r"[A-Z]", password))
    lower = bool(re.search(r"[a-z]", password))
    number = bool(re.search(r"\d", password))
    special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    length = len(password) >= 8

    req1.configure(
        text=("✅ Min 8 Characters" if length else "❌ Min 8 Characters"),
        text_color=("lime" if length else "red"),
    )

    req2.configure(
        text=("✅ One Number" if number else "❌ One Number"),
        text_color=("lime" if number else "red"),
    )

    req3.configure(
        text=("✅ Uppercase" if upper else "❌ Uppercase"),
        text_color=("lime" if upper else "red"),
    )

    req4.configure(
        text=("✅ Special Character" if special else "❌ Special Character"),
        text_color=("lime" if special else "red"),
    )

    req5.configure(
        text=("✅ Lowercase" if lower else "❌ Lowercase"),
        text_color=("lime" if lower else "red"),
    )

    if length and upper and lower and number and special:

        req1.grid_remove()
        req2.grid_remove()
        req3.grid_remove()
        req4.grid_remove()
        req5.grid_remove()

        strong_password_label.configure(text="✅ Strong Password")

    else:

        req1.grid()
        req2.grid()
        req3.grid()
        req4.grid()
        req5.grid()

        strong_password_label.configure(text="")


# =====================================
# LIVE CONFIRM PASSWORD CHECK
# =====================================


def check_confirm_password(event=None):

    password = password_entry.get()

    confirm_password = confirm_password_entry.get()

    if confirm_password == "":

        confirm_password_error.configure(text="")

        return

    if password != confirm_password:

        confirm_password_error.configure(
            text="❌ Passwords do not match", text_color="red"
        )

    else:

        confirm_password_error.configure(
            text="✅ Passwords match", text_color="#00ff66"
        )


# =====================================
# REGISTER FUNCTION
# =====================================


def handle_register():

    global generated_otp
    global pending_user

    username = username_entry.get().strip()
    email = email_entry.get().strip().lower()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not username or not email or not password or not confirm_password:

        messagebox.showwarning("Missing Data", "Please fill all fields.")

        return

    if "@" not in email or "." not in email:

        messagebox.showerror("Email Error", "Please enter a valid email address.")

        return

    if len(username) < 6:

        messagebox.showerror(
            "Username Error", "Username must be at least 3 characters."
        )

        return

    if (
        len(password) < 8
        or not re.search(r"[A-Z]", password)
        or not re.search(r"[a-z]", password)
        or not re.search(r"\d", password)
        or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    ):

        messagebox.showerror(
            "Password Error", "Please satisfy all password requirements."
        )
        return

    if password != confirm_password:

        messagebox.showerror("Password Error", "Passwords do not match.")

        return

    # =====================================
    # CHECK EXISTING EMAIL
    # =====================================

    if email_exists(email):

        messagebox.showerror("Registration Error", "Email already exists.")

        return

    # =====================================
    # CHECK EXISTING USERNAME
    # =====================================

    if username_exists(username):

        messagebox.showerror("Registration Error", "Username already exists.")

        return

    # =====================================
    # GENERATE OTP
    # =====================================

    generated_otp = generate_otp()

    pending_user = {"username": username, "email": email, "password": password}

    # =====================================
    # SAVE OTP + USER DATA
    # =====================================

    temp_data = {
        "otp": generated_otp,
        "username": username,
        "email": email,
        "password": password,
    }

    with open("temp_otp.json", "w") as file:

        json.dump(temp_data, file)

    # =====================================
    # SEND OTP
    # =====================================

    success = send_otp_email(email, generated_otp)

    if success:

        messagebox.showinfo("OTP Sent", "Verification OTP has been sent to your email.")

        app.destroy()

        subprocess.Popen(["python", "gui/verify_otp.py"])

    else:

        messagebox.showerror("Email Error", "Failed to send OTP.")


# =====================================
# SHOW / HIDE PASSWORD
# =====================================


def toggle_password():

    if password_entry.cget("show") == "*":

        password_entry.configure(show="")
        show_password_btn.configure(text="🙈")

    else:

        password_entry.configure(show="*")
        show_password_btn.configure(text="👁")


def toggle_confirm_password():

    if confirm_password_entry.cget("show") == "*":

        confirm_password_entry.configure(show="")
        show_confirm_btn.configure(text="🙈")

    else:

        confirm_password_entry.configure(show="*")
        show_confirm_btn.configure(text="👁")


# =====================================
# WINDOW
# =====================================

app = ctk.CTk()

app.title("CryptVault - Register")

app.geometry("550x670")

app.resizable(False, False)

app.configure(fg_color="#02060a")

# =====================================
# BACKGROUND
# =====================================

bg_path = os.path.join(project_root, "assets", "register.jpg")

bg_image = ctk.CTkImage(
    light_image=Image.open(bg_path), dark_image=Image.open(bg_path), size=(550, 670)
)

bg_label = ctk.CTkLabel(app, image=bg_image, text="")

bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# =====================================
# GLASS CARD
# =====================================

main_frame = ctk.CTkFrame(
    app, width=450, height=655, corner_radius=15, fg_color="#111111", border_width=0
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

main_frame.pack_propagate(False)

# =====================================
# VAULT IMAGE
# =====================================

vault_icon = ctk.CTkImage(
    light_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    dark_image=Image.open(os.path.join(project_root, "assets", "vault.png")),
    size=(55, 55),
)

# =====================================
# VAULT ICON
# =====================================

icon_label = ctk.CTkLabel(main_frame, image=vault_icon, text="")

icon_label.pack(pady=(5, 5))

# =====================================
# TITLE
# =====================================

title_label = ctk.CTkLabel(
    main_frame, text="Create your CryptVault Account", font=("Segoe UI", 18, "bold")
)

title_label.pack(pady=(0, 5))
# =====================================
# USERNAME
# =====================================

username_label = ctk.CTkLabel(main_frame, text="Username")

username_label.pack()

username_entry = ctk.CTkEntry(
    main_frame,
    width=350,
    height=45,
    corner_radius=15,
    placeholder_text="Enter username",
)

username_entry.pack(pady=(3, 3))

# =====================================
# EMAIL
# =====================================

email_label = ctk.CTkLabel(main_frame, text="Email")

email_label.pack()

email_entry = ctk.CTkEntry(
    main_frame,
    width=350,
    height=45,
    corner_radius=15,
    placeholder_text="Enter email address",
)

email_entry.pack(pady=(3, 3))

# =====================================
# PASSWORD
# =====================================

password_label = ctk.CTkLabel(main_frame, text="Password")

password_label.pack()

password_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

password_frame.pack(pady=(3, 3))

password_entry = ctk.CTkEntry(
    password_frame,
    width=295,
    height=45,
    corner_radius=15,
    show="*",
    placeholder_text="Enter password",
)

password_entry.pack(side="left", padx=(0, 3))
password_entry.bind("<Control-c>", lambda e: "break")
password_entry.bind("<Control-v>", lambda e: "break")
password_entry.bind("<Control-x>", lambda e: "break")
password_entry.bind("<Control-a>", lambda e: "break")
password_entry.bind("<KeyRelease>", check_password_strength)

show_password_btn = ctk.CTkButton(
    password_frame,
    text="👁",
    width=45,
    height=45,
    corner_radius=15,
    command=toggle_password,
)

show_password_btn.pack(side="left")

# =====================================
# CONFIRM PASSWORD
# =====================================

confirm_password_label = ctk.CTkLabel(main_frame, text="Confirm Password")

confirm_password_label.pack()

confirm_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

confirm_frame.pack(pady=(3, 3))

confirm_password_entry = ctk.CTkEntry(
    confirm_frame,
    width=295,
    height=45,
    corner_radius=15,
    show="*",
    placeholder_text="Confirm password",
)

confirm_password_entry.pack(side="left", padx=(0, 3))

confirm_password_entry.bind("<KeyRelease>", check_confirm_password)

confirm_password_entry.bind("<Control-c>", lambda e: "break")
confirm_password_entry.bind("<Control-v>", lambda e: "break")
confirm_password_entry.bind("<Control-x>", lambda e: "break")
confirm_password_entry.bind("<Control-a>", lambda e: "break")

show_confirm_btn = ctk.CTkButton(
    confirm_frame,
    text="👁",
    width=45,
    height=45,
    corner_radius=15,
    command=toggle_confirm_password,
)

show_confirm_btn.pack(side="left")

# =====================================
# CONFIRM PASSWORD STATUS
# =====================================

confirm_password_error = ctk.CTkLabel(
    main_frame, text="", text_color="red", font=("Segoe UI", 11)
)

confirm_password_error.pack(pady=(0, 2))

# =====================================
# PASSWORD REQUIREMENTS FRAME
# =====================================

requirements_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

requirements_frame.pack(pady=(0, 0))

req1 = ctk.CTkLabel(
    requirements_frame, text="❌ 8 Characters", text_color="red", font=("Segoe UI", 10)
)

req1.grid(row=0, column=0, padx=6)

req2 = ctk.CTkLabel(
    requirements_frame, text="❌ Uppercase", text_color="red", font=("Segoe UI", 10)
)

req2.grid(row=0, column=1, padx=6)

req3 = ctk.CTkLabel(
    requirements_frame, text="❌ Lowercase", text_color="red", font=("Segoe UI", 10)
)

req3.grid(row=0, column=2, padx=6)

req4 = ctk.CTkLabel(
    requirements_frame, text="❌ Number", text_color="red", font=("Segoe UI", 10)
)

req4.grid(row=0, column=3, padx=6)

req5 = ctk.CTkLabel(
    requirements_frame, text="❌ Special", text_color="red", font=("Segoe UI", 10)
)

req5.grid(row=0, column=4, padx=6)

# =====================================
# STRONG PASSWORD LABEL
# =====================================

strong_password_label = ctk.CTkLabel(
    requirements_frame, text="", text_color="#00ff66", font=("Segoe UI", 11, "bold")
)

strong_password_label.grid(row=1, column=0, columnspan=5, pady=(0, 0))

# =====================================
# REGISTER BUTTON
# =====================================

register_button = ctk.CTkButton(
    main_frame,
    text="Register",
    width=350,
    height=45,
    corner_radius=15,
    font=("Segoe UI", 16, "bold"),
    command=handle_register,
    fg_color="#1f6aa5",
    hover_color="#144870",
)

register_button.pack(pady=(0, 0))

# =====================================
# LOGIN SECTION
# =====================================

login_label = ctk.CTkLabel(
    main_frame,
    text="Already have an account?",
    text_color="lightgray",
    font=("Segoe UI", 14),
)

login_label.pack(pady=(0, 0))

login_button = ctk.CTkButton(
    main_frame,
    text="Login",
    width=350,
    height=45,
    corner_radius=15,
    fg_color="transparent",
    border_width=2,
    border_color="#1f6aa5",
    hover_color="#10253a",
    command=open_login_page,
)

login_button.pack()

# =====================================
# FOOTER
# =====================================

footer_label = ctk.CTkLabel(main_frame, text="CryptVault v1.0", text_color="gray")

footer_label.pack(side="bottom", pady=5)

# =====================================
# ENTER KEY SUPPORT
# =====================================

app.bind("<Return>", lambda event: handle_register())

# =====================================
# RUN APP
# =====================================

app.mainloop()
