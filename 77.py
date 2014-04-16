import util

UP_TO = 1000

primes = util.primes_in_range(2, UP_TO)

ways = [0] * UP_TO
ways[0] = 1
for p in primes:
  for n in range(p, UP_TO):
    ways[n] += ways[n - p]

for x, w in enumerate(ways):
  if 5000 < w:
    print x
    break
