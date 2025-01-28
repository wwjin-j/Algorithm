import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node):
    if node is not None:
        print(node.value, end="")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.value, end="")
        inorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end="")

n = int(input())
tree = {}

for _ in range(n):
    parent, left, right = input().split()
    if parent not in tree:
        tree[parent] = Node(parent)
    if left != ".":
        tree[left] = Node(left)
        tree[parent].left = tree[left]
    if right != ".":
        tree[right] = Node(right)
        tree[parent].right = tree[right]

root = tree["A"]

preorder(root)
print()
inorder(root)
print()
postorder(root)