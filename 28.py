def build_spiral(width):
  assert width % 2 == 1
  d = {}
  x, y = 0, 0
  n = 1
  d[(x, y)] = n
  for i in range(1, width - 1, 2):
    x += 1
    for j in range(i):
      n += 1
      d[(x, y)] = n
      y -= 1
    for j in range(i + 1):
      n += 1
      d[(x, y)] = n
      x -= 1
    for j in range(i + 1):
      n += 1
      d[(x, y)] = n
      y += 1
    for j in range(i + 1):
      n += 1
      d[(x, y)] = n
      x += 1
    n += 1
    d[(x, y)] = n
  return d

class Spiral(object):
  def __init__(self, width):
    self.width = width
    self.d = build_spiral(width)

  def sum_of_diagonals(self):
    edge = int(self.width / 2)
    r = 0
    for x in range(-edge, edge + 1):
      y = x
      r += self.d[(x, y)]
      y = -x
      r += self.d[(x, y)]
    r -= self.d[(0, 0)]
    return r

print Spiral(1001).sum_of_diagonals()
