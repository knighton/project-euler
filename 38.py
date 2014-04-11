def is_pandigital(s):
  return ''.join(sorted(s)) == '123456789'

pandigital_nn = []
for i in range(100000):
  for n in range(1, 6):
    nn = []
    for j in range(1, n):
      nn.append(i * j)
    s = ''.join(map(str, nn))
    if is_pandigital(s):
      print '--', s
      pandigital_nn.append(int(s))
print max(pandigital_nn)
