count = 0
for i in range(1, 10):  # >10 would result in more than one digit per.
  for j in range(1000):
    n = i ** j
    num_digits = len(str(n))
    if j == num_digits:
      print '%d ^ %d = %d (%d digits)' % (i, j, n, num_digits)
      count += 1
print count
