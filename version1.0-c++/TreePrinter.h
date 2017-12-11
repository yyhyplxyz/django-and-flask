#ifndef TREE_PRINTER_H
#define TREE_PRINTER_H

template<class TreeNode, class ValueType>
class TreePrinter
{
public:
    typedef TreeNode *TreeNode::*PtrToMember;
    typedef ValueType TreeNode::*PtrToData;

    TreePrinter(PtrToMember p, PtrToMember l, PtrToMember r, PtrToData d) :
        edge_len(2), num_out(0), vec(), parent(p), left(l), right(r), value(d)
    {
    }

    void set_edge_length(int len)
    {
        edge_len = std::max(len, 2); // 边沿最小宽度为2
    }

    void operator() (TreeNode *node)
    {
        assert(node);
        TreeNode *lc = node->*left;
        TreeNode *rc = node->*right;
        int      lbl = 0, rbl = 0;  // 左边沿字符长度，右边沿字符长度
        int      spaces = node->pos * edge_len - num_out; // 占位空白字符数

        if (lc) { lbl = edge_len * (node->pos-(node->*left)->pos) - 1; }
        if (rc) { rbl = edge_len * ((node->*right)->pos-node->pos) - 1; }

        spaces -= lbl;
        assert(spaces >= 0);

        while (spaces--) {
            num_out += printf(" ");
        }

        if (node->*left) {
            vec.push_back(num_out-1);
            while (lbl--) {
                num_out += printf("_");
            }
        }

        num_out += out_value(node->*value);

        if (node->*right) {
            while (rbl--) {
                num_out += printf("_");
            }
            vec.push_back(num_out);
        }

        if (node->newline) {
            new_line();
        }
    }

private:
    int out_value(char c)        { return printf("%c", c); }
    int out_value(int i)         { return printf("%d", i); }
    int out_value(const char *p) { return printf("%s", p); }

    void new_line()
    {
         printf("\n");
         if (!vec.empty()) {
             int n = 0, end = vec[vec.size()-1];
             for (int i = 0; i <= end && n < (int)vec.size(); ++i) {
                 if (i == vec[n]) {
                     printf("|");
                     n++;
                 } else {
                     printf(" ");
                 }
             }
         }
         printf("\n");
         num_out = 0;
         vec.clear();
    }

    int                   edge_len;
    int                   num_out;   // 已输出字符数
    std::vector<int>      vec;
    PtrToMember           parent;
    PtrToMember           left;
    PtrToMember           right;
    ValueType TreeNode:: *value;
};

#endif // TREE_PRINTER_H  
