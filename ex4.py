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

    def left_rotate(self, pivot):
        son = pivot.right
        if(son is None):
            return pivot

        pivot.right = son.left
        if(son.left):
            son.left.parent = pivot
        
        son.parent = pivot.parent
        if(pivot.parent is None):
            self.root = son
        else:
            if(pivot == pivot.parent.left):
                pivot.parent.left = son
            else:
                pivot.parent.right = son
        
        son.left = pivot
        pivot.parent = son
        
        self.set_height(pivot)
        self.set_height(son)
        return son
    
    def right_rotate(self, pivot):
        son = pivot.left
        if(son is None):
            return pivot
        
        pivot.left = son.right
        if(son.right):
            son.right.parent = pivot
        
        son.parent = pivot.parent
        if(pivot.parent is None):
            self.root = son
        else:
            if(pivot == pivot.parent.left):
                pivot.parent.left = son
            else:
                pivot.parent.right = son
        
        son.right = pivot
        pivot.parent = son
        
        self.set_height(pivot)
        self.set_height(son)
        
        return son
        
    def lr_rotate(self, pivot):
        ancestor = pivot.parent
        son = pivot.left
        grandson = son.right
        
        pivot.left = grandson
        if (grandson is not None):
            son.right = grandson.left
            grandson.left = son
        
        if (ancestor is None):
            self.root = grandson
        elif (pivot.data > ancestor.data):
            ancestor.left = grandson
        else:
            ancestor.right = grandson
        if (grandson is not None):
            pivot.left = grandson.right
            grandson.right = pivot   
    
    def rl_rotate(self, pivot):
        ancestor = pivot.parent
        son = pivot.right
        grandson = son.left
        
        pivot.right = grandson
        if (grandson is not None):
            son.left = grandson.right
            grandson.right = son
        
        if (ancestor is None):
            self.root = grandson
        elif (pivot.data > ancestor.data):
            ancestor.right = grandson
        else:
            ancestor.left = grandson
        if (grandson is not None):
            pivot.right = grandson.left
            grandson.left = pivot   
    
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
            print("Case 1: Pivot not detected")

        else:
            if(pivot_balance == -1):
                # Case 2: Pivot exists and adding to the shorter subtree
                if(data < pivot.data):
                    print("Case 2: A pivot exists, and a node was added to the shorter subtree") 
            
                else:
                    son = pivot.right
                    if(son is None):
                        print("Case 3: Unexpected condition: pivot.right is None")
                    
                    elif(data > son.data):
                        print("Case 3a: adding a node to an outside subtree")
                        self.left_rotate(pivot)
                        self.set_height(self.root)

                    else:
                        print("Case 3b: rl rotate")
                        self.rl_rotate(pivot)
                        self.set_height(self.root)
                        return self.root
                    
            elif(pivot_balance == 1):
                if(data > pivot.data):
                    print("Case 2: A pivot exists, and a node was added to the shorter subtree")
                
                else:
                    son = pivot.left
                    if(son is None):
                        print("Case 3: Unexpected condition: pivot.left is None")
                    
                    elif(data< son.data):
                        print("Case 3a: adding a node to an outside subtree")
                        self.right_rotate(pivot)
                        self.set_height(self.root)
                    
                    else:
                        print("Case 3b: lr rotate")
                        self.lr_rotate(pivot)
                        self.set_height(self.root)
                        return self.root
            else:
                print("Case: Unhandled pivot balance", pivot_balance)
        
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
    print("Tree Tests (Exercises 2 & 3)")
    #   Case 1
    tree.insert_data(5)
    tree.insert_data(3)

    #   Case 2
    tree.insert_data(8)
    
    #   Case 3a     
    tree.insert_data(9)
    tree.insert_data(10)    
    
    print("Tree Tests (Exercise 4)")
    
    #   Case 3b
    tree.insert_data(7)
    
    print(f"Expected = 7\nActual = {tree.root.left.right.data}\n")
    
    tree2 = AVLTree()
    
    numbers = [6, 2, 7, 1, 4]
    
    for num in numbers:
        tree2.insert_data(num)
        
    tree2.insert_data(3)
        
    print(f"Expected = 3\nActual = {tree2.root.left.right.data}\n")
    