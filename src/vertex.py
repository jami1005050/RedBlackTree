#Date: 21/10/2019
#Class: CS5310
#Assignment: Red black tree
#Author(s): Mohammad Jaminur Islam

from src.constant import RED


class Vertex:
    def __init__(self,value,color = RED): #red black tree node
        self.color = color #node color
        self.value = value #node value
        self.parent = None #node parent
        self.left_child = None # node left child
        self.right_child = None #node right child