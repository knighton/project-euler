r = 0
for i in range(1, 1000000):
  d = str(i)
  if d == d[::-1]:
    b = bin(i)[2:]
    if b == b[::-1]:
      r += i
print r
