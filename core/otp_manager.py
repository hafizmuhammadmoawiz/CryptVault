import random
import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# =====================================
# OTP GENERATOR
# =====================================


def generate_otp():

    return str(random.randint(100000, 999999))


# =====================================
# SEND OTP EMAIL
# =====================================


def send_otp_email(receiver_email, otp):

    # Credentials are loaded from environment variables, never hardcoded.
    # Set these in a local .env file (see .env.example) which is git-ignored.
    sender_email = os.environ.get("CRYPTVAULT_SMTP_EMAIL")

    app_password = os.environ.get("CRYPTVAULT_SMTP_APP_PASSWORD")

    if not sender_email or not app_password:
        print(
            "OTP Error: CRYPTVAULT_SMTP_EMAIL / CRYPTVAULT_SMTP_APP_PASSWORD "
            "environment variables are not set."
        )
        return False

    subject = "CryptVault - OTP Verification"

    body = f"""
Hello,

Use this code to register on CryptVault.

Your One-Time Password (OTP) is:

=================
      {otp}
=================

This code will expire in 1 minute.

This code is valid for account verification purposes only.

Security Notice:
• Never share this OTP with anyone.
• Dev2Sec staff will never ask for your OTP.
• If you did not request this code, please ignore this email.

Thank you for choosing CryptVault.

-------------------------
Dev2Sec Team
-------------------------
"""

    try:

        message = MIMEMultipart()

        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(sender_email, app_password)

        server.send_message(message)

        server.quit()

        return True

    except Exception as error:

        print("OTP Error:", error)

        return False


# =====================================
# TESTING
# =====================================

# if __name__ == "__main__":

#   otp = generate_otp()

#  print("Generated OTP:", otp)

# result = send_otp_email("mazzkhanmastoi786@gmail.com", otp)

# print(result)
