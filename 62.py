import collections
digits2cubesof = collections.defaultdict(list)
for i in range(1, 100000):
  cube = i ** 3
  dig = str(sorted(str(cube)))
  digits2cubesof[dig].append(i)
  vv = digits2cubesof[dig]
  if len(vv) == 5:
    vv = sorted(vv)
    print vv
    print vv[0] ** 3
    break
