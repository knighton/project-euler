def d(n):
  return sorted(str(n))

def want(n):
  return d(n) == d(2 * n) == d(3 * n) == d(4 * n) == d(5 * n) == d(6 * n)

for i in range(1, 1000000):
  if want(i):
    print i
    break
