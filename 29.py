nn = []
for a in range(2, 101):
  for b in range(2, 101):
    n = a ** b
    nn.append(n)
print len(set(nn))
