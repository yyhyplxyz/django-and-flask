#include <iostream>
#include <string>
#include <fstream>
#include"binaryTree.h"
#include <vector>
#include "bst.h"
#include "VisualTree.h"
#include <queue>
#include <isdigit>
using namespace std;
typedef char*                ValueType;
typedef TreeNode<ValueType> NodeType;

BSTree<ValueType>                tree;
VisualTree<NodeType, ValueType>  vtree(&NodeType::parent,
									   &NodeType::left,
									   &NodeType::right,
									   &NodeType::val);

int level = 0;

void checkInput(const string& test) {
	if(test.length()!= 0)
		return 0;
	if(test[0] > '6' || test[0] < '1') 
		return 0;
	return 1;
}

void checkAge(string& test) {
	
	while(1) {
		cin>>t->test;
		int yesy = 1;
		for(int i = 0; i < test.length(); i++ ) {
			if(!isdigit(test[i]))
				yes = 0;
		}
		if(yes == 1)
			break;
		else {
			cout << "输入有误，请输入正确的年龄信息。" << endl;
		}
	}
}

binaryTree::binaryTree()//¹¹Ôìº¯Êý
{
	root=NULL;
}

int binaryTree::is_rename(string name,binaryTreeNode *&root,int i)//ÅÐ¶ÏÊÇ·ñÖØÃû
{
	if(root)
	{
		if(root->person_name==name)
		{
			i=1;
		}
		is_rename(name,root->first_child,i);
		is_rename(name,root->next_sibling,i);
	}
	return i;
}

void readSex_fixed(string &sex){
	cin >> sex;
	while(sex != "male" && sex != "female"){
		cout << "输入有误，请输入 \"male\"  \"female\"";
		cin >> sex;
	}
	return;
}

