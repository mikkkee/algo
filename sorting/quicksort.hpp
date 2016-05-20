template <typename T> void swap(T &a, T &b) {
  T tmp = a;
  a = b;
  b = tmp;
}

template <typename T> int partition(T &a, int lo, int hi) {
  auto pivot = a[hi];
  int i = lo;
  int j = lo;
  while (j < hi) {
    if (a[j] > pivot) {
      ++j;
    } else {
      swap(a[i], a[j]);
      ++i;
      ++j;
    }
  }
  swap(a[i], a[hi]);
  return i;
}

template <typename T> void quicksort(T &a, int lo, int hi) {
  if (lo < hi) {
    int p = partition(a, lo, hi);
    quicksort(a, lo, p - 1);
    quicksort(a, p + 1, hi);
  }
}
