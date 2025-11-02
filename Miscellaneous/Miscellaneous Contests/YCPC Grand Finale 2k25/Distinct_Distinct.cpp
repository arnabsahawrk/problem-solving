#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long x;
    cin >> x;

    if (x == 1)
    {
        cout << 1 << endl;
        return 0;
    }

    long long ans = 1;
    for (long long d = 2; d * d <= x; ++d)
    {
        if (x % d == 0)
        {
            int e = 0;
            while (x % d == 0)
            {
                e++;
                x /= d;
            }
            ans *= (e + 1);
        }
    }

    if (x > 1)
    {
        ans *= 2;
    }

    cout << ans << endl;
    return 0;
}