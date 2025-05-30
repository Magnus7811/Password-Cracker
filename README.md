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

--------------------------------------

## How I Made This Tool? (My Development Journey)

Hey there! Ever wondered how cool computer programs are built? Well, I made this tool to crack passwords on different types of files, and it was a super fun adventure! Think of it like a detective trying to open different kinds of locked boxes (like ZIP files, PDF files, etc.). Here’s how I built it, step-by-step, with all the special tools I used:

### **1. My Main Brain: Python 3**

I used **Python 3** as the main language for building this tool. Why Python?
* **It's easy to read:** Like a storybook! It's clear, so it's simple to write and understand the "spells" (code) for the computer.
* **It has lots of helpers:** Python comes with many ready-made tools and can easily get more.

Here are some special Python helpers I used:

* **`zipfile` module:** Imagine you have a special toolbox just for ZIP files. This helper allowed my tool to peek inside ZIP files and try different passwords to unlock them.
* **`PyPDF2` library:** This is like another special toolbox, but for PDF files. It helps my tool check if a PDF is locked and then try to unlock it using passwords.
* **`itertools` module:** For the "brute-force" attack (which is like trying *every single possible* password combo!), this helper is a super-fast brain. It helps my tool quickly think of all the different password guesses without getting stuck.
* **`string` module:** This helper is like a list of all characters (like numbers, small letters, big letters, symbols). It helps my tool pick which characters to use when it's trying to guess passwords.
* **`os` and `sys` modules:** These are like my tool's hands and eyes for talking to the computer directly.
    * `os` helps with things like clearing the screen (making it neat!) or finding where files are.
    * `sys` helps my tool show messages right on the same line in your Termux screen, so you can see the progress happening live, like a speedometer!
* **`subprocess` module:** This is a *really* important one! Imagine my Python tool knows a lot, but not *everything*. For some super tricky locks (like RAR and 7z files), Python doesn't have a built-in "key." So, `subprocess` is like my tool's ability to **call other expert programs** on your computer (like big brothers or specialized locksmiths) and ask them to try unlocking those files. My tool tells the expert program what to do, and then listens to what the expert says back.

### **2. My Mobile Workshop: Termux**

I built and run this tool mostly in **Termux**. What's Termux? It's like turning your Android phone into a mini Linux computer! It lets you run powerful command-line tools and Python scripts right from your phone, which is super cool for doing cybersecurity practice anywhere.

### **3. My Expert Helpers: External Command-Line Tools**

Since Python can't do everything on its own, I used these amazing tools:

* **`unrar`:** This is the "special locksmith" I mentioned for RAR files. My Python tool calls `unrar` to do the actual unlocking attempts for RAR archives.
* **`p7zip` (`7z`/`7za`):** This is another "special locksmith" for 7z files. Just like `unrar`, my Python tool tells `7z` or `7za` what passwords to try.
* **`John the Ripper` / `Hashcat`:** For super tough locks like DOCX files, even these locksmiths are needed. My tool doesn't try to open DOCX directly, but it tells you about these *super-smart detective* tools. They are experts at finding codes for very complex locks that my Python tool can't handle alone.

### **4. How I Built It (My Plan & Choices):**

1.  **Building with LEGO Blocks (Modular Design):** Instead of making one giant block of code, I broke my tool into smaller, separate "LEGO blocks" (called functions). One block for cracking ZIPs, another for PDFs, another for handling brute-force. This makes the code neat, easier to understand, and simpler to fix or add new features later.
2.  **Making it Look Cool & Easy (User Interface - UI/UX):**
    * I wanted it to feel like a "green hacker vibe," so I used special color codes (like green for success, red for errors, yellow for warnings, and blue for info) and a cool hacker face at the start.
    * To make sure you know what's happening, especially when the tool is busy guessing passwords, I added a **dynamic progress bar**. It's like a speedometer that shows you the current password being tried right on your screen, updating constantly.
