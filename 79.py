import itertools

def get_all_chrs(ss):
  cc = set()
  for s in ss:
    for c in s:
      cc.add(c)
  cc = list(cc)
  return cc

def works(order, ss):
  c2orderindexof = {}
  for x, c in enumerate(order):
    c2orderindexof[c] = x

  for s in ss:
    sindexofs = []
    for c in s:
      sindexofs.append(c2orderindexof[c])
    if sindexofs != list(sorted(sindexofs)):
      return False

  return True

ss = open('79/keylog.txt').read().split('\n')
ss = filter(lambda s: s.strip(), ss)
cc = get_all_chrs(ss)
for order in itertools.permutations(cc):
  if works(order, ss):
    print ''.join(order)
