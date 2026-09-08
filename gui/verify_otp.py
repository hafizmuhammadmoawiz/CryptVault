import sys
import os
import subprocess

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(project_root)

import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import json
from core.otp_manager import generate_otp, send_otp_email

from core.authentication import register_user

# =====================================
# BUTTON ICONS
# =====================================

otp_icon = ctk.CTkImage(
    light_image=Image.open(os.path.join(project_root, "assets", "veri.png")),
    dark_image=Image.open(os.path.join(project_root, "assets", "veri.png")),
    size=(24, 24),
)

resend_icon = ctk.CTkImage(
    light_image=Image.open(os.path.join(project_root, "assets", "resendd.png")),
    dark_image=Image.open(os.path.join(project_root, "assets", "resendd.png")),
    size=(24, 24),
)

back_icon = ctk.CTkImage(
    light_image=Image.open(os.path.join(project_root, "assets", "backk.png")),
    dark_image=Image.open(os.path.join(project_root, "assets", "backk.png")),
    size=(24, 24),
)

# =====================================
# SETTINGS
# =====================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =====================================
# FUNCTIONS
# =====================================


def verify_otp():

    entered_otp = (
        otp1.get() + otp2.get() + otp3.get() + otp4.get() + otp5.get() + otp6.get()
    )

    if len(entered_otp) != 6:

        messagebox.showerror("OTP Error", "Please enter all 6 digits.")

        return

    try:

        with open("temp_otp.json", "r") as file:

            data = json.load(file)

        stored_otp = str(data["otp"])

        if entered_otp != stored_otp:

            messagebox.showerror("Invalid OTP", "OTP verification failed.")

            return

        result = register_user(data["username"], data["email"], data["password"])

        if result["success"]:

            if os.path.exists("temp_otp.json"):
                os.remove("temp_otp.json")

            messagebox.showinfo("Success", "Account created successfully.")

            app.destroy()

            subprocess.Popen(["python", "gui/login_page.py"])

        else:

            messagebox.showerror("Registration Failed", result["message"])

    except Exception as error:

        messagebox.showerror("Error", str(error))


def resend_otp():

    try:

        with open("temp_otp.json", "r") as file:

            data = json.load(file)

        new_otp = generate_otp()

        data["otp"] = new_otp

        with open("temp_otp.json", "w") as file:

            json.dump(data, file)

        success = send_otp_email(data["email"], new_otp)

        if success:

            messagebox.showinfo("OTP Sent", "A new OTP has been sent to your email.")

        else:

            messagebox.showerror("Email Error", "Failed to resend OTP.")

    except Exception as error:

        messagebox.showerror("Error", str(error))


# =====================================
# OTP NAVIGATION
# =====================================


def otp_key_handler(event, current_box, previous_box=None, next_box=None):

    key = event.keysym

    # LEFT

    if key == "Left":

        if previous_box:

            previous_box.focus()

        return "break"

    # RIGHT

    if key == "Right":

        if next_box:

            next_box.focus()

        return "break"

    # BACKSPACE

    if key == "BackSpace":

        if current_box.get() == "" and previous_box:

            previous_box.delete(0, "end")

            previous_box.focus()

            return "break"

        return

    # ONLY NUMBERS

    if len(event.char) > 0:

        if not event.char.isdigit():

            return "break"

        current_box.delete(0, "end")

        current_box.insert(0, event.char)

        if next_box:

            next_box.focus()

        return "break"


def handle_paste(event):

    try:

        pasted_text = app.clipboard_get()

    except:

        return "break"

    pasted_text = pasted_text.strip()

    if not pasted_text.isdigit():

        return "break"

    if len(pasted_text) != 6:

        return "break"

    boxes = [otp1, otp2, otp3, otp4, otp5, otp6]

    for i in range(6):

        boxes[i].delete(0, "end")

        boxes[i].insert(0, pasted_text[i])

    otp6.focus()

    return "break"


def back_to_register():

    app.destroy()

    subprocess.Popen(["python", "gui/register_page.py"])


# =====================================
# WINDOW
# =====================================

app = ctk.CTk()

