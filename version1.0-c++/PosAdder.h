#ifndef POS_ADDER_H
#define POS_ADDER_H

#include "InfoH.h"

class PosAdder
{
public:
    PosAdder(int n_) : n(n_) {}
    int operator() (InfoH *node) { return node->add_pos(n); }
private:
    int n;
};

#endif // POS_ADDER_H  
