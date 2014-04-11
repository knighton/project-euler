def get_proper_divisors(n):
  divs = []
  for i in range(1, n / 2 + 1):
    if n % i == 0:
      divs.append(i)
  return divs

def is_abundant(n):
  divs = get_proper_divisors(n)
  return n < sum(divs)

def is_sum_of_two_abundants(n, ab):
  for i in range(0, n / 2 + 1):
    if ab[i] and ab[n - i]:
      return True
  return False

ab = []
for i in range(30000):
  ab.append(is_abundant(i))

r = 0
for i in range(30000):
  # print i, ab[i], is_sum_of_two_abundants(i, ab)
  if not is_sum_of_two_abundants(i, ab):
    r += i
print r
