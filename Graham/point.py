class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def calcDistance(self,point2):
        return abs(point2.x-self.x) + abs(point2.y-self.y)

class PointSymbolTable: #technically a binary tree
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    
    def valuesToList(self):#in order traversal to list
        list = []
        if self.left is not None:
            list.extend(self.left.valuesToList())
        list.append(self.value)
        if self.right is not None:
            list.extend(self.right.valuesToList())
        return list
    
    def get(self, key):#normal binary tree get 
        if self.key == key:
            return self.value
        elif self.key < key:
            if self.right is not None:
                return self.right.key
            return None
        else:
            if self.left is not None:
                return self.left.key
            return None
    
    def put(self, key, value, ref):#normal binary tree put
        if self.key == key:
            #always keep furthest point from ref
            if value.calcDistance(ref) > self.value.calcDistance(ref):
                self.value = value
        elif self.key < key:
            if self.right is not None:
                self.right.put(key, value, ref)
            else:
                self.right = PointSymbolTable(key, value)
        else:
            if self.left is not None:
                self.left.put(key, value, ref)
            else:
                self.left = PointSymbolTable(key, value)