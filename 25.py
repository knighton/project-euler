a = 1
b = 1
i = 1
while True:
  if len(str(a)) == 1000:
    print i
    print a
    break

  c = a + b
  a = b
  b = c
  i += 1
