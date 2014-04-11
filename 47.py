import util

def num_distinct_prime_factors(n):
  nn = util.factorize(n)
  return len(set(nn))

ndpfs = []
for i in xrange(2, 1000000000):
  if i % 1000 == 0:
    print i
  n = num_distinct_prime_factors(i)
  ndpfs.append(n)
  if ndpfs[-4:] == [4, 4, 4, 4]:
    print i - 3
    break
