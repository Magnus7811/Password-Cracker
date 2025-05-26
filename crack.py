import zipfile
import os
import itertools
import string
import time
import PyPDF2
import subprocess
import sys

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Prints a stylish banner with your name and a hacker emoji."""
    clear_screen()
    print("\n" + "="*50)
    print("       ____    _____       _        ____    _  __  ")
    print("      / ___|  |  _ ||     / \      / ___|  | |/ /  ")               
    print("     | |      | |_)||    / _ \    | |      | |</   ")
    print("     | |___   |  _ <\   / ___ \   |_|___   | |\<\  ")
    print("      \___/   |_|  \_| /_/   \_\  \_____|  |_| \_\ ")
    print("\n" +"🔥 INFOSEC PIYUSH - CRACK PASSWORD USING CRACKER 🔥")
    print("    Your friendly neighborhood password buster.")
    print("="*50 + "\n")  
    time.sleep(1)  # Small pause for dramatic effect


def crack_zip_with_wordlist(zip_path, wordlist_path):
    """Attempts to crack a ZIP file using a wordlist."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            print(f"[*] Starting wordlist attack on ZIP file: {zip_path}")
            start_time = time.time()
            with open(wordlist_path, 'r', errors='ignore') as f_zip:
                for line_num, line in enumerate(f_zip, 1):
                    password = line.strip()
                    # Added a visual indicator for progress
                    if line_num % 1000 == 0:
                        sys.stdout.write(f"\r[*] Trying {line_num} passwords... Current: '{password}'")
                        sys.stdout.flush()
                    try:
                        zf.extractall(pwd=bytes(password, 'utf-8'))
                        end_time = time.time()
                        print(f"\n[+] Password found from wordlist for ZIP: {password}")
                        print(f"[+] Attempted {line_num} passwords.")
                        print(f"[+] Time taken: {end_time - start_time:.2f} seconds.")
                        return
                    except (RuntimeError, zipfile.BadZipFile):
                        pass
                    except Exception as e:
                        # Log unexpected errors for debugging
                        # print(f"[-] An unexpected error occurred with password '{password}': {e}")
                        pass
            print("\n[-] Password not found in wordlist for ZIP.")
    except FileNotFoundError:
        print(f"[!] ZIP file not found at: {zip_path}")
    except zipfile.BadZipFile:
        print(f"[!] The file at {zip_path} is not a valid ZIP file or is corrupted.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

def brute_force_zip(zip_path, max_length=4, charset_type='alphanumeric'):
    """Attempts to brute-force a ZIP file with specified character set and max length."""
    charset_map = {
        'numeric': string.digits,
        'lowercase_alpha': string.ascii_lowercase,
        'uppercase_alpha': string.ascii_uppercase,
        'alpha': string.ascii_letters,
        'alphanumeric': string.ascii_letters + string.digits,
        'all_printable': string.ascii_letters + string.digits + string.punctuation
    }
    chars = charset_map.get(charset_type, string.ascii_letters + string.digits) # Default to alphanumeric

    print(f"[*] Starting brute-force for ZIP with charset: '{chars}' and max length: {max_length}")

    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            start_time = time.time()
            attempt_count = 0
            for length in range(1, max_length + 1):
                print(f"[*] Trying passwords of length {length} for ZIP...")
                for attempt in itertools.product(chars, repeat=length):
                    password = ''.join(attempt)
                    attempt_count += 1
                    # Added a visual indicator for progress
                    if attempt_count % 10000 == 0: # Update less frequently for brute-force as it's slower
                        sys.stdout.write(f"\r[*] Total attempts: {attempt_count}... Current: '{password}'")
                        sys.stdout.flush()
                    try:
                        zf.extractall(pwd=bytes(password, 'utf-8'))
                        end_time = time.time()
                        print(f"\n[+] Password found by brute-force for ZIP: {password}")
                        print(f"[+] Total attempts: {attempt_count}")
                        print(f"[+] Time taken: {end_time - start_time:.2f} seconds.")
                        return
                    except (RuntimeError, zipfile.BadZipFile):
                        pass
                    except Exception as e:
                        pass
            print(f"\n[-] Brute-force failed for ZIP. Password not found within max length {max_length}.")
            print(f"[-] Total attempts made: {attempt_count}")
    except FileNotFoundError:
        print(f"[!] ZIP file not found at: {zip_path}")
    except zipfile.BadZipFile:
        print(f"[!] The file at {zip_path} is not a valid ZIP file or is corrupted.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

def crack_pdf_with_wordlist(pdf_path, wordlist_path):
    """Attempts to crack a PDF file using a wordlist."""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            if not pdf_reader.is_encrypted:
                print("[!] PDF is not encrypted. No password needed.")
                return

            print(f"[*] Starting wordlist attack on PDF file: {pdf_path}")
            start_time = time.time()
            with open(wordlist_path, 'r', errors='ignore') as f_pdf:
                for line_num, line in enumerate(f_pdf, 1):
                    password = line.strip()
                    # Added a visual indicator for progress
                    if line_num % 500 == 0:
                        sys.stdout.write(f"\r[*] Trying {line_num} passwords... Current: '{password}'")
                        sys.stdout.flush()
                    try:
                        if pdf_reader.decrypt(password):
                            end_time = time.time()
                            print(f"\n[+] Password found from wordlist for PDF: {password}")
                            print(f"[+] Attempted {line_num} passwords.")
                            print(f"[+] Time taken: {end_time - start_time:.2f} seconds.")
                            return
                    except PyPDF2.errors.FileNotDecryptedError:
                        pass
                    except Exception as e:
                        pass
            print("\n[-] Password not found in wordlist for PDF.")
    except FileNotFoundError:
        print(f"[!] PDF file not found at: {pdf_path}")
    except PyPDF2.errors.PdfReadError:
        print(f"[!] The file at {pdf_path} is not a valid PDF or is corrupted.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

def brute_force_pdf(pdf_path, max_length=4, charset_type='alphanumeric'):
    """Attempts to brute-force a PDF file with specified character set and max length."""
    charset_map = {
        'numeric': string.digits,
        'lowercase_alpha': string.ascii_lowercase,
        'uppercase_alpha': string.ascii_uppercase,
        'alpha': string.ascii_letters,
        'alphanumeric': string.ascii_letters + string.digits,
        'all_printable': string.ascii_letters + string.digits + string.punctuation
    }
    chars = charset_map.get(charset_type, string.ascii_letters + string.digits)

    print(f"[*] Starting brute-force for PDF with charset: '{chars}' and max length: {max_length}")

    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            if not pdf_reader.is_encrypted:
                print("[!] PDF is not encrypted. No password needed.")
                return

            start_time = time.time()
            attempt_count = 0
            for length in range(1, max_length + 1):
                print(f"[*] Trying passwords of length {length} for PDF...")
                for attempt in itertools.product(chars, repeat=length):
                    password = ''.join(attempt)
                    attempt_count += 1
                    # Added a visual indicator for progress
                    if attempt_count % 10000 == 0:
                        sys.stdout.write(f"\r[*] Total attempts: {attempt_count}... Current: '{password}'")
                        sys.stdout.flush()
                    try:
                        if pdf_reader.decrypt(password):
                            end_time = time.time()
                            print(f"\n[+] Password found by brute-force for PDF: {password}")
                            print(f"[+] Total attempts: {attempt_count}")
                            print(f"[+] Time taken: {end_time - start_time:.2f} seconds.")
                            return
                    except PyPDF2.errors.FileNotDecryptedError:
                        pass
                    except Exception as e:
                        pass
            print(f"\n[-] Brute-force failed for PDF. Password not found within max length {max_length}.")
            print(f"[-] Total attempts made: {attempt_count}")
    except FileNotFoundError:
        print(f"[!] PDF file not found at: {pdf_path}")
    except PyPDF2.errors.PdfReadError:
        print(f"[!] The file at {pdf_path} is not a valid PDF or is corrupted.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

def check_unrar_installed():
    """Checks if the 'unrar' command-line tool is installed."""
    try:
        subprocess.run(['unrar', '--version'], capture_output=True, check=True, text=True, timeout=5)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return False

def crack_rar_with_wordlist(rar_path, wordlist_path):
    """Attempts to crack a RAR file using a wordlist (requires unrar)."""
    if not check_unrar_installed():
        print("[!] 'unrar' command-line tool not found. Please install it.")
        print("    In Termux: 'pkg install unrar'")
        print("    On Debian/Ubuntu: 'sudo apt-get install unrar'")
        print("    On Fedora: 'sudo dnf install unrar'")
        return

    print(f"[*] Starting wordlist attack for RAR file: {rar_path}")
    try:
        start_time = time.time()
        # Create a temporary directory for extraction to avoid clutter
        temp_dir = os.path.join(os.path.dirname(rar_path), "unrar_temp")
        os.makedirs(temp_dir, exist_ok=True)

        with open(wordlist_path, 'r', errors='ignore') as f_rar:
            for line_num, line in enumerate(f_rar, 1):
                password = line.strip()
                # Added a visual indicator for progress
                if line_num % 100 == 0: # RAR cracking can be slower
                    sys.stdout.write(f"\r[*] Trying {line_num} passwords... Current: '{password}'")
                    sys.stdout.flush()

                # Use 'e' (extract to current directory, ignoring paths) instead of 'x' for cleaner temp extraction
                command = ['unrar', 'e', '-p' + password, '-o-', rar_path, temp_dir + os.sep]
                # -o- : Don't overwrite existing files
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=False, timeout=10)
                    # RAR success messages can vary, check for common indicators
                    if "All OK" in result.stdout or "Extracting from" in result.stdout and result.returncode == 0:
                        end_time = time.time()
                        print(f"\n[+] Password found from wordlist for RAR: {password}")
                        print(f"[+] Attempted {line_num} passwords.")
                        print(f"[+] Time taken: {end_time - start_time:.2f} seconds.")
                        # Clean up the temporary directory if successful
                        if os.path.exists(temp_dir):
                            os.system(f'rm -rf "{temp_dir}"') # Using os.system for broader compatibility
                        return
                except subprocess.TimeoutExpired:
                    # print(f"[-] Command timed out for password: {password}") # Uncomment for verbose error checking
                    pass
                except Exception as e:
                    # print(f"[-] An unexpected error occurred: {e}") # Uncomment for verbose error checking
                    pass
        print("\n[-] Password not found in wordlist for RAR.")
        if os.path.exists(temp_dir):
            os.system(f'rm -rf "{temp_dir}"')
    except FileNotFoundError:
        print(f"[!] RAR file not found at: {rar_path}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")
        if os.path.exists(temp_dir):
            os.system(f'rm -rf "{temp_dir}"')

def brute_force_rar(rar_path, max_length=4, charset_type='alphanumeric'):
    """Attempts to brute-force a RAR file (requires unrar)."""
    if not check_unrar_installed():
        print("[!] 'unrar' command-line tool not found. Please install it.")
        print("    In Termux: 'pkg install unrar'")
        print("    On Debian/Ubuntu: 'sudo apt-get install unrar'")
        print("    On Fedora: 'sudo dnf install unrar'")
        return

    charset_map = {
        'numeric': string.digits,
        'lowercase_alpha': string.ascii_lowercase,
        'uppercase_alpha': string.ascii_uppercase,
        'alpha': string.ascii_letters,
        'alphanumeric': string.ascii_letters + string.digits,
        'all_printable': string.ascii_letters + string.digits + string.punctuation
    }
    chars = charset_map.get(charset_type, string.ascii_letters + string.digits)

    print(f"[*] Starting brute-force for RAR with charset: '{chars}' and max length: {max_length}")

    try:
        start_time = time.time()
        attempt_count = 0
        temp_dir = os.path.join(os.path.dirname(rar_path), "unrar_temp")
        os.makedirs(temp_dir, exist_ok=True)

        for length in range(1, max_length + 1):
            print(f"[*] Trying passwords of length {length} for RAR...")
            for attempt in itertools.product(chars, repeat=length):
                password = ''.join(attempt)
                attempt_count += 1
                # Added a visual indicator for progress
                if attempt_count % 5000 == 0:
                    sys.stdout.write(f"\r[*] Total attempts: {attempt_count}... Current: '{password}'")
                    sys.stdout.flush()

                command = ['unrar', 'e', '-p' + password, '-o-', rar_path, temp_dir + os.sep]
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=False, timeout=10)
                    if "All OK" in result.stdout or "Extracting from" in result.stdout and result.returncode == 0:
                        end_time = time.time()
                        print(f"\n[+] Password found by brute-force for RAR: {password}")
                        print(f"[+] Total attempts: {attempt_count}")
                        print(f"[+] Time taken: {end_time - start_time:.2f} seconds.")
                        if os.path.exists(temp_dir):
                            os.system(f'rm -rf "{temp_dir}"')
                        return
                except subprocess.TimeoutExpired:
                    pass
                except Exception as e:
                    pass
        print(f"\n[-] Brute-force failed for RAR. Password not found within max length {max_length}.")
        print(f"[-] Total attempts made: {attempt_count}")
        if os.path.exists(temp_dir):
            os.system(f'rm -rf "{temp_dir}"')
    except FileNotFoundError:
        print(f"[!] RAR file not found at: {rar_path}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")
        if os.path.exists(temp_dir):
            os.system(f'rm -rf "{temp_dir}"')

def check_7z_installed():
    """Checks if either '7z' or '7za' command-line tool is installed."""
    try:
        subprocess.run(['7z', '--help'], capture_output=True, check=True, text=True, timeout=5)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        try:
            subprocess.run(['7za', '--help'], capture_output=True, check=True, text=True, timeout=5)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            return False

def get_7z_command():
    """Returns the correct 7z command ('7z' or '7za')."""
    try:
        subprocess.run(['7z', '--help'], capture_output=True, check=True, text=True, timeout=5)
        return '7z'
    except:
        return '7za'

def crack_7z_with_wordlist(sevenz_path, wordlist_path):
    """Attempts to crack a 7z file using a wordlist (requires 7z or 7za)."""
    if not check_7z_installed():
        print("[!] '7z' or '7za' command-line tool not found. Please install 'p7zip'.")
        print("    In Termux: 'pkg install p7zip'")
        print("    On Debian/Ubuntu: 'sudo apt-get install p7zip-full'")
        print("    On Fedora: 'sudo dnf install p7zip p7zip-plugins'")
        return

    _7z_cmd = get_7z_command()
    print(f"[*] Starting wordlist attack for 7z file: {sevenz_path}")
    try:
        start_time = time.time()
        temp_dir = os.path.join(os.path.dirname(sevenz_path), "7z_temp")
        os.makedirs(temp_dir, exist_ok=True)

        with open(wordlist_path, 'r', errors='ignore') as f_7z:
            for line_num, line in enumerate(f_7z, 1):
                password = line.strip()
                # Added a visual indicator for progress
                if line_num % 100 == 0:
                    sys.stdout.write(f"\r[*] Trying {line_num} passwords... Current: '{password}'")
                    sys.stdout.flush()

                # -aoa: Overwrite all existing files without prompt
                command = [_7z_cmd, 'x', sevenz_path, f'-o{temp_dir}', '-p' + password, '-aoa']
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=False, timeout=10)
                    # 7z typically returns 0 on success and "Everything is Ok" in stdout
                    if result.returncode == 0 and "Everything is Ok" in result.stdout:
                        end_time = time.time()
                        print(f"\n[+] Password found from wordlist for 7z: {password}")
                        print(f"[+] Attempted {line_num} passwords.")
                        print(f"[+] Time taken: {end_time - start_time:.2f} seconds.")
                        if os.path.exists(temp_dir):
                            os.system(f'rm -rf "{temp_dir}"')
                        return
                except subprocess.TimeoutExpired:
                    pass
                except Exception as e:
                    pass
        print("\n[-] Password not found in wordlist for 7z.")
        if os.path.exists(temp_dir):
            os.system(f'rm -rf "{temp_dir}"')
    except FileNotFoundError:
        print(f"[!] 7z file not found at: {sevenz_path}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")
        if os.path.exists(temp_dir):
            os.system(f'rm -rf "{temp_dir}"')

def brute_force_7z(sevenz_path, max_length=4, charset_type='alphanumeric'):
    """Attempts to brute-force a 7z file (requires 7z or 7za)."""
    if not check_7z_installed():
        print("[!] '7z' or '7za' command-line tool not found. Please install 'p7zip'.")
        print("    In Termux: 'pkg install p7zip'")
        print("    On Debian/Ubuntu: 'sudo apt-get install p7zip-full'")
        print("    On Fedora: 'sudo dnf install p7zip p7zip-plugins'")
        return

    _7z_cmd = get_7z_command()
    charset_map = {
        'numeric': string.digits,
        'lowercase_alpha': string.ascii_lowercase,
        'uppercase_alpha': string.ascii_uppercase,
        'alpha': string.ascii_letters,
        'alphanumeric': string.ascii_letters + string.digits,
        'all_printable': string.ascii_letters + string.digits + string.punctuation
    }
    chars = charset_map.get(charset_type, string.ascii_letters + string.digits)

    print(f"[*] Starting brute-force for 7z with charset: '{chars}' and max length: {max_length}")

    try:
        start_time = time.time()
        attempt_count = 0
        temp_dir = os.path.join(os.path.dirname(sevenz_path), "7z_temp")
        os.makedirs(temp_dir, exist_ok=True)

        for length in range(1, max_length + 1):
            print(f"[*] Trying passwords of length {length} for 7z...")
            for attempt in itertools.product(chars, repeat=length):
                password = ''.join(attempt)
                attempt_count += 1
                # Added a visual indicator for progress
                if attempt_count % 5000 == 0:
                    sys.stdout.write(f"\r[*] Total attempts: {attempt_count}... Current: '{password}'")
                    sys.stdout.flush()

                command = [_7z_cmd, 'x', sevenz_path, f'-o{temp_dir}', '-p' + password, '-aoa']
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=False, timeout=10)
                    if result.returncode == 0 and "Everything is Ok" in result.stdout:
                        end_time = time.time()
                        print(f"\n[+] Password found by brute-force for 7z: {password}")
                        print(f"[+] Total attempts: {attempt_count}")
                        print(f"[+] Time taken: {end_time - start_time:.2f} seconds.")
                        if os.path.exists(temp_dir):
                            os.system(f'rm -rf "{temp_dir}"')
                        return
                except subprocess.TimeoutExpired:
                    pass
                except Exception as e:
                    pass
        print(f"\n[-] Brute-force failed for 7z. Password not found within max length {max_length}.")
        print(f"[-] Total attempts made: {attempt_count}")
        if os.path.exists(temp_dir):
            os.system(f'rm -rf "{temp_dir}"')
    except FileNotFoundError:
        print(f"[!] 7z file not found at: {sevenz_path}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")
        if os.path.exists(temp_dir):
            os.system(f'rm -rf "{temp_dir}"')

