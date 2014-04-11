#!/usr/bin/python

class Factorizer(object):
  """factor numbers with a cache."""

  def __init__(self):
    # caches
    self.n2factors = {}
    self.n2isprime = {}

  def factorize(self, n):
    if n < 2:
      return []

    if n in self.n2factors:
      return self.n2factors[n]

    while n % 2 == 0:
      return [2] + self.factorize(n / 2)

    stop = int(n ** 0.5) + 1
    for i in range(3, stop, 2):
      while n % i == 0:
        return [i] + self.factorize(n / i)

    if n != 1:
      return [n]
    else:
      return []

  def is_prime(self, n):
    if n in self.n2isprime:
      return self.n2isprime[n]

    if n in self.n2factors:
      return len(self.n2factors) == 1

    if n < 2:
      assert False

    if n % 2 == 0:
      self.n2isprime[n] = False
      return False

    stop = int(n ** 0.5 + 1)
    for i in range(3, stop, 2):
      if n % i == 0:
        self.n2isprime[n] = False
        return False

    self.n2isprime[n] = True
    return True


_f = Factorizer()

def factorize(n):
  return _f.factorize(n)

def is_prime(n):
  return _f.is_prime(n)

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def lcm(a, b):
  return a * b / gcd(a, b)
