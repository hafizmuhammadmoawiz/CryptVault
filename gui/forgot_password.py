import sys
import os
import subprocess

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(project_root)

import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import json
import subprocess

from core.authentication import email_exists
from core.otp_manager import generate_otp, send_otp_email

# =====================================
# SETTINGS
# =====================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =====================================
# FUNCTIONS
# =====================================


def back_to_login():

    app.destroy()

    subprocess.Popen(["python", "gui/login_page.py"])


def send_otp():

    email = email_entry.get().strip().lower()

    if not email:

        messagebox.showwarning("Missing Data", "Please enter your email.")

        return

    if not email_exists(email):

        messagebox.showerror("Email Error", "Email does not exist.")

        return

    otp = generate_otp()

    temp_data = {"email": email, "otp": otp}

    with open("forgot_otp.json", "w") as file:

        json.dump(temp_data, file)

    success = send_otp_email(email, otp)

    if success:

        messagebox.showinfo("OTP Sent", "OTP has been sent to your registered email.")

        app.destroy()

        subprocess.Popen(["python", "gui/forgot_verify_otp.py"])

    else:

        messagebox.showerror("Email Error", "Failed to send OTP.")


# =====================================
# WINDOW
# =====================================

app = ctk.CTk()

app.title("CryptVault - Password Recovery")

app.geometry("550x650")

app.resizable(False, False)

app.configure(fg_color="#02060a")

# =====================================
# BACKGROUND
# =====================================

bg_path = os.path.join(project_root, "assets", "forgot.jpg")

bg_image = ctk.CTkImage(
    light_image=Image.open(bg_path), dark_image=Image.open(bg_path), size=(600, 700)
)

bg_label = ctk.CTkLabel(app, image=bg_image, text="")

bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# =====================================
# MAIN GLASS CARD
# =====================================

main_frame = ctk.CTkFrame(
    app,
    width=455,
    height=615,
    corner_radius=30,
    fg_color="#0f1117",
    border_width=2,
    border_color="#4da6ff",
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

main_frame.pack_propagate(False)

id = "y9w5mf"
# =====================================
# SECURITY ICON
# =====================================

icon_label = ctk.CTkLabel(main_frame, text="🛡", font=("Segoe UI", 50))

icon_label.pack(pady=(12, 4))

# =====================================
# TITLE
# =====================================

title_label = ctk.CTkLabel(
    main_frame, text="Password Recovery", font=("Segoe UI", 28, "bold")
)

title_label.pack(pady=(0, 4))

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Secure Account Recovery Portal",
    font=("Segoe UI", 13),
    text_color="lightgray",
)

subtitle_label.pack(pady=(0, 11))

# =====================================
# INFO BANNER
# =====================================

info_frame = ctk.CTkFrame(
    main_frame, width=300, height=55, corner_radius=18, fg_color="#123a5c"
)

info_frame.pack(pady=(3, 13))

info_frame.pack_propagate(False)

info_label = ctk.CTkLabel(
    info_frame,
    text="📧 A One-Time Password (OTP)\nwill be sent to your registered email",
    font=("Segoe UI", 13, "bold"),
    justify="center",
)

info_label.place(relx=0.5, rely=0.5, anchor="center")

# =====================================
# SECURITY MESSAGE
# =====================================

security_note = ctk.CTkLabel(
    main_frame,
    text="Only verified account owners can reset passwords.",
    font=(
        "Segoe UI",
        12,
    ),
    text_color="#8f8f8f",
)

security_note.pack(pady=(0, 10))

id = "mtv7w2"
# =====================================
# EMAIL SECTION TITLE
# =====================================

email_section_label = ctk.CTkLabel(
    main_frame, text="Registered Email Address", font=("Segoe UI", 15, "bold")
)

email_section_label.pack(pady=(4, 4))

# =====================================
# EMAIL INPUT
# =====================================

email_entry = ctk.CTkEntry(
    main_frame,
    width=380,
    height=58,
    corner_radius=18,
    placeholder_text="Enter your registered email address",
    font=("Segoe UI", 14),
)

email_entry.pack(pady=(0, 10))

# =====================================
# RECOVERY TIPS BOX
# =====================================

tips_frame = ctk.CTkFrame(
    main_frame, width=400, height=110, corner_radius=18, fg_color="#151c24"
)

tips_frame.pack(pady=(4, 12))

tips_frame.pack_propagate(False)

tips_label = ctk.CTkLabel(
    tips_frame,
    text=(
        "✓ Use the email linked to your account\n\n"
        "✓ Check spam folder if OTP is not received\n\n"
        "✓ OTP will expire after a limited time"
    ),
    justify="left",
    font=("Segoe UI", 11),
)

tips_label.place(relx=0.05, rely=0.5, anchor="w")


# =====================================
# BUTTONS FRAME
# =====================================

buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

buttons_frame.pack(pady=(5, 10))

# =====================================
# SEND OTP BUTTON
# =====================================

send_btn = ctk.CTkButton(
    buttons_frame,
    text="📨 Send OTP",
    width=180,
    height=55,
    corner_radius=18,
    font=("Segoe UI", 14, "bold"),
    fg_color="#1f6aa5",
    hover_color="#144870",
    border_width=1,
    border_color="#4da6ff",
    command=send_otp,
)

send_btn.grid(row=0, column=0, padx=(0, 5))

# =====================================
# BACK TO LOGIN
# =====================================

back_btn = ctk.CTkButton(
    buttons_frame,
    text="⬅ Back",
    width=180,
    height=55,
    corner_radius=18,
    font=("Segoe UI", 14, "bold"),
    fg_color="transparent",
    border_width=2,
    border_color="#4da6ff",
    hover_color="#10253a",
    command=back_to_login,
)

back_btn.grid(row=0, column=1, padx=(5, 0))


# =====================================
# FOOTER
# =====================================

footer_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

footer_frame.pack(side="bottom", fill="x", pady=(0, 15))


footer_label2 = ctk.CTkLabel(
    footer_frame,
    text="🔐 Protecting Your Digital Assets",
    font=("Segoe UI", 11),
    text_color="#6c6c6c",
)
footer_label2.pack()

# =====================================
# KEY BINDINGS
# =====================================

app.bind("<Escape>", lambda event: back_to_login())

# =====================================
# RUN APP
# =====================================

app.mainloop()
