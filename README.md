# CryptVault

CryptVault is a desktop application (built with Python and CustomTkinter) for securely storing private files. Instead of keeping your sensitive documents in plain form, CryptVault encrypts every file you upload and gives you back an encryption key — the file itself is never stored in a readable form, and not even the app/database keeps a copy of your key.

## How It Works

1. **Register / Login** — Create an account or log in. Registration and password recovery are protected with email OTP (One-Time Password) verification.
2. **Upload a File** — From your dashboard, upload any file you want to protect.
3. **Encryption** — CryptVault encrypts the file using the `cryptography` library and generates a unique key for it.
4. **You Keep the Key** — The generated `.key` file (paired with the encrypted `.enc` file) is given to you to store safely (e.g. on a USB drive, password manager, etc.). CryptVault does not retain a usable copy of your key.
5. **Retrieve Later** — To get your original file back, provide both the `.enc` file and its matching `.key` file, and CryptVault decrypts it back to the original.

This design means that even someone with full access to the server/database cannot read your files without the key that only you hold.

## Features

- User registration, login, and OTP-based email verification
- Forgot-password flow with OTP re-verification
- File encryption and decryption with per-file keys
- User dashboard (upload, view, manage your own encrypted files)
- Admin dashboard (user/account oversight)
- File integrity verification
- Extra security utilities: password generator, hash identifier, password-strength/attack simulation tools

## Tech Stack

- **Python 3**
- **CustomTkinter** — desktop GUI
- **cryptography** — file encryption/decryption
- **bcrypt** — password hashing
- **SQLite** — local database (users, files, logs, security events)
- **smtplib** — OTP delivery via email

## Project Structure

```
SecureVaultFile/
├── main.py                  # Entry point
├── core/                    # Authentication and OTP logic
├── gui/                     # All application screens (login, dashboards, tools, etc.)
├── database/                # SQLite database + database manager
├── assets/                  # Images/icons used by the GUI
├── vault/                   # Encrypted files land here at runtime
├── backups/                 # Backup storage used at runtime
└── requirements.txt
```

## Setup

1. Clone the repository and move into the project folder:
   ```
   git clone <your-repo-url>
   cd SecureVaultFile
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure email OTP sending. Copy `.env.example` to `.env` and fill in a Gmail address plus a Gmail **App Password** (not your normal password — generate one at https://myaccount.google.com/apppasswords):
   ```
   cp .env.example .env
   ```

4. Run the app from the project's root folder:
   ```
   python main.py
   ```

   The SQLite database is created automatically on first run.

## Security Notes

- Passwords are never stored in plain text — they are hashed with `bcrypt` before being saved.
- SMTP credentials for sending OTP emails are read from environment variables (`.env`), never hardcoded in source.
- Encryption keys are handed to the user and are not retained anywhere else in the system — losing your `.key` file means the encrypted file cannot be recovered.

## Disclaimer

This project was built as a learning/portfolio project to practice applied cryptography, secure authentication flows, and desktop application development. It has not undergone a professional security audit and should not be used to protect real sensitive data in production without further review.