app.title("CryptVault - OTP Verification")

app.geometry("550x670")

app.resizable(False, False)

# =====================================
# BACKGROUND
# =====================================

bg_path = os.path.join(project_root, "assets", "otp.jpg")

bg_image = ctk.CTkImage(
    light_image=Image.open(bg_path), dark_image=Image.open(bg_path), size=(600, 700)
)

bg_label = ctk.CTkLabel(app, image=bg_image, text="")

bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# =====================================
# MAIN CARD
# =====================================

main_frame = ctk.CTkFrame(
    app,
    width=450,
    height=630,
    corner_radius=30,
    fg_color="#0f1117",
    border_width=2,
    border_color="#4da6ff",
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

main_frame.pack_propagate(False)


# =====================================
# SECURITY ICON
# =====================================

icon_label = ctk.CTkLabel(main_frame, text="🛡", font=("Segoe UI", 44))

icon_label.pack(pady=(7, 3))

# =====================================
# TITLE
# =====================================

title_label = ctk.CTkLabel(
    main_frame, text="Verify Your Email", font=("Segoe UI", 28, "bold")
)

title_label.pack(pady=(0, 3))

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Secure Account Verification",
    font=("Segoe UI", 14),
    text_color="lightgray",
)

subtitle_label.pack(pady=(0, 9))

# =====================================
# INFO BANNER
# =====================================

info_frame = ctk.CTkFrame(
    main_frame, width=280, height=55, corner_radius=18, fg_color="#123a5c"
)

info_frame.pack(pady=(2, 8))

info_frame.pack_propagate(False)

info_label = ctk.CTkLabel(
    info_frame,
    text="📧 A verification code has been\nsent to your email address",
    font=("Segoe UI", 13, "bold"),
    justify="center",
)

info_label.place(relx=0.5, rely=0.5, anchor="center")

# =====================================
# SECURITY MESSAGE
# =====================================

security_note = ctk.CTkLabel(
    main_frame,
    text="Enter the 6-digit OTP received in your inbox.",
    font=("Segoe UI", 12),
    text_color="#8f8f8f",
)

security_note.pack(pady=(0, 0))


# =====================================
# OTP LABEL
# =====================================

otp_label = ctk.CTkLabel(
    main_frame, text="Enter Verification OTP", font=("Segoe UI", 15, "bold")
)

otp_label.pack(pady=(5, 5))

# =====================================
# OTP BOXES FRAME
# =====================================

otp_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

otp_frame.pack(pady=(0, 20))

# =====================================
# OTP BOXES
# =====================================

otp1 = ctk.CTkEntry(
    otp_frame,
    width=50,
    height=55,
    corner_radius=12,
    justify="center",
    font=("Segoe UI", 22, "bold"),
    border_color="#4da6ff",
    border_width=2,
)

otp1.grid(row=0, column=0, padx=3)

otp2 = ctk.CTkEntry(
    otp_frame,
    width=50,
    height=55,
    corner_radius=12,
    justify="center",
    font=("Segoe UI", 22, "bold"),
    border_color="#4da6ff",
    border_width=2,
)

otp2.grid(row=0, column=1, padx=3)

otp3 = ctk.CTkEntry(
    otp_frame,
    width=50,
    height=55,
    corner_radius=12,
    justify="center",
    font=("Segoe UI", 22, "bold"),
    border_color="#4da6ff",
    border_width=2,
)

otp3.grid(row=0, column=2, padx=3)

otp4 = ctk.CTkEntry(
    otp_frame,
    width=50,
    height=55,
    corner_radius=12,
    justify="center",
    font=("Segoe UI", 22, "bold"),
    border_color="#4da6ff",
    border_width=2,
)

otp4.grid(row=0, column=3, padx=3)

otp5 = ctk.CTkEntry(
    otp_frame,
    width=50,
    height=55,
    corner_radius=12,
    justify="center",
    font=("Segoe UI", 22, "bold"),
    border_color="#4da6ff",
    border_width=2,
)

otp5.grid(row=0, column=4, padx=3)

