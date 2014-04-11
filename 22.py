s = open('22/names.txt').read()
ss = eval(s)
ss = sorted(ss)

def value(s):
  r = 0
  for c in s:
    r += ord(c) - ord('A') + 1
  return r

nn = map(value, ss)
for i in range(len(nn)):
  nn[i] *= (i + 1)

print sum(nn)
