fac = lambda n: n * fac(n - 1) if n > 1 else 1

f = lambda n, r: fac(n) / (fac(r) * fac(n - r))

count = 0
for n in range(1, 101):
  for r in range(1, n + 1):
    c = f(n, r)
    if c > 1000000:
      count += 1
print count
