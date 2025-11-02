#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q;
    cin >> Q;

    unordered_map<int, int> freq;
    unordered_map<int, set<int, greater<int>>> rev_freq;
    set<int> freq_groups;

    while (Q--)
    {
        int type;
        cin >> type;

        if (type == 1)
        {
            int X;
            cin >> X;

            int prev_count = freq[X];
            if (prev_count > 0)
            {
                rev_freq[prev_count].erase(X);
                if (rev_freq[prev_count].empty())
                {
                    rev_freq.erase(prev_count);
                    freq_groups.erase(prev_count);
                }
            }

            int new_count = prev_count + 1;
            freq[X] = new_count;
            rev_freq[new_count].insert(X);
            if (rev_freq[new_count].size() == 1)
            {
                freq_groups.insert(new_count);
            }
        }
        else
        {
            if (freq.empty())
            {
                cout << "empty\n";
                continue;
            }

            int f = *freq_groups.begin();
            auto &elements = rev_freq[f];
            int X = *elements.begin();

            elements.erase(elements.begin());
            if (elements.empty())
            {
                rev_freq.erase(f);
                freq_groups.erase(f);
            }

            int k = max(1, f / 2);
            int new_count = f - k;

            if (new_count > 0)
            {
                freq[X] = new_count;
                rev_freq[new_count].insert(X);
                if (rev_freq[new_count].size() == 1)
                {
                    freq_groups.insert(new_count);
                }
            }
            else
            {
                freq.erase(X);
            }

            cout << X << "\n";
        }
    }

    return 0;
}