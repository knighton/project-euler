import util

UP_TO = 100

ways = [0] * (UP_TO + 1)
ways[0] = 1
for n in range(1, UP_TO):
  for x in range(n, UP_TO + 1):
    ways[x] += ways[x - n]

for x, w in enumerate(ways):
  print x, w
