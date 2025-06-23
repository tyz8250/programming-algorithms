'''
双方向リストの挿入は片方向リスト同様にO(1)で実行可能
リストの最後にデータを追加するときは、リストの最後の部分がどこであるか知っている必要あり。
双方向リストが各要素（ノード）の前後に位置情報を持っているため。
新しいデータを最後に追加した場合、その位置情報（末尾）を更新しなければならない。
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, arr):
        if len(arr) <= 0:
            self.head = Node(None)
            self.tail = self.head
            return

        self.head = Node(arr[0])
        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            currentNode.next.prev = currentNode
            currentNode = currentNode.next

        self.tail = currentNode

    def at(self, index):
        iterator = self.head
        for i in range(0, index):
            iterator = iterator.next
            if iterator == None: return None

        return iterator
    
    # リストの先頭に追加
    def preappend(self, newNode):
        # 元の先頭ノードの前を新しいノードに設定。
        self.head.prev = newNode
        # 新しいノードの次を元の先頭ノードに設定。
        newNode.next = self.head
        # 新しいノードは先頭になるため、その前はNoneに設定。
        newNode.prev = None
        # 新しいノードをリストの新しい先頭に設定
        self.head = newNode

    # リストの最後に追加
    def append(self, newNode):
        # 元の末尾ノードの次を新しいノードに設定
        self.tail.next = newNode
        # 新しいノードは末尾になるため、その次はNoneに設定。
        newNode.next = None
        # 新しいノードの前を元の末尾ノードに設定。
        newNode.prev = self.tail
        # 新しいノードをリストの新しい末尾に設定。
        self.tail = newNode        

    # 与えられたノードの次に追加する。
    def addNextNode(self, node, newNode):
        # 指定されたノードの次のノードを一時的に保存。
        tempNode = node.next
        # 指定されたノードの次を新しいノードに設定。
        node.next = newNode
        # 新しいノードの次を保存していたノード（元の次のノード）に設定。
        newNode.next = tempNode
        # 新しいノードの前を指定されたノードに設定。
        newNode.prev = node
        # もし指定されたノードが末尾なら、新しいノードが新たな末尾になるため末尾を更新。
        if node is self.tail: 
            self.tail = newNode
        else: 
            # それ以外の場合は、一時的に保存していたノード（元の次のノード）の前を新しいノードに設定。
            tempNode.prev = newNode