#Define el nodo (llave y apuntador siguiente)
class Node:                         
    def __init__(self, data): 
        self.data = data
        self.num = 0
        self.expenses = 0
        self.income = 0
        self.next = None 
        
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
          
class LinkedList:

#Define apuntadores cabeza y cola    
    def __init__(self):              
        self.head = None
        self.tail = None 

#Devuelve lista enlazada        
    def isEmpty(self):               
        return self.head

#Imprime lista    
    def print(self):                
        i = self.head
        while i != None:
            print("Nombre: " + str(i.data) + " Inventario: " + str(i.num) + " Costo: " + str(i.expenses) + " Ingresos:" + str(i.income))
            i = i.next
        print()

#Elimina el objeto si este existe, falta considerar los elementos en inventario:        
    def delete(self, key):
        curr = self.head
        prev = None
        if curr.data == None:
            return
        if curr != None and curr.data == key:
            self.head = curr.next
            return self.delete(key);
        
        while curr!= self.tail and curr.next!= None:
            if curr.data != key:
                prev = curr
                curr = curr.next
            else: 
                curr = curr.next
                prev.next = curr
                return
        
        if curr == self.tail and curr == key:
            self.tail = prev
            self.tail.next = None    
        else:
            print("El elemento no existe")
    
#Busca el producto y devuelve sus atributos                 
    def search(self,key):
        curr = self.head
        while curr:
            if curr.data == key:
                print("Nombre: " + str(curr.data) + " Inventario: " + str(curr.num) + " Costo: " + str(curr.expenses) + " Ingreso: " + str(curr. income))
                return
            
#Busca el nombre como clave y modifica los atributos                  
    def buy(self,key,num, price):
        if num <= 0:
            return print("El numero de elementos no es posible")
        if price <= 0:
            return print("El precio de compra no es posible")
        curr = self.head
        if curr == None:
            return print("El elemento no existe")            
        while curr:
            if curr.data == key:
                curr.num = curr.num + num
                curr.expenses = curr.expenses + price
                return
            else:
                curr = curr.next               
        return print("la operacion no es posible")

#Busca el nombre como clave y modifica los atributos        
    def sell(self,key,num,price):
        if num <= 0:
            return print("El numero de elementos no es posible")
        if price <= 0:
            return print("El precio de compra no es posible")        
        curr = self.head
        if curr == None:
            return print("El elemento no existe")            
        while curr:
            if curr.data == key:
                if num <= curr.num:
                    curr.num = curr.num - num
                    curr.income = curr.income + price
                    return
                else:
                    return print("No hay suficientes elementos en inventario, la operacion no es posible")                    
            else:
                curr = curr.next               
        return print("la operacion no es posible")            
                
#Agrega elemento teniendo en cuenta la unicidad               
    def add(self,key):
        nodo = Node(key)
        curr = self.head        
        if curr == None:
            self.head = nodo
            self.tail = nodo
            return       
        while curr != self.tail:
            if curr.data != key:
                curr = curr.next                
            elif curr.data == key:
                print("el elemento ya existe, no se agrego")
                return       
        curr.next = nodo
        self.tail = nodo
        print("La operacion se realizo con exito")                            
        

#Switch Case para operacion
def Operation(operation, Li):
    
    if operation == 1:
        print("Inserte Nombre")
        name = input()
        Li.add(name)
                        
    elif operation == 2:
        print("Inserte Nombre")
        name = input()
        Li.delete(name) 
            
    elif operation == 3:
        print("Inserte Nombre")
        name = input()
        try:
            print("Inserte numero de elementos comprados") 
            sum = int(input())
            print("Inserte costo")
            price = int(input())
            Li.buy(name, sum, price)
        except ValueError:
            print("Error, ha ingresado una cadena de caracteres")
            
    elif operation == 4:
        print("Inserte Nombre")
        name = input()
        try:
            print("Inserte numero de elementos vendidos") 
            sum = int(input())
            print("Inserte ingreso")
            price = int(input())
            Li.sell(name, sum, price)
        except ValueError:
            print("Error, ha ingresado una cadena de caracteres")     
                        
    elif operation == 5:
        print("Inserte Nombre")
        name = input()
        Li.search(name)
            
    elif operation == 6:
        Li.print()
            
    else:
        print("Ha ingresado un valor erroneo")
    
    
            
user = True
li = LinkedList()
queue = Queue()
stack = Stack()

while user == True:
    print("1 agregar")
    print("2 eliminar")
    print("3 comprar")
    print("4 vender")   
    print("5 buscar elemento")
    print("6 mostrar elementos")
    print("Inserte operacion a realizar")
    op = input()
    try:
        op = int(op)
        Operation(op,li)      
    except:
        print("Error, no ha ingresado un numero")   
    print("Si desea realizar otra operacion, ingrese 1, para salir presione otro numero")       
    program = int(input())
    if program != 1:
        user = False
print("Programa finalizado") 