import util

DEBUG = False

def digits_are_same(n, indexes):
  if not indexes:
    return True

  s = str(n)
  z = s[indexes[0]]
  for i in range(1, len(indexes)):
    if s[indexes[i]] != z:
      return False

  return True

def is_prime(n):
  if 2 <= n:
    return util.is_prime(n)
  else:
    return False

def go(p):
  if DEBUG:
    print '-' * 80
    print 'testing prime:', p

  s = str(p)
  digits = map(str, range(10))
  for indexes_to_replace in util.nonempty_combinations_all_lengths(range(len(s))):
    if not digits_are_same(p, indexes_to_replace):
      continue

    if DEBUG:
      print 'replace these indexes:', indexes_to_replace

    num_primes = 0
    for d in digits:
      if DEBUG:
        print 'replace with:', d, '->',
      p2 = []
      for x in range(len(s)):
        if x in indexes_to_replace:  # O(digits in number).
          p2.append(d)
        else:
          p2.append(s[x])

      # on a hunch, ban numbers that start with zero (are not same length).
      starts_with_zero = p2[0] == '0'

      p2 = int(''.join(map(str, p2)))
      is_p = is_prime(p2)
      if is_p and not starts_with_zero:
        num_primes += 1
      if DEBUG:
        print p2, '*' if is_p else ''

    if 8 <= num_primes:
      print p
      return True

    if DEBUG:
      print
  return False

for i in range(3, 1000000, 2):
  if util.is_prime(i):
    if go(i):
      break
