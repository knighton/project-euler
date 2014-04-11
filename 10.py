import util

sum_of_primes = 2
prime = 3
while prime < 2000000:
  if util.is_prime(prime):
    sum_of_primes += prime
  prime += 2

print sum_of_primes
