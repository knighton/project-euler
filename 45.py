tri = lambda n: n * (n + 1) / 2
penta = lambda n: n * (3 * n - 1) / 2
hexa = lambda n: n * (2 * n - 1)

tris = map(tri, xrange(1000000))
pentas = map(penta, xrange(1000000))
hexas = map(hexa, xrange(1000000))

import collections
n2count = collections.defaultdict(int)
for n in tris + pentas + hexas:
  n2count[n] += 1

for n, count in sorted(n2count.iteritems()):
  if count == 3:
    print n
