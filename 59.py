import itertools

def get_ciphertext():
  s = open('59/cipher1.txt').read()
  nn = map(int, s.split(','))
  return nn

def encode(ct, key):
  r = []
  for x, n in enumerate(ct):
    key_n = key[x % len(key)]
    r.append(n ^ key_n)
  return r

ct = get_ciphertext()

for key in itertools.product(range(128), repeat=3):
  pt = encode(ct, key)

  giveup = False
  for n in pt:
    if n < 32 or n >= 127:
      giveup = True
      break
  if giveup:
    continue

  text = ''.join(map(chr, pt)).lower()
  if 'the ' not in text:
    continue

  print '-' * 80
  print 'key:', map(chr, key)
  print 'sum:', sum(pt)
  print 'plaintext:', text
