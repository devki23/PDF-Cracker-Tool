PDF-Cracker-Tool<br>
<br>
-A Python-based tool to brute-force or dictionary-attack password-protected PDF files.<br>
<br>
Features:<br>
- Dictionary attack using a wordlist
- Brute-force attack with customizable character sets
- Multi-threaded password attempts
- Progress bar with live updates
<br> 
Files Included:<br>
<br>
- pdf_cracker.py: Main script<br>
- CP_protected.pdf: Test PDF (password: 1234)<br>
- wordlist.txt: Sample wordlist of passwords<br>
<br>
Requirements:<br>
<br>
- pikepdf Library<br>
- tqdm Library<br>
<br>
How to Run:<br>
<br>
- Dictionary Attack Command:<br>
python pdf_cracker.py CP_protected.pdf --Wordlist Wordlist.txt
<br>
- Brute-force Attack Command:<br>
python pdf_cracker.py CP_protected.pdf --generate --min-len 1 --max-len 4 --charset 1234
