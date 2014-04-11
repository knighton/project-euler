def fac(n):
  if n == 1:
    return 1
  else:
    return n * fac(n - 1)

n = fac(100)
print sum(map(int, str(n)))
