def triangular_numbers():
  r = 0
  to_add = 1
  while True:
    r += to_add
    to_add += 1
    yield r

def get_num_divisors(n):
  r = 0
  stop = int(n ** 0.5)
  for i in range(1, stop):
    if n % i == 0:
      r += 2
  if stop * stop == n:
    r += 1
  return r

i = 0
for n in triangular_numbers():
  i += 1
  d = get_num_divisors(n)
  if n % 100 == 0:
    print i, n, d
  if 500 < d:
    print 'got:', n
    break
