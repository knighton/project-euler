n = 3
d = 7
max_f = None
best_num = None
best_denom = None
limit = 1000000

for denom in range(limit, 0, -1):
  num = (n * denom - 1) / d
  f = num / float(denom)
  if f > max_f:
    max_f = f
    best_num = num
    best_denom = denom
print '%d/%d' % (best_num, best_denom)
