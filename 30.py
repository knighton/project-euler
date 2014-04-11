def is_curious(n):
  nn = map(int, str(n))
  ff = map(lambda n: n ** 5, nn)
  return sum(ff) == n

ii = []
for i in range(2, 1000000):
  if is_curious(i):
    ii.append(i)
print ii
print sum(ii)
