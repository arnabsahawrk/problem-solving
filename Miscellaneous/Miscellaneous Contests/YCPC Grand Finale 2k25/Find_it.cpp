#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int value;
    Node *left;
    Node *right;

    Node(int value)
    {
        this->value = value;
        this->left = nullptr;
        this->right = nullptr;
    }
};

void input_tree(Node *&root)
{
    int val;
    cin >> val;

    if (val != -1)
        root = new Node(val);

    queue<Node *> q;
    if (val != -1)
        q.push(root);

    while (!q.empty())
    {
        Node *parent = q.front();
        q.pop();

        int left, right;
        cin >> left >> right;

        Node *leftChild = nullptr, *rightChild = nullptr;
        if (left != -1)
            leftChild = new Node(left);

        if (right != -1)
            rightChild = new Node(right);

        parent->left = leftChild;
        parent->right = rightChild;

        if (parent->left)
            q.push(leftChild);
        if (parent->right)
            q.push(rightChild);
    }
}

void find_it(Node *root, map<int, int> &mp)
{
    if (root == nullptr)
        return;

    if (root->left == nullptr && root->right == nullptr)
        mp[root->value]++;

    find_it(root->left, mp);
    find_it(root->right, mp);
}

int main()
{
    Node *root = nullptr;

    input_tree(root);

    map<int, int> mp;
    find_it(root, mp);

    int most = 0, freq = 0;
    for (auto it : mp)
    {
        if (it.second > freq)
        {
            most = it.first;
            freq = it.second;
        }
    }

    cout << most << endl;

    return 0;
}