# 🔐 CryptVault

**A desktop file vault that encrypts your private files and hands the encryption key only to you — not even the app keeps a copy.**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Encryption](https://img.shields.io/badge/Encryption-Fernet-2E7D32?style=flat-square&logo=letsencrypt&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-1f6feb?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

> ⚠️ **Project Status:** CryptVault is a work in progress, not a finished product. The core vault (register/login, OTP verification, file encryption & decryption, and the security tools) is functional and shown below. It's being built alongside an internship, so development is currently paused while that takes priority — more features (like the Admin dashboard) are planned as work continues.

---

## 📖 Table of Contents

- [Why CryptVault?](#-why-cryptvault)
- [How It Works](#-how-it-works)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Security Notes](#-security-notes)
- [Roadmap](#-roadmap)
- [Disclaimer](#-disclaimer)
- [License](#-license)

---

## 🎯 Why CryptVault?

We all have files — documents, IDs, personal photos — that we'd rather no one else could open, even if our computer or an online backup were ever compromised. Most "secure storage" tools still trust *someone else* (the app, the vendor, the cloud) to hold the key that can unlock your data.

CryptVault takes a simpler, zero-trust approach: **it encrypts the file and gives the key to you, and only you.** The app itself never stores a usable copy of it. Lose the key, and neither CryptVault nor anyone else can open the file — which is exactly the point.

## 🔄 How It Works

1. **Upload a file** from your dashboard.
2. **Fernet encryption runs locally** (AES-128-CBC + HMAC-SHA256, from Python's `cryptography` library).
3. Two outputs are created:
   - `file.enc` — the encrypted file (safe to store anywhere)
   - `file.key` — the one and only key that can unlock it
4. **You save `file.key` yourself** (USB drive, password manager, etc.) — CryptVault does **not** keep a copy.
5. To get your file back later, provide both `file.enc` and `file.key` — CryptVault decrypts it back to the original.

## ✨ Features

**Authentication & Account Security**
- Register / Login with client-side password strength checks (length, upper/lower case, number, special character)
- Email OTP (One-Time Password) verification on registration, with expiry
- Forgot-password flow, also protected by OTP re-verification

**Core Vault**
- Per-file encryption (Fernet: AES-128-CBC + HMAC-SHA256 authentication) with a uniquely generated key for every file
- Decryption requires both the encrypted file **and** its matching key file
- "My Files" tracker — see each file's original path, encrypted path, key path, size, and encryption status at a glance

**Built-in Security Tools**
- 🔑 **Password Generator** — customizable length & character sets, with entropy shown
- 🛡️ **Password Attack Simulator** — estimates brute-force time and checks resistance to dictionary/hybrid attacks
- 🧬 **File Integrity Verifier** — generate and verify SHA-256 hashes to detect if a file has been altered
- 🔍 **Hash Identifier** — detects the algorithm behind a hash string (MD5, SHA-1, SHA-256, SHA-512)

## 📸 Screenshots

### 🔐 Login
![Login](./screenshots/login_Page.png)

### 📝 Register
![Register](./screenshots/Register_Page.png)

### 📧 Email OTP Verification
![Email OTP Verification](./screenshots/Registration_OTP.png)

### ✉️ OTP Email
![OTP Email](./screenshots/OTP_Email.png)

### 🔑 Forgot Password
![Forgot Password](./screenshots/Forgot_Page.png)

### 🖥️ User Dashboard
![User Dashboard](./screenshots/User_Dashboard.png)

### 🔒 Encrypt a File
![Encrypt a File](./screenshots/Encryption_Page.png)

### 🔓 Decrypt a File
![Decrypt a File](./screenshots/Decryption_Page.png)

### 📁 My Files
![My Files](./screenshots/My_File.png)

### 🛡️ Security Tools Suite
![Security Tools Suite](./screenshots/Security_Tools.png)

### 🔨 Password Attack Simulator
![Password Attack Simulator](./screenshots/Password_Attack_Simulation.png)

### 🔐 Password Generator
![Password Generator](./screenshots/Password_Generator.png)

### 🧬 File Integrity Verifier
![File Integrity Verifier](./screenshots/File_Integrity.png)

### 🔍 Hash Identifier
![Hash Identifier](./screenshots/HASH_Identifier.png)

## 🛠 Tech Stack

| Layer                | Technology                                          |
| -------------------- | --------------------------------------------------- |
| Language             | Python 3                                            |
| GUI                  | CustomTkinter                                       |
| Encryption           | `cryptography` (Fernet — AES-128-CBC + HMAC-SHA256) |
| Password Hashing     | `bcrypt`                                            |
| Database             | SQLite                                              |
| Email / OTP Delivery | `smtplib`                                           |

## 📂 Project Structure

```
SecureVaultFile/
├── main.py                  # Entry point
├── core/                    # Authentication and OTP logic
├── gui/                     # All application screens
├── database/                # SQLite database + database manager
├── assets/                  # Images/icons used by the GUI
├── screenshots/             # README screenshots
├── vault/                   # Encrypted files land here at runtime
├── backups/                 # Backup storage used at runtime
├── .env.example             # Template for required environment variables
└── requirements.txt
```

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/CryptVault.git
   cd CryptVault
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure email OTP delivery**

   Copy the example environment file and fill in your own credentials:
   ```bash
   cp .env.example .env
   ```
   You'll need a Gmail address and a Gmail **App Password** (not your normal password) — generate one at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).

4. **Run the app**
   ```bash
   python main.py
   ```
   The SQLite database is created automatically on first run.

## 🔒 Security Notes

- Passwords are **never** stored in plain text — they're hashed with `bcrypt`.
- SMTP credentials are read from environment variables via `.env`, never hardcoded in source.
- Encryption keys are handed to the user and are **not** retained anywhere else — there is no "reset my key" option, by design.

## 🗺 Roadmap

- [ ] Complete the Admin dashboard
- [ ] 2FA (TOTP) support — schema already in place in the database
- [ ] Packaged executable (no Python install required)
- [ ] Automated tests for the encryption/decryption core

## ⚠️ Disclaimer

CryptVault is a personal learning/portfolio project built to practice applied cryptography, secure authentication flows, and desktop app development. It is **still under active development** and has not undergone a professional security audit — it should not be relied on to protect real sensitive data in production.

## 📄 License

Licensed under the [MIT License](LICENSE).
