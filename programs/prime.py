# prime.py
# Cari bilangan prima 1-100.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = [i for i in range(1, 101) if is_prime(i)]
print(f"Bilangan prima 1-100 ({len(primes)} buah):")
print(", ".join(str(x) for x in primes))
