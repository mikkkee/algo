#include <iostream>
#include <string>
#include <vector>
#include "quicksort.hpp"


int main() {
  std::cout << "Enter your vector:\n";
  std::vector<std::string> a;
  std::string i;
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
