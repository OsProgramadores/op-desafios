#include <bits/stdc++.h>

using namespace std;

vector<int> eratostenes(int n) {
  vector<bool> is_prime(n + 1, true);
  vector<int> ans;

  is_prime[0] = is_prime[1] = false;
  for (int i = 2; i <= n; i++) {
    if (is_prime[i]) {
      ans.push_back(i);

      if (i > n / i) {
        continue;
      }

      for (int j = i * i; j <= n; j += i) {
        is_prime[j] = false;
      }
    }
  }

  return ans;
}

int main() {
  int max_prime = 10000;
  auto list = eratostenes(max_prime);

  for (int i = 0; i < (int) list.size(); i++) {
    if (i > 0) {
      cout << " ";
    }
    cout << list[i];
  }
  cout << endl;

  return 0;
}