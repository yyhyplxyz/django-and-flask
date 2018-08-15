cmake_minimum_required(VERSION 3.8)
project(shiyan5_2)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        binaryTree.cpp
        binaryTree.h
        binaryTreeNode.h
        bst.h
        ExtremumGetter.h
        InfoH.h
        main.cpp
        person_information.h
        PosAdder.h
        PosSetter.h
        TreePrinter.h
        VisualTree.h)

add_executable(shiyan5_2 ${SOURCE_FILES})