# fibonacci.py
# Deret Fibonacci: 15 suku pertama.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


terms = 15
sequence = [fibonacci(i) for i in range(terms)]
print("Fibonacci:", ", ".join(str(x) for x in sequence))
