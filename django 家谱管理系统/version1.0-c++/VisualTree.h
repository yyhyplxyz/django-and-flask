#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>
#include "ExtremumGetter.h"
#include "PosAdder.h"
#include "PosSetter.h"
#include "TreePrinter.h"

struct IntExtremumPair {
    int min;
    int max;
    IntExtremumPair(int rh1 = 0, int rh2 = 0) : min(rh1), max(rh2) {}
};

template<class TreeNode, class ValueType>
class VisualTree
{
public:
    typedef TreeNode *TreeNode::*           PtrToMember;
    typedef ValueType TreeNode::*           PtrToData;

    VisualTree(PtrToMember p, PtrToMember lc, PtrToMember rc, PtrToData val);

    void draw(TreeNode *node, const char *promot = NULL);

private:
    void                     adjust_pos(TreeNode *root);
    TreeNode*                ancestor(TreeNode *node);
    int                      digits(int n);
    int                      digits(char c);
    int                      digits(const char*s);
    IntExtremumPair          extreme_pos(TreeNode *p);
    ExtremumGetter<TreeNode> extreme_node(TreeNode *root);
    int                      scan_tree(TreeNode *root);
    template<class VST> void traverse_level(TreeNode *p, VST &vst);


    ExtremumGetter<TreeNode> getter;
    TreePrinter<TreeNode, ValueType> printer;
    PosSetter<TreeNode>      setter;
    PtrToMember              parent, left, right;
    ValueType TreeNode::    *value;
};

/*
 * 构造函数
 */
template<class TreeNode, class ValueType>
VisualTree<TreeNode, ValueType>::VisualTree(PtrToMember p, PtrToMember lc, PtrToMember rc, PtrToData val) :
    getter(), printer(p,lc,rc,val), setter(p,lc,rc), parent(p), left(lc), right(rc), value(val)
{
}

/*
 * 越界调整
 */
template<class TreeNode, class ValueType>
void VisualTree<TreeNode, ValueType>::adjust_pos(TreeNode *root)
{
    if (root == NULL) {
        return;
    }

    int diff = 0;
    IntExtremumPair extr;
    if (root->*left) {
        extr = extreme_pos(root->*left);
        if (root->pos <= extr.max) { // 左子树越界:将根节点右移及其右子树右移
            diff = extr.max - root->pos + 1;
            PosAdder adder(diff);
            root->add_pos(diff);
            traverse_level(root->*right, adder);
            adjust_pos(ancestor(root));
        }
    }

    if (root->*right) { // 右子树越界：将右字树右移
        extr = extreme_pos(root->*right);
        if (extr.min <= root->pos) {
            diff = root->pos - extr.min + 1;
            PosAdder adder(diff);
            traverse_level(root->*right, adder);
            adjust_pos(ancestor(root));
        }
    }
}

/*
 * 寻找节点node的第一个具有左孩子的祖先
 * @return 祖先地址或者NULL
 */
template<class TreeNode, class ValueType>
TreeNode *VisualTree<TreeNode, ValueType>::ancestor(TreeNode *node)
{
    TreeNode *pchild = node;
    TreeNode *pparent = node->*parent;
    while (pparent && pchild == pparent->*right) {
        pchild = pparent;
        pparent = pchild->*parent;
    }

    return pparent;
}

/*
 * 计算一个整数n输出时占用的字符数
 * @return 整数n输出时所占字符数
 */
template<class TreeNode, class ValueType>
int VisualTree<TreeNode, ValueType>::digits(int n)
{
    int len = 0;
    if (n < 0) {
        len++;
        n = -n;
    }
    do {
        len++;
        n /= 10;
    } while (n);
    return len;
}

/*
 * 输出一个字符所占用的字符数
 * @return 1
 */
template<class TreeNode, class ValueType>
int VisualTree<TreeNode, ValueType>::digits(char c)
{
    return 1;
}


/*
 * 输出一个字符串所占用的字符数
 * @return 字符串长度
 */
template<class TreeNode, class ValueType>
int VisualTree<TreeNode, ValueType>::digits(const char *s)
{
    return strlen(s);
}

