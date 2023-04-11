import sys
input = sys.stdin.readline

n = int(input())
tree = {}

class Node:
    def __init__(self, data, leftNode, rightNode):
        self.data = data
        self.leftNode = leftNode
        self.rightNode = rightNode
        
def preOrder(node):
    print(node.data, end="")
    if node.leftNode != None:
        preOrder(tree[node.leftNode])
    if node.rightNode != None:
        preOrder(tree[node.rightNode])
        
def inOrder(node):
    if node.leftNode != None:
        inOrder(tree[node.leftNode])
    print(node.data, end="")
    if node.rightNode != None:
        inOrder(tree[node.rightNode])
        
def postOrder(node):
    if node.leftNode != None:
        postOrder(tree[node.leftNode])
    if node.rightNode != None:
        postOrder(tree[node.rightNode])
    print(node.data, end="")
        
for _ in range(n):
    data, left, right = map(str, input().split())
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[data] = Node(data, left, right)
    
preOrder(tree['A'])
print()
inOrder(tree['A'])
print()
postOrder(tree['A'])
