"""
スタックやキューのデータ構造
"""

class stack:
    """
    original stack class
    """
    def __init__(self):
        self.stack = []
    def push(self,item):
        return self.stack.append(item)
    def pop(self):
        #組み込み関数の「pop」は引数指定しない場合は、一番後ろから取り出す
        return self.stack.pop()
    def is_empty(self):
        return self.stack == []
    def size(self):
        return len(self.stack)
    def top(self):
        return self.stack[-1]

class queue:
    """
    original queue class
    """
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return self.queue == []
    def enqueue(self,item):
        return self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def size(self):
        return len(self.queue)