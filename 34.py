def fac(n):
  if n == 0:
    return 1
  else:
    return n * fac(n - 1)

def is_curious(n):
  s = str(n)
  nn = map(int, s)
  return sum(map(fac, nn)) == n

ii = []
for i in range(3, 1000000):
  if is_curious(i):
    ii.append(i)
print ii
print sum(ii)
