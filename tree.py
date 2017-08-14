# -*- coding:utf-8 -*
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preTraverse(root):
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)

def prestack(root):
    if root == None:
        return
    stack=[]
    node=root
    while node or stack:
        while node:
            print(node.value)
            stack.append(node)
            node=node.left

        node=stack.pop()
        node=node.right

def afterstack(root):
    if root == None:
        return
    stack=[]
    stack_m = []
    node=root
    while node or stack:
        while node:
            stack_m.append(node.value)
            stack.append(node)
            node=node.right

        node=stack.pop()
        node=node.left
    while stack_m:
        print (stack_m.pop())


def level_queue( root):

    if root == None:
        return
    myQueue = []
    node = root
    myQueue.append(node)
    while myQueue:
        node = myQueue.pop(0)
        print (node.value)
        if node.left != None:
            myQueue.append(node.left)
        if node.right != None:
            myQueue.append(node.right)

def middlestack(root):
    if root == None:
        return
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        print(node.value)
        node = node.right

def midTraverse(root):
    if root == None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)

def afterTraverse(root):
    if root == None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)


if __name__=='__main__':
    root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    print('前序遍1111历：')
    preTraverse(root)
    print('\n')

    print('前序遍历：')
    prestack(root)
    print('\n')


    print('中序遍历：')
    middlestack(root)
    print('\n')

    print('中序遍2222历：')
    midTraverse(root)
    print('\n')

    print('后序遍历：')
    afterTraverse(root)
    print('\n')


    print('afterstack：')
    afterstack(root)

    print('level_queue：')
    level_queue(root)