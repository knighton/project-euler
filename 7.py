import util

primes = [2]
n = 3
while len(primes) < 10001:
  if util.is_prime(n):
    primes.append(n)
  n += 2

print primes[-1]
