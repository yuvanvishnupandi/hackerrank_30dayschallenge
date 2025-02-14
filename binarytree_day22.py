#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* left;
    Node* right;
    
    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};

class BST {
public:
    Node* insert(Node* root, int data) {
        if (root == nullptr) {
            return new Node(data);
        }
        if (data < root->data) {
            root->left = insert(root->left, data);
        } else {
            root->right = insert(root->right, data);
        }
        return root;
    }

    int getHeight(Node* root) {
        if (root == nullptr) {
            return -1;
        }
        int leftHeight = getHeight(root->left);
        int rightHeight = getHeight(root->right);
        return max(leftHeight, rightHeight) + 1;
    }
};

int main() {
    int n, data;
    cin >> n;
    
    Node* root = nullptr;
    BST tree;
    
    for (int i = 0; i < n; i++) {
        cin >> data;
        root = tree.insert(root, data);
    }
    
    cout << tree.getHeight(root) << endl;
    
    return 0;
}
