#Date: 21/10/2019
#Class: CS5310
#Assignment: Red black tree
#Author(s): Mohammad Jaminur Islam

import unittest

from src.redBlackTree import RedBlackTree
from src.vertex import Vertex


class MyTestCase(unittest.TestCase): #test rb insert and delete
    def test_vertex(self):
        vertex = Vertex(20) #node creation test
        assert isinstance(vertex,Vertex)
    def test_red_black_tree(self):
        redBlackTree = RedBlackTree() #red black tree creation
        assert isinstance(redBlackTree,RedBlackTree)

    def test_insert(self): #test insert for red black tree
        redBlackTree = RedBlackTree()  #initialize rb tree
        redBlackTree.insert_node(20) #insert 1 node
        assert redBlackTree.length == 1
        # print("redblack tree root",redBlackTree.root.value," color: ",redBlackTree.root.color)
        redBlackTree.insert_node(30)
        assert redBlackTree.length == 2
        # print("redblack tree right child", redBlackTree.root.right_child.value, " color: ", redBlackTree.root.right_child.color)
    def test_search_and_insert(self): #insert test and search
        redBlackTree = RedBlackTree()
        redBlackTree.insert_node(20)
        assert redBlackTree.length == 1
        # print("redblack tree root", redBlackTree.root.value, " color: ", redBlackTree.root.color)
        redBlackTree.insert_node(30)
        assert redBlackTree.length == 2
        redBlackTree.insert_node(10)
        assert redBlackTree.length == 3
        redBlackTree.insert_node(40)
        assert redBlackTree.length == 4
        redBlackTree.insert_node(50)
        assert redBlackTree.length == 5

        node40 = redBlackTree.search(40) #node search
        node10 = redBlackTree.search(10)
        node30 = redBlackTree.search(30)
        # print("vertex value: ",node10.value," color: ",node10.color)
        # print("vertex value: ", node40.value, " color: ", node40.color," parent: ",node40.parent.value)
        # print("vertex value: ", node30.value, " color: ", node30.color," parent: ",node30.parent.value)
        redBlackTree.insert_node(60)
        redBlackTree.insert_node(70)
        redBlackTree.insert_node(80)
        assert redBlackTree.length == 8 #check the number of nodes

        node20 = redBlackTree.search(20)
        node40 = redBlackTree.search(40)
        node60 = redBlackTree.search(30)
        # print("vertex value: ", node40.value, " color: ", node40.color, " parent: ", node40.parent.value)
        # print("vertex value: ", node20.value, " color: ", node20.color, " parent: ", node20.parent.value)
        # print("vertex value: ", node60.value, " color: ", node60.color," parent: ",node60.parent.value)


        redBlackTree.insert_node(6)
        redBlackTree.insert_node(15)
        redBlackTree.insert_node(18)
        redBlackTree.insert_node(35)
        redBlackTree.insert_node(27)
        redBlackTree.insert_node(29)
        redBlackTree.insert_node(25)
        redBlackTree.insert_node(11)
        redBlackTree.insert_node(12)
        redBlackTree.insert_node(13)
        redBlackTree.insert_node(14)
        # print("vertex value: ", node40.value, " color: ", node40.color, " parent: ", node40.parent.value)
        # print("vertex value: ", node20.value, " color: ", node20.color, " parent: ", node20.parent.value)
        # print("vertex value: ", node60.value, " color: ", node60.color," parent: ",node60.parent.value)


    def test_delete(self): #test delete node
        bst = RedBlackTree()
        bst.insert_node(55)
        bst.insert_node(40)
        bst.insert_node(65)
        bst.insert_node(60)
        bst.insert_node(75)
        bst.insert_node(57)
        print("After deleting an element")
        bst.deleteNode(40) #delete node 40
        bst.deleteNode(57) #delete node 40
        assert bst.length == 4

        print("root: ", bst.root.value, " root left:  ", bst.root.left_child.value," root right: ",bst.root.right_child.value)
    def test_min_node(self): #test min and max
        bst = RedBlackTree()
        bst.insert_node(55)
        bst.insert_node(40)
        bst.insert_node(65)
        bst.insert_node(60)
        bst.insert_node(75)
        bst.insert_node(57)
        node = bst.root
        node_min  = bst.min_node(node)
        max_node = bst.max_node(node)
        print("max: ",max_node.value," min: ",node_min.value)
        assert node_min.value == 40
        assert max_node.value == 75
if __name__ == '__main__':
    unittest.main()
