import timeit
import random
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import sys
sys.setrecursionlimit(11000)

class Node:
    def __init__(self, data, parent=None):
        self.parent = parent
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, data):
        current = root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        new_node = Node(data, parent) 
        if root is None:
            root = new_node
        elif data <= parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        
        self.set_height(root)
            
        return root
    
    def search(self, root, data):
        current = root
        while current is not None:
            if data == current.data:
                return current
            elif data <= current.data:
                current = current.left
            else:
                current = current.right
        return None
    
    def insert_data(self, data):
        self.root = self.insert(self.root, data)
        
    def search_data(self, data):
        return self.search(self.root, data)
    
    def set_height(self, root):
        if root is not None:
            self.set_height(root.left)
            self.set_height(root.right)
            root.height = 1 + max(self.height(root.left), self.height(root.right))
        
def doTasks(tree, tasks):
    for task in tasks:
        tree.search_data(task)

if __name__ == "__main__":
    largest_absolute_balances = []
    
    tasks = list(range(1000))
    
    avg_times = []
    
    for i in range(1000):
        tree = AVLTree()
        random.shuffle(tasks)
        for task in tasks:
            tree.insert_data(task)
        
        largest_absolute_balance = abs(tree.balance(tree.root))
        largest_absolute_balances.append(largest_absolute_balance)
        time = timeit.timeit(lambda: doTasks(tree, tasks), number=1)
        avg = time
        avg_times.append(avg)
        
        df_data = np.array([[avg, largest_absolute_balance]])
        df = pd.DataFrame(df_data, columns=['avg time (ms)', 'largest absolute balance'])
        print(df.to_string(index=False))

    ax = plt.figure().add_subplot()
    ax.scatter(largest_absolute_balances, avg_times,  c="red")
    ax.set_title("largest absolute balance vs. average time")
    ax.set_xlabel("largest absolute balance")
    ax.set_ylabel("average time (ms)")
    ax.set_xlim(0)
    ax.set_ylim(0)
    plt.show()