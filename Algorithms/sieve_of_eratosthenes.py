import math
# Sieve of Eratosthenes
# find primes till maximum
def sieve(maximum):
    primes = [1] * maximum

    # 0 and 1 are not primes set them to 0
    primes[0] = 0
    primes[1] = 0
    i = 2

    while i * i < math.sqrt(maximum):
      i += 1
      if primes[i] == 1:
          j = i * i
          while j < maximum:
            j += i
            primes[j] = 0;

    for c in range(0, maximum):
        if primes[c] == 1:
            print(c)

maximum = raw_input("Enter a maximum:")
sieve(int(maximum))
