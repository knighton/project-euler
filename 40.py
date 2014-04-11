def get_digit(n):
  cur_offset = 1
  cur_number_len = 1
  while True:
    next_offset = cur_offset + cur_number_len * (10 ** cur_number_len / 10 * 9)
    if n < next_offset:
      index_into_stretch = (n - cur_offset)
      num = index_into_stretch / cur_number_len + 10 ** (cur_number_len - 1)
      r = str(num)[index_into_stretch % cur_number_len]
      return int(r)

    # step.
    cur_number_len += 1
    cur_offset = next_offset
  assert False

print '--'
for i in range(120):
  print i, get_digit(i)
print '--'

r = 1
for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
  r *= get_digit(i)
print r
