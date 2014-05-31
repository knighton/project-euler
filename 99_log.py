import math
ss = open('99/base_exp.txt').read().split()
nnn = map(lambda s: map(int, s.split(',')), ss)
nn = []
for i, (base, exp) in enumerate(nnn):
  n = math.log(base) * exp
  print base, exp, 'ok'
  nn.append((n, i + 1))
print max(nn)