def crack_docx_info():
    """Provides information on cracking DOCX files."""
    print("\n--- DOCX File Cracking Information ---")
    print("[!] Cracking DOCX files is significantly more complex than ZIP/PDF/RAR/7z.")
    print("    Microsoft Office documents (DOCX, XLSX, PPTX) use robust encryption.")
    print("    Direct password cracking with Python libraries is generally not feasible.")
    print("\n[Hacker Tip]: For DOCX files, you typically need a multi-stage approach:")
    print("    1.  **Extract the hash:** Use tools like `office2john` (from John the Ripper suite) or `hashcat` utilities.")
    print("        Example: `python office2john.py protected.docx > docx_hash.txt`")
    print("    2.  **Crack the hash:** Use powerful, GPU-accelerated cracking tools.")
    print("        -   **Hashcat:** Industry standard for hash cracking. It supports various attack modes (wordlist, brute-force, mask).")
    print("            Example: `hashcat -m 9600 -a 0 docx_hash.txt wordlist.txt` (for Office 2007-2013) or `-m 9700` (for Office 2016+)")
    print("        -   **John the Ripper (JtR):** Another excellent, versatile cracker.")
    print("            Example: `john --wordlist=wordlist.txt docx_hash.txt`")
    print("\n[!] This tool can't directly crack DOCX passwords, but it can guide you!")
    print("    Please install John the Ripper or Hashcat for DOCX cracking.")
    print("    (e.g., 'pkg install john' in Termux for John the Ripper)")
    print("---------------------------------------\n")
    input("Press Enter to return to the main menu...") # Keep the message on screen until user acknowledges

