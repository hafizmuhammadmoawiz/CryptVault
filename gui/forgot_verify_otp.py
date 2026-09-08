import sys
import os
import json
import re
import subprocess

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(project_root)

import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

from core.authentication import update_password
from core.otp_manager import generate_otp, send_otp_email

# =====================================
# SETTINGS
# =====================================

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")

# =====================================
# PASSWORD VISIBILITY
# =====================================

password_visible = False

confirm_password_visible = False

# =====================================
# TOGGLE PASSWORD
# =====================================


def toggle_password():

    global password_visible

    password_visible = not password_visible

    if password_visible:

        password_entry.configure(show="")

        show_password_btn.configure(text="🙈")

    else:

        password_entry.configure(show="*")

        show_password_btn.configure(text="👁")


# =====================================
# TOGGLE CONFIRM PASSWORD
# =====================================


def toggle_confirm_password():

    global confirm_password_visible

    confirm_password_visible = not confirm_password_visible

    if confirm_password_visible:

        confirm_password_entry.configure(show="")

        show_confirm_btn.configure(text="🙈")

    else:

        confirm_password_entry.configure(show="*")

        show_confirm_btn.configure(text="👁")


# =====================================
# PASSWORD POLICY
# =====================================


def check_password_strength(event=None):

    password = password_entry.get()

    upper = bool(re.search(r"[A-Z]", password))

    lower = bool(re.search(r"[a-z]", password))

    number = bool(re.search(r"\d", password))

    special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    length = len(password) >= 8

    req1.configure(text_color=("lime" if length else "red"))

    req2.configure(text_color=("lime" if upper else "red"))

    req3.configure(text_color=("lime" if lower else "red"))

    req4.configure(text_color=("lime" if number else "red"))

    req5.configure(text_color=("lime" if special else "red"))


# =====================================
# PASSWORD MATCH
# =====================================


def check_confirm_password(event=None):

    password = password_entry.get()

    confirm_password = confirm_password_entry.get()

    if not confirm_password:

        match_label.configure(text="")

        return

    if password == confirm_password:

        match_label.configure(text="✅ Passwords match", text_color="#00ff66")

    else:

        match_label.configure(text="❌ Passwords do not match", text_color="red")


# =====================================
# BACK TO LOGIN
# =====================================


def back_to_login():

    app.destroy()

    subprocess.Popen(["python", "gui/login_page.py"])


# =====================================
# PLACEHOLDERS
# =====================================

# =====================================
# RESEND OTP
# =====================================


def resend_otp():

    try:

        with open("forgot_otp.json", "r") as file:

            data = json.load(file)

        new_otp = generate_otp()

        data["otp"] = new_otp

        with open("forgot_otp.json", "w") as file:

            json.dump(data, file)

        success = send_otp_email(data["email"], new_otp)

        if success:

            messagebox.showinfo("OTP Sent", "A new OTP has been sent to your email.")

        else:

            messagebox.showerror("Email Error", "Failed to resend OTP.")

    except Exception as error:

        messagebox.showerror("Error", str(error))


# =====================================
# CHANGE PASSWORD
# =====================================


def change_password():

    entered_otp = (
        otp1.get() + otp2.get() + otp3.get() + otp4.get() + otp5.get() + otp6.get()
    )

    if len(entered_otp) != 6:

        messagebox.showerror("OTP Error", "Please enter all 6 OTP digits.")

        return

    password = password_entry.get()

    confirm_password = confirm_password_entry.get()

    try:

        with open("forgot_otp.json", "r") as file:

            data = json.load(file)

        stored_otp = str(data["otp"])

        email = data["email"]

        if entered_otp != stored_otp:

            messagebox.showerror("Invalid OTP", "OTP verification failed.")

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

        success = update_password(email, password)

        if success:

            if os.path.exists("forgot_otp.json"):

                os.remove("forgot_otp.json")

            success_label.configure(
                text="✅ Your password has been changed successfully.",
                text_color="#00ff66",
            )

            app.after(
                2000,
                lambda: (
                    app.destroy(),
                    subprocess.Popen(["python", "gui/login_page.py"]),
                ),
            )

        else:

            messagebox.showerror("Error", "Failed to update password.")

    except Exception as error:

        messagebox.showerror("Error", str(error))


# =====================================
# WINDOW
# =====================================

app = ctk.CTk()

app.title("Password Reset Verification")

app.geometry("600x680")