void binaryTree::creat_binary_tree(binaryTreeNode *&root)//´´½¨¶þ²æÊ÷£¨×ÓÅ®ÐÖµÜ´´½¨·ÇµÝ¹é£©ÓÐËÄ¸öÖ¸ÕëÓò£¬ÓÐÁ½¸öÖ¸ÕëÊÇÓÃÓÚÏßË÷£¨front_sbliding,frong_parent£©
{
	root=NULL;
	binaryTreeNode *t,*p;//tÖ¸ÕëÎªnew³öÀ´µÄ£¬pÎª¸úËæÖ¸Õë
	t=new binaryTreeNode;
	if(root==NULL)
	{
		cout<<"请输入祖先年龄：";
		checkAge()
		cin>>t->person_num;
		cout<<"请输入祖先姓名：";
		cin>>t->person_name;
		cout<<"请输入祖先性别：(male/female)";
		readSex_fixed(t->person_sex);
		cout<<"输入其配偶姓名：";
		cin>>t->partner_name;

		if(t->person_sex=="male")
		    t->partner_sex="female";
		else
			t->partner_sex="male";
		root=t;
		root->next_sibling=NULL;
		root->first_child=NULL;
		root->front_parent=NULL;
		root->front_sibling=NULL;
		p=t;
        char* tmp = new char[10];
        for(int i = 0; i < t->person_name.length(); i++)
        {
            tmp[i] = t->person_name[i];
        }
        tree.insert(tmp);
        delete[] tmp;
	}
	cout<<"是否编辑下一代(Y/N)：";
	char is_continue;
	cin>>is_continue;
	if(is_continue=='Y'||is_continue=='y')
	{
		t=new binaryTreeNode;
		cout<<"输入"<<p->person_name<<"子女年龄:";
		cin>>t->person_num;
		cout<<"输入"<<p->person_name<<"子女姓名:";
		cin>>t->person_name;
		if(is_rename(t->person_name,root,0)==1)
		{
			cout<<"有重复，请重新输入"<<p->person_name<<"子女姓名:";
			cin>>t->person_name;
		}
		cout<<"输入"<<p->person_name<<"子女性别:";
		cin>>t->person_sex;
		cout<<"输入"<<t->person_name<<"配偶姓名:";
		cin>>t->partner_name;
		if(t->partner_sex=="male")
			t->partner_sex="female";
		else
			t->partner_sex="male";
		p->first_child=t;
		t->front_parent=p;
		t->front_sibling=NULL;
		p=t;
		p->first_child=NULL;
		p->next_sibling=NULL;
        char* tmp = new char[10];
        for(int i = 0; i < t->person_name.length(); i++)
        {
            tmp[i] = t->person_name[i];
        }
        tree.insert(tmp, 0, true);
        delete[] tmp;

	}
	else return;
	char choose;
    int pos = 1;
	while(1)
	{
		cout<<"※※※※※※※※※※※※※※※※※※※※※※※※※※"<<endl;
		cout<<"创建"<<p->person_name<<"的子女请按1"<<endl;
		cout<<"创建"<<p->person_name<<"的兄弟请按2"<<endl;
		cout<<"不再创建请按3"<<endl;
		cout<<"※※※※※※※※※※※※※※※※※※※※※※※※※※"<<endl;
		cin>>choose;
		switch(choose)
		{
		case '1':
			{
				t=new binaryTreeNode;
				cout<<"输入"<<p->person_name<<"子女年龄:";
				cin>>t->person_num;
				cout<<"输入"<<p->person_name<<"子女姓名:";
				cin>>t->person_name;
				if(is_rename(t->person_name,root,0)==1)
				{
					cout<<"有重复，请重新输入"<<p->person_name<<"子女姓名:";
					cin>>t->person_name;
				}
				cout<<"输入"<<p->person_name<<"子女性别:";
				readSex_fixed(t->person_sex);
				cout<<"输入"<<t->person_name<<"配偶姓名:";
				cin>>t->partner_name;
				if(t->partner_sex=="male")
					t->partner_sex="female";
				else
					t->partner_sex="male";
				p->first_child=t;
				t->front_parent=p;
				t->front_sibling=NULL;
				p=t;
				p->first_child=NULL;
				p->next_sibling=NULL;
                char* tmp = new char[10];
                for(int i = 0; i < t->person_name.length(); i++)
                {
                    tmp[i] = t->person_name[i];
                }
                tree.insert(tmp, pos++, true);
                delete[] tmp;
				break;
			}
		case '2':
			{
				t=new binaryTreeNode;
				cout<<"输入"<<p->person_name<<"兄弟年龄:";
				cin>>t->person_num;
				cout<<"输入"<<p->person_name<<"兄弟姓名:";
				cin>>t->person_name;
				if(is_rename(t->person_name,root,0)==1)
				{
					cout<<"有重复，请重新输入"<<p->person_name<<"子女姓名:";
				    cin>>t->person_name;
				}
				cout<<"输入"<<p->person_name<<"兄弟性别:";
				readSex_fixed(t->person_sex);
				cout<<"输入"<<t->person_name<<"配偶姓名:";
				cin>>t->partner_name;
				if(t->partner_sex=="male")
					t->partner_sex="female";
				else
					t->partner_sex="male";
				p->next_sibling=t;
				t->front_sibling=p;
		//		t->front_parent=NULL;
				p=t;
				p->next_sibling=NULL;
				p->first_child=NULL;
                char* tmp = new char[10];
                for(int i = 0; i < t->person_name.length(); i++)
                {
                    tmp[i] = t->person_name[i];
                }
                tree.insert(tmp, pos, false);
                delete[] tmp;
				break;
			}
		case '3':
			{
				cout<<"家谱树创建完毕……"<<endl;
				return;
			}
		}
	}
}

void binaryTree::showintree(binaryTreeNode *&root, int i) {
    cout << "家谱图如下所示：" << endl;
    cout << "-----------------------" << endl;
    vtree.draw(tree.root());

}
void binaryTree::show_binary_tree(binaryTreeNode *&root,int i)//ÏÔÊ¾£¨°¼Èë·¨£©¶þ²æÊ÷£¬²¢Ð´ÈëÎÄ¼þÖÐ
{
	fstream file("./family.txt",ios::app );
	if(!file)
	{
		cerr<<"文件没打开！"<<endl;
	}
	if(root)
	{
		int j;
		for( j=i; j>0; j--)
		{
			cout<<"   ";
			file<<"   ";
		}
        cout<<root->person_name<<endl;
		file<<root->person_name<<endl;
		show_binary_tree( root->first_child, i+1 );
		show_binary_tree( root->next_sibling, i );
	}
    file.close();
}

