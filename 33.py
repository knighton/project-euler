import util

def ones(n):
  return n % 10

def tens(n):
  return (n / 10) % 10

rr = []
for a in range(10, 100):
  for b in range(a + 1, 100):
    if ones(a) == tens(b):
      if tens(a) * b  == ones(b) * a:
        rr.append(((a, b), (tens(a), ones(b))))
print rr

num = rr[0][0][0]
denom = rr[0][0][1]
for pair in rr[1:]:
  a = pair[0]
  num *= a[0]
  denom *= a[1]
print num, denom

gcd = util.gcd(num, denom)
print num / gcd, denom / gcd
