def collatz(n, cache):
  if n in cache:
    return cache[n]

  if n % 2 == 0:
    r = n / 2
  else:
    r = 3 * n + 1

  cache[n] = r
  return r

def collatz_len(n, cache):
  r = 1
  while True:
    n = collatz(n, cache)
    r += 1
    if n == 1:
      break
  return r

cache = {}
max_len = 0
max_i = None
for i in range(2, 1000000):
  if i % 100000 == 0:
    print '.'
  cur_len = collatz_len(i, cache)
  if max_len < cur_len:
    max_len = cur_len
    max_i = i
print max_i
