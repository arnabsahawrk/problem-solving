#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    
    string s;
    cin >> s;

    vector<int> freq(26, 0);

    for (char c : s) {
        freq[c - 'a']++;
    }

    int oddCount = 0;
    for (int f : freq) {
        if (f % 2 != 0) {
            oddCount++;
        }
    }

    int differentPos = max(0, oddCount - 1);

    if (differentPos <= k) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
