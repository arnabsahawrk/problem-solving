#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        unordered_set<int> present;
        for (int i = 0; i < n; i++)
        {
            int val;
            cin >> val;
            present.insert(val);
        }

        int count = 0;
        for (int i = 1; i <= n; i++)
        {
            if (present.find(i) == present.end())
                count++;
        }

        cout << count << endl;
    }

    return 0;
}