void binaryTree::search_all_information1(string num,binaryTreeNode *&root)//Ç°ÐòËÑË÷£¬²¢ÏÔÊ¾ÏêÏ¸ÐÅÏ¢
{
	if(root)
	{
		if(root->person_num==num)
		{
			binaryTreeNode *cur;
			cur=root;
			cout<<"-------------------------------------"<<endl;
		    cout<<"此人已找到，详细信息如下："<<endl;
			cout<<"年龄："<<root->person_num<<endl;
			cout<<"姓名："<<root->person_name<<endl;
			cout<<"性别："<<root->person_sex<<endl;
			cout<<"配偶："<<root->partner_name<<endl;
			cout<<"-------------------------------------"<<endl;
			if(cur->front_parent==NULL&&cur->front_sibling==NULL)
				cout<<root->person_name<<"为祖先，没有双亲！"<<endl;
			else
			{
				while(cur->front_sibling)
					cur=cur->front_sibling;
				cout<<root->person_name<<"的双亲为："<<endl;
			    if(cur->front_parent->person_sex=="male")
			    {  
				    cout<<root->person_name<<"的父亲："<<cur->front_parent->person_name<<endl;
				    cout<<root->person_name<<"的母亲："<<cur->front_parent->partner_name<<endl;
			    }
			    else
			    {
				    cout<<root->person_name<<"的父亲："<<cur->front_parent->partner_name<<endl;
				    cout<<root->person_name<<"的母亲："<<cur->front_parent->person_name<<endl;
			    }
		     }
			cout<<"-------------------------------------"<<endl;
			cur=root;
			if(cur->first_child==NULL)
				cout<<root->person_name<<"没有子女!"<<endl;
			else
			{
				cout<<root->person_name<<"的所有子女："<<endl;
				cur=root->first_child;
				cout<<cur->person_name<<endl;
				cur=cur->next_sibling;//·ÀÖ¹Ö»ÓÐÒ»¸öº¢×Ó
				while(cur)
				{
					cout<<cur->person_name<<endl;
					cur=cur->next_sibling;
				}
			}
			cout<<"-------------------------------------"<<endl;
			cur=root;
			if(root->front_sibling==NULL&&root->next_sibling==NULL)
			{
				if(root->front_sibling==NULL&&root->next_sibling==NULL&&root->front_parent==NULL)
					cout<<root->person_name<<"为祖先，没有兄弟！"<<endl;
				else
				    cout<<root->person_name<<"为独生子，没有兄弟"<<endl;
			}
			else
			{
				cout<<root->person_name<<"的所有兄弟："<<endl;
				
				while(cur->front_sibling)
				{
					cur=cur->front_sibling;
					cout<<cur->person_name<<endl;
				}
				cur=root;
				while(cur->next_sibling)
				{
					cur=cur->next_sibling;
					cout<<cur->person_name<<endl;
				}
			}
			cout<<"-------------------------------------"<<endl;
			return;
		}
		search_all_information1(num,root->first_child);
		search_all_information1(num,root->next_sibling);
	}
}

void binaryTree::search_all_information2(string name,binaryTreeNode *&root)//ºÍÉÏÒ»¸öº¯Êý²î²»¶à
{
	if(root)
	{
		if(root->person_name==name)
		{
			binaryTreeNode *cur;
			cur=root;
			cout<<"-------------------------------------"<<endl;
			cout<<"此人已找到，详细信息如下："<<endl;
			cout<<"年龄："<<root->person_num<<endl;
			cout<<"姓名："<<root->person_name<<endl;
			cout<<"性别："<<root->person_sex<<endl;
			cout<<"配偶："<<root->partner_name<<endl;
			cout<<"-------------------------------------"<<endl;
			if(cur->front_parent==NULL&&cur->front_sibling==NULL)
				cout<<root->person_name<<"为祖先，没有双亲！"<<endl;
			else
			{
				while(cur->front_sibling)
					cur=cur->front_sibling;
				cout<<root->person_name<<"的双亲为："<<endl;
				if(cur->front_parent->person_sex=="male")
				{  
					cout<<root->person_name<<"的父亲："<<cur->front_parent->person_name<<endl;
					cout<<root->person_name<<"的母亲："<<cur->front_parent->partner_name<<endl;
				}
				else
				{
					cout<<root->person_name<<"的父亲："<<cur->front_parent->partner_name<<endl;
					cout<<root->person_name<<"的母亲："<<cur->front_parent->person_name<<endl;
				}
			}
			cout<<"-------------------------------------"<<endl;
			cur=root;
			if(cur->first_child==NULL)
				cout<<root->person_name<<"没有子女!"<<endl;
			else
			{
				cout<<root->person_name<<"的所有子女："<<endl;
				cur=root->first_child;
				cout<<cur->person_name<<endl;
				cur=cur->next_sibling;//·ÀÖ¹Ö»ÓÐÒ»¸öº¢×Ó
				while(cur)
				{
					cout<<cur->person_name<<endl;
					cur=cur->next_sibling;
				}
			}
			cout<<"-------------------------------------"<<endl;
			cur=root;
			if(root->front_sibling==NULL&&root->next_sibling==NULL)
			{
				if(root->front_sibling==NULL&&root->next_sibling==NULL&&root->front_parent==NULL)
					cout<<root->person_name<<"为祖先，没有兄弟！"<<endl;
				else
					cout<<root->person_name<<"为独生子，没有兄弟"<<endl;
			}
			else
			{
				cout<<root->person_name<<"的所有兄弟："<<endl;
				while(cur->front_sibling)
				{
					cur=cur->front_sibling;
					cout<<cur->person_name<<endl;
				}
				cur=root;
				while(cur->next_sibling)
				{
					cur=cur->next_sibling;
					cout<<cur->person_name<<endl;
				}
			}
			cout<<"-------------------------------------"<<endl;
			return;
		}
		search_all_information2(name,root->first_child);
		search_all_information2(name,root->next_sibling);
	}
}

