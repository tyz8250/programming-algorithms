'''
スタックはLIFOの原則に従った線形のデータ構造。
スタックに追加された最後の要素が、最初に削除される要素と一致する。
'''

# Nodeという名前のクラスを定義。これはスタックの各要素を表す。
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stackという名前のクラスを定義。これはスタック全体を表す。
class Stack:
    # Stackクラスのインスタンスを作成するとき、最初はヘッド（一番上の要素）が存在しない状態になる。
    def __init__(self):
        self.head = None
    
    # pushというメソッドを定義。これは新しい要素をスタックの一番上に追加するためのもの。
    def push(self,data):
        # 現在のヘッドを一時的に保存。
        temp = self.head
        # 新しいNodeを作成し、それを新しいヘッドとする。
        self.head = Node(data)
        # 新しいヘッドの次のNodeとして、元のヘッドを設定する。
        self.head.next = temp
    
    # popというメソッドを定義。これはスタックの一番上の要素を取り出すためのもの。
    def pop(self):
        # スタックが空の場合、何も取り出せないのでNoneを返す。
        if self.head == None: return None
        # 現在のヘッドを一時的に保存。
        temp = self.head
        # ヘッドの次のNode（つまり、2番目の要素）を新しいヘッドとする。
        self.head = self.head.next
        # 保存しておいた元のヘッド（つまり、取り出された要素）のデータを返す。
        return temp.data
    
    # peekというメソッドを定義。これはスタックの一番上の要素を確認するためのもの。
    def peek(self):
        # スタックが空の場合、確認できる要素がないのでNoneを返す。
        if self.head is None: return None
        # 現在のヘッド（つまり、一番上の要素）のデータを返す。
        return self.head.data
    
    # 新しいスタックを作成。
s = Stack()

# スタックに2を追加。
s.push(2)
# スタックの一番上の要素（つまり、今は2）を確認する。この時点では、printは2を出力。
print(s.peek())

# スタックに4を追加。今、スタックの一番上の要素は4になる。
s.push(4)
# スタックに3を追加。今、スタックの一番上の要素は3になる。
s.push(3)
# スタックに1を追加。今、スタックの一番上の要素は1になる。
s.push(1)

# スタックの一番上の要素を取り出す。取り出した要素は1なので、次に一番上にくる要素は3になる。
s.pop()
# スタックの一番上の要素（つまり、今は3）を確認。この時点では、printは3を出力する。
print(s.peek())