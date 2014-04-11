def is_prime(n):
  if n < 2:
    return False

  if n == 2:
    return True

  if n % 2 == 0:
    return False

  stop = int(n ** 0.5) + 1
  for i in range(3, stop, 2):
    if n % i == 0:
      return False

  return True

def is_prime_caching(n, cache):
  if n in cache:
    return cache[n]

  b = is_prime(n)
  cache[n] = b
  return b

def is_truncatable_prime(n, prime_cache):
  if not is_prime_caching(n, prime_cache):
    return False

  s = str(n)
  for i in range(1, len(s)):
    n = int(s[:-i])
    if not is_prime_caching(n, prime_cache):
      return False
    n = int(s[i:])
    if not is_prime_caching(n, prime_cache):
      return False

  return True

d = {}
wants = []
i = 11
while len(wants) < 11:
  if is_truncatable_prime(i, d):
    wants.append(i)
  i += 1
print wants
print sum(wants)