3.  **Having a Plan B (Error Handling):** What if something goes wrong? Like if you type a wrong file name or the file is broken? My tool has "Plan B" sections (called `try-except` blocks). If an error happens, it doesn't just crash. Instead, it catches the problem, tells you what went wrong in red text, and then lets you try again.
4.  **Cleaning Up My Room (Temporary File Management):** When `unrar` or `7z` try to open files, they sometimes make temporary files. My tool makes sure to create special "play areas" (temporary folders) for these files and then cleans them up automatically when the job is done, so your phone doesn't get cluttered.
5.  **Checking Your Work (Input Validation):** Before starting a long crack, my tool tries to check if you've given it good information, like if the file actually exists or if you typed a number correctly. It's like double-checking your homework before handing it in!

### **5. Tricky Parts & How I Solved Them:**

1.  **Python Couldn't Do Everything (RAR/7z):** The biggest challenge was the absence of native Python libraries for RAR and 7z archives. My Python tool didn't know how to open RAR or 7z files by itself.
    * **My Solution:** I used the `subprocess` helper to call the `unrar` and `7z` expert programs. It was like teaching my Python tool to send messages to them and understand their replies.
2.  **Showing Live Progress:** How do you make the guessing word appear right on the same line and update super fast?
    * **My Solution:** This was achieved by using `sys.stdout.write('\r' + message)` (which means "write this message, then go back to the start of the line") and `sys.stdout.flush()` (which means "show it right now!").
3.  **Brute-Force Is SO SLOW!:** Trying *every single possible password* can take millions of years for long passwords.
    * **My Solution:** While not a magic bullet, `itertools.product` was chosen for its highly optimized approach to generating combinations. I also made sure to warn users that brute-force attacks are very, very slow for longer passwords, encouraging realistic expectations.
4.  **DOCX Files Were Super Tricky:** DOCX files have very strong locks that are hard for simple programs to pick.
    * **My Solution:** Instead of trying to pick that lock myself, I decided to be helpful! My tool tells you about the *real* professional lock pickers (like John the Ripper and Hashcat) that are designed for those types of tricky locks. It gives you tips on how to use them, so you're not left stuck.

### **6. What I Learned from This Adventure:**

Building this tool taught me so much!
* **Deepened Understanding of Security Concepts:** Gained practical insight into how various file types keep their secrets locked up and the methods used in password cracking.
* **Mastery of `subprocess` Module:** Learned how to effectively make my Python programs talk to other powerful tools on the computer, a highly useful skill for automation.
* **CLI UI/UX Design:** Understood the importance of clear communication, real-time feedback, and a friendly look in command-line applications.
* **Robust Error Handling:** Learned the necessity of anticipating problems and writing resilient code that provides helpful messages instead of crashing.
* **Leveraging Open-Source Tools:** Realized how much more powerful my tool could be by integrating with other amazing free tools made by the community.

### **7. What's Next? (Future Plans for This Tool)**

Building this tool was just the beginning of my adventure! Here are some cool things I'd love to add or improve in the future:

* **More Types of Locked Boxes:** Right now, my tool can tackle ZIP, PDF, RAR, and 7z. But there are many other kinds of locked files out there! I want to teach it how to open more types of encrypted documents or archives.
* **Making it Super Speedy:** For brute-force attacks (trying every single password), it can sometimes take a very, very long time. I want to explore ways to make the tool faster, maybe by teaching it to try many, many passwords all at the same time (like having many helpers working together, or using a very fast helper if my computer has one!).
* **Smarter Guessing:** Instead of just trying words from a list or random combinations, I want to teach my tool to guess "smarter." This means it could try common patterns people use in passwords, or cleverly change words (like adding numbers to the end), which might help it find passwords quicker.
* **Directly Grabbing Secret Hints:** For files like DOCX, we currently need a separate expert tool to pull out the "secret hint" (hash) first. I'd love to make my tool smart enough to grab those hints directly, so it's a one-stop-shop for cracking!
* **A Button-Clicker Version:** Right now, you use my tool by typing commands in Termux. Maybe one day, I could make a version with buttons and windows (what we call a Graphical User Interface, or GUI) so it's even easier for everyone to use, even without typing commands!

--------------------------------------

## Disclaimer

This tool is mobile friendly and intended for educational purposes and ethical penetration testing ONLY. Do not use it on systems or files for which you do not have explicit permission. Unauthorized access to computer systems is illegal and punishable by law. The developer is not responsible for any misuse.

