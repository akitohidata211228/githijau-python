# calculator.py
# Kalkulator dua angka.

def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return "Error: pembagian nol" if b == 0 else a / b
    return "Operasi tidak dikenal"


print("9 + 4 =", calculate(9, 4, "+"))
print("9 / 4 =", calculate(9, 4, "/"))
