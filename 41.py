import itertools
import util

def pandigitals(last_digit):
  assert 0 <= last_digit <= 9
  dd = range(1, last_digit + 1)[::-1]
  print '??', dd
  for nn in itertools.permutations(dd):
    yield int(''.join(map(str, nn)))

def get_biggest_pandigital_prime():
  for biggest_digit in range(1, 10)[::-1]:
    for n in pandigitals(biggest_digit):
      if util.is_prime(n):
        return n
  return None

print get_biggest_pandigital_prime()
