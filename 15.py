def get(a, b, cache):
  if (a, b) in cache:
    return cache[(a, b)]

  if a == b == 0:
    cache[(a, b)] = 1
    return 1

  if a == 0:
    sum_a = 0
  else:
    sum_a = get(a - 1, b, cache)

  if b == 0:
    sum_b = 0
  else:
    sum_b = get(a, b - 1, cache)

  r = sum_a + sum_b
  cache[(a, b)] = r
  return r

cache = {}
print get(20, 20, cache)
