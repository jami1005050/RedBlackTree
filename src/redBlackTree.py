#Date: 21/10/2019
#Class: CS5310
#Assignment: Red black tree
#Author(s): Mohammad Jaminur Islam


from src.constant import NOCOLOR, BLACK, RED
from src.vertex import Vertex


class RedBlackTree:
    def __init__(self,rootValue = None):

        self.nil = Vertex(None,BLACK) #for assigning null childs
        if (rootValue is None):
            self.root = self.nil
        else:
            self.root = Vertex(rootValue)
        self.length = 0 #to keep track of the number of nodes

    def search(self,value, x=None):#search a node from start or from a given node
        # v = self.root.value
        if x is None:  #if given node is null
            # print("x is none")
            x = self.root
        # print("x: ",x.value," v: ",v)
        while x != self.nil and value != x.value: #check until not found a match upto leaf nodes
            if value < x.value: #if searched value is less then root
                x = x.left_child
                # print("left: ",x.value)

            else: #if searched value is greater than or equal root
                x = x.right_child
                # print("right: ",x.value)

        return x

    def insertFixup(self, z): #fixup to keep the red black structure that is
        # Every node is either red or black. The root is black. Every leaf(NIL) is black. If a node is red, then both
        # its children are black.For each node, all simple paths from the node to descendant leaves contain the same
        # number of black nodes.~~~ from coreman~~~
        # print("for Z: ",z.value)
        while z.parent.color == RED:
            # print("..executing..")
            if z.parent == z.parent.parent.left_child:
                # print("z parent is equal to z's parents parents left")
                y = z.parent.parent.right_child
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:

                    if z == z.parent.right_child:
                        z = z.parent
                        self.leftRotate(z)
                    z.parent.red = BLACK
                    z.parent.parent.color = RED
                    self.rightRotate(z.parent.parent)
            else:
                # print("z parent is equal to z's parents parents right")
                y = z.parent.parent.left_child
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left_child:
                        z = z.parent
                        self.rightRotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.leftRotate(z.parent.parent)
        self.root.color = BLACK

    def leftRotate(self, x):
        "Left rotate x."
        y = x.right_child
        x.right_child = y.left_child
        if y.left_child != self.nil:
            y.left_child.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left_child:
            x.parent.left_child = y
        else:
            x.parent.right_child = y
        y.left_child = x
        x.parent = y

    def rightRotate(self, y):
        "Left rotate y."
        x = y.left_child
        y.left_child = x.right_child
        if x.right_child != self.nil:
            x.right_child.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.right_child:
            y.parent.right_child = x
        else:
            y.parent.left_child = x
        x.right_child = y
        y.parent = x

    def insert_node(self, z): #insert a node by its value
        y = self.nil
        x = self.root #fetch the root
        vertex = Vertex(z) #create a node
        while x != self.nil: #only execute when root exist
            y = x
            if vertex.value < x.value:#find the insertion position by checking the values
                x = x.left_child
            else:
                x = x.right_child
        vertex.parent = y #initially put the null parent in case have some node in the tree
        # it will set the parent found from the above for loop
        if y == self.nil:
            # print("y is equal nil")
            self.root = vertex #if its first insert make it root
        elif vertex.value < y.value: #otherwise make the current vertex as left child as lesser than parent
            y.left_child = vertex
        else:
            y.right_child = vertex
        vertex.left_child = self.nil #set the left and right child as nil and set the color as red
        vertex.right_child = self.nil
        vertex.color = RED
        self.length = self.length + 1
        self.insertFixup(vertex) #after insertion some fixup done by this function

    def deleteFixup(self, x): #delete fixup
        while x != self.root and x.color == BLACK:
            if x == x.parent.left_child:
                s = x.parent.right_child
                if s.color == RED:
                    s.color = BLACK
                    x.parent.color = RED
                    self.leftRotate(x.parent) #rotate left
                    s = x.parent.right_child
                if s.left_child.color == 0 and s.right_child.color == RED:
                    s.color = BLACK
                    x = x.parent
                else:
                    if s.right_child.color == BLACK:
                        s.left_child.color = BLACK
                        s.color = RED
                        self.rightRotate(s) #rotate right
                        s = x.parent.right_child
                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.right_child.color = BLACK
                    self.leftRotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left_child
                if s.color == RED:
                    s.color = BLACK
                    x.parent.color = RED
                    self.rightRotate(x.parent)
                    s = x.parent.left_child
                if s.right_child.color == BLACK and s.right_child.color == BLACK:
                    s.color = RED
                    x = x.parent
                else:
                    if s.left_child.color == BLACK:
                        s.right_child.color = BLACK
                        s.color = RED
                        self.leftRotate(s)
                        s = x.parent.left_child
                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.left_child.color = BLACK
                    self.rightRotate(x.parent)
                    x = self.root
        x.color = BLACK

    def redBlackTransplant(self, u, v):#change the node parent and make the target node free for delete
        if u.parent == None:
            self.root = v
        elif u == u.parent.left_child:
            u.parent.left_child = v
        else:
            u.parent.right_child = v
        v.parent = u.parent

    def deleteNode(self, value): #delete node
        z = self.search(value) #search the node
        if z == self.nil:
            print("Couldn't find key in the tree")
            return
        y = z
        redOrBlack = y.color
        if z.left_child == self.nil: #adjust nodes if left node nil
            x = z.right_child
            self.redBlackTransplant(z, z.right_child)
        elif (z.right_child == self.nil): #adjust node if right node nil
            x = z.left_child
            self.redBlackTransplant(z, z.left_child)
        else: #if no nodes nil then adjust the node
            print("neither child is null")
            y = self.min_node(z.right_child)
            print("min node is: ",y.value)
            redOrBlack = y.color
            x = y.right_child
            if y.parent == z:
                x.parent = y
            else:
                self.redBlackTransplant(y, y.right_child)
                y.right_child = z.right_child
                y.right_child.parent = y
            self.redBlackTransplant(z, y)
            y.left_child = z.left_child
            y.left_child.parent = y
            y.color = z.color
        if redOrBlack == BLACK:
            print("calling a deletion fixup with x",x.value)
            self.deleteFixup(x) #fix the colors after delete
        self.length =self.length -1

    def min_node(self, node): #return the min node
        while node.left_child != self.nil: #go until found the lowest
            node = node.left_child
        return node

    def max_node(self, node):#return the max node
        while node.right_child != self.nil:
            node = node.right_child
        return node

    def successor_node(self, x): #return successor
        if x.right_child != self.nil:
            return self.min_node(x.right_child)
        y = x.parent
        while y != self.nil and x == y.right_child:
            x = y
            y = y.parent
        return y

    def predecessor_node(self, x): #return predecessor
        if (x.left_child != self.nil):
            return self.max_node(x.left_child)
        y = x.parent
        while y != self.TNULL and x == y.left_child:
            x = y
            y = y.parent
        return y


if '__main__' == __name__:
    pass