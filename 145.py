def reversed_via_str(n):
  return int(str(n)[::-1])

def reversed(n):
  r = 0
  while 0 < n:
    r = 10 * r + n % 10
    n /= 10
  return r

def are_digits_odd_str(n):
  s = str(n)
  nn = map(ord, s)
  return sum(map(lambda n: n % 2 == 1, nn)) == len(s)

def are_digits_odd(n):
  while 0 < n:
    if (n % 10) % 2 == 0:
      return False
    n /= 10
  return True

def is_reversible(n):
  if n % 10 == 0:  # can't have trailing or leading zeros
    return False
  n2 = reversed(n)
  n3 = n + n2
  return are_digits_odd(n3)

r = 0
for i in range(1000000):
  if is_reversible(i):
    r += 1
print 'sum for a million (a billion for problem stmt):', r
