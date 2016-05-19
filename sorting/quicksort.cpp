#include <iostream>
#include <string>
#include <vector>

template <typename T>
void swap(T &a, T &b) {
  T tmp = a;
  a = b;
  b = tmp;
}

template <typename T>
int partition(std::vector<T> &a, int lo, int hi) {
  T pivot = a[hi];
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

template <typename T>
void quicksort(std::vector<T> &a, int lo, int hi) {
  // std::cout << lo << " " << hi << std::endl;
  if (lo < hi) {
    int p = partition(a, lo, hi);
    // std::cout << "partition(" << lo <<", " << hi << ") is: " << p << std::endl;
    quicksort(a, lo, p-1);
    quicksort(a, p+1, hi);
  }
}

int main() {
  std::cout << "Enter your vector:\n";
  std::vector<int> a;
  int i;
  while(std::cin >> i) {
    a.push_back(i);
  }
  std::cout << "The vector you've input is: ";
  for (auto &j : a) {
    std::cout << j << " ";
  }
  std::cout << "\nThe vector sorted is: ";
  quicksort(a, 0, a.size() - 1);
  for (auto &j : a) {
    std::cout << j << " ";
  }
  std::cout << std::endl;
}
