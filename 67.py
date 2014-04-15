def get_triangle(f):
  ss = open(f).readlines()
  ss = filter(lambda s: s.strip(), ss)
  nnn = map(lambda s: map(int, s.split()), ss)
  return nnn

def get_test_triangle():
  return [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
  ]

f = '67/triangle.txt'
tri = get_triangle(f)
sums = [list(tri[-1])]
for y in reversed(xrange(len(tri) - 1)):
  print '?', y, len(tri) - y + 1
  row = []
  for x in range(len(tri[y])):
    a = sums[len(sums) - 1][x]
    b = sums[len(sums) - 1][x + 1]
    row.append(max(a, b) + tri[y][x])
  sums.append(row)
print sums[-1][0]
