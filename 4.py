r = 0
r_number = None
for a in range(100, 1000):
  for b in range(100, 1000):
    prod = a * b
    s = str(prod)
    if s == s[::-1]:
      r = max(r, len(s))
      r_number = max(r_number, prod)
print r_number
