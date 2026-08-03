# palindrome.py
# Cek apakah sebuah kata merupakan palindrom.

import re


def is_palindrome(text):
    cleaned = re.sub(r"[^a-z0-9]", "", text.lower())
    return cleaned == cleaned[::-1]


for s in ["Racecar", "Hello", "Kasur ini rusak"]:
    print(f'"{s}" -> ' + ("palindrom" if is_palindrome(s) else "bukan"))
