def digital_sum(n):
  return sum(map(int, str(n)))

max_ds = None
for a in range(100):
  for b in range(100):
    n = a ** b
    ds = digital_sum(n)
    max_ds = max(ds, max_ds)
print max_ds
