ss = open('89/roman.txt').read().split()

c2val = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}

ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

def int_from_roman(s):
  prev_c = s[0]
  n = 1
  spans = []
  for c in s[1:]:
    if c == prev_c:
      n += 1
    else:
      spans.append((n, c2val[prev_c]))
      n = 1
      prev_c = c
  spans.append((n, c2val[prev_c]))

  r = 0
  prev_mul = 0
  for count, mul in reversed(spans):
    change = count * mul
    if mul < prev_mul:
      change = -change
    prev_mul = mul
    r += change
  return r

def roman_from_int(n):
  rr = []

  one = n % 10
  rr.append(ones[one])
  n /= 10

  ten = n % 10
  rr.append(tens[ten])
  n /= 10

  hundred = n % 10
  rr.append(hundreds[hundred])
  n /= 10

  rr.append('M' * n)

  return ''.join(reversed(rr))

dsum = 0
for s in ss:
  n = int_from_roman(s)
  s2 = roman_from_int(n)
  print s, '->', n, '->', s2
  d = len(s) - len(s2)
  dsum += d
print dsum
