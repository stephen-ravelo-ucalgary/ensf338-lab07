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
        pivot = None
        pivot_balance = None

        while current is not None:
            parent = current
            if self.balance(current) != 0:
                pivot = current
                pivot_balance = self.balance(pivot)
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

        # Case 1: No Pivot
        if pivot == None:
            print("Case #1: Pivot not detected")

        # Case 2: Pivot exists and adding to the shorter subtree
        elif pivot_balance == -1 and data < pivot.data:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")

        elif pivot_balance == 1 and data > pivot.data:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")

        # Case 3: Pivot exists and adding to the longer subtree
        else:
            print("Case #3: Not supported")


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
    tree = AVLTree()

    # Case 1
    tree.insert_data(5)     # test 1
    tree.insert_data(3)

    # Case 2
    tree.insert_data(7)     # test 2
    tree.insert_data(8)
    tree.insert_data(6)     # test 3

    # Case 3
    tree.insert_data(1)
    tree.insert_data(0)     # test 4
