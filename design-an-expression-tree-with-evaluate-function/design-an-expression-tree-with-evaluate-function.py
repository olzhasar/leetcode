import abc 
from abc import ABC, abstractmethod 
import operator

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class TreeNode(Node):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def get_func(self, val):
        if val == '+':
            return operator.add
        if val == '-':
            return operator.sub
        if val == '*':
            return operator.mul
        if val == '/':
            return operator.floordiv
        raise ValueError(f"Unsupported operator {val}")

    def evaluate(self):
        if not self.left:
            return int(self.val)
        
        return self.get_func(self.val)(self.left.evaluate(), self.right.evaluate())

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        
        for val in postfix:
            if val.isnumeric():
                node = TreeNode(val)
            else:
                node = TreeNode(val, right=stack.pop(), left=stack.pop())
            stack.append(node)
        
        return stack[0]
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""