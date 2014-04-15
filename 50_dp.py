import itertools
import util

def show_sums(sums):
  for row in sums:
    print '\t'.join(map(str, row))

def get_primes_below(below):
  primes = []
  for i in range(2, below):
    if util.is_prime(i):
      primes.append(i)
  return primes

def mk_sums_table(primes):
  sums = [primes]
  while len(sums[-1]):
    row = []
    for i in range(len(sums[-1]) - 1):
      row.append(sums[-1][i] + sums[0][i + len(sums)])
    sums.append(row)
  return sums

def get_deepest_prime_below(sums, below):
  rr = []
  for y in reversed(xrange(len(sums))):
    for x in range(len(sums[y])):
      n = sums[y][x]
      if util.is_prime(n) and n < below:
        rr.append(n)
    if rr:
      break
  return rr

primes = get_primes_below(10000)

sums = mk_sums_table(primes)

print get_deepest_prime_below(sums, 1000000)
