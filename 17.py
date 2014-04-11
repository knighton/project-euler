ones = ('zero one two three four five six seven eight nine ' +
        'ten eleven twelve thirteen fourteen fifteen sixteen seventeen ' +
        'eighteen nineteen').split()
tens = '_ _ twenty thirty forty fifty sixty seventy eighty ninety'.split()

def say_under_100(n):
  assert 0 <= n < 100

  if n < len(ones):
    return ones[n]

  r = tens[n / 10]
  n %= 10
  if n:
    r += '-' + ones[n]
  return r

def say_under_1000(n):
  assert 0 <= n < 1000

  if n < 100:
    return say_under_100(n)

  r = ones[n / 100] + ' hundred'
  n %= 100
  if n:
    r += ' and ' + say_under_100(n)
  return r

def say(n):
  assert 0 <= n < 1000000

  if n < 1000:
    return say_under_1000(n)

  r = say_under_1000(n / 1000) + ' thousand'
  n %= 1000
  if n:
    r += ' and ' + say_under_1000(n)
  return r

for n, s in [
  (2, 'two'),
  (17, 'seventeen'),
  (21, 'twenty-one'),
  (100, 'one hundred'),
  (101, 'one hundred and one'),
  (999, 'nine hundred and ninety-nine'),
  (1000, 'one thousand'),
  (1001, 'one thousand and one'),
  (1101, 'one thousand and one hundred and one'),
]:
  assert say(n) == s

ss = map(say, range(1, 1001))
s = ''.join(ss)
s = ''.join(s.split('-'))
s = ''.join(s.split())
print len(s)