otp6 = ctk.CTkEntry(
    otp_frame,
    width=50,
    height=55,
    corner_radius=12,
    justify="center",
    font=("Segoe UI", 22, "bold"),
    border_color="#4da6ff",
    border_width=2,
)

otp6.grid(row=0, column=5, padx=3)


# =====================================
# OTP EVENTS
# =====================================

otp1.bind("<KeyPress>", lambda e: otp_key_handler(e, otp1, None, otp2))

otp2.bind("<KeyPress>", lambda e: otp_key_handler(e, otp2, otp1, otp3))

otp3.bind("<KeyPress>", lambda e: otp_key_handler(e, otp3, otp2, otp4))

otp4.bind("<KeyPress>", lambda e: otp_key_handler(e, otp4, otp3, otp5))

otp5.bind("<KeyPress>", lambda e: otp_key_handler(e, otp5, otp4, otp6))

otp6.bind("<KeyPress>", lambda e: otp_key_handler(e, otp6, otp5, None))

# =====================================
# CTRL + V PASTE
# =====================================

otp1.bind("<Control-v>", handle_paste)
otp2.bind("<Control-v>", handle_paste)
otp3.bind("<Control-v>", handle_paste)
otp4.bind("<Control-v>", handle_paste)
otp5.bind("<Control-v>", handle_paste)
otp6.bind("<Control-v>", handle_paste)

# =====================================
# INSTRUCTIONS CARD
# =====================================

tips_frame = ctk.CTkFrame(
    main_frame, width=280, height=80, corner_radius=18, fg_color="#151c24"
)

tips_frame.pack(pady=(3, 9))

tips_frame.pack_propagate(False)

tips_label = ctk.CTkLabel(
    tips_frame,
    text="✓ Check your Inbox and Spam folder\n\n" "✓ Do not share your OTP with anyone",
    justify="left",
    font=("Segoe UI", 12),
)

tips_label.place(relx=0.05, rely=0.5, anchor="w")


# =====================================
# BUTTONS FRAME
# =====================================

buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

buttons_frame.pack(pady=(7, 7))

# =====================================
# VERIFY OTP BUTTON
# =====================================

verify_btn = ctk.CTkButton(
    buttons_frame,
    text=" Verify OTP",
    image=otp_icon,
    compound="left",
    width=180,
    height=55,
    corner_radius=18,
    font=("Segoe UI", 14, "bold"),
    fg_color="#1f6aa5",
    hover_color="#2d84c7",
    border_width=2,
    border_color="#4da6ff",
    command=verify_otp,
)

verify_btn.grid(row=0, column=0, padx=(0, 8))

# =====================================
# RESEND OTP BUTTON
# =====================================

resend_btn = ctk.CTkButton(
    buttons_frame,
    text=" Resend OTP",
    image=resend_icon,
    compound="left",
    width=180,
    height=55,
    corner_radius=18,
    font=("Segoe UI", 14, "bold"),
    fg_color="#252b35",
    hover_color="#3a3a3a",
    border_width=2,
    border_color="#4da6ff",
    command=resend_otp,
)

resend_btn.grid(row=0, column=1, padx=(8, 0))

# =====================================
# BACK BUTTON
# =====================================

back_btn = ctk.CTkButton(
    main_frame,
    text=" Back To Register",
    image=back_icon,
    compound="left",
    width=380,
    height=55,
    corner_radius=18,
    font=("Segoe UI", 14, "bold"),
    fg_color="transparent",
    border_width=2,
    border_color="#4da6ff",
    hover_color="#10253a",
    command=back_to_register,
)

back_btn.pack(pady=(5, 10))

# =====================================
# FOOTER
# =====================================

footer_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

footer_frame.pack(side="bottom", fill="x", pady=(0, 15))

footer_label2 = ctk.CTkLabel(
    footer_frame,
    text="🔐 Protecting Your Digital Identity",
    font=("Segoe UI", 11),
    text_color="#6c6c6c",
)

footer_label2.pack()

# =====================================
# ESC SHORTCUT
# =====================================

app.bind("<Escape>", lambda event: back_to_register())

# =====================================
# RUN APP
# =====================================

app.mainloop()
