#ifndef POS_SETTER_H
#define POS_SETTER_H

#include "InfoH.h"

template<class TreeNode>
class PosSetter
{
public:
    PosSetter(TreeNode* TreeNode::* p, TreeNode *TreeNode::* l, TreeNode *TreeNode::* r) :
        parent(p), left(l), right(r)
    {
    }

    void operator() (TreeNode *node)
    {
        TreeNode *p = node->*parent;
        if (p != NULL) {
            if (node == p->*left)  { node->pos = p->pos - 1; }
            if (node == p->*right) { node->pos = p->pos + 1; }
        }
    }

private:
    TreeNode *TreeNode:: *parent;
    TreeNode *TreeNode:: *left;
    TreeNode *TreeNode:: *right;
};


#endif // POS_SETTER_H  
