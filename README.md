# Termux-Password-Cracker (Infosec Piyush) 🔥

A versatile Mobile friendly Python-based command-line tool for cracking passwords of various encrypted file types (ZIP, PDF, RAR, 7z) within the Termux environment. It supports both wordlist and brute-force attack modes, providing a "green hacker vibe" UI experience.

## Features

* **Multi-format Support:** Cracks ZIP, PDF, RAR, and 7z archives.
* **Attack Modes:**
    * **Wordlist Attack:** Faster, uses a list of common passwords.
    * **Brute-force Attack:** Comprehensive, generates passwords based on character sets and length (can be very slow).
* **User-Friendly Interface:** Clear, color-coded prompts and status updates.
* **Dynamic Progress:** Shows real-time cracking attempts.
* **DOCX Guidance:** Provides information on external tools (John the Ripper, Hashcat) for DOCX file cracking.

## Requirements

* Python 3 (comes pre-installed with Termux)
* `PyPDF2` (for PDF cracking)
* `unrar` command-line tool (for RAR cracking)
* `p7zip` (providing `7z` or `7za` command-line tools for 7z cracking)

## Installation

1.  **Install Termux:** Download from F-Droid or Google Play Store.
2.  **Update Termux Packages:**
    ```bash
    pkg update && pkg upgrade
    ```
3.  **Install Python and Git:**
    ```bash
    pkg install python git
    ```
4.  **Install Required Python Libraries:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Install External Tools (for RAR/7z/DOCX features):**
    ```bash
    # For RAR files
    pkg install unrar

    # For 7z files
    pkg install p7zip

    # For DOCX (Hash & Crack) - Recommended:
    pkg install john # Provides office2john utility
    # Or install Hashcat if preferred (more complex install in Termux)
    ```
6.  **Clone the Repository (or place `f8.py` in a directory):**
    If you're cloning this project:
    ```bash
    git clone [https://github.com/Magnus7811/Termux-Password-Cracker.git](https://github.com/Magnus7811/Termux-Password-Cracker.git)
    cd Termux-Password-Cracker
    ```
    If you're just putting your `crack.py` here, ensure it's in this folder.

## Usage

1.  Navigate to the project directory:
    ```bash
    cd Termux-Password-Cracker
    ```
2.  Run the script:
    ```bash
    python crack.py
    ```
3.  Follow the on-screen prompts to select file type, attack mode, and provide paths.

## Disclaimer

This tool is mobile friendly and intended for educational purposes and ethical penetration testing ONLY. Do not use it on systems or files for which you do not have explicit permission. Unauthorized access to computer systems is illegal and punishable by law. The developer is not responsible for any misuse.

