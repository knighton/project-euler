import util

primes = []
for i in range(2, 1000000):
  if util.is_prime(i):
    primes.append(i)

for n in range(3, 1000000, 2):
  if util.is_prime(n):
    continue

  found = False
  for p in primes:
    if not (p < n):
      break
    sq = (n - p) / 2
    b = int(sq ** 0.5) ** 2 == sq
    if b:
      found = True
      break
  print n, found
  if not found:
    break