app.resizable(False, False)

# =====================================
# BACKGROUND
# =====================================

bg_path = os.path.join(project_root, "assets", "forgot_verify.jpg")

bg_image = ctk.CTkImage(
    light_image=Image.open(bg_path), dark_image=Image.open(bg_path), size=(600, 680)
)

bg_label = ctk.CTkLabel(app, image=bg_image, text="")

bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# =====================================
# MAIN CARD
# =====================================

main_frame = ctk.CTkFrame(
    app,
    width=560,
    height=660,
    corner_radius=30,
    fg_color="#0f1117",
    border_width=2,
    border_color="#4da6ff",
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

main_frame.pack_propagate(False)

# =====================================
# TITLE
# =====================================

icon_label = ctk.CTkLabel(main_frame, text="🛡", font=("Segoe UI", 35))

icon_label.pack(pady=(5, 5))

title_label = ctk.CTkLabel(
    main_frame, text="Password Reset Verification", font=("Segoe UI", 24, "bold")
)

title_label.pack()

subtitle_label = ctk.CTkLabel(
    main_frame,
    text="Verify OTP And Create New Password",
    font=("Segoe UI", 13),
    text_color="lightgray",
)

subtitle_label.pack(pady=(0, 3))

# =====================================
# INFO CARD
# =====================================

info_frame = ctk.CTkFrame(
    main_frame, width=370, height=50, corner_radius=18, fg_color="#123a5c"
)

info_frame.pack(pady=(5, 5))

info_frame.pack_propagate(False)

info_label = ctk.CTkLabel(
    info_frame,
    text="📧 Enter OTP Sent To Your Registered Email",
    font=("Segoe UI", 13, "bold"),
)

info_label.place(relx=0.5, rely=0.5, anchor="center")

# =====================================
# OTP LABEL
# =====================================

otp_label = ctk.CTkLabel(
    main_frame, text="Verification Code", font=("Segoe UI", 15, "bold")
)

otp_label.pack(pady=(3, 3))

# =====================================
# OTP FRAME
# =====================================

otp_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

otp_frame.pack(pady=(0, 4))

# =====================================
# OTP BOXES
# =====================================

otp1 = ctk.CTkEntry(
    otp_frame,
    width=50,
    height=50,
    corner_radius=12,
    justify="center",
    font=("Segoe UI", 24, "bold"),
    border_width=2,
    border_color="#4da6ff",
    fg_color="#151c24",
)

otp1.grid(row=0, column=0, padx=4)

otp2 = ctk.CTkEntry(
    otp_frame,
    width=50,
    height=50,
    corner_radius=12,
    justify="center",
    font=("Segoe UI", 24, "bold"),
    border_width=2,
    border_color="#4da6ff",
    fg_color="#151c24",
)

otp2.grid(row=0, column=1, padx=4)

otp3 = ctk.CTkEntry(
    otp_frame,
    width=50,
    height=50,
    corner_radius=12,
    justify="center",
    font=("Segoe UI", 24, "bold"),
    border_width=2,
    border_color="#4da6ff",
    fg_color="#151c24",
)

otp3.grid(row=0, column=2, padx=4)

otp4 = ctk.CTkEntry(
    otp_frame,
    width=50,
    height=50,
    corner_radius=12,
    justify="center",
    font=("Segoe UI", 24, "bold"),
    border_width=2,
    border_color="#4da6ff",
    fg_color="#151c24",
)

otp4.grid(row=0, column=3, padx=4)

otp5 = ctk.CTkEntry(
    otp_frame,
    width=50,
    height=50,
    corner_radius=12,
    justify="center",
    font=("Segoe UI", 24, "bold"),
    border_width=2,
    border_color="#4da6ff",
    fg_color="#151c24",
)

otp5.grid(row=0, column=4, padx=4)

otp6 = ctk.CTkEntry(
    otp_frame,
    width=50,
    height=50,
    corner_radius=12,
    justify="center",
    font=("Segoe UI", 24, "bold"),
    border_width=2,
    border_color="#4da6ff",
    fg_color="#151c24",
)

otp6.grid(row=0, column=5, padx=4)

# =====================================
# OTP LIST
# =====================================

otp_entries = [otp1, otp2, otp3, otp4, otp5, otp6]

# =====================================
# OTP FUNCTIONS
# =====================================


def move_next(event, current_box, next_box):

    value = current_box.get()

    value = "".join(filter(str.isdigit, value))

    if len(value) > 1:

        value = value[-1]

    current_box.delete(0, "end")

    current_box.insert(0, value)

    if len(value) == 1:

        next_box.focus_set()


def handle_backspace(event, current_box, previous_box):

    if event.keysym != "BackSpace":

        return

    # Agar current box me value hai
    if current_box.get():

        current_box.delete(0, "end")

        return "break"

    # Agar current box empty hai
    previous_box.focus_set()

    previous_box.delete(0, "end")

    return "break"


def handle_arrow_keys(event, previous_box=None, next_box=None):

    if event.keysym == "Left":

        if previous_box:

            previous_box.focus_set()

        return "break"

    if event.keysym == "Right":

        if next_box:

            next_box.focus_set()

        return "break"


def bind_arrow_keys():

    otp1.bind("<Left>", lambda e: "break")

    otp1.bind("<Right>", lambda e: (otp2.focus_set(), "break")[-1])

    otp2.bind("<Left>", lambda e: (otp1.focus_set(), "break")[-1])

    otp2.bind("<Right>", lambda e: (otp3.focus_set(), "break")[-1])

    otp3.bind("<Left>", lambda e: (otp2.focus_set(), "break")[-1])

    otp3.bind("<Right>", lambda e: (otp4.focus_set(), "break")[-1])

    otp4.bind("<Left>", lambda e: (otp3.focus_set(), "break")[-1])

    otp4.bind("<Right>", lambda e: (otp5.focus_set(), "break")[-1])

    otp5.bind("<Left>", lambda e: (otp4.focus_set(), "break")[-1])

    otp5.bind("<Right>", lambda e: (otp6.focus_set(), "break")[-1])

    otp6.bind("<Left>", lambda e: (otp5.focus_set(), "break")[-1])


# =====================================
# OTP PASTE
# =====================================


def paste_otp(event):

    try:

        pasted = app.clipboard_get()

        pasted = "".join(filter(str.isdigit, pasted))

        if len(pasted) != 6:

            return "break"

        for i in range(6):

            otp_entries[i].delete(0, "end")

            otp_entries[i].insert(0, pasted[i])

        otp6.focus()

        return "break"

    except:

        return "break"


# =====================================
# ONLY NUMBERS ALLOWED
# =====================================


def allow_only_numbers(event):

    # Allow navigation keys
    if event.keysym in ["BackSpace", "Left", "Right", "Tab"]:

        return

    # Only digits
    if not event.char.isdigit():

        return "break"

    # Only one digit per box
    if len(event.widget.get()) >= 1:

        return "break"


# =====================================
# NEW PASSWORD
# =====================================

password_label = ctk.CTkLabel(main_frame, text="New Password")

password_label.pack(pady=(3, 0))

password_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

password_frame.pack(pady=(3, 3))

password_entry = ctk.CTkEntry(
    password_frame,
    width=300,
    height=45,
    corner_radius=15,
    show="*",
    placeholder_text="Enter new password",
)

password_entry.pack(side="left", padx=(0, 3))

# BLOCK COPY / PASTE

password_entry.bind("<Control-c>", lambda e: "break")

password_entry.bind("<Control-v>", lambda e: "break")

password_entry.bind("<Control-x>", lambda e: "break")

password_entry.bind("<Control-a>", lambda e: "break")

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

confirm_password_label = ctk.CTkLabel(main_frame, text="Confirm New Password")

confirm_password_label.pack()

confirm_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

confirm_frame.pack(pady=(3, 3))

confirm_password_entry = ctk.CTkEntry(
    confirm_frame,
    width=300,
    height=45,
    corner_radius=15,
    show="*",
    placeholder_text="Confirm new password",
)

confirm_password_entry.pack(side="left", padx=(0, 3))

# BLOCK COPY / PASTE

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
# LIVE EVENTS
# =====================================

password_entry.bind("<KeyRelease>", check_password_strength)

confirm_password_entry.bind("<KeyRelease>", check_confirm_password)

# =====================================
# PASSWORD POLICY
# =====================================

requirements_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

requirements_frame.pack(pady=(0, 0))

req1 = ctk.CTkLabel(
    requirements_frame, text="❌ 8 Characters", text_color="red", font=("Segoe UI", 10)
)

req1.grid(row=0, column=0, padx=5)

req2 = ctk.CTkLabel(
    requirements_frame, text="❌ Uppercase", text_color="red", font=("Segoe UI", 10)
)

req2.grid(row=0, column=1, padx=5)

req3 = ctk.CTkLabel(
    requirements_frame, text="❌ Lowercase", text_color="red", font=("Segoe UI", 10)
)

req3.grid(row=0, column=2, padx=5)

req4 = ctk.CTkLabel(
    requirements_frame, text="❌ Number", text_color="red", font=("Segoe UI", 10)
)

req4.grid(row=0, column=3, padx=5)

req5 = ctk.CTkLabel(
    requirements_frame, text="❌ Special", text_color="red", font=("Segoe UI", 10)
)

req5.grid(row=0, column=4, padx=5)

# =====================================
# PASSWORD MATCH STATUS
# =====================================

match_label = ctk.CTkLabel(main_frame, text="", font=("Segoe UI", 11, "bold"))

match_label.pack(pady=(0, 0))


# =====================================
# BUTTONS FRAME
# =====================================

buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

buttons_frame.pack(pady=(1, 1))

# =====================================
# CHANGE PASSWORD BUTTON
# =====================================

change_password_btn = ctk.CTkButton(
    buttons_frame,
    text="🔑 Change Password",
    width=190,
    height=55,
    corner_radius=18,
    font=("Segoe UI", 14, "bold"),
    fg_color="#1f6aa5",
    hover_color="#2d84c7",
    border_width=2,
    border_color="#4da6ff",
    command=change_password,
)

change_password_btn.grid(row=0, column=0, padx=(0, 10))

# =====================================
# RESEND OTP BUTTON
# =====================================

resend_btn = ctk.CTkButton(
    buttons_frame,
    text="📨 Resend OTP",
    width=190,
    height=55,
    corner_radius=18,
    font=("Segoe UI", 14, "bold"),
    fg_color="#252b35",
    hover_color="#3a3a3a",
    border_width=2,
    border_color="#4da6ff",
    command=resend_otp,
)

resend_btn.grid(row=0, column=1, padx=(10, 0))

# =====================================
# SUCCESS LABEL
# =====================================

success_label = ctk.CTkLabel(main_frame, text="", font=("Segoe UI", 12, "bold"))

success_label.pack(pady=(0, 8))

# =====================================
# BACK TO LOGIN BUTTON
# =====================================

back_btn = ctk.CTkButton(
    main_frame,
    text="⬅ Back To Login",
    width=400,
    height=50,
    corner_radius=18,
    font=("Segoe UI", 14, "bold"),
    fg_color="transparent",
    border_width=2,
    border_color="#4da6ff",
    hover_color="#10253a",
    command=back_to_login,
)

back_btn.pack(pady=(1, 1))

# =====================================
# FOOTER
# =====================================

footer_label = ctk.CTkLabel(
    main_frame,
    text="🔐 Secure Password Recovery System",
    font=("Segoe UI", 11),
    text_color="#6c6c6c",
)

footer_label.pack(side="bottom", pady=(0, 12))

# =====================================
# OTP EVENTS
# =====================================

otp1.bind("<KeyRelease>", lambda e: move_next(e, otp1, otp2))

otp2.bind("<KeyRelease>", lambda e: move_next(e, otp2, otp3))

otp3.bind("<KeyRelease>", lambda e: move_next(e, otp3, otp4))

otp4.bind("<KeyRelease>", lambda e: move_next(e, otp4, otp5))

otp5.bind("<KeyRelease>", lambda e: move_next(e, otp5, otp6))

# =====================================
# BACKSPACE
# =====================================

otp2.bind("<BackSpace>", lambda e: handle_backspace(e, otp2, otp1))

otp3.bind("<BackSpace>", lambda e: handle_backspace(e, otp3, otp2))

otp4.bind("<BackSpace>", lambda e: handle_backspace(e, otp4, otp3))

otp5.bind("<BackSpace>", lambda e: handle_backspace(e, otp5, otp4))

otp6.bind("<BackSpace>", lambda e: handle_backspace(e, otp6, otp5))


bind_arrow_keys()

# =====================================
# PASTE SUPPORT
# =====================================

for entry in otp_entries:

    entry.bind("<Control-v>", paste_otp)

    entry.bind("<Key>", allow_only_numbers)
# =====================================
# ESC SHORTCUT
# =====================================

app.bind("<Escape>", lambda e: back_to_login())


# =====================================
# RUN APP
# =====================================

app.mainloop()
