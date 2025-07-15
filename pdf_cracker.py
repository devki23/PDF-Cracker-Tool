import argparse
import itertools
import string
from concurrent.futures import ThreadPoolExecutor, as_completed

import pikepdf
from pikepdf import PasswordError  
from tqdm import tqdm

def generate_passwords(chars: str, min_len: int, max_len: int):
    for length in range(min_len, max_len + 1):
        for pwd_tuple in itertools.product(chars, repeat=length):
            yield "".join(pwd_tuple)


def load_passwords(wordlist_file: str):
    with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield line

def try_password(pdf_path: str, password: str):
    try:
        with pikepdf.open(pdf_path, password=password):
            return password
    except PasswordError:
        return None
    except Exception as exc:            
        print(f"[!] Error with {password!r}: {exc}")
        return None


def decrypt_pdf(pdf_path: str, passwords, total_pw: int, max_workers: int = 4):
    with ThreadPoolExecutor(max_workers=max_workers) as pool, \
            tqdm(total=total_pw, desc="Cracking", unit="pwd") as bar:

        future_map = {pool.submit(try_password, pdf_path, pwd): pwd
                      for pwd in passwords}

        for future in as_completed(future_map):
            bar.update(1)
            result = future.result()
            if result:                 
                for fut in future_map:
                    fut.cancel()
                return result
    return None

def main():
    parser = argparse.ArgumentParser(
        description="Decrypt a password‑protected PDF (dictionary or brute force)"
    )
    parser.add_argument("pdf", help="Path to the protected PDF file")

    word = parser.add_argument_group("Dictionary attack")
    word.add_argument("--Wordlist", help="Path to password list (one per line)")

    brute = parser.add_argument_group("Brute‑force generation")
    brute.add_argument("--generate", action="store_true", help="Generate passwords on the fly")
    brute.add_argument("--min-len", type=int, default=1, help="Minimum length when generating (default 1)")
    brute.add_argument("--max-len", type=int, default=3, help="Maximum length when generating (default 3)")
    brute.add_argument("--charset", default=string.ascii_letters + string.digits + string.punctuation, help="Characters to use for generation")

    parser.add_argument("--workers", type=int, default=4, help="Thread count (default 4)")
    args = parser.parse_args()

    if args.Wordlist:
        passwords = load_passwords(args.Wordlist)
        total_pw = sum(1 for _ in load_passwords(args.Wordlist))
    elif args.generate:
        passwords = generate_passwords(args.charset, args.min_len, args.max_len)
        total_pw = sum(len(args.charset) ** l
                       for l in range(args.min_len, args.max_len + 1))
    else:
        parser.error("Either --Wordlist or --generate must be supplied.")

    print(f"[+] Target PDF   : {args.pdf}")
    print(f"[+] Passwords    : {total_pw:,}")
    print(f"[+] Threads      : {args.workers}\n")

    found = decrypt_pdf(args.pdf, passwords, total_pw, args.workers)

    if found:
        print(f"\n✅ Password FOUND → {found!r}")
    else:
        print("\n❌ Password not found in provided set.")


if __name__ == "__main__":
    main()
