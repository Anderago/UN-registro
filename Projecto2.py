class Node:                         
    def __init__(self, data): 
        self.data = data
        self.next = None

class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.num = 0
        self.expenses = 0
        self.incomes = 0
        self.left = None
        self.right = None
        self.height = 1

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop() 
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head    
        
    def enqueue(self, key):
        nodo = Node(key)
        if not self.isEmpty():
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.next = nodo                
            self.tail = nodo
            
    def dequeue(self):
        curr = self.head
        curr = curr.next
        self.head = curr  

class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, data):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(data)
        elif data < root.data:
            root.left = self.insert_node(root.left, data)
        elif data > root.data:
            root.right = self.insert_node(root.right, data)
        else:
            return print("Un articulo tiene el mismo nombre")    

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if data < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if data > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root
    
# Function to delete a node
    def delete_node(self, root, data):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    
    def buy(self,root,data,num,price):
        self.find(root,data)
        if num <= 0:
            return print("El numero de elementos no es posible")
        if price <= 0:
            return print("El precio de compra no es posible")
        root.num = root.num + num
        root.expenses = root.expenses + price     
        
        
    def sell(self,root,data,num,price):    
        self.find(root,data)
        if num <= 0:
            return print("El numero de elementos no es posible")
        if price <= 0:
            return print("El precio de venta no es posible")
        root.num = root.num - num
        root.incomes = root.incomes + price                 
        
        
    def search(self,root,data):
        self.find(root, data)    
        print("Nombre: " + str(root.data) + " Inventario: " + str(root.num) +
                " Costo: " + str(root.expenses) + " Ingreso: " + str(root. incomes) + 
                " Beneficios: " + str(root.incomes-root.expenses))  
        
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        print("Nombre: " + str(root.data) + " Inventario: " + str(root.num) + 
              " Costo: " + str(root.expenses) + " Ingresos:" + str(root.incomes) 
              + " Beneficios: " + str(root.incomes-root.expenses))
        self.inOrder(root.right)        
    
    def find(self,root,data):
        if not root:
            return print("El elemento no existe")
        elif data < root.data:
            root.left = self.insert_node(root.left, data)
        elif data > root.data:
            root.right = self.insert_node(root.right, data)
        else:
            return root 
            

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factor of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)


tree = AVLTree()
queue = Queue()
stack = Stack()
root = None
user = True

while user == True:
    print("1 agregar elemento")
    print("2 eliminar elemento")
    print("3 comprar unidades")
    print("4 vender unidades")   
    print("5 buscar elemento")
    print("6 mostrar elementos")
    print("Inserte operacion a realizar")
    op = input()
    if op.isnumeric() == True:
        op = int(op)
        
        if op == 1:
            print("Inserte Nombre")
            name = input()
            root = tree.insert_node(root, name)              
                        
        elif op == 2:
            print("Inserte Nombre")
            name = input()
            root = tree.delete_node(root, name)
            
        elif op == 3:
            print("Inserte Nombre")
            name = input()
            try:
                print("Inserte numero de elementos comprados") 
                sum = int(input())
                print("Inserte costo")
                price = int(input())
                tree.buy(root, name, sum, price)
            except ValueError:
                print("Error, ha ingresado una cadena de caracteres")
            
        elif op == 4:
            print("Inserte Nombre")
            name = input()
            try:
                print("Inserte numero de elementos vendidos") 
                sum = int(input())
                print("Inserte ingreso")
                price = int(input())
                tree.sell(root, name, sum, price)
            except ValueError:
                print("Error, ha ingresado una cadena de caracteres")                      
                
        elif op == 5:
            print("Inserte Nombre")
            name = input()
            tree.search(root, name)        
                
        elif op == 6:
            tree.inOrder(root)                
        else:
            print("Ha ingresado un valor erroneo")
    else:          
        print("Error, no ha ingresado un numero")     
    print("Si desea realizar otra operacion, ingrese 1, para salir ingrese otro valor")       
    program = input()
    if program != 1:
        user = False
print("Programa finalizado")  