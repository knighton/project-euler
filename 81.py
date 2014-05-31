s = open('81/matrix.txt').read()
nnn = map(lambda s: map(int, s.split(',')), s.split())
print nnn

"""
mmm = []
for i in range(len(nnn)):
  mmm.append([0] * len(nnn)[i])
mmm[-1][-1] = 
"""

def min_path_sum(m, x, y, cache):
  if (x, y) in cache:
    return cache[(x, y)]
  options = []
  if 0 <= x + 1 < len(m[y]):
    right = m[x][y] + min_path_sum(m, x + 1, y, cache)
    options.append(right)
  if 0 <= y + 1 < len(m):
    down = m[x][y] + min_path_sum(m, x, y + 1, cache)
    options.append(down)
  if not options:
    options.append(m[x][y])  # bottom right corner
  r = min(options)
  cache[(x, y)] = r
  return r

cache = {}
print min_path_sum(nnn, 0, 0, cache)