/*
 * 图形化显示二叉树
 * @input root:树的根节点，promot:可选提示信息,应以'\0'结尾
 */
template<class TreeNode, class ValueType>
void VisualTree<TreeNode, ValueType>::draw(TreeNode *root, const char *promot)
{
    if (promot) {
        printf("%s\n", promot);
    }

    if (root == NULL) {
        printf("Empty tree!\n");
        return;
    }

    int len = scan_tree(root);

    printer.set_edge_length(len);
    traverse_level(root, printer);
}

/*
 * 获得最靠左和最靠右的两个节点指针
 * @return std::pair, 其中first指向最左节点，second指向最右节点
 */
template<class TreeNode, class ValueType>
ExtremumGetter<TreeNode>
VisualTree<TreeNode, ValueType>::extreme_node(TreeNode *node)
{
    getter.init(node, node);
    traverse_level(node, getter);
    return getter;
}

/*
 * 获得最靠左的节点和最靠右的节点pos
 * @return 包含最小/最大位置坐标的IntExtremumPair
 */
template<class TreeNode, class ValueType>
IntExtremumPair VisualTree<TreeNode, ValueType>::extreme_pos(TreeNode *node)
{
    ExtremumGetter<TreeNode> nodes = extreme_node(node);
    IntExtremumPair ret;
    if (nodes.min()) { ret.min = nodes.min()->pos; }
    if (nodes.max()) { ret.max = nodes.max()->pos; }
    return ret;
}

/*
 * 扫描整棵树，设置相关信息（换行标记/数据位数）
 * @return 最大数据位数
 */
template<class TreeNode, class ValueType>
int VisualTree<TreeNode, ValueType>::scan_tree(TreeNode *root)
{
    int                    cnt;     // 当前深度已扫描节点个数
    int                    depth;   // 当前扫描深度
    int                    max_len;
    std::queue<TreeNode*>  qnode;
    std::vector<int>       num_node;  // num_node[i]:  深度为i的节点总数

    num_node.push_back(1); // 一个根节点
    num_node.push_back(0); // 初始化第1层
    qnode.push(root);

    // 将根节点位置设为0，据此算出其他节点相对位置
    root->pos = 0;
    traverse_level(root, setter);

    // 获取最左最右坐标
    IntExtremumPair extr = extreme_pos(root);

    // 将最左节点坐标调整为0,其他节点整体右移
    PosAdder adder(root->pos - extr.min);
    traverse_level(root, adder);

    cnt = 0; depth = 0; max_len = 0;
    for ( ; !qnode.empty(); qnode.pop()) {
        TreeNode *temp = qnode.front();
        adjust_pos(temp);
        if (temp->*left)  {
            qnode.push(temp->*left);
            num_node[depth+1]++;
        }
        if (temp->*right) {
            qnode.push(temp->*right);
            num_node[depth+1]++;
        }

        if (++cnt == num_node[depth]) {
            temp->newline = true;
            depth++;
            num_node.push_back(cnt = 0); // 初始化下下层节点个数
        } else {
            temp->newline = false;
        }

        max_len = std::max(max_len, digits(temp->*value));
    }

    // 使树和屏幕左侧之间不留空隙
    extr = extreme_pos(root);
    if (extr.min > 0) {
        PosAdder adder(-extr.min);
        traverse_level(root,adder);
    }
    return max_len;
}

/*
 * 层次遍历二叉树，对树中每个节点执行操作vst
 */
template<class TreeNode, class ValueType>
template<class VST>
void VisualTree<TreeNode, ValueType>::traverse_level(TreeNode *root, VST &vst)
{
    if (root == NULL) {
        return;
    }

    TreeNode             *temp;
    std::queue<TreeNode*> qnode;
    for (qnode.push(root); !qnode.empty(); qnode.pop()) {
        temp = qnode.front();
        vst(temp);
        if (temp->*left)  { qnode.push(temp->*left); }
        if (temp->*right) { qnode.push(temp->*right); }
    }
}  
