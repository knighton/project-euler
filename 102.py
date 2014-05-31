class Point(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return '(x=%s y=%s)' % (self.x, self.y)

class Triangle(object):
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def __str__(self):
    return '(Tri a=%s b=%s c=%s)' % (self.a, self.b, self.c)

def triangle_from_line(s):
  nn = map(int, s.split(','))
  a = Point(nn[0], nn[1])
  b = Point(nn[2], nn[3])
  c = Point(nn[4], nn[5])
  return Triangle(a, b, c)

def triangle_contains_point(tri, p):
  # from http://jsfiddle.net/PerroAZUL/zdaY8/1/
  p0 = tri.a
  p1 = tri.b
  p2 = tri.c
  A = 0.5 * (-p1.y * p2.x + p0.y * (-p1.x + p2.x) + \
             p0.x * (p1.y - p2.y) + p1.x * p2.y)
  sign = -1 if A < 0 else 1
  s = (p0.y * p2.x - p0.x * p2.y + (p2.y - p0.y) * p.x + \
       (p0.x - p2.x) * p.y) * sign
  t = (p0.x * p1.y - p0.y * p1.x + (p0.y - p1.y) * p.x + \
       (p1.x - p0.x) * p.y) * sign
  return s > 0 and t > 0 and (s + t) < 2 * A * sign

ss = open('102/triangles.txt').readlines()
tt = map(triangle_from_line, ss)
origin = Point(0, 0)
count = 0
for t in tt:
  if triangle_contains_point(t, origin):
    count += 1
print count
