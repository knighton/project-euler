import itertools
import util

def prod(nn):
  r = 1
  for n in nn:
    r *= n
  return r

def select_some(aa):
  for i in range(len(aa)):
    for sub_aa in itertools.combinations(aa, i):
      yield sub_aa

ii = []
for i in range(2, 30000):
  if i % 1000 == 0:
    print i
  nn = util.factorize(i)
  for selected_nn in select_some(nn):
    a = prod(selected_nn)
    b = i / a
    s = ''.join(sorted(str(a) + str(b) + str(i)))
    if s == '123456789':
      print '%d * %d = %d' % (a, b, i)
      ii.append(i)
      break
print sum(ii)
