a = 1
b = 2
total = 0
while b < 4000000:
  if b % 2 == 0:
    total += b
  c = a + b
  a = b
  b = c
print total
