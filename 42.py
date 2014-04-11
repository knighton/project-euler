s = open('42/words.txt').read()
ss = eval(s)

nn = []
for s in ss:
  n = sum(map(lambda c: ord(c) - ord('A') + 1, s))
  nn.append(n)
max_n = max(nn)

tris = []
i = 0
while True:
  n = i * (i + 1) / 2
  tris.append(n)
  i += 1
  if max_n < n:
    break
tris = set(tris)

count = 0
for n in nn:
  if n in tris:
    count += 1

print count
