#include <iostream>
#include "binaryTree.h"
using namespace std;
void show_contents()//Ä¿Â¼
{
        cout<<"              ※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※"<<endl;
        cout<<"              ※ 1、创建家谱树                                 ※"<<endl;
        cout<<"              ※ 2、显示家谱树                               ※"<<endl;
        cout<<"              ※ 3、查询(输出双亲、所有子女、所有兄弟结点信息) ※"<<endl;
        cout<<"              ※ 4、查询(是祖先的第几代子孙)                   ※"<<endl;
        cout<<"              ※ 5、增加孩子                                   ※"<<endl;
        cout<<"              ※ 6、退出家谱图                                 ※"<<endl;
        cout<<"              ※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※"<<endl;
        cout<<"请输入你的选择：";
        char choose;
}

int main()
{
	binaryTree tree;
	while(1)
	{
		 show_contents();
	     //cout<<"ÇëÊäÈëÄãµÄÑ¡Ôñ£º";
	     char choose;
	     cin>>choose;
	     switch(choose)
	     {
	     case '1'://´´½¨¶þ²æÊ÷
		    {
			    tree.creat_binary_tree(tree.root);
			    break;
		    }
	     case '2'://ÏÔÊ¾¶þ²æÊ÷£¨Ç°Ðò±éÀúÏÔÊ¾£©
		    {
			    tree.show_binary_tree(tree.root,0);
				tree.showintree(tree.root,0);
			    break;
		    }
	     case '3'://ÊÕË÷£¨Ç°Ðò±éÀúËÑË÷£©
		    {
                cout<<"******************************************"<<endl;
                cout<<" 1、年龄搜索     2、姓名搜索              "<<endl;
                cout<<"******************************************"<<endl;
                cout<<"请输入你的选择：";
				char choose_num_information;
				cin>>choose_num_information;
				if(choose_num_information=='1')//±àºÅËÑË÷£¬²¢ÏÔÊ¾ÏêÏ¸ÐÅÏ¢
				{
				     cout<<"输入年龄：";
				     string num;
				     cin>>num;
				     tree.search_all_information1(num,tree.root);
				}
				if(choose_num_information=='2')//ÐÕÃûËÑË÷£¬²¢ÏÔÊ¾ÏêÏ¸ÐÅÏ¢
				{
				    cout<<"输入姓名：";
					string name;
					cin>>name;
					tree.search_all_information2(name,tree.root);
				}
			    break;
		    }
	     case '4'://ËÑË÷£¨Ç°Ðò£©£¬²¢ÏÔÊ¾ÆäÎªµÚ¼¸´ú
		    {
				cout<<"******************************************"<<endl;
                cout<<" 1、年龄搜索第几代     2、姓名搜索第几代  "<<endl;
                cout<<"******************************************"<<endl;
                cout<<"请输入你的选择：";
				char choose_num_height;
				cin>>choose_num_height;
				if (choose_num_height=='1')//±àºÅËÑË÷£¬²¢ÏÔÊ¾µÚ¼¸´ú
				{
					cout<<"输入年龄：";
					string num;
					cin>>num;
					tree.search_all_height1(num,tree.root);
				}
				if (choose_num_height=='2')//ÐÕÃûËÑË÷£¬²¢ÏÔÊ¾µÚ¼¸´ú
				{
					cout<<"输入姓名：";
					string name;
					cin>>name;
					tree.search_all_height2(name,tree.root);
				}
			    break;
		    }
	     case '5'://Ôö¼Óº¢×Ó½Úµã
		    {
				cout<<"你要为哪个人增加孩子（输入其姓名）:";
				string person_add;
				cin>>person_add;
				tree.add_child(person_add,tree.root);

			    break;
		    }
		 case '6':
		    {
				return 0;
		    }
	     }
	}
	return 0;
}
