'''
双方向リストーインデックス

リスト内の要素にアクセスする方法-->線形探索
at関数-->i番目のインデックスを受け取りi+1番目のノードを返す関数
find関数-->キーを受け取って要素の中から最初のキーを検索する関数
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
        # 片方向リストと同じ処理
        for i in range(0, index):
            iterator = iterator.next
            if iterator == None : return None
        
        return iterator
    
    def printList(self):
        iterator = self.head
        while(iterator != None):
            print(iterator.data, end=" ")
            iterator = iterator.next
        print()

numList = DoublyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])
numList.printList()
print(numList.at(0).data)
print(numList.at(2).data)
print(numList.at(12).data)
        


