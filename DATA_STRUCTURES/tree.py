node_list = []

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.right = right
        self.left = left

class Tree:

    def __init__(self,root = None):
        self.root = root

    def insert_root(self, data):
        self.root = Node(data)

    def insert_left(self,node, data):
        node.left = Node(data)

    def insert_right(self, node, data):
        node.right = Node(data)

    def __str__(self):
        st = ""
        
        def rec_str(n):
            nonlocal st
            if n is None:
                st += "_"
            else:
                st += str(n.data)
                st += "("
                rec_str(n.left)
                st += ","
                rec_str(n.right)
                st += ")"

        rec_str(self.root)
        return st

class BinarySearchTree(Tree):
    def __init__(self, root=None):
        super().__init__(root)


    def insert(self, data):
        
        def insert_data(n,data):

            if data < n.data:

                if n.left == None:
                    self.insert_left(n, data)

                else:
                    insert_data(n.left, data)


            elif data > n.data:
                
                if n.right == None:
                    self.insert_right(n, data)
                
                else:
                    insert_data(n.right, data)
        
        
            else:
                print("Δεν γίνεται να δημιουργήσεις κόμβο με ίδια data.")
                return None

        insert_data(self.root, data)
        
    
    def __str__(self):
        st = ""
        
        def rec_str(n):
            nonlocal st
            if n is None:
                pass
            else:
                rec_str(n.left)
                st += str(n.data)
                st += ","
                rec_str(n.right)

        rec_str(self.root)
        return st
        
        

Tbin = BinarySearchTree()
Tbin.insert_root(2)
Tbin.insert(5)
Tbin.insert(8)
Tbin.insert(11)
Tbin.insert(1)
Tbin.insert(7)

print(str(Tbin))
    