#include <iostream>
#include<string>
using namespace std;
struct binaryTreeNode
{
public:
	string person_num;
	string person_name;
	string person_sex;
	string partner_name;
	string partner_sex;
	binaryTreeNode *first_child,*next_sibling,*front_parent,*front_sibling;
};