void binaryTree::search_all_height1(string num,binaryTreeNode *&root)//ºóÐø±éÀúËÑË÷£¬²¢ÏÔÊ¾ÆäµÚ¼¸´ú
{
	int height=0;
	if(root)
	{
		if(root->person_num==num)
		{
			binaryTreeNode *cur;
			cur=root;
			while(1)
			{
			   while(cur->front_sibling)
			   {
				   cur=cur->front_sibling;
			   }
			   if(cur->front_parent!=NULL)
			   {
				   height++;
				   cur=cur->front_parent;
			   }
			   else
				   break;
			}
			if(height==0)
				cout<<root->person_name<<"为祖先!"<<endl;
			else
				cout<<root->person_name<<"为第"<<height<<"代子孙!"<<endl;
			return;
		}
		search_all_height1(num,root->first_child);
		search_all_height1(num,root->next_sibling);
	}
}

void binaryTree::search_all_height2(string name,binaryTreeNode *&root)
{
	int height=0;//µÚ¼¸´ú
	if(root)
	{
		if(root->person_name==name)
		{
			binaryTreeNode *cur;
			cur=root;
			while(1)//ÈÃÆäÑ­»·£¬µ±cur->front_sibling=NULLÊ±£¬Ôò½øÈëÉÏÒ»´ú
			{
				while(cur->front_sibling)
				{
					cur=cur->front_sibling;
				}
				if(cur->front_parent!=NULL)
				{
					height++;
					cur=cur->front_parent;
				}
				else
					break;
			}
			if(height==0)
				cout<<root->person_name<<"为祖先!"<<endl;
			else
				cout<<root->person_name<<"为第"<<height<<"代子孙!"<<endl;
			return;
		}
		search_all_height2(name,root->first_child);
		search_all_height2(name,root->next_sibling);
	}
}

void binaryTree::add_child(string name,binaryTreeNode *&root)
{
    char* tem = new char[10];
    for(int i = 0; i < name.length(); i++)
    {
        tem[i] = name[i];
    }

	if(root)
	{
		if(root->person_name==name)
		{
			binaryTreeNode *cur,*child;
			child=new binaryTreeNode;
			cur=root;
			if(cur->first_child==NULL)//Èç¹û¸ÃÈËÃ»ÓÐº¢×Ó£¬ÔòÖ±½Ó´´½¨Æä×ÓÅ®
			{	
				cur->first_child=child;
				child->next_sibling=NULL;
				child->front_parent=root;
				child->front_sibling=NULL;
				child->first_child=NULL;
				cout<<"输入孩子年龄：";
				cin>>child->person_num;
				cout<<"输入孩子姓名：";
				cin>>child->person_name;
				cout<<"输入孩子性别：";
				readSex_fixed(child->person_sex);
		        cout<<root->partner_name<<"的孩子添加完毕"<<endl;
				tree.add_child(tem, tree.root(),const_cast<char*>(child->person_name.c_str()));
				delete[] tem;
			}
			else//·ñÔò£¬Ö±µ½cur->next_sibing=NULLÊ±£¬Ìí¼Óº¢×Ó
			{
				cur=cur->first_child;
				while(cur->next_sibling)
                {
                    cur=cur->next_sibling;
                }
				cur->next_sibling=child;
				child->first_child=NULL;
				child->next_sibling=NULL;
				child->front_sibling=cur;
				cout<<"输入孩子年龄：";
				cin>>child->person_num;
				cout<<"输入孩子姓名：";
				cin>>child->person_name;
				cout<<"输入孩子性别：";
				readSex_fixed(child->person_sex);
				cout<<root->partner_name<<"的孩子添加完毕"<<endl;
				tree.add_child(tem, tree.root(), const_cast<char*>(child->person_name.c_str()));
				delete[] tem;
			}
			return;
		}
        //level++;
		add_child(name,root->first_child);
		add_child(name,root->next_sibling);
	}
}