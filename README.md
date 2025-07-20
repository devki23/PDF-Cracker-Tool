## PDF-Cracker-Tool
-A Python-based tool to brute-force or dictionary-attack password-protected PDF files.<br>

## Features:
- Dictionary attack using a wordlist
- Brute-force attack with customizable character sets
- Multi-threaded password attempts
- Progress bar with live updates

## Files Included:
- pdf_cracker.py: Main script
- CP_protected.pdf: Test PDF (password: 1234)
- wordlist.txt: Sample wordlist of passwords
  
## Requirements:

- pikepdf Library
- tqdm Library

## How to Run:
- Dictionary Attack Command:<br>
python pdf_cracker.py CP_protected.pdf --Wordlist Wordlist.txt<br>
- Brute-force Attack Command:<br>
python pdf_cracker.py CP_protected.pdf --generate --min-len 1 --max-len 4 --charset 1234<br>
  
## Screanshoots:
<img width="1920" height="1080" alt="Python_file_code(1)" src="https://github.com/user-attachments/assets/c20fd9b3-7d1b-4aac-8118-0e7351fdc5dc" />
<img width="1920" height="1080" alt="Python_file_code(2)" src="https://github.com/user-attachments/assets/d308f4f6-da5d-4f08-a1d4-ad0fb369e94c" />
<img width="1920" height="1080" alt="Wordlist_txt" src="https://github.com/user-attachments/assets/bc05f6a2-0d56-42ef-861f-b1eb6e663132" />
<img width="1920" height="1080" alt="Terminal_Output" src="https://github.com/user-attachments/assets/7fb94f04-a84a-4f7d-a91a-84919e0184b3" />
