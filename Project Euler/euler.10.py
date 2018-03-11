from math import ceil

def is_prime(num):
    top = int(ceil(num ** 0.5))
    for x in xrange(3, top + 1, 2):
        if num % x == 0:
            return False
    return True

def primes(max=10):
    yield 2
    current = 3
    while current < max:
        if is_prime(current):
            yield current
        current += 2

if __name__ == "__main__":
    print sum(primes(2000000))
