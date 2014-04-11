import util

n = 1
for i in range(1, 21):
  n = util.lcm(i, n)
print n
