#ifndef EXTREMUM_GETTER_H
#define EXTREMUM_GETTER_H

template<class TreeNode>
class ExtremumGetter
{
public:
    ExtremumGetter(TreeNode *min = 0, TreeNode *max = 0) {
        init(min, max);
    }

    void operator() (TreeNode *p) {
        if ((min_ && p->pos < min_->pos) || !min_) { min_ = p; }
        if ((max_ && p->pos > max_->pos) || !max_) { max_ = p; }
    }

    void init(TreeNode *min, TreeNode *max) {
        min_ = min; max_ = max;
        if (min_ && max_ && max_->pos < min_->pos) {
            std::swap(min_, max_);
        }
    }

    TreeNode *min() const { return min_; }
    TreeNode *max() const { return max_; }

private:
    TreeNode *min_;
    TreeNode *max_;
};

#endif // EXTREMUM_GETTER  
