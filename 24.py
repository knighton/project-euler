import itertools

digits = range(10)
ith = 1
for x in itertools.permutations(digits):
  if ith == 1000000:
    print ''.join(map(str, x))
    break
  ith += 1
