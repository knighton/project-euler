import util

print 'getting primes...'
primes = []
for i in range(2, 10000):
  if util.is_prime(i):
    primes.append(i)
primes_set = set(primes)

print 'getting sums...'
sums = []
tmp = 0
for i in range(len(primes)):
  sums.append(tmp)
  tmp += primes[i]

print 'main loop...'
done = False
for window_length in reversed(range(len(primes))):
  print 'window length = %s', window_length
  for off in range(len(primes) - window_length):
    n = sums[off + window_length] - sums[off]
    if util.is_prime(n) and n < 1000000:
      print n
      done = True
      break
  if done:
    break
