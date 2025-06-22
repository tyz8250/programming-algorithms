'''
双方向リストは、各ノードが次のノードへの単一ポインタだけでなく、前のノードへのポインタも含む。
片方向リストを逆方向に辿る場合、リストの末尾からポインタをたどっていく必要があり、不便。
双方向リストでは適切なポインタをたどるだけで、リストをどちらの方向にもたどることができる。
'''

class Node:
    def __init__(self,data):
        # データフィールドの定義
        self.data = data
        # prevフィールドはリストの中でこのノードの前に存在するノードを指す。
        self.prev = None
        # nextフィールドはリストの中でこのノードの後に存在するノードを指す。
        self.next = None

class DoublyLinkedList:
    def __init__(self, arr):
        # 双方リストは、先頭と末尾のノードを追跡する。
        # 空の配列が渡された場合、データとしてNoneを持つ単一のノードを作成する。
        if len(arr) <= 0:
            self.head = Node(None)
            self.tail = self.head
            return
        
        # リストの初めのノードを作成
        self.head = Node(arr[0])
        currentNode = self.head

        # 残りの要素に対し、各ノードを作成し、前のノードとリンク
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            #次のノードのprevフィールドを現在のノードにリンクさせる
            currentNode.next.prev = currentNode
            currentNode = currentNode.next

        # 末尾のノードを追跡する。
        self.tail = currentNode

    # リストの内容を表示するメソッド
    def printList(self):
        iterator = self.head;
        while(iterator != None):
            print(iterator.data, end=" ")
            iterator = iterator.next
        print()

numList = DoublyLinkedList([35,23,546,67,86,234,56,767,34,1,98,78,555])

# リストの内容を表示する
numList.printList()

# リストの先頭とその次のノードのデータを表示
print(numList.head.data)
print(numList.head.next.data)

# リストの末尾とその前のノードのデータを表示
print(numList.tail.data)
print(numList.tail.prev.data)