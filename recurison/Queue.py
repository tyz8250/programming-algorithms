'''
キュー（Queue）は、FIFO（First-In-First-Out）の原則に従った線形データ構造
「最初に入ったものが最初に出てくる」という規則
Enqueue（エンキュー）: キューの末尾に新しい要素を追加。
Dequeue（デキュー）: キューの先頭の要素を削除し、その要素を返す。
'''


# ノードクラスを作成。このノードはキューの各要素を表現する。
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# キュークラスを作成。このキューはFIFO（先入れ先出し）の原則に従う。
class Queue:
    def __init__(self):
        # キューの先頭を表すノード
        self.head = None
        # キューの末尾を表すノード
        self.tail = None

    # キューの先頭を参照。キューが空の場合はNoneを返す。
    def peekFront(self):
        if self.head is None: return None
        return self.head.data

    # キューの末尾を参照。キューが空の場合は先頭を参照する。
    def peekBack(self):
        if self.tail is None: return self.peekFront()
        return self.tail.data

    def enqueue(self,data):
        # 新たなデータをキューの末尾に追加する。
        if self.head is None:
            # キューが空の場合は新たにノードを作成し、先頭と末尾に設定。
            self.head = Node(data)
            self.tail = self.head
        else:
            # そうでなければ新たなノードを末尾に追加。
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self):
        # キューの先頭のデータを取り出す。キューが空の場合はNoneを返す。
        if self.head is None: return None

        # 先頭のノードを一時的に保存。
        temp = self.head
        # 先頭を次のノードに移す。
        self.head = self.head.next
        # もしキューが空になった場合は、末尾もNoneに設定。
        if self.head is None: self.tail = None

        # 先頭から取り出したデータを返す。
        return temp.data

# キューを作成。
q = Queue()
# 最初にキューの先頭と末尾を表示。
print(q.peekFront())
print(q.peekBack())

# 4をキューに追加し、先頭と末尾を表示。
q.enqueue(4)
print(q.peekFront())
print(q.peekBack())

# 50をキューに追加し、先頭と末尾を表示。
q.enqueue(50)
print(q.peekFront())
print(q.peekBack())

# 64をキューに追加し、先頭と末尾を表示。
q.enqueue(64)
print(q.peekFront())
print(q.peekBack())

# キューからデータを取り出し、取り出したデータを表示。
print("dequeued :" + str(q.dequeue()))
# キューの先頭と末尾を表示。
print(q.peekFront())
print(q.peekBack())