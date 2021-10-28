#include<iostream>
using namespace std;
struct Node{
	int data;
	struct Node *left;
	struct Node *right;
};

struct Node* Delete(struct Node *root, int data){
	if(root == NULL) return root;
	else if(data < root->data) root->left = Delete(root->left, data);
	else if(data > root->data) root->right = Delete(root->right,data);
	else{
		// Case 1: No child
		if(root->left == NULL && root->right == NULL){
			delete root;
			root = NULL;
			return root;
		}
		// Case 2: One Child
		else if(root->left == NULL){
			struct Node *temp = root;
			root = root->right;
			delete temp;
			return root;
		}
		else if(root->left == NULL){
			struct Node *temp = root;
			root = root->left;
			delete temp;
			return root;
		}
	}
}