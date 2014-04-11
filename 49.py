import itertools
import util

def get_digit_perm_triples_we_have(n, primes_set):
  digits = str(n)
  have = []
  for nn in itertools.permutations(digits):
    n = int(''.join(nn))
    if n in primes_set:
      have.append(n)
  have = set(have)
  for nn in itertools.permutations(have, 3):
    yield nn

primes = []
for i in range(1000, 10000):
  if util.is_prime(i):
    primes.append(i)
primes_set = set(primes)

triples = set()
for p in primes:
  for triple in get_digit_perm_triples_we_have(p, primes_set):
    a, b, c = triple
    if b - a == c - b and b - a > 0:
      triples.add(triple)
for t in sorted(triples):
  print t, ''.join(map(str, t))
