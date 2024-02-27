import math
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
    
class Stack:
    def __init__(self):
        #initialised as empty stack, infinite size
        self.values = []
        self.top = -1

    def isEmpty(self):
        return 0==self.top
    
    def push(self,value):
        self.values.append(value)
        self.top += 1

    def pop(self):
        if self.isEmpty():
            return None
        self.top -= 1
        return self.values.pop()
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.values[self.top]
    
    def peekNext(self):
        if self.__top > 0:
            return self.values[self.top-1]
        return None
    
    def size(self):
        return self.top+1

def cross_product(p1,p2,p3):
    return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y)

def getAngle(p1,p2):
    return math.atan2(p2.y - p1.y, p2.x - p1.x)

def akn_graham_scan(listOfPoints):
    stack=Stack()

    #find point with lowest y co-ordinate - if y is the same take lowest x
    point0 = listOfPoints[0]
    for current in listOfPoints[1:]:
        if (current.y < point0.y) or ((current.y == point0.y) and (current.x < point0.x)):
            point0 = current
    
    #initialise symbol table with angle key and point value
    symTable = PointSymbolTable(getAngle(point0,listOfPoints[0]),listOfPoints[0])

    #calculate angles then sort by angle using symbol table
    for current in listOfPoints:
        if current != point0:
            symTable.put(getAngle(point0,current),current,point0)
    
    sortedPoints = [point0] + symTable.valuesToList()
    #push first two points onto stack
    stack.push(sortedPoints[0])
    stack.push(sortedPoints[1])
    for i in range(2,len(sortedPoints)):
        while stack.size() > 1 and cross_product(stack.peekNext(),stack.peek(),sortedPoints[i]) <= 0:
                #if < 0 then we are turning right so pop the last point from the stack
                stack.pop()
        stack.push(sortedPoints[i])
    return stack.values