if __name__ == "__main__":
    while True:
        print_banner()
        print("Select Target File Type:")
        print("1. ZIP File")
        print("2. PDF File")
        print("3. RAR File (Requires 'unrar' tool)")
        print("4. 7z File (Requires '7z' or '7za' tool)")
        print("5. DOCX File (Info on external tools)")
        print("0. Exit")

        file_type_choice = input("\nEnter choice (0-5): ").strip()

        if file_type_choice == '0':
            print("\n[+] Exiting. Stay safe out there, Infosec Piyush!")
            break

        if file_type_choice == '5':
            crack_docx_info()
            continue # Go back to main menu after showing DOCX info

        file_path = input("Enter file path: ").strip()

        if not os.path.exists(file_path):
            print("[!] File not found. Please check the path and try again.")
            time.sleep(2)
            continue

        print("\nSelect Attack Mode:")
        print("1. Wordlist Attack (Fastest if you have a good wordlist)")
        print("2. Brute-force Attack (Can be very slow, but guarantees a find if length/charset is right)")
        mode = input("Enter choice (1/2): ").strip()

        wordlist_path = ""
        max_len = 0
        selected_charset = ""

        if mode == '1':
            wordlist_path = input("Enter wordlist path: ").strip()
            if not os.path.exists(wordlist_path):
                print("[!] Wordlist not found. Please check the path and try again.")
                time.sleep(2)
                continue
        elif mode == '2':
            print("\nSelect Brute-force Character Set:")
            print("1. Numeric (0-9)")
            print("2. Lowercase Alphabetic (a-z)")
            print("3. Uppercase Alphabetic (A-Z)")
            print("4. All Alphabetic (a-zA-Z)")
            print("5. Alphanumeric (a-zA-Z0-9) - Recommended for general use")
            print("6. All Printable (a-zA-Z0-9 and common symbols like !@#$) - Very slow!")
            charset_choice = input("Enter choice (1-6): ").strip()

            charset_map = {
                '1': 'numeric', '2': 'lowercase_alpha', '3': 'uppercase_alpha',
                '4': 'alpha', '5': 'alphanumeric', '6': 'all_printable'
            }
            selected_charset = charset_map.get(charset_choice)

            if not selected_charset:
                print("[!] Invalid character set choice. Please select from 1-6.")
                time.sleep(2)
                continue

            try:
                max_len_str = input("Enter max password length (e.g., 4, be realistic!): ").strip()
                max_len = int(max_len_str)
                if max_len <= 0:
                    print("[!] Max password length must be a positive integer.")
                    time.sleep(2)
                    continue
                if max_len > 8 and selected_charset in ['alpha', 'alphanumeric', 'all_printable']:
                    print("[!] Warning: Max length > 8 with complex charsets can take a very long time!")
                    if input("   Are you sure you want to continue? (y/n): ").lower() != 'y':
                        continue
            except ValueError:
                print("[!] Invalid input for max password length. Please enter a number.")
                time.sleep(2)
                continue
        else:
            print("[!] Invalid attack mode choice. Please select 1 or 2.")
            time.sleep(2)
            continue

        print("\n[*] Commencing attack sequence...\n")
        time.sleep(1)

        # Execute the chosen cracking function
        if file_type_choice == '1': # ZIP
            if mode == '1':
                crack_zip_with_wordlist(file_path, wordlist_path)
            else:
                brute_force_zip(file_path, max_len, selected_charset)
        elif file_type_choice == '2': # PDF
            if mode == '1':
                crack_pdf_with_wordlist(file_path, wordlist_path)
            else:
                brute_force_pdf(file_path, max_len, selected_charset)
        elif file_type_choice == '3': # RAR
            if mode == '1':
                crack_rar_with_wordlist(file_path, wordlist_path)
            else:
                brute_force_rar(file_path, max_len, selected_charset)
        elif file_type_choice == '4': # 7z
            if mode == '1':
                crack_7z_with_wordlist(file_path, wordlist_path)
            else:
                brute_force_7z(file_path, max_len, selected_charset)
        
        print("\n--- Attack sequence complete ---")
        input("Press Enter to return to the main menu...") # Pause before clearing for next menu iteration

