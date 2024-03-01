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
        return (self.left.valuesToList() if self.left else []) + [self.value] + (self.right.valuesToList() if self.right else [])
    
    def get(self, key):#normal binary tree get 
        return self.value if self.key == key else (self.right.get(key) if self.key < key else self.left.get(key))
    
    def put(self, key, value, ref):#normal binary tree put
        if self.key == key:
            #always keep furthest point from ref
            self.value = value if value.calcDistance(ref) > self.value.calcDistance(ref) else self.value
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
    
def cross_product(p1,p2,p3):
    return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y)

def sort_key(start,p1): #sort by -1/tan (angle)
    if p1.y == start.y:
        return float('inf') if p1.x - start.x < 0 else float('-inf')
    return - (p1.x - start.x) / (p1.y - start.y)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

def akn_graham_scan(listOfPoints):
    stack=[]
    #find point with lowest y co-ordinate - if y is the same take lowest x
    point0 = listOfPoints[0]
    for current in listOfPoints[1:]:
        if (current.y < point0.y) or ((current.y == point0.y) and (current.x < point0.x)):
            point0 = current
    #initialise symbol table with angle key and point value
    symTable = PointSymbolTable(sort_key(point0,listOfPoints[0]),listOfPoints[0])

    #calculate angles then sort by angle using symbol table
    for current in listOfPoints:
        if current != point0:
            symTable.put(sort_key(point0,current),current,point0)
    
    sortedPoints = [point0] + symTable.valuesToList()
    #push first two points onto stack
    stack.append(sortedPoints[0])
    stack.append(sortedPoints[1])
    for i in range(2,len(sortedPoints)):
        while len(stack) > 1 and cross_product(stack[-2],stack[-1],sortedPoints[i]) <= 0:
                #if < 0 then we are turning right so pop the last point from the stack - anticlockwise search
                stack.pop()
        stack.append(sortedPoints[i])
    return stack