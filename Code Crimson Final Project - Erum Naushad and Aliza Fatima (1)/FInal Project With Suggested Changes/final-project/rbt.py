from collections import OrderedDict
import sys
from typing import Type, TypeVar
import time
import random 
from pprint import pprint
from collections import OrderedDict

class RBNode:
    def __init__(self, key, color="red"):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
    
    def is_null(self) -> bool:
        return not self.key

    def get_key(self):
        return self.key

    def get_color(self):
        return self.color


class RBTree:
    def __init__(self):
        self.NIL = RBNode(None, "black")
        self.root = self.NIL

    def get_root(self):
        return self.root

    def insert(self, key):
        node = RBNode(key)
        node.left = self.NIL
        node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        node.color = "red"
        self._fix_insert(node)

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._left_rotate(node.parent.parent)
        self.root.color = "black"

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def delete(self, key):
        node = self._search(self.root, key)
        if node != self.NIL:
            self._delete_node(node)

    def _delete_node(self, node):
        if node.left == self.NIL or node.right == self.NIL:
            y = node
        else:
            y = self._successor(node)

        if y.left != self.NIL:
            x = y.left
        else:
            x = y.right

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != node:
            node.key = y.key

        if y.color == "black":
            self._fix_delete(x)

    def _fix_delete(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == "red":
                    sibling.color = "black"
                    x.parent.color = "red"
                    self._left_rotate(x.parent)
                    sibling = x.parent.right
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    x = x.parent
                else:
                    if sibling.right.color == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self._right_rotate(sibling)
                        sibling = x.parent.right
                    sibling.color = x.parent.color
                    x.parent.color = "black"
                    sibling.right.color = "black"
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == "red":
                    sibling.color = "black"
                    x.parent.color = "red"
                    self._right_rotate(x.parent)
                    sibling = x.parent.left
                if sibling.right.color == "black" and sibling.left.color == "black":
                    sibling.color = "red"
                    x = x.parent
                else:
                    if sibling.left.color == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self._left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.color = x.parent.color
                    x.parent.color = "black"
                    sibling.left.color = "black"
                    self._right_rotate(x.parent)
                    x = self.root

        x.color = "black"

    def _successor(self, node):
        if node.right != self.NIL:
            return self._minimum(node.right)

        parent = node.parent
        while parent != self.NIL and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def _search(self, node, data):
        if node.is_null() or data == node.get_key():
            return node

        if data < node.get_key():
            return self._search(node.left, data)
        return self._search(node.right, data)

    def search(self, data) -> bool:
        return self._search(self.root, data).get_key() == data

    def print_tree(self) -> None:
        pprint(self.print_helper(self.root), sort_dicts=False)

    def print_helper(self, node) -> OrderedDict:
        if node.is_null():
            return dict()
        else:
            return dict(OrderedDict([
                ("root", (node.get_key(), node.get_color())),
                ("left", self.print_helper(node.left)),
                ("right", self.print_helper(node.right))]))


def gen_rand_rbt():
    random.seed(time.process_time())
    rbt = RBTree()
    num_nodes = random.randrange(8, 15)
    print(num_nodes)

    for i in range(num_nodes):
        rbt.insert(random.randrange(500))

    return rbt

# rbt = RBTree()
# rbt.insert(10)
# rbt.insert(5)
# rbt.insert(15)
# rbt.print_tree()