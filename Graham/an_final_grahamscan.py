# Reusable data structures and functions for the algorithms
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
          return f"{self.x},{self.y}"

def distance(p, q):
    return abs(p.x - q.x) + abs(p.y - q.y)

def cross_product(p,q,r):
    return (q.x - p.x)*(r.y - p.y) - (r.x - p.x)*(q.y - p.y)
    
class PointSymbolTable: #technically a binary tree
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    
    # in order traversal to list
    def valuesToList(self):
        return (self.left.valuesToList() if self.left else []) + [self.value] + (self.right.valuesToList() if self.right else [])
    
    # normal binary tree get
    def get(self, key): 
        if self.key == key:
            return self.value
        else:
            if self.key < key:
                return self.right.get(key)
            else:
                return self.left.get(key)

    # normal binary tree put
    def put(self, key, value, ref):
        if self.key == key:
            # always keep furthest point from reference point
            self.value = value if distance(value, ref) > distance(self.value, ref) else self.value
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
