import util

def are_all_rotations_prime(n):
  if n < 2:
    return False

  if not util.is_prime(n):
    return False

  s = str(n)
  for i in range(len(s)):
    s2 = s[i:] + s[:i]
    if not util.is_prime(int(s2)):
      return False

  print '!!', n
  return True

r = 0
for i in range(2, 1000000):
  if are_all_rotations_prime(i):
    r += 1
print r
