def get_end(n):
  while n not in (1, 89):
    digits = map(int, str(n))
    n = sum(map(lambda a: a * a, digits))
  return n

count = 0
for i in range(1, 10000000):
  if get_end(i) == 89:
    count += 1
print count
