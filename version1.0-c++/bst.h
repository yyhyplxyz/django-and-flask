#ifndef BST_H  // binary search tree
#define BST_H

#include <cassert>
#include <algorithm> // swap
#include "InfoH.h"
#include <string.h>
#define IS_ROOT(p)   ((p)->parent == NULL)
#define IS_LEAT(p)   ((p)->left == NULL && (p)->right == NULL)
#define IS_LEFT(p)   (!IS_ROOT(p) && (p) == (p)->parent->left)
#define IS_RIGHT(p)  (!IS_ROOT(p) && (p) == (p)->parent->right)

template<typename T>
struct TreeNode : public InfoH {
    T        val;
    TreeNode *parent;
    TreeNode *left;
    TreeNode *right;

    TreeNode(const T v) : InfoH(), val(v), parent(0), left(0), right(0) {}
    TreeNode(const T v, TreeNode *p) : InfoH(), val(v), parent(p), left(0), right(0) {}
};

template<typename T>
class BSTree
{
public:
    /*
     * 构造函数
     */
    BSTree() : root_(0) {}

    /*
     * 析构函数
     */
    virtual ~BSTree()
    {
        while (!empty()) {
            remove(root_);
        }
    }

    /*
     * 判断树是否为空
     * @return true:空, false:非空
     */
    bool empty()
    {
        return root_ == NULL;
    }
    /*
    *  对左右子树进行交换
    *
    */
    void Interchange(TreeNode<T>* bt)
    {
      if(bt)
      {
        Interchange(bt->left);
        Interchange(bt->right);
        TreeNode<T>* p = bt->left;
        TreeNode<T>* q = bt->right;
        bt->left = q;
        bt->right = p;
      }
      else
      return;
    }
void add_child(char* elem, TreeNode<T>* ru, char* name)
{
    if(ru)
    {
        if(strcmp(ru->val, elem))
        {
           TreeNode<T>* cur;
            cur=ru;
            if(cur->left==NULL)//如果该人没有孩子，则直接创建其子女
            {
                cur->left=new TreeNode<T> (name, cur);
            }
            else//否则，直到cur->next_sibing=NULL时，添加孩子
            {
                cur=cur->left;
                if(cur->right)
                {
                    cur->right = new TreeNode<T> (name, cur);
                }
                else{
                    while(cur->right)
                    {
                        cur=cur->right;
                    }
                    cur->right = new TreeNode<T> (name, cur);
                }
            }
            return;
        }
        //level++;
        add_child(elem,ru->left, name);
        add_child(elem,ru->right, name);
    }
}

    /*
     * 插入一个新节点
     * @return 新插入节点地址
     */

    TreeNode<T> *insert(const T va, int pos=0, bool isdescendant = true)
    {
        T val = new char[10];
        strcpy(val, va);
        if (root_ == NULL && pos == 0) {
            return root_ = new TreeNode<T>(val);
        }
        else
        {
            TreeNode<T> *parent = root_;
            while(pos--)
            {
                parent = root_->left;
            }
            if(isdescendant)
            {
                return parent->left = new TreeNode<T>(val, parent);
            }
            else
            {
                return parent->right =  new TreeNode<T>(val, parent);
            }
        }

      /*  TreeNode<T> *parent = root_;
        TreeNode<T> *hole = 0;

        hole = (root_->val < val ? root_->right : root_->left);
        while (hole != NULL) {
            parent = hole;
            hole = (hole->val < val ? hole->right : hole->left);
        }

        if (parent->val < val) {
            return parent->right = new TreeNode<T>(val, parent);
        } else {
            return parent->left = new TreeNode<T>(val, parent);
        }*/
    }

    /*
     * 寻找值为x的节点
     * @reutrn 节点地址,如果不存在返回NULL
     */
    TreeNode<T> *find(T &x)
    {
        TreeNode<T> *temp = root_;
        while (temp != NULL) {
            if (temp->val == x) {
                break;
            }
            temp = (temp->val < x ? temp->right : temp->left);
        }
        // temp == NULL
        return temp;
    }

    /*
     * 删除指定节点
     */
    void remove(TreeNode<T> *p)
    {
        assert(p != NULL);

        TreeNode<T> *temp = NULL;
        if (p->left && p->right) {          // 有两个孩子
            TreeNode<T> *temp = succ(p);
            std::swap(p->val, temp->val);   // 交换和后继节点的内容
            remove(temp);                   // 删除后继节点
        } else if (p->left || p->right) {   // 只有一个孩子
            temp = (p->left ? p->left : p->right);
            if (IS_ROOT(p)) {
                root_ = temp;
                root_->parent = NULL;
            } else if (IS_LEFT(p)) {
                p->parent->left = temp;
                temp->parent = p->parent;
            } else {
                p->parent->right = temp;
                temp->parent = p->parent;
            }
            delete p;
        } else { // 没有孩子
            if (IS_ROOT(p)) {
                root_ = NULL;
            } else if (IS_LEFT(p)) {
                p->parent->left = NULL;
            } else {
                p->parent->right = NULL;
            }
            delete p;
        }
    }

    /*
     * 返回根节点地址
     */
    TreeNode<T>*root() const
    {
        return root_;
    }
private:
    /*
     * 寻找最小节点
     * @reutrn 最小节点地址
     */
    TreeNode<T> *min_node(TreeNode<T> *p)
    {
        assert(p != NULL);
        TreeNode<T> *temp = p;
        while (temp->left != NULL) {
            temp = temp->left;
        }
        return temp;
    }

    /*
     * 寻找最大节点
     * @return 最大节点地址
     */
    TreeNode<T> *max_node(TreeNode<T> *p)
    {
        assert(p != NULL);
        TreeNode<T> *temp = p;
        while (temp->right != NULL) {
            temp = temp->right;
        }
        return temp;
    }

    /*
     * 寻找指定节点p的后继节点（比p节点大的所有节点中的最小节点）
     * @return 后继节点地址
     */
    TreeNode<T> *succ(TreeNode<T> *p)
    {
        assert(p != NULL);
        if (p->right) {    // 节点有右子树：右子树中最小节点即为后继节点
            return min_node(p->right);
        }
        // else
        TreeNode<T> *child = p;
        TreeNode<T> *father = p->parent;
        while (father && !IS_LEFT(child)) { // 节点无右子树：第一个有左孩子的祖先节点即为后继节点
            child = father;
            father = child->parent;
        }
        return father;
    }

    TreeNode<T> *root_;
};

#endif
