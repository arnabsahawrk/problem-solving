#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    string song;
    Node *next;
    Node *prev;

    Node(string song)
    {
        this->song = song;
        this->next = nullptr;
        this->prev = nullptr;
    }
};

int sizeLL = 0;

void insert_at_head(Node *&head, Node *&tail, string song)
{
    Node *newNode = new Node(song);
    if (!head)
    {
        head = newNode;
        tail = newNode;
    }
    else
    {
        newNode->next = head;
        head->prev = newNode;
        head = newNode;
    }
    sizeLL++;
}

void insert_at_tail(Node *&head, Node *&tail, string song)
{
    Node *newNode = new Node(song);
    if (!tail)
    {
        head = newNode;
        tail = newNode;
    }
    else
    {
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
    }
    sizeLL++;
}

void insert_at_index(Node *&head, Node *&tail, string song, int idx)
{
    if (idx < 0 || idx > sizeLL)
    {
        cout << "Invalid" << endl;
        return;
    }

    if (idx == 0)
    {
        insert_at_head(head, tail, song);
        return;
    }
    else if (idx == sizeLL)
    {
        insert_at_tail(head, tail, song);
        return;
    }

    Node *newNode = new Node(song);
    Node *temp = head;
    for (int i = 0; i < idx - 1; i++)
    {
        temp = temp->next;
    }
    newNode->next = temp->next;
    newNode->prev = temp;
    temp->next->prev = newNode;
    temp->next = newNode;

    sizeLL++;
}

void delete_at_index(Node *&head, Node *&tail, int idx)
{
    if (idx < 0 || idx >= sizeLL)
    {
        cout << "Invalid" << endl;
        return;
    }

    Node *deleteNode;
    if (idx == 0)
    {
        deleteNode = head;
        head = head->next;
        if (head)
            head->prev = nullptr;
        else
            tail = nullptr;
    }
    else if (idx == sizeLL - 1)
    {
        deleteNode = tail;
        tail = tail->prev;
        tail->next = nullptr;
    }
    else
    {
        Node *temp = head;
        for (int i = 0; i < idx; i++)
            temp = temp->next;

        deleteNode = temp;
        temp->prev->next = temp->next;
        temp->next->prev = temp->prev;
    }

    delete deleteNode;
    sizeLL--;
}

void display(Node *node)
{
    while (node)
    {
        cout << node->song << " ";
        node = node->next;
    }

    cout << endl;
}

int main()
{
    Node *head = nullptr, *tail = nullptr;
    int query;
    cin >> query;

    while (query--)
    {
        string operation;
        cin >> operation;

        if (operation == "ADD")
        {
            int idx;
            cin >> idx;

            string song;
            cin >> song;
            insert_at_index(head, tail, song, idx);
        }
        else if (operation == "DELETE")
        {
            int idx;
            cin >> idx;
            delete_at_index(head, tail, idx);
        }
        else
        {
            if (sizeLL == 0)
                cout << "EMPTY" << endl;
            else
                display(head);
        }
    }

    return 0;
}