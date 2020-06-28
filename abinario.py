class Nodo:
    def __init__(self, valor=None, left=None, right=None):
        self.valor = valor
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.valor)
        
class aBinarios:
    def __init__(self):
        self.root = None

    def Insertar(self, element):
        if self.root == None:
            self.root = element
        else:
            aux = self.root
            padre = None
            while aux != None:
                padre = aux
                if int(element.valor)>=int(aux.valor):
                    aux = aux.right
                else:
                    aux = aux.left
            if int(element.valor)>=int(padre.valor):
                padre.right = element
            else:
                padre.left = element

    def isEmpty(self):
        return (self.root == None)

    def Elimin(self, element):
        self.root = self.Eliminar(element, self.root)

    def Eliminar(self, element, node):
        if node == None:
            return node

        compare = element-node.valor

        if compare < 0:
            node.left = self.Eliminar(element, node.left)
        elif compare > 0:
            node.right = self.Eliminar(element, node.right)
        elif node.left != None and node.right != None:
            node.valor = self.BuscarMin(node.right).valor
            node.right = self.Eliminar(node.valor, node.right)
        else:
            if node.left != None:
                node = node.left
            else:
                node = node.right
        return node

    def BuscarMn(self):
        if self.isEmpty():
            return None
        else:
            return self.BuscarMin(self.root)

    def BuscarMin(self, node):
        if node == None:
            return None
        elif node.left == None:
            return node
        else:
            return self.BuscarMin(node.left)

    def BuscarMx(self):
        if self.isEmpty():
            return None
        else:
            return self.BuscarMax(self.root)

    def BuscarMax(self, node):
        if node != None:
            while node.right != None:
                node = node.right
        return node
                
    def getRoot(self):
        return self.root

    def InOrden(self, element):
        if element != None:
            self.InOrden(element.left)
            print(element)
            self.InOrden(element.right)
            
    def PreOrden(self, element):
        if element != None:
            print(element)
            self.PreOrden(element.left)
            self.PreOrden(element.right)
            
    def PostOrden(self, element):
        if element != None:
            self.PostOrden(element.left)
            self.PostOrden(element.right)
            print(element)
    
        
ab = aBinarios()
print(ab.isEmpty())
ab.Insertar(Nodo(34567))
ab.Insertar(Nodo(789))
ab.Insertar(Nodo(6))
ab.Insertar(Nodo(78900))
ab.PostOrden(ab.getRoot())
ab.PreOrden(ab.getRoot())
ab.Elimin(78900)
ab.InOrden(ab.getRoot())
print(ab.isEmpty())
