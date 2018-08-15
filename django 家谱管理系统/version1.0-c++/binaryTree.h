#include <iostream>
#include "binaryTreeNode.h"
using namespace std;
class binaryTree
{
public:
	binaryTreeNode *root;
public:
	binaryTree();
	void creat_binary_tree(binaryTreeNode *&root);
	void show_binary_tree(binaryTreeNode *&root,int i);
	void search_all_information1(string num,binaryTreeNode *&root);
	void search_all_information2(string name,binaryTreeNode *&root);
	void search_all_height1(string num,binaryTreeNode *&root);
	void search_all_height2(string name,binaryTreeNode *&root);
	void add_child(string num,binaryTreeNode *&root);
	int is_rename(string name,binaryTreeNode *&root,int i);
    void showintree(binaryTreeNode *&root,int i);
};


