from math import sqrt, pi, atan2
import timeit
import random
import matplotlib

class Stack:
    def __init__(self):
        #initialised as empty stack, infinite size
        self.__values = []
        self.__top = 0

    def isEmpty(self):
        return 0==self.__top
    
    def push(self,value):
        self.__values[self.__top] = value
        self.__top +=1

    def pop(self):
        val = self.peek()
        if val is not None:
            self.__top -= 1
        return val
    
    def peek(self):
        if not self.isEmpty():
            return self.__values[self.__top]
        return None

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def calcAngle(self,point2):
        #cos x = (a . b) / |a| |b|
        return (atan2(point2.y-self.y, point2.x-self.x) + 2*pi) % (2 * pi)
    def calcDistance(self,point2):
        return sqrt((point2.y-self.y)**2 + (point2.x-self.x)**2)

class SymbolTableTree:
    def __init__(self, key, value):
        self.__value = value
        self.__left = None
        self.__right = None
        self.__key = key
    
    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right
    
    def getKey(self):
        return self.__key
    
    def getValue(self):
        return self.__value
    
    def setLeft(self, left):
        self.__left = left
    
    def setRight(self, right):
        self.__right = right
    
    def setValue(self, value):
        self.__value = value
    
    def get(self, key):
        if self.__key == key:
            return self.__value
        elif self.__key < key:
            if self.__right is not None:
                return self.__right.get(key)
            else:
                return None
        else:
            if self.__left is not None:
                return self.__left.get(key)
            else:
                return None
    
    def put(self, key, value, ref):
        if self.__key == key:
            if value.calcDistance(ref) > self.__value.calcDistance(ref):
                self.setValue(value)
        elif self.__key < key:
            if self.__right is not None:
                self.__right.put(key, value)
            else:
                self.__right = SymbolTableTree(key, value)
        else:
            if self.__left is not None:
                self.__left.put(key, value)
            else:
                self.__left = SymbolTableTree(key, value)
     
def akn_graham_scan(listOfPoints):
    stack=Stack()
    #find point with lowest y co-ordinate - if y is the same take lowest x
    point0 = listOfPoints[0]
    for current in listOfPoints:
        if (current.y < point0.y) or ((current.y == point0.y) and (current.x < point0.x)):
            point0 = current
    
    symTable = SymbolTableTree(listOfPoints[0].calcAngle(point0),listOfPoints[0])
    #calculate angles
    for current in listOfPoints:
        symTable.put(current.calcAngle(point0),current)
"""
let points be the list of points
let stack = empty_stack()

find the lowest y-coordinate and leftmost point P0
sort points by polar angle with P0, 
if several points have the same polar angle 
then only keep the farthest

for point in points:
    # pop the last point from the stack if we turn clockwise to reach this point
    while count stack > 1 and ccw(next_to_top(stack), top(stack), point) <= 0:
        pop stack
    push point to stack
end
"""