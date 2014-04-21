#include <cstdio>

template <typename T>
T Reversed(T n) {
  T r = 0;
  while (n) {
    r = 10 * r + n % 10;
    n /= 10;
  }
  return r;
}

template <typename T>
bool AreDigitsOdd(T n) {
  while (n) {
    if ((n % 10) % 2 == 0) {
      return false;
    }
    n /= 10;
  }
  return true;
}

bool IsReversible(int n) {
  if (n % 10 == 0) {
    return false;
  }

  int rev_n = Reversed(n);

  int sum = n + rev_n;

  return AreDigitsOdd(sum);
}

int main() {
  int r = 0;
  int limit = 1000000000;
  for (int i = 1; i < limit; ++i) {
    if (IsReversible(i)) {
      ++r;
    }
  }
  printf("%d\n", r);
}
