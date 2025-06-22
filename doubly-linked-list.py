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
