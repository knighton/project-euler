import itertools

def has_property(s):
  if (int(s[1:4]) % 2 == 0 and
      int(s[2:5]) % 3 == 0 and
      int(s[3:6]) % 5 == 0 and
      int(s[4:7]) % 7 == 0 and
      int(s[5:8]) % 11 == 0 and
      int(s[6:9]) % 13 == 0 and
      int(s[7:10]) % 17 == 0):
    return True
  return False

r = 0
print map(str, range(10))
for s in itertools.permutations(map(str, range(10))):
  s = ''.join(s)
  n = int(s)
  if has_property(s):
    print n
    r += n
print r
