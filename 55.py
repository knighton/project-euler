def reversed_num(n):
  return int(str(n)[::-1])

def is_palindrome(n):
  s = str(n)
  return s == s[::-1]

def is_lychrel_to(n, max_iter):
  for i in range(max_iter):
    n += reversed_num(n)
    if is_palindrome(n):
      return True
  return False

def is_lychrel(n):
  return is_lychrel_to(n, 50)

count = 0
for i in range(10000):
  if not is_lychrel(i):
    count += 1
print count
