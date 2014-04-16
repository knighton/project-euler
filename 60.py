import collections
import itertools
import util

PRIMES_UP_TO = 10000

def is_prime_pair(a, b):
  ab = int(str(a) + str(b))
  if not util.is_prime(ab):
    return False

  ba = int(str(b) + str(a))
  if not util.is_prime(ba):
    return False

  return True

def is_prime_pair_caching(a, b, prime_pair_cache):
  key = (a, b)
  if key in prime_pair_cache:
    return prime_pair_cache[key]
  r = is_prime_pair(a, b)
  prime_pair_cache[key] = r
  return r

def is_prime_set(selected, prime_pair_cache):
  for i in range(len(selected)):
    a = selected[i]
    for j in range(i):
      b = selected[j]
      if not is_prime_pair_caching(a, b, prime_pair_cache):
        return False
  return True

print 'getting primes up to %d...' % PRIMES_UP_TO
primes = []
for i in range(2, PRIMES_UP_TO):
  if util.is_prime(i):
    primes.append(i)

print 'getting prime pairs... (%d primes)' % (len(primes),)
prime_pair_cache = {}
prime2with = collections.defaultdict(list)
count = 0
for pair in itertools.combinations(primes, 2):
  if count % 100000 == 0:
    print 'checked %d pairs...' % count
  count += 1
  if is_prime_set(pair, prime_pair_cache):
    a, b = pair
    prime2with[a].append(b)
    prime2with[b].append(a)

print 'treeing for prime pair sets...'
sum2tuple = collections.defaultdict(list)
for a in sorted(prime2with):
  print 'first prime = %d...' % a
  for b in prime2with[a]:
    if b <= a:
      continue
    for c in prime2with[b]:
      if c <= b:
        continue
      for d in prime2with[c]:
        if d <= c:
          continue
        for e in prime2with[d]:
          if e <= d:
            continue
          pp = (a, b, c, d, e)
          if is_prime_set(pp, prime_pair_cache):
            sum2tuple[sum(pp)].append(pp)

m = min(sum2tuple)
print sum2tuple[m], '->', m
