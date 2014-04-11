for p in range(1001):
  r = 0
  for a in range(1, 1000):
    for b in range(1, 1000):
      for c in range(1, 1000):
        if a * a + b * b == c * c:
          r += 1
  print p